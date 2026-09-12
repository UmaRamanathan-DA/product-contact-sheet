"""
Regenerates index.html (standalone page) and artifact-fragment.html
(source for the Claude Artifact) from the assets in build/assets/.

Run from anywhere:  python3 build/generate.py
"""
import base64
import mimetypes
import os

HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HERE)
ASSETS_DIR = os.path.join(HERE, "assets")

def data_uri(filename):
    path = os.path.join(ASSETS_DIR, filename)
    mime, _ = mimetypes.guess_type(path)
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    return f"data:{mime};base64,{b64}"

def img(name, alt):
    return f'<img src="{data_uri(name + ".jpg")}" alt="{alt}" loading="lazy">'

def video(name):
    return f'<video src="{data_uri(name + ".mp4")}" autoplay muted loop playsinline preload="metadata" controls></video>'

rolls = [
    {
        "num": "01",
        "title": "Field Assessment Redesign",
        "badge": "Independent freelance work &mdash; for a client",
        "tag": "MOBILE APP &middot; ENTERPRISE &middot; COMPLIANCE",
        "desc": "Offline-first mobile redesign so compliance assessors can complete inspections onsite, without network or device dependency.",
        "frames": [
            ("asm-1", "Compliance assessment mobile screen, offline capture"),
            ("asm-2", "Compliance assessment mobile screen, checklist"),
            ("asm-3", "Compliance assessment mobile screen, summary"),
            ("asm-4", "Compliance assessment cards view screen"),
            ("asm-5", "Compliance assessment summary dashboard screen"),
            ("asm-6", "Compliance assessment dashboard, hover state"),
        ],
    },
    {
        "num": "02",
        "title": "bobabean",
        "badge": None,
        "video": "boba-video",
        "note": "Select interface icons in this concept are the work of practicing designers, referenced here to sharpen product and visual-design judgment &mdash; not presented as original asset work.",
        "tag": "MOBILE APP &middot; F&amp;B",
        "desc": "A retro-styled coffee app that turns ordering back into a ritual, instead of collapsing it into two taps.",
        "frames": [
            ("boba-1", "bobabean splash screen"),
            ("boba-2", "bobabean drink customization screen"),
            ("boba-6", "bobabean customization screen, variant 1"),
            ("boba-7", "bobabean customization screen, variant 2"),
            ("boba-8", "bobabean customization screen, variant 3"),
            ("boba-9", "bobabean customization screen, variant 4"),
            ("boba-10", "bobabean customization screen, variant 5"),
            ("boba-11", "bobabean menu screen"),
            ("boba-3", "bobabean order confirmed screen"),
            ("boba-4", "bobabean pending order screen"),
            ("boba-5", "bobabean in-store tablet display"),
        ],
    },
    {
        "num": "03",
        "title": "Boards &amp; Paddles",
        "badge": None,
        "tag": "MOBILE APP &middot; MARKETPLACE &middot; OUTDOOR",
        "desc": "One app to book ocean-sports gear and packages, and see who else from the community is going.",
        "frames": [
            ("bp-1", "Boards and Paddles main mobile screen"),
            ("bp-2", "Boards and Paddles booking screen"),
            ("bp-3", "Boards and Paddles gear listing screen"),
            ("bp-4", "Boards and Paddles community screen"),
            ("bp-5", "Boards and Paddles screen, variant 4"),
            ("bp-6", "Boards and Paddles screen, variant 5"),
        ],
    },
    {
        "num": "04",
        "title": "PetMe",
        "badge": None,
        "tag": "MOBILE APP &middot; CONSUMER &middot; iOS / ANDROID",
        "desc": "One app for every pet need &mdash; bookings, records, and reminders that today live across five different apps and a paper folder.",
        "frames": [
            ("petme-1", "PetMe home screen with upcoming pet care tasks"),
            ("petme-6", "PetMe home screen, alternate state"),
            ("petme-2", "PetMe booking flow screen"),
            ("petme-3", "PetMe pet profile and records screen"),
            ("petme-4", "PetMe reminders screen"),
            ("petme-5", "PetMe service provider screen"),
            ("petme-7", "PetMe scheduling screen"),
        ],
    },
    {
        "num": "05",
        "title": "Ksara Decor",
        "badge": "Brand line: Through the Glass Artly",
        "tag": "E-COMMERCE &middot; STOREFRONT &middot; SUSTAINABILITY",
        "desc": "Hand-painted, rescued-glass corporate gifts &mdash; reimagined as a shoppable storefront.",
        "frames": [
            ("ksd-1", "Ksara Decor hand-painted bottle product shot"),
            ("ksd-2", "Ksara Decor bottle product shot, alternate angle"),
            ("ksd-3", "Ksara Decor bottle painting detail shot"),
            ("ksd-4", "Ksara Decor storefront scroller screen"),
        ],
    },
    {
        "num": "06",
        "title": "Loan Distribution Equity Analysis",
        "badge": None,
        "video": "loan-fairness-video",
        "tag": "DATA VIZ &middot; GEOSPATIAL &middot; TABLEAU",
        "desc": "Geospatial Tableau analysis surfacing where loan distribution diverges from equitable access, not just where volume is highest.",
        "frames": [],
    },
    {
        "num": "07",
        "title": "Taxi Business Insights",
        "badge": None,
        "layout": "grid-2",
        "tag": "DATA VIZ &middot; OPERATIONS &middot; TABLEAU &amp; PYTHON",
        "desc": "Where a Glasgow taxi fleet's demand actually happens, and whether pricing holds up &mdash; turned from raw trip data into visible patterns.",
        "frames": [
            ("taxi-1", "Taxi business insights dashboard overview"),
            ("taxi-2", "Taxi pickups by hour of day chart"),
            ("taxi-3", "Taxi drop-off postcode by hour chart"),
            ("taxi-4", "Taxi fare analysis chart"),
        ],
    },
]

