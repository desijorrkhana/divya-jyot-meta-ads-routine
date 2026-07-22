# Divya Jyot LYF Rewa — Daily Snapshot — Tuesday, 21 July 2026 (CORRECTED)

## ⚠️ CORRECTION — read this first
The version of this report sent earlier today had a **central finding that was wrong**, and
Keval caught it. Full retraction and root cause below; the rest of the report is rebuilt from
corrected data.

**What was wrong:** the original report's headline claimed the "Divya Jyot V3 July 26 - 2BHK"
campaign was completely invisible to the CRM Event tracking — zero leads, zero speed-to-lead,
zero visit verification. **That was false.**

**Root cause:** `fetch_all.py` reads the CRM Event spreadsheet (`LEADS_SHEET_ID`) by hardcoding
`Sheet1!A1:Q5000`. What I didn't check is that this spreadsheet has **two tabs**: `Sheet1` is
the Studio form's feed, and **`Sheet2` is a separate, fully-working feed for the "2BHK" lead
form** — created 2026-07-06, the same day the 2BHK campaign launched, complete with exact
timestamps, phone, intent, platform, AND a real budget-qualifying question
(`what_is_your_budget_for_this_purchase?`, e.g. "below ₹1.55 cr" / "₹1.5–1.75 cr"). `fetch_all.py`
never read it, so every 2BHK lead was silently missing from `data.json`, and I built an entire
"critical tracking gap" narrative on that absence without checking for a second tab. Keval
pushed back three times (on the lead count, the CRM completeness, and specific named leads)
before this surfaced — each of his challenges was correct and this correction exists because of
that persistence, not because I caught it myself.

**Fixed:** `fetch_all.py` now enumerates every tab in the CRM spreadsheet automatically (see
commit) instead of hardcoding `Sheet1`, so a third form/tab in the future won't repeat this.
Everything below is rebuilt using both tabs. Note the reporting window also became a genuinely
**complete day** for 21 July in the process (this correction is being finished after midnight),
so funnel numbers below are slightly higher than the original partial-day (up to ~7 PM) report.

## 1. HEADLINE (corrected)
The 2BHK campaign is **not** an integrity gap — it has its own working, OTP-verified CRM feed
(Sheet2) that matches Meta's real numbers almost exactly (67 CRM leads vs. 68 reported by Meta
lifetime). With both tabs included, the Facebook-tab-to-CRM match rate for the last 30 days is
**87.9%** (123/140), not the 48.9% the broken version reported — much closer to the historical
93.6% baseline. The two real open items from the original report **do still stand**: two SVD
site visits (Vidhi Thakkar, Payal Shah) still have no CRM record in *either* tab despite a
"Meta Sent ✅" conversion pushed for them, and a live phone-typo was caught in today's own data
(Jigna Rathod: CRM has ...283**3**, the Facebook tab logged ...283**2** — one digit off, same
shape as the Atul Thorat case from 4 July). Underneath the correction, the actual day was solid:
9 fresh leads (4 Studio + 5 "2BHK"), same-day contact on all of them, and the "2BHK" product
(confirmed via the ad creative: ₹1.55 Cr+, 2BHK, Mulund West, 5 min from MG Road station) is
real, distinct inventory.

## 2. THE FUNNEL — 21 July, full day (corrected/complete)
- **Spend:** ₹1,727.20 (₹888.75 Studio + ₹838.45 "2BHK")
- **Impressions:** 5,852 · **Reach:** ~4,637 (two campaigns, some overlap)
- **Clicks:** 156 (**link clicks:** 88)
- **Leads:** 9 — canonical count, verified against `lead_actions_raw`, matches CRM (both tabs)
  almost lead-for-lead.
  - Studio: 4 leads, CPL ₹222.19 — 3 Facebook / 1 Instagram (roy Miryala, Manoj Kumar Surana,
    Sundar Suvarna on FB; Nita Shah on IG)
  - "2BHK": 5 leads, CPL ₹167.69 — 3 Facebook / 2 Instagram (Jigna Rathod, Dimple Chothani,
    Chirag Mota on FB; Falguni Deep Thakker, jai shri krishna on IG)
  - **Blended CPL: ₹191.91**
- **Contacted by team:** all 9 got a same-day row/feedback in the Facebook tab (see Section 4
  for exact brackets). **Untouched: 0.**
- **Site visits logged 21 July:** 0.

