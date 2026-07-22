#!/usr/bin/env python3
"""Builds dashboard.html (self-contained, no external deps) from data.json.

Run after fetch_all.py. The GitHub Actions cron does: fetch -> build -> commit,
so the committed dashboard.html is always the freshest snapshot. The page is
static; a <meta refresh> makes an open browser tab re-read the file periodically
so a locally-served copy stays current without any JS.
"""
import html
import json, os, re
from datetime import datetime, timedelta, timezone

IST = timezone(timedelta(hours=5, minutes=30))
HERE = os.path.dirname(os.path.abspath(__file__))

STUDIO = "Divya Jyot V3 June26"
BHK2 = "Divya Jyot V3 July 26 - 2BHK"
SHORT = {STUDIO: "Studio", BHK2: "2BHK"}
BASELINE_VISIT_RATE = 4.5  # % — historical V3 baseline

def normphone(p):
    d = "".join(ch for ch in str(p) if ch.isdigit())
    return d[-10:] if len(d) >= 10 else d

def parse_dmy(s, today):
    s = (s or "").strip()
    for fmt in ("%d/%m/%Y", "%m/%d/%Y"):
        try:
            dt = datetime.strptime(s, fmt).date()
            if datetime(2024, 1, 1).date() <= dt <= today:
                return dt
        except ValueError:
            pass
    return None

def esc(s):
    return html.escape(str(s), quote=True)

def rupees(x):
    return f"₹{x:,.0f}"

