# Annotation Guidelines for Song Sentence Boundary Detection

## 1. What “Sentence Boundary” Means
A *sentence boundary* (`1`) marks the end of a **complete idea as expressed in the lyric**, even if the line is **not a full grammatical sentence**.

If the line continues the same idea into the next line, mark it as `0`.  
If the line feels lyrically complete, mark it as `1`.

> **Annotate lyrical completeness, not grammatical correctness.**

---

## 2. Annotation Rules

| Case | Mark as | Example | Reason |
|------|---------|---------|--------|
| Full independent clause | **1** | “There will be an answer, let it be” | Complete idea |
| Imperative or standalone phrase | **1** | “Let it be” / “Shine on ’til tomorrow” | Independent lyrical unit |
| **Dependent clause that ends a lyrical idea** | **1** | “That you found a girl and you're married now” | Lyrically complete even if grammatically dependent |
| Dependent clause that clearly continues a thought | **0** | “And when the brokenhearted people living in the world agree” | Thought continues |
| Section headers (e.g., `[Chorus]`, `[Verse]`, `[Bridge]`) | **0** | `[Chorus]` | Non-sentence metadata |
| Empty lines or instrumental notes | **0** | `(Instrumental Bridge)` | Non-verbal cue |
| Mid-sentence continuations across lines | **0** | “For though they may be parted…” → next line completes idea | Does not end thought |

---

## 3. Special Cases

- **Repetitions:** If a phrase repeats (e.g., “Let it be, let it be, let it be”), treat the entire line as one complete thought → `1`.  
- **Conjunctions:** Lines beginning with *And*, *But*, *For*, *Though*, or *That* may be `1` **if the line feels lyrically complete**, otherwise `0`.  
- **Interjections:** Words like “Yeah,” or “Oh,” do not affect completeness — e.g., “Oh, there will be an answer, let it be” → `1`.

---

## 4. Example Block (from *Let It Be*)

| line | label | reason |
|------|--------|--------|
| And when the brokenhearted people living in the world agree | 0 | incomplete idea |
| There will be an answer, let it be | 1 | complete idea |
| For though they may be parted, there is still a chance that they will see | 0 | thought continues |
| There will be an answer, let it be | 1 | complete idea |
| [Chorus] | 0 | section marker |
| Let it be, let it be, let it be, yeah, let it be | 1 | full thought |
| Whisper words of wisdom, let it be | 1 | complete idea |

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
- Only `0` or `1` values in the boundary column  
- Section headers remain `0`  
- File saved in `annotations/` folder  

---

## 7. When You're Unsure

- Mark the line with a `?` in a third column called `notes`  
- Prefer `0` for ambiguous cases (under-segmentation is safer)  
- Add difficult cases to `EDGE_CASES.md`

---
