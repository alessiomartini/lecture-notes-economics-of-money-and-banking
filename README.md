# Economics of Money and Banking (Perry Mehrling) — Lecture Notes

Personal LaTeX study notes for Perry Mehrling's course *Economics of Money and Banking*
(Barnard College / Columbia University; ColumbiaLearn on YouTube, Coursera, INET).
22 lectures, cut into 192 short video segments; one chapter per lecture.

The compiled book is `lecture-notes/build/book.pdf` (refreshed by every full build).

## Structure

```
├── README.md  CLAUDE.md  FUTURE-ARCHITECTURE.md
├── tools/transcripts.py        # playlist + captions -> videos.csv, per-segment transcripts, videos.tex
├── materials/                  # course material as downloaded (sources of the notes)
│   ├── playlist.json           # yt-dlp metadata of the 192-video playlist
│   ├── videos.csv              # index, lecture, part, titles, YouTube id, duration
│   ├── transcripts/
│   │   ├── LXX-PYY.txt         # clean auto-caption text of lecture XX, segment YY (m:ss local times)
│   │   ├── raw/                # yt-dlp json3 auto-captions, one per video
│   │   └── transcript-lecture-*.txt   # original concatenated transcripts of lectures 1-12 (cross-check)
│   ├── week1/                  # from the Week 1 zip: Mehrling's lecture notes (Lec 1-2), human .srt captions, Allyn Young reading
│   ├── web/                    # saved Coursera / INET / YouTube playlist pages
│   └── Week28money002%29.zip   # original Week 1 download with the videos (not in git)
└── lecture-notes/              # the LaTeX book (same setup as the MIT 18.642 notes)
    ├── main.tex  preamble.tex  videos.tex (generated)
    ├── chapters/ch00-requests.tex, ch01-four-prices.tex, ...
    └── .vscode/                # LaTeX Workshop: save = fast build of the saved chapter
```

## Build

Open `lecture-notes/` in VS Code with LaTeX Workshop: saving a chapter rebuilds only that chapter
(`.vscode/build.py`); the recipe *Whole book (latexmk)* builds everything and copies the result to
`build/book.pdf`. From a shell:

```bash
cd lecture-notes && python .vscode/build.py full
```

Requires a TeX distribution with `latexmk` (MiKTeX/TeX Live) and Python 3.

## Refreshing the transcripts

```bash
python -m pip install --user yt-dlp
python -m yt_dlp --flat-playlist -J "https://www.youtube.com/playlist?list=PLSuwqsAnJMtwZEwkJgHZCod2xP9b7skF5" > materials/playlist.json
python -m yt_dlp --skip-download --write-auto-subs --sub-langs en-orig --sub-format json3 --sleep-subtitles 2 --ignore-errors -o "materials/transcripts/raw/%(playlist_index)03d-%(id)s.%(ext)s" "https://www.youtube.com/playlist?list=PLSuwqsAnJMtwZEwkJgHZCod2xP9b7skF5"
python tools/transcripts.py
```

`tools/transcripts.py` checks its own output (192 segments, lectures 1–22, parts numbered without
gaps, Lecture 1 length = start of Lecture 2 in the original transcript) and lists missing captions.

## Annotations

Same system as the 18.642 notes: `\note{...}` (new), `\note*` (done), `\note+` (seen),
`answer` boxes, `\feedback`, `\request` in `ch00-requests.tex`. See the chapter "How to use these
notes" in the PDF. Video tags `\ts{L}{P}{m:ss}` link to segment P of lecture L at that second.
