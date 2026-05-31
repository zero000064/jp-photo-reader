# Grammar Matching Architecture

The Japanese Photo Reader extension employs a hybrid local processing engine to identify grammar points in Japanese text. The engine relies on deterministic string and token matching powered by morphological analysis, with an optional LLM-based fallback classifier.

## Overview

The matching process is divided into the following sequential steps:
1. **Text Normalization**
2. **Morphological Tokenization**
3. **Deterministic Token Pattern Rules**
4. **LLM Candidate Recovery (Optional)**
5. **Character-Level Span Matching**
6. **Scoring & Confidence Calculation**
7. **Deduplication**

---

## 1. Text Normalization
Before processing, the Japanese text undergoes normalization to ensure consistency. This involves standardizing full-width and half-width characters, normalizing punctuation, and removing unnecessary whitespace.

## 2. Morphological Tokenization
The normalized text is tokenized using a Japanese morphological analyzer (primarily **SudachiPy**, with fallback support for Fugashi/MeCab). 

The tokenizer breaks the sentence into semantic tokens and extracts:
- **Surface**: The actual text as it appears in the sentence (e.g., `切っ`)
- **Lemma**: The dictionary form / base form of the word (e.g., `切る`)
- **Reading**: The phonetic pronunciation (e.g., `キッ`)
- **POS (Part of Speech)**: Detailed grammatical roles (e.g., `Verb, Godan, Renyoukei`)

## 3. Deterministic Token Pattern Rules
Before searching the main grammar database, the engine runs hardcoded token pattern rules. These are highly specific, regex-like token checks for extremely common or difficult-to-parse grammar structures (such as `てみる` or `かもしれない`). If a sequence of tokens exactly matches the part-of-speech and lemma requirements of a rule, it is immediately flagged as a high-confidence match.

## 4. LLM Candidate Recovery (Optional)
If the user has enabled the local **Ollama** integration, the raw sentence is passed to an LLM. The LLM acts purely as a classifier, returning a list of predicted Hanabira grammar point titles. 

Because the LLM does not provide character spans (where the grammar actually exists in the text), the deterministic engine performs an aggressive search to "recover" the exact location of the LLM's candidates within the token stream. 

## 5. Character-Level Span Matching
For all grammar points in the Hanabira JSON database, the engine attempts to find their defined string **"markers"**. 

Historically, this was done by strictly looking at token boundaries. However, due to tokenizer inconsistencies, the engine now uses **Character-Level Span Recovery**:
1. All token surfaces are joined into a continuous, un-tokenized string.
2. The engine searches for exact substring matches of the grammar marker.
3. When a substring match is found, its character indices are mapped *back* onto the original token array to identify which tokens belong to the match.

> **Note on Conjugation:** Because the span matcher looks for exact substring matches against the token *surface*, grammar points written in their dictionary form (e.g., `さしあげる`) will fail to match conjugated forms in the text (e.g., `さしあげました`).

## 6. Scoring & Confidence Calculation
Once a match is found (either via formation patterns or marker spans), it is passed to a scoring function that assigns a **Confidence Score (0.0 to 1.0)**. 

The score is calculated using:
- **Base Score**: `0.38`
- **Marker Count**: Bonus for matching multiple markers (`min(0.22, 0.06 * markers)`).
- **Match Length**: Bonus for longer, more specific matches.
- **JLPT Weight**: Beginner grammar (N5/N4) receives a slight bonus over advanced grammar (N1) because beginner grammar points appear more frequently.
- **POS Hints**: Bonus if the tokens match the expected parts of speech for that grammar formation.
- **Example Overlap**: Bonus if the target sentence shares vocabulary with the grammar point's predefined example sentences.

If the final confidence score falls below **`0.58`**, the match is discarded as a false positive.

## 7. Deduplication
The engine generates many overlapping matches (for example, matching both `ている` and `いる` on the same word). 
The final step sorts all matches by:
1. Confidence score (highest first)
2. Matched text length (longest first)
3. JLPT level (N5 > N1)

A deduplication pass then removes any matches that are entirely contained within the token span of a higher-ranked match, leaving only the most accurate and descriptive grammar points.

## 8. Matching Approach (Source Values)
To evaluate performance and diagnose matches, the engine attaches a `source` (Approach) property to every matched grammar point. This approach is exposed to the user in the frontend extension. The possible values are:

- **Hanabira.org Japanese Content**: Found via the default deterministic character-level span matcher using the core string markers.
- **Hanabira formation pattern**: Found via dynamically generated token sequence paths extracted from Hanabira's formation rules (e.g., matching a verb in TE form followed by a specific token).
- **Token rule**: Found via hardcoded token and part-of-speech rules in the backend (used as a fallback for complex structures like `てみる` or `てもいい` that span recovery struggles with).
- **Classifier candidate + span recovery**: The Ollama LLM classifier accurately predicted the grammar point's presence, and the local engine successfully recovered its exact substring span within the sentence.
- **Classifier candidate**: The Ollama LLM classifier predicted the grammar point, but the local engine could not recover a reliable exact span. The grammar point is surfaced as a low-confidence hint for the reader.
