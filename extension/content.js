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
    if (message?.type === "JPR_UPDATE_GRAMMAR_ANALYSIS") {
      if (currentResult) currentResult.grammar_analysis = message.result?.grammar_analysis;
      const container = panel?.querySelector("#jpr-grammar-analysis-container");
      if (container) container.innerHTML = renderGrammarAnalysis(message.result?.grammar_analysis || "");
      sendResponse({ ok: true });
      return;
    }
    if (message?.type === "JPR_UPDATE_SENTENCE_ANALYSIS") {
      if (currentResult) currentResult.sentence_analysis = message.result?.sentence_analysis;
      const container = panel?.querySelector("#jpr-sentence-analysis-container");
      if (container) container.innerHTML = renderSentenceAnalysis(message.result?.sentence_analysis, currentResult?.sentence_structure || []);
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
    panel.addEventListener("click", onPanelClick);
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
    const sentenceAnalysis = result.sentence_analysis || null;
    const grammarMatches = result.grammar_matches || [];
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
          <h2>Sentence Analysis</h2>
          <div id="jpr-sentence-analysis-container">
            ${sentenceAnalysis ? renderSentenceAnalysis(sentenceAnalysis, structure) : '<div class="jpr-muted">Generating sentence tree (think mode)... This may take a moment.</div>'}
          </div>
        </section>
        <section>
          <h2>Matched Grammar</h2>
          ${renderGrammarMatches(grammarMatches, result.grammar_reference_attribution || "")}
        </section>
        <section>
          <h2>Grammar Analysis</h2>
          <div id="jpr-grammar-analysis-container">
            ${grammarAnalysis ? renderGrammarAnalysis(grammarAnalysis) : '<div class="jpr-muted">Generating grammar analysis (think mode)... This may take a moment.</div>'}
          </div>
        </section>
        ${renderGrammarQuestionAnswer(grammarQuestion, grammarAnswer)}
      </div>
    `;
    panel.querySelector(".jpr-close").addEventListener("click", closePanel);
    panel.querySelector(".jpr-text")?.addEventListener("mouseup", onRecognizedTextSelection);
    panel.querySelector(".jpr-text")?.addEventListener("keyup", onRecognizedTextSelection);

    if (!sentenceAnalysis && result.text) {
      chrome.runtime.sendMessage({ type: "FETCH_SENTENCE_ANALYSIS", text: result.text });
    }
    if (!grammarAnalysis && result.text) {
      chrome.runtime.sendMessage({ type: "FETCH_GRAMMAR_ANALYSIS", text: result.text });
    }
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

  function onPanelClick(event) {
    const grammarButton = event.target.closest(".jpr-open-grammar");
    if (grammarButton) {
      void showGrammarMarkdownDetail(grammarButton.dataset.markdownFile || "");
      return;
    }

    const button = event.target.closest(".jpr-pronounce");
    if (!button) return;
    const text = button.dataset.pronounce || "";
    if (text) pronounceJapanese(text);
  }

  function pronounceJapanese(text) {
    if (!window.speechSynthesis || !window.SpeechSynthesisUtterance) return;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "ja-JP";
    utterance.rate = 0.85;
    window.speechSynthesis.speak(utterance);
  }


  async function showGrammarMarkdownDetail(markdownFile) {
    const body = panel?.querySelector(".jpr-body");
    if (!body || !markdownFile) return;
    let detail = body.querySelector(".jpr-grammar-detail");
    if (!detail) {
      detail = document.createElement("section");
      detail.className = "jpr-grammar-detail";
      const grammarSection = body.querySelector(".jpr-grammar-matches")?.closest("section");
      if (grammarSection) {
        grammarSection.insertAdjacentElement("afterend", detail);
      } else {
        body.appendChild(detail);
      }
    }
    detail.innerHTML = "<h2>Grammar Reference</h2><div class=\"jpr-muted\">Loading grammar reference...</div>";
    try {
      const response = await chrome.runtime.sendMessage({ type: "GET_GRAMMAR_MARKDOWN", markdownFile });
      if (!response?.ok) throw new Error(response?.error || "Grammar reference lookup failed");
      detail.innerHTML = renderGrammarMarkdown(response.result || {});
      detail.scrollIntoView({ block: "nearest" });
    } catch (error) {
      detail.innerHTML = "<h2>Grammar Reference</h2><div class=\"jpr-error\">" + escapeHtml(error.message) + "</div>";
    }
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


  function renderSentenceAnalysis(analysis, structure) {
    const tree = analysis?.tree;
    if (!tree) return "<div class=\"jpr-muted\">No sentence analysis returned.</div>";
    const summary = analysis.summary ? "<div class=\"jpr-analysis-summary\">" + escapeHtml(analysis.summary) + "</div>" : "";
    return "<div class=\"jpr-sentence-analysis\">" + summary + renderAnalysisNode(tree, 0, structure || []) + "</div>";
  }

  function renderAnalysisNode(node, depth, structure) {
    const children = Array.isArray(node.children) ? node.children : [];
    const label = node.type || node.role || "phrase";
    const value = String(node.value || "");
    const translation = node.translation ? "<div class=\"jpr-analysis-translation\">" + escapeHtml(node.translation) + "</div>" : "";
    const role = node.role && node.role !== label ? "<span class=\"jpr-analysis-role\">" + escapeHtml(node.role) + "</span>" : "";
    const dictionaryEntries = depth > 0 ? dictionaryEntriesForAnalysisNode(value, structure) : [];
    const audioButton = value ? "<button class=\"jpr-pronounce jpr-analysis-audio\" type=\"button\" title=\"Pronounce\" aria-label=\"Pronounce " + escapeHtml(value) + "\" data-pronounce=\"" + escapeHtml(value) + "\">🔊</button>" : "";
    return "<div class=\"jpr-analysis-node jpr-analysis-depth-" + Math.min(depth, 4) + "\">" +
      "<div class=\"jpr-analysis-node-head\">" +
      "<span class=\"jpr-analysis-label\">" + escapeHtml(label) + "</span>" + role + audioButton +
      "</div>" +
      "<div class=\"jpr-analysis-value\">" + escapeHtml(value) + "</div>" +
      translation +
      (dictionaryEntries.length ? renderTokenDictionary(dictionaryEntries) : "") +
      (children.length ? "<div class=\"jpr-analysis-children\">" + children.map((child) => renderAnalysisNode(child, depth + 1, structure)).join("") + "</div>" : "") +
      "</div>";
  }

  function dictionaryEntriesForAnalysisNode(value, structure) {
    if (!value || !Array.isArray(structure)) return [];
    const normalizedValue = normalizeJapaneseForMatch(value);
    if (!normalizedValue) return [];
    const entries = [];
    const seen = new Set();
    for (const item of structure) {
      const surface = String(item.surface || "");
      if (!surface) continue;
      const normalizedSurface = normalizeJapaneseForMatch(surface);
      if (normalizedValue !== normalizedSurface && !normalizedValue.includes(normalizedSurface)) continue;
      for (const entry of item.dictionary || []) {
        const key = [entry.expression || entry.query || "", entry.reading || "", (entry.glosses || []).join("|")].join("::");
        if (seen.has(key)) continue;
        seen.add(key);
        entries.push(entry);
      }
    }
    return entries;
  }

  function normalizeJapaneseForMatch(value) {
    return String(value || "").replace(/[\s\u3000、。,.!?！？\-ー]/g, "");
  }


  function renderGrammarMatches(matches, attribution) {
    if (!Array.isArray(matches) || !matches.length) return "<div class=\"jpr-muted\">No grammar reference matches found.</div>";
    const attributionHtml = attribution ? "<div class=\"jpr-attribution\">" + escapeHtml(attribution) + "</div>" : "";
    return "<div class=\"jpr-grammar-matches\">" + matches.map(renderGrammarMatch).join("") + attributionHtml + "</div>";
  }

  function renderGrammarMatch(match) {
    const confidence = typeof match.confidence === "number" ? Math.round(match.confidence * 100) + "%" : "";
    const markers = (match.matched_markers || []).map((item) => item.marker).filter(Boolean).join(" / ");
    const examples = Array.isArray(match.examples) ? match.examples.slice(0, 2) : [];
    const examplesHtml = examples.length ? "<div class=\"jpr-match-examples\">" + examples.map(renderGrammarExample).join("") + "</div>" : "";
    return "<div class=\"jpr-entry jpr-grammar-match\">" +
      "<div class=\"jpr-match-head\"><strong>" + escapeHtml(match.title || "Untitled grammar") + "</strong>" +
      "<span>" + escapeHtml(match.jlpt_level || "") + (confidence ? " · " + escapeHtml(confidence) : "") + "</span></div>" +
      (match.matched_text ? "<div class=\"jpr-match-text\">Matched: <strong>" + escapeHtml(match.matched_text) + "</strong></div>" : "") +
      (markers ? "<div class=\"jpr-muted\">Markers: " + escapeHtml(markers) + "</div>" : "") +
      (match.source ? "<div class=\"jpr-muted\">Approach: " + escapeHtml(match.source) + "</div>" : "") +
      (match.formation ? "<div class=\"jpr-match-formation\">" + escapeHtml(match.formation) + "</div>" : "") +
      (match.short_explanation ? "<div>" + escapeHtml(match.short_explanation) + "</div>" : "") +
      (match.markdown_file ? "<button class=\"jpr-open-grammar\" type=\"button\" data-markdown-file=\"" + escapeHtml(match.markdown_file) + "\">Open grammar reference</button>" : "") +
      examplesHtml +
      "</div>";
  }

  function renderGrammarExample(example) {
    return "<div class=\"jpr-match-example\"><div>" + escapeHtml(example.jp || "") + "</div>" +
      (example.en ? "<small>" + escapeHtml(example.en) + "</small>" : "") + "</div>";
  }


  function renderGrammarMarkdown(result) {
    const title = result.title || "Grammar Reference";
    const markdown = result.markdown || "";
    const attribution = result.attribution || "";
    return "<h2>Grammar Reference</h2>" +
      "<div class=\"jpr-entry jpr-markdown-detail\">" +
      "<h3>" + escapeHtml(title) + "</h3>" +
      renderMarkdown(markdown) +
      (attribution ? "<small>" + escapeHtml(attribution) + "</small>" : "") +
      "</div>";
  }

  function renderMarkdown(markdown) {
    const lines = String(markdown || "").split(/\r?\n/);
    const html = [];
    let listOpen = false;
    const closeList = () => {
      if (listOpen) {
        html.push("</ul>");
        listOpen = false;
      }
    };
    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed) {
        closeList();
        continue;
      }
      const heading = trimmed.match(/^(#{1,4})\s+(.+)$/);
      if (heading) {
        closeList();
        const level = Math.min(4, heading[1].length + 2);
        html.push("<h" + level + ">" + renderInlineMarkdown(heading[2]) + "</h" + level + ">");
        continue;
      }
      const bullet = trimmed.match(/^[-*]\s+(.+)$/);
      if (bullet) {
        if (!listOpen) {
          html.push("<ul>");
          listOpen = true;
        }
        html.push("<li>" + renderInlineMarkdown(bullet[1]) + "</li>");
        continue;
      }
      closeList();
      html.push("<p>" + renderInlineMarkdown(trimmed) + "</p>");
    }
    closeList();
    return "<div class=\"jpr-markdown-body\">" + html.join("") + "</div>";
  }

  function renderInlineMarkdown(text) {
    return escapeHtml(text)
      .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
      .replace(/`([^`]+)`/g, "<code>$1</code>");
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
    const expression = entry.expression || entry.query || "";
    const reading = entry.reading ? " <span>" + escapeHtml(entry.reading) + "</span>" : "";
    const pronounceText = entry.reading || expression;
    return "<div class='jpr-token-dictionary-entry'>" +
      "<div class='jpr-token-dictionary-head'>" +
      "<span><strong>" + escapeHtml(expression) + "</strong>" + reading + "</span>" +
      "<button class='jpr-pronounce' type='button' title='Pronounce' aria-label='Pronounce " + escapeHtml(expression) + "' data-pronounce='" + escapeHtml(pronounceText) + "'>🔊</button>" +
      "</div><div>" + glosses + "</div></div>";
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
