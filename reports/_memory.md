# Routine memory — read at the start of every run, update at the end

## Added 2026-08-28 (run, ~7PM IST)

- **LEADS COLLAPSED TO 1 TODAY** (vs 6-14/day this week) on the lowest spend day of the month
  (Rs1,102 vs Rs1,400-2,400 range). Studio and 2BHK both went to zero leads. Account/campaign
  status confirmed clean (ACTIVE, no pacing cap), frequency flat-to-falling (rules out fatigue) —
  no explanation found. **Next run: check if lead volume recovered; if still low, escalate.**
- **Manali Bhat's phone typo (`98892377787` should be `9892377787`) — STILL NOT FIXED, 2nd day,**
  but her row now shows "Ringing" against the wrong number — cell still needs fixing regardless.
  **Next run: confirm the cell got corrected and ask how "Ringing" happened.**
- **Srikant Iyer (8879085434) — day 17, zero contact ever, most urgent open item.** NEW: his
  phone matches NO record in `meta_leads_timed` at all (unlike typo cases). Push for a decision
  (call or write-off) — cannot carry into a 3rd week.
- **2BHK ad-variant health: "57 Seconds" dark 7 straight days; "29 Seconds connectivity hook"**
  also went dark today. Only 2 of 4 variants ran, both cratered (0 leads, week's worst CTR).
  Check adset budget allocation, not creative fatigue. **Next run: watch if dark variants return.**
- **Site visits: FIFTH straight zero-verified-visit day** (12 CRM-verified, flat since 23 Aug).
  Real cost-per-visit ~Rs4,490, visit rate 5.91%. Longest stretch tracked — conversion problem.
- **Suraj Shukla discrepancy:** today found a "25/8/26 Coming next week" entry that the 26/27
  Aug reports said didn't exist (missed or backdated). No visit yet, not overdue on new promise —
  ask the team directly when it was actually logged.
- **1BHK Hindi CPL elevated 2 straight days (Rs651.54 -> Rs428.92)** after a strong mid-week run
  — watch for a cooling trend (zero-lead flag itself is resolved).
- **contact_history coverage degrading 2nd straight day** (4 revisions vs 6 vs usual 8+) — a
  3rd thin day is worth a LEARNED RULES entry.
- **khan and Kamlesh Doshi — day 6 each, still untouched since 23 Aug.**
- **Naresh Marpalli's SVD phone typo — still NOT fixed, 9th flag** (8108784706 should be
  8108784766; his facebook_tab row already has the correct number).
- **Arvind Gupta (2 rows) and Mangesh Jadyal (3 rows) duplicates — still unmerged**, both dialed
  again today — cleanup pending, not neglect.
- **Backlog-cohort 7-figure re-verified again, holds exactly** (Vinod Panchal, Rajesh Mehta,
  Hitesh, Srikant Iyer, Kripal Singh, Milind Apte, Mahesh Gupta) — no drift, 2nd straight run.
- **Account health confirmed via Graph API: ACTIVE, balance Rs21,473.** Studio SiteVisit pixel
  still missing on "Open - DJR" adset — cheap fix, still open.
- Telegram delivery: confirm this run's send succeeded — check the printed line after `--send`.
