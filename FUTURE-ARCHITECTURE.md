# Future work, half-done work, things tried

## Status (6 Oct 2026)
- Chapter 1 (lecture 1) written and checked; chapters 2–22 to do, in order.
- Transcripts: auto-captions downloaded per segment with yt-dlp (some segments may have failed:
  `python tools/transcripts.py` lists the missing ones; rerun yt-dlp with `--playlist-items`).
- `main.tex`: Part II (`\part{Advanced...}`) is commented out until chapter 13 exists.

## Ideas
- Readings: only the Allyn Young chapters are in `materials/week1/readings`; the other readings
  (Minsky, Dunbar, Bagehot, Hicks, Treynor, Mundell, Kindleberger, Gurley–Shaw, FOMC 1952) are
  summarised from what the lectures say. Add the PDFs if found, and summarise them in `reading` boxes.
- Mehrling's own lecture notes exist for every lecture (Coursera module 1, "Lecture Notes (for
  download)"); only Lec 1–2 are here. With the others, each chapter could be checked against them.
- Appendix A: map lecture -> segments -> videos -> readings (generate from `materials/videos.csv`).
- Coursera midterm-review module (10 videos: Q&A on standard/subordinate coin, war finance,
  forward parity, CHIPS/Fedwire, Fed balance sheet) is not in the YouTube playlist.

## Tried and changed
- Floating `figure` inside paracol: left a page almost empty (right-column item pushed to the next
  page). Replaced by the non-floating `nfigure` environment.
- T-account columns as justified `p` columns: ugly hyphenation; now ragged-right with `\amt`.
- The template in `~/.claude/templates/lecture-notes` is older than the 18.642 preamble (no paracol,
  answers, requests, history temple): this project started from the 18.642 preamble instead.

## Status (Oct 2026)
- Chapters 1-22 written, built, committed (one chapter per lecture).
- Missing content: segments L19.2 (FOMC 1952 reading), L20.1 (FT: internationalization of the euro),
  L21.4 (global dimension) have no YouTube captions. Plan: download audio (yt-dlp -x) and transcribe
  locally with faster-whisper into materials/transcripts/LXX-PYY.txt, then add the sections.
  Oct 2026 attempt: YouTube answered "Sign in to confirm you're not a bot" for every player client
  (IP flagged); needs a retry later or cookies (`--cookies-from-browser`, only with Alessio's OK).
- Playlist errors: video L19.4 ("What is a swap") contains the same lecture as L19.5; L8.10 duplicates L8.9.
- Possible next: appendix A (materials map).

- Mehrling's written notes (sites.bu.edu/perry), one PDF per lecture, in materials/mehrling-notes/ (+ .txt with page markers). Cite with `\mn{L}{page}`. TODO: integrate them into all 22 chapters; L19.2 and L20.1 are not covered by them (still need audio).
