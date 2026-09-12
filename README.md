# Product Contact Sheet

A quick-glance gallery of shipped mobile app and product design work, laid out like a photographer's contact sheet — project name, one-liner, and every frame from the design work, roll by roll.

Live site: published via GitHub Pages from this repo's `main` branch.

Analytics & AI project rolls are loading in next.

## Structure

- `index.html` — the published page. Self-contained: every image and the bobabean video are embedded as base64 data URIs, so it has no runtime dependency on this repo's other files (only Google Fonts loads externally).
- `build/generate.py` — regenerates `index.html` (and `build/artifact-fragment.html`, used for republishing to a Claude Artifact) from the assets below. Project copy, roll order, and layout all live in this script.
- `build/assets/` — the source images and video the generator embeds. Add a file here and reference it in `generate.py`'s `rolls` list to add a new frame.

## Regenerating

```
python3 build/generate.py
```

Then commit the updated `index.html` and push.
