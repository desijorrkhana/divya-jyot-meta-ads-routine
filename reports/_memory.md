# Routine memory — read at the start of every run, update at the end

## Added 2026-09-12 (run, ~7:15PM IST data)

- **Dileep Mehta — day 5, still ZERO dial on the real number (9769701334).** Wrong number
  (9769701332) sits at 3 calls total (last 11/9), no 4th call today. Needs a human to retype
  the correct number — this isn't going to self-correct.
- **"Ankit" typo — resolved in the WRONG direction.** The wrong-number row (7201116501) was
  marked "30/8/26 Not interested" — the team closed out a conversation with the wrong person.
  Real number (7021116501) has never been dialed. Same failure class as the historical Atul
  Thorat case.
- **Jigna Rathod and Parag Gore — same wrong-number pattern, already known from prior reports,
  still unresolved.** Parag Gore's wrong number (9820973478) got dialed AGAIN today
  (12/9/26 Ringing) — active, ongoing waste, not just stale. Jigna Rathod's wrong number
  (9969283482) last touched 28/8 ("Not interested"). Real CRM numbers (…479, …483) never
  dialed for either.
- **Standing pattern to watch: 4 confirmed wrong-number cases now** (Ankit, Jigna Rathod, Parag
  Gore, Dileep Mehta), found via a same-timeframe hamming-distance-1/2 scan between CRM
  forward-misses and facebook_tab reverse-misses. Worth running this same scan every future
  run rather than re-deriving from memory alone — it caught Parag Gore's fresh dial today that
  memory alone wouldn't have surfaced as "still active."
- **Satya Bhatia — RESOLVED.** Got a 2nd call today (12/9 Ringing) after 3 days stalled. Drop
  from active watch unless he stalls again.
- **Mahesh Mandlik — 14 Sep visit now 2 days out, still no reminder call logged.** Needs a call
  in the next 24-48h or the date will slip silently.
- **"Dhaval (urmii)" SVD row — RESOLVED.** CRM has "Urmi Rajgor Monani" (9594621242, arrived
  7 Sep) — clean relative-tag match. Not fake. Drop from watch.
- **6-lead never-logged backlog** (Manal 8850584609, Himalaya Agrawal 9920455937, Raju Shinde
  9987335339, Celine 9967446816, Sagar Rane 7738037947, Bahrati Soni 9820620907) — flagged one
  final time per the standing instruction from 11 Sep. **DROP from active tracking next run
  unless the team has acted on it** — don't let this become a permanent unresolved bullet.
- **Srikant Iyer (day 32), Vinod Panchal (day 41), Hitesh (day 32)** — zero 2nd contact ever,
  now flagged 6+ times with no action. **DROP from active tracking next run** per the same
  logic as the 6-lead backlog, unless something changes.
- **Niilesh Kathole (9323290235) — day 6, still zero trace.** Keep repeating the ask for a
  direct human answer; stop re-deriving from data.json, nothing new to find there.
- **Naresh Marpalli SVD phone typo — 24th flag** (8108784706 should be 8108784766).
- **NEW: Ramesh Khade (9819530753) form-vs-call budget mismatch.** CRM form said budget
  ₹1.01cr–1.10cr, but he told the sales team ₹80L max (team marked "out of budget"). Worth a
  second look if he re-engages — the form bucket isn't reliable for this lead.
- **NEW: Mahesh Kondal (9819772318) dual-product submission.** Submitted both Studio and 1BHK
  Hindi forms same day (09:30 and 08:09). Sheet has one generic "Ringing" row — team may not
  know he expressed interest in both. Worth a direct question on which product he wants.
- **NEW: 3 unexplained SVD rows, all pushed to Meta as conversions** — Neha Joshi (24/8),
  Jayesh (25/8), Divya Singh (30/8). No CRM match, no FB-call tag, no typo/relative-tag
  candidate found (checked this run via hamming-distance + name search). Worth a source
  spot-check with the team; per standing rule most unmarked direct-callers turn out legit, so
  this isn't an accusation, just unresolved.
- **1BHK Gujarati — still fully dark**, 0 clicks today. ~17 days since a real lead now.
- **2BHK — rising CPM (8-day high, ₹505) + 2 straight zero-lead days despite the week's best
  CTR (3.08%) today.** Clicks converting to clicks but not to form-fills — worth checking the
  lead form itself, not the creative, since CTR is clearly fine.
- **2BHK 57 Seconds — 26 days dark, kill/keep call more overdue than ever.**
- **Reverse check: 22 real-phone unmatched (in line with 22-24 baseline), separately 9
  placeholder/no-phone rows** (kept as a distinct bucket — see LEARNED RULES update).
- **Forward check: 15/480 unique CRM phones unmatched** (511 total records scanned) —
  consistent with the 15/507 baseline from 11 Sep.
- **Today's speed-to-lead was genuinely strong**: 3/3 leads contacted same day, one (Madan
  Shinde) inside ~3.5 minutes — fastest logged in recent memory. Credit the team explicitly
  next time this comes up in "improve over time" framing.
- Telegram delivery: confirm this run's send succeeded — check the printed line after `--send`.
