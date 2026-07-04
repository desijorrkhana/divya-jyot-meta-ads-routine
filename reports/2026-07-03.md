# Divya Jyot LYF Rewa — Daily Snapshot — Thursday, 3 July 2026

**Window: yesterday, full day (midnight–midnight IST).** This is the first automated run of
this routine — no prior report to follow up on, and no `reports/_memory.md` yet.

⚠️ **Data pipeline note:** before this report could be generated, `fetch_all.py` was pulling
**zero** Meta Ads data — every single Meta API call was failing with HTTP 400
(`action_attribution_windows[0] must be one of...`). Meta's v25.0 API changed the attribution
format the script used; it's fixed now (verified against the live API) and this report runs on
real numbers. Separately, the Facebook/SVD Google Sheet reads were intermittently corrupting
mid-fetch ("decryption failed or bad record mac") because three concurrent reads shared one
un-thread-safe HTTP connection — also fixed. Flagging both so you know the last several days of
"no data" or partial reports (if any) were an infra problem, not an ad or team problem.

## 1. HEADLINE
CPL looks mediocre (₹180) but the **real number is good**: ~₹2,200–2,550 per confirmed site
visit and a **6.7% visit rate — beating the ~4.5% V3 baseline**. The problem yesterday wasn't
the ad, it was the sales side: a 3–6-month-intent lead (**Sunil Bagul**) sat completely
**unlogged and uncalled for 20+ hours**, and 3 older leads from weeks ago were never entered
in the sheet at all.

## 2. THE FUNNEL — yesterday, 3 July, full day IST
- **Spend:** ₹721.26
- **Impressions:** 3,583 · **Reach:** 2,838
- **Clicks:** 78 (**link clicks:** 50)
- **Leads:** 4 — canonical count (`onsite_conversion.lead_grouped` = 4), matches `lead` = 4 and
  every other lead-ish action type exactly. No double-count anomaly — this is what you'll see
  in Ads Manager. **CPL: ₹180.31.**
- **Platform split:** 2 Facebook / 2 Instagram
- **Contacted by team:** 3 of 4 same-day · **Untouched:** 1 of 4 (still zero contact as of
  this report)
