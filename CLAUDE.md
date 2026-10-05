# Instructions for Claude — Mehrling lecture notes

Talk to Alessio in Italian; the notes, code and docs are in English.
Global preferences (`~/.claude/rules/alessio-preferences.md`, section "Lecture notes") apply in full:
fixed box colours, screen layout with right column, notes/answers/requests system, history boxes,
"New concepts" definition boxes, etymology of new terms, enumerations one item per line, exercises
without solutions, `mysolution` never edited (comments go in `\feedback`).

## Sources and how to use them
- One chapter per lecture (`chapters/chNN-<slug>.tex`), sections follow the video segments.
- Read the segment transcripts `materials/transcripts/LXX-PYY.txt` (auto-captions, lower case, no
  punctuation: paraphrase in clean English, fix mis-hearings such as "badget" -> Bagehot, "stigm" ->
  Stigum, "alan young" -> Allyn Young). Never drop content of a segment.
- Lectures 1–2 also have human captions (`materials/week1/srt/`) and Mehrling's own lecture notes PDFs
  (`materials/week1/lecture-notes/`): prefer them for wording, use the YouTube times for links.
- Every point gets a video tag `\ts{L}{P}{m:ss}` with the time from the `LXX-PYY.txt` line where it is
  said. `\seg{L}{P}{text}` links a whole segment (Sources box).
- Numbers quoted in class are reported as said; when they are dubious, say so (e.g. "as said in class").
- History boxes: fact-checked, with a References line.

## LaTeX conventions (preamble.tex)
- T-accounts: `\tacct[width]{Title}{assets, rows separated by \\}{liabilities}` inside `taccts`;
  `\amt{852}` right-aligns an amount.
- Use `nfigure` (non-floating) instead of `figure`: floats inside paracol left almost empty pages.
- Boxes: `intuition`, `finance` ("In the markets"), `casestudy` (FT article of the day), `reading`
  (assigned reading), `keyformulas`, `secondary`, `history`, `aside`, `coursenote`, `example`.
- A right-column item queued at the end of a section must be flushed with `\flushside` before a
  `\section*` heading, or it inherits the heading font.
- When writing LaTeX through the shell, backslashes get mangled: use the Edit/Write tools.

## Build and check
`cd lecture-notes && python .vscode/build.py full`, then grep `build/main.log` for
`\.tex:[0-9]+:`, `undefined`, `Overfull`; look at the rendered pages (Read tool on `build/main.pdf`).
Commit after each verified chapter; push only when asked.
