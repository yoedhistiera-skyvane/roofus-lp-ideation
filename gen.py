#!/usr/bin/env python3
"""Roofus LP timeline + texture assets via Nano Banana Pro (gemini-3-pro-image).
Reference images pin the real wipe pack / wipe-on-finger. Key from ~/.gemini_key.
Usage: python3 gen.py <asset_key> [asset_key ...]   (no args = all)
"""
import json, sys, base64, mimetypes, pathlib, urllib.request, urllib.error

KEY = (pathlib.Path.home()/".gemini_key").read_text().strip()
ROOT = pathlib.Path(__file__).parent
REF = ROOT/"assets"
OUT = ROOT/"assets/gen"
OUT.mkdir(exist_ok=True)
MODEL = "gemini-3-pro-image"

NEG = ("AVOID: deformed hands, extra fingers, fused or missing fingers, malformed limbs, "
       "uncanny or distorted faces, plastic skin, mutated dog anatomy, extra legs or tails, "
       "gibberish or misspelled text, invented brand logo, fake wordmark, warped product "
       "label, watermark, signature, low-res, jpeg artifacts, oversaturated, cluttered busy "
       "background, cartoon style, illustration style.")

PALETTE = ("Warm cozy natural color grade with soft cream #F3EDE4 tones, honest home "
           "lighting, premium DTC pet-brand look.")

DOG = ("The dog is the SAME dog in every image of this set: a small adult cream-and-tan "
       "Shih Tzu mix, about 6 kg, dark round eyes, slightly scruffy soft coat, wearing a "
       "simple teal fabric collar. Anatomically correct: four legs, one tail, natural "
       "proportions. ")

WIPE = ("The product is a white textured dental finger wipe worn over an adult's index "
        "finger, matching the attached reference photos exactly — same fabric weave, same "
        "fit. Do not restyle it, do not add printing to the wipe. ")

PACK_MINTY = "Image1_DentalFingerWipe-Minty.webp"
APPLY_REF = "Image1_DentalFingerWipe-Minty_Dog-Apply.webp"

