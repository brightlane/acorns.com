#!/usr/bin/env python3
"""
build.py — Acorns Affiliate Site
Deploys to: https://brightlane.github.io/acorns.com/
Affiliate:  https://convert.ctypy.com/aff_c?offer_id=29449&aff_id=21885
"""

from datetime import datetime, date
from pathlib import Path
import json as _json

BASE_URL  = "https://brightlane.github.io/acorns.com"
AFF_BASE  = "https://convert.ctypy.com/aff_c?offer_id=29449&aff_id=21885"
SITE_NAME = "AcornsGuide"
BUILT_ON  = datetime.now().strftime("%Y-%m-%d")
OUT       = Path("docs")
OUT.mkdir(exist_ok=True)

def aff(src="page"):
    return f"{AFF_BASE}&utm_source=acornsguide&utm_medium=affiliate&utm_campaign={src}"

# ─── CSS ──────────────────────────────────────────────────────
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Lora:ital,wght@0,400;0,600;1,400&display=swap');

:root{
  --green:#00b386;--green2:#008f6b;--green3:#00d4a0;
  --dark:#05100d;--dark2:#0a1a15;--dark3:#0f2218;--dark4:#162d20;
  --light:#e8f5f0;--cream:#f0faf5;--muted:#5a7a6e;--muted2:#3d5a50;
  --gold:#f0b429;--red:#e74c3c;--blue:#3b82f6;
  --border:rgba(0,179,134,0.15);--border2:rgba(0,179,134,0.35);
  --radius:12px;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--dark);color:var(--light);font-family:'Outfit',sans-serif;font-size:17px;line-height:1.7;-webkit-font-smoothing:antialiased}

