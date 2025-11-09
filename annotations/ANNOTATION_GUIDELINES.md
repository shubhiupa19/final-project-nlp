# Annotation Guidelines for Song Sentence Boundary Detection

## 1. What “Sentence Boundary” Means
A *sentence boundary* (`1`) marks the end of a complete idea or grammatical sentence.  
If the line continues a thought or is not independently complete, mark it as `0`.
If the line ends a thoughht or completes a sentence, mark it as `1`.

---

## 2. Annotation Rules

| Case | Mark as | Example | Reason |
|------|----------|----------|--------|
| Full independent clause | **1** | “There will be an answer, let it be” | Complete idea |
| Imperative or standalone phrase | **1** | “Let it be” / “Shine on ’til tomorrow” | Independent sentence |
| Dependent clause starting with connectors (*when, because, though, and, for though, while*) | **0** | “And when the brokenhearted people living in the world agree” | Thought continues |
| Section headers (e.g., `[Chorus]`, `[Verse]`, `[Bridge]`) | **0** | `[Chorus]` | Non-sentence metadata |
| Empty lines or instrumental notes | **0** | `(Instrumental Bridge)` | Non-verbal cue |
| Mid-sentence continuations across lines | **0** | “I wake up to the sound of music, Mother Mary comes to me” → “Speaking words of wisdom, ‘Let it be’” | Second line completes the first |

---

## 3. Special Cases

- **Repetitions:** If a phrase repeats (e.g., “Let it be, let it be, let it be”), treat the **entire line** as one complete thought → mark `1`.  
- **Conjunctions:** Lines beginning with “And”, “But”, “For”, or “Though” often need `0` unless they can stand alone as full sentences.  
- **Interjections:** Words like “Yeah,” or “Oh,” at the start don’t change sentence completeness — e.g., “Oh, there will be an answer, let it be” → `1`.

---

## 4. Example Block (from *Let It Be*)

| line | label | reason |
|------|--------|--------|
| And when the brokenhearted people living in the world agree | 0 | incomplete clause |
| There will be an answer, let it be | 1 | completes idea |
| For though they may be parted, there is still a chance that they will see | 0 | dependent |
| There will be an answer, let it be | 1 | ends thought |
| [Chorus] | 0 | section marker |
| Let it be, let it be, let it be, yeah, let it be | 1 | complete thought |
| Whisper words of wisdom, let it be | 1 | final closure |

---

## 5. File Format
- Output files must have **two columns:**
  - `line`
  - `sentence_boundary_exists_after_this_line`
- Save as `.csv`
- File name format: `<song_title>.csv` (snake_case)

---

## 6. Sanity Check Before Commit
- No stray commas or quotes  
- No blank rows  
- Only `0` or `1` in the second column  
- Section headers (e.g. Chorus, Verse, etc) remain as `0`  
- File saved in `annotations/` folder  

## 7. When You're Unsure
- Mark the line with a `?` in a third column `notes`
- When it's ambiguous, err on the side of `0` (no boundary), since it's safe to miss boundaries than to break up 
independent clauses (under-segment vs over-segment)
- Add the line to `EDGE_CASES.md`

---