- **Site visits logged yesterday:** 1 (see note below — a returning Facebook lead, not one of
  yesterday's 4 fresh Meta leads)

## 3. AD PERFORMANCE (agency hat)
| Window | CTR | CPC | CPM | Frequency | Reach |
|---|---|---|---|---|---|
| Yesterday | 2.18% | ₹9.25 | ₹201.30 | 1.26 | 2,838 |
| Last 7 days | 2.48% | ₹8.32 | ₹205.95 | 1.80 | 11,828 |
| Last 30 days | 2.78% | ₹8.48 | ₹235.52 | 2.73 | 23,717 |

- **Not fatigue.** Frequency yesterday (1.26) is *lower* than the 7-day (1.80) and 30-day
  (2.73) figures — the audience is turning over, not getting hammered repeatedly. CTR softening
  slightly (2.78% → 2.48% → 2.18%) alongside falling frequency is a mild, inconclusive trend,
  not a fatigue alarm. Don't touch the creative on this signal alone.
- **Single creative, single real adset.** Every rupee of real spend and every lead is one ad
  ("Studio") in one adset ("Open - DJR"). The other adset, "Luxury - DJ", spent ₹7.76 over 30
  days for 0 leads and 0 clicks — immaterial in size but dead weight; fold its tiny budget into
  the working adset.
- Delivery is healthy post-pause (per the June 22 account-security pause / resume) — spend and
  leads are flowing normally both yesterday and over the trailing week.
- **Today so far (partial, forward glance):** ₹570.10 spent, 4 leads already, CPL ₹142.53, CTR
  2.55% — tracking fine, nothing actionable yet since the day isn't over.

## 4. SPEED-TO-LEAD (sales-manager hat) — the most important section
All 4 of yesterday's Meta leads, matched by phone to the Facebook tab:

| Lead | Meta arrival (IST) | Intent | Sheet status / first contact | Lag |
|---|---|---|---|---|
| Doshi Jaswant | 15:20 | just_exploring | Cold — "Ringing" (attempted, no connect) | 0 days (attempted same day) |
| Dhanraj | 15:21 | within_3_months | Cold — "Details shared, coming Sunday" | 0 days — **connected** |
| **Sunil Bagul** | **19:41** | **3–6_months** | **Not in the sheet at all** | **⚠️ untouched, 20+ hrs and counting** |
| Amey Angane | 22:09 | within_3_months | Cold — "1RK, ₹70L budget, coming tomorrow" | 0 days — **connected** (see budget flag below) |

**Precision note:** the sheet has no per-call timestamps for these entries, only the row's
"Created" date and free-text feedback — so lag is day-level, not hour-level, for anyone who
*was* contacted. Exact hour-level lag isn't available in the data as logged.

**Credit where due:** 3 of 4 leads got a real same-day attempt, and 2 of those turned into an
actual conversation with real intel captured (budget, timeline). That's solid work.

**The miss:** Sunil Bagul is exactly the case this section exists to catch — OTP-verified,
phone in hand, 3–6-month intent (better odds than "just exploring"), and as of this report he
has never been called or logged. Call him first thing.

**Bigger pattern — leads going missing, not just slow:** widening to the trailing 30 days (94
Meta leads, 88 matched to the sheet = **93.6% match rate**, 6 leads never entered at all), 3 of
those 6 aren't recent — they're **weeks old** and simply never made it into the sheet:
Ravi DU (arrived 10 Jun), Andre Brian Edward Rozario (14 Jun), Atul Thorat (24 Jun). These
aren't a speed problem, they're a logging/process leak — leads falling out of the pipeline
before anyone gets a chance to call them. Worth checking why (form → sheet handoff gap?
name/number parsing issue?) since it's now happened 6 times in a month.

## 5. LEAD QUALITY (sales-manager hat)
- **Status breakdown, last 30 days (94 leads):** 76 Cold, 11 Dead, 6 never logged, 1 Warm.
  Most "Cold" leads are early-stage (rung once, no connect yet) rather than confirmed
  low-quality — too soon to call them dead weight.
- **Dominant quality leak, confirmed in the data:** of 88 leads matched to real feedback text,
  **36 (41%) explicitly asked for a 1BHK / 2BHK / 1RK** — a flat product mismatch, since this
  project is a bare-shell **studio only**. Zero matched leads' feedback mentions "studio"
  specifically. That's a strong signal the ad/instant-form isn't making the product clear
  before people submit their number — the team is spending call time discovering a mismatch
  the ad copy could screen out up front.
- **Budget mismatches spotted directly in yesterday's/recent feedback:** Amey Angane offered
  ₹70L against the ₹87L ask (1RK); several recent leads in the last 7 days cited ₹75–90L for
  1BHK requests — under or borderline vs. what this project can serve.
- **Real cost-per-site-visit vs. vanity CPL** (the metric that actually matters):
  - **Last 30 days:** 6 confirmed visits (SVD tab) / ₹15,259.80 spent / 90 leads →
    **₹2,543 per visit, 6.7% visit rate.** Beats the ~4.5% V3 baseline.
  - **Last 7 days:** 2 visits / ₹4,384.74 / 27 leads → **₹2,192 per visit, 7.4% visit rate.**
    Trending better than the 30-day average.
  - **Yesterday alone:** 1 visit / ₹721.26 — too small a single day to trend, but noted.
  - **Bottom line: don't touch this ad on CPL.** The number that matters is beating baseline.

## 6. DIAGNOSTIC STEPS
1. **[Sales, urgent]** Call Sunil Bagul (8108715063) today — untouched 3–6-month lead, already
   20+ hours cold.
2. **[Sales]** Investigate the 3 fully-orphaned leads from weeks ago (Ravi DU, Andre Rozario,
   Atul Thorat) — find where they fell out between the form and the sheet, and check today
   forward that new leads aren't silently dropping the same way (today's 2 newest leads,
   Manoj Agrawal and Subhash Soni, aren't logged yet either — likely just too fresh, but worth
   a same-day check given the pattern).
3. **[Agency]** Tighten ad copy/creative to make "bare-shell STUDIO" explicit before the click —
   41% of engaged leads are asking for a BHK layout this project doesn't have. This is a
   messaging fix, not a budget or pause decision.
4. **[Agency]** Fold the "Luxury - DJ" adset's token spend into "Open - DJR" — it's produced 0
   leads for ₹7.76 over 30 days. Immaterial money, but no reason to leave it split.
5. **[Sales]** When a call connects, screen budget in the first minute (per the Amey Angane
   example, ₹70L vs. the ₹87L ask) — saves follow-up cycles on leads that can't close here
   regardless of how warm they get.

## 7. ANYTHING ELSE
The SVD tab's "Meta Sent" column (confirms whether a site-visit conversion event was pushed
back to Meta via CAPI) shows **❌ Invalid parameter for essentially every visit logged from
August 2025 through mid-June 2026**, and only starts showing **✅ success from ~19 June 2026
onward** (6 straight successes through yesterday's visit). If that sync was broken for ~10
months, Meta's algorithm had zero real-world signal on which leads actually converted to
visits for most of this campaign's life — it's only had usable optimization data for about two
weeks. Worth keeping an eye on: if it silently breaks again, you'll lose the one signal that
actually correlates with revenue, not just clicks.

---
*Match rate: 88/94 (93.6%) of the last 30 days' Meta leads found in the Facebook tab; 3/4
(75%) of yesterday's. No fabricated numbers — anything not directly computable from data.json
is marked as such above.*
