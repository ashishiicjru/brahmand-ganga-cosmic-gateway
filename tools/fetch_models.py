#!/usr/bin/env python3
"""Fetch web-ready 3D assets for Cosmos Tour Pro.
Run from project root: python tools/fetch_models.py
"""
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib, json, sys
ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'tools'/'models_manifest.json'
UA='Cosmos-Tour-Pro/4.0 model-fetcher'
def fetch(item):
    out=ROOT/item['path']; out.parent.mkdir(parents=True,exist_ok=True)
    req=Request(item['url'],headers={'User-Agent':UA})
    with urlopen(req,timeout=60) as r, open(out,'wb') as f:
        while True:
            b=r.read(1024*1024)
            if not b: break
            f.write(b)
    sha=hashlib.sha256(out.read_bytes()).hexdigest()
    print(f"OK {out} sha256={sha[:16]}…")
    return sha
items=json.loads(MANIFEST.read_text())['models']; failed=[]
for item in items:
    try: item['sha256']=fetch(item)
    except Exception as e: failed.append((item['name'],str(e))); print(f"FAILED {item['name']}: {e}",file=sys.stderr)
(MANIFEST.parent/'download_log.json').write_text(json.dumps({'models':items,'failed':failed},indent=2))
print(f'Downloaded: {len(items)-len(failed)}/{len(items)}')
if failed: sys.exit(1)
