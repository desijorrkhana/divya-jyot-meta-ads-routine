# Divya Jyot LYF Rewa — Daily Snapshot — 2026-07-03

**First report ever produced by this routine — no prior reports to follow up on.** (See "Anything Else" for a data-pipeline issue found and fixed today.)

## 1. HEADLINE
Today is a quiet lead day (2 leads by ~7PM on ₹462 spend) but that's noise, not signal — the real story is the team: 57% of this week's leads are stuck in a "Ringing, no pickup" loop despite repeated attempts, and the real cost per site visit (~₹4,843) is **~29x** the vanity CPL (₹169) you'd see in Ads Manager.

## 2. THE FUNNEL — today so far (midnight–7PM IST, 2026-07-03; numbers will keep moving)
- **Spend:** ₹462.46
- **Impressions / Reach:** 2,314 / 1,876
- **Clicks (link clicks):** 50 (33)
- **Leads:** 2 — CPL ₹231.23. Platform split: 1 FB, 1 IG. Intent: 1 within_3_months, 1 just_exploring.
  - Sanity-checked against `lead_actions_raw`: canonical `onsite_conversion.lead_grouped` = 2, matches `leads` = 2. No double-count bug today.
- **Contacted vs untouched (of today's 2):** both reached same day (day-level precision — see Speed-to-Lead). Doshi Jaswant is still "Ringing"; Dhanraj got details shared and said he's **coming Sunday** — that's a live warm lead, chase it.
- **Site visits logged today:** **1 confirmed** — Hitendra/Heena Dedhia (see section 5). First real site-visit win we can point to this week.

## 3. AD PERFORMANCE (agency hat)
Single ad running: campaign "Divya Jyot V3 June26" → adset "Open - DJR" → ad "Studio". (A second adset, "Luxury - DJ", is essentially dormant: ₹7.76 spend, 0 leads over 30 days — not worth discussing further.)

| Window | Spend | Leads | CPL | CTR | CPC | CPM | Frequency |
|---|---|---|---|---|---|---|---|
| Today so far | ₹462 | 2 | ₹231 | 2.16% | ₹9.25 | ₹200 | 1.23 |
| Yesterday | ₹596 | 7 | ₹85 | 2.21% | ₹9.03 | ₹200 | 1.22 |
| Last 7 days | ₹4,243 | 26 | ₹163 | 2.49% | ₹8.32 | ₹208 | 1.78 |
| Last 30 days | ₹14,528 | 86 | ₹169 | 2.81% | ₹8.45 | ₹237 | 2.72 |

- **Delivery is healthy post-pause.** The June 22 account-security pause is well behind us — the last-7-day window (6/26–7/2) shows 26 leads flowing normally, so the resumed budget-threshold setup is working.
- **No fatigue signal.** Frequency is low (1.22–1.23 daily) and CTR is only mildly softer than the 7-day trend (2.16–2.21% vs 2.49%) — not the kind of drop that says "refresh the creative." CPC has drifted up slightly (₹9.25 today vs ₹8.32 over 7 days) but within normal noise.
- **Don't read into today's CPL spike (₹231 vs ₹85 yesterday).** That's 2 leads vs 7 — sample too small to mean anything. Per standing instruction: never pause on CPL alone, and this is exactly the kind of day that would tempt someone to.

## 4. SPEED-TO-LEAD (sales-manager hat) — the most important section

**Today + yesterday, every lead, matched by phone (day-level precision — the sheet has no call timestamps, only dates):**

| Lead | Arrived (Meta, IST) | First logged contact | Lag | Intent |
|---|---|---|---|---|
| Shanker Tekwani | 07-02 09:46 | 07-03 | 1 day | within_3_months |
| Dilip Gawai | 07-02 16:16 | 07-03 | 1 day | just_exploring |
| Anjali Warang | 07-02 18:47 | 07-03 | 1 day | 3–6_months |
| Navin Maru | 07-02 20:05 | 07-02* | same day | 3–6_months |
| Manisha Shah | 07-02 21:41 | 07-02* | same day | 3–6_months |
| Mital Joshi | 07-02 23:22 | 07-02* | same day | within_3_months |
| Chavan | 07-02 23:35 | 07-02* | same day | just_exploring |
| Doshi Jaswant | 07-03 15:20 | 07-03* | same day | just_exploring |
| Dhanraj | 07-03 15:21 | 07-03* | same day | within_3_months |

\* No dated follow-up recorded — feedback was logged without its own date stamp, so "same day" is inferred from the sheet row's creation date, not a confirmed call time.

Average lag today+yesterday: ~0.3 days. But the one that matters: **Shanker Tekwani, a within_3_months (highest-urgency) lead, sat a full day before first contact.** He was reached today and it's now looking budget-marginal (see section 5) — the day's delay didn't help.

**Historical pattern (all 88 Meta-timed leads to date, 84 with a determinable contact date):**
- Same-day: 29 (34.5%) | 1–3 days: 42 (50%) | >3 days: 13 (15.5%) | average lag: 1.68 days
- **Biggest finding: 17 of 88 leads (19%) — including several within_3_months — were ALL first-contacted on the exact same day, 2026-06-18,** after sitting 4 to 9 days. This isn't a one-off slow lead, it's a batch backlog-clearing event: leads arriving June 10–14 got worked in one sweep on June 18, not as they came in. That's the single biggest speed-to-lead failure in this campaign's history — a batch process, not a real-time one.
- Slowest named: **anant** (9 days), **Madhukar Bhavsar S., theDaniel, Vipul Rakhasia** (8 days each, all within_3_months) — all part of the June 18 catch-up.
- Fastest: several June 10 leads contacted same day (Sailee Joag, Adarsh Thakur, Shweta Mahendra Singh, Sudarshan Gaikwad) — **credit due here**, this is what good response looks like.
- 3 leads across the full history **never appear in the Facebook tab at all**: Ravi DU, Andre Brian Edward Rozario, Atul Thorat. Worth confirming these weren't silently dropped.

## 5. LEAD QUALITY (sales-manager hat)
Assessed the last 7 days + today (28 leads) by reading the feedback/follow-up text against each lead's Meta intent:

- **Warm / worth prioritizing (4):** Priya (2BHK, said coming Saturday), Naresh Khatri (budget ₹90L — fits, said he's coming), Dhanraj (budget shared, coming Sunday), Surendra Prajapati (budget ₹90L, good fit, but 7 days of unanswered ringing — reach him a different way, he's within_3_months and still open).
- **Budget mismatch (3, ~11%):** Nishant Kamdar (₹75L for a 1RK), Sachi Iyer (₹75L), Shanker Tekwani (₹80L — closer, might be salvageable). All well under or near the ₹87L ask.
- **Dead / unreachable (5, ~18%):** Parag Chavan (out of service), Kumar C Kummi (out of service), Vikas Bodwade (not interested), Rahul Padaya (invalid number), Navin Maru (not interested).
- **Stuck in limbo (16, ~57%):** Repeated "Ringing" with no pickup across 3–7 attempts (e.g. Jyothi Gowda: 7 straight days of ringing, unanswered). This is the dominant pattern this week — more of a reachability problem than a quality problem, and it's swallowing more leads than dead/budget-mismatch combined.
- Notably, **no clear location-mismatch leads** (Ghatkopar/Navi Mumbai/rentals) this week — a change from the documented historical leak, though several leads have terse "budget not disclose" notes that may be hiding the real objection.

**Real cost per site visit vs. vanity CPL:**
- Confirmed "visit done" mentions (cross-checked against both the Facebook tab and the SVD tracker — see caveat below) in the last 30 days: **3** — Swati Wankhede (6/19), Manjulamahida (6/19), Sandeep Shah (6/20) — against ₹14,528 in 30-day ad spend.
- **Real cost per site visit ≈ ₹4,843 — about 29x the ₹169 CPL Ads Manager shows.** Visit rate: 3/86 = 3.5%, below the ~4.5% historical baseline.
- **Zero confirmed visits in the last 7 days** (6/26–7/2) from 26 leads — until **today**, when Hitendra/Heena Dedhia (arrived FB tab 7/1, contacted 7/3, visited today, confirmed by both the FB log's "VISIT DONE" note and the SVD tracker's Meta-CAPI-sent timestamp of 3:47pm) broke the streak. That's the one concrete proof point this week that reasonably fast follow-through converts.
- **Caveat:** this count relies on the team's own free-text notes (e.g. "visit done"), and the SVD tracker tab is internally inconsistent — for Swati Wankhede it shows "Not interested" after the visit date, while the primary Facebook log confirms the visit happened. Treat 3/86 as a floor, not a precise count.

## 6. DIAGNOSTIC STEPS
1. **Sales — fix the reachability wall first.** 57% of this week's leads are stuck on unanswered "Ringing," more than dead + budget-mismatch combined. Try different call windows (evening/weekend) or add a WhatsApp/SMS nudge after the 3rd unanswered attempt — this is the single highest-leverage fix available right now.
2. **Sales — chase today, named:** Priya, Naresh Khatri, Dhanraj (all said "coming" — lock the actual date), and Surendra Prajapati (good ₹90L budget fit, within_3_months, but unreachable for 7 days — try a different channel/time before he goes cold).
3. **Sales — screen budget on the first call.** Nishant Kamdar and Sachi Iyer are both ~₹75L against an ₹87L product — tell them the price up front rather than spending 2-3 ringing cycles on a lead that structurally can't close.
4. **Agency — no action needed on the ad itself.** CTR/frequency show no fatigue; today's CPL spike is a 2-lead sample, not a trend. Keep the current creative running.
5. **Both — audit the SVD tracker.** It contradicts the primary sales log on at least one confirmed visit. If Keval is using that tab for visit counts, it's likely undercounting real visits.

## 7. ANYTHING ELSE
**Data pipeline was broken before this report could be produced, and is now fixed.** `fetch_all.py` was failing every single Meta Ads API call with an HTTP 400 — Meta's Graph API v25.0 changed the `action_attribution_windows` parameter format (from `{event_type, window_days}` objects to plain strings like `"7d_click"`), and the old format now hard-errors instead of degrading gracefully. Fixed in `fetch_all.py`. Separately, the Google Sheets client had no request timeout, which caused the whole fetch to hang indefinitely on an intermittent proxy stall (reproduced twice); added a 25s timeout plus a retry-with-backoff on the sheet reads. Verified with three consecutive clean runs before writing this report. Without this fix, today's report would have had zero ad performance data.

---
*Data window: today = 2026-07-03 (midnight–7PM IST, partial day), yesterday = 2026-07-02. Meta-lead-to-sheet match rate: 85/88 (96.6%). Speed-to-lead precision is day-level only — the sheet does not record call timestamps.*
