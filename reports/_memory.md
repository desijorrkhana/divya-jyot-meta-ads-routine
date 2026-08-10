# Routine memory — read at the start of every run, update at the end

## Updated 2026-08-10

- **Billing outage now DAY 3.** Balance has read Rs 0 for over 24 hours (since it cleared on 9
  Aug) with `account_status` still stuck at 3 (UNSETTLED) and delivery still fully dark. Next run:
  check `account_status` first thing — if it's flipped to 1 (ACTIVE) and today_campaigns has real
  rows, report the reactivation. If still 3, this is now a genuinely stuck reactivation past the
  point of "wait for it" — the language in the report should keep escalating.
- **Team activity collapsed 10 Aug: only 2 touches logged all day** (vs 129 on 9 Aug, 11 on 8
  Aug), with zero fresh leads to explain it either way. None of the 8 named priority leads from
  the 9 Aug report were retried. Next run: check whether 11 Aug returns to a normal dialing
  cadence, or whether the drop is now a pattern. If the named leads below are STILL untouched a
  2nd day running, escalate — that's no longer a one-off lull.
- **6th confirmed fake Meta-Sent visit: Sunil Prajapati** (9594868604, SVD row created and Meta
  Sent same-day 10 Aug, zero CRM match, zero prior facebook_tab row — no paper trail at all before
  the "visit"). This is a new, more brazen variant of the fake-visit pattern — worth watching
  whether it recurs, since it means a fake can be manufactured and pushed to Meta within hours.
  Fake count timeline: 4 fakes flat for 2+ weeks -> +1 (Bhavin Vora) 9 Aug -> +1 (Sunil Prajapati)
  10 Aug. Both new fakes landed on dark-account days — check next run whether that correlation
  holds or breaks.
- **Bhavin Vora (5th fake) got "10/8/26 Coming this sunday"** — watch for a "Revisit done"-style
  2nd fake entry against him, same pattern as Ajay Gupta's 9 Aug second fake visit.
- **Named leads to check on next run** (all untouched 10 Aug, all still open):
  - Bahrati Soni / Sangita Samant (6 Aug priority, 1 unanswered Ringing each, 4 days now) — still
    untested on the "different time of day" recommendation.
  - Sangeeta Rohit Keshariya (within_3mo, 6 Aug) — STILL has zero record in facebook_tab, 4 days.
  - Vishal Kasar (1BHK, Rs 1.10cr, on-budget) — promised visit since 5 Aug, day 5 now with no hard
    reconfirmation and no dial at all on 10 Aug. Highest live loss risk in the pipeline right now.
  - Jigna Rathod (real 9969283483) / Sandesh Padwal (real 9819910669) — both still on wrong
    numbers, 20 and 17 days respectively, not redialed 10 Aug.
  - Atul Thorat (9819877789, within_3mo) — 47 days, easiest fix in the report, still not done.
  - Celine (9967446816, within_3mo) — 16 straight reports now, still zero record anywhere.
- **30-day cost-per-visit (11 Jul-10 Aug): Rs 3,288.28/visit, 10.34% visit rate, 15 verified
  visits / 145 leads — unchanged from 9 Aug (no new spend or visits).** Lead count reconciled
  exactly (145 Meta vs 145 CRM) again this run.
