const API_BASE = "http://127.0.0.1:8000";
const CROP_PADDING_CSS_PX = 10;
const MIN_OCR_IMAGE_EDGE = 900;
const MAX_OCR_IMAGE_EDGE = 2200;

chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "jp-photo-reader-image",
    title: "Recognize Japanese in image",
    contexts: ["image"]
  });
});

chrome.contextMenus.onClicked.addListener(async (info, tab) => {
  if (info.menuItemId !== "jp-photo-reader-image" || !tab?.id || !info.srcUrl) return;
  await ensureContentScript(tab.id);
  await analyzeImageUrl(tab.id, info.srcUrl);
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  void handleMessage(message, sender).then(sendResponse);
  return true;
});

async function handleMessage(message, sender) {
  if (message?.type === "START_SELECTION") {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (!tab?.id) return { ok: false, error: "No active tab" };
    await ensureContentScript(tab.id);
    await chrome.tabs.sendMessage(tab.id, { type: "JPR_START_SELECTION" });
    return { ok: true };
  }

  if (message?.type === "CAPTURE_SELECTION") {
    const tabId = sender.tab?.id;
    const windowId = sender.tab?.windowId;
    if (!tabId || !windowId) return { ok: false, error: "No sender tab" };
    try {
      await chrome.tabs.sendMessage(tabId, { type: "JPR_SET_BUSY", busy: true });
      const dataUrl = await chrome.tabs.captureVisibleTab(windowId, { format: "png" });
      const cropped = await cropDataUrl(dataUrl, message.rect, message.devicePixelRatio || 1);
      const result = await analyzeDataUrl(cropped);
      await chrome.tabs.sendMessage(tabId, { type: "JPR_SHOW_RESULT", result });
      return { ok: true };
    } catch (error) {
      await chrome.tabs.sendMessage(tabId, { type: "JPR_SHOW_ERROR", error: error.message });
      return { ok: false, error: error.message };
    }
  }

  if (message?.type === "ANALYZE_TEXT") {
    const result = await postJson(API_BASE + "/analyze-text", {
      text: message.text,
      grammar_question: ""
    });
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (tab?.id) {
      await ensureContentScript(tab.id);
      await chrome.tabs.sendMessage(tab.id, { type: "JPR_SHOW_RESULT", result });
    }
    return { ok: true, result };
  }

  if (message?.type === "ANSWER_GRAMMAR_QUESTION") {
    const grammarQuestion = String(message.grammarQuestion || "").trim();
    if (!grammarQuestion) return { ok: false, error: "Enter a grammar question first." };
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (!tab?.id) return { ok: false, error: "No active tab" };
    await ensureContentScript(tab.id);
    const current = await chrome.tabs.sendMessage(tab.id, { type: "JPR_GET_CURRENT_RESULT" });
    const text = String(current?.result?.text || "").trim();
    if (!text) return { ok: false, error: "Analyze image or text first, then ask a grammar question." };
    const result = await postJson(API_BASE + "/answer-grammar-question", {
      text,
      grammar_question: grammarQuestion
    });
    await chrome.tabs.sendMessage(tab.id, { type: "JPR_UPDATE_GRAMMAR_ANSWER", result });
    return { ok: true, result };
  }

  if (message?.type === "GET_ACTIVE_SELECTION_TEXT") {
    const text = await getActiveSelectionText();
    return { ok: true, text };
  }

  if (message?.type === "LOOKUP_ACTIVE_SELECTION") {
    const text = String(message.text || "").trim() || await getActiveSelectionText();
    if (!text) return { ok: false, error: "No highlighted text" };
    const result = await postJson(`${API_BASE}/lookup-text`, { text });
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (tab?.id) {
      await ensureContentScript(tab.id);
      await chrome.tabs.sendMessage(tab.id, { type: "JPR_SHOW_LOOKUP_RESULT", result });
    }
    return { ok: true, result };
  }

  if (message?.type === "OPEN_GOOGLE_SEARCH") {
    const text = String(message.text || "").trim() || await getActiveSelectionText();
    if (!text) return { ok: false, error: "No highlighted text" };
    await openGoogleSearch(text);
    return { ok: true };
  }

  if (message?.type === "LOOKUP_TEXT") {
    const result = await postJson(`${API_BASE}/lookup-text`, { text: message.text });
    return { ok: true, result };
  }

  return { ok: false, error: "Unknown message" };
}

