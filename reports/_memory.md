# Routine memory — read at the start of every run, update at the end

## Added 2026-08-19 (interactive session with Keval, morning)

- **1BHK form fix CONFIRMED WORKING: 19 Aug leads carry real phone numbers** (Rashi 7208720970,
  Manish Doshi 9029026060, Gunjan Gangar 9022112040, Reva Amit 9699998599, Shailesh 8433533722 —
  all in `facebook_tab` with digits, team already dialing). Yesterday's 6 no-phone leads remain
  uncallable unless Keval exports them from Leads Center (told him how).
- **NEW CRM tab AGAIN: `Sheet4`** (form renamed/re-created "1BHK form 8/18/26",
  form_id f:2132729500922621) — third tab churn in 2 days (Sheet3 → Sheet4). Only 1 of the 5
  19-Aug leads (Raju Dangi, 11:11 IST, within_3_months, ₹1.01–1.10cr) synced to Sheet4; the
  other 4 are sheet-only ("Unsynced" on the dashboard). **Next run: check whether the remaining
  4 backfilled into Sheet4, and watch for yet another new tab whenever the form is edited.**
- **VERIFIED VIA API (adsets endpoint, 19 Aug): ALL active ad sets already run
  `optimization_goal: QUALITY_LEAD`** ("Maximize qualified leads") — do NOT advise "switch to
  conversion leads," that was wrong; it's already on. Key difference found: **2BHK + both 1BHK
  ad sets have `promoted_object` wired to pixel 1523674755877090 / custom event "SiteVisit"
  (the V3 CRM Events dataset) — Studio's two ad sets have NO dataset/event attached (page_id
  only).** Recommended to Keval: attach the same dataset+SiteVisit event to Studio (accepting
  a learning-phase reset). **Track whether he does it, and watch Studio's delivery after.**
- **Direct consequence for integrity checks: 2BHK/1BHK ads now literally optimize on pushed
  SiteVisit conversions (~14 real/28d), so every fake "Meta Sent ✅" visit (4 confirmed in 30d)
  is ~22%-level signal pollution — treat any NEW fake pushed visit as a top-severity finding,
  not a bookkeeping note.**
- **Keval started updating Leads Center stages daily as of 19 Aug** — encourage/verify this
  keeps happening; it's the main quality signal for Studio until its dataset is wired, and
  supplementary signal for 2BHK/1BHK.
- Dashboard code (build_dashboard.py) gained two features on 19 Aug, both live on main:
  no-phone leads and CRM-unsynced leads now appear in Open integrity flags AND the Speed to
  lead table ("Unsynced" campaign chip, ⚠ by name). Live URL:
  https://divya-jyot-meta-ads-routine-dashboard.keval-921.workers.dev

## Updated 2026-08-18 (2nd run today, ~7PM check)

- **1BHK phone-number gap: unresolved across TWO checks today (~5PM and ~7PM), zero movement.**
  Same 2 blank-name/blank-phone rows in `Sheet3`, same 6 dashed-phone rows in `facebook_tab`
  (Urmi Gala, Vilas Shah, Lalji, Priyanka Rane, Shailesh, Madhu Tiwari). No live test of the
  fixed form has been done by anyone yet. **Next run: check for ANY post-fix submission with a
  real phone. If still none after a full second day, escalate to "ask Keval to test it live"
  explicitly rather than waiting for organic traffic — a full business day of silence is now the
  norm, not a fluke.** Duplicate-adset issue ("1BHK Gujarati" under two adsets) also still
  unconsolidated.
- **NEW FINDING — phone number mismatch for Ankit and Sandesh Padwal between the live sheet and
  what prior reports/memory have been carrying.** Sheet today: Ankit `7201116501`, Sandesh Padwal
  `9819910699`. Prior memory/reports: Ankit `7021116501`, Padwal `9819910669` (both have
  transposed digits vs the sheet). Not yet determined which is correct — flagged in today's
  report so nobody dials a possibly-wrong number off an old report. **Next run: check whether
  this was a data-entry correction in the sheet, or whether the report has been carrying a typo
  for weeks — resolve which number is real.**
- **Studio: 0 leads for the FULL DAY on 18 Aug (₹180.65 spend)** — first full 0-lead day seen in
  recent reports. Delivery itself healthy (impressions/clicks normal), account confirmed ACTIVE.
  One day isn't a trend. **Next run: if Studio is also weak, treat as a real signal, not noise.**
- **Ankit, Sandesh Padwal, Parag Gore — still zero dial today (18 Aug) as of ~7PM,** both checks.
  Day 8 / day 26 / day 3. See phone-number caveat above before calling.
- **Srikant Iyer — day 7, still zero CRM record, zero follow-up ever.** Unchanged.
- **Celine — day 23+, still zero record anywhere** (not re-verified this run, carry forward).
- **Sham Gosavi (created 16 Aug) — zero follow-up logged, now 2+ days.** Needs a call regardless
  of his own "coming after 2 days" timeline.
- **Ushma Katira — post-visit note still "coming tomorrow" as of 17 Aug, no update today.** Note:
  her post-visit follow-ups live in the SVD-tab row (visited 14 Aug), not facebook_tab — check
  there, not the pre-visit facebook_tab row, for her latest status.
- **Shikha Thakkar's visit slipped to "next Sunday" (23 Aug)** — unchanged, watch that date.
- **Arvind Gupta's "coming tomorrow" (16→17 Aug) did not convert** — no new note since 17 Aug.
- **Dhananjay Kholamkar — 20 Aug (Thursday) commitment still stands,** no new note.
- **Reverse-check/phone-typo tracked list NOT independently re-verified for TWO runs running**
  (17 Aug and both 18 Aug runs) — do a full re-check first thing next calendar-day run, don't
  carry forward a third time: Jigna Rathod, Atul Thorat (typo-explained), Bhavin Vora, Nikita
  Gaurav, Sandesh Howal, Srikant Iyer.
- **Cost-per-visit, 28-day window (19 Jul–18 Aug), Studio+2BHK only: ~₹3,852/visit, 8.64% visit
  rate, 14 verified visits / 162 leads / ₹53,927.29 spend.** (1BHK's 7 leads/₹541.28 excluded —
  no visit history yet.)
- **Process note: this was the SECOND run of the daily routine on 18 Aug** (first at ~5PM,
  reaching main at 11:39 UTC; this one ~7PM). Ran the full pipeline (fetch, analyze, write,
  commit, Telegram send) as instructed rather than assuming duplicate — if a genuine same-day
  double-fire recurs without new information to report, a future run should judge whether a
  second Telegram send is warranted rather than sending automatically.
