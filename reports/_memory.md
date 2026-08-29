# Routine memory — read at the start of every run, update at the end

## Added 2026-08-29 (run, ~7PM IST)

- **URGENT — Meta account entered billing GRACE PERIOD today** (`account_status` 9, was 1/ACTIVE
  yesterday), ₹2,67,040 owed on Visa ending 0005, `disable_reason` 0 (pure billing). All 3
  campaigns still ACTIVE and delivering today, but this is Meta's last warning before DISABLED.
  **Next run: check account_status first thing — if still 9 or now 2 (DISABLED), escalate hard.**
- **contact_history bug FIXED this run** — `_parse_fb_tab_xlsx` was reading phone from a
  hardcoded wrong column (5, a blank spacer) instead of the real Phone column (6), so every
  bracket came back null for 4 straight days (26-29 Aug). Fixed to resolve columns from the
  header row dynamically. Verified working post-fix (real brackets returned). **Next run:
  confirm brackets are still populated (not a one-time fluke) — if null again, don't assume the
  same root cause, re-diagnose.**
- **Jyothi Gowda (7304218100) — new row today claims "Visited" with NO matching SVD entry.**
  Re-engagement lead (old June inquiry, went cold, resubmitted for 1BHK). Ask the team directly
  whether this visit is real. **Next run: check if an SVD row appeared for her, or get an
  explanation.**
- **Srikant Iyer (8879085434) — day 18, zero contact ever, still unresolved.** Longest-running
  open item. Push for a decision every single run until closed.
- **Site visits: SIXTH straight zero-verified-visit day** (12 CRM-verified, flat since 23 Aug).
  Real cost-per-visit ~₹4,450.61, visit rate 5.85%. Longest stretch tracked, still growing.
- **2BHK "57 Seconds" ad variant — 8 straight dark days**, still no explanation. "29 Seconds
  connectivity hook" flag from yesterday resolved (came back online today).
- **1BHK Hindi CPL scare — RESOLVED**, cooled from ₹651.54 (27th) to ₹138.09 (today).
- **Manali Bhat's phone typo — still not fixed, 3rd flag, AND now stale** (no dial today either,
  first idle day since flagged).
- **Naresh Marpalli's SVD phone typo — still not fixed, 10th flag** (8108784706 should be
  8108784766; facebook_tab already has the correct number; lead itself actively worked).
- **khan and Kamlesh Doshi — day 7 each, still untouched since 23 Aug.**
- **Arvind Gupta (2 rows) and Mangesh Jadyal (3 rows) duplicates — still unmerged**, and for the
  first time neither got a dial today (last: 28 Aug) — watch this doesn't drift into neglect.
- **Backlog-cohort 7-figure re-verified again, holds exactly, 3rd straight run** (Vinod Panchal,
  Rajesh Mehta, Hitesh, Srikant Iyer, Kripal Singh, Milind Apte, Mahesh Gupta). Three of the
  seven are tagged "Broker" (Rajesh Mehta, Kripal Singh, Milind Apte) — worth formally closing
  rather than leaving open indefinitely.
- **Rama Verma's "coming today" (25 Aug) — now 4 days overdue**, one redial (28 Aug, no pickup),
  nothing today.
- **Suraj Shukla's "coming next week" (made 25 Aug) — not yet due, becomes checkable Monday.**
- Reverse-check reveals one previously-unnamed unmatched row: **Ankit (7201116501, 11 Aug)** —
  folded into the "unexplained non-Meta lead" bucket, not treated as new/alarming (old row).
- Telegram delivery: confirm this run's send succeeded — check the printed line after `--send`.