def render_frame(roll_frame_count, idx, name, alt):
    num = f"{idx+1:02d}/{roll_frame_count:02d}"
    return f'''<figure class="frame">
              <span class="frame-num">{num}</span>
              {img(name, alt)}
            </figure>'''

def render_video_frame(video_name):
    return f'''<figure class="frame frame-video">
              <span class="frame-num">WALKTHROUGH</span>
              {video(video_name)}
            </figure>'''

roll_sections = []
for r in rolls:
    frame_items = [
        render_frame(len(r["frames"]), i, name, alt) for i, (name, alt) in enumerate(r["frames"])
    ]
    if r.get("video"):
        frame_items = [render_video_frame(r["video"])] + frame_items
    frames_html = "\n            ".join(frame_items)
    badge_html = f'<span class="badge">{r["badge"]}</span>' if r["badge"] else ""
    note_html = f'<p class="asset-note">{r["note"]}</p>' if r.get("note") else ""
    frames_class = "frames grid-2" if r.get("layout") == "grid-2" else "frames"
    roll_sections.append(f'''
      <section class="roll" aria-labelledby="roll-{r['num']}-title">
        <div class="roll-head">
          <span class="roll-index">ROLL {r['num']}</span>
          <div class="roll-heading">
            <h2 id="roll-{r['num']}-title">{r['title']}</h2>
            {badge_html}
            <p class="roll-desc">{r['desc']}</p>
            {note_html}
          </div>
          <span class="roll-tag">{r['tag']}</span>
        </div>
        <div class="{frames_class}">
            {frames_html}
        </div>
      </section>''')

roll_sections_html = "\n".join(roll_sections)