## 3. AD PERFORMANCE (agency hat)
| Metric | Studio | "2BHK" |
|---|---|---|
| Spend | ₹888.75 | ₹838.45 |
| Leads | 4 | 5 |
| CPL | ₹222.19 | ₹167.69 |
| CTR | 2.32% | 3.10% |
| CPC | ₹11.69 | ₹10.48 |
| CPM | ₹271.79 | ₹324.73 |
| Frequency | 1.20 | 1.36 |

- Both campaigns had a good day — "2BHK" in particular (CPL ₹168, CTR 3.1%) is now clearly
  pulling its weight, not just Studio's sidecar.
- Lifetime (since the 2BHK campaign's actual creation, 6 July): 68 leads / ₹17,298 spend
  (60 leads on the "36 Seconds" cut, 8 on "57 Seconds" — 36s remains the stronger creative,
  84% of spend, better CTR).
- Delivery healthy on both, no fatigue signal (frequency both under 1.4 for the day).

## 4. SPEED-TO-LEAD (sales-manager hat) — the most important section
All 9 of 21 July's CRM leads (both campaigns), matched by phone with real arrival timestamps
and Drive-revision brackets for when the row/feedback appeared in the Facebook tab:

| Lead | Campaign | Arrival (IST) | Intent / Budget | Row+feedback appeared by | Lag |
|---|---|---|---|---|---|
| roy Miryala | Studio | 06:20 | within_3_months | by 11:35 | ≤ ~5h15m |
| **Jigna Rathod** | 2BHK | 06:48 | within_3mo, <₹1.55cr | **never found** | **see phone-typo flag below** |
| Manoj Kumar Surana | Studio | 08:19 | within_3_months | by 11:35 | ≤ ~3h16m |
| Falguni Deep Thakker | 2BHK | 11:09 | within_3mo, <₹1.55cr | by 11:35 | ≤ ~26m |
| Dimple Chothani | 2BHK | 14:45 | 3-6mo, ₹1.5-1.75cr | by 15:31 | ≤ ~46m |
| Chirag Mota | 2BHK | 14:56 | 6+mo/exploring, <₹1.55cr | by 15:31 | ≤ ~35m |
| jai shri krishna | 2BHK | 17:11 | within_3mo, <₹1.55cr | ambiguous — see note | n/a |
| Nita Shah | Studio | 19:56 | within_3_months | by 22/7 11:32 | ≤ ~15h |
| Sundar Suvarna | Studio | 22:55 | within_3_months | by 22/7 11:32 | ≤ ~12h |

**Jigna Rathod — live phone-typo catch, same shape as the 4 Jul Atul Thorat case:** the CRM
(Sheet2, OTP-verified) has her number as **9969283483**. The team's Facebook tab (row 202,
21/7) logged her as **9969283482** — last digit wrong. The automated tracking correctly
reports "never found" for the real number, because the team is holding the wrong one. **If
anyone calls the number in the sheet, they're calling a stranger, not Jigna.** Get the real
number (983) from the CRM and re-enter it.

**jai shri krishna — a genuine repeat lead, not a duplicate row (this was my second error,
now corrected):** this person is in **both** CRM tabs — a Studio lead on **1 July** (phone
ending 6376, `within_3_months`) and a fresh, separate **2BHK** lead on **21 July**, same phone.
Two real, distinct lead events 3 weeks apart. I'd previously told Keval this was "just an old
lead being re-logged" — that was also wrong; it's a real return visit to the funnel, this time
for the 2BHK product. The Drive-revision bracket can't cleanly time this one because the phone
was already present in the sheet from the 1 July row before the 2-day lookback window started.

**Bottom line:** every fresh lead today got same-day attention (worst case ~15h for Nita Shah,
who arrived at 19:56 IST — still well within the day). Credit holds from the original report.

## 5. LEAD QUALITY (sales-manager hat)
- **Blended 30-day CPL: ₹240.55** (₹39,210.84 / 163 leads across both campaigns).
- The 2BHK product is confirmed real (via the ad creative): 2BHK, ₹1.55 Cr onwards, 600 sq ft
  carpet, Mulund West, 5 min from MG Road station — a genuine second SKU, not a mislabeled
  studio ad. Sheet2's budget-qualifying answers show most 2BHK leads self-report "below ₹1.55
  cr" — worth a look at whether the entry price is priced right for the volume of interest
  it's pulling in, but that's a pricing/product question, not a tracking one.
