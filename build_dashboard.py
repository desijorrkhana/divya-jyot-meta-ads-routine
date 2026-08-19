#!/usr/bin/env python3
"""Builds dashboard.html (self-contained, no external deps) from data.json.

Run after fetch_all.py. The GitHub Actions cron does: fetch -> build -> commit,
so the committed dashboard.html is always the freshest snapshot. All raw series
are embedded as JSON and rendered client-side, so the date-range filter works
offline with no server. Every reports/YYYY-MM-DD.md is embedded in the Reports
section, so the archive travels with the file.
"""
import html
import json, os, re, glob
from datetime import datetime, timedelta, timezone

IST = timezone(timedelta(hours=5, minutes=30))
HERE = os.path.dirname(os.path.abspath(__file__))

STUDIO = "Divya Jyot V3 June26"
BHK2 = "Divya Jyot V3 July 26 - 2BHK"
BHK1 = "Divya Jyot V4 Aug26 - 1BHK"
# Short display names, in a fixed display order — this dict IS the campaign list.
# A new campaign just needs one entry here; every chart/table/legend below is
# built from this dict's values (and its position gives it the next color/chip
# class), so nothing else needs to change when a 4th campaign launches.
SHORT = {STUDIO: "Studio", BHK2: "2BHK", BHK1: "1BHK"}
CAMPS = list(SHORT.values())
V3_START = "2026-06-10"
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

def md_lite(text):
    """Very small markdown renderer for the embedded reports: headings, bold,
    bullets; markdown tables and anything indented stay monospace."""
    out, in_pre = [], False
    for ln in text.split("\n"):
        table_ln = ln.lstrip().startswith("|")
        if table_ln and not in_pre:
            out.append('<pre class="mdtable">'); in_pre = True
        if not table_ln and in_pre:
            out.append("</pre>"); in_pre = False
        if in_pre:
            out.append(esc(ln)); continue
        s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", esc(ln))
        if ln.startswith("### "):  out.append(f"<h5>{s[4:]}</h5>")
        elif ln.startswith("## "): out.append(f"<h4>{s[3:]}</h4>")
        elif ln.startswith("# "):  out.append(f"<h3>{s[2:]}</h3>")
        elif ln.startswith("- "):  out.append(f'<div class="li">• {s[2:]}</div>')
        elif ln.strip() in ("---", "***"): out.append("<hr>")
        elif not ln.strip():       out.append('<div class="gap"></div>')
        else:                      out.append(f"<div>{s}</div>")
    if in_pre:
        out.append("</pre>")
    return "\n".join(out)