# each: (prompt, [ref files], aspect)
ASSETS = {
 "t1_first_signal": (
    DOG + WIPE +
    "Photoreal lifestyle photograph, 4:3 landscape. A cozy living-room floor scene in soft "
    "morning light: a woman's hands gently lifting the small dog's upper lip with one hand "
    "while her other index finger, wearing the white textured dental wipe, approaches the "
    "dog's teeth. The dog sits calm but curious, head slightly tilted, one small training "
    "treat waiting on the rug nearby. Only the owner's forearms and hands are in frame — no "
    "face, no torso. 50mm lens, shallow depth of field, warm window light from the left. "
    "First-week training mood: gentle, patient, slightly tentative. No text, no logo. "
    + PALETTE + " " + NEG, [APPLY_REF, PACK_MINTY], "4:3"),

 "t2_shift": (
    DOG +
    "Photoreal lifestyle photograph, 4:3 landscape. Early-morning couch scene: the small "
    "dog lies relaxed on a cream linen sofa with its chin resting close to its owner's "
    "face — the owner (a woman in her early 30s with dark hair in a loose bun, natural "
    "unretouched skin) lies with eyes half-closed, smiling softly, completely comfortable "
    "with the dog breathing right at her nose. Fresh-breath intimacy is the whole story. "
    "Soft warm dawn light through sheer curtains, 35mm lens, shallow depth of field, candid "
    "and unposed. No product in frame. No text, no logo. " + PALETTE + " " + NEG, [], "4:3"),

 "t3_visible": (
    DOG +
    "Photoreal close-up photograph, 4:3 landscape. An owner's thumb gently lifts the small "
    "dog's upper lip to reveal clean white premolars and a healthy pink gumline — the dog "
    "calm, eyes soft, comfortable with the handling. Sharp crisp focus on the revealed "
    "teeth and gumline, healthy and clean, NO tartar, NO redness. The owner's other hand "
    "holds a phone slightly out of focus in the foreground corner, mid progress-photo. "
    "Bright honest daylight, 85mm macro feel. Realistic dog dentition: small clean teeth, "
    "natural pink-and-black gum pigment. No text, no logo. " + PALETTE + " " + NEG,
    [], "4:3"),

 "t4_baseline": (
    DOG +
    "Photoreal lifestyle photograph, 4:3 landscape. A calm veterinary exam-room scene: the "
    "small dog sits relaxed on the exam table while a friendly veterinarian in a teal scrub "
    "top gently lifts its lip and smiles slightly, visibly pleased with what she sees. The "
    "dog's owner's hands rest reassuringly nearby. Clean bright modern clinic, soft "
    "diffused light, shallow depth of field, warm and unthreatening — a good-news visit, "
    "not a scary one. Natural unretouched faces. No text, no logo, no brand marks on "
    "equipment. " + PALETTE + " " + NEG, [], "4:3"),

 "tex_scrub": (
    WIPE +
    "Photoreal EXTREME macro product photograph, 3:2 landscape. The white textured "
    "dental finger wipe stretched over an adult index fingertip, filling the frame "
    "diagonally. Hard raking side-light skims across the fabric so the raised ridged weave "
    "texture reads in crisp tactile relief — every ridge and loop of the dual-texture "
    "visible. Clean warm cream #F3EDE4 seamless background, soft falloff, premium studio "
    "macro look, tack-sharp focus on the ridges at the fingertip. Natural realistic hand "
    "skin. No text, no logo. " + PALETTE + " " + NEG, [APPLY_REF, PACK_MINTY], "3:2"),

 "tex_formula": (
    WIPE +
    "Photoreal macro product photograph, 3:2 landscape. The white textured dental wipe "
    "laid flat, draped over a soft curve, its surface carrying a fresh moisture sheen with "
    "a few fine glistening micro-droplets of clear cleaning solution catching the light. "
    "Two small fresh mint leaves rest beside it on a clean warm cream #F3EDE4 surface, "
    "soft daylight, shallow depth of field, spa-clean and appetizingly fresh. Tack-sharp "
    "focus on the moist fabric texture. No text, no logo. " + PALETTE + " " + NEG,
    [PACK_MINTY], "3:2"),
}

def part_img(fp):
    data = pathlib.Path(fp).read_bytes()
    mime = mimetypes.guess_type(str(fp))[0] or "image/png"
    return {"inlineData": {"mimeType": mime, "data": base64.b64encode(data).decode()}}

def generate(name):
    prompt, refs, aspect = ASSETS[name]
    parts = [{"text": prompt}]
    for r in refs:
        parts.append(part_img(REF/r))
    if refs:
        parts.insert(0, {"text": "Use the attached reference image(s) as the exact product to depict. "
                                 "Match the wipe fabric, fit and pack design precisely."})
    body = json.dumps({
        "contents": [{"parts": parts}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"],
                             "imageConfig": {"aspectRatio": aspect}},
    }).encode()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}"
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=240) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        print(f"  x {name}: HTTP {e.code} {e.read().decode()[:400]}"); return False
    for p in data.get("candidates", [{}])[0].get("content", {}).get("parts", []):
        inline = p.get("inlineData") or p.get("inline_data")
        if inline and inline.get("data"):
            out = OUT/f"{name}.png"
            out.write_bytes(base64.b64decode(inline["data"]))
            print(f"  ok {name} -> {out}"); return True
    print(f"  x {name}: no image. {json.dumps(data)[:300]}"); return False

if __name__ == "__main__":
    names = sys.argv[1:] or list(ASSETS)
    print(f"Rendering {len(names)} with {MODEL}...")
    n = sum(generate(x) for x in names)
    print(f"Done {n}/{len(names)}")
