const statusEl = document.querySelector("#status");
const grammarQuestionEl = document.querySelector("#grammar-question");
const analyzeTextButton = document.querySelector("#analyze-text");
const highlightSection = document.querySelector("#highlight-section");
const highlightedTextEl = document.querySelector("#highlighted-text");
const lookupHighlightButton = document.querySelector("#lookup-highlight");
const googleHighlightButton = document.querySelector("#google-highlight");

let highlightedText = "";

chrome.storage.local.get({ grammarQuestion: "" }, ({ grammarQuestion }) => {
  grammarQuestionEl.value = grammarQuestion;
});

loadHighlightedText();

grammarQuestionEl.addEventListener("input", async () => {
  await chrome.storage.local.set({ grammarQuestion: grammarQuestionEl.value.trim() });
});

grammarQuestionEl.addEventListener("keydown", (event) => {
  if (event.key !== "Enter" || event.shiftKey || event.ctrlKey || event.metaKey || event.altKey) return;
  event.preventDefault();
  void answerGrammarQuestion();
});

document.querySelector("#select-area").addEventListener("click", async () => {
  statusEl.textContent = "Starting selection...";
  const response = await chrome.runtime.sendMessage({ type: "START_SELECTION" });
  if (!response?.ok) {
    statusEl.textContent = response?.error || "Could not start selection";
    return;
  }
  window.close();
});

lookupHighlightButton.addEventListener("click", async () => {
  if (!highlightedText) return;
  statusEl.textContent = "Looking up highlighted text...";
  try {
    const response = await chrome.runtime.sendMessage({ type: "LOOKUP_ACTIVE_SELECTION", text: highlightedText });
    if (!response?.ok) throw new Error(response?.error || "Lookup failed");
    window.close();
  } catch (error) {
    statusEl.textContent = error.message;
  }
});

googleHighlightButton.addEventListener("click", async () => {
  if (!highlightedText) return;
  statusEl.textContent = "Opening Google...";
  try {
    const response = await chrome.runtime.sendMessage({ type: "OPEN_GOOGLE_SEARCH", text: highlightedText });
    if (!response?.ok) throw new Error(response?.error || "Could not open Google");
    window.close();
  } catch (error) {
    statusEl.textContent = error.message;
  }
});

analyzeTextButton.addEventListener("click", async () => {
  const textInput = document.querySelector("#text-input").value.trim();
  if (!textInput) {
    statusEl.textContent = "Enter text to analyze.";
    return;
  }

  statusEl.textContent = "Analyzing...";
  try {
    const response = await chrome.runtime.sendMessage({ type: "ANALYZE_TEXT", text: textInput });
    if (!response?.ok) throw new Error(response?.error || "Analysis failed");
    window.close();
  } catch (error) {
    statusEl.textContent = error.message;
  }
});

async function answerGrammarQuestion() {
  const grammarQuestion = grammarQuestionEl.value.trim();
  if (!grammarQuestion) {
    statusEl.textContent = "Enter a grammar question first.";
    return;
  }

  statusEl.textContent = "Answering grammar question...";
  try {
    const response = await chrome.runtime.sendMessage({ type: "ANSWER_GRAMMAR_QUESTION", grammarQuestion });
    if (!response?.ok) throw new Error(response?.error || "Question failed");
    window.close();
  } catch (error) {
    statusEl.textContent = error.message;
  }
}

async function loadHighlightedText() {
  try {
    const response = await chrome.runtime.sendMessage({ type: "GET_ACTIVE_SELECTION_TEXT" });
    highlightedText = response?.text || "";
    if (!highlightedText) return;
    highlightedTextEl.textContent = highlightedText;
    highlightSection.hidden = false;
  } catch {
    highlightedText = "";
  }
}
