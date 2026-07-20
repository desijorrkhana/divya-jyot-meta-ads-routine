# Routine memory — read at the start of every run, update at the end

## Updated 2026-07-20 (catch-up run after 15-day report gap, last report was 4 July)

- **CRM/2BHK blind spot (top priority, new this run):** all 138 rows in `meta_leads_timed`
  since 10 June are tagged campaign="Divya Jyot V3 June26"/adset="Open - DJR" — the "2BHK"
  campaign (39% of last-30-day leads) has zero footprint in the CRM Event sheet. Speed-to-lead
  and intent analysis are blind to those leads. Check every run whether this is still true; if
  it's fixed, note it and restore full-coverage speed-to-lead.
- **Fake-attribution pattern is now systemic, not isolated:** 9 of 18 (50%) "Meta Sent ✅"
  Facebook SVD visits in the last 30 days have no CRM match. New this week: Payal Shah
  (18 Jul, 9769884201) and Vidhi Thakkar (20 Jul, 9820194111) — neither has ANY record in
  facebook_tab or CRM, unlike the Dedhia case which at least had a facebook_tab row. Watch for
  more of these every run; ask the team directly where these leads actually came from.
- **Sushma Ravasia / "Jagdish Ravasia {Sushma}" (9372158643 vs her real 8850455636):** visit
  logged 20 Jul under what's almost certainly her husband's name/phone (same SVD row number as
  her facebook_tab row, matching flat req, her own row says "Visit done" 20/7). Circumstantial
  but strong — confirm with team, currently counted as a real V3 visit.
- **Sunil Bagul (8108715063):** still unresolved since 3 July — one "Busy" note, nothing since.
  16+ days cold. Needs a decision (call or mark Dead), not another flag next time.
- **Atul Thorat (correct number 9819877789):** the "fix" attempt made it worse — sheet now
  shows `98198777789`, an 11-digit garble matching neither the correct number nor the original
  typo (8198777789). Still status Dead. Re-check whether anyone has actually called the right
  number.
- **Ravi (9321110668 / 8369593191):** both numbers now listed on one row (typo papered over,
  not resolved) but the lead itself is stalled at "21/6/26 Ringing" — a month with no update.
- **Positive: orphaned-lead logging mostly fixed.** 30-day CRM-to-sheet match rate is now
  95/96 (99.0%), up from 93.6% on 4 July. Andre Rozario got logged. Keep tracking this rate —
  don't need to re-flag individual leads unless it regresses.
- **Sunil Sidhwani (9175119337, arrived 19 Jul 23:48, within_3_months):** wants 2BHK at ₹1.4cr
  vs. the studio/₹87L product — budget/layout mismatch despite good intent tier and same-day
  contact. Watch whether the team screens this out or keeps chasing a bad fit.
- **"Kulin Ganatra" (9820154624, entered 19 Jul, no CRM match):** inferred but unconfirmed to
  be the invisible 2BHK lead Meta counted for 19 Jul. Only "Ringing" so far — follow up on
  outcome and whether the CRM-gap theory holds (check if a future revision reveals his true
  campaign once/if the 2BHK feed gets fixed).
- **Ashok Savalkar:** "20/7/26 Call back 4pm" — check next run whether that call happened.
- 2BHK ad "2BHK 36 Seconds" frequency climbing (2.95 over 30d) — not fatigue yet (CTR still
  2.12%), but worth checking again next run before it becomes one.
