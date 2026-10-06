"""Transcribe uncaptioned segments locally (faster-whisper) into materials/transcripts/LXX-PYY.txt,
same format as tools/transcripts.py: header line, then 'm:ss text' lines."""
import csv
from pathlib import Path
from faster_whisper import WhisperModel

ROOT = Path(__file__).resolve().parent.parent
SEGS = {'dlaIO_35Vp8', 'mmgYLekyw3Y', 'MsJ1GOM33OU'}

import av
import numpy as np


def decode(path):
    """16 kHz mono float32 (the installed PyAV is older than faster-whisper's own decoder expects)."""
    with av.open(str(path)) as c:
        rs = av.AudioResampler(format='s16', layout='mono', rate=16000)
        out = [f.to_ndarray() for fr in c.decode(audio=0) for f in rs.resample(fr)]
    return np.concatenate(out, axis=1).flatten().astype(np.float32) / 32768.0


rows = {r['id']: r for r in csv.DictReader(open(ROOT / 'materials/videos.csv', encoding='utf-8'))}
model = WhisperModel('small.en', device='cpu', compute_type='int8')
for vid in SEGS:
    r = rows[vid]
    L, P = int(r['lecture']), int(r['part'])
    d = int(r['duration'])
    segs, _ = model.transcribe(decode(next((ROOT / 'materials/audio').glob(vid + '.*'))), vad_filter=True)
    lines = [f"Lec {L}: {r['lecture_title']} | Part {P}: {r['part_title']} | https://youtu.be/{vid} | {d // 60}:{d % 60:02d}"]
    for s in segs:
        t = int(s.start)
        lines.append(f"{t // 60}:{t % 60:02d} {s.text.strip()}")
    out = ROOT / f'materials/transcripts/L{L:02d}-P{P:02d}.txt'
    out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(out.name, len(lines) - 1)
