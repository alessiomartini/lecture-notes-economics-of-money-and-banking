# Instructions for Claude — Mehrling lecture notes

@~/.claude/templates/lecture-notes/RULES.md
If RULES.md is missing (cloud session), the rules below still apply; don't recreate it.

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
- `cd lecture-notes && python build.py` recompiles the changed chapters and refreshes `build/book.pdf` (continuous-scroll book; chapter PDFs in `lecture-notes/build/scroll/`, links between chapters are not kept). `python build.py ch05` forces one chapter, `all` = full latexmk build, `pages` = paged `build/book-pages.pdf` (use it to check Overfull boxes).
- Page is 31.5x18 cm: keep figures/tables under ~15 cm and right-column boxes on the page.
- Then grep `build/main.log` for `\.tex:[0-9]+:`, `undefined`, `Overfull`, and look at the rendered pages (Read tool on `build/main.pdf`).
