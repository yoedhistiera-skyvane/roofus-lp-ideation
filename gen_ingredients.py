#!/usr/bin/env python3
"""Roofus LP ingredient images via Nano Banana Pro. Same pattern as gen.py."""
import json, sys, base64, mimetypes, pathlib, urllib.request, urllib.error

KEY = (pathlib.Path.home()/".gemini_key").read_text().strip()
ROOT = pathlib.Path(__file__).parent
OUT = ROOT/"assets/gen"
OUT.mkdir(exist_ok=True)
MODEL = "gemini-3-pro-image"

NEG = ("AVOID: gibberish or misspelled text, any text, labels, logos, watermarks, hands, "
       "people, animals, plastic look, oversaturated colors, cluttered busy background, "
       "low-res, jpeg artifacts, cartoon style, illustration style.")

STYLE = ("Bright natural food-photography style, square 1:1. Clean warm cream #FBF8F6 "
         "seamless surface and background, soft daylight from the left, shallow depth of "
         "field, subject centered with generous margin, appetizing, fresh, premium DTC "
         "pet-brand look. No text, no label, no logo. ")

ASSETS = {
 "ing_coconut": (STYLE +
    "A halved fresh coconut showing bright white flesh, beside a small clear glass bowl of "
    "translucent gentle cleansing gel with a soft sheen. Minimal, spa-clean. " + NEG, "1:1"),
 "ing_shea": (STYLE +
    "A small rustic bowl of ivory shea butter with a soft swirled dollop texture, two shea "
    "nuts resting beside it. Creamy, gentle, natural. " + NEG, "1:1"),
 "ing_aloe": (STYLE +
    "Fresh cut aloe vera leaf segments showing translucent gel interior, one small glass "
    "dish of clear aloe gel beside them. Cool, calming, hydrating. " + NEG, "1:1"),
 "ing_flavor": (STYLE +
    "A sprig of fresh vibrant peppermint leaves next to a small glass jar of creamy natural "
    "peanut butter with a wooden spoon resting on it. Real-food, appetizing. " + NEG, "1:1"),
}

def generate(name):
    prompt, aspect = ASSETS[name]
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"],
                             "imageConfig": {"aspectRatio": aspect}},
    }).encode()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}"
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=240) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        print(f"  x {name}: HTTP {e.code} {e.read().decode()[:300]}"); return False
    for p in data.get("candidates", [{}])[0].get("content", {}).get("parts", []):
        inline = p.get("inlineData") or p.get("inline_data")
        if inline and inline.get("data"):
            (OUT/f"{name}.png").write_bytes(base64.b64decode(inline["data"]))
            print(f"  ok {name}"); return True
    print(f"  x {name}: no image"); return False

if __name__ == "__main__":
    names = sys.argv[1:] or list(ASSETS)
    n = sum(generate(x) for x in names)
    print(f"Done {n}/{len(names)}")
