
# SCRIPT DESCRIPTION:
# The purpose of this script is to extract one specific song's lyrics from the dataset
# In order to use it, you need to provide the artist name and song title as command line arguments, and 
# store the output file in the annotations/ directory.
# Example format : extract_song.py "Adele" "Hello" "annotations/hello.csv"

import pandas as pd
from pathlib import Path
import sys

DATA_CSV = Path("data/song_lyrics.csv")

def create_song_csv(artist, title, output_path):
    cols = ['artist', 'title', 'lyrics', 'language']
    df = pd.read_csv(DATA_CSV, usecols=cols)
    df = df[df['language'] == 'en']
    song_df = df[(df['artist'].str.lower() == artist.lower()) & (df['title'].str.lower() == title.lower())]
    if song_df.empty:
        print(f"No exact match for {artist} : {title}. Trying partial match now:")
        song_df = df[df["artist"].str.contains(artist, case=False, na=False) & df["title"].str.contains(title, case=False, na=False)]

    lyrics = song_df.iloc[0]['lyrics']
    lines = lyrics.split('\n')
    pd.DataFrame({
    "line": lines,
    "sentence_boundary_exists_after_this_line": ""
}).to_csv(output_path, index=False)

    print(f"Saved {len(lines)} lines to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python extract_song.py <artist> <title> <output_path>")
        sys.exit(1)
    artist = sys.argv[1]
    title = sys.argv[2]
    output_path = sys.argv[3]
    create_song_csv(artist, title, output_path)
