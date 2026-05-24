(() => {
  if (window.__jpPhotoReaderLoaded) return;
  window.__jpPhotoReaderLoaded = true;

  let overlay = null;
  let selection = null;
  let start = null;
  let panel = null;
  let currentResult = null;

  chrome.runtime.onMessage.addListener((message, _sender, sendResponse) => {
    if (message?.type === "JPR_PING") {
      sendResponse({ ok: true });
      return;
    }
    if (message?.type === "JPR_START_SELECTION") {
      startSelection();
      sendResponse({ ok: true });
      return;
    }
    if (message?.type === "JPR_SET_BUSY") {
      showBusy();
      sendResponse({ ok: true });
      return;
    }
    if (message?.type === "JPR_SHOW_RESULT") {
      showResult(message.result);
      sendResponse({ ok: true });
      return;
    }
    if (message?.type === "JPR_GET_CURRENT_RESULT") {
      sendResponse({ ok: true, result: currentResult });
      return;
    }
    if (message?.type === "JPR_UPDATE_GRAMMAR_ANSWER") {
      updateGrammarQuestionAnswer(message.result || {});
      sendResponse({ ok: true });
      return;
    }
    if (message?.type === "JPR_SHOW_LOOKUP_RESULT") {
      showLookupResult(message.result);
      sendResponse({ ok: true });
      return;
    }
    if (message?.type === "JPR_SHOW_ERROR") {
      showError(message.error);
      sendResponse({ ok: true });
    }
  });

  function startSelection() {
    removeOverlay();
    overlay = document.createElement("div");
    overlay.className = "jpr-overlay";
    overlay.innerHTML = '<div class="jpr-hint">Drag over full vertical Japanese columns</div>';
    document.documentElement.appendChild(overlay);

    overlay.addEventListener("mousedown", onMouseDown);
    overlay.addEventListener("mousemove", onMouseMove);
    overlay.addEventListener("mouseup", onMouseUp);
    overlay.addEventListener("keydown", onKeyDown);
    overlay.tabIndex = 0;
    overlay.focus();
  }

  function onMouseDown(event) {
    start = { x: event.clientX, y: event.clientY };
    selection = document.createElement("div");
    selection.className = "jpr-selection";
    overlay.appendChild(selection);
    updateSelection(event.clientX, event.clientY);
  }

  function onMouseMove(event) {
    if (!start || !selection) return;
    updateSelection(event.clientX, event.clientY);
  }

  function onMouseUp(event) {
    if (!start || !selection) return;
    updateSelection(event.clientX, event.clientY);
    const rect = selection.getBoundingClientRect();
    removeOverlay();
    if (rect.width < 8 || rect.height < 8) return;
    chrome.runtime.sendMessage({
      type: "CAPTURE_SELECTION",
      rect: {
        left: rect.left,
        top: rect.top,
        width: rect.width,
        height: rect.height
      },
      devicePixelRatio: window.devicePixelRatio || 1
    });
  }

  function onKeyDown(event) {
    if (event.key === "Escape") removeOverlay();
  }

  function updateSelection(x, y) {
    const left = Math.min(start.x, x);
    const top = Math.min(start.y, y);
    const width = Math.abs(start.x - x);
    const height = Math.abs(start.y - y);
    Object.assign(selection.style, {
      left: `${left}px`,
      top: `${top}px`,
      width: `${width}px`,
      height: `${height}px`
    });
  }

  function removeOverlay() {
    overlay?.remove();
    overlay = null;
    selection = null;
    start = null;
  }

  function ensurePanel() {
    if (panel) return panel;
    panel = document.createElement("aside");
    panel.className = "jpr-panel";
    document.documentElement.appendChild(panel);
    return panel;
  }

  function showBusy() {
    ensurePanel().innerHTML = `
      <div class="jpr-panel-header">
        <strong>Japanese Photo Reader</strong>
        <button class="jpr-close" type="button">x</button>
      </div>
      <div class="jpr-body"><div class="jpr-muted">Analyzing with local backend...</div></div>
    `;
    panel.querySelector(".jpr-close").addEventListener("click", closePanel);
  }

  function showError(error) {
    ensurePanel().innerHTML = `
      <div class="jpr-panel-header">
        <strong>Japanese Photo Reader</strong>
        <button class="jpr-close" type="button">x</button>
      </div>
      <div class="jpr-body"><div class="jpr-error">${escapeHtml(error)}</div></div>
    `;
    panel.querySelector(".jpr-close").addEventListener("click", closePanel);
  }

  function showResult(result) {
    currentResult = result || {};
    const structure = result.sentence_structure || [];
    const grammarAnalysis = result.grammar_analysis || result.grammar || "";
    const grammarQuestion = result.grammar_question || "";
    const grammarAnswer = result.grammar_answer || "";
    ensurePanel().innerHTML = `
      <div class="jpr-panel-header">
        <strong>Japanese Photo Reader</strong>
        <button class="jpr-close" type="button">x</button>
      </div>
      <div class="jpr-body">
        <section>
          <h2>Recognized Text</h2>
          <pre class="jpr-text">${escapeHtml(result.text || "")}</pre>
        </section>
        <section>
          <h2>Selection</h2>
          <div class="jpr-selection-result jpr-muted">Highlight text above to analyze the selection.</div>
        </section>
        <section>
          <h2>Structure</h2>
          ${structure.length ? structure.map(renderStructureItem).join("") : '<div class="jpr-muted">No structure parsed.</div>'}
        </section>
        <section>
          <h2>Grammar Analysis</h2>
          ${renderGrammarAnalysis(grammarAnalysis)}
        </section>
        ${renderGrammarQuestionAnswer(grammarQuestion, grammarAnswer)}
      </div>
    `;
    panel.querySelector(".jpr-close").addEventListener("click", closePanel);
    panel.querySelector(".jpr-text")?.addEventListener("mouseup", onRecognizedTextSelection);
    panel.querySelector(".jpr-text")?.addEventListener("keyup", onRecognizedTextSelection);
  }

  function showLookupResult(result) {
    currentResult = null;
    ensurePanel().innerHTML = `
      <div class="jpr-panel-header">
        <strong>Japanese Photo Reader</strong>
        <button class="jpr-close" type="button">x</button>
      </div>
      <div class="jpr-body">
        <section>
          <h2>Highlighted Text</h2>
          ${renderSelectedTextLookup(result.text || "", result)}
        </section>
      </div>
    `;
    panel.querySelector(".jpr-close").addEventListener("click", closePanel);
  }

  async function onRecognizedTextSelection() {
    const selectedText = String(window.getSelection()?.toString() || "").trim();
    const selectionResult = panel?.querySelector(".jpr-selection-result");
    if (!selectionResult || !selectedText) return;

    selectionResult.classList.add("jpr-muted");
    selectionResult.innerHTML = "Looking up selection...";
    try {
      const response = await chrome.runtime.sendMessage({ type: "LOOKUP_TEXT", text: selectedText });
      if (!response?.ok) throw new Error(response?.error || "Selection lookup failed");
      selectionResult.classList.remove("jpr-muted");
      selectionResult.innerHTML = renderSelectedTextLookup(selectedText, response.result || {});
    } catch (error) {
      selectionResult.classList.remove("jpr-muted");
      selectionResult.innerHTML = `<div class="jpr-error">${escapeHtml(error.message)}</div>`;
    }
  }

  function updateGrammarQuestionAnswer(result) {
    if (!currentResult) return;
    currentResult = {
      ...currentResult,
      grammar_question: result.grammar_question || "",
      grammar_answer: result.grammar_answer || ""
    };
    const body = panel?.querySelector(".jpr-body");
    if (!body) return;
    const existing = body.querySelector(".jpr-grammar-question-answer");
    const html = renderGrammarQuestionAnswer(currentResult.grammar_question, currentResult.grammar_answer);
    if (existing) {
      if (html) {
        existing.outerHTML = html;
      } else {
        existing.remove();
      }
    } else if (html) {
      body.insertAdjacentHTML("beforeend", html);
    }
  }

  function renderSelectedTextLookup(selectedText, result) {
    const entries = result.dictionary || [];
    return `
      <div class="jpr-selected-text"><strong>${escapeHtml(selectedText)}</strong></div>
      <div class="jpr-actions">
        <a class="jpr-button-link" href="${googleSearchUrl(selectedText)}" target="_blank" rel="noopener noreferrer">Search Google</a>
      </div>
      <h3>Dictionary</h3>
      ${entries.length ? entries.map(renderDictionaryEntry).join("") : '<div class="jpr-muted">No dictionary entries found.</div>'}
    `;
  }

  function closePanel() {
    panel?.remove();
    panel = null;
    currentResult = null;
  }

  function renderDictionaryEntry(entry) {
    const glosses = (entry.glosses || []).slice(0, 4).map(escapeHtml).join("; ");
    return `
      <div class="jpr-entry">
        <div><strong>${escapeHtml(entry.expression)}</strong> <span>${escapeHtml(entry.reading || "")}</span></div>
        <div>${glosses}</div>
        <small>${escapeHtml(entry.source || "")}</small>
      </div>
    `;
  }

  function renderGrammarAnalysis(grammar) {
    if (Array.isArray(grammar)) {
      const text = grammar
        .map((item) => item.analysis || item.explanation || item.meaning || "")
        .filter(Boolean)
        .join("\n\n");
      return text ? renderGrammarText(text) : '<div class="jpr-muted">No grammar analysis returned.</div>';
    }
    return grammar ? renderGrammarText(grammar) : '<div class="jpr-muted">No grammar analysis returned.</div>';
  }

  function renderGrammarText(text) {
    return '<div class="jpr-entry"><div>' + escapeHtml(text) + '</div></div>';
  }

  function renderGrammarQuestionAnswer(question, answer, headingTag = "h2") {
    if (!question && !answer) return "";
    const heading = headingTag === "h3" ? "h3" : "h2";
    const questionHtml = question ? "<div class=\"jpr-muted\">Question: " + escapeHtml(question) + "</div>" : "";
    return "<section class=\"jpr-grammar-question-answer\"><" + heading + ">Grammar Question Answer</" + heading + ">" + questionHtml + renderGrammarAnalysis(answer) + "</section>";
  }

  function renderStructureItem(item) {
    const reading = item.reading ? ` <span>${escapeHtml(item.reading)}</span>` : "";
    const lemma = item.lemma && item.lemma !== item.surface ? `<div>${escapeHtml(item.lemma)}</div>` : "";
    const tokenId = item.token_id ? `<span class="jpr-token-id">#${escapeHtml(item.token_id)}</span> ` : "";
    return `
      <div class="jpr-entry">
        <div>${tokenId}<strong>${escapeHtml(item.surface)}</strong>${reading}</div>
        ${lemma}
        <small>${escapeHtml(item.role || "unknown")}${item.pos ? ` · ${escapeHtml(item.pos)}` : ""}</small>
        ${renderTokenDictionary(item.dictionary || [])}
      </div>
    `;
  }

  function renderTokenDictionary(entries) {
    if (!entries.length) return `<div class="jpr-token-dictionary jpr-muted">No dictionary entry.</div>`;
    return `
      <div class="jpr-token-dictionary">
        ${entries.slice(0, 3).map(renderTokenDictionaryEntry).join("")}
      </div>
    `;
  }

  function renderTokenDictionaryEntry(entry) {
    const glosses = (entry.glosses || []).slice(0, 3).map(escapeHtml).join("; ");
    const reading = entry.reading ? ` <span>${escapeHtml(entry.reading)}</span>` : "";
    return `
      <div class="jpr-token-dictionary-entry">
        <strong>${escapeHtml(entry.expression || entry.query || "")}</strong>${reading}
        <div>${glosses}</div>
      </div>
    `;
  }

  function googleSearchUrl(text) {
    return "https://www.google.com/search?q=" + encodeURIComponent(text);
  }

  function escapeHtml(value) {
    return String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }
})();
