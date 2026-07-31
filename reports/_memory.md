# Routine memory — read at the start of every run, update at the end

## Updated 2026-07-31

- **Celine — #1 open item, now ~124 hours (day 6), still ZERO record anywhere in the sheet** (26 Jul
  15:19:14, within_3_months, phone 9967446816). 6th straight report flagging this. This has outlasted
  every prior open item — next run: if still unlogged, this needs a real escalation (not another
  automated flag), someone has to physically reconcile CRM vs sheet.
- **Jigna Rathod (day 10.5) and Sandesh Padwal (day 7.5) both went COMPLETELY SILENT today** — no call
  attempt logged at all, on top of both being on wrong/typo'd numbers for 10+ and 7+ days respectively.
  This is a new, worse failure mode than the wrong-number issue itself. Next run: check if anyone called
  their real numbers (Jigna 9969283483, Sandesh 9819910669) or if the silence continues.
- **Sagar Rane — day 5 unresolved**, still on Sunil Raorane's phone (9870380830); his real number
  7738037947 (within_3_months) still nowhere in the sheet, no new note in 3 days.
- **Viren's booked visit is TOMORROW (1 Aug)** and his confirmation call has now gone unanswered 2 days
  running (30/7 Busy, 31/7 Busy). Highest-priority item for next run: did the visit actually happen?
- **Mithun Gagat RESOLVED this run** — finally reached, confirmed budget 40L/1RK, real disqualification.
  Drop from urgent tracking.
- **Raju Patil, Akshay Rahate — 3 failed voice attempts each over 3 days, still not reached.** Kritika's
  2BHK submission (26 Jul) got a 3rd attempt on 30/7 then NOTHING today — stalled, not just slow.
  Recommend WhatsApp/SMS fallback; watch next run whether it's tried.
- **NEW PATTERN, worth tracking: 1BHK/1RK-seeking leads on the Studio campaign.** 5 of last 29 Studio
  leads (20-31 Jul, 17%) explicitly wanted a 1BHK/1RK instead of a studio — 3 of those in just the last
  2 days (Suryakant Kajrolkar, Ankit Kumar Pandey, plus Mithun Gagat's 1RK). Watch whether this rate
  holds or was a short cluster; if it persists, it's worth flagging to the agency as a creative-copy
  issue, not just individual lead noise.
- **2BHK campaign CTR: 3 straight days of decline to a fresh 30-day low** (2.02% 29 Jul -> 1.51% 30 Jul
  -> 1.33% 31 Jul), with frequency flat (no classic fatigue signature). Recommended a creative test this
  run, not a pause. Watch next run whether CTR keeps falling or stabilizes, and whether a test was
  actually started.
- **Site visits: back to zero on 31 Jul**, one day after Pawan Varma (30 Jul) broke a 3-day dry spell.
  Real V3 visit count holds at 17 (30-day window 2-31 Jul), cost-per-visit Rs 3,047.61, 9.50% visit rate.
  Watch whether zero-visit days start stacking again.
- **Priyank Thakkar's "out of service" (30/7) softened to "incoming not available" (31/7)** — could be
  temporary, not confirmed dead. One more attempt warranted before writing off.
- **Devangi Piprani Mehta — 4 attempts across 4 days (Voicemail, Ringing, Ringing, Busy), still no live
  conversation.** Carried, watch for a connect or escalate.
- **Ashok Savalkar — day 5 quiet** since his 26 Jul "1cr budget" note. Live warm negotiation going cold;
  needs a nudge.
- **Jagdish Ravasia {Sushma}'s promised update is due ~1 Aug** — nothing yet as of 31 Jul, on schedule.
- **Reverse-check misses (5, unchanged): Atul Thorat, Nikita Gaurav, Jigna Rathod, Sandesh Howal, Sandesh
  Padwal.** Phone-typo/never-logged CRM gaps (3, unchanged): Sandesh Padwal, Celine, Sagar Rane. Both
  fully explained, no new mystery gaps this run — 34/34 (100%) match rate on this week's fresh leads.
- **ENVIRONMENT: fetch_all.py crashed on `_cffi_backend` import error this run** (google-auth's
  cryptography dependency lacked its Rust/cffi backend in this container). Fixed with
  `pip install --ignore-installed cffi cryptography` before running. Added as a LEARNED RULE in the
  spec file in case it recurs on a fresh container next run.