HEAD_CSS = '''
  :root {
    /* dark is the primary palette for this page */
    --bg: #0B0A0E;
    --surface: #17151C;
    --surface-2: #1F1C25;
    --ink: #F6F3F7;
    --ink-soft: #ACA6B3;
    --ink-faint: #6E6976;
    --accent: #FF3D8A;
    --accent-ink: #2A0416;
    --accent-soft: #33101F;
    --rule: #2A2731;
    --frame-border: #2C2933;
    --frame-shadow: 0 14px 28px -10px rgba(0, 0, 0, 0.7), 0 4px 10px -2px rgba(0, 0, 0, 0.5);
    --frame-shadow-hover: 0 20px 36px -10px rgba(0, 0, 0, 0.75), 0 6px 14px -2px rgba(0, 0, 0, 0.55);
    --frame-edge: rgba(255, 255, 255, 0.07);
  }

  @media (prefers-color-scheme: light) {
    :root:not([data-theme="dark"]) {
      --bg: #F5F2F4;
      --surface: #FFFFFF;
      --surface-2: #ECE7EA;
      --ink: #1B181E;
      --ink-soft: #59535E;
      --ink-faint: #928C97;
      --accent: #C4006A;
      --accent-ink: #FFFFFF;
      --accent-soft: #FBDCEB;
      --rule: #E4DEE3;
      --frame-border: #E4DEE3;
      --frame-shadow: 0 14px 28px -12px rgba(40, 20, 35, 0.22), 0 4px 10px -3px rgba(40, 20, 35, 0.12);
      --frame-shadow-hover: 0 20px 36px -12px rgba(40, 20, 35, 0.28), 0 6px 14px -3px rgba(40, 20, 35, 0.16);
      --frame-edge: rgba(255, 255, 255, 0.6);
    }
  }

  :root[data-theme="light"] {
    --bg: #F5F2F4;
    --surface: #FFFFFF;
    --surface-2: #ECE7EA;
    --ink: #1B181E;
    --ink-soft: #59535E;
    --ink-faint: #928C97;
    --accent: #C4006A;
    --accent-ink: #FFFFFF;
    --accent-soft: #FBDCEB;
    --rule: #E4DEE3;
    --frame-border: #E4DEE3;
    --frame-shadow: 0 14px 28px -12px rgba(40, 20, 35, 0.22), 0 4px 10px -3px rgba(40, 20, 35, 0.12);
    --frame-shadow-hover: 0 20px 36px -12px rgba(40, 20, 35, 0.28), 0 6px 14px -3px rgba(40, 20, 35, 0.16);
    --frame-edge: rgba(255, 255, 255, 0.6);
  }

  * { box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--ink);
    font-family: var(--font-body);
    margin: 0;
    padding: 0 0 96px;
  }

  :root {
    --font-display: 'Fraunces', Georgia, 'Times New Roman', serif;
    --font-body: 'Archivo', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    --font-mono: 'IBM Plex Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  }

  .wrap {
    max-width: 1120px;
    margin: 0 auto;
    padding: 56px 32px 0;
  }

  header.masthead {
    padding-bottom: 40px;
    border-bottom: 1px solid var(--rule);
    margin-bottom: 8px;
  }

  .byline {
    display: flex;
    align-items: baseline;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 26px;
  }

  .byline-name {
    font-family: var(--font-display);
    font-weight: 600;
    font-size: 16px;
    color: var(--ink);
  }

  .byline-studio {
    font-family: var(--font-mono);
    font-size: 11px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--accent);
    padding-left: 12px;
    border-left: 1px solid var(--rule);
  }

  .byline-title {
    font-family: var(--font-mono);
    font-size: 11px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--ink-faint);
    padding-left: 12px;
    border-left: 1px solid var(--rule);
  }

  .eyebrow {
    font-family: var(--font-mono);
    font-size: 11.5px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--accent);
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 18px;
  }

  .eyebrow::before {
    content: "";
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--accent);
    display: inline-block;
    box-shadow: 0 0 0 4px var(--accent-soft);
  }

  h1.title {
    font-family: var(--font-display);
    font-optical-sizing: auto;
    font-weight: 500;
    font-size: clamp(34px, 5vw, 54px);
    line-height: 1.06;
    margin: 0 0 18px;
    text-wrap: balance;
    max-width: 16ch;
  }

  h1.title em {
    color: var(--accent);
    font-style: italic;
  }

  p.intro {
    font-size: 16.5px;
    line-height: 1.65;
    color: var(--ink-soft);
    max-width: 62ch;
    margin: 0;
  }

  p.intro strong {
    color: var(--ink);
    font-weight: 600;
  }

  p.intro .highlight {
    color: var(--accent);
    font-weight: 600;
  }

  .rolls {
    display: flex;
    flex-direction: column;
  }

  .roll {
    padding: 44px 0 40px;
    border-bottom: 1px solid var(--rule);
  }

  .roll-head {
    display: grid;
    grid-template-columns: 64px 1fr auto;
    align-items: start;
    gap: 20px;
    margin-bottom: 22px;
  }

  .roll-index {
    font-family: var(--font-mono);
    font-size: 12px;
    letter-spacing: 0.08em;
    color: var(--ink-faint);
    padding-top: 6px;
  }

  .roll-heading h2 {
    font-family: var(--font-display);
    font-weight: 500;
    font-size: clamp(22px, 2.6vw, 28px);
    margin: 0 0 8px;
    text-wrap: balance;
  }

  .badge {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 10.5px;
    letter-spacing: 0.05em;
    color: var(--accent);
    background: var(--accent-soft);
    border-radius: 999px;
    padding: 4px 10px;
    margin-bottom: 10px;
  }

  .asset-note {
    font-size: 12.5px;
    line-height: 1.5;
    color: var(--ink-faint);
    font-style: italic;
    max-width: 56ch;
    margin: 10px 0 0;
  }

  .roll-desc {
    font-size: 14.5px;
    line-height: 1.55;
    color: var(--ink-soft);
    max-width: 56ch;
    margin: 0;
  }

  .roll-tag {
    font-family: var(--font-mono);
    font-size: 10.5px;
    letter-spacing: 0.09em;
    color: var(--ink-faint);
    text-align: right;
    padding-top: 8px;
    white-space: nowrap;
  }

  /* Row-wise grid -- frames flow left to right, top to bottom in number order.
     No forced aspect ratio (align-items: start), so nothing gets cropped;
     shorter frames just leave quiet space beneath them in their row. */
  .frames {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 20px;
    align-items: start;
  }

  /* Fixed 2x2 grid for rolls where frames read better large (e.g. wide dashboard charts) */
  .frames.grid-2 {
    grid-template-columns: repeat(2, 1fr);
    gap: 22px;
  }

  @media (max-width: 480px) {
    .frames.grid-2 { grid-template-columns: 1fr; }
  }

  .frame {
    position: relative;
    margin: 0;
    background: var(--surface);
    border: 1px solid var(--frame-edge);
    border-radius: 4px;
    overflow: hidden;
    box-shadow: var(--frame-shadow);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
  }

  .frame:hover {
    transform: translateY(-4px);
    box-shadow: var(--frame-shadow-hover);
  }

  .frame img {
    width: 100%;
    height: auto;
    display: block;
  }

  .frame-video .frame-num {
    letter-spacing: 0.06em;
  }

  .frame-video video {
    width: 100%;
    height: auto;
    display: block;
  }

  .frame-num {
    position: absolute;
    top: 6px;
    left: 6px;
    font-family: var(--font-mono);
    font-size: 9.5px;
    letter-spacing: 0.03em;
    color: var(--accent-ink);
    background: var(--accent);
    padding: 2px 5px;
    border-radius: 2px;
    z-index: 1;
  }

  .contact {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 14px;
    padding: 36px 0;
    border-top: 1px solid var(--rule);
  }

  .contact-line {
    font-family: var(--font-display);
    font-style: italic;
    font-size: clamp(17px, 2vw, 20px);
    margin: 0;
  }

  .contact-links {
    display: flex;
    gap: 20px;
    font-family: var(--font-mono);
    font-size: 12px;
    letter-spacing: 0.04em;
  }

  .contact-links a {
    color: var(--ink-soft);
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: color 0.15s ease, border-color 0.15s ease;
  }

  .contact-links a:hover {
    color: var(--accent);
    border-color: var(--accent);
  }

  footer {
    max-width: 1120px;
    margin: 0 auto;
    padding: 0 32px;
    font-family: var(--font-mono);
    font-size: 11px;
    letter-spacing: 0.04em;
    color: var(--ink-faint);
  }

  @media (max-width: 900px) {
    .frames { grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); }
  }

  @media (max-width: 640px) {
    .wrap { padding: 40px 20px 0; }
    footer { padding: 0 20px; }
    .roll-head {
      grid-template-columns: 1fr;
      gap: 6px;
    }
    .roll-index { padding-top: 0; }
    .roll-tag { text-align: left; padding-top: 4px; }
    .frames { grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); }
    .frames.grid-2 { grid-template-columns: 1fr; }
  }

  @media (prefers-reduced-motion: reduce) {
    .frame { transition: none; }
    .frame:hover { transform: none; }
  }
'''