def build():
    with open(os.path.join(HERE, "data.json")) as f:
        d = json.load(f)
    now = datetime.now(IST)
    today = now.date()

    leads = d["sheet"]["meta_leads_timed"]
    if not leads:
        # An empty CRM makes every visit look unverified and every lead untracked —
        # a dashboard built on that is actively misleading. Fail the build instead.
        raise SystemExit(f"CRM leads empty (meta_leads_error={d['sheet'].get('meta_leads_error')!r}) "
                         "— refusing to build a misleading dashboard")
    fb_tab = d["sheet"]["facebook_tab"]
    svd = d["sheet"]["svd_tab"]
    ch = d["sheet"].get("contact_history", {}) or {}
    ch_leads = ch.get("leads", {}) or {}
    crm_by_phone = {l["phone10"]: l for l in leads if l["phone10"]}

    # ---- Facebook tab: phone -> sorted list of row-created dates (for day-level contact) ----
    fhdr = [h.strip().lower() for h in fb_tab[0]]
    fi_created, fi_phone = fhdr.index("created"), fhdr.index("phone")
    fi_name = fhdr.index("name") if "name" in fhdr else None
    fi_status = fhdr.index("status") if "status" in fhdr else None
    fb_dates_by_phone = {}
    for r in fb_tab[1:]:
        if len(r) <= fi_phone:
            continue
        ph = normphone(r[fi_phone])
        dt = parse_dmy(r[fi_created], today)
        if ph:
            fb_dates_by_phone.setdefault(ph, [])
            if dt:
                fb_dates_by_phone[ph].append(dt.isoformat())
    for v in fb_dates_by_phone.values():
        v.sort()

    # ---- per-lead contact assessment (display strings prebuilt; JS only filters) ----
    def contact_for(l):
        ph, arr_s = l["phone10"], l["created_time_ist"]
        arr_date = arr_s[:10]
        info = ch_leads.get(ph) or {}
        br = info.get("feedback_appeared_between")
        if br and br[1]:
            try:
                by = datetime.strptime(br[1], "%Y-%m-%d %H:%M:%S")
                arr = datetime.strptime(arr_s, "%Y-%m-%d %H:%M:%S")
                mins = int((by - arr).total_seconds() // 60)
                if mins < 0:
                    return "row pre-exists (repeat lead)", "repeat lead", "ok"
                lag = f"≤ {mins//60}h{mins%60:02d}m" if mins >= 60 else f"≤ {mins}m"
                return f"by {br[1][5:16]}", lag, "ok"
            except ValueError:
                pass
        dates = fb_dates_by_phone.get(ph)
        if dates is not None:  # phone appears in the sheet
            same_or_after = [x for x in dates if x >= arr_date]
            if same_or_after:
                dd = same_or_after[0]
                gap = (datetime.fromisoformat(dd).date() - datetime.fromisoformat(arr_date).date()).days
                lag = "same day" if gap == 0 else f"+{gap}d"
                return f"on {dd} (day-level)", lag, "ok" if gap <= 1 else "warn"
            return "older row only (repeat?)", "day-level unknown", "ok"
        if arr_date >= (today - timedelta(days=2)).isoformat():
            return "—", "NOT in sheet yet", "warn"
        return "—", "never logged", "warn"

    crm_rows = []
    for l in sorted(leads, key=lambda x: x["created_time_ist"], reverse=True):
        if l["created_time_ist"][:10] < V3_START:
            continue
        logged, lag, st = contact_for(l)
        crm_rows.append({
            "ts": l["created_time_ist"], "name": l["name"],
            "camp": SHORT.get(l["campaign"], l["campaign"] or "?"),
            "intent": l.get("intent", ""), "budget": l.get("budget", ""),
            "phone": l["phone10"], "logged": logged, "lag": lag, "st": st,
        })

    # A recent facebook_tab lead with a real phone but no CRM match (see the matching flag
    # above) needs to show up here too — this table, not the flags list, is what gets checked
    # day to day. There's no CRM arrival time to measure a real lag against, so it's shown
    # day-level only with the campaign left honestly unattributed rather than guessed.
    if fi_name is not None:
        unsynced_cutoff = today - timedelta(days=2)
        for r in fb_tab[1:]:
            if len(r) <= fi_phone:
                continue
            ph = normphone(r[fi_phone] or "")
            if not ph or ph in crm_by_phone:
                continue
            dt = parse_dmy(r[fi_created], today)
            if not dt or dt < unsynced_cutoff:
                continue
            nm = (r[fi_name] if len(r) > fi_name else "").strip() or "(no name)"
            crm_rows.append({
                "ts": dt.isoformat(), "name": f"{nm} ⚠", "camp": "Unsynced",
                "intent": "", "budget": "",
                "phone": ph, "logged": "not in CRM — see team sheet", "lag": "not computable", "st": "warn",
            })

    # ---- daily meta series (30d, per campaign, with clicks/impressions for range aggregates) ----
    daily = []
    for r in d["meta"].get("last30_daily_campaigns", []):
        if r.get("date") and r.get("campaign") in SHORT:
            daily.append({"date": r["date"], "camp": SHORT[r["campaign"]],
                          "spend": r.get("spend", 0) or 0, "leads": r.get("leads", 0) or 0,
                          "imp": r.get("impressions", 0) or 0, "clicks": r.get("clicks", 0) or 0,
                          "link": r.get("link_clicks", 0) or 0})
    daily_min = min((r["date"] for r in daily), default=today.isoformat())

    # ---- daily per-ad series (30d) for the ad-level range table ----
    daily_ads = []
    for r in d["meta"].get("last30_daily_ads", []):
        if r.get("date") and r.get("campaign") in SHORT and r.get("ad"):
            daily_ads.append({"date": r["date"], "camp": SHORT[r["campaign"]],
                              "ad": r["ad"], "adset": r.get("adset") or "",
                              "spend": r.get("spend", 0) or 0, "leads": r.get("leads", 0) or 0,
                              "imp": r.get("impressions", 0) or 0, "clicks": r.get("clicks", 0) or 0})

    # ---- SVD verification (all rows since 2024; JS filters by range) ----
    hdr = [h.strip().lower() for h in svd[0]]
    i_src, i_name, i_num, i_date = hdr.index("source"), hdr.index("name"), hdr.index("number"), hdr.index("visit date")
    KNOWN_BAD = {"8976779929": "pre-V3 lead (Apr) — not a V3 result",
                 "9673213241": "never a Meta lead (Dedhia case, 4 Jul)"}
    ANNOTATED_OK = {"9372158643": "relative's phone; team-annotated {Sushma} — ties to real CRM lead"}
    visits = []
    for r in svd[1:]:
        if len(r) <= i_num:
            continue
        vd = parse_dmy(r[i_date] if len(r) > i_date else "", today)
        if not vd or "facebook" not in (r[i_src] if len(r) > i_src else "").lower():
            continue
        ph = normphone(r[i_num])
        crm = crm_by_phone.get(ph)
        if crm:
            status, note = "verified", SHORT.get(crm["campaign"], crm["campaign"])
        elif ph in KNOWN_BAD:
            status, note = "bad", KNOWN_BAD[ph]
        elif ph in ANNOTATED_OK:
            status, note = "annotated", ANNOTATED_OK[ph]
        elif vd.isoformat() < V3_START:
            status, note = "prev3", "pre-V3 era visit (informational)"
        else:
            status, note = "unverified", "no CRM record in any tab — ask the team"
        visits.append({"date": vd.isoformat(), "name": (r[i_name] or "").strip(),
                       "phone": ph, "status": status, "note": note})

    # ---- fixed-window tiles (today + trailing 30d) ----
    def agg(rows):
        return {r.get("campaign"): r for r in rows if "error" not in r}
    t = agg(d["meta"]["today_campaigns"])
    l30rows = [r for r in d["meta"]["last30_ads"] if "error" not in r]
    spend_today = sum(r.get("spend", 0) for r in t.values())
    leads_today = sum(r.get("leads", 0) for r in t.values())
    spend30 = sum(r.get("spend", 0) for r in l30rows)
    leads30 = sum(r.get("leads", 0) for r in l30rows)
    cutoff30 = (today - timedelta(days=30)).isoformat()
    v30 = [v for v in visits if v["date"] >= cutoff30]
    n_ver = sum(1 for v in v30 if v["status"] in ("verified", "annotated"))
    cost_per_visit = spend30 / n_ver if n_ver else None
    visit_rate = 100.0 * n_ver / leads30 if leads30 else None
    total_fb = matched_fb = 0
    for r in fb_tab[1:]:
        if len(r) <= fi_phone:
            continue
        ph = normphone(r[fi_phone]); dt = parse_dmy(r[fi_created], today)
        if not ph or not dt or dt.isoformat() < cutoff30:
            continue
        total_fb += 1
        matched_fb += 1 if ph in crm_by_phone else 0
    match_rate = 100.0 * matched_fb / total_fb if total_fb else None

    # ---- open integrity flags ----
    flags = []
    for v in v30:
        if v["status"] == "unverified":
            flags.append(("serious", f"SVD visit {v['date']} — {esc(v['name'])} ({v['phone']}): "
                                     f"no CRM record in any tab, but conversion was pushed to Meta."))
        elif v["status"] == "bad":
            flags.append(("critical", f"SVD visit {v['date']} — {esc(v['name'])} ({v['phone']}): {v['note']}; "
                                      f"conversion pushed to Meta pollutes optimization."))
    fb_phones = set(fb_dates_by_phone)
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
    # Leads logged with a placeholder/blank phone (e.g. a form missing the phone question) are
    # invisible everywhere else on this dashboard, since every table above is keyed by phone10 —
    # surface them here by name instead so real spend on an uncallable lead never goes unseen.
    if fi_name is not None:
        no_phone_cutoff = (today - timedelta(days=7)).isoformat()
        for r in fb_tab[1:]:
            if len(r) <= fi_phone:
                continue
            raw_phone = r[fi_phone] or ""
            if normphone(raw_phone) or any(c.isdigit() for c in str(raw_phone)):
                continue  # has a usable or at least partially-digit number — not this case
            dt = parse_dmy(r[fi_created], today)
            if not dt or dt.isoformat() < no_phone_cutoff:
                continue
            nm = (r[fi_name] if len(r) > fi_name else "").strip() or "(no name)"
            status = (r[fi_status] if fi_status is not None and len(r) > fi_status else "").strip()
            flags.append(("serious", f"{esc(nm)} (created {dt.isoformat()}) — no phone number captured "
                                     f"anywhere{f', status {esc(status)}' if status else ''}; "
                                     f"currently un-callable by the sales team."))
    # A recent facebook_tab row WITH a real phone but no matching CRM (meta_leads_timed) record
    # is a different gap than the no-phone case above: the team can see and call this lead, but
    # it's absent from the dashboard's main leads table (which is sourced from the CRM sheet
    # only) and from every CRM-based stat on this page. Short 2-day window — this is meant to
    # catch a live sync gap, not relitigate old/non-Meta rows the reverse-check in the report
    # already handles with more care (name-typo matching, known-fake precedents, etc).
    if fi_name is not None:
        unsynced_cutoff = today - timedelta(days=2)
        for r in fb_tab[1:]:
            if len(r) <= fi_phone:
                continue
            ph = normphone(r[fi_phone] or "")
            if not ph or ph in crm_by_phone:
                continue
            dt = parse_dmy(r[fi_created], today)
            if not dt or dt < unsynced_cutoff:
                continue
            nm = (r[fi_name] if len(r) > fi_name else "").strip() or "(no name)"
            flags.append(("serious", f"{esc(nm)} ({ph}, created {dt.isoformat()}) — has a real phone number "
                                     f"in the team's sheet but no matching CRM record yet; not on this "
                                     f"dashboard's leads table or in any CRM-based stat until it syncs. "
                                     f"Verify it's a live sync lag and not a non-Meta entry."))
    flags_html = "".join(
        f'<li class="flag-{sev}"><span class="flag-ico">{"✗" if sev=="critical" else "⚠"}</span> {msg}</li>'
        for sev, msg in flags) or '<li class="muted">No open integrity flags. ✓</li>'

    # ---- reports archive ----
    report_files = sorted(glob.glob(os.path.join(HERE, "reports", "2*.md")), reverse=True)
    reports_html = []
    for i, path in enumerate(report_files):
        date_name = os.path.basename(path)[:-3]
        with open(path, encoding="utf-8") as f:
            body = f.read()
        reports_html.append(
            f'<details class="report"{" open" if i == 0 else ""}><summary>{date_name}</summary>'
            f'<div class="rbody">{md_lite(body)}</div></details>')
    reports_html = "".join(reports_html) or '<p class="muted">No reports committed yet.</p>'

    camp_legend = "".join(
        f'<span><i style="background:var(--s{i+1})"></i>{esc(c)}</span>' for i, c in enumerate(CAMPS))
    leads_sub = " · ".join(f"{esc(name)} {t.get(camp, {}).get('leads', 0)}" for camp, name in SHORT.items())

    vr_txt = f"{visit_rate:.1f}%" if visit_rate is not None else "—"
    vr_delta = ""
    if visit_rate is not None:
        good = visit_rate >= BASELINE_VISIT_RATE
        vr_delta = (f'<div class="delta {"up" if good else "down"}">'
                    f'{"▲" if good else "▼"} baseline {BASELINE_VISIT_RATE}%</div>')

    payload = json.dumps({
        "daily": daily, "dailyAds": daily_ads, "crm": crm_rows, "visits": visits,
        "today": today.isoformat(), "dailyMin": daily_min, "v3Start": V3_START,
        "camps": CAMPS,
    }, ensure_ascii=False)

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
  --s1: #2a78d6; --s2: #eb6834; --s3: #1f9e6b;
  --good: #0ca30c; --serious: #ec835a; --critical: #d03b3b; --good-text: #006300;
  --wash: rgba(11,11,11,.045);
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  color-scheme: dark;
  --surface: #1a1a19; --page: #0d0d0d; --ink: #ffffff; --ink2: #c3c2b7;
  --muted: #898781; --grid: #2c2c2a; --axis: #383835; --border: rgba(255,255,255,.10);
  --s1: #3987e5; --s2: #d95926; --s3: #2bbf85; --good-text: #0ca30c; --wash: rgba(255,255,255,.06);
}} }}
:root[data-theme="dark"] {{
  color-scheme: dark;
  --surface: #1a1a19; --page: #0d0d0d; --ink: #ffffff; --ink2: #c3c2b7;
  --muted: #898781; --grid: #2c2c2a; --axis: #383835; --border: rgba(255,255,255,.10);
  --s1: #3987e5; --s2: #d95926; --s3: #2bbf85; --good-text: #0ca30c; --wash: rgba(255,255,255,.06);
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
.filters {{ display: flex; flex-wrap: wrap; align-items: center; gap: 8px;
  background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
  padding: 10px 12px; margin: 14px 0; }}
.filters .lbl {{ font-size: 12px; color: var(--ink2); margin-right: 2px; }}
.preset {{ border: 1px solid var(--border); background: none; color: var(--ink);
  font: 600 12px system-ui, sans-serif; border-radius: 999px; padding: 4px 12px; cursor: pointer; }}
.preset:hover {{ background: var(--wash); }}
.preset.on {{ background: var(--ink); color: var(--page); border-color: var(--ink); }}
.filters input[type=date] {{ border: 1px solid var(--border); background: none; color: var(--ink);
  border-radius: 7px; padding: 3px 7px; font: 12px system-ui, sans-serif; }}
.rangenote {{ font-size: 12px; color: var(--muted); margin-left: auto; }}
.cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 12px; }}
.card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 14px; }}
.card h3 {{ font-size: 13px; font-weight: 600; margin-bottom: 8px; }}
.legend {{ display: flex; gap: 14px; font-size: 12px; color: var(--ink2); margin-bottom: 6px; }}
.legend i {{ display: inline-block; width: 10px; height: 10px; border-radius: 3px; margin-right: 5px; vertical-align: -1px; }}
svg {{ width: 100%; height: auto; display: block; }}
.grid {{ stroke: var(--grid); stroke-width: 1; }}
.axis {{ stroke: var(--axis); stroke-width: 1; }}
.tick {{ fill: var(--muted); font-size: 10px; font-variant-numeric: tabular-nums; }}
.s1 {{ fill: var(--s1); }} .s2 {{ fill: var(--s2); }} .s3 {{ fill: var(--s3); }}
rect.s1:hover, rect.s2:hover, rect.s3:hover {{ opacity: .8; }}
.tablewrap {{ overflow-x: auto; background: var(--surface); border: 1px solid var(--border); border-radius: 10px; }}
table {{ border-collapse: collapse; width: 100%; font-size: 13px; }}
th {{ text-align: left; color: var(--ink2); font-weight: 600; font-size: 12px; }}
th, td {{ padding: 8px 12px; border-bottom: 1px solid var(--grid); white-space: nowrap; }}
tr:last-child td {{ border-bottom: 0; }}
td.num, th.num {{ font-variant-numeric: tabular-nums; }}
.chip {{ display: inline-block; padding: 1px 8px; border-radius: 999px; font-size: 12px; font-weight: 600; color: #fff; }}
.chip.c1 {{ background: var(--s1); }} .chip.c2 {{ background: var(--s2); }} .chip.c3 {{ background: var(--s3); }}
.st-good {{ color: var(--good-text); }} .st-serious {{ color: var(--critical); }}
.st-critical {{ color: var(--critical); font-weight: 600; }} .st-muted {{ color: var(--muted); }}
.muted {{ color: var(--muted); }}
ul.flags {{ list-style: none; display: grid; gap: 8px; }}
ul.flags li {{ background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
  padding: 10px 12px; font-size: 13px; }}
li.flag-critical {{ border-left: 3px solid var(--critical); }}
li.flag-serious {{ border-left: 3px solid var(--serious); }}
.flag-ico {{ margin-right: 4px; }}
details.report {{ background: var(--surface); border: 1px solid var(--border); border-radius: 10px;
  margin-bottom: 8px; }}
details.report summary {{ cursor: pointer; padding: 10px 14px; font-weight: 600; font-size: 13px; }}
details.report .rbody {{ padding: 4px 16px 14px; font-size: 13px; border-top: 1px solid var(--grid); }}
.rbody h3 {{ font-size: 15px; margin: 12px 0 6px; }}
.rbody h4 {{ font-size: 13.5px; margin: 12px 0 4px; }}
.rbody h5 {{ font-size: 13px; margin: 10px 0 4px; color: var(--ink2); }}
.rbody .li {{ margin: 2px 0 2px 10px; }}
.rbody .gap {{ height: 8px; }}
.rbody hr {{ border: 0; border-top: 1px solid var(--grid); margin: 10px 0; }}
.rbody pre.mdtable {{ overflow-x: auto; background: var(--wash); border-radius: 8px;
  padding: 8px 10px; font-size: 12px; line-height: 1.5; margin: 6px 0; }}
footer {{ margin-top: 26px; color: var(--muted); font-size: 12px; }}
</style></head><body><div class="wrap">
<header>
  <h1>Divya Jyot LYF Rewa — Meta Ads</h1>
  <span class="updated">Updated {now.strftime("%a %d %b %Y, %H:%M IST")} · auto-rebuilds hourly 9AM–7PM IST · tab refreshes every 15m</span>
</header>

<div class="tiles">
  <div class="tile"><div class="k">Spend today (so far)</div><div class="v">{rupees(spend_today)}</div></div>
  <div class="tile"><div class="k">Leads today</div><div class="v">{leads_today}</div>
    <div class="sub">{leads_sub}</div></div>
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

<div class="filters">
  <span class="lbl">Range</span>
  <button class="preset" data-days="1">Today</button>
  <button class="preset" data-days="7">7D</button>
  <button class="preset on" data-days="14">14D</button>
  <button class="preset" data-days="30">30D</button>
  <button class="preset" data-days="all">All V3</button>
  <span class="lbl" style="margin-left:8px">From</span><input type="date" id="from">
  <span class="lbl">To</span><input type="date" id="to">
  <span class="rangenote" id="rangenote"></span>
</div>

<div class="cards">
  <div class="card"><h3>Leads per day</h3>
    <div class="legend">{camp_legend}</div>
    <div id="chart-leads"></div></div>
  <div class="card"><h3>Spend per day</h3>
    <div class="legend">{camp_legend}</div>
    <div id="chart-spend"></div></div>
</div>

<h2>Cost per lead</h2>
<div class="cards">
  <div class="card"><h3>CPL per day <span class="muted" style="font-weight:400">(days with 0 leads show no bar)</span></h3>
    <div class="legend">{camp_legend}</div>
    <div id="chart-cpl"></div></div>
  <div class="card"><h3>CPL over the selected range</h3>
    <div id="cpl-summary"></div></div>
</div>

<h2>Campaigns — selected range</h2>
<div class="tablewrap"><table>
<thead><tr><th>Campaign</th><th class="num">Spend</th><th class="num">Meta leads</th><th class="num">CPL</th>
<th class="num">CTR</th><th class="num">CPC</th><th class="num">CPM</th><th class="num">CRM leads</th></tr></thead>
<tbody id="camp-body"></tbody></table></div>

<h2>Ads — selected range</h2>
<div class="tablewrap"><table>
<thead><tr><th>Ad</th><th>Campaign</th><th class="num">Spend</th><th class="num">Leads</th><th class="num">CPL</th>
<th class="num">CTR</th><th class="num">CPC</th><th class="num">CPM</th><th class="num">Share of spend</th></tr></thead>
<tbody id="ads-body"></tbody></table></div>

<h2>Speed to lead — selected range</h2>
<div class="tablewrap"><table>
<thead><tr><th>Lead</th><th>Campaign</th><th class="num">Arrived (IST)</th><th>Intent</th><th>Budget</th>
<th>Logged in sheet</th><th>Lag</th></tr></thead>
<tbody id="speed-body"></tbody></table></div>

<h2>Site visits — selected range (SVD vs CRM)</h2>
<div class="tablewrap"><table>
<thead><tr><th class="num">Date</th><th>Name</th><th class="num">Phone</th><th>Verification</th></tr></thead>
<tbody id="visits-body"></tbody></table></div>

<h2>Open integrity flags</h2>
<ul class="flags">{flags_html}</ul>

<h2>Daily reports archive</h2>
{reports_html}

<footer>Verified visit = phone matches an OTP-verified CRM lead (either form tab). "Logged in sheet" comes from
the team sheet's Drive revision history (bracket upper bound) when available, else the sheet row's created date
(day-level). Meta spend/CTR data covers the trailing 30 days only; CRM leads go back to V3 start ({V3_START}).
Baseline visit rate {BASELINE_VISIT_RATE}%.</footer>
</div>

<script>
const DATA = {payload};
const $ = (s) => document.querySelector(s);
const fromEl = $("#from"), toEl = $("#to");
const fmtR = (v) => "₹" + Math.round(v).toLocaleString("en-IN");
// chip/series class per campaign, by its position in DATA.camps — so a new
// campaign just needs adding to CAMPS in build_dashboard.py and gets the next
// color/chip class automatically, no chart code changes.
const campClass = (c) => "c" + (Math.max(0, DATA.camps.indexOf(c)) + 1);

function isoAddDays(iso, n) {{
  // Parse and add in UTC: local-time parse + toISOString() made +1 day a no-op
  // for viewers ahead of UTC (IST), so the charts' day list never advanced.
  const d = new Date(iso + "T00:00:00Z");
  d.setUTCDate(d.getUTCDate() + n);
  return d.toISOString().slice(0, 10);
}}
function setRangeDays(days) {{
  toEl.value = DATA.today;
  fromEl.value = days === "all" ? DATA.v3Start : isoAddDays(DATA.today, -(days - 1));
  render();
}}
function listDays(from, to) {{
  const out = [];
  for (let d = from; d <= to && out.length < 400; d = isoAddDays(d, 1)) out.push(d);
  return out;
}}
function niceMax(v) {{
  if (v <= 0) return 1;
  for (const m of [1,2,2.5,5,10,20,25,50,100,200,250,500,1000,2000,2500,5000,10000]) if (m >= v) return m;
  return Math.ceil(v);
}}
function barChart(el, days, val, fmt) {{
  const W = 660, H = 200, PL = 46, PB = 26, PT = 12;
  const pw = W - PL - 12, ph = H - PB - PT;
  const camps = DATA.camps, N = camps.length;
  const mx = niceMax(Math.max(1, ...days.flatMap(dt => camps.map(c => val(c, dt)))));
  const n = days.length, gw = pw / Math.max(n, 1);
  const bw = Math.max(2, Math.min(22, (gw - (N - 1) * 2) / N));
  const groupW = N * bw + (N - 1) * 2;
  let s = "";
  [0, mx / 2, mx].forEach((yv, gi) => {{
    const yy = PT + ph - ph * yv / mx;
    if (gi) s += `<line x1="${{PL}}" y1="${{yy}}" x2="${{W - 12}}" y2="${{yy}}" class="grid"/>`;
    s += `<text x="${{PL - 6}}" y="${{yy + 4}}" class="tick" text-anchor="end">${{fmt(yv)}}</text>`;
  }});
  const step = Math.max(1, Math.ceil(n / 8));
  days.forEach((dt, i) => {{
    const x0 = PL + i * gw + (gw - groupW) / 2;
    camps.forEach((c, si) => {{
      const v = val(c, dt), bh = ph * v / mx;
      s += `<rect x="${{(x0 + si * (bw + 2)).toFixed(1)}}" y="${{(PT + ph - bh).toFixed(1)}}"` +
           ` width="${{bw.toFixed(1)}}" height="${{Math.max(bh, 0).toFixed(1)}}" rx="2" class="s${{si + 1}}">` +
           `<title>${{dt.slice(5)}} · ${{c}}: ${{fmt(v)}}</title></rect>`;
    }});
    if (i % step === (n - 1) % step)
      s += `<text x="${{x0 + bw}}" y="${{H - 8}}" class="tick" text-anchor="middle">${{+dt.slice(8)}}/${{+dt.slice(5, 7)}}</text>`;
  }});
  s += `<line x1="${{PL}}" y1="${{PT + ph}}" x2="${{W - 12}}" y2="${{PT + ph}}" class="axis"/>`;
  el.innerHTML = `<svg viewBox="0 0 ${{W}} ${{H}}" role="img">${{s}}</svg>`;
}}
function render() {{
  let from = fromEl.value || DATA.dailyMin, to = toEl.value || DATA.today;
  if (from > to) [from, to] = [to, from];
  const inR = (d) => d >= from && d <= to;
  const note = from < DATA.dailyMin ? `Meta spend/CTR data starts ${{DATA.dailyMin}}; CRM leads shown for the full range.` : "";
  $("#rangenote").textContent = note;

  const dayList = listDays(from < DATA.dailyMin ? DATA.dailyMin : from, to);
  const byKey = {{}};
  DATA.daily.forEach(r => {{ byKey[r.camp + "|" + r.date] = r; }});
  const get = (c, dt, f) => (byKey[c + "|" + dt] || {{}})[f] || 0;
  barChart($("#chart-leads"), dayList, (c, dt) => get(c, dt, "leads"), v => String(v));
  barChart($("#chart-spend"), dayList, (c, dt) => get(c, dt, "spend"),
           v => v >= 1000 ? "₹" + (v / 1000) + "k" : "₹" + Math.round(v));
  barChart($("#chart-cpl"), dayList,
           (c, dt) => get(c, dt, "leads") ? get(c, dt, "spend") / get(c, dt, "leads") : 0,
           v => v >= 1000 ? "₹" + (v / 1000) + "k" : "₹" + Math.round(v));

  // CPL summary tiles for the range
  let cplHtml = '<div class="tiles" style="grid-template-columns:repeat(auto-fit,minmax(120px,1fr))">';
  let tsp = 0, tld = 0;
  DATA.camps.forEach(c => {{
    const rs = DATA.daily.filter(r => r.camp === c && inR(r.date));
    const sp = rs.reduce((a, r) => a + r.spend, 0), ld = rs.reduce((a, r) => a + r.leads, 0);
    tsp += sp; tld += ld;
    cplHtml += `<div class="tile"><div class="k">${{c}} CPL</div>` +
      `<div class="v" style="font-size:20px">${{ld ? fmtR(sp / ld) : "—"}}</div>` +
      `<div class="sub">${{fmtR(sp)}} / ${{ld}} leads</div></div>`;
  }});
  cplHtml += `<div class="tile"><div class="k">Blended CPL</div>` +
    `<div class="v" style="font-size:20px">${{tld ? fmtR(tsp / tld) : "—"}}</div>` +
    `<div class="sub">${{fmtR(tsp)}} / ${{tld}} leads</div></div></div>`;
  $("#cpl-summary").innerHTML = cplHtml;

  // ad-level aggregates over range
  const adAgg = {{}};
  DATA.dailyAds.filter(r => inR(r.date)).forEach(r => {{
    const k = r.camp + "|" + r.ad;
    const a = adAgg[k] || (adAgg[k] = {{camp: r.camp, ad: r.ad, spend: 0, leads: 0, imp: 0, clicks: 0}});
    a.spend += r.spend; a.leads += r.leads; a.imp += r.imp; a.clicks += r.clicks;
  }});
  const adRows = Object.values(adAgg).sort((a, b) => b.spend - a.spend);
  const totalAdSpend = adRows.reduce((a, r) => a + r.spend, 0);
  $("#ads-body").innerHTML = adRows.map(r =>
    `<tr><td>${{r.ad}}</td><td><span class="chip ${{campClass(r.camp)}}">${{r.camp}}</span></td>` +
    `<td class="num">${{fmtR(r.spend)}}</td><td class="num">${{r.leads}}</td>` +
    `<td class="num">${{r.leads ? fmtR(r.spend / r.leads) : "—"}}</td>` +
    `<td class="num">${{r.imp ? (100 * r.clicks / r.imp).toFixed(2) + "%" : "—"}}</td>` +
    `<td class="num">${{r.clicks ? fmtR(r.spend / r.clicks) : "—"}}</td>` +
    `<td class="num">${{r.imp ? fmtR(1000 * r.spend / r.imp) : "—"}}</td>` +
    `<td class="num">${{totalAdSpend ? (100 * r.spend / totalAdSpend).toFixed(0) + "%" : "—"}}</td></tr>`
  ).join("") || `<tr><td colspan="9" class="muted">No ad-level data in this range (Meta daily data covers the trailing 30 days).</td></tr>`;

  // campaign aggregates over range
  let rows = "";
  DATA.camps.forEach((c, si) => {{
    const rs = DATA.daily.filter(r => r.camp === c && inR(r.date));
    const sp = rs.reduce((a, r) => a + r.spend, 0), ld = rs.reduce((a, r) => a + r.leads, 0);
    const im = rs.reduce((a, r) => a + r.imp, 0), ck = rs.reduce((a, r) => a + r.clicks, 0);
    const crmN = DATA.crm.filter(r => r.camp === c && inR(r.ts.slice(0, 10))).length;
    rows += `<tr><td><span class="chip c${{si + 1}}">${{c}}</span></td>` +
      `<td class="num">${{fmtR(sp)}}</td><td class="num">${{ld}}</td>` +
      `<td class="num">${{ld ? fmtR(sp / ld) : "—"}}</td>` +
      `<td class="num">${{im ? (100 * ck / im).toFixed(2) + "%" : "—"}}</td>` +
      `<td class="num">${{ck ? fmtR(sp / ck) : "—"}}</td>` +
      `<td class="num">${{im ? fmtR(1000 * sp / im) : "—"}}</td>` +
      `<td class="num">${{crmN}}</td></tr>`;
  }});
  $("#camp-body").innerHTML = rows;

  // speed to lead
  const sp = DATA.crm.filter(r => inR(r.ts.slice(0, 10)));
  $("#speed-body").innerHTML = sp.map(r => {{
    const cls = r.st === "warn" ? "st-serious" : "st-good";
    const ico = r.st === "warn" ? "⚠" : "✓";
    return `<tr><td>${{r.name}}</td><td><span class="chip ${{campClass(r.camp)}}">${{r.camp}}</span></td>` +
      `<td class="num">${{r.ts.slice(5, 16)}}</td><td>${{r.intent}}</td><td>${{r.budget || "—"}}</td>` +
      `<td>${{r.logged}}</td><td class="${{cls}}">${{ico}} ${{r.lag}}</td></tr>`;
  }}).join("") || `<tr><td colspan="7" class="muted">No CRM leads in this range.</td></tr>`;

  // visits
  const ic = {{verified: ["st-good", "✓"], annotated: ["st-good", "✓"], unverified: ["st-serious", "⚠"],
              bad: ["st-critical", "✗"], prev3: ["st-muted", "•"]}};
  const vs = DATA.visits.filter(v => inR(v.date));
  $("#visits-body").innerHTML = vs.map(v =>
    `<tr><td class="num">${{v.date}}</td><td>${{v.name}}</td><td class="num">${{v.phone}}</td>` +
    `<td class="${{ic[v.status][0]}}">${{ic[v.status][1]}} ${{v.status === "verified" ? "" : ""}}${{v.note}}</td></tr>`
  ).join("") || `<tr><td colspan="4" class="muted">No Facebook-sourced visits in this range.</td></tr>`;
}}
document.querySelectorAll(".preset").forEach(b => b.addEventListener("click", () => {{
  document.querySelectorAll(".preset").forEach(x => x.classList.remove("on"));
  b.classList.add("on");
  setRangeDays(b.dataset.days === "all" ? "all" : +b.dataset.days);
}}));
[fromEl, toEl].forEach(el => el.addEventListener("change", () => {{
  document.querySelectorAll(".preset").forEach(x => x.classList.remove("on"));
  render();
}}));
setRangeDays(14);
</script>
</body></html>"""

    out = os.path.join(HERE, "dashboard.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Wrote dashboard.html ({len(page):,} bytes, {len(crm_rows)} CRM leads, "
          f"{len(visits)} visits, {len(report_files)} reports, {len(flags)} flags)")

if __name__ == "__main__":
    build()