def build():
    with open(os.path.join(HERE, "data.json")) as f:
        d = json.load(f)
    now = datetime.now(IST)
    today = now.date()

    leads = d["sheet"]["meta_leads_timed"]
    fb_tab = d["sheet"]["facebook_tab"]
    svd = d["sheet"]["svd_tab"]
    ch = d["sheet"].get("contact_history", {}) or {}
    crm_by_phone = {l["phone10"]: l for l in leads if l["phone10"]}

    # ---- daily series (last 14 days shown) ----
    daily = [r for r in d["meta"].get("last30_daily_campaigns", []) if r.get("date")]
    days = sorted({r["date"] for r in daily})[-14:]
    series = {c: {dt: {"spend": 0.0, "leads": 0} for dt in days} for c in (STUDIO, BHK2)}
    for r in daily:
        c, dt = r.get("campaign"), r.get("date")
        if c in series and dt in series[c]:
            series[c][dt]["spend"] += r.get("spend", 0) or 0
            series[c][dt]["leads"] += r.get("leads", 0) or 0

    # ---- today / yesterday tiles ----
    def agg(rows):
        out = {}
        for r in rows:
            if "error" in r:
                continue
            out[r.get("campaign")] = r
        return out
    t = agg(d["meta"]["today_campaigns"])
    y = agg(d["meta"]["yesterday_campaigns"])
    l30 = d["meta"]["last30_ads"]
    spend_today = sum(r.get("spend", 0) for r in t.values())
    leads_today = sum(r.get("leads", 0) for r in t.values())
    spend30 = sum(r.get("spend", 0) for r in l30 if "error" not in r)
    leads30 = sum(r.get("leads", 0) for r in l30 if "error" not in r)

    # ---- SVD verification, last 30 days ----
    hdr = [h.strip().lower() for h in svd[0]]
    def col(name):
        return hdr.index(name)
    i_src, i_name, i_num, i_date = col("source"), col("name"), col("number"), col("visit date")
    cutoff30 = today - timedelta(days=30)
    KNOWN_BAD = {"8976779929": "pre-V3 lead (Apr) — not a V3 result",
                 "9673213241": "never a Meta lead (Dedhia case, 4 Jul)"}
    ANNOTATED_OK = {"9372158643": "relative's phone; team-annotated {Sushma} — ties to real CRM lead"}
    visits = []
    for r in svd[1:]:
        if len(r) <= i_num:
            continue
        vd = parse_dmy(r[i_date] if len(r) > i_date else "", today)
        if not vd or vd < cutoff30 or "facebook" not in (r[i_src] if len(r) > i_src else "").lower():
            continue
        ph = normphone(r[i_num])
        crm = crm_by_phone.get(ph)
        if crm:
            status, note = "verified", SHORT.get(crm["campaign"], crm["campaign"])
        elif ph in KNOWN_BAD:
            status, note = "bad", KNOWN_BAD[ph]
        elif ph in ANNOTATED_OK:
            status, note = "annotated", ANNOTATED_OK[ph]
        else:
            status, note = "unverified", "no CRM record in any tab — ask the team"
        visits.append({"date": vd.isoformat(), "name": (r[i_name] or "").strip(),
                       "phone": ph, "status": status, "note": note})
    n_ver = sum(1 for v in visits if v["status"] in ("verified", "annotated"))
    cost_per_visit = spend30 / n_ver if n_ver else None
    visit_rate = 100.0 * n_ver / leads30 if leads30 else None

    # ---- Facebook-tab match rate, last 30 days ----
    fhdr = [h.strip().lower() for h in fb_tab[0]]
    fi_created, fi_name, fi_phone = fhdr.index("created"), fhdr.index("name"), fhdr.index("phone")
    total_fb = matched_fb = 0
    fb_phones = set()
    for r in fb_tab[1:]:
        if len(r) <= fi_phone:
            continue
        ph = normphone(r[fi_phone])
        if ph:
            fb_phones.add(ph)
        dt = parse_dmy(r[fi_created], today)
        if not ph or not dt or dt < cutoff30:
            continue
        total_fb += 1
        if ph in crm_by_phone:
            matched_fb += 1
    match_rate = 100.0 * matched_fb / total_fb if total_fb else None

    # ---- speed-to-lead, last 48h ----
    cutoff48 = (now - timedelta(hours=48)).strftime("%Y-%m-%d %H:%M:%S")
    recent = sorted((l for l in leads if l["created_time_ist"] >= cutoff48),
                    key=lambda l: l["created_time_ist"], reverse=True)
    ch_leads = ch.get("leads", {}) or {}
    speed_rows = []
    for l in recent:
        info = ch_leads.get(l["phone10"]) or {}
        fb_seen = l["phone10"] in fb_phones
        br = info.get("feedback_appeared_between")
        if br and br[1]:
            try:
                by = datetime.strptime(br[1], "%Y-%m-%d %H:%M:%S")
                arr = datetime.strptime(l["created_time_ist"], "%Y-%m-%d %H:%M:%S")
                mins = int((by - arr).total_seconds() // 60)
                if mins < 0:
                    # bracket predates arrival = the phone was already in the sheet
                    # before this lead came in (a returning/repeat lead)
                    lag, st = "repeat lead (row pre-exists)", "ok"
                else:
                    lag = f"≤ {mins//60}h{mins%60:02d}m" if mins >= 60 else f"≤ {mins}m"
                    st = "ok"
            except ValueError:
                lag, st = "in sheet (time unknown)", "ok"
        elif info and info.get("feedback_appeared_between") is None and info.get("row_appeared_between") is None and not fb_seen:
            lag, st = "NOT in sheet yet", "warn"
        elif fb_seen:
            lag, st = "in sheet (day-level)", "ok"
        else:
            lag, st = "NOT in sheet yet", "warn"
        speed_rows.append({"name": l["name"], "campaign": SHORT.get(l["campaign"], l["campaign"]),
                           "arrived": l["created_time_ist"][5:16], "intent": l.get("intent", ""),
                           "budget": l.get("budget", ""), "lag": lag, "status": st})

    # ---- open integrity flags (curated, standing) ----
    flags = []
    for v in visits:
        if v["status"] == "unverified":
            flags.append(("serious", f"SVD visit {v['date']} — {esc(v['name'])} ({v['phone']}): "
                                     f"no CRM record in any tab, but conversion was pushed to Meta."))
        elif v["status"] == "bad":
            flags.append(("critical", f"SVD visit {v['date']} — {esc(v['name'])} ({v['phone']}): {v['note']}; "
                                      f"conversion pushed to Meta pollutes optimization."))
    # live phone-typo check: CRM lead whose exact phone is absent from the FB tab but a
    # 1-digit-off variant is present
    for l in leads:
        if l["created_time_ist"][:10] < (today - timedelta(days=3)).isoformat():
            continue
        p = l["phone10"]
        if not p or p in fb_phones:
            continue
        near = [q for q in fb_phones if len(q) == 10 and sum(a != b for a, b in zip(p, q)) == 1]
        if near:
            flags.append(("serious", f"Phone typo suspected: CRM lead {esc(l['name'])} is {p}, "
                                     f"sheet has {near[0]} — team may be dialing a wrong number."))

    # ---- charts (inline SVG) ----
    W, H, PAD_L, PAD_B, PAD_T = 660, 200, 44, 26, 12
    plot_w, plot_h = W - PAD_L - 12, H - PAD_B - PAD_T

    def nice_max(v):
        if v <= 0: return 1
        for m in (1, 2, 2.5, 5, 10, 20, 25, 50, 100, 200, 250, 500, 1000, 2000, 2500, 5000):
            if m >= v: return m
        return v

    def bars_chart(metric, fmt):
        mx = nice_max(max((series[c][dt][metric] for c in series for dt in days), default=1))
        n = len(days)
        group_w = plot_w / max(n, 1)
        bar_w = max(4.0, (group_w - 6) / 2)
        parts = []
        for gi, yv in enumerate((0, mx / 2, mx)):
            yy = PAD_T + plot_h - plot_h * (yv / mx)
            parts.append(f'<line x1="{PAD_L}" y1="{yy:.1f}" x2="{W-12}" y2="{yy:.1f}" class="grid"/>' if gi else '')
            parts.append(f'<text x="{PAD_L-6}" y="{yy+4:.1f}" class="tick" text-anchor="end">{fmt(yv)}</text>')
        for i, dt in enumerate(days):
            x0 = PAD_L + i * group_w + (group_w - 2 * bar_w - 2) / 2
            for si, c in enumerate((STUDIO, BHK2)):
                v = series[c][dt][metric]
                bh = plot_h * (v / mx)
                bx, by = x0 + si * (bar_w + 2), PAD_T + plot_h - bh
                label = f"{dt[5:]} · {SHORT[c]}: {fmt(v)}"
                parts.append(
                    f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bar_w:.1f}" height="{max(bh,0):.1f}" '
                    f'rx="2" class="s{si+1}"><title>{esc(label)}</title></rect>')
            if i % 2 == (len(days) - 1) % 2:
                parts.append(f'<text x="{x0 + bar_w:.1f}" y="{H-8}" class="tick" text-anchor="middle">{dt[8:]}/{int(dt[5:7])}</text>')
        parts.append(f'<line x1="{PAD_L}" y1="{PAD_T+plot_h}" x2="{W-12}" y2="{PAD_T+plot_h}" class="axis"/>')
        return f'<svg viewBox="0 0 {W} {H}" role="img">{"".join(parts)}</svg>'

    leads_svg = bars_chart("leads", lambda v: f"{v:g}")
    spend_svg = bars_chart("spend", lambda v: f"₹{v/1000:g}k" if v >= 1000 else f"₹{v:g}")

    # ---- campaign summary table ----
    def row_for(c):
        tt, yy = t.get(c, {}), y.get(c, {})
        l30c = [r for r in l30 if r.get("campaign") == c]
        s30 = sum(r.get("spend", 0) for r in l30c); ld30 = sum(r.get("leads", 0) for r in l30c)
        return {
            "name": SHORT.get(c, c),
            "t_spend": tt.get("spend", 0), "t_leads": tt.get("leads", 0),
            "t_cpl": tt.get("cpl"), "t_ctr": tt.get("ctr"), "t_freq": tt.get("frequency"),
            "y_spend": yy.get("spend", 0), "y_leads": yy.get("leads", 0),
            "s30": s30, "l30": ld30, "cpl30": (s30 / ld30) if ld30 else None,
        }
    camp_rows = [row_for(STUDIO), row_for(BHK2)]

    def fmt_or(v, fmt="{:.0f}", dash="—"):
        return fmt.format(v) if v not in (None, 0) or (isinstance(v, (int, float)) and v == 0 and "{" in fmt) else dash

    status_dot = {"ok": ("good", "✓"), "warn": ("serious", "⚠"),
                  "verified": ("good", "✓"), "annotated": ("good", "✓"),
                  "unverified": ("serious", "⚠"), "bad": ("critical", "✗")}

    speed_html = "".join(
        f'<tr><td>{esc(r["name"])}</td><td><span class="chip {"c1" if r["campaign"]=="Studio" else "c2"}">{r["campaign"]}</span></td>'
        f'<td class="num">{r["arrived"]}</td><td>{esc(r["intent"])}</td><td>{esc(r["budget"] or "—")}</td>'
        f'<td class="st-{status_dot[r["status"]][0]}">{status_dot[r["status"]][1]} {esc(r["lag"])}</td></tr>'
        for r in speed_rows) or '<tr><td colspan="6" class="muted">No leads in the last 48 hours.</td></tr>'

    visits_html = "".join(
        f'<tr><td class="num">{v["date"]}</td><td>{esc(v["name"])}</td><td class="num">{v["phone"]}</td>'
        f'<td class="st-{status_dot[v["status"]][0]}">{status_dot[v["status"]][1]} {esc(v["note"])}</td></tr>'
        for v in sorted(visits, key=lambda v: v["date"], reverse=True))

    flags_html = "".join(
        f'<li class="flag-{sev}"><span class="flag-ico">{"✗" if sev=="critical" else "⚠"}</span> {msg}</li>'
        for sev, msg in flags) or '<li class="muted">No open integrity flags. ✓</li>'

    camp_html = "".join(
        f'<tr><td><span class="chip {"c1" if r["name"]=="Studio" else "c2"}">{r["name"]}</span></td>'
        f'<td class="num">{rupees(r["t_spend"])}</td><td class="num">{r["t_leads"]}</td>'
        f'<td class="num">{fmt_or(r["t_cpl"], "₹{:.0f}")}</td>'
        f'<td class="num">{fmt_or(r["t_ctr"], "{:.2f}%")}</td><td class="num">{fmt_or(r["t_freq"], "{:.2f}")}</td>'
        f'<td class="num">{rupees(r["y_spend"])}</td><td class="num">{r["y_leads"]}</td>'
        f'<td class="num">{rupees(r["s30"])}</td><td class="num">{r["l30"]}</td>'
        f'<td class="num">{fmt_or(r["cpl30"], "₹{:.0f}")}</td></tr>'
        for r in camp_rows)

    vr_txt = f"{visit_rate:.1f}%" if visit_rate is not None else "—"
    vr_delta = ""
    if visit_rate is not None:
        good = visit_rate >= BASELINE_VISIT_RATE
        vr_delta = (f'<div class="delta {"up" if good else "down"}">'
                    f'{"▲" if good else "▼"} baseline {BASELINE_VISIT_RATE}%</div>')

    page = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="900">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Divya Jyot — Meta Ads Live Dashboard</title>
