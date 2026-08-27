# Routine memory — read at the start of every run, update at the end

## Added 2026-08-27 (run, ~7PM IST)

- **BACKLOG-COHORT DISCREPANCY (22 vs 11, open since 24 Aug) — RESOLVED this run.** Exhaustive
  recheck (own row + every OTHER facebook_tab row sharing the same phone, since a redial is
  sometimes logged as a brand-new duplicate row instead of a follow-up column + linked SVD)
  finds only **7 genuinely untouched leads** in the 1–17 Aug (99-lead) cohort: Vinod Panchal
  (`9821077073`), Rajesh Mehta (`9820249947`), Hitesh (`9137860437`), Srikant Iyer
  (`8879085434`), Kripal Singh (`7045334487`), Milind Apte (`9004378780`), Mahesh Gupta (dashed
  phone, uncallable). Full methodology written into a LEARNED RULES update in
  `CLAUDE-crossref-routine.md` (extends the 07-29 duplicate-phone rule). **Next run: re-verify
  this 7-figure holds; if it drifts again, move the computation into `fetch_all.py` itself.**
- **Srikant Iyer (8879085434, created 12 Aug) — day 16, STILL zero contact ever.** Survives
  every methodology correction. Push for an explicit decision (call or write off) — this has
  now been flagged for over two weeks straight.
- **NEW phone-typo flag: Manali Bhat, facebook_tab row #1665 (created 27 Aug), phone
  `98892377787` (11 digits, extra "8") should be `9892377787`.** Same failure pattern as Atul
  Thorat (24 Jun) — she is currently uncallable until fixed. Confirm next run whether the typo
  got corrected and she got dialed.
- **Site visits: FOURTH straight zero-verified-visit day** (12 CRM-verified, flat since 23 Aug).
  Real cost-per-visit now ~₹4,410.78, visit rate 5.94%. This keeps happening despite fast,
  active contact work — looks like a conversion/closing problem, not a contact-effort problem.
  Longest zero-visit stretch this routine has tracked; watch urgently whether tomorrow breaks it.
- **1BHK Hindi ad — zero leads today on ₹406.24 spend with a normal CTR (1.71%, 16 link
  clicks)**, a sharp reversal after 4 leads (26 Aug) and 11 leads (25 Aug) on similar/lower
  spend. Read as noise for now (small same-day sample) but flagged — **next run: check whether
  it repeats. One zero-lead day is noise, two in a row is a signal worth investigating the form
  itself for.**
- **Rama Verma's "coming today" (made 25 Aug) — now 2 days overdue, zero redial logged.**
  **Suraj Shukla's "coming tomorrow" (made 24 Aug) — now 3 days overdue, zero redial logged.**
  Both need a direct redial to close the loop, escalating each day they're not closed.
- **Kadam Snehal Prathamesh (9870543084, 2BHK-ad lead who said "budget 90 lakhs," flagged 26
  Aug) and Amit Nathani (8779448443, budget ₹1.5-1.75cr above the 2BHK ceiling, flagged 26
  Aug) — neither has a new follow-up yet, still on day-1 feedback (day 2 now).** Not urgent yet
  (normal cadence is 1-2 days) but worth a call today before it becomes a 3rd flag.
- **khan (8454971010) — feedback still "Muslim," now day 5, no re-contact.**
- **Kamlesh Doshi (7208544065) — still not requalified, no contact since 23 Aug (day 5).**
- **Naresh Marpalli's SVD phone typo — still NOT fixed, now 8th flag** (8108784706 should be
  8108784766) — the lead itself IS being actively worked, this is purely a data-cleanliness
  issue.
- **Arvind Gupta duplicate (2 rows) and Mangesh Jadyal duplicate (3 rows) — still unmerged**,
  both actively worked as recently as 23 Aug — cleanup pending, not neglect.
- **contact_history revision coverage was thin this run (only 6 revisions scanned in the 2-day
  window, vs the usual 8+)** — brackets came back null for all 5 of today's leads even where
  the live sheet showed contact already happened. Fell back to day-level precision. Watch
  whether coverage recovers on the next run.
- **Account health confirmed via direct Graph API: ACTIVE, balance ₹46,301, no billing issue.**
- **Studio SiteVisit pixel — reconfirmed missing again today** via direct Graph API check
  (adset "Open - DJR" still no pixel_id/custom_event_str). Cheap fix, still open, multiple
  flags now.
- **2BHK "57 Seconds" — still fully dark, zero spend again today, several days running now.**
- Telegram delivery: confirm this run's send succeeded before assuming the routine is done —
  check the printed line after `--send`.
