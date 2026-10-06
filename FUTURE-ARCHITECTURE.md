# Future work, half-done work, things tried

## Status (6 Oct 2026)
- Chapter 1 (lecture 1) written and checked; chapters 2–22 to do, in order.
- Transcripts: auto-captions downloaded per segment with yt-dlp (some segments may have failed:
  `python tools/transcripts.py` lists the missing ones; rerun yt-dlp with `--playlist-items`).
- `main.tex`: Part II (`\part{Advanced...}`) is commented out until chapter 13 exists.

## Ideas
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
- L19.2, L20.1, L21.4 had no YouTube captions: transcribed locally (tools/whisper_segments.py, audio in materials/audio, gitignored) and written up.
  L21.4 (global dimension) have no YouTube captions. Plan: download audio (yt-dlp -x) and transcribe
  locally with faster-whisper into materials/transcripts/LXX-PYY.txt, then add the sections.
  Oct 2026 attempt: YouTube answered "Sign in to confirm you're not a bot" for every player client
  (IP flagged); needs a retry later or cookies (`--cookies-from-browser`, only with Alessio's OK).
- Playlist errors: ColumbiaLearn video L19.4 duplicates L19.5; the right segment is the re-upload eZk9A6Pw10g (OVERRIDE in tools/transcripts.py, transcribed with whisper). L8.9 and L8.10 are the same recording; the continuous 7-12 recording shows no segment is missing (note in ch08).
- Readings linked from sites.bu.edu/perry lecture pages: downloaded (materials/readings/) and integrated as `reading`/`coursenote` boxes in ch3, 7, 9, 10, 12-22. L07 deal.pdf is the 2015 release of the weekly NY Fed dealer report (only copy recovered): noted in ch07 with its Treasury repo figures. Corrections found: AIG collateral $30-35bn was to all counterparties (Goldman $8.4bn, SIGTARP Table 2); UBS report names monolines, not AIG, as NegBasis protection sellers. Bagehot, Minsky, Dunbar, Kindleberger, Gurley-Shaw, Treynor still summarised from the lectures only.
- Possible next: appendix A (materials map).

- Mehrling's written notes (sites.bu.edu/perry), one PDF per lecture, in materials/mehrling-notes/ (+ .txt with page markers). Cite with `\mn{L}{page}`. Integrated into all 22 chapters (Oct 2026); page links with \mn{L}{page}.
