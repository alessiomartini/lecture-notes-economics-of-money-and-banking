# Instructions for Claude — Mehrling lecture notes

@~/.claude/templates/lecture-notes/RULES.md

## Sources and how to use them
- The GitHub repo is **public**. Never commit third-party material: `materials/transcripts/`, `week1/`,
  `mehrling-notes/`, `web/`, reading PDFs/texts and audio are gitignored and local only (history was
  cleaned in Oct 2026). Check `git status` for these paths before every commit.
- One chapter per lecture (`chapters/chNN-<slug>.tex`), sections follow the video segments.
- Read the segment transcripts `materials/transcripts/LXX-PYY.txt` (auto-captions, lower case, no
  punctuation: paraphrase in clean English, fix mis-hearings such as "badget" -> Bagehot, "stigm" ->
  Stigum, "alan young" -> Allyn Young). Never drop content of a segment.
- Lectures 1–2 also have human captions (`materials/week1/srt/`) and Mehrling's own lecture notes PDFs
  (`materials/week1/lecture-notes/`): prefer them for wording, use the YouTube times for links.
- Every point gets a video tag `\ts{L}{P}{m:ss}` with the time from the `LXX-PYY.txt` line where it is
  said. `\seg{L}{P}{text}` links a whole segment (Sources box).
- Numbers quoted in class are reported as said; when they are dubious, say so (e.g. "as said in class").

## LaTeX conventions (preamble.tex)
- T-accounts: `\tacct[width]{Title}{assets, rows separated by \\}{liabilities}` inside `taccts`;
  `\amt{852}` right-aligns an amount.
- Use `nfigure` (non-floating) instead of `figure`: floats inside paracol left almost empty pages.
- No end-of-book "Pseudo-exam and second reading" appendix so far (all exercises are short); passages taken out of the text go to a `\section*{Set aside}` at the chapter end.
- Boxes: `intuition`, `finance` ("In the markets"), `casestudy` (FT article of the day), `reading`
  (assigned reading), `keyformulas`, `secondary`, `history`, `aside`, `coursenote`, `example`.
- A right-column item queued at the end of a section must be flushed with `\flushside` before a
  `\section*` heading, or it inherits the heading font.
- When writing LaTeX through the shell, backslashes get mangled: use the Edit/Write tools.

## Build and check
`cd lecture-notes && python build.py` (full build, latexmk, refreshes `build/book.pdf`; the VS Code per-chapter build was archived in `lecture-notes/archive/vscode/`, 2026-11-05). Page is 31.5×18 cm: check figures/tables taller than ~15 cm and right-column boxes running off the page. Then grep `build/main.log` for
`\.tex:[0-9]+:`, `undefined`, `Overfull`; look at the rendered pages (Read tool on `build/main.pdf`).

- Video links: never put consecutive `\ts` links to the same video; keep only the earliest. Run `python tools/dedup_ts.py` after writing a chapter.

- Mehrling's written notes per lecture: `materials/mehrling-notes/` (PDF + text with `=== pN` markers); cite with `\mn{L}{page}` (links to the PDF page on sites.bu.edu).

## Scroll book

`build/book.pdf` is the continuous-scroll book; chapter PDFs are in `lecture-notes/build/scroll/`. `python build.py` recompiles only the chapters whose .tex changed and reassembles; `python build.py ch05` forces a chapter; `python build.py all` = full latexmk build + all chapters; `python build.py pages` = paged book (`build/book-pages.pdf`, use it to check Overfull boxes). Longer chapters are split into several PDF pages. Links between chapters are not kept.
