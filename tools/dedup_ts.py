"""Collapse runs of adjacent \\ts{L}{P}{t} links to the same video, keeping the first (earliest)."""
import re, sys, glob

TS = r'\\ts\{(\d+)\}\{(\d+)\}\{([\d:]+)\}'
RUN = re.compile(r'(?:' + TS + r')(?:\s*' + TS + r')+')


def collapse(m):
    parts = re.findall(TS, m.group(0))
    out, prev = [], None
    for l, p, t in parts:
        if (l, p) != prev:
            out.append('\\ts{%s}{%s}{%s}' % (l, p, t))
        prev = (l, p)
    return ''.join(out)


def run(text):
    return RUN.sub(collapse, text)


if __name__ == '__main__':
    assert run(r'a \ts{1}{2}{0:10}\ts{1}{2}{0:30}\ts{1}{3}{0:05} b') == r'a \ts{1}{2}{0:10}\ts{1}{3}{0:05} b'
    for f in sys.argv[1:] or glob.glob('lecture-notes/chapters/*.tex'):
        s = open(f, encoding='utf-8').read()
        n = run(s)
        if n != s:
            open(f, 'w', encoding='utf-8').write(n)
            print(f, s.count('\\ts{') - n.count('\\ts{'))
