# Routine memory — read at the start of every run, update at the end

## Added 2026-09-03 (run, ~7:10PM IST data)

- **URGENT — account_status flipped back to 1 (ACTIVE), balance ₹1,698, disable_reason 0 — but
  delivery is STILL zero, a 2nd straight dark day.** All 3 campaigns confirmed `effective_status:
  ACTIVE` with full `budget_remaining` (not budget-capped), no `issues_info` flags. This RULES OUT
  the simple "billing hold, wait for it to clear" story from yesterday — the account is clean by
  every API-visible signal and still not spending. **Next run: re-check account_status fresh
  FIRST. If still ACTIVE-but-dark on day 3, stop treating this as self-resolving — say so plainly
  and recommend escalating to Meta support directly, don't just repeat "wait it out."**
- **Zero sales-side dial activity logged ANYWHERE in the sheet today (3 Sep) — checked directly,
  no row in facebook_tab or svd_tab carries a "3/9" dated entry.** A real reversal from 2 Sep's
  strong catch-up effort. Two explanations, undetermined: (a) team genuinely didn't call today,
  or (b) today's calls happened but aren't logged yet (lag). **Next run: check if 3 Sep entries
  appear backfilled. If they do, it was a lag — say so and stop worrying. If 3 Sep is STILL
  empty even after another day, that's a real process gap, escalate harder.**
- **Dinesh Kukreja (9819422186) and Satya Bhatia (9821022491) — now day 4, ZERO follow-up since
  arriving 31 Aug — literally nothing added past the original intake note on either row.** The
  worst neglect currently being tracked. **Next run: confirm they finally got a first call —
  day 5 if not, escalate by name in the headline, not just a diagnostic bullet.**
- **Srikant Iyer (8879085434, day 22), Vinod Panchal (9821077073, day 31), Hitesh (9137860437,
  day 22) — none of these three has EVER received a second contact since their original intake
  note.** Not "gone cold" — genuinely never called back. This is worse than a speed-to-lead lag;
  it's leads the team appears to have logged and forgotten. Keep pushing every run.
- **Mangesh Jadyal (9730229334) — "2/9/26 Visited out of budget" note, still ZERO matching SVD
  row, now 1+ day old with no new note either way.** Leaning toward miscommunication (not a real
  visit) the longer this goes unconfirmed. **Next run: if still no SVD match, say so plainly and
  push the team for a direct yes/no rather than carrying it a 3rd day.**
- **Sonal Pandya and Karishma Chheda — RESOLVED (partially).** Both SVD rows now read "budget not
  disclose" — team did have the conversation, both declined to give a number. Drop from "unasked"
  tracking; Sonal's stated ₹1.50cr (from her original CRM record) still sits above the ~₹1.4cr
  2BHK ceiling if that number holds — worth one direct follow-up on whether ₹1.4cr works for her,
  low priority.
- **Suraj Shukla (9699995989) — "coming next week" promise from 25 Aug is now well over a week
  overdue, still no visit, last dial 2 Sep ("Ringing"), no dial today.** Worth a direct question
  about the promise specifically next time he's reached, not another generic "Ringing" entry.
- **Arvind Gupta's two rows (9324315180 / 9234315180) — no dial today on either, so no new signal
  on which is real.** Still unresolved, low urgency (he's still being reached via one or the
  other most days).
- **Reverse check stable at 21/457 (4.6%), forward check 100% (92/92) — 4th straight clean run,
  same 21 names, no new unexplained rows** (expected: zero new leads Sep 2 or Sep 3).
- **4 unresolved SVD rows, unchanged for a 4th straight run**: Bhavin Vora, Neha Joshi, Jayesh,
  Divya Singh — no CRM match, no FB-call tag, no typo found.
- **Naresh Marpalli's SVD typo — still not fixed, 15th flag** (`8108784706`→`8108784766`).
- **Jyoti Gowda's "already visited... liked 631" claim (29 Aug) — day 6, still no SVD match,
  still no team answer.** Push every run until resolved.
- **2BHK "57 Seconds" — essentially no real spend at all in the last 30 days of data (one ₹0 row
  21 Aug) — still no explicit kill/keep decision, now the longest-open ad-side item.** **1BHK
  Gujarati — 5 straight zero-lead REAL delivery days (28 Aug–1 Sep)**, the 2-day account outage
  doesn't extend or reset this streak — needs a fresh, undiluted read once delivery resumes.
- **"2BHK 29 Seconds (connectivity hook)" is the actual current workhorse variant** for 2BHK
  (last real lead 31 Aug) — worth naming explicitly in reports so it doesn't get lost in the
  36-second/57-second framing.
- Telegram delivery: confirm this run's send succeeded — check the printed line after `--send`.
