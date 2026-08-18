# Divya Jyot LYF Rewa — Daily Snapshot — Tuesday, 18 August 2026
*(End-of-window update — this run refreshes today's own earlier ~5PM snapshot with the full midnight–~7PM IST window; nothing after ~19:10 IST is captured.)*

## FOLLOW-UP FROM TODAY'S EARLIER REPORT (~5PM run)
- **1BHK phone-number gap: STILL UNRESOLVED, ~2 hours later.** No new 1BHK submission has landed
  anywhere in the system since the last check. `meta_leads_timed` still shows only the same 2
  blank-name/blank-phone 1BHK rows (13:20 test lead, 13:36 Madhu Tiwari). `facebook_tab` still
  shows exactly the same 6 dashed-phone rows (Urmi Gala, Vilas Shah, Lalji, Priyanka Rane,
  Shailesh, Madhu Tiwari) — no 7th, no post-fix row with a real number. The open question from
  the last report ("has anyone submitted since the phone question was added?") is **still
  open** — recommend Keval send a live test submission through the actual public ad now rather
  than waiting for organic traffic to prove it, since a full business day may pass with zero
  confirmation either way otherwise.
- **Studio: confirmed 0 leads for the FULL DAY** (₹180.65 spend, midnight–~7PM) — no longer "too
  early to call," this is now the final today-so-far number. See Section 3.
- **No new SVD visits today** (still 0, unchanged from the 5PM check).
- **No new dials logged on any watchlist lead since the 5PM check** — Ankit, Sandesh Padwal,
  Parag Gore, Sham Gosavi, Srikant Iyer all sit exactly where they were 2 hours ago. See Section 6.

## 1. HEADLINE
**The 1BHK campaign has now spent a full business day (₹541.28, 7 Meta-reported leads) without
producing a single lead the sales team can call — the phone-question fix has not been confirmed
working end-to-end, and nobody has tested it live yet.** Secondary: Studio closed the day at
**zero leads on ₹180.65 spend**, its first full 0-lead day in recent memory — worth a look even
though one day alone isn't a fatigue verdict.

## 2. THE FUNNEL (full day, midnight–~7PM IST, 18 August) — by campaign
| Campaign | Spend | Impr | Reach | Clicks | Link clicks | Leads | CPL |
|---|---|---|---|---|---|---|---|
| Studio | ₹180.65 | 1,423 | 1,256 | 12 | 7 | 0 | — |
| 2BHK | ₹895.14 | 3,824 | 2,699 | 88 | 54 | 1 | ₹895.14 |
| 1BHK (new) | ₹541.28 | 2,176 | 1,606 | 78 | 38 | 7 | ₹77.33 |
| **Combined** | **₹1,617.07** | **7,423** | **5,561** | **178** | **99** | **8** | **₹202.13** |

- Studio: 0 leads on ₹180.65 spend, the whole day. Delivery itself was healthy (1,423
  impressions, 12 clicks) — this is a conversion gap, not a delivery outage. Confirmed via direct
  Graph API check: `account_status: 1` (ACTIVE), balance ₹58,831, `disable_reason: 0` — not an
  account problem.
- 2BHK: still just the 1 lead from this morning, Sangeeta Asnani (10:52am, ig, "2BHK 29 Seconds |
  connectivity hook") — contacted same-day.
- 1BHK: 7 leads per Meta's canonical count (`onsite_conversion.lead_grouped` = 7, matches `lead`
  and the other action types 1:1 — no double-count anomaly). Of these, only 1 (Madhu Tiwari) has
  any CRM record; the rest are inferred from the identical dashed-phone pattern in `facebook_tab`
  (see 5b) since the CRM tab (`Sheet3`) hasn't caught the other 6 yet.
- Contacted: Studio n/a, 2BHK 1/1, 1BHK 0 of 7 reachable by phone.
- Site visits logged today: 0.

## 3. AD PERFORMANCE (agency hat) — by campaign
- **Studio:** CTR 0.84% for the full day — below its recent 1.5–2.2% range, and now backed by a
  full day's sample (12 clicks / 1,423 impressions), not just a thin morning read. Frequency
  1.13, normal — this isn't fatigue from over-showing to the same people. Yesterday this same
  campaign did 4 leads on ₹773.34; today, more than 4x less spend AND zero leads. One low day
  isn't a trend, but it's the first time in recent reports Studio has gone a full day at zero —
  worth checking again tomorrow before writing it off as noise.
- **2BHK:** CTR 2.30%, frequency 1.42 — both normal, no fatigue signal. "2BHK 29 Seconds |
  connectivity hook" carried nearly all of today's spend and the lead (₹849.67, CTR 2.35%); the
  "36 Seconds" and "29 Seconds | Legacy hook" variants got token spend with 0 leads — same
  pattern as the 5PM check, connectivity-hook remains the working creative.
- **1BHK — day 2 of real delivery, still no meaningful trend to compare against.** CTR strong:
  "1BHK Hindi" 4.82%, "1BHK Gujarati" 2.99–4.14% (split across the still-unconsolidated
  duplicate adsets `Open - DJR - 1BHK` / `Open - DJR - 1BHK gujrati`) — both well above Studio's
  and 2BHK's today. Every number Meta shows looks great; Section 5b is why that's currently
  meaningless in practice.

Trailing 7 days (pre-1BHK): Studio ₹8,240.08/35 leads/CPL ₹235.43; 2BHK ₹8,565.45/26 leads/CPL
₹329.44 — today's Studio (0 leads) sits below this range for the first time; 2BHK sits within it.

## 4. SPEED-TO-LEAD (sales-manager hat)
Unchanged from the 5PM check: only one lead today has a working CRM record with a phone —
Sangeeta Asnani (2BHK), contacted same-day with real requirement info captured (day-level
precision; no finer `contact_history` bracket available for her yet).

The 1BHK campaign — 7 leads, potentially the day's fastest-moving story — remains completely
unmeasurable for speed-to-lead, because 6 of 7 leads have no phone number anywhere in the system
and the 7th hasn't synced to the CRM at all. That gap is itself today's most important
speed-to-lead finding: the team cannot be fast or slow on a lead they can never dial.

| Lead | Meta arrival (IST) | Sheet update | Lag |
|---|---|---|---|
| Sangeeta Asnani (2BHK) | 10:51:59 | same day (exact time not in `contact_history` yet) | same-day, precision day-level only |
| 1BHK leads (7) | 13:20–~7PM (exact times mostly not visible) | 6 of 7 appear same-day as dashed-phone "Dead" rows within minutes; 1 not yet synced | not computable — no phone to anchor contact_history, and the "contact" itself is a same-minute auto-Dead, not a real call |

## 5. LEAD QUALITY (sales-manager hat)
Sangeeta Asnani (2BHK): wants "both" (unspecified config), Mulund (matches project location),
budget undisclosed — no obvious mismatch flag, too early to grade further.

1BHK leads: quality remains UNASSESSABLE — no phone, and 5 of the 6 dashed-phone rows carry no
requirement/feedback text at all (just "Not contact"), so there's no signal beyond a name and
email.

**Real cost-per-visit vs vanity CPL — 28-day window, 19 Jul–18 Aug, CRM-verified only:**
- Studio + 2BHK: spend ₹53,927.29, leads 162, vanity CPL ₹332.88.
- 14 CRM-verified visits (unchanged — no new SVD entries today).
- **Real cost-per-visit: ~₹3,852. Visit rate: 8.64%.** (1BHK excluded — zero visit history since
  it only launched yesterday; its 7 leads/₹541.28 sit outside this ratio.)
- All-campaigns-combined 28-day spend (including 1BHK): ₹54,468.57 / 169 leads / vanity CPL
  ₹322.30 — shown for completeness, but the Studio+2BHK-only figure above is the fair
  apples-to-apples number since 1BHK can't convert to a visit yet.

## 5b. DATA INTEGRITY CROSS-CHECK
**Still the day's dominant issue, now confirmed unchanged across two checks ~2 hours apart:** the
1BHK campaign's leads land with no phone number, and the sales team marks them Dead within
minutes without ever being able to call them. See FOLLOW-UP section above for what's changed
(nothing) since the 5PM report. Full chain of evidence (unchanged from the earlier report today):
`Sheet3` connected but its 2 rows (test lead + Madhu Tiwari, 13:36 IST) predate the phone
question being added to the form; Madhu Tiwari cross-matches to a dashed-phone `facebook_tab` row
marked Dead within minutes; 5 more identical-pattern rows (Urmi Gala, Vilas Shah, Lalji, Priyanka
Rane, Shailesh) strongly suspected to be the rest of today's 7 Meta-reported leads, manually
entered from Ads Manager since the auto-sync hasn't caught them.

**Reverse-check / phone-typo tracked list — NOT independently re-verified today** (this run's
integrity-check time again went to confirming the 1BHK situation was unchanged rather than a
fresh sweep): Jigna Rathod, Atul Thorat (typo-explained), Sandesh Padwal (typo-explained), Ankit
(typo-explained), Bhavin Vora, Nikita Gaurav, Sandesh Howal, Srikant Iyer. **This is now two
runs in a row without a full re-check — do it first thing next calendar-day run, not carried
forward a third time.**

## 6. DIAGNOSTIC STEPS
1. **URGENT, agency+sales — get a live confirmation on the 1BHK form fix, don't wait for organic
   traffic.** Keval or the team should submit the actual public ad's form once, right now, and
   confirm a phone number reaches `Sheet3`/`facebook_tab`. A full business day of ₹541+ spend
   has produced zero confirmation either way. If it's still broken, pause or throttle 1BHK until
   fixed — every lead today has been functionally wasted regardless of its great CPL.
2. **Sales — Ankit (day 8), Sandesh Padwal (day 26), Parag Gore (day 3) — still no dial logged
   today at all**, per either the 5PM or this ~7PM check. Push all three first thing tomorrow;
   numbers: Ankit 7201116501 (sheet shows a typo'd "7201116501" vs CRM/memory's "7021116501" —
   worth double-checking which is correct before dialing), Sandesh Padwal 9819910699 (sheet) /
   9819910669 (memory) — same typo-risk flag, verify against the CRM record before calling.
3. **Sales — Sham Gosavi, zero contact in 2+ days now.** Still no follow-up logged at all since
   his 16 Aug creation. Call tomorrow without waiting for his own "coming after 2 days" timeline.
4. **Sales — Srikant Iyer (day 7) and Celine (day 23+), still zero record anywhere.** Ask the
   team directly whether these were ever actually dialed off-sheet.
5. **Agency — consolidate the duplicate "1BHK Gujarati" adset** (`Open - DJR - 1BHK` vs
   `Open - DJR - 1BHK gujrati`) so performance data isn't split across two buckets.
6. **Agency — watch Studio tomorrow.** One 0-lead day on reduced spend isn't a trend yet, but
   it's a first — if tomorrow also underperforms the ₹235 CPL / steady-lead baseline, treat it as
   a real signal, not noise.

## 7. ANYTHING ELSE
Item 2 above surfaced a phone-number MISMATCH between what's in `facebook_tab` today and what
`reports/_memory.md` has been carrying for Ankit and Sandesh Padwal (last digit pairs transposed
in both cases — "7201116501" vs "7021116501", "9819910699" vs "9819910669"). This wasn't checked
digit-by-digit before; flagging it now rather than repeating a possibly-wrong number in another
diagnostic step. Whoever calls these two tomorrow should pull the number directly from the sheet
row itself, not from a prior day's report, until this is resolved.

## LOOKING AHEAD
- Get a live, confirmed-working 1BHK form submission with a real phone number — the single
  highest-priority open item after two checks today with zero movement.
- Resolve the Ankit / Sandesh Padwal phone-number discrepancy noted above before the next call
  attempt.
- Full reverse-check re-verification — now overdue two runs running.
- Watch Studio's next full day for a repeat 0-lead outcome before calling it a real dip.
- Watch for Ushma Katira's revisit (last note: "coming tomorrow" as of 17 Aug, still no update)
  and Shikha Thakkar's 23 Aug commitment.