async function analyzeImageUrl(tabId, srcUrl) {
  try {
    await chrome.tabs.sendMessage(tabId, { type: "JPR_SET_BUSY", busy: true });
    const response = await fetch(srcUrl);
    if (!response.ok) throw new Error(`Could not fetch image: ${response.status}`);
    const blob = await response.blob();
    const dataUrl = await blobToDataUrl(blob);
    const result = await analyzeDataUrl(dataUrl);
    await chrome.tabs.sendMessage(tabId, { type: "JPR_SHOW_RESULT", result });
  } catch (error) {
    await chrome.tabs.sendMessage(tabId, { type: "JPR_SHOW_ERROR", error: error.message });
  }
}

async function analyzeDataUrl(dataUrl) {
  return postJson(API_BASE + "/analyze-image", {
    image: dataUrl,
    explain_grammar: true,
    grammar_question: ""
  });
}

async function getActiveSelectionText() {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (!tab?.id) return "";
  const [injection] = await chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: () => String(window.getSelection()?.toString() || "").trim()
  });
  return String(injection?.result || "").trim();
}

async function openGoogleSearch(text) {
  const url = "https://www.google.com/search?q=" + encodeURIComponent(text);
  await chrome.tabs.create({ url });
}

async function postJson(url, body) {
  const response = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  if (!response.ok) {
    const text = await response.text();
    throw new Error(`Backend error ${response.status}: ${text}`);
  }
  return response.json();
}

async function cropDataUrl(dataUrl, rect, devicePixelRatio) {
  const blob = await (await fetch(dataUrl)).blob();
  const bitmap = await createImageBitmap(blob);
  const rawSx = Math.round(rect.left * devicePixelRatio);
  const rawSy = Math.round(rect.top * devicePixelRatio);
  const rawSw = Math.max(1, Math.round(rect.width * devicePixelRatio));
  const rawSh = Math.max(1, Math.round(rect.height * devicePixelRatio));
  const padding = Math.round(CROP_PADDING_CSS_PX * devicePixelRatio);

  const sx = Math.max(0, rawSx - padding);
  const sy = Math.max(0, rawSy - padding);
  const endX = Math.min(bitmap.width, rawSx + rawSw + padding);
  const endY = Math.min(bitmap.height, rawSy + rawSh + padding);
  const sw = Math.max(1, endX - sx);
  const sh = Math.max(1, endY - sy);

  const largestEdge = Math.max(sw, sh);
  const upScale = Math.max(1, Math.ceil(MIN_OCR_IMAGE_EDGE / largestEdge));
  const scale = Math.min(upScale, MAX_OCR_IMAGE_EDGE / largestEdge);
  const targetWidth = Math.max(1, Math.round(sw * scale));
  const targetHeight = Math.max(1, Math.round(sh * scale));

  const canvas = new OffscreenCanvas(targetWidth, targetHeight);
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "#ffffff";
  ctx.fillRect(0, 0, targetWidth, targetHeight);
  ctx.imageSmoothingEnabled = true;
  ctx.imageSmoothingQuality = "high";
  ctx.filter = "contrast(1.18) saturate(0.9)";
  ctx.drawImage(bitmap, sx, sy, sw, sh, 0, 0, targetWidth, targetHeight);
  const croppedBlob = await canvas.convertToBlob({ type: "image/png" });
  return blobToDataUrl(croppedBlob);
}

function blobToDataUrl(blob) {
  return blob.arrayBuffer().then((buffer) => {
    const bytes = new Uint8Array(buffer);
    let binary = "";
    for (let index = 0; index < bytes.length; index += 1) {
      binary += String.fromCharCode(bytes[index]);
    }
    return "data:" + (blob.type || "application/octet-stream") + ";base64," + btoa(binary);
  });
}

async function ensureContentScript(tabId) {
  try {
    await chrome.tabs.sendMessage(tabId, { type: "JPR_PING" });
  } catch {
    await chrome.scripting.insertCSS({ target: { tabId }, files: ["content.css"] });
    await chrome.scripting.executeScript({ target: { tabId }, files: ["content.js"] });
  }
}