<style>
:root {{
  color-scheme: light;
  --surface: #fcfcfb; --page: #f9f9f7; --ink: #0b0b0b; --ink2: #52514e;
  --muted: #898781; --grid: #e1e0d9; --axis: #c3c2b7; --border: rgba(11,11,11,.10);
  --s1: #2a78d6; --s2: #eb6834;
  --good: #0ca30c; --serious: #ec835a; --critical: #d03b3b; --good-text: #006300;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  color-scheme: dark;
  --surface: #1a1a19; --page: #0d0d0d; --ink: #ffffff; --ink2: #c3c2b7;
  --muted: #898781; --grid: #2c2c2a; --axis: #383835; --border: rgba(255,255,255,.10);
  --s1: #3987e5; --s2: #d95926; --good-text: #0ca30c;
}} }}
:root[data-theme="dark"] {{
  color-scheme: dark;
  --surface: #1a1a19; --page: #0d0d0d; --ink: #ffffff; --ink2: #c3c2b7;
  --muted: #898781; --grid: #2c2c2a; --axis: #383835; --border: rgba(255,255,255,.10);
  --s1: #3987e5; --s2: #d95926; --good-text: #0ca30c;
}}
* {{ box-sizing: border-box; margin: 0; }}
body {{ background: var(--page); color: var(--ink);
  font: 14px/1.45 system-ui, -apple-system, "Segoe UI", sans-serif; padding: 20px; }}
