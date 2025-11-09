## Sentence Boundary Detection in Song Lyrics

This project aims to build a sentence boundary detection (SBD) system for song lyrics, a domain where conventional punctuation-based models (like NLTK’s Punkt or spaCy’s sentencizer) often fail.
We analyze lyric text from the Genius Song Lyrics with Language Information dataset, annotate sentence boundaries manually, and train classifiers to detect where one sentence ends and the next begins.

### Motivation

Standard SBD tools rely heavily on punctuation marks (., ?, !) and line breaks to find boundaries.
However, lyrics use line breaks and rhythm instead of punctuation, so models need to learn sentence-like boundaries based on structure, capitalization, and semantics rather than grammar alone.

### Project Structure

```
final-project-nlp/
│
├── annotations/                 # CSV files with manual sentence boundary annotations
│   └── let_it_be.csv
│
├── data/                        # Large dataset (not tracked by Git)
│   └── song_lyrics.csv
│
├── scripts/
│   └── extract_song.py          # Extracts one song into annotation-ready CSV format
│
├── ANNOTATION_GUIDELINES.md     # Rules for consistent sentence boundary annotation
├── README.md                    # Project overview and setup instructions
└── requirements.txt             # Dependencies for model training (future step)
```

### Dataset Setup

We use the Genius Song Lyrics with Language Information dataset from Kaggle.

1. Download the dataset: https://www.kaggle.com/datasets/carlosgdcj/genius-song-lyrics-with-language-information
2. Extract the CSV file: After unzipping, you should see `song_lyrics.csv`
3. Place the file in this folder: `final-project-nlp/data/song_lyrics.csv`
4. Do NOT commit this file: The dataset is ~8 GB and too large for GitHub. It is listed in .gitignore, so Git will automatically skip it.

### Annotation Workflow

1. Use the extract_song.py script to isolate one song from the dataset: `bash python scripts/extract_song.py "The Beatles" "Let It Be" "annotations/let_it_be.csv" `
2. Annotate manually
