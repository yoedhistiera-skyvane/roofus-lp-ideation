# roofus-lp-ideation

Landing-page ideas for Roofus dental wipes. Each page is a self-contained variant to test against the live site.

## Pages
- **`roofus-advertorial-lp.html`** — advertorial-style LP.
- **`roofus-cold-breath-test-lp.html`** — cold-traffic "diagnosis" page (this variant).
- **`roofus-diffuser-kit-adv-loudnights.html`** — Calming Diffuser Kit advertorial ("Every Sound" angle). Assets in `assets/diffuser-loudnights/`. Problem-first, buy box in the lower third, built for cold / problem-unaware traffic. Assets live in `assets/`.

---

## roofus-cold-breath-test-lp.html

Built to test **alongside** `get.roofuspet.com`, not replace it.

- **get.roofuspet.com** = offer page. Deal-first, for warm / retargeting traffic.
- **This page** = diagnosis page. Problem-first, buy box lower, for **cold, problem-unaware** traffic. Pair with educational / UGC hooks.

Measure on **Shopify / Northbeam**, not Meta's dashboard (Meta over-reports for Roofus).

### Files
- `roofus-cold-breath-test-lp.html` — the full landing page, single self-contained file (open it directly)
- `assets/` — brand fonts + logo + product/gallery/UGC images (`brand/`), generated timeline & ingredient images (`gen/`), UGC videos
- `claims-sources.md` — every stat on the page with its primary source (Cornell, AVMA, VCA, AVDC, AAHA, CareCredit) + compliance guardrails
- `gen.py` / `gen_ingredients.py` — Nano Banana Pro image-generation scripts (need `~/.gemini_key`, not committed)

### Before launch (needs brand input)
1. Real verified reviews — the 6 review cards are placeholder; aggregate figures (4.9★, 17,800+) are real
2. Checkout URLs per bundle → `CHECKOUT` map in the `<script>`, + Meta pixel in `<head>`
3. Real "Pet Eye Wipes" product image (not on the CDN; grab from Shopify admin)
4. Optional: acceptance-video loop up top + a named before/after story

### QA
Verified on desktop + 375px mobile: no horizontal overflow, all images resolve, scent swap + kit/add-on pricing + review slider all work, 0 emoji / 0 em-dashes in body copy.

---

## roofus-diffuser-kit-adv-loudnights.html

Advertorial for the **Roofus Calming Diffuser Kit** (dog). It clones the structure of pawprintlab.com/pages/your-dogs-weight, with all copy rewritten.

- **Angle:** `EverySound-OnEdge`. Noise sensitivity is the most common anxiety trait in dogs (about 1 in 3, Salonen 2020). The hook is a daily moment (the delivery truck at 3:40pm, the 6am trash truck, car doors, afternoon storms), not fireworks, so the page works all year.
- **Entry awareness:** Problem-aware. Pair with moment-led hooks.
- **Hand-off:** every CTA (banner, 2 mid-page, buy box, sticky) goes to the custom PDP `get.roofuspet.com/calming-diffuser`, carrying utm_*/fbclid plus `lp=/adv/every-sound` and `cta=adv-banner|adv-mid1|adv-mid2|adv-buybox|adv-sticky`. The PDP stores these as Shopify cart attributes. No checkout on this page.
- **Buy box:** what's inside + how long, 3 USPs (Safe & Drug-Free Relief / Helps Ease Stress Behaviors / Round-the-Clock Calm), "Launch price from $31.49 · SAVE UP TO 59%", with the Subscribe & Save qualifier in the fine print.

### Claim guardrails (keep these)
- "Helps ease" / "supports calm" only. Never stops, ends, cures, treats anxiety, or clinically proven.
- No reviews, star ratings or customer counts. Roofus has no verifiable diffuser reviews yet. The page uses a 60-day guarantee block instead.
- The cited pheromone studies (Landsberg 2015, Sheppard & Mills 2003) tested other brands' products, and the page says so.
- Never show a dog licking or nosing the diffuser (the label warns it's harmful if swallowed).
- Story photos are AI-generated and disclosed as illustrative in the footer. The product shot is the client's own render.

### Before launch
1. The PDP hero still leads with "STOP MY DOG'S ACCIDENTS!", which mismatches this page. Add a loud-nights/every-sound hero variant, or accept the mismatch.
2. The PDP shows review counts and reviews that can't be verified. That's an FTC risk, so raise it with the client.
3. If prices change, update "from $31.49" and "up to 59%" (the 59% applies to the 3-room kit on Subscribe & Save).
4. Host it on the client domain (e.g. `get.roofuspet.com/adv/every-sound`) so the pixel fires.