FONT_LINKS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,450;9..144,500;9..144,600&family=Archivo:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">'''

BODY_HTML = f'''<div class="wrap">
  <header class="masthead">
    <div class="byline">
      <span class="byline-name">Uma Ramanathan</span>
      <span class="byline-studio">Canvas &amp; Coefficients Studio</span>
      <span class="byline-title">Product Ideation &middot; Design &middot; Analytics &middot; AI</span>
    </div>
    <div class="eyebrow">Quick-glance gallery</div>
    <h1 class="title">Product, in <em>frames</em>.</h1>
    <p class="intro">
      A contact sheet, not a case-study deck &mdash; <strong>shipped and prototyped app design work</strong>,
      rolled out frame by frame the way I'd walk a founder through it over coffee.
      I also build <span class="highlight">real analytical dashboards and AI automations</span> end-to-end &mdash;
      the data-viz rolls below are early proof, with AI automation case studies loading in next.
    </p>
  </header>

  <div class="rolls">
{roll_sections_html}
  </div>

  <section class="contact">
    <p class="contact-line">Let's talk product.</p>
    <div class="contact-links">
      <a href="mailto:umaramanathan54@gmail.com">Email</a>
      <a href="https://www.linkedin.com/in/uma-ramanathan-canvasandcoefficients" target="_blank" rel="noopener">LinkedIn</a>
    </div>
  </section>
</div>

<footer>CANVAS &amp; COEFFICIENTS STUDIO &mdash; UMA RAMANATHAN &mdash; CONTACT SHEET</footer>'''

# 1. Artifact fragment (no doctype/html/head/body -- the Artifact tool wraps this)
fragment = f'''<title>Product Contact Sheet</title>
<style>
{HEAD_CSS}</style>
{FONT_LINKS}

{BODY_HTML}
'''
FRAGMENT_OUT = os.path.join(HERE, "artifact-fragment.html")
with open(FRAGMENT_OUT, "w") as f:
    f.write(fragment)
print("wrote fragment:", FRAGMENT_OUT, len(fragment), "chars")

# 2. Standalone full document -- this is the published page (repo root, index.html)
standalone = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Product Contact Sheet</title>
<meta name="description" content="A quick-glance contact sheet of shipped mobile app and product design work, with analytics &amp; AI rolls loading next.">
<style>
  :root {{ color-scheme: dark light; }}
  html, body {{ margin: 0; padding: 0; }}
  img {{ max-width: 100%; }}
{HEAD_CSS}</style>
{FONT_LINKS}
</head>
<body>
{BODY_HTML}
</body>
</html>
'''
STANDALONE_OUT = os.path.join(REPO_ROOT, "index.html")
with open(STANDALONE_OUT, "w") as f:
    f.write(standalone)
print("wrote standalone:", STANDALONE_OUT, len(standalone), "chars")
