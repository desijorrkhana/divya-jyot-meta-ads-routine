# Routine memory — read at the start of every run, update at the end

## Added 2026-08-19 (evening run, ~7:11PM IST)

- **Studio: TWO consecutive full 0-lead days (18 Aug ₹180.65, 19 Aug ₹193.77).** CTR/frequency
  both healthy both days, account confirmed ACTIVE (₹96,503 balance) via direct Graph check.
  This has crossed from "one day, could be noise" into a real signal. **Next run: if a 3rd
  0-lead day happens, this is the headline. Check whether anyone tested the Studio form live
  (recommended today) and whether the Studio pixel/dataset got attached (recommended
  yesterday morning, confirmed still missing via adsets API today).**
- **1BHK form fix CONFIRMED holding on day 2: 8/8 today's leads have real phones, all dialed
  same-day.** But a NEW bottleneck replaced the old one: only 3 of 8 (Raju Dangi, Jinesh Shah,
  Satyam Barnwal) synced to CRM `Sheet4`; the other 5 (Manish Doshi, Shailesh, Gunjan Gangar,
  Reva Amit, Rashi) are sheet-only as of ~7PM. **Next run: check if these 5 backfilled
  overnight — if not, this is now a standing sync-lag problem, not a one-off, escalate
  explicitly to Keval.**
- **Two NEW reverse-check misses found this run (full sweep re-verified, first time in 3
  runs):** (1) Mahesh Gupta, 17 Aug, dashed phone — looks like the 1BHK form-bug pattern but
  Meta shows ZERO 1BHK spend on 17 Aug, so it's unrelated/unexplained, not part of that chain —
  keep watching, don't assume it's the same bug. (2) "Srishti [punit bhayani]", 15 Aug — solved:
  relative-tag pattern like Jagdish Ravasia, real CRM lead "Punit Bhayani" exists from 3 Aug
  with a different phone. No action needed, just documented.
- **Atul Thorat's phone is STILL wrong, and changed shape again**: now `98198777789` (11
  digits, extra stray "7"), still not the real `9819877789`. 8+ weeks unresolved since first
  flagged 24 Jun. Push this explicitly next time — it's a 10-second fix nobody has done.
- **Raju Dangi (today's 1BHK lead) wants COMMERCIAL, not residential** — flag if he calls back,
  likely a mismatch not worth much more call time.
- **3 straight zero-site-visit days now (17-19 Aug)** — last visit was Manoj Goklani, 16 Aug.
  Watch if this breaks tomorrow or becomes its own trend alongside Studio's lead drought.
- **Cost-per-visit, 28-day window (20 Jul-19 Aug), Studio+2BHK only: ~₹4,095/visit, 8.07% visit
  rate, 13 CRM-verified visits / 161 leads / ₹53,234.68 spend.** Window shifted forward a day
  from the last report (was 14 visits/₹53,927.29/19Jul-18Aug) — the drop from 14→13 is just the
  window rolling forward with no new visit added, not a data problem.
- **Sandesh Howal: zero calls logged in 20 days (last note 30 Jul, tagged "Broker") despite
  still showing status "Cold".** Not previously flagged this way — worth asking the team
  directly whether he was reclassified/dropped rather than simply forgotten.
- **Watchlist, unchanged / still zero contact since 17 Aug:** Ankit (`7201116501` per sheet,
  mismatch vs older memory value still unresolved), Sandesh Padwal (`9819910699` per sheet,
  same caveat), Jigna Rathod, Nikita Gaurav, Parag Gore, Srikant Iyer (day 7, zero follow-up
  ever), **Sham Gosavi (created 16 Aug, zero follow-up in 3 days now — longest untouched)**.
- **Ushma Katira** — post-visit "coming tomorrow" note (17 Aug) still stale, 2 days now (check
  her SVD-tab row, not facebook_tab, for updates).
- **Shikha Thakkar** — still "next Sunday" (23 Aug), no change. **Dhananjay Kholamakar**
  (note: sheet spells it "kholamakar") — "coming this Thursday" = 20 Aug, tomorrow, watch it.
- Reverse-check / phone-typo list fully re-verified THIS run (was overdue 2 runs) — do NOT
  need a full re-sweep next run unless something looks off; spot-check is enough.
- Telegram delivery: confirm this run's send succeeded before assuming the routine is done —
  check the printed line after `--send`.