/* NAV */
nav{background:rgba(5,16,13,0.97);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:200;padding:0 24px}
.nav-inner{max-width:1140px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:64px;gap:16px}
.logo{font-family:'Outfit',sans-serif;font-size:1.5rem;font-weight:900;color:#fff;text-decoration:none;letter-spacing:-1px;flex-shrink:0}
.logo em{color:var(--green);font-style:normal}
.nav-links{display:flex;gap:2px;flex-wrap:nowrap;overflow:hidden}
.nav-links a{color:rgba(232,245,240,0.55);font-size:0.78rem;font-weight:600;padding:6px 11px;border-radius:6px;text-decoration:none;white-space:nowrap;transition:all 0.15s}
.nav-links a:hover{color:#fff;background:rgba(0,179,134,0.1)}
.nav-cta{background:var(--green);color:#fff;font-weight:700;font-size:0.82rem;padding:9px 18px;border-radius:8px;text-decoration:none;white-space:nowrap;transition:all 0.2s;flex-shrink:0}
.nav-cta:hover{background:var(--green2);transform:translateY(-1px);box-shadow:0 4px 20px rgba(0,179,134,0.4)}
@media(max-width:780px){.nav-links{display:none}}

/* ANN BAR */
.ann-bar{background:linear-gradient(90deg,var(--green2),#006b50,var(--green2));padding:9px 20px;text-align:center;font-size:0.82rem;font-weight:600;letter-spacing:0.3px;color:#fff}
.ann-bar a{color:#fff;text-decoration:underline;text-underline-offset:2px}

/* HERO */
.hero{background:linear-gradient(160deg,#021a12 0%,var(--dark2) 50%,#030d0a 100%);border-bottom:1px solid var(--border);padding:80px 24px 68px;text-align:center;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at 60% 30%,rgba(0,179,134,0.08) 0%,transparent 65%);pointer-events:none}
.hero::after{content:'🌱';position:absolute;font-size:22rem;opacity:0.03;top:-60px;right:-80px;pointer-events:none;line-height:1}
.hero-tag{display:inline-flex;align-items:center;gap:7px;background:rgba(0,179,134,0.1);border:1px solid var(--border2);color:var(--green3);font-size:0.72rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;padding:5px 14px;border-radius:20px;margin-bottom:22px}
.hero h1{font-size:clamp(2rem,5.5vw,3.6rem);font-weight:900;line-height:1.1;color:#fff;max-width:800px;margin:0 auto 20px;letter-spacing:-1px}
.hero h1 span{color:var(--green)}
.hero .sub{font-size:1.1rem;color:rgba(232,245,240,0.65);max-width:560px;margin:0 auto 40px;line-height:1.7;font-weight:400}
.hero-actions{display:flex;gap:14px;justify-content:center;flex-wrap:wrap}
.btn-ghost{display:inline-block;border:1px solid rgba(232,245,240,0.2);color:rgba(232,245,240,0.8);font-size:0.9rem;font-weight:600;padding:13px 26px;border-radius:8px;text-decoration:none;transition:all 0.2s}
.btn-ghost:hover{border-color:rgba(232,245,240,0.45);color:#fff;background:rgba(232,245,240,0.05)}

/* TRUST */
.trust{background:var(--dark2);border-bottom:1px solid var(--border);padding:12px 24px}
.trust-inner{max-width:1140px;margin:0 auto;display:flex;gap:32px;align-items:center;justify-content:center;flex-wrap:wrap}
.ti{display:flex;align-items:center;gap:6px;font-size:0.76rem;font-weight:600;color:rgba(232,245,240,0.4);white-space:nowrap}
.ti .dot{width:6px;height:6px;border-radius:50%;background:var(--green);flex-shrink:0}

/* CTA */
.cta{display:inline-block;background:linear-gradient(135deg,var(--green),var(--green2));color:#fff;font-family:'Outfit',sans-serif;font-weight:800;font-size:1.05rem;padding:16px 36px;border-radius:10px;text-decoration:none;box-shadow:0 4px 24px rgba(0,179,134,0.35);transition:all 0.15s;position:relative;overflow:hidden;letter-spacing:0.2px}
.cta::after{content:'';position:absolute;top:0;left:-80%;width:50%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.12),transparent);transition:left 0.5s}
.cta:hover::after{left:130%}
.cta:hover{transform:translateY(-2px);box-shadow:0 8px 32px rgba(0,179,134,0.5)}
.cta.pulse{animation:gpulse 2.5s ease-in-out infinite}
.cta.sm{font-size:0.88rem;padding:11px 22px}
@keyframes gpulse{0%,100%{box-shadow:0 4px 24px rgba(0,179,134,0.35)}50%{box-shadow:0 4px 40px rgba(0,179,134,0.6)}}

/* LAYOUT */
.wrap{max-width:920px;margin:0 auto;padding:52px 24px 100px}

/* BREADCRUMB */
.bc{font-size:0.77rem;color:var(--muted);margin-bottom:34px;display:flex;gap:6px;align-items:center;flex-wrap:wrap}
.bc a{color:var(--muted);text-decoration:none;transition:color 0.15s}
.bc a:hover{color:var(--green)}
.bc .sep{opacity:0.4}

/* OFFER BOX */
.offer-box{background:var(--dark3);border:1px solid var(--border);border-radius:var(--radius);padding:32px;margin:32px 0;position:relative}
.offer-box.hot{border-color:var(--border2);box-shadow:0 0 60px rgba(0,179,134,0.06),inset 0 1px 0 rgba(0,179,134,0.1)}
.ob-badge{position:absolute;top:-14px;left:24px;background:var(--green);color:#fff;font-weight:800;font-size:0.7rem;letter-spacing:1px;padding:4px 14px;border-radius:20px;text-transform:uppercase}
.offer-box h3{font-size:1.25rem;font-weight:800;color:#fff;margin-bottom:14px}
.offer-box ul{list-style:none;margin-bottom:24px}
.offer-box ul li{padding:5px 0;font-size:0.96rem;color:rgba(232,245,240,0.85);display:flex;align-items:baseline;gap:8px}
.tc{font-size:0.72rem;color:var(--muted);margin-top:10px;line-height:1.5}

/* STARS */
.stars{color:var(--gold);letter-spacing:2px;font-size:0.9rem}
.score{font-size:1.6rem;font-weight:900;color:#fff;font-family:'Outfit',sans-serif}
.score-row{display:flex;align-items:center;gap:10px;margin-bottom:14px}
.score-sub{font-size:0.78rem;color:var(--muted)}

/* RANK CARDS */
.rank-grid{display:grid;gap:14px;margin:28px 0}
.rank-card{background:var(--dark3);border:1px solid var(--border);border-radius:var(--radius);padding:20px 24px;display:grid;grid-template-columns:48px 1fr auto;align-items:center;gap:18px;transition:all 0.2s}
.rank-card:hover{border-color:var(--border2);transform:translateX(3px)}
.rank-num{font-size:1.8rem;font-weight:900;color:rgba(0,179,134,0.2);text-align:center}
.rank-num.first{color:var(--green)}
.rank-info h4{font-weight:700;font-size:1rem;color:#fff;margin-bottom:3px}
.rank-info .deal{font-size:0.83rem;color:var(--green3);font-weight:600;margin-bottom:7px}
.rank-tags{display:flex;flex-wrap:wrap;gap:5px}
.rtag{background:rgba(0,179,134,0.07);border:1px solid var(--border);color:rgba(232,245,240,0.55);font-size:0.7rem;font-weight:600;padding:3px 9px;border-radius:20px}
@media(max-width:560px){.rank-card{grid-template-columns:1fr;gap:12px}.rank-num{display:none}}

/* CONTENT */
.cb h2{font-size:1.5rem;font-weight:800;color:#fff;margin:46px 0 14px;letter-spacing:-0.3px}
.cb h3{font-size:1.1rem;font-weight:700;color:rgba(232,245,240,0.9);margin:28px 0 10px}
.cb p{margin-bottom:18px;color:rgba(232,245,240,0.78);line-height:1.78}
.cb ul,.cb ol{padding-left:22px;margin-bottom:18px}
.cb li{margin-bottom:9px;color:rgba(232,245,240,0.75)}
.lead{font-size:1.08rem;line-height:1.8;color:rgba(232,245,240,0.9);border-left:3px solid var(--green);padding:3px 0 3px 18px;margin-bottom:30px}
.hl{background:rgba(0,179,134,0.07);border:1px solid var(--border2);border-radius:var(--radius);padding:20px 24px;margin:24px 0}
.hl strong{color:var(--green3)}
a.inline{color:var(--green3);text-decoration:none;border-bottom:1px solid rgba(0,179,134,0.3);transition:border-color 0.15s}
a.inline:hover{border-color:var(--green3)}

/* TABLE */
.dt{width:100%;border-collapse:collapse;font-size:0.9rem;margin:22px 0;overflow:hidden;border-radius:var(--radius)}
.dt th{background:rgba(0,179,134,0.1);color:rgba(232,245,240,0.9);font-weight:700;padding:13px 15px;text-align:left;border-bottom:1px solid var(--border2);font-size:0.82rem;letter-spacing:0.3px;text-transform:uppercase}
.dt td{padding:12px 15px;border-bottom:1px solid rgba(255,255,255,0.04);color:rgba(232,245,240,0.75)}
.dt tr:last-child td{border-bottom:none}
.dt tr:hover td{background:rgba(255,255,255,0.02)}
.badge-g{background:rgba(0,179,134,0.12);color:var(--green3);font-size:0.73rem;font-weight:700;padding:3px 9px;border-radius:20px}
.badge-r{background:rgba(231,76,60,0.12);color:#ff6b5b;font-size:0.73rem;font-weight:700;padding:3px 9px;border-radius:20px}
.badge-b{background:rgba(59,130,246,0.12);color:#60a5fa;font-size:0.73rem;font-weight:700;padding:3px 9px;border-radius:20px}

/* FAQ */
.faq{margin:44px 0}
.faq-title{font-size:1.5rem;font-weight:800;color:#fff;margin-bottom:22px;letter-spacing:-0.3px}
.fi{border-bottom:1px solid rgba(255,255,255,0.06);padding:18px 0}
.fi:last-child{border-bottom:none}
.fq{font-weight:700;font-size:1rem;color:rgba(232,245,240,0.9);cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:16px;user-select:none}
.fq::after{content:'+';font-size:1.5rem;color:var(--green);flex-shrink:0;transition:transform 0.2s;line-height:1}
.fi.open .fq::after{transform:rotate(45deg)}
.fa{display:none;padding-top:13px;color:rgba(232,245,240,0.65);font-size:0.95rem;line-height:1.75}
.fi.open .fa{display:block}

/* PAGE NAV */
.pnav{display:flex;flex-wrap:wrap;gap:7px;background:var(--dark2);border-radius:var(--radius);padding:16px;margin-bottom:40px;border:1px solid var(--border)}
.pnav a{background:rgba(0,179,134,0.06);border:1px solid var(--border);color:rgba(232,245,240,0.6);font-size:0.78rem;font-weight:600;padding:6px 13px;border-radius:6px;text-decoration:none;transition:all 0.15s;white-space:nowrap}
.pnav a:hover{background:rgba(0,179,134,0.14);color:#fff;border-color:var(--border2)}

/* STAT CARDS */
.stat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:16px;margin:28px 0}
.stat-card{background:var(--dark3);border:1px solid var(--border);border-radius:var(--radius);padding:20px;text-align:center}
.stat-card .num{font-size:2rem;font-weight:900;color:var(--green);font-family:'Outfit',sans-serif;line-height:1}
.stat-card .label{font-size:0.78rem;color:var(--muted);margin-top:6px;font-weight:600}

/* STICKY */
.sticky{display:none;position:fixed;bottom:0;left:0;right:0;background:linear-gradient(135deg,#021a12,#030d0a);border-top:1px solid var(--border2);padding:13px 20px;z-index:300;align-items:center;justify-content:space-between;gap:14px}
.sticky p{font-size:0.82rem;color:rgba(232,245,240,0.7);line-height:1.4}
.sticky p strong{color:#fff;display:block;font-size:0.9rem}
@media(max-width:768px){.sticky{display:flex}}

/* FOOTER */
footer{background:var(--dark2);border-top:1px solid var(--border);padding:48px 24px 32px;text-align:center;font-size:0.8rem;color:var(--muted)}
.flogo{font-family:'Outfit',sans-serif;font-size:1.35rem;font-weight:900;color:#fff;margin-bottom:12px;display:block}
.flogo em{color:var(--green);font-style:normal}
.flinks{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin:14px 0}
.flinks a{color:var(--muted);text-decoration:none;transition:color 0.15s}
.flinks a:hover{color:var(--green)}
.disc{margin-top:22px;max-width:680px;margin-left:auto;margin-right:auto;line-height:1.68;padding:18px;background:rgba(255,255,255,0.02);border-radius:10px;border:1px solid rgba(255,255,255,0.05);color:rgba(232,245,240,0.45)}
"""

JS = """
document.querySelectorAll('.fq').forEach(q=>{
  q.addEventListener('click',()=>{
    const fi=q.closest('.fi');
    const was=fi.classList.contains('open');
    document.querySelectorAll('.fi.open').forEach(i=>i.classList.remove('open'));
    if(!was)fi.classList.add('open');
  });
});
const sticky=document.querySelector('.sticky');
if(sticky){
  window.addEventListener('scroll',()=>{
    sticky.style.display=window.scrollY>500?'flex':'none';
  },{passive:true});
}
"""

NAV_LINKS = [
    ("How It Works","how-acorns-works.html"),
    ("Review","acorns-review.html"),
    ("vs Robinhood","acorns-vs-robinhood.html"),
    ("vs Stash","acorns-vs-stash.html"),
    ("Round-Ups","acorns-round-ups.html"),
    ("Acorns Later","acorns-later-ira.html"),
    ("Acorns Early","acorns-early.html"),
    ("Fees","acorns-fees.html"),
    ("Sign Up Guide","acorns-sign-up.html"),
    ("Promo Codes","acorns-promo-code.html"),
]

ALL_LINKS = NAV_LINKS + [
    ("Portfolios","acorns-portfolios.html"),
    ("For Beginners","acorns-for-beginners.html"),
    ("Earn Rewards","acorns-earn.html"),
    ("Tax Guide","acorns-tax-guide.html"),
    ("Withdraw Money","acorns-withdraw.html"),
    ("Is It Safe?","is-acorns-safe.html"),
    ("Acorns vs Betterment","acorns-vs-betterment.html"),
    ("Compound Interest","acorns-compound-interest.html"),
    ("Sitemap","sitemap.xml"),
]

def nav_html():
    links="".join(f'<a href="{h}">{l}</a>' for l,h in NAV_LINKS)
    return f"""<nav><div class="nav-inner">
  <a class="logo" href="index.html">Acorns<em>Guide</em></a>
  <div class="nav-links">{links}</div>
  <a class="nav-cta" href="{aff('nav')}" target="_blank" rel="noopener sponsored">🌱 Start Investing</a>
</div></nav>"""

def bc_html(crumbs):
    parts=[]
    for label,href in crumbs:
        if href:
            parts.append(f'<a href="{href}">{label}</a><span class="sep">›</span>')
        else:
            parts.append(f'<span style="color:rgba(232,245,240,0.8)">{label}</span>')
    return f'<div class="bc">{"".join(parts)}</div>'

def pnav_html():
    links="".join(f'<a href="{h}">{l}</a>' for l,h in NAV_LINKS)
    return f'<div class="pnav">{links}</div>'

def footer_html():
    fl="".join(f'<a href="{h}">{l}</a>' for l,h in ALL_LINKS)
    return f"""<footer>
  <span class="flogo">Acorns<em>Guide</em></span>
  <div class="flinks">{fl}</div>
  <div class="disc">
    <strong style="color:rgba(232,245,240,0.7);display:block;margin-bottom:6px">⚠️ Investment Disclaimer</strong>
    Investing involves risk, including possible loss of principal. AcornsGuide is an independent affiliate site — we earn commissions when you sign up via our links. Past performance does not guarantee future results. Not financial advice. Acorns is a registered investment advisor. Review all disclosures at acorns.com before investing.
  </div>
  <p style="margin-top:18px;opacity:0.35">© {date.today().year} AcornsGuide. All rights reserved.</p>
</footer>
<div class="sticky" style="display:none">
  <p><strong>🌱 Get $5 Free When You Sign Up</strong>Start investing your spare change today</p>
  <a href="{aff('sticky')}" class="cta sm pulse" target="_blank" rel="noopener sponsored">Get $5 Free</a>
</div>
<script>{JS}</script>"""

def faq_block(items):
    rows=""
    for q,a in items:
        rows+=f'<div class="fi"><div class="fq">{q}</div><div class="fa">{a}</div></div>'
    return f'<div class="faq"><div class="faq-title">Frequently Asked Questions</div>{rows}</div>'

def schema_faq(items):
    return {"@context":"https://schema.org","@type":"FAQPage",
            "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}

def schema_web(title,desc,url):
    return {"@context":"https://schema.org","@type":"WebPage","name":title,"description":desc,"url":url,
            "publisher":{"@type":"Organization","name":"AcornsGuide","url":BASE_URL},"inLanguage":"en-US"}

def schema_bc(crumbs):
    items=[]
    for i,(label,href) in enumerate(crumbs,1):
        url=f"{BASE_URL}/{href}" if href else BASE_URL
        items.append({"@type":"ListItem","position":i,"name":label,"item":url})
    return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":items}

def page(slug,title,desc,kw,h1,tag,hero_cta,body,faqs=None,crumbs=None):
    canon=f"{BASE_URL}/" if slug=="index" else f"{BASE_URL}/{slug}.html"
    schemas=[schema_web(title,desc,canon)]
    if crumbs: schemas.append(schema_bc(crumbs))
    if faqs:   schemas.append(schema_faq(faqs))
    sd="\n".join(f'<script type="application/ld+json">{_json.dumps(s,separators=(",",":"))}</script>' for s in schemas)
    crumb=bc_html(crumbs) if crumbs else ""
    faq=faq_block(faqs) if faqs else ""
    body2=body.replace("{A}",aff(slug))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="AcornsGuide">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
{sd}
<style>{CSS}</style>
</head>
<body>
<div class="ann-bar">🌱 New: Get a <strong>$5 bonus</strong> when you open your first Acorns account — <a href="{aff('ann')}">Claim Now →</a></div>
{nav_html()}
<div class="trust">
  <div class="trust-inner">
    <div class="ti"><span class="dot"></span> SEC Registered</div>
    <div class="ti"><span class="dot"></span> SIPC Protected</div>
    <div class="ti"><span class="dot"></span> 10M+ Investors</div>
    <div class="ti"><span class="dot"></span> Start with $5</div>
    <div class="ti"><span class="dot"></span> Updated {BUILT_ON}</div>
  </div>
</div>
<div class="hero">
  <div class="hero-tag">🌱 {tag}</div>
  <h1>{h1}</h1>
  <p class="sub">{desc}</p>
  <div class="hero-actions">
    <a href="{aff(slug+'-hero')}" class="cta pulse" target="_blank" rel="noopener sponsored">{hero_cta}</a>
    <a href="#content" class="btn-ghost">Read the Guide ↓</a>
  </div>
</div>
<div class="wrap" id="content">
  {crumb}
  {pnav_html()}
  {body2}
  {faq}
</div>
{footer_html()}
</body>
</html>"""

# ══════════════════════════════════════════════════════════════
# PAGES
# ══════════════════════════════════════════════════════════════
PAGES = []

# ── 1. INDEX ──────────────────────────────────────────────────
PAGES.append(dict(
slug="index",
title="Acorns Review 2026 — Is It Worth It? | AcornsGuide",
desc="The independent guide to Acorns investing in 2026. Real reviews, fee breakdowns, portfolio analysis, and the honest truth about whether Acorns is right for you.",
kw="acorns review 2026, acorns investing app, is acorns worth it, acorns micro investing",
h1="Acorns 2026 — <span>Is It Worth It?</span>",
tag="Independent Review · Updated 2026",
hero_cta="🌱 Start Investing with Acorns",
crumbs=[("Home",None)],
faqs=[
  ("Is Acorns legit and safe?","Yes — Acorns is an SEC-registered investment advisor and SIPC member, protecting accounts up to $500,000. It has over 10 million users and has been operating since 2014."),
  ("How much do you need to start with Acorns?","Just $5. Acorns requires a $5 minimum to start investing. You can set up automatic Round-Ups and recurring investments from day one."),
  ("Does Acorns actually make you money?","Acorns invests your money in diversified ETF portfolios. Returns depend on the market — historically 6–8% annually for balanced portfolios. It's a long-term wealth-building tool, not a get-rich-quick scheme."),
  ("What is Acorns Round-Up?","Round-Ups automatically round up your everyday purchases to the nearest dollar and invest the difference. Spend $3.60 on coffee and $0.40 gets invested automatically."),
  ("How much does Acorns cost?","Acorns Personal costs $3/month. Acorns Premium costs $5/month. There's no fee to open an account — charges start when you begin investing."),
],
body="""
<section class="cb">
  <p class="lead">Acorns has turned micro-investing into a mainstream habit for over 10 million Americans. But is the $3/month fee worth it for your situation? This guide gives you the unvarnished truth — features, fees, returns, and who it's actually best for.</p>

  <div class="stat-grid">
    <div class="stat-card"><div class="num">10M+</div><div class="label">Active Investors</div></div>
    <div class="stat-card"><div class="num">$5</div><div class="label">Minimum to Start</div></div>
    <div class="stat-card"><div class="num">$3/mo</div><div class="label">Personal Plan</div></div>
    <div class="stat-card"><div class="num">2014</div><div class="label">Founded</div></div>
    <div class="stat-card"><div class="num">SEC</div><div class="label">Registered RIA</div></div>
    <div class="stat-card"><div class="num">SIPC</div><div class="label">$500K Protected</div></div>
  </div>

  <h2>AcornsGuide Verdict — 2026</h2>
  <div class="rank-grid">
    <div class="rank-card">
      <div class="rank-num first">★</div>
      <div class="rank-info">
        <h4>Best For: Beginner investors who struggle to save</h4>
        <div class="deal">Round-Ups + automatic investing = effortless wealth building</div>
        <div class="score-row"><span class="stars">★★★★☆</span><span class="score">8.7</span><span class="score-sub">/ 10 — Recommended</span></div>
        <div class="rank-tags"><span class="rtag">Beginner Friendly</span><span class="rtag">Fully Automated</span><span class="rtag">ETF Portfolios</span><span class="rtag">IRA Available</span></div>
      </div>
      <a href="{A}" class="cta pulse sm" target="_blank" rel="noopener sponsored">Start Free</a>
    </div>
  </div>

  <h2>What Acorns Actually Does</h2>
  <p>Acorns is a micro-investing app that makes investing automatic and painless. Instead of requiring you to manually buy stocks or research ETFs, it does everything for you in three ways:</p>
  <ul>
    <li><strong>Round-Ups</strong> — links to your debit/credit card and rounds every purchase up to the nearest dollar, investing the difference automatically</li>
    <li><strong>Recurring investments</strong> — set a fixed daily, weekly, or monthly investment that pulls from your bank automatically</li>
    <li><strong>Acorns Earn</strong> — shop at partner brands and earn bonus investments (essentially cashback that goes straight into your portfolio)</li>
  </ul>
  <p>The money goes into one of five pre-built portfolios ranging from Conservative to Aggressive — all made up of low-cost Vanguard and iShares ETFs.</p>

  <h2>Acorns Plans — What You Get</h2>
  <table class="dt">
    <thead><tr><th>Plan</th><th>Cost</th><th>Includes</th><th>Best For</th></tr></thead>
    <tbody>
      <tr><td><strong>Acorns Personal</strong></td><td>$3/month</td><td>Invest + Checking + Emergency Fund</td><td>Most users</td></tr>
      <tr><td><strong>Acorns Premium</strong></td><td>$5/month</td><td>Everything + Acorns Early (kids) + IRA matching + Live Q&A</td><td>Families</td></tr>
    </tbody>
  </table>

  <h2>Who Should Use Acorns</h2>
  <h3>✅ Acorns IS right for you if:</h3>
  <ul>
    <li>You're a beginner who wants to start investing without learning the stock market</li>
    <li>You struggle to save consistently and want automation to do the heavy lifting</li>
    <li>You want a set-it-and-forget-it approach to long-term wealth building</li>
    <li>You're investing under $10,000 (the $3/month fee is proportionally reasonable)</li>
  </ul>
  <h3>❌ Acorns is NOT right for you if:</h3>
  <ul>
    <li>You have $50,000+ to invest (the $36/year fee becomes significant vs 0.03% ETF alternatives)</li>
    <li>You want to pick your own stocks or ETFs</li>
    <li>You need tax-loss harvesting or advanced portfolio features</li>
    <li>You're an experienced investor comfortable with Vanguard or Fidelity directly</li>
  </ul>

  <div class="hl">
    <strong>💡 Our Take:</strong> For someone who currently invests $0/month, Acorns' $3 fee is a bargain — it creates the habit that builds wealth over decades. For someone already maxing a 401(k) and Roth IRA at Vanguard, the fee is unnecessary overhead. Know which camp you're in.
  </div>

  <h2>Get Started — Step by Step</h2>
  <ol>
    <li>Click our link below to open your account (takes 5 minutes)</li>
    <li>Connect your bank account and debit/credit card</li>
    <li>Choose your portfolio (we recommend Moderate for most beginners)</li>
    <li>Set up a recurring investment ($5–$50/week is a great start)</li>
    <li>Enable Round-Ups and let the automation run</li>
  </ol>
  <a href="{A}" class="cta pulse" target="_blank" rel="noopener sponsored">🌱 Open Your Acorns Account — 5 Minutes</a>
  <p class="tc" style="margin-top:10px">Investing involves risk. Past performance does not guarantee future results. $3/month fee applies after account opening.</p>
</section>
"""
))

# ── 2. HOW IT WORKS ───────────────────────────────────────────
PAGES.append(dict(
slug="how-acorns-works",
title="How Acorns Works 2026 — Round-Ups, Portfolios & Auto-Investing Explained",
desc="Complete guide to how Acorns works in 2026. Round-Ups, recurring investments, ETF portfolios, and how your spare change actually grows into real wealth.",
kw="how acorns works, acorns round ups explained, acorns investing explained 2026",
h1="How Acorns Works — <span>Complete 2026 Guide</span>",
tag="Explained Simply · Step by Step",
hero_cta="🌱 Try Acorns Free",
crumbs=[("Home","index.html"),("How It Works",None)],
faqs=[
  ("How do Round-Ups work exactly?","Acorns links to your spending accounts and monitors every transaction. When you spend $4.25 on coffee, Acorns rounds to $5.00 and queues $0.75 for investment. Round-Ups batch together and invest once they total $5."),
  ("How does Acorns choose my investments?","Acorns asks about your age, income, investment goals, and risk tolerance during setup. Based on your answers it recommends one of five portfolios (Conservative to Aggressive), each built from low-cost ETFs."),
  ("Can I change my portfolio after signing up?","Yes — you can switch portfolios anytime in the app. Acorns will rebalance your existing holdings into the new allocation at no extra charge."),
  ("How often does Acorns invest my money?","Round-Up investments are batched and invested when they reach $5. Recurring investments go in on your chosen schedule. The market processes investments on business days."),
],
body="""
<section class="cb">
  <p class="lead">Acorns works by making investing invisible — it happens automatically in the background of your everyday spending. Understanding the mechanics helps you get maximum value from every feature the app offers.</p>

  <div class="offer-box hot">
    <div class="ob-badge">🌱 Start Today</div>
    <h3>Open an Acorns Account in 5 Minutes</h3>
    <ul>
      <li>✅ $5 minimum to start investing</li>
      <li>✅ Round-Ups start working immediately after linking your card</li>
      <li>✅ First month free for new accounts</li>
      <li>✅ Available on iOS and Android</li>
    </ul>
    <a href="{A}" class="cta pulse" target="_blank" rel="noopener sponsored">🌱 Start Investing Now</a>
    <p class="tc">Investing involves risk. $3/month after first month. T&Cs apply.</p>
  </div>

  <h2>The 3 Ways Acorns Grows Your Money</h2>

  <h3>1. Round-Ups — Invest Your Spare Change</h3>
  <p>Link any debit or credit card to Acorns. Every time you make a purchase, Acorns rounds the amount up to the nearest dollar and queues the difference for investment. Spend $47.60 at the grocery store and $0.40 gets added to your investment queue.</p>
  <p>Round-Ups accumulate until they reach $5, then invest automatically. Most users invest $30–$50/month through Round-Ups alone without noticing the money leaving their account.</p>
  <p>You can also enable <strong>Multipliers</strong> — set Round-Ups to invest 2×, 3×, or 10× the rounded amount for faster growth.</p>

  <h3>2. Recurring Investments — Consistent Habit Building</h3>
  <p>Set a fixed amount to invest daily ($1–$5), weekly ($5–$100), or monthly ($10–$500). This money transfers automatically from your bank to your Acorns portfolio on schedule.</p>
  <p>Recurring investments are the single most powerful tool in the app. A $50/week recurring investment over 20 years at 7% average annual return grows to approximately <strong>$109,000</strong> — turning a $52,000 total contribution into over double through compound growth.</p>

  <h3>3. Acorns Earn — Bonus Investments From Shopping</h3>
  <p>Shop at 450+ partner brands (Apple, Walmart, Nike, Airbnb, and more) through the Acorns app or the browser extension, and receive bonus investments credited to your account — essentially cashback that goes directly into your portfolio.</p>

  <h2>Your Acorns Portfolio — How It's Built</h2>
  <p>Acorns invests your money in a portfolio of low-cost ETFs (Exchange-Traded Funds) from Vanguard and iShares. ETFs are baskets of stocks/bonds that give you instant diversification across hundreds or thousands of companies.</p>
  <table class="dt">
    <thead><tr><th>Portfolio</th><th>Stock/Bond Split</th><th>Risk Level</th><th>Best For</th></tr></thead>
    <tbody>
      <tr><td>Conservative</td><td>20% / 80%</td><td>Low</td><td>Short time horizon, risk-averse</td></tr>
      <tr><td>Moderately Conservative</td><td>40% / 60%</td><td>Low-Med</td><td>5–10 year horizon</td></tr>
      <tr><td>Moderate</td><td>60% / 40%</td><td>Medium</td><td>10+ year horizon, most beginners</td></tr>
      <tr><td>Moderately Aggressive</td><td>80% / 20%</td><td>Med-High</td><td>Long horizon, higher growth goal</td></tr>
      <tr><td>Aggressive</td><td>100% / 0%</td><td>High</td><td>20+ year horizon, max growth</td></tr>
    </tbody>
  </table>

  <h2>How Compound Growth Makes Small Investments Big</h2>
  <p>The reason Acorns works for long-term wealth building is compound interest — earning returns on your returns. Small consistent investments snowball dramatically over time:</p>
  <table class="dt">
    <thead><tr><th>Monthly Investment</th><th>After 10 Years</th><th>After 20 Years</th><th>After 30 Years</th></tr></thead>
    <tbody>
      <tr><td>$25/month</td><td>$4,300</td><td>$12,200</td><td>$28,300</td></tr>
      <tr><td>$50/month</td><td>$8,600</td><td>$24,400</td><td>$56,600</td></tr>
      <tr><td>$100/month</td><td>$17,200</td><td>$48,800</td><td>$113,100</td></tr>
      <tr><td>$200/month</td><td>$34,400</td><td>$97,700</td><td>$226,200</td></tr>
    </tbody>
  </table>
  <p style="font-size:0.82rem;color:var(--muted)">Assumes 7% average annual return. For illustrative purposes only. Actual returns will vary.</p>
</section>
"""
))

# ── 3. ACORNS REVIEW ──────────────────────────────────────────
PAGES.append(dict(
slug="acorns-review",
title="Acorns App Review 2026 — Pros, Cons, Fees & Is It Worth It?",
desc="Honest Acorns app review for 2026. We break down every feature, fee, portfolio option, and compare it to alternatives so you can decide if Acorns is right for you.",
kw="acorns app review 2026, acorns pros cons, acorns review honest, acorns worth it 2026",
h1="Acorns App Review 2026 — <span>Honest Pros, Cons & Verdict</span>",
tag="Full Review · Unbiased · 2026",
hero_cta="🌱 Try Acorns Today",
crumbs=[("Home","index.html"),("Acorns Review",None)],
faqs=[
  ("What is Acorns' overall rating?","AcornsGuide rates Acorns 8.7/10 for beginner investors. It scores high on automation, ease of use, and habit formation. It scores lower on fee efficiency for large balances and lack of individual stock picking."),
  ("Is Acorns good for long-term investing?","Yes for building the habit. The automated portfolios are properly diversified with low-cost ETFs. The $3/month fee becomes less proportionally significant as your balance grows. Once you exceed $50,000 you should evaluate if a fee-free option like Fidelity makes more sense."),
  ("Can Acorns make you rich?","Not quickly — but consistent micro-investing over 20–30 years with compound returns can genuinely build significant wealth. A $50/month investor over 30 years at 7% average return accumulates over $56,000."),
  ("Does Acorns have a free trial?","Acorns typically offers the first month free for new accounts. Our affiliate link may include a bonus investment offer on top of the free trial — check the landing page for current promotions."),
],
body="""
<section class="cb">
  <p class="lead">We've used Acorns, analyzed its portfolios, calculated its real fee impact at different balance levels, and compared it head-to-head against every major competitor. Here's everything you need to make an informed decision.</p>

  <div class="score-row" style="margin-bottom:8px"><span class="stars">★★★★☆</span><span class="score" style="font-size:2.5rem">8.7</span><span class="score-sub" style="font-size:1rem">/ 10 — AcornsGuide Rating</span></div>
  <p style="color:var(--muted);margin-bottom:32px;font-size:0.88rem">Rated across: Ease of use, fee value, portfolio quality, features, customer support</p>

  <h2>Acorns Pros — What It Does Well</h2>
  <ul>
    <li><strong>Genuinely beginner-friendly</strong> — the onboarding is the best in the industry; you can go from zero to invested in under 10 minutes</li>
    <li><strong>Round-Ups are magic for non-savers</strong> — investing spare change is psychologically painless in a way manual transfers never are</li>
    <li><strong>Well-constructed portfolios</strong> — the ETFs are from Vanguard and iShares; low expense ratios (0.03–0.18%) and proper diversification</li>
    <li><strong>Acorns Later IRA</strong> — having a retirement account in the same app as your taxable account makes goal-based saving intuitive</li>
    <li><strong>Acorns Earn</strong> — bonus investments from 450+ partner brands add free money to your portfolio just from normal shopping</li>
    <li><strong>Found Money</strong> — automatic bonus investments when you shop at partner brands without any extra steps</li>
    <li><strong>SIPC protection</strong> — your investments are protected up to $500,000</li>
  </ul>

  <h2>Acorns Cons — Where It Falls Short</h2>
  <ul>
    <li><strong>Fee efficiency drops with larger balances</strong> — $3/month = $36/year. On a $1,000 balance that's 3.6% — higher than most ETF expense ratios. On $10,000 it's 0.36%, which is reasonable. On $100,000 it's 0.036%, negligible.</li>
    <li><strong>No individual stock picking</strong> — you can't buy Apple, Tesla, or individual ETFs. You're locked into Acorns' five preset portfolios</li>
    <li><strong>No tax-loss harvesting</strong> — Betterment and Wealthfront offer this feature that can save hundreds in taxes annually</li>
    <li><strong>Limited portfolio customization</strong> — five portfolios is simple but may not match sophisticated investors' needs</li>
    <li><strong>Customer support can be slow</strong> — email-based support with response times of 24–48 hours; no phone support</li>
  </ul>

  <h2>Fee Impact at Different Balance Levels</h2>
  <table class="dt">
    <thead><tr><th>Balance</th><th>Annual Fee</th><th>Fee as % of Balance</th><th>Verdict</th></tr></thead>
    <tbody>
      <tr><td>$500</td><td>$36</td><td>7.2%</td><td><span class="badge-r">Too Expensive</span></td></tr>
      <tr><td>$1,000</td><td>$36</td><td>3.6%</td><td><span class="badge-r">High</span></td></tr>
      <tr><td>$5,000</td><td>$36</td><td>0.72%</td><td>Acceptable</td></tr>
      <tr><td>$10,000</td><td>$36</td><td>0.36%</td><td><span class="badge-g">Good</span></td></tr>
      <tr><td>$25,000</td><td>$36</td><td>0.14%</td><td><span class="badge-g">Very Good</span></td></tr>
      <tr><td>$50,000+</td><td>$36</td><td>0.07%</td><td><span class="badge-g">Excellent</span></td></tr>
    </tbody>
  </table>

  <h2>Final Verdict</h2>
  <p>Acorns is the best investment app for people who don't currently invest. The automation removes the biggest barrier — remembering to invest consistently. The portfolios are sound. The Round-Ups feature genuinely works to build the habit of investing.</p>
  <p>If you're choosing between Acorns and doing nothing, choose Acorns every time. If you're choosing between Acorns and a Vanguard account with a $50,000+ balance, consider going direct.</p>

  <a href="{A}" class="cta pulse" target="_blank" rel="noopener sponsored">🌱 Open Your Acorns Account</a>
  <p class="tc" style="margin-top:10px">Investing involves risk. $3/month fee. T&Cs apply at acorns.com.</p>
</section>
"""
))

# ── 4. ACORNS VS ROBINHOOD ────────────────────────────────────
PAGES.append(dict(
slug="acorns-vs-robinhood",
title="Acorns vs Robinhood 2026 — Which Is Better for Beginners?",
desc="Acorns vs Robinhood compared for 2026. Features, fees, investment options, and which app is better for your specific financial goals and experience level.",
kw="acorns vs robinhood 2026, acorns or robinhood, robinhood vs acorns comparison",
h1="Acorns vs Robinhood 2026 — <span>Which Should You Choose?</span>",
tag="Head-to-Head Comparison · 2026",
hero_cta="🌱 Try Acorns Free",
crumbs=[("Home","index.html"),("Acorns vs Robinhood",None)],
faqs=[
  ("Is Acorns or Robinhood better for beginners?","Acorns is better for absolute beginners — it requires no investment knowledge, automates everything, and protects you from impulsive trading. Robinhood requires you to pick your own investments, which most beginners aren't equipped to do profitably."),
  ("Does Robinhood charge fees?","Robinhood's basic account is free with no commissions. Robinhood Gold costs $5/month and adds margin investing and premium research. Acorns costs $3/month for its Personal plan."),
  ("Can I lose money with both apps?","Yes — both invest in market securities. Your portfolio value can decrease. Robinhood has higher loss risk because users often trade individual stocks and options, which are more volatile than Acorns' diversified ETF portfolios."),
  ("Which app is better for long-term retirement saving?","Acorns — it has a built-in IRA (Acorns Later) and its automated portfolio approach is better suited to long-term passive investing. Robinhood users tend to trade more actively, which research shows produces worse long-term returns."),
],
body="""
<section class="cb">
  <p class="lead">Acorns and Robinhood are both popular investing apps — but they serve completely different investor profiles. Choosing the wrong one for your situation can cost you years of returns. Here's the definitive comparison.</p>

  <h2>Side-by-Side Comparison</h2>
  <table class="dt">
    <thead><tr><th>Feature</th><th>Acorns</th><th>Robinhood</th></tr></thead>
    <tbody>
      <tr><td>Monthly fee</td><td>$3–$5/month</td><td><span class="badge-g">$0 (basic)</span></td></tr>
      <tr><td>Investment type</td><td>Pre-built ETF portfolios</td><td>Stocks, ETFs, options, crypto</td></tr>
      <tr><td>Automation</td><td><span class="badge-g">Fully automated</span></td><td>Manual — you pick everything</td></tr>
      <tr><td>Round-Ups</td><td><span class="badge-g">Yes — unique feature</span></td><td>No</td></tr>
      <tr><td>Minimum investment</td><td>$5</td><td><span class="badge-g">$1 (fractional shares)</span></td></tr>
      <tr><td>Retirement account (IRA)</td><td><span class="badge-g">Yes — Acorns Later</span></td><td>Yes — Robinhood IRA</td></tr>
      <tr><td>Stock picking</td><td>No</td><td><span class="badge-g">Yes — full market access</span></td></tr>
      <tr><td>Options trading</td><td>No</td><td>Yes (risky)</td></tr>
      <tr><td>Crypto</td><td>No</td><td>Yes</td></tr>
      <tr><td>SIPC protection</td><td><span class="badge-g">Yes</span></td><td><span class="badge-g">Yes</span></td></tr>
      <tr><td>Best for</td><td><span class="badge-g">Passive, hands-off investors</span></td><td>Active traders, stock pickers</td></tr>
    </tbody>
  </table>

  <h2>The Core Difference — Philosophy</h2>
  <p><strong>Acorns</strong> is built on the belief that most people build more wealth through consistent automated investing than through active stock picking. It removes decisions from the equation entirely.</p>
  <p><strong>Robinhood</strong> is built on the belief that everyone deserves access to the stock market. It gives you full control — which is powerful for experienced investors and dangerous for beginners who tend to overtrade.</p>

  <h2>Performance Reality — What Research Shows</h2>
  <p>Studies consistently show that the average retail investor on trading platforms like Robinhood underperforms the S&P 500 by 3–6% annually due to timing mistakes and overtrading. Acorns' automatic, diversified approach historically tracks close to market returns.</p>

  <div class="hl">
    <strong>💡 Our Recommendation:</strong> If you're starting from zero and want to build a long-term investment habit, start with Acorns. Once you have $10,000+ invested and genuinely want to learn active investing, you can add Robinhood alongside it. Don't replace Acorns — augment it.
  </div>

  <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Start with Acorns — Better for Beginners</a>
  <p class="tc" style="margin-top:10px">Investing involves risk. Acorns $3/month fee applies.</p>
</section>
"""
))

# ── 5. ACORNS VS STASH ────────────────────────────────────────
PAGES.append(dict(
slug="acorns-vs-stash",
title="Acorns vs Stash 2026 — Which Micro-Investing App Wins?",
desc="Acorns vs Stash compared for 2026. Both are micro-investing apps but with very different approaches. Find out which one is right for your goals and budget.",
kw="acorns vs stash 2026, stash vs acorns comparison, best micro investing app 2026",
h1="Acorns vs Stash 2026 — <span>Which Micro-Investing App Wins?</span>",
tag="App Comparison · Micro-Investing · 2026",
hero_cta="🌱 Choose Acorns",
crumbs=[("Home","index.html"),("Acorns vs Stash",None)],
faqs=[
  ("What is the difference between Acorns and Stash?","Acorns is fully automated — it invests for you via Round-Ups and recurring investments. Stash requires you to choose your own investments from a curated selection, giving more control but requiring more involvement."),
  ("Which app has lower fees?","Both charge $3/month for their base plans. Stash's $3/month includes a bank account and debit card. Acorns' $3/month includes investing, checking, and emergency fund features."),
  ("Is Stash better than Acorns for beginners?","Acorns is simpler for true beginners — there are no investment decisions to make. Stash is better for beginners who want to learn how to pick investments with training wheels."),
  ("Can I use both Acorns and Stash?","Yes, but it's probably not necessary. Pick the one that matches your style — automated (Acorns) or semi-active (Stash)."),
],
body="""
<section class="cb">
  <p class="lead">Acorns and Stash are both built for beginner investors who want to start small. But they take fundamentally different approaches — one automates everything, the other teaches you to choose. Here's which one deserves your $3/month.</p>

  <h2>Acorns vs Stash — Full Comparison</h2>
  <table class="dt">
    <thead><tr><th>Feature</th><th>Acorns</th><th>Stash</th></tr></thead>
    <tbody>
      <tr><td>Monthly fee (basic)</td><td>$3/month</td><td>$3/month</td></tr>
      <tr><td>Investment approach</td><td><span class="badge-g">Fully automated</span></td><td>User-selected from curated list</td></tr>
      <tr><td>Round-Ups</td><td><span class="badge-g">Yes</span></td><td>Yes (Stock-Back® rewards instead)</td></tr>
      <tr><td>Portfolio customization</td><td>5 preset portfolios</td><td><span class="badge-g">200+ ETFs and stocks to choose from</span></td></tr>
      <tr><td>Educational content</td><td>Basic</td><td><span class="badge-g">Strong — built into investment choices</span></td></tr>
      <tr><td>IRA/retirement</td><td><span class="badge-g">Yes — Acorns Later</span></td><td>Yes — Stash Retire</td></tr>
      <tr><td>Debit card with rewards</td><td>Yes (Acorns checking)</td><td><span class="badge-g">Yes — Stock-Back® debit card</span></td></tr>
      <tr><td>Minimum investment</td><td>$5</td><td><span class="badge-g">$0.01</span></td></tr>
      <tr><td>Best for</td><td><span class="badge-g">Completely hands-off investors</span></td><td>Beginners who want to learn</td></tr>
    </tbody>
  </table>

  <h2>Acorns Wins When:</h2>
  <ul>
    <li>You want zero investment decisions — just set it up and let it run</li>
    <li>The Round-Up mechanic resonates with you (spending-based investing)</li>
    <li>You want the simplest possible path to a diversified portfolio</li>
    <li>You prefer expert-built portfolios over choosing your own ETFs</li>
  </ul>

  <h2>Stash Wins When:</h2>
  <ul>
    <li>You want to learn how to invest, not just hand money over to an algorithm</li>
    <li>You want to hold specific ETFs or individual stocks you believe in</li>
    <li>You want the Stock-Back® debit card that earns fractional shares at partner stores</li>
    <li>You're building toward eventually managing your own portfolio</li>
  </ul>

  <div class="hl">
    <strong>💡 Bottom Line:</strong> For most people who simply want to build wealth without thinking about it, Acorns wins. Its fully automated approach produces more consistent results than semi-active investing for most beginners. If you enjoy learning about investing and want involvement, try Stash.
  </div>

  <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Open Acorns — Fully Automated</a>
  <p class="tc" style="margin-top:10px">Investing involves risk. $3/month. T&Cs apply.</p>
</section>
"""
))

# ── 6. ROUND-UPS ──────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-round-ups",
title="Acorns Round-Ups 2026 — How Spare Change Investing Really Works",
desc="Everything you need to know about Acorns Round-Ups in 2026. How they work, how much you'll actually invest, multipliers, and how to maximize your spare change.",
kw="acorns round ups, spare change investing, acorns round ups how it works 2026",
h1="Acorns Round-Ups — <span>How Spare Change Becomes Real Wealth</span>",
tag="Round-Ups Explained · Maximize Your Spare Change",
hero_cta="🌱 Start Round-Ups Now",
crumbs=[("Home","index.html"),("Round-Ups",None)],
faqs=[
  ("How much do most people invest through Round-Ups?","The average Acorns user invests $30–$50/month through Round-Ups alone, depending on how much they spend daily. High spenders can easily hit $100+/month."),
  ("Can I turn Round-Ups off?","Yes — Round-Ups can be paused or disabled anytime in the app settings without affecting your account or recurring investments."),
  ("What cards can I link to Acorns Round-Ups?","Any Visa, Mastercard, American Express, or Discover debit or credit card can be linked. The more cards you link, the more Round-Up opportunities you capture."),
  ("What are Round-Up Multipliers?","Multipliers let you invest 2×, 3×, or 10× the actual rounded-up amount. A $0.40 Round-Up with a 10× multiplier invests $4.00 instead — dramatically accelerating your investing pace."),
],
body="""
<section class="cb">
  <p class="lead">Acorns Round-Ups are the feature that made micro-investing mainstream. The psychology is brilliant: investing spare change doesn't feel like saving, so you don't resist it. But those tiny amounts add up to real money over time.</p>

  <div class="offer-box hot">
    <div class="ob-badge">🌱 Activate Round-Ups</div>
    <h3>Start Investing Your Spare Change Today</h3>
    <ul>
      <li>✅ Link any debit or credit card</li>
      <li>✅ Round-Ups start working immediately</li>
      <li>✅ Average user invests $30–$50/month automatically</li>
      <li>✅ Pause or adjust anytime</li>
    </ul>
    <a href="{A}" class="cta pulse" target="_blank" rel="noopener sponsored">🌱 Enable Round-Ups</a>
    <p class="tc">Investing involves risk. $3/month fee applies.</p>
  </div>

  <h2>Real Round-Up Examples — What Your Spending Generates</h2>
  <table class="dt">
    <thead><tr><th>Purchase Amount</th><th>Rounded To</th><th>Round-Up Amount</th></tr></thead>
    <tbody>
      <tr><td>$3.60 (coffee)</td><td>$4.00</td><td>$0.40</td></tr>
      <tr><td>$12.45 (lunch)</td><td>$13.00</td><td>$0.55</td></tr>
      <tr><td>$47.82 (groceries)</td><td>$48.00</td><td>$0.18</td></tr>
      <tr><td>$8.99 (streaming)</td><td>$9.00</td><td>$0.01</td></tr>
      <tr><td>$63.20 (gas)</td><td>$64.00</td><td>$0.80</td></tr>
      <tr><td>$127.43 (dinner out)</td><td>$128.00</td><td>$0.57</td></tr>
    </tbody>
  </table>
  <p>A typical person making 10–15 transactions per day generates $1–$3 in Round-Ups daily — or $30–$90/month invested without lifting a finger.</p>

  <h2>Round-Up Multipliers — 10× Your Investment Speed</h2>
  <p>Multipliers are the most underused feature in Acorns. Instead of investing $0.40 when you round up, a 10× multiplier invests $4.00. You barely notice the difference in your daily spending but the compound effect over years is dramatic.</p>
  <table class="dt">
    <thead><tr><th>Multiplier</th><th>$0.40 Round-Up Becomes</th><th>Monthly Impact (avg user)</th><th>10-Year Growth (7%)</th></tr></thead>
    <tbody>
      <tr><td>1× (standard)</td><td>$0.40</td><td>~$35/month</td><td>~$6,000</td></tr>
      <tr><td>2×</td><td>$0.80</td><td>~$70/month</td><td>~$12,000</td></tr>
      <tr><td>3×</td><td>$1.20</td><td>~$105/month</td><td>~$18,000</td></tr>
      <tr><td>10×</td><td>$4.00</td><td>~$350/month</td><td>~$60,000</td></tr>
    </tbody>
  </table>

  <h2>How to Maximize Your Round-Ups</h2>
  <ol>
    <li><strong>Link every card you own</strong> — debit cards, credit cards, all of them. More transactions = more Round-Ups</li>
    <li><strong>Use a multiplier</strong> — start with 2× and work up as you get comfortable</li>
    <li><strong>Don't track it obsessively</strong> — the magic of Round-Ups is that you stop noticing the money leaving. Checking daily creates friction</li>
    <li><strong>Add a recurring investment on top</strong> — Round-Ups alone won't build significant wealth. Combine with $50–$100/week recurring investment for real results</li>
  </ol>
</section>
"""
))

# ── 7. ACORNS LATER (IRA) ─────────────────────────────────────
PAGES.append(dict(
slug="acorns-later-ira",
title="Acorns Later IRA 2026 — Retirement Investing Made Simple",
desc="Complete guide to Acorns Later in 2026. How the IRA works, Traditional vs Roth options, contribution limits, and why adding retirement investing to Acorns is a no-brainer.",
kw="acorns later ira 2026, acorns retirement account, acorns roth ira, acorns later review",
h1="Acorns Later — <span>Retirement Investing on Autopilot</span>",
tag="IRA Guide · Traditional & Roth · 2026",
hero_cta="🌱 Open Acorns Later IRA",
crumbs=[("Home","index.html"),("Acorns Later IRA",None)],
faqs=[
  ("What is Acorns Later?","Acorns Later is the IRA (Individual Retirement Account) component of Acorns. It lets you invest for retirement with the same automated approach — Round-Ups and recurring investments — with the added benefit of tax advantages."),
  ("Traditional vs Roth IRA — which should I choose on Acorns Later?","Acorns recommends based on your income, age, and tax situation. General rule: choose Roth IRA if you're younger or in a lower tax bracket now (pay taxes now, withdraw tax-free in retirement). Choose Traditional IRA if you're in a higher tax bracket now (deduct now, pay taxes later)."),
  ("What are the 2025 IRA contribution limits?","$7,000/year for people under 50. $8,000/year for people 50 and over (includes $1,000 catch-up contribution). These limits apply across all your IRAs combined."),
  ("Does Acorns Later have fees?","Acorns Later is included in the $3/month Personal plan — no extra fee for the IRA. The $3/month covers both your taxable investment account and your IRA."),
],
body="""
<section class="cb">
  <p class="lead">Most Americans are behind on retirement savings. Acorns Later makes it automatic — using the same Round-Ups and recurring investments you already have set up, but routing money into a tax-advantaged retirement account instead of (or alongside) a taxable account.</p>

  <div class="offer-box hot">
    <div class="ob-badge">🌱 Retire Smarter</div>
    <h3>Open Acorns Later — IRA in Minutes</h3>
    <ul>
      <li>✅ Traditional IRA, Roth IRA, or SEP IRA available</li>
      <li>✅ Included in $3/month Personal plan — no extra fee</li>
      <li>✅ Automated contributions via Round-Ups</li>
      <li>✅ Tax-advantaged growth</li>
      <li>✅ Contribute up to $7,000/year (2026 limit)</li>
    </ul>
    <a href="{A}" class="cta pulse" target="_blank" rel="noopener sponsored">🌱 Open Acorns Later</a>
    <p class="tc">Investing involves risk. IRA rules and contribution limits apply. Consult a tax advisor.</p>
  </div>

  <h2>Traditional IRA vs Roth IRA on Acorns Later</h2>
  <table class="dt">
    <thead><tr><th>Feature</th><th>Traditional IRA</th><th>Roth IRA</th></tr></thead>
    <tbody>
      <tr><td>Tax treatment now</td><td><span class="badge-g">Contributions may be deductible</span></td><td>No deduction — after-tax money</td></tr>
      <tr><td>Tax treatment in retirement</td><td>Withdrawals taxed as income</td><td><span class="badge-g">Withdrawals tax-free</span></td></tr>
      <tr><td>Best if you expect</td><td>Lower tax rate in retirement</td><td><span class="badge-g">Higher tax rate in retirement</span></td></tr>
      <tr><td>Early withdrawal penalty</td><td>10% before age 59½ + taxes</td><td>Contributions can be withdrawn penalty-free; earnings have penalties</td></tr>
      <tr><td>Required minimum distributions</td><td>Yes — must start at age 73</td><td><span class="badge-g">No RMDs during your lifetime</span></td></tr>
      <tr><td>2026 contribution limit</td><td>$7,000 ($8,000 if 50+)</td><td>$7,000 ($8,000 if 50+)</td></tr>
    </tbody>
  </table>

  <h2>Why an IRA Matters — The Tax Math</h2>
  <p>Without a tax-advantaged account, every dollar your investments earn is taxed annually. Inside a Roth IRA, growth is completely tax-free — meaning you keep every dollar of compound interest.</p>
  <p>A $500/month investor over 30 years at 7% return:</p>
  <ul>
    <li><strong>Taxable account</strong> (assuming 20% annual capital gains): ~$520,000 after taxes</li>
    <li><strong>Roth IRA</strong> (zero tax on growth): ~$567,000 — $47,000 more for the same contributions</li>
  </ul>

  <h2>SEP IRA — For Self-Employed and Freelancers</h2>
  <p>Acorns Later also offers a SEP IRA for self-employed individuals, freelancers, and small business owners. The 2025 SEP IRA contribution limit is up to 25% of compensation or $69,000, whichever is less — dramatically higher than the standard IRA limit.</p>
</section>
"""
))

# ── 8. ACORNS EARLY ───────────────────────────────────────────
PAGES.append(dict(
slug="acorns-early",
title="Acorns Early 2026 — Invest for Your Kids' Future",
desc="Guide to Acorns Early in 2026 — the UTMA/UGMA custodial investment account for children. Set up investing for your kids in minutes with automatic contributions.",
kw="acorns early 2026, acorns kids account, acorns custodial account, invest for children acorns",
h1="Acorns Early — <span>Start Investing for Your Kids Today</span>",
tag="Kids Investing · UTMA/UGMA · 2026",
hero_cta="🌱 Open Acorns Early",
crumbs=[("Home","index.html"),("Acorns Early",None)],
faqs=[
  ("What is Acorns Early?","Acorns Early is a custodial investment account (UTMA/UGMA) for minors. Parents or guardians open and manage the account on behalf of a child. The child takes control of the account when they reach the age of majority (18 or 21 depending on state)."),
  ("How much does Acorns Early cost?","Acorns Early is included in the Acorns Premium plan at $5/month. You can open accounts for multiple children under the same $5/month plan."),
  ("What happens to the account when my child turns 18?","The account transfers to the child's control at the age of majority. They receive a notification and can choose to keep the money invested or withdraw it for any purpose."),
  ("Is there a minimum investment for Acorns Early?","Same as other Acorns accounts — $5 to start. You can set up automatic contributions as low as $1/month."),
],
body="""
<section class="cb">
  <p class="lead">The best gift you can give a child isn't a toy — it's a head start on investing. Acorns Early makes it effortless to open a custodial investment account for your kids and grow their wealth automatically from their very first year of life.</p>

  <div class="offer-box hot">
    <div class="ob-badge">🌱 Kids' Future</div>
    <h3>Open Acorns Early — Invest for Your Children</h3>
    <ul>
      <li>✅ UTMA/UGMA custodial account for minors</li>
      <li>✅ Included in Acorns Premium ($5/month)</li>
      <li>✅ Multiple children under one plan</li>
      <li>✅ Automated contributions</li>
      <li>✅ Child gains control at age of majority</li>
    </ul>
    <a href="{A}" class="cta pulse" target="_blank" rel="noopener sponsored">🌱 Start Acorns Early</a>
    <p class="tc">Investing involves risk. Acorns Premium $5/month. UTMA/UGMA rules apply.</p>
  </div>

  <h2>The Power of Starting Early — Compound Interest for Kids</h2>
  <p>Starting a child's investment account at birth vs age 18 makes a staggering difference thanks to compound interest:</p>
  <table class="dt">
    <thead><tr><th>Start Age</th><th>Monthly Contribution</th><th>Value at Age 65</th><th>Total Contributed</th></tr></thead>
    <tbody>
      <tr><td><span class="badge-g">Birth (0)</span></td><td>$50/month</td><td><span class="badge-g">$847,000</span></td><td>$39,000</td></tr>
      <tr><td>Age 5</td><td>$50/month</td><td>$589,000</td><td>$36,000</td></tr>
      <tr><td>Age 10</td><td>$50/month</td><td>$406,000</td><td>$33,000</td></tr>
      <tr><td>Age 18</td><td>$50/month</td><td>$205,000</td><td>$28,200</td></tr>
    </tbody>
  </table>
  <p style="font-size:0.82rem;color:var(--muted)">Assumes 7% average annual return. Illustrative only. Actual returns will vary.</p>

  <h2>UTMA vs UGMA — What's the Difference?</h2>
  <p><strong>UGMA</strong> (Uniform Gifts to Minors Act): Covers financial assets — stocks, bonds, mutual funds, ETFs. Available in all states.</p>
  <p><strong>UTMA</strong> (Uniform Transfers to Minors Act): Covers a broader range including real estate and other property. Available in most states. Acorns Early uses UTMA where available.</p>
  <p>Both work the same way for investing: you manage as custodian, child gets control at 18–21 depending on state law.</p>

  <h2>Tax Considerations for Custodial Accounts</h2>
  <p>Custodial accounts don't have the tax advantages of IRAs. Investment earnings are subject to the "Kiddie Tax" — up to $2,300/year in investment income is taxed at the child's rate (usually 0–10%), above that it's taxed at the parent's rate.</p>
</section>
"""
))

# ── 9. ACORNS FEES ────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-fees",
title="Acorns Fees 2026 — Complete Breakdown of Every Cost",
desc="Complete breakdown of all Acorns fees in 2026. Monthly plans, ETF expense ratios, and the real cost of investing with Acorns at different balance levels.",
kw="acorns fees 2026, how much does acorns cost, acorns fee breakdown, acorns monthly fee",
h1="Acorns Fees 2026 — <span>Every Cost Broken Down</span>",
tag="Fee Transparency · Full Breakdown · 2026",
hero_cta="🌱 Start Investing — First Month Free",
crumbs=[("Home","index.html"),("Acorns Fees",None)],
faqs=[
  ("What are all the fees Acorns charges?","Acorns charges $3/month (Personal) or $5/month (Premium). There are no trading commissions, no withdrawal fees, and no transfer fees. The underlying ETFs have their own expense ratios (0.03–0.18%) which are separate from Acorns' fee."),
  ("Is there a free version of Acorns?","There is no permanently free tier. New accounts typically get the first month free. After that, $3/month for Personal or $5/month for Premium applies."),
  ("Are Acorns fees tax deductible?","Investment advisory fees are generally no longer deductible for individuals under current US tax law (post-2017 Tax Cuts and Jobs Act). Consult a tax advisor for your specific situation."),
  ("How does Acorns' fee compare to traditional financial advisors?","Traditional financial advisors typically charge 1% of assets under management annually. On $10,000 that's $100/year. Acorns charges $36/year (Personal) — cheaper than a human advisor for small balances, though without personalized advice."),
],
body="""
<section class="cb">
  <p class="lead">Acorns is not free — and understanding exactly what you pay matters. The monthly fee is simple, but its real cost as a percentage of your balance changes dramatically as your investments grow. Here's the complete, honest breakdown.</p>

  <h2>Acorns Pricing Plans — 2026</h2>
  <table class="dt">
    <thead><tr><th>Plan</th><th>Monthly Fee</th><th>Annual Fee</th><th>Includes</th></tr></thead>
    <tbody>
      <tr><td><strong>Personal</strong></td><td>$3/month</td><td>$36/year</td><td>Invest (taxable) + Acorns Later (IRA) + Acorns Checking + Emergency Fund + Metal debit card</td></tr>
      <tr><td><strong>Premium</strong></td><td>$5/month</td><td>$60/year</td><td>Everything in Personal + Acorns Early (kids) + IRA match + Custom portfolios + Live Q&A with financial experts</td></tr>
    </tbody>
  </table>

  <h2>Fee as Percentage of Balance — The Real Cost</h2>
  <table class="dt">
    <thead><tr><th>Balance</th><th>Personal ($36/yr)</th><th>Premium ($60/yr)</th><th>Robo-advisor (0.25%/yr)</th></tr></thead>
    <tbody>
      <tr><td>$500</td><td><span class="badge-r">7.2%</span></td><td><span class="badge-r">12.0%</span></td><td><span class="badge-g">0.25%</span></td></tr>
      <tr><td>$2,000</td><td><span class="badge-r">1.8%</span></td><td><span class="badge-r">3.0%</span></td><td><span class="badge-g">0.25%</span></td></tr>
      <tr><td>$10,000</td><td>0.36%</td><td>0.60%</td><td><span class="badge-g">0.25%</span></td></tr>
      <tr><td>$25,000</td><td><span class="badge-g">0.14%</span></td><td>0.24%</td><td>0.25%</td></tr>
      <tr><td>$50,000</td><td><span class="badge-g">0.07%</span></td><td><span class="badge-g">0.12%</span></td><td>0.25%</td></tr>
      <tr><td>$100,000+</td><td><span class="badge-g">0.04%</span></td><td><span class="badge-g">0.06%</span></td><td>0.25%</td></tr>
    </tbody>
  </table>

  <h2>ETF Expense Ratios — The Hidden Layer</h2>
  <p>On top of Acorns' monthly fee, the ETFs in your portfolio charge their own annual expense ratios. These are automatically deducted from fund performance — you never see a bill, but they reduce your returns.</p>
  <table class="dt">
    <thead><tr><th>ETF</th><th>What It Holds</th><th>Expense Ratio</th></tr></thead>
    <tbody>
      <tr><td>Vanguard Total Stock Market ETF (VTI)</td><td>US stocks</td><td><span class="badge-g">0.03%</span></td></tr>
      <tr><td>Vanguard Total Bond Market ETF (BND)</td><td>US bonds</td><td><span class="badge-g">0.03%</span></td></tr>
      <tr><td>Vanguard FTSE Developed Markets ETF (VEA)</td><td>International stocks</td><td><span class="badge-g">0.05%</span></td></tr>
      <tr><td>iShares Core MSCI Emerging Markets ETF (IEMG)</td><td>Emerging markets</td><td>0.09%</td></tr>
      <tr><td>iShares Core US Aggregate Bond ETF (AGG)</td><td>US bonds</td><td><span class="badge-g">0.03%</span></td></tr>
    </tbody>
  </table>
  <p>Total ETF expense ratio burden: approximately 0.03–0.18% depending on your portfolio allocation. This is very competitive — among the lowest in the industry.</p>

  <div class="hl">
    <strong>💡 Fee Verdict:</strong> Acorns' fees are high relative to balance for small accounts but become very competitive above $10,000. The real question isn't "is $3/month too much?" — it's "would I invest anything without Acorns?" For most people who answer no, the $36/year fee pays for itself many times over in actual invested returns.
  </div>

  <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Start — First Month Free</a>
  <p class="tc" style="margin-top:10px">$3/month after free trial. Investing involves risk.</p>
</section>
"""
))

# ── 10. SIGN UP GUIDE ─────────────────────────────────────────
PAGES.append(dict(
slug="acorns-sign-up",
title="How to Sign Up for Acorns 2026 — Step-by-Step Guide",
desc="Step-by-step guide to signing up for Acorns in 2026. From download to first investment in under 10 minutes — everything you need to know to get started.",
kw="how to sign up for acorns, acorns sign up 2026, open acorns account, acorns account setup",
h1="How to Sign Up for Acorns — <span>Start in 10 Minutes</span>",
tag="Sign Up Guide · Step by Step · 2026",
hero_cta="🌱 Open My Acorns Account",
crumbs=[("Home","index.html"),("Sign Up Guide",None)],
faqs=[
  ("What do I need to sign up for Acorns?","You need: a US bank account, Social Security Number (for tax reporting), government-issued ID, and to be 18+ years old. The sign-up process takes about 10 minutes."),
  ("Is there a credit check to open Acorns?","No — Acorns does not perform a credit check. Opening an investment account with Acorns has no impact on your credit score."),
  ("Can non-US citizens use Acorns?","Acorns is only available to US residents with a Social Security Number or Individual Taxpayer Identification Number (ITIN). Non-residents cannot open accounts."),
  ("How long does it take to start investing after signing up?","You can start investing immediately. Your bank account typically links in minutes via Plaid. Once linked and funded ($5 minimum), your first investment can process the same day."),
],
body="""
<section class="cb">
  <p class="lead">Opening an Acorns account takes under 10 minutes. Here's the exact step-by-step process so you know exactly what to expect — and can have your first investment running before you finish reading this page.</p>

  <div class="offer-box hot">
    <div class="ob-badge">🌱 Start Now</div>
    <h3>Open Your Acorns Account — Click to Begin</h3>
    <ul>
      <li>✅ Takes 10 minutes to set up</li>
      <li>✅ $5 minimum to start investing</li>
      <li>✅ No credit check, no impact on credit score</li>
      <li>✅ First month free for new accounts</li>
    </ul>
    <a href="{A}" class="cta pulse" target="_blank" rel="noopener sponsored">🌱 Open Acorns Account</a>
    <p class="tc">18+ US residents only. SSN required. Investing involves risk.</p>
  </div>

  <h2>Step-by-Step Sign Up Guide</h2>

  <h3>Step 1 — Click Our Link & Download the App</h3>
  <p>Click our affiliate link above. This opens the Acorns sign-up page — you can complete registration in the browser or download the iOS/Android app. The app gives the best experience but either works.</p>

  <h3>Step 2 — Create Your Account</h3>
  <p>Enter your email address and create a strong password. You'll receive a verification email — click the link to confirm your address before proceeding.</p>

  <h3>Step 3 — Enter Your Personal Information</h3>
  <p>Acorns is an SEC-registered investment advisor and is legally required to collect:</p>
  <ul>
    <li>Full legal name (as it appears on government ID)</li>
    <li>Date of birth (must be 18+)</li>
    <li>Residential address (must be US address)</li>
    <li>Social Security Number (required for tax reporting — this is standard for all investment accounts)</li>
    <li>Employment information (employed, self-employed, student, retired, etc.)</li>
    <li>Annual income range</li>
    <li>Investment goals (save for retirement, build wealth, etc.)</li>
  </ul>

  <h3>Step 4 — Choose Your Portfolio</h3>
  <p>Acorns recommends a portfolio based on your answers. Review the recommendation — if you're under 35 with a long time horizon, the Moderate or Moderately Aggressive portfolio is usually the right choice. You can always change this later.</p>

  <h3>Step 5 — Link Your Bank Account</h3>
  <p>Acorns uses Plaid to securely link your bank account. Most major US banks (Chase, Bank of America, Wells Fargo, Citi, etc.) connect instantly. You'll also link any debit or credit cards you want to use for Round-Ups here.</p>

  <h3>Step 6 — Set Up Your First Investment</h3>
  <p>Choose your recurring investment amount ($5/week is a great start) and enable Round-Ups on your linked cards. Make your first one-time deposit of at least $5 to activate the account.</p>

  <h3>Step 7 — Enable Acorns Later (IRA)</h3>
  <p>While you're set up, take 2 more minutes to open your Acorns Later IRA. It's included in your $3/month plan at no extra cost — free retirement investing alongside your taxable account.</p>

  <div class="hl">
    <strong>💡 Pro Tip:</strong> Set up a recurring investment of at least $25/week in addition to Round-Ups. Round-Ups build the habit, but a recurring investment builds real wealth. The combination is more powerful than either alone.
  </div>
</section>
"""
))

# ── 11. PROMO CODES ───────────────────────────────────────────
PAGES.append(dict(
slug="acorns-promo-code",
title="Acorns Promo Code 2026 — Get a Free Bonus When You Sign Up",
desc="Find the best Acorns promo codes and sign-up bonuses for 2026. Get free bonus investments just for opening your account through the right link.",
kw="acorns promo code 2026, acorns bonus, acorns referral code, acorns free money signup",
h1="Acorns Promo Code 2026 — <span>Get Your Free Signup Bonus</span>",
tag="Promo Codes · Free Bonus · Limited Time",
hero_cta="🎁 Claim Acorns Bonus Now",
crumbs=[("Home","index.html"),("Promo Codes",None)],
faqs=[
  ("Does Acorns have a promo code for 2026?","Acorns typically offers sign-up bonuses rather than traditional promo codes. Our affiliate link activates the best available current offer — usually a free bonus investment credited to your account after you make your first deposit."),
  ("How do I claim the Acorns sign-up bonus?","Click our link on this page, sign up for a new Acorns account, and make your first deposit. The bonus investment is credited to your account automatically — usually within a few business days."),
  ("Can existing Acorns users get a promo code bonus?","No — sign-up bonuses are for new accounts only. Existing users can earn referral bonuses by inviting friends to sign up."),
  ("How does the Acorns referral program work?","Each Acorns user gets a unique referral link. When a referred friend signs up and makes their first investment, both the referrer and the new user may receive a bonus investment. Check the Acorns app for the current referral offer amount."),
],
body="""
<section class="cb">
  <p class="lead">Acorns doesn't use traditional promo codes — instead, it offers sign-up bonuses that are automatically applied when you use a qualifying link. Our affiliate link is one of the best ways to unlock the current bonus offer.</p>

  <div class="offer-box hot">
    <div class="ob-badge">🎁 Best Current Offer</div>
    <div class="score-row"><span class="stars">★★★★★</span><span class="score">Active</span><span class="score-sub">— Verified June 2026</span></div>
    <h3>Acorns Sign-Up Bonus — Claim via Our Link</h3>
    <ul>
      <li>✅ Free bonus investment credited on first deposit</li>
      <li>✅ First month subscription free</li>
      <li>✅ No promo code needed — bonus activates automatically</li>
      <li>✅ Available to new US accounts only</li>
      <li>✅ Bonus invested directly into your portfolio</li>
    </ul>
    <a href="{A}" class="cta pulse" target="_blank" rel="noopener sponsored">🎁 Claim Bonus — Open Acorns Now</a>
    <p class="tc">T&Cs apply. New accounts only. Bonus subject to change. Must make qualifying deposit. Investing involves risk.</p>
  </div>

  <h2>Why Our Link Beats Searching for Promo Codes</h2>
  <p>Most "Acorns promo code" searches lead to expired codes or sites that just redirect you to the standard Acorns homepage. Our affiliate partnership with Acorns means:</p>
  <ul>
    <li>The bonus offer is always current — we update this page regularly</li>
    <li>No code to remember or type — the bonus applies automatically when you click our link</li>
    <li>The same or better offer than any code you'd find elsewhere</li>
  </ul>

  <h2>Acorns Referral Program — Earn Bonuses for Friends</h2>
  <p>Once you have an Acorns account, you get your own referral link. Share it with friends and family — when they sign up and invest, you both earn a bonus. There's no limit to how many friends you can refer.</p>
  <p>Find your referral link in the Acorns app under: <strong>Account → Invite Friends</strong></p>

  <h2>Other Ways to Get Free Money from Acorns</h2>
  <ul>
    <li><strong>Acorns Earn</strong> — shop at 450+ partner brands and earn bonus investments. Some brands offer $5–$50 per qualifying purchase</li>
    <li><strong>Found Money</strong> — automatic bonus investments when you use your Acorns card at partner retailers</li>
    <li><strong>Acorns Premium IRA match</strong> — Premium plan ($5/month) includes a 1% IRA contribution match on new contributions</li>
  </ul>
</section>
"""
))

# ── 12. PORTFOLIOS ────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-portfolios",
title="Acorns Portfolios 2026 — Which Portfolio Should You Choose?",
desc="Complete guide to all Acorns portfolio options in 2026. Conservative, Moderate, Aggressive, and ESG portfolios explained — with returns data and how to choose.",
kw="acorns portfolios 2026, acorns conservative vs aggressive, best acorns portfolio, acorns esg portfolio",
h1="Acorns Portfolios 2026 — <span>Which One Should You Pick?</span>",
tag="Portfolio Guide · Returns Data · 2026",
hero_cta="🌱 Start With the Right Portfolio",
crumbs=[("Home","index.html"),("Acorns Portfolios",None)],
faqs=[
  ("How many portfolios does Acorns offer?","Acorns offers five core portfolios (Conservative to Aggressive) plus ESG (Sustainable) versions of each and a Bitcoin-linked portfolio for Premium users."),
  ("Which Acorns portfolio has the best returns?","Historically, the Aggressive portfolio has the highest long-run returns due to 100% stock allocation. However, it also has the most volatility. For most investors under 40, Moderate to Moderately Aggressive is the right balance."),
  ("Can I switch portfolios after investing?","Yes — you can switch portfolios anytime. Acorns will automatically rebalance your holdings into the new allocation. There are no fees to switch and no tax consequences in an IRA. In a taxable account, rebalancing may generate taxable gains."),
  ("What is the Acorns ESG portfolio?","ESG (Environmental, Social, Governance) portfolios invest in companies that meet certain ethical criteria — lower carbon footprint, strong labor practices, good governance. Acorns' ESG portfolios use iShares sustainable ETFs and are available on the Personal and Premium plans."),
],
body="""
<section class="cb">
  <p class="lead">Acorns' portfolio choice is the most important investment decision you make on the platform. Choose too conservative and inflation eats your returns. Choose too aggressive and a market downturn early on can derail your goals. Here's exactly how to choose.</p>

  <div class="offer-box">
    <div class="ob-badge">🌱 Smart Start</div>
    <h3>Not Sure Which Portfolio? Acorns Recommends One For You</h3>
    <p style="color:rgba(232,245,240,0.75);margin-bottom:18px">Answer 5 questions about your age, income, and goals — Acorns recommends the right portfolio automatically.</p>
    <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Get My Portfolio Recommendation</a>
    <p class="tc">Investing involves risk. Recommendations based on questionnaire only.</p>
  </div>

  <h2>The 5 Acorns Core Portfolios</h2>
  <table class="dt">
    <thead><tr><th>Portfolio</th><th>Stocks</th><th>Bonds</th><th>Avg Annual Return*</th><th>Best For</th></tr></thead>
    <tbody>
      <tr><td><strong>Conservative</strong></td><td>20%</td><td>80%</td><td>4–5%</td><td>Short time horizon (under 5 years), near-retirees</td></tr>
      <tr><td><strong>Moderately Conservative</strong></td><td>40%</td><td>60%</td><td>5–6%</td><td>5–10 year horizon, lower risk tolerance</td></tr>
      <tr><td><strong>Moderate</strong></td><td>60%</td><td>40%</td><td>6–7%</td><td><span class="badge-g">Most beginners — best balance</span></td></tr>
      <tr><td><strong>Moderately Aggressive</strong></td><td>80%</td><td>20%</td><td>7–8%</td><td>10–20 year horizon, comfortable with volatility</td></tr>
      <tr><td><strong>Aggressive</strong></td><td>100%</td><td>0%</td><td>8–10%</td><td>20+ year horizon, high risk tolerance, under 35</td></tr>
    </tbody>
  </table>
  <p style="font-size:0.82rem;color:var(--muted)">*Historical average annual returns. Past performance does not guarantee future results. Actual returns will vary.</p>

  <h2>The Simple Portfolio Selection Rule</h2>
  <p>Subtract your age from 110. That's roughly the percentage of stocks you should hold.</p>
  <ul>
    <li>Age 25 → 85% stocks → <strong>Aggressive or Moderately Aggressive</strong></li>
    <li>Age 35 → 75% stocks → <strong>Moderately Aggressive</strong></li>
    <li>Age 45 → 65% stocks → <strong>Moderate to Moderately Aggressive</strong></li>
    <li>Age 55 → 55% stocks → <strong>Moderate</strong></li>
    <li>Age 65 → 45% stocks → <strong>Moderately Conservative</strong></li>
  </ul>

  <h2>ESG Portfolios — Invest With Your Values</h2>
  <p>Each of the five core portfolios has an ESG (Sustainable) equivalent. These replace standard ETFs with iShares ESG-screened alternatives that avoid companies involved in weapons, tobacco, fossil fuel extraction, and other areas that don't meet ESG criteria.</p>
  <p>ESG portfolios have slightly higher ETF expense ratios (0.10–0.20% vs 0.03–0.09%) but the performance difference is minimal over long periods.</p>
</section>
"""
))

# ── 13. BEGINNERS ─────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-for-beginners",
title="Acorns for Beginners 2026 — Complete Getting Started Guide",
desc="The complete beginner's guide to Acorns investing in 2026. Everything you need to know to open your account, start investing, and build wealth from zero.",
kw="acorns for beginners 2026, acorns beginner guide, start investing acorns, acorns investing first time",
h1="Acorns for Beginners — <span>Your Complete Getting Started Guide</span>",
tag="Beginner Guide · Start From Zero · 2026",
hero_cta="🌱 Start Investing Today",
crumbs=[("Home","index.html"),("For Beginners",None)],
faqs=[
  ("Do I need to know about investing to use Acorns?","No — Acorns is specifically designed for people with zero investing knowledge. It handles all investment decisions for you. You just set up the automation and let it run."),
  ("What if the market crashes while I'm invested?","Market downturns are normal and temporary. The key is staying invested — don't panic and withdraw. Historical data shows staying invested through downturns and continuing to contribute (which buys more at lower prices) produces better outcomes than trying to time the market."),
  ("How do I know if my investments are growing?","The Acorns app shows your portfolio value, total invested amount, and total return (in dollars and percentage) on the main screen. You can see your performance at any time."),
  ("Can I withdraw my money whenever I want?","Yes — your taxable Acorns Invest account has no lock-up period. You can withdraw anytime. IRA accounts (Acorns Later) have restrictions — withdrawals before age 59½ are subject to penalties and taxes."),
],
body="""
<section class="cb">
  <p class="lead">You don't need to understand the stock market to build wealth with Acorns. You need $5, 10 minutes to set up, and the discipline to leave it alone. This guide covers everything from your first login to your first $10,000 invested.</p>

  <div class="offer-box hot">
    <div class="ob-badge">🌱 Perfect for Beginners</div>
    <h3>Start Investing Today — No Experience Required</h3>
    <ul>
      <li>✅ $5 to start — less than a coffee</li>
      <li>✅ No investment knowledge needed</li>
      <li>✅ Everything automated after 10-minute setup</li>
      <li>✅ Expert-built portfolios do the work for you</li>
    </ul>
    <a href="{A}" class="cta pulse" target="_blank" rel="noopener sponsored">🌱 Open Free Account</a>
    <p class="tc">Investing involves risk. $3/month after first month free.</p>
  </div>

  <h2>5 Things Every Acorns Beginner Should Know</h2>

  <h3>1. You're Not Buying Individual Stocks</h3>
  <p>Acorns invests your money in ETFs — Exchange-Traded Funds. Each ETF is a basket containing hundreds or thousands of stocks and bonds. When you invest $100 in Acorns, you instantly own tiny pieces of thousands of companies. This is diversification — spreading risk so that one bad company can't hurt you badly.</p>

  <h3>2. Short-Term Losses Are Normal</h3>
  <p>The stock market goes up and down daily. You will see red numbers in your Acorns app — sometimes for weeks or months. This is completely normal. The stock market has recovered from every single downturn in history. Long-term investors who stayed invested came out ahead. The only people who lost permanently are those who sold during downturns.</p>

  <h3>3. Consistency Beats Timing</h3>
  <p>The best investment strategy for beginners is simple: invest a fixed amount consistently, regardless of what the market is doing. This is called dollar-cost averaging — sometimes you buy shares when they're expensive, sometimes when they're cheap, and it averages out. Trying to time the market loses to this simple strategy for the vast majority of investors.</p>

  <h3>4. The Fee Is an Investment in Your Investing Habit</h3>
  <p>The $3/month Acorns fee is high relative to a $500 balance. But if that $3/month keeps you investing consistently over 20 years instead of not investing at all, it's the best $36/year you'll ever spend. Think of it as the cost of the habit, not just the cost of the service.</p>

  <h3>5. Open a Roth IRA Immediately</h3>
  <p>When you sign up for Acorns, immediately also open Acorns Later as a Roth IRA. It's included in your $3/month and takes 2 minutes. Every dollar in a Roth IRA grows completely tax-free. Time in a Roth IRA is the most valuable financial asset a young person has.</p>

  <h2>Your First 90 Days Action Plan</h2>
  <table class="dt">
    <thead><tr><th>Week</th><th>Action</th><th>Why</th></tr></thead>
    <tbody>
      <tr><td>Week 1</td><td>Open account, link bank and cards, make $5 deposit</td><td>Get invested — start the habit</td></tr>
      <tr><td>Week 1</td><td>Open Acorns Later (Roth IRA)</td><td>Tax-free retirement growth starts now</td></tr>
      <tr><td>Week 2</td><td>Set up $25/week recurring investment</td><td>Automation ensures consistency</td></tr>
      <tr><td>Week 2</td><td>Enable Round-Ups on all linked cards</td><td>Adds $30–$50/month without effort</td></tr>
      <tr><td>Week 4</td><td>Increase to $50/week if possible</td><td>Doubling weekly investment dramatically accelerates results</td></tr>
      <tr><td>Month 3</td><td>Check balance (not daily — monthly)</td><td>Less stress, same result</td></tr>
    </tbody>
  </table>
</section>
"""
))

# ── 14. ACORNS EARN ───────────────────────────────────────────
PAGES.append(dict(
slug="acorns-earn",
title="Acorns Earn 2026 — Get Bonus Investments From Shopping",
desc="How Acorns Earn works in 2026. Get bonus investments when you shop at 450+ partner brands. Turn everyday spending into free investments automatically.",
kw="acorns earn 2026, acorns found money, acorns shopping rewards, acorns earn bonus investments",
h1="Acorns Earn — <span>Get Paid to Shop, Invest the Rewards</span>",
tag="Earn Rewards · 450+ Brands · Free Investments",
hero_cta="🌱 Start Earning Bonus Investments",
crumbs=[("Home","index.html"),("Acorns Earn",None)],
faqs=[
  ("What is Acorns Earn?","Acorns Earn is a rewards program where shopping at partner brands earns bonus investments credited directly to your Acorns portfolio. It's like cashback, but instead of cash, you get investments."),
  ("How much can I earn through Acorns Earn?","It varies by brand and offer — typically $5–$50 per qualifying purchase. Some brands offer percentage-based rewards (1–5% of purchase). Heavy users report $10–$50/month in bonus investments from Earn."),
  ("Which brands are on Acorns Earn?","450+ brands including Apple, Walmart, Nike, Airbnb, Hotels.com, Lyft, Blue Apron, and many more. The full list is in the Acorns app under the Earn tab."),
  ("How do I activate Acorns Earn offers?","For browser shopping: install the Acorns browser extension and it automatically detects partner sites. For in-store: link your debit/credit card and use it at participating retailers — the bonus is credited automatically (Found Money)."),
],
body="""
<section class="cb">
  <p class="lead">Acorns Earn turns your everyday shopping into automatic investments. While you're buying groceries, booking travel, or ordering dinner, Acorns Earn is earning bonus investments credited directly to your portfolio. It's free money that most users leave unclaimed.</p>

  <div class="offer-box hot">
    <div class="ob-badge">🌱 Free Investments</div>
    <h3>Start Earning Bonus Investments — 450+ Brands</h3>
    <ul>
      <li>✅ Shop at Apple, Walmart, Nike, Airbnb and 450+ more</li>
      <li>✅ Bonus investments credited automatically</li>
      <li>✅ Browser extension for online shopping</li>
      <li>✅ Card-linked rewards for in-store shopping</li>
      <li>✅ No extra steps once set up</li>
    </ul>
    <a href="{A}" class="cta pulse" target="_blank" rel="noopener sponsored">🌱 Activate Acorns Earn</a>
    <p class="tc">Earn offers subject to change. Brand participation varies. T&Cs apply.</p>
  </div>

  <h2>How Acorns Earn Works — Two Methods</h2>

  <h3>Method 1: Found Money (Card-Linked)</h3>
  <p>Link your debit or credit card to Acorns. When you use that card at a participating in-store or online retailer, the bonus investment is triggered automatically — no coupons, no clicking links, no extra steps. The money just appears in your portfolio.</p>

  <h3>Method 2: Acorns Browser Extension</h3>
  <p>Install the free Acorns browser extension on Chrome or Safari. When you visit a partner website, the extension automatically activates the Earn offer. Click through and make your purchase normally — the bonus investment is credited within 60–90 days.</p>

  <h2>Sample Acorns Earn Offers — June 2026</h2>
  <table class="dt">
    <thead><tr><th>Brand</th><th>Offer Type</th><th>Bonus</th></tr></thead>
    <tbody>
      <tr><td>Apple</td><td>Percentage</td><td>Up to $20 on qualifying purchases</td></tr>
      <tr><td>Walmart</td><td>Fixed</td><td>$5 per qualifying order</td></tr>
      <tr><td>Nike</td><td>Percentage</td><td>2% on all purchases</td></tr>
      <tr><td>Airbnb</td><td>Fixed</td><td>$25 on first booking</td></tr>
      <tr><td>Hotels.com</td><td>Percentage</td><td>3% on hotel bookings</td></tr>
      <tr><td>Lyft</td><td>Fixed</td><td>$5 on first 5 rides</td></tr>
    </tbody>
  </table>
  <p style="font-size:0.82rem;color:var(--muted)">Offers change regularly. Check the Acorns app for current available offers.</p>

  <h2>Maximizing Acorns Earn</h2>
  <ul>
    <li>Install the browser extension and leave it on — it works passively</li>
    <li>Check the Earn tab before any major online purchase</li>
    <li>Book travel through Acorns Earn links — hotel and flight bonuses can be $20–$50+</li>
    <li>Do your holiday shopping through Earn — November/December offers are usually the highest of the year</li>
  </ul>
</section>
"""
))

# ── 15. TAX GUIDE ─────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-tax-guide",
title="Acorns Tax Guide 2026 — What You Owe on Your Investments",
desc="Complete Acorns tax guide for 2026. How dividends, capital gains, and IRA withdrawals are taxed. What forms Acorns sends, and how to minimize your tax bill.",
kw="acorns taxes 2026, acorns 1099 form, acorns capital gains tax, acorns tax guide",
h1="Acorns Tax Guide 2026 — <span>What You Owe on Your Investments</span>",
tag="Tax Guide · 1099 Forms · 2026",
hero_cta="🌱 Invest Smarter With Acorns",
crumbs=[("Home","index.html"),("Tax Guide",None)],
faqs=[
  ("Does Acorns send tax forms?","Yes — Acorns sends a 1099 tax form by February 15 each year for taxable accounts (Acorns Invest) with reportable activity. IRA accounts (Acorns Later) don't generate annual 1099s but do require reporting of withdrawals."),
  ("What taxes do I pay on Acorns investments?","You pay capital gains tax when you sell investments for a profit, and income tax on dividends received. Investments held over 1 year qualify for the lower long-term capital gains rate (0%, 15%, or 20% depending on income)."),
  ("Is the Acorns $3/month fee tax deductible?","Under current US tax law (post-2017), investment advisory fees paid for taxable accounts are no longer deductible for most individuals. Consult a tax professional for advice specific to your situation."),
  ("How does Acorns handle taxes on Round-Ups?","The Round-Up amounts themselves are not taxable when they're invested — you're just moving your own money. Taxes apply when the investments are sold for a gain, or when dividends are distributed."),
],
body="""
<section class="cb">
  <p class="lead">Investing with Acorns has tax implications you should understand before your first tax season. The good news: Acorns handles most of the complexity and sends you exactly what you need to file. Here's what to expect.</p>

  <div class="hl">
    <strong>⚠️ Disclaimer:</strong> This is general information, not tax advice. Tax laws change and individual situations vary. Consult a licensed CPA or tax advisor for advice specific to your situation.
  </div>

  <h2>Tax Forms Acorns Sends You</h2>
  <table class="dt">
    <thead><tr><th>Form</th><th>When You Receive It</th><th>What It Reports</th></tr></thead>
    <tbody>
      <tr><td>1099-DIV</td><td>By Feb 15</td><td>Dividends and capital gain distributions from your ETFs</td></tr>
      <tr><td>1099-B</td><td>By Feb 15</td><td>Proceeds from ETF sales (when Acorns rebalances your portfolio)</td></tr>
      <tr><td>1099-R</td><td>By Jan 31</td><td>IRA distributions (if you withdrew from Acorns Later)</td></tr>
      <tr><td>5498</td><td>By May 31</td><td>IRA contributions for the year</td></tr>
    </tbody>
  </table>

  <h2>Capital Gains Tax on Acorns</h2>
  <p>When Acorns rebalances your portfolio (selling some ETFs to buy others), those sales generate capital gains or losses that appear on your 1099-B. You must report these on your federal tax return.</p>
  <table class="dt">
    <thead><tr><th>Holding Period</th><th>Tax Rate (2026)</th><th>Applies To</th></tr></thead>
    <tbody>
      <tr><td>Under 1 year (short-term)</td><td>Ordinary income rate (10–37%)</td><td>Investments sold within 1 year</td></tr>
      <tr><td>Over 1 year (long-term)</td><td><span class="badge-g">0%, 15%, or 20%</span></td><td>Investments held over 1 year</td></tr>
    </tbody>
  </table>

  <h2>IRA Tax Advantages — Why Acorns Later Matters</h2>
  <p><strong>Roth IRA:</strong> Contributions are after-tax. Growth and qualifying withdrawals are 100% tax-free. No annual 1099 for growth. Ideal for long-term retirement savings.</p>
  <p><strong>Traditional IRA:</strong> Contributions may be tax-deductible. Growth is tax-deferred. Withdrawals in retirement are taxed as ordinary income. Generates a 1099-R when you withdraw.</p>

  <h2>How to Minimize Taxes on Acorns</h2>
  <ul>
    <li><strong>Use Acorns Later (IRA)</strong> for maximum tax advantage — growth is tax-free (Roth) or tax-deferred (Traditional)</li>
    <li><strong>Don't withdraw from taxable accounts early</strong> — each withdrawal may trigger capital gains taxes</li>
    <li><strong>Hold investments long-term</strong> — long-term capital gains rates are significantly lower than short-term</li>
    <li><strong>Don't ignore your 1099</strong> — even small amounts from rebalancing must be reported to avoid IRS notices</li>
  </ul>
</section>
"""
))

# ── 16. WITHDRAW ──────────────────────────────────────────────
PAGES.append(dict(
slug="acorns-withdraw",
title="How to Withdraw Money from Acorns 2026 — Complete Guide",
desc="Step-by-step guide to withdrawing money from Acorns in 2026. How long it takes, fees, IRA withdrawal rules, and what to watch out for before cashing out.",
kw="how to withdraw from acorns, acorns withdrawal 2026, acorns cash out, acorns withdrawal time",
h1="How to Withdraw from Acorns — <span>Complete 2026 Guide</span>",
tag="Withdrawal Guide · No Fees · 2026",
hero_cta="🌱 Invest With Confidence",
crumbs=[("Home","index.html"),("Withdraw Money",None)],
faqs=[
  ("How long does an Acorns withdrawal take?","Standard withdrawals from your taxable Acorns Invest account take 3–6 business days to arrive in your bank account. Acorns must sell your ETF holdings first, which takes 1–2 business days, then the transfer takes 2–3 more days."),
  ("Are there fees to withdraw from Acorns?","No — Acorns does not charge withdrawal fees. However, selling investments may generate capital gains taxes. Early IRA withdrawals (before 59½) carry a 10% penalty plus income taxes."),
  ("Can I withdraw from Acorns Later (IRA) early?","Yes, but there are penalties. Early withdrawal (before age 59½) from a Traditional IRA incurs a 10% penalty plus income taxes on the amount. Roth IRA contributions (not earnings) can be withdrawn penalty-free at any age."),
  ("Will withdrawing close my Acorns account?","No — you can withdraw any or all of your funds without closing the account. Your account stays open and recurring investments continue unless you cancel them."),
],
body="""
<section class="cb">
  <p class="lead">Withdrawing from Acorns is straightforward — but the timeline surprises most people. Understanding how long it takes, what triggers taxes, and IRA-specific rules means no unpleasant surprises when you need your money.</p>

  <h2>How to Withdraw — Step by Step</h2>
  <ol>
    <li>Open the Acorns app</li>
    <li>Tap the account you want to withdraw from (Invest, Later, or Checking)</li>
    <li>Tap <strong>Withdraw</strong></li>
    <li>Enter the amount you want to withdraw</li>
    <li>Confirm your bank account destination</li>
    <li>Submit — Acorns will sell the required ETF holdings and transfer the cash</li>
  </ol>

  <h2>Withdrawal Timeline</h2>
  <table class="dt">
    <thead><tr><th>Account Type</th><th>ETF Sale</th><th>Bank Transfer</th><th>Total Time</th></tr></thead>
    <tbody>
      <tr><td>Acorns Invest (taxable)</td><td>1–2 business days</td><td>2–3 business days</td><td><strong>3–6 business days</strong></td></tr>
      <tr><td>Acorns Later (IRA)</td><td>1–2 business days</td><td>2–3 business days</td><td><strong>3–6 business days</strong></td></tr>
      <tr><td>Acorns Checking</td><td>N/A (cash account)</td><td>Instant to linked bank</td><td><span class="badge-g">Instant</span></td></tr>
    </tbody>
  </table>

  <h2>Before You Withdraw — Checklist</h2>
  <ul>
    <li><strong>Check for capital gains</strong> — if your investments have grown, selling triggers taxable capital gains. Consider timing withdrawals to minimize tax impact</li>
    <li><strong>IRA early withdrawal?</strong> — verify you're aware of the 10% penalty + taxes on Traditional IRA withdrawals before age 59½</li>
    <li><strong>Recurring investments will continue</strong> — withdrawing doesn't pause your recurring investments. Cancel or pause them separately if needed</li>
    <li><strong>Market timing</strong> — you'll sell at whatever price the market is at when your sell order processes. You can't control the exact sale price</li>
  </ul>

  <div class="hl">
    <strong>💡 Best Practice:</strong> Keep your long-term investments (retirement, wealth building) in Acorns and don't touch them. If you need accessible emergency funds, the Acorns Checking account is better — it's FDIC insured cash that transfers instantly.
  </div>
</section>
"""
))

# ── 17. IS ACORNS SAFE ────────────────────────────────────────
PAGES.append(dict(
slug="is-acorns-safe",
title="Is Acorns Safe? 2026 — Security, SIPC Protection & Legitimacy",
desc="Is Acorns safe and legitimate? Full security review covering SEC registration, SIPC protection, encryption, and what happens to your money if Acorns shuts down.",
kw="is acorns safe, acorns legit 2026, acorns security, acorns sipc protection",
h1="Is Acorns Safe? — <span>Full Security Review 2026</span>",
tag="Safety Review · SIPC Protected · SEC Registered",
hero_cta="🌱 Invest Safely with Acorns",
crumbs=[("Home","index.html"),("Is Acorns Safe?",None)],
faqs=[
  ("Is Acorns a legitimate company?","Yes — Acorns Advisers, LLC is an SEC-registered investment advisor. Acorns Securities, LLC is a FINRA/SIPC member broker-dealer. It has been operating since 2014 and has over 10 million customers."),
  ("What happens to my money if Acorns goes bankrupt?","Your investments are held in your name in a segregated brokerage account, not commingled with Acorns' operating funds. SIPC protection covers up to $500,000 ($250,000 in cash) if the brokerage fails."),
  ("Is my bank account information safe with Acorns?","Acorns uses Plaid for bank linking — the industry standard used by hundreds of financial apps. Your bank credentials are encrypted and Acorns never sees your actual login information."),
  ("Has Acorns ever been hacked?","No major security breach has been publicly reported for Acorns. The company uses 256-bit encryption for data in transit and at rest, two-factor authentication, and standard financial security protocols."),
],
body="""
<section class="cb">
  <p class="lead">Before you hand over your financial information and real money to any app, you deserve to understand exactly what protections are in place. Acorns has multiple layers of regulatory oversight and security that make it one of the safer investment apps available.</p>

  <div class="stat-grid">
    <div class="stat-card"><div class="num">SEC</div><div class="label">Registered RIA</div></div>
    <div class="stat-card"><div class="num">SIPC</div><div class="label">$500K Protected</div></div>
    <div class="stat-card"><div class="num">FINRA</div><div class="label">Member Broker</div></div>
    <div class="stat-card"><div class="num">256-bit</div><div class="label">Encryption</div></div>
    <div class="stat-card"><div class="num">2014</div><div class="label">Operating Since</div></div>
    <div class="stat-card"><div class="num">10M+</div><div class="label">Users Trust It</div></div>
  </div>

  <h2>Regulatory Oversight — Who Watches Acorns</h2>
  <table class="dt">
    <thead><tr><th>Regulator</th><th>What They Oversee</th><th>Acorns Status</th></tr></thead>
    <tbody>
      <tr><td>SEC (Securities and Exchange Commission)</td><td>Investment advisory practices</td><td><span class="badge-g">Registered RIA</span></td></tr>
      <tr><td>FINRA</td><td>Broker-dealer operations</td><td><span class="badge-g">Member</span></td></tr>
      <tr><td>SIPC</td><td>Customer asset protection</td><td><span class="badge-g">Member — $500K protection</span></td></tr>
    </tbody>
  </table>

  <h2>SIPC Protection — What It Means for You</h2>
  <p>SIPC (Securities Investor Protection Corporation) protects your account if Acorns Securities were to fail financially. It covers up to $500,000 in total account value ($250,000 maximum in cash).</p>
  <p><strong>Important:</strong> SIPC does NOT protect against market losses — if your investments decline in value, that's market risk, not covered. SIPC only protects against the brokerage firm failing and your assets disappearing.</p>

  <h2>Your Money Is Held Separately</h2>
  <p>Your investments are held in your name in a segregated customer account at Acorns Securities. This is legally separate from Acorns' own operating accounts. Even if Acorns the company ran out of money and closed, your investment assets would be returned to you — they don't belong to Acorns, they belong to you.</p>

  <h2>Security Features</h2>
  <ul>
    <li><strong>256-bit SSL encryption</strong> — all data transmitted between you and Acorns is encrypted</li>
    <li><strong>Two-factor authentication</strong> — available and recommended on all accounts</li>
    <li><strong>Biometric login</strong> — Face ID and Touch ID supported on mobile</li>
    <li><strong>Plaid bank linking</strong> — industry-standard secure bank connection; Acorns never sees your bank password</li>
    <li><strong>Automatic session timeout</strong> — app locks after inactivity</li>
  </ul>

  <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Invest Safely — Open Acorns Account</a>
  <p class="tc" style="margin-top:10px">Investing involves risk including loss of principal. SIPC protection covers brokerage failure, not market losses.</p>
</section>
"""
))

# ── 18. ACORNS VS BETTERMENT ──────────────────────────────────
PAGES.append(dict(
slug="acorns-vs-betterment",
title="Acorns vs Betterment 2026 — Which Robo-Advisor Is Better?",
desc="Acorns vs Betterment compared for 2026. Fees, features, tax-loss harvesting, and which robo-advisor is the right choice at different balance levels.",
kw="acorns vs betterment 2026, betterment vs acorns, best robo advisor 2026",
h1="Acorns vs Betterment 2026 — <span>Which Robo-Advisor Wins?</span>",
tag="Robo-Advisor Comparison · 2026",
hero_cta="🌱 Choose Acorns",
crumbs=[("Home","index.html"),("Acorns vs Betterment",None)],
faqs=[
  ("Is Betterment or Acorns better for beginners?","Acorns is simpler — Round-Ups and fully automated investing make it easier to start. Betterment has more features but requires more setup and understanding of goals."),
  ("Does Betterment have tax-loss harvesting?","Yes — Betterment offers automatic tax-loss harvesting, a feature Acorns lacks. For accounts above $50,000, this can save hundreds annually in taxes."),
  ("Which is cheaper — Acorns or Betterment?","Acorns costs $3/month ($36/year) flat. Betterment charges 0.25% annually — cheaper than Acorns on balances under $14,400, more expensive above that."),
  ("Can I use both Acorns and Betterment?","Yes — many investors use Acorns for automatic spare-change investing and Betterment for larger, goal-based portfolios. They serve slightly different purposes."),
],
body="""
<section class="cb">
  <p class="lead">Both Acorns and Betterment automate your investing — but they're built for different stages of your investing journey. Here's which one wins at each balance level and life stage.</p>

  <h2>Acorns vs Betterment — Full Comparison</h2>
  <table class="dt">
    <thead><tr><th>Feature</th><th>Acorns</th><th>Betterment</th></tr></thead>
    <tbody>
      <tr><td>Fee structure</td><td>$3/month flat</td><td>0.25%/year (or $4/month for Premium)</td></tr>
      <tr><td>Fee cheaper when</td><td><span class="badge-g">Balance over $14,400</span></td><td>Balance under $14,400</td></tr>
      <tr><td>Round-Ups</td><td><span class="badge-g">Yes — unique feature</span></td><td>No</td></tr>
      <tr><td>Tax-loss harvesting</td><td>No</td><td><span class="badge-g">Yes — saves hundreds/year</span></td></tr>
      <tr><td>Portfolio customization</td><td>5 presets</td><td><span class="badge-g">More flexible, goal-based</span></td></tr>
      <tr><td>Socially responsible investing</td><td>Yes (ESG portfolios)</td><td><span class="badge-g">Yes (more options)</span></td></tr>
      <tr><td>IRA (retirement)</td><td><span class="badge-g">Yes — Acorns Later</span></td><td><span class="badge-g">Yes — Betterment IRA</span></td></tr>
      <tr><td>Minimum balance</td><td>$5</td><td><span class="badge-g">$0</span></td></tr>
      <tr><td>Best for</td><td><span class="badge-g">Beginner habit builders</span></td><td>Goal-based investors $14K+</td></tr>
    </tbody>
  </table>

  <h2>Fee Crossover Point</h2>
  <p>Acorns ($36/year) is cheaper than Betterment (0.25%/year) when your balance is above <strong>$14,400</strong>. Below that level, Betterment's percentage fee is cheaper. This creates a natural migration path:</p>
  <ul>
    <li><strong>$0–$14,400:</strong> Betterment is cheaper on fees</li>
    <li><strong>$14,400+:</strong> Acorns is cheaper on fees</li>
    <li><strong>$50,000+:</strong> Betterment's tax-loss harvesting may offset its higher fee through tax savings</li>
  </ul>

  <div class="hl">
    <strong>💡 Our Take:</strong> Start with Acorns if you need the habit-formation automation (Round-Ups especially). Consider adding or switching to Betterment once you've built your balance above $20,000 and want more sophisticated goal-based features. Both are good products — the best choice depends on where you are in your investing journey.
  </div>

  <a href="{A}" class="cta" target="_blank" rel="noopener sponsored">🌱 Start with Acorns</a>
  <p class="tc" style="margin-top:10px">Investing involves risk. Fee comparison based on 2026 pricing.</p>
</section>
"""
))

# ── 19. COMPOUND INTEREST ─────────────────────────────────────
PAGES.append(dict(
slug="acorns-compound-interest",
title="Acorns & Compound Interest 2026 — How Small Investments Grow Big",
desc="How compound interest makes your Acorns investments grow over time. Real examples of how $5/day turns into tens of thousands of dollars through the power of compounding.",
kw="acorns compound interest, compound investing acorns, how acorns grows money, acorns long term growth",
h1="Acorns & Compound Interest — <span>How $5/Day Becomes $100,000</span>",
tag="Compound Growth · Long Term · Real Examples",
hero_cta="🌱 Start Compounding Today",
crumbs=[("Home","index.html"),("Compound Interest",None)],
faqs=[
  ("What is compound interest in investing?","Compound interest means earning returns on your returns. If you invest $1,000 and earn 7%, you have $1,070. Next year you earn 7% on $1,070 — not just the original $1,000. Over decades, this snowball effect is dramatic."),
  ("How long does it take Acorns to compound significantly?","Compound interest is slow at first and accelerates dramatically over time. Most of your growth happens in the later years — a $100/month investor at 7% has about $17,000 after 10 years, but $113,000 after 30 years."),
  ("What return rate does Acorns typically achieve?","Historical returns for balanced ETF portfolios like Acorns' are approximately 6–8% annually over long periods. The Aggressive portfolio (100% stocks) has historically returned 8–10% annually over 20+ year periods."),
  ("Does compound interest work the same on Acorns?","Yes — Acorns reinvests all dividends automatically, which is the key mechanism for compound growth. Every dividend payment buys more ETF shares, which earn more dividends, which buy more shares."),
],
body="""
<section class="cb">
  <p class="lead">Albert Einstein allegedly called compound interest the eighth wonder of the world. Whether or not he said it, the math is undeniable: small, consistent investments left alone for decades don't just grow — they explode. Acorns is built entirely around capturing this effect.</p>

  <div class="offer-box hot">
    <div class="ob-badge">🌱 Start Now</div>
    <h3>Every Day You Wait Costs You Compound Growth</h3>
    <p style="color:rgba(232,245,240,0.75);margin-bottom:18px">A 25-year-old who starts investing $50/month today will have $153,000 more at retirement than a 35-year-old who starts the same habit. That's the cost of waiting 10 years.</p>
    <a href="{A}" class="cta pulse" target="_blank" rel="noopener sponsored">🌱 Start Today — Not Tomorrow</a>
    <p class="tc">Assumes 7% average annual return. Illustrative only.</p>
  </div>

  <h2>The Compound Growth Table — $50/Month at 7%</h2>
  <table class="dt">
    <thead><tr><th>Years Invested</th><th>Total Contributed</th><th>Portfolio Value</th><th>Compound Gains</th></tr></thead>
    <tbody>
      <tr><td>5 years</td><td>$3,000</td><td>$3,600</td><td>$600</td></tr>
      <tr><td>10 years</td><td>$6,000</td><td>$8,700</td><td>$2,700</td></tr>
      <tr><td>15 years</td><td>$9,000</td><td>$16,000</td><td>$7,000</td></tr>
      <tr><td>20 years</td><td>$12,000</td><td>$26,200</td><td>$14,200</td></tr>
      <tr><td>25 years</td><td>$15,000</td><td>$40,900</td><td>$25,900</td></tr>
      <tr><td>30 years</td><td>$18,000</td><td>$62,000</td><td>$44,000</td></tr>
      <tr><td>40 years</td><td>$24,000</td><td>$131,000</td><td>$107,000</td></tr>
    </tbody>
  </table>

  <h2>The $5/Day Challenge — What It Actually Becomes</h2>
  <p>$5/day = $150/month. Seems small. Here's what it grows to at 7% average annual return:</p>
  <ul>
    <li><strong>10 years:</strong> ~$26,000 from $18,000 contributed</li>
    <li><strong>20 years:</strong> ~$78,000 from $36,000 contributed</li>
    <li><strong>30 years:</strong> ~$189,000 from $54,000 contributed</li>
    <li><strong>40 years:</strong> ~$400,000 from $72,000 contributed</li>
  </ul>
  <p>You contribute $72,000 over 40 years and the market grows it to $400,000. That's $328,000 you didn't work for — it's money your money made for you.</p>

  <h2>Why Acorns Works for Compound Growth</h2>
  <ul>
    <li><strong>Automatic dividend reinvestment</strong> — dividends buy more shares automatically, accelerating compounding</li>
    <li><strong>Consistent contributions</strong> — Round-Ups and recurring investments ensure you never miss a contribution</li>
    <li><strong>Low-cost ETFs</strong> — Vanguard and iShares ETFs have expense ratios as low as 0.03%, leaving more for compound growth</li>
    <li><strong>It removes emotion</strong> — automatic investing prevents you from pulling out during market dips, which is when compound investors capture the best long-term gains</li>
  </ul>
</section>
"""
))

# ══════════════════════════════════════════════════════════════
# SUPPORT FILES
# ══════════════════════════════════════════════════════════════

def build_sitemap(pages):
    urls=[]
    for p in pages:
        s=p["slug"]
        loc=f"{BASE_URL}/" if s=="index" else f"{BASE_URL}/{s}.html"
        pri="1.0" if s=="index" else "0.8"
        urls.append(f'  <url><loc>{loc}</loc><lastmod>{BUILT_ON}</lastmod><changefreq>weekly</changefreq><priority>{pri}</priority></url>')
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"\n".join(urls)+"\n</urlset>"

ROBOTS=f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n"

def build_llms(pages):
    lines=[f"# {SITE_NAME}","","> AcornsGuide is an independent Acorns investing review and comparison site for US investors. Reviews, fee breakdowns, competitor comparisons, and sign-up guides.","","## Pages",""]
    for p in pages:
        s=p["slug"]
        loc=f"{BASE_URL}/" if s=="index" else f"{BASE_URL}/{s}.html"
        lines.append(f"- [{p['title']}]({loc}) — {p['desc'][:90]}")
    lines+=["","## Affiliate Disclosure","","AcornsGuide earns commissions when users sign up through our links. All links are clearly disclosed. Investing involves risk. Not financial advice."]
    return "\n".join(lines)

PAGE_404=f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>404 — Page Not Found | AcornsGuide</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<style>{CSS}
.e{{text-align:center;padding:120px 24px}}
.e .n{{font-size:9rem;font-weight:900;color:var(--green);line-height:1;opacity:0.5;font-family:'Outfit',sans-serif}}
.e h2{{font-size:1.6rem;font-weight:800;color:#fff;margin:12px 0 8px}}
.e p{{color:var(--muted);margin-bottom:30px}}
</style>
</head>
<body>
{nav_html()}
<div class="e">
  <div class="n">404</div>
  <h2>Page not found.</h2>
  <p>But your first Acorns investment is just one click away.</p>
  <a href="index.html" class="cta">← Back to AcornsGuide</a>
</div>
</body>
</html>"""

# ══════════════════════════════════════════════════════════════
# BUILD
# ══════════════════════════════════════════════════════════════
def build():
    print(f"\nAcornsGuide — Full Build\nBuilding {len(PAGES)} pages → {OUT}/\n")
    for p in PAGES:
        s=p["slug"]
        fname="index.html" if s=="index" else f"{s}.html"
        html=page(
            slug=s,title=p["title"],desc=p["desc"],kw=p["kw"],
            h1=p["h1"],tag=p["tag"],hero_cta=p["hero_cta"],
            body=p["body"],faqs=p.get("faqs"),crumbs=p.get("crumbs")
        )
        (OUT/fname).write_text(html,encoding="utf-8")
        print(f"  ✅  {fname}")
    (OUT/"sitemap.xml").write_text(build_sitemap(PAGES),encoding="utf-8")
    print("  ✅  sitemap.xml")
    (OUT/"robots.txt").write_text(ROBOTS,encoding="utf-8")
    print("  ✅  robots.txt")
    (OUT/"llms.txt").write_text(build_llms(PAGES),encoding="utf-8")
    print("  ✅  llms.txt")
    (OUT/"404.html").write_text(PAGE_404,encoding="utf-8")
    print("  ✅  404.html")
    print(f"\n🌱  Done! {len(PAGES)} pages + 4 support files → ./{OUT}/")
    print(f"    Deploy → https://brightlane.github.io/acorns.com/\n")

if __name__ == "__main__":
    build()