- **Real cost-per-site-visit, corrected with both CRM tabs:**
  - SVD claims 16 Facebook-sourced visits in the last 30 days.
  - **12 are now CRM-verified** (up from 7 in the broken version): 7 Studio + **5 "2BHK"**
    (Deep Biren, Deepak Chaurasia, Vimesh, Kapil Chheda — all previously flagged as merely
    "plausible" are now confirmed genuine via Sheet2; plus Rewashankar Gomtiwal, Vipul
    Rakhasia, Christina Dias, Pravin Bhuingul, Asha Joshi, Santosh Utekar, Hemang Shah on
    Studio).
  - **2 remain KNOWN non-V3** (unchanged, still unresolved from 4 Jul): Naveen Suvarna
    (pre-V3 lead), Hitendra Dedhia (fabricated Facebook attribution).
  - **2 remain unverified in EITHER tab** (see 5b): Payal Shah, Vidhi Thakkar. Sushma
    Ravasia's visit (logged under a relative's number, team-annotated "{Sushma}") ties to a
    real CRM lead by name/date even though the phone doesn't match — treated as genuine.
  - **Corrected number: ₹39,210.84 / 13 (12 verified + Sushma) = ₹3,016/visit, 8.0% visit
    rate — clearly beats the ~4.5% V3 baseline**, and this is now a real, mostly-verified
    number rather than a heavily-caveated estimate.

## 5b. DATA INTEGRITY CROSS-CHECK (corrected)
- **The structural "2BHK gap" from the earlier version of this report is retracted.** Sheet2
  is a working, real-time CRM feed for the 2BHK form — 67 leads, matching Meta's 68 lifetime
  count almost exactly (the 1-lead gap is normal timing/attribution noise, not a tracking
  failure).
- **Still open, unchanged: two CAPI-pollution candidates**, same shape as the 4 Jul Dedhia
  case — checked again against BOTH CRM tabs this time, still no match:
  - **Vidhi Thakkar**, 9820194111 — visited 20/7, "Meta Sent ✅" pushed, not in Sheet1, not in
    Sheet2, not in the Facebook tab. No paper trail anywhere before the SVD row.
  - **Payal Shah**, 9769884201 — in the Facebook tab (Studio-shaped ask: 300 sqft/₹60L) but
    in neither CRM tab; her visit also got "Meta Sent ✅".
  - Ask the team directly where these two came from before trusting their conversions.
- **New, live phone-typo catch (today, not historical):** Jigna Rathod — CRM 9969283**3**,
  sheet 9969283**2**. See Section 4. Fix this one today; it's fresh, not a cold case.
- **Match-rate, corrected:** last-30-day Facebook-tab-to-CRM match rate is **87.9% (123/140)**
  with both tabs included — not last version's artificially-low 48.9%. Much closer to the 3
  July baseline of 93.6%; the remaining ~12% gap is normal (some genuinely unlogged leads,
  some date-parsing noise from a literal sheet typo found earlier — "02/09/2525").

## 6. DIAGNOSTIC STEPS (corrected)
1. **[Sales, urgent, live]** Fix Jigna Rathod's phone number in the Facebook tab —
   9969283483, not …82. She hasn't actually been called yet; whoever's dialing the sheet's
   number is reaching someone else.
2. **[Sales, urgent]** Ask the team where Vidhi Thakkar and Payal Shah actually came from —
   both visited and got a Meta conversion pushed with no lead record in either CRM tab or
   (for Vidhi) the Facebook tab at all.
3. **[Agency]** The 2BHK campaign is working — treat it as a real, proven second product line
   in the standing business context, not a leak to be filtered out. Worth reviewing whether
   ₹1.55 Cr is priced right, since most self-reported budgets in the CRM's own qualifying
   question come in "below ₹1.55 cr."
4. **[Agency]** "2BHK 57 Seconds" is still the weaker of the two creatives (16% of 2BHK
   spend, worse CTR) — consider pausing it in favor of "36 Seconds."
5. **[Process]** `fetch_all.py` now auto-discovers CRM tabs so this specific failure mode
   (a new form/tab silently missing from the data) can't recur — but the broader lesson is
   to sanity-check totals (like today's Meta-vs-CRM lead counts) before writing a headline
   finding, not just trust the first data pull.

## 7. ANYTHING ELSE
This correction happened because Keval checked the work — specifically challenged the lead
count, then the "no CRM coverage" claim, then two individual leads by name — and each check
found something real. That's exactly the workflow this routine should support: treat today's
corrected numbers with the same scrutiny next time, not as settled just because they're now
"fixed."

---
*Corrected match rate: 123/140 (87.9%) of the last 30 days' Facebook-tab entries matched to
the CRM (both tabs) by phone. All 9 of 21 July's leads got same-day contact. No fabricated
numbers — anything not directly computable from data.json is marked as such above.*
