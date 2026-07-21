# Roofus LP — Cold-Traffic Breath-Test Variant

A landing page built to test **alongside** `get.roofuspet.com`, not replace it.

- **get.roofuspet.com** = offer page. Deal-first, for warm / retargeting traffic.
- **This page** = diagnosis page. Problem-first, buy box pushed to the lower third, built for **cold, problem-unaware** traffic. Pair with educational / UGC hooks.

Measure on **Shopify / Northbeam**, not Meta's dashboard (Meta over-reports for Roofus).

## Files
- `index.html` — the full landing page, single self-contained file
- `assets/` — brand fonts + logo + product/gallery/UGC images (`brand/`), generated timeline & ingredient images (`gen/`), UGC videos
- `claims-sources.md` — every stat on the page with its primary source (Cornell, AVMA, VCA, AVDC, AAHA, CareCredit) + compliance guardrails
- `gen.py` / `gen_ingredients.py` — Nano Banana Pro image-generation scripts (need `~/.gemini_key`, not committed)

## Before launch (needs brand input)
1. Real verified reviews — the 6 review cards are placeholder; aggregate figures (4.9★, 17,800+) are real
2. Checkout URLs per bundle → `CHECKOUT` map in the `<script>`, + Meta pixel in `<head>`
3. Real "Pet Eye Wipes" product image (not on the CDN; grab from Shopify admin)
4. Optional: acceptance-video loop up top + a named before/after story

## QA
Verified on desktop + 375px mobile: no horizontal overflow, all images resolve, scent swap + kit/add-on pricing + review slider all work, 0 emoji / 0 em-dashes in body copy.
