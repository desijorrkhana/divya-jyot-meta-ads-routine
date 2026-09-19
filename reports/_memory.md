# Routine memory — read at the start of every run, update at the end

## Added 2026-09-19 (run, ~7:10PM IST data)

- **ESCALATED per standing instruction: named priority backlog needs a DIRECT INSTRUCTION from
  Keval to the team, not another report flag.** Mahesh Mandlik (spelled "Mandilik" in the sheet —
  search for that spelling), Sunil Guraldas Sidhwani's Vastu callback (see below, now the sharpest
  case), Ankit/Jigna Rathod/Parag Gore/Dileep Mehta's real numbers, Niilesh Kathole, Mahesh Kondal,
  "Raj," Hitesh Munshi, Ramesh Khade — 4+ consecutive reports, zero progress. Even the WRONG-number
  redials (Parag Gore, Dileep Mehta) stopped for 2 straight days (18th, 19th) — nobody is dialing
  these numbers at all anymore, right or wrong.
- **Sunil Guraldas Sidhwani (9175119337) — now the most urgent single case.** He's a DUPLICATE
  lead: original Studio submission 19 Jul, visited 7 Aug ("Visit done"), then RE-SUBMITTED the
  form for 1BHK on 16 Sep (new facebook_tab row same phone). That new row's only entry is "Vasstu
  problem" (16 Sep) — 4 straight days of total silence since. This is a warm, previously-converted
  (visited) lead going cold over an addressable objection, not cold outreach. CHECK FIRST THING
  NEXT RUN whether a callback finally happened.
- **Nitin Gurav — RESOLVED.** Contacted, feedback "Busy" logged (attempted, no connect yet).
- **2 new/newly-discovered leads**: Swati Kawade (9325890164, fb, 1BHK Hindi, 3-6_months, budget
  1.01-1.10cr, arrived 02:16:34 19 Sep, "Ringing" logged) and Mahesh Rathod (9920286150, fb, 1BHK
  Gujarati, within_3_months, budget 1.11-1.20cr, arrived 21:23:31 18 Sep — post-7PM, invisible to
  the 18 Sep report — "Cut the call" logged). Both dialed fast, neither connected yet — CHECK
  whether either gets a real connect next run.
- **contact_history had a ~16-hour overnight scan gap (last scan 18:53:01 on the 18th, next scan
  10:51:50 on the 19th)** — widened both new leads' lag brackets to hours instead of minutes.
  Nothing to fix (Drive quota pacing, as designed) but worth noting precision was worse than
  recent days.
- **Raju Kasabe (9004034850) — genuinely good news.** CRM lead 16 Sep (1BHK Hindi, within_3_months,
  below-1cr) -> CRM-verified visit 19 Sep, logged SAME DAY with no lag (unlike Nirav Madiyar's
  1-day lag). Clean 3-day lead-to-visit. CHECK post-visit outcome next run before it goes stale
  like Nirav Madiyar's did.
- **Nirav Madiyar — still no post-visit outcome logged**, 2 days since his 17 Sep visit. Flag
  again if still nothing next run.
- **1BHK Gujarati's streak-break (18 Sep, 2 leads) looks like a one-off** — reverted to 0 leads
  today, only 1 of the last 9 days had any Gujarati leads. Don't call it recovered yet.
- **2BHK's CTR-below-7-day-range problem resolved after 2 days** — today's CTR (2.51%) is back
  in range. No 3rd-day escalation needed on that specific metric.
- **Studio now on a 3rd straight zero-lead day (17, 18, 19 Sep)** — new pattern, not previously
  tracked at this length. Watch for a 4th day before treating as a real trend; Studio historically
  runs thin volume so this may just be noise.
- **1BHK CTR hit a new 7-day high today (2.95%, prior max 2.20%)**, driven by Hindi (3.13%).
- **"2BHK 57 Seconds" — 33 days dark, 6th straight report flag.**
- **Cost-per-visit trailing 30d (21 Aug-19 Sep): 12 CRM-verified (Rs 4,417.73/visit, 7.06%), 17
  explained total (Rs 3,118.40/visit, 10.00%).** Vanity CPL Rs 311.84 (170 leads/Rs 53,012.80) —
  window rolled forward, dropping a high-lead day (19 Aug) out of the lookback; not a real quality
  change, just the rolling-window edge. Don't compare this lead-count number to yesterday's 189
  without noting that.
- **Reverse check: 22 unmatched, unchanged. Forward check: 16 unmatched, unchanged.** Clean sync
  night again — both new leads matched correctly on both sides.
- **CODE BUG FOUND AND FIXED in build_dashboard.py this run** (not fetch_all.py) — see the new
  LEARNED RULE in the main spec file. Two things were fixed: (1) the SVD source classifier now
  matches "facebbok" as well as "facebook" (previously silently dropped Nityanand Singh's row from
  the dashboard entirely); (2) added the missing Dhaval/Urmi (9821799349) ANNOTATED_OK entry that
  an earlier day's memory claimed was already added but never was. Pushed directly to `main`
  (build_dashboard.py is NOT covered by report-sync.yml's auto-copy — this is a structural gap,
  now documented). CONFIRM NEXT RUN that this survived the next scheduled dashboard build.
- **Naresh Marpalli SVD phone typo — 31st flag** (8108784706 should be 8108784766), still
  uncorrected.
- Telegram delivery: confirm this run's send succeeded — check the printed line after `--send`.