.wrap {{ max-width: 1080px; margin: 0 auto; }}
header {{ display: flex; flex-wrap: wrap; align-items: baseline; gap: 10px; margin-bottom: 18px; }}
h1 {{ font-size: 19px; font-weight: 650; }}
.updated {{ color: var(--ink2); font-size: 13px; }}
h2 {{ font-size: 13px; font-weight: 600; color: var(--ink2); text-transform: uppercase;
  letter-spacing: .04em; margin: 26px 0 10px; }}
.tiles {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; }}
.tile {{ background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 12px 14px; }}
.tile .k {{ font-size: 12px; color: var(--ink2); margin-bottom: 4px; }}
.tile .v {{ font-size: 24px; font-weight: 650; }}
.tile .sub {{ font-size: 12px; color: var(--muted); margin-top: 2px; }}
.delta {{ font-size: 12px; margin-top: 2px; }}
.delta.up {{ color: var(--good-text); }} .delta.down {{ color: var(--critical); }}
.cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 12px; }}
.card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 14px; }}
.card h3 {{ font-size: 13px; font-weight: 600; margin-bottom: 8px; }}
.legend {{ display: flex; gap: 14px; font-size: 12px; color: var(--ink2); margin-bottom: 6px; }}
.legend i {{ display: inline-block; width: 10px; height: 10px; border-radius: 3px; margin-right: 5px; vertical-align: -1px; }}
svg {{ width: 100%; height: auto; display: block; }}
.grid {{ stroke: var(--grid); stroke-width: 1; }}
.axis {{ stroke: var(--axis); stroke-width: 1; }}
.tick {{ fill: var(--muted); font-size: 10px; font-variant-numeric: tabular-nums; }}
.s1 {{ fill: var(--s1); }} .s2 {{ fill: var(--s2); }}
rect.s1:hover, rect.s2:hover {{ opacity: .8; }}
.tablewrap {{ overflow-x: auto; background: var(--surface); border: 1px solid var(--border); border-radius: 10px; }}
table {{ border-collapse: collapse; width: 100%; font-size: 13px; }}
th {{ text-align: left; color: var(--ink2); font-weight: 600; font-size: 12px; }}
th, td {{ padding: 8px 12px; border-bottom: 1px solid var(--grid); white-space: nowrap; }}
tr:last-child td {{ border-bottom: 0; }}
td.num, th.num {{ font-variant-numeric: tabular-nums; }}
.chip {{ display: inline-block; padding: 1px 8px; border-radius: 999px; font-size: 12px; font-weight: 600; color: #fff; }}
.chip.c1 {{ background: var(--s1); }} .chip.c2 {{ background: var(--s2); }}
.st-good {{ color: var(--good-text); }} .st-serious {{ color: var(--critical); }} .st-critical {{ color: var(--critical); font-weight: 600; }}
.muted {{ color: var(--muted); }}
ul.flags {{ list-style: none; display: grid; gap: 8px; }}
ul.flags li {{ background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
  padding: 10px 12px; font-size: 13px; }}
li.flag-critical {{ border-left: 3px solid var(--critical); }}
li.flag-serious {{ border-left: 3px solid var(--serious); }}
.flag-ico {{ margin-right: 4px; }}
footer {{ margin-top: 26px; color: var(--muted); font-size: 12px; }}
</style></head><body><div class="wrap">
<header>
  <h1>Divya Jyot LYF Rewa — Meta Ads</h1>
  <span class="updated">Updated {now.strftime("%a %d %b %Y, %H:%M IST")} · auto-rebuilds every 4h · tab refreshes every 15m</span>
</header>

<div class="tiles">
  <div class="tile"><div class="k">Spend today (so far)</div><div class="v">{rupees(spend_today)}</div></div>
  <div class="tile"><div class="k">Leads today</div><div class="v">{leads_today}</div>
    <div class="sub">Studio {t.get(STUDIO,{}).get("leads",0)} · 2BHK {t.get(BHK2,{}).get("leads",0)}</div></div>
  <div class="tile"><div class="k">Blended CPL today</div>
    <div class="v">{rupees(spend_today/leads_today) if leads_today else "—"}</div></div>
  <div class="tile"><div class="k">Cost / verified visit (30d)</div>
    <div class="v">{rupees(cost_per_visit) if cost_per_visit else "—"}</div>
    <div class="sub">{n_ver} CRM-verified visits</div></div>
  <div class="tile"><div class="k">Visit rate (30d)</div><div class="v">{vr_txt}</div>{vr_delta}</div>
  <div class="tile"><div class="k">Sheet↔CRM match (30d)</div>
    <div class="v">{f"{match_rate:.0f}%" if match_rate is not None else "—"}</div>
    <div class="sub">{matched_fb}/{total_fb} rows matched</div></div>
</div>

<h2>Last 14 days</h2>
<div class="cards">
  <div class="card"><h3>Leads per day</h3>
    <div class="legend"><span><i style="background:var(--s1)"></i>Studio</span><span><i style="background:var(--s2)"></i>2BHK</span></div>
    {leads_svg}</div>
  <div class="card"><h3>Spend per day</h3>
    <div class="legend"><span><i style="background:var(--s1)"></i>Studio</span><span><i style="background:var(--s2)"></i>2BHK</span></div>
    {spend_svg}</div>
</div>

<h2>Campaigns</h2>
<div class="tablewrap"><table>
<thead><tr><th>Campaign</th><th class="num">Spend today</th><th class="num">Leads</th><th class="num">CPL</th>
<th class="num">CTR</th><th class="num">Freq</th><th class="num">Spend yday</th><th class="num">Leads yday</th>
<th class="num">Spend 30d</th><th class="num">Leads 30d</th><th class="num">CPL 30d</th></tr></thead>
<tbody>{camp_html}</tbody></table></div>

<h2>Speed to lead — last 48 hours</h2>
<div class="tablewrap"><table>
<thead><tr><th>Lead</th><th>Campaign</th><th class="num">Arrived (IST)</th><th>Intent</th><th>Budget</th><th>Contacted</th></tr></thead>
<tbody>{speed_html}</tbody></table></div>

<h2>Site visits — last 30 days (SVD vs CRM)</h2>
<div class="tablewrap"><table>
<thead><tr><th class="num">Date</th><th>Name</th><th class="num">Phone</th><th>Verification</th></tr></thead>
<tbody>{visits_html}</tbody></table></div>

<h2>Open integrity flags</h2>
<ul class="flags">{flags_html}</ul>

<footer>Verified visit = phone matches an OTP-verified CRM lead (either form tab). Contact lag comes from
Drive revision history of the team sheet — brackets, not exact call times. Source of truth for leads:
CRM Event sheet; for visits: SVD tab cross-checked against CRM. Baseline visit rate {BASELINE_VISIT_RATE}%.</footer>
</div></body></html>"""

    out = os.path.join(HERE, "dashboard.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Wrote dashboard.html ({len(page):,} bytes, {len(visits)} visits, {len(speed_rows)} recent leads, {len(flags)} flags)")

if __name__ == "__main__":
    build()
