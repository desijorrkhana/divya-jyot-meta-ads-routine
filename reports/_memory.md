# Routine memory — read at the start of every run, update at the end

## Updated 2026-08-03

- **Ajay Gupta — now a CONFIRMED fake conversion (5th in 30 days), not just a watch item.** The SVD row
  now shows "Meta Sent ✅ 2/8/2026, 5:39:34 pm" despite zero match anywhere in CRM or facebook_tab. Next
  run: check whether the tag gets removed/corrected, or whether a 6th shows up the same way.
- **Big backlog-vs-frontdoor tradeoff, 2 days running, exactly opposite each day.** 2 Aug: frontdoor fast,
  backlog silent. 3 Aug: backlog got its biggest sweep yet (~48 touches — Viren, Devangi, Jigna Rathod,
  Sandesh Padwal, Raju Patil, Akshay Rahate, Kritika ×2, Priyank Thakkar, Ashok Savalkar, plus SVD nurture
  on 8 more names), but ALL 5 of 2 Aug's fresh leads (Suhas Kuchekar, Chandril Panchal, Ajay Sharma, Dhaval
  Shah, Vishal Kasar) got zero follow-up on 3 Aug. Next run: does the swing continue a 3rd day, or does
  someone finally cover both? This is now the top open question, ahead of any single named lead.
- **Ajay Sharma (within_3mo, real 2BHK budget) — still the standing highest-value miss**, now 2 days
  without a follow-up attempt (Ringing 1 Aug → Busy 2 Aug → nothing 3 Aug). Watch specifically next run.
- **Celine — still ZERO record, now ~196 hours (day 9), 9th straight report.** Longest-open item in this
  routine's history. Next run: still worth a manual sheet check by name if nothing changes.
- **Ashok Savalkar finally got touched today (3/8 Busy)** after 7 days silent — first movement since the
  26/7 "₹1cr budget" note. Not yet a real conversation. Watch whether it continues.
- **Ronak Shah and Sujit Gupta were recalled 2 Aug but NOT recalled 3 Aug** — the "recall as recommended"
  pattern from 2 Aug did not repeat. Watch whether they get picked up again.
- **Jagdish Ravasia {Sushma}'s promised update is now 4 days overdue** (since 30/7 "update in two days").
  Re-confirmed real (not fake) again this run via the CRM's "Sushma Ravasia" match — stop re-verifying
  this every run, it's settled; just watch for the actual update.
- **Kalpesh Dedhiya (new today, within_3mo)** — the only real connection of the day: wants a 2BHK at
  ₹1.70cr (above the ₹1.55cr screening ceiling) via the Studio ad, tentative "coming for monday" visit —
  AMBIGUOUS whether today or next Monday (10 Aug). Next run: check if a firm visit date landed, and
  whether he showed up.
- **Phone-typo backlog still unfixed: Jigna Rathod (day 13, within_3mo — never actually reached because
  of it) and Sandesh Padwal (day 10)** — both dialed again today on the wrong numbers. This is now a
  13-day-old trivial fix costing a real within_3mo lead any chance of contact. Escalate harder if still
  unfixed next run.
- **Subhash Raichura (a confirmed fake) was closed out today** ("Not interested") — no further tracking
  needed on the sales side for this one.
- **"2BHK" CTR recovery (validated 1-2 Aug) reversed 3 Aug** (1.51% vs 7-day avg 1.73%; Studio also softer
  than trend). Small sample (89 clicks, partial day) — confirm whether this holds or reverses again
  tomorrow before treating it as a real trend change.
- **Real V3 visit count holds at 19 (30-day window 4 Jul–2 Aug)** — no new CRM-verified visit landed
  today (expected, zero new SVD entries). Cost-per-visit ₹2,876.49 (10.73% visit rate), essentially flat
  vs yesterday's ₹2,842.90/10.73%.
- **Reverse-check misses (5, unchanged): Atul Thorat, Nikita Gaurav, Jigna Rathod, Sandesh Howal, Sandesh
  Padwal** — all pre-26 Jul, no new ones. This week's (26 Jul–3 Aug) match rate: 40/40 = 100%, clean.
- **Meta-Sent fake-conversion count: 5 confirmed (Hitendra Dedhia, Payal Shah, Vidhi Thakkar, Subhash
  Raichura, Ajay Gupta)** — Ajay Gupta graduated from watchlist to confirmed this run.
- **Fetch note: Google Sheets 503'd on facebook_tab/svd_tab this run** (transient "service unavailable"),
  required a manual retry outside the normal fetch_all.py flow. Fixed in fetch_all.py itself (retry with
  backoff added to fetch_sheets()'s read() helper) — should self-heal from here; watch that it doesn't
  recur unfixed.
