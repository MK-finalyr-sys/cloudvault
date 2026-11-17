#!/usr/bin/env python3
"""Prepare a licensed, rebranded CloudVault distribution from the upstream source."""
from pathlib import Path
import json, re, shutil
root=Path(__file__).resolve().parent.parent
replacements=[("FlareDrive: REMASTERED","CloudVault"),("FlareDrive","CloudVault"),("flaredrive-rev","cloudvault"),("flaredrive","cloudvault"),("drive.epb.wiki","cloudvault.example")]
extensions={".ts",".tsx",".vue",".html",".json",".jsonc",".md",".css",".scss",".webmanifest"}
excluded={"LICENSE","bun.lock","bun.lockb","package-lock.json"}
for p in root.rglob("*"):
    if not p.is_file() or p.name in excluded or p.suffix not in extensions or ".git" in p.parts or "node_modules" in p.parts or ".github" in p.parts: continue
    try: old=p.read_text(encoding="utf-8")
    except UnicodeError: continue
    new=old
    for a,b in replacements: new=new.replace(a,b)
    if new!=old:p.write_text(new,encoding="utf-8")
# Preserve the original MIT license, attribution and upstream provenance.
pkg=root/"package.json"
if pkg.exists():
    data=json.loads(pkg.read_text())
    data["name"]="cloudvault"
    data["description"]="CloudVault: S3-compatible object storage manager on Cloudflare Workers"
    data["repository"]={"type":"git","url":"git+https://github.com/MK-finalyr-sys/cloudvault.git"}
    data["homepage"]="https://github.com/MK-finalyr-sys/cloudvault"
    data.pop("bugs",None)
    pkg.write_text(json.dumps(data,indent=2)+"\n")
wr=root/"wrangler.jsonc"
if wr.exists():
    txt=wr.read_text()
    txt=re.sub(r'("database_id"\s*:\s*")[^"]+(")',r'\g<1>REPLACE_WITH_CLOUDVAULT_D1_ID\2',txt)
    txt=re.sub(r'("id"\s*:\s*")[^"]+(")',r'\g<1>REPLACE_WITH_CLOUDVAULT_KV_ID\2',txt)
    if '"SITE_NAME"' not in txt: txt=txt.replace('"ALLOW_REGISTER": "false",','"ALLOW_REGISTER": "false",\n    "SITE_NAME": "CloudVault",')
    wr.write_text(txt)
# Replace project artwork with a neutral, original vector mark; avoid shipping mascot artwork.
logo=root/"public"/"cloudvault-logo.svg"
logo.parent.mkdir(parents=True,exist_ok=True)
logo.write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128"><rect width="128" height="128" rx="28" fill="#10243a"/><path d="M32 77c-10-1-15-9-13-18 2-9 10-14 19-13 7-21 36-24 47-6 14-1 25 10 25 23 0 13-10 23-23 23H39" fill="none" stroke="#6ee7d2" stroke-width="10" stroke-linecap="round"/><path d="M64 52v39m-15-14 15 14 15-14" fill="none" stroke="white" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>''')
logos=root/"public"/"logos"
if logos.exists(): shutil.rmtree(logos)
for p in root.rglob("*"):
    if not p.is_file() or p.suffix not in extensions or ".git" in p.parts or ".github" in p.parts:continue
    try: old=p.read_text()
    except UnicodeError:continue
    new=re.sub(r'(?:/logos/|\./public/logos/)[^\s"\x27)<>]+',"/cloudvault-logo.svg",old)
    if new!=old:p.write_text(new)
html=root/"index.html"
if html.exists():
    txt=html.read_text()
    txt=txt.replace('href="/favicon.png"','href="/cloudvault-logo.svg"').replace('type="image/png" href="/cloudvault-logo.svg"','type="image/svg+xml" href="/cloudvault-logo.svg"')
    html.write_text(txt)
print("CloudVault rebranding complete. Configure fresh D1/KV IDs before deployment.")
