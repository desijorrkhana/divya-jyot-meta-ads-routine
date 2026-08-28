DIVYA JYOT LYF REWA — DAILY SNAPSHOT — Friday, 28 August 2026
(Window: midnight-~7PM IST. Today's figures will keep moving after this report.)

FOLLOW-UP FROM LAST REPORT (27 Aug):
- Manali Bhat's phone typo — STILL NOT FIXED, now flagged a 2nd day, and something odd is
  happening. Her sheet row still reads 98892377787 (should be 9892377787), exactly as flagged
  yesterday — but her row now shows a new "Ringing" entry. If the team actually dialed the
  number as written, that's not her real phone. Either someone found her correct number
  another way (good, but the cell is still wrong and will break future matching), or a status
  got logged without a real successful dial. Fix the cell today regardless.
- Srikant Iyer (8879085434) — day 17, still zero contact ever. Unmoved again, the longest-
  running open item in this routine. New finding this run: his phone does not match ANY record
  in the CRM at all (unlike the typo cases, where a near-match exists) — worth asking the team
  where this lead actually came from, though that doesn't change the recommendation: call him
  or formally write him off today.
- Aahana and Anupama Subhash Sabat (flagged "untouched" yesterday) — both contacted since.
  Aahana: "Ringing". Anupama: "Busy". Good, same-day misses closed within 24h.
- Rama Verma's "coming today" (2 days overdue as of yesterday) — redialed today ("28/8/26
  Ringing"), no answer yet but the loop is no longer silent.
- Suraj Shukla — a discrepancy worth flagging honestly. Yesterday's and the day before's
  reports both said "zero redial logged" since his 24 Aug row. Today's re-check finds his row
  DOES carry a follow-up entry — "25/8/26 Coming next week" — which either was missed by the
  last two runs or was added since and dated retroactively. Current true state: no visit yet,
  promise now reads "next week" (not overdue yet). Worth a direct check with the team.
- Backlog-cohort 7-figure — RE-VERIFIED, holds exactly. All 7 names (Vinod Panchal, Rajesh
  Mehta, Hitesh, Srikant Iyer, Kripal Singh, Milind Apte, Mahesh Gupta) still show exactly one
  entry each, zero contact since creation. No drift.
- "khan" and Kamlesh Doshi — still untouched, now day 6 each. Neither requalified since 23 Aug.
- Naresh Marpalli's SVD phone typo — still not fixed, 9th flag (confirmed his facebook_tab row
  DOES carry the correct number — this is purely an SVD data-entry issue; lead is being worked).
- Arvind Gupta and Mangesh Jadyal duplicates — still unmerged, but both got fresh dials today —
  active, not neglected.
- 1BHK Hindi's zero-lead day (27 Aug) did NOT repeat — it produced 1 lead today. Flag resolved,
  but see AD PERFORMANCE — the CPL trend on this ad is worth watching for a different reason.

1. HEADLINE:
Leads collapsed to just 1 today — Studio and 2BHK both went to ZERO leads on a combined ~Rs632
spend, only 1BHK delivered (Krishna Upadhyay, dialed same-day). Lowest lead day of the last 10,
on the lowest spend day too (Rs1,102 vs a Rs1,400-2,400 daily range this month) — but account
status is ACTIVE, all 3 campaigns are ACTIVE with no pacing/budget issue, and frequency is flat-
to-falling everywhere, so it does not read as fatigue. Meanwhile zero CRM-verified site visits
extends to a 5th straight day (still 12 CRM-verified, flat since 23 Aug) — the conversion
problem flagged for days running is unchanged.

2. THE FUNNEL (today so far, midnight-~7PM IST) — by campaign:
- Studio: spend Rs148.17, impr 803, reach 719, clicks 14, link clicks 10, leads 0, CPL n/a
- 2BHK: spend Rs483.88, impr 1,702, reach 1,335, clicks 19, link clicks 13, leads 0, CPL n/a
- 1BHK: spend Rs470.18, impr 1,635, reach 1,316, clicks 36, link clicks 18, leads 1, CPL Rs470.18
- Combined: spend Rs1,102.23, impr 4,140, reach 3,370, clicks 69, link clicks 41, leads 1,
  blended CPL Rs1,102.23

- Leads verified against lead_actions_raw: the 1BHK lead's canonical count (1) matches the
  reported leads figure (1) exactly — no double-count anomaly.
- CRM (meta_leads_timed) shows exactly 1 lead today (Krishna Upadhyay, 1BHK Hindi,
  within_3_months, arrived 10:30:53 IST) — an exact match to Meta's count.
- Platform: fb.
- Dialed same-day: 1 of 1. Krishna's sheet row (created today) already carries feedback —
  "Busy on meeting he calll me" — by the ~7PM pull. Untouched: 0.
- Site visits logged today: 0. No new SVD row appeared (last row is still 25 Aug's Jayesh).
  Fifth straight day with zero new CRM-verified visits.

3. AD PERFORMANCE (agency hat) — by campaign:
6-day daily trend (23-28 Aug) used for comparison; today is a partial day. Direct Graph API
check today: account_status 1 (ACTIVE), disable_reason 0, balance Rs21,473 (down from Rs46,301
on 27 Aug, purely ongoing spend) — no billing/account issue. All 3 campaigns confirmed
effective_status ACTIVE, daily budgets untouched (Rs250/Rs901/Rs650 for Studio/2BHK/1BHK) — no
pacing cap explains today's low numbers.

- Studio: 0 leads. CTR 1.74% is the lowest of the 6-day window, but frequency 1.12 is ALSO the
  lowest (trend: 1.19 to 1.12, steadily falling) — reads as a quiet delivery day, not fatigue.
  Reconfirmed again via Graph API: the "Open - DJR" adset's promoted_object still has no
  pixel_id/custom_event_str, while 1BHK, 1BHK Gujarati and 2BHK adsets all correctly carry the
  pixel + SiteVisit custom event. Still open, still cheap, flagged again.
- 2BHK: 0 leads on Rs483.88 spend, the worst outcome of the week. CTR 1.12% is the window's low
  by a wide margin (previous low this week was 1.73%). Frequency 1.27 is mid-range and
  declining — not fatigue. Per-ad: "36 Seconds" carried the spend (Rs358, 0 leads, CTR 1.13% —
  well below its own 1.47-2.65% range this week); "29 Seconds Legacy hook" spent Rs126.28 (its
  highest spend day this week) for 0 leads, CTR 1.06%. Two of the campaign's four ad variants
  didn't run at all today — "57 Seconds" has now been fully dark for 7 straight days (last
  spend 21 Aug), and "29 Seconds connectivity hook" also went dark today after running every
  day 22-27 Aug. Worth checking whether Meta is simply not allocating budget to those variants,
  or whether they were manually paused.
- 1BHK: 1 lead, CPL Rs470.18. Per-ad: "1BHK Hindi" produced the 1 lead but at a CPL that's
  stayed elevated for 2 straight days now (Rs51.51 on 25 Aug to Rs158.15 (26th) to Rs651.54
  (27th) to Rs428.92 (today)) after a strong mid-week run — worth watching as a possible
  cooling trend, distinct from yesterday's "zero leads" scare (which did not repeat). "1BHK
  Gujarati" had 0 leads today despite its best CTR of the week (4.49%, Rs41.26 spend, small
  sample) — noise on small numbers, not a concern yet.

4. SPEED-TO-LEAD (sales-manager hat):
Only 1 fresh Meta lead today — a thin sample, reported honestly as such.
- Krishna Upadhyay — 1BHK Hindi, within_3_months. Meta arrival 10:30:53 IST. Sheet status:
  "Busy on meeting he calll me" (dialed, callback expected). Lag: same day (day-level only)

Precision note: sheet.contact_history's revision-mining scanned only 4 revisions in today's
2-day lookback window — thinner than yesterday's already-thin 6, and the SECOND straight day of
degraded coverage. It returned a fully-null bracket for Krishna's phone even though the live
sheet snapshot shows his row already has feedback logged — the mining tool not catching WHEN
the edit happened, not evidence it didn't happen. Falling back to day-level precision: contacted
same day, exact time unknown. Watch whether revision coverage keeps degrading over a 3rd run.

Cross intent with speed: Krishna is within_3_months and got a same-day dial — credit the team
here, this is exactly the fast turnaround an OTP-verified lead needs.

5. LEAD QUALITY (sales-manager hat):
Today's single lead is too thin to assess quality trends from — Krishna Upadhyay (1BHK Hindi,
within_3_months, budget "below Rs1.00 cr") got a same-day dial with a genuine callback signal
("Busy on meeting he calll me" — not a rejection). No budget/location mismatch evident yet.

Real cost-per-visit vs. the vanity CPL — trailing ~28 days (29 Jul-28 Aug, the full window
available), all 3 campaigns, CRM-verified only:
- Spend Rs53,884.98, 203 leads, vanity CPL Rs265.44.
- 12 CRM-verified visits, real cost-per-visit: ~Rs4,490.41. Visit rate: 5.91%. Flat at 12 since
  23 Aug — this is now the FIFTH straight day (24-28 Aug) with zero new CRM-verified visits,
  extending the longest such stretch this routine has tracked.
- Plus 4 legitimate direct-caller visits still in-window (Ajay Gupta, Sunil Prajapati, Maya
  Jain, Pravin Jain) — cost-per-visit including direct-callers: ~Rs3,367.81 (16 visits), rate
  7.88%.
- This is happening despite fast, active contact work on fresh leads (today's single lead is a
  clean example) and continued post-visit follow-up — this remains a conversion/closing
  problem, not a contact-effort problem. Worth asking the team directly, again: are visits
  genuinely stalling at the scheduling stage, or happening without making it into the SVD tab?

5b. DATA INTEGRITY CROSS-CHECK:
- Reverse check (every facebook_tab row created since V3 start, 10 Jun 2026, checked against
  CRM by phone, currency-format/dual-number/typo-tolerant normalization applied): 448 V3-era
  rows, 27 with no CRM phone match (6.0%). Breakdown: 8 are known dashed/placeholder phone rows
  (uncallable by design, mostly the 18 Aug 1BHK pipe-break batch); 3 are known typos (Atul
  Thorat, Manali Bhat, Arvind Gupta's duplicate row); 3 fit the established direct-caller
  pattern (Bhavin Vora, Jayesh, Neha Joshi — each has a long, real, dated call history
  predating or matching an SVD visit, consistent with the OTP-friction explanation Keval gave
  19 Aug); 1 is the new Srikant Iyer finding above; the remaining ~11 (Nikita Gaurav, Jigna
  Rathod, Sandesh Howal, Sandesh Padwal, Srishti, Parag Gore, Manish Doshi, Shailesh, Gunjan
  Gangar, Reva Amit, Rashi) have no obvious explanation from this run's data alone — plausibly
  non-Meta leads (referrals, walk-ins, repeat customers) the team logs in the same sheet, but
  flagged honestly as unverified rather than assumed.
- Forward check (CRM leads since 20 Aug against facebook_tab): 76 CRM leads, 75 matched cleanly
  (98.7%) — the sole miss is the already-known Manali Bhat typo. No new phone-typo misses found.
- Naresh Marpalli's SVD phone typo — still uncorrected, 9th flag (confirmed again this run).
  Lead itself actively worked.
- Arvind Gupta (2 rows) and Mangesh Jadyal (3 rows) — still unmerged duplicates, both dialed
  again today — cleanup pending, not neglect.
- Account health: account_status 1 (ACTIVE), balance Rs21,473 — no billing issue.
- CRM tab check: Sheet1-Sheet4 all present and reading correctly, no new tab appeared — no
  integration gap today.

6. DIAGNOSTIC STEPS:
1. URGENT, sales — fix Manali Bhat's phone cell (98892377787 to 9892377787) regardless of
   whether "Ringing" reflects a real contact — the cell itself will keep breaking lookups until
   it's corrected.
2. URGENT, sales — decide on Srikant Iyer today. Day 17, zero contact ever, and now a flag that
   his phone has no CRM match at all — call him now or formally write him off; stop letting this
   carry silently into a 3rd week.
3. Sales — push specifically for site-visit conversion. Fifth straight day at exactly 12
   CRM-verified visits despite fast, active contact work on fresh leads — ask the team directly
   whether visits are stalling in scheduling/closing or not making it into the SVD tab.
4. Agency — check why 2 of 2BHK's 4 ad variants ("57 Seconds," "29 Seconds connectivity hook")
   went fully dark, and why the two that ARE running both cratered to 0 leads and the week's
   worst CTR today — this, not fatigue, is what's driving 2BHK's whole day. Check adset-level
   budget allocation before assuming a creative problem.
5. Sales — requalify "khan" and Kamlesh Doshi (day 6 each, untouched since 23 Aug), fix the
   Naresh Marpalli SVD phone typo (9th flag), and merge the Arvind Gupta / Mangesh Jadyal
   duplicates once convenient.

7. ANYTHING ELSE:
Today's real story is the funnel, not the sales team — leads collapsed to 1 (vs 6-14/day this
week) on the lowest spend day of the month, with account/campaign health all confirmed clean.
Frequency is flat-to-falling across all 3 campaigns, ruling out fatigue as the cause, which
leaves either genuine day-to-day auction variance or something upstream (audience saturation
building slowly, a Friday effect, or reduced competitive pressure changing Meta's delivery mix)
that one day's data can't distinguish. Watch tomorrow closely: if leads stay this low with
spend back to normal, escalate; if it's a one-day blip, no action needed. Separately, the
Manali Bhat "Ringing"-against-a-typo'd-number anomaly is worth a direct, quick question to the
team — either they have a workaround worth documenting, or a status is being logged without a
real dial.

LOOKING AHEAD:
- Watch whether tomorrow's lead volume recovers to the normal 6-14/day range, or whether today
  was the start of a real slowdown.
- Confirm Manali Bhat's phone actually gets corrected, and clarify how "Ringing" got logged
  against the wrong number.
- Watch whether Srikant Iyer finally gets a decision (call or write-off) — day 17 is long
  enough, and confirm whether the team can explain where this lead actually came from.
- Watch whether the 5-day zero-verified-visit streak finally breaks.
- Watch "1BHK Hindi"'s CPL trend — 2 elevated days running after a strong mid-week stretch.
- Confirm whether "57 Seconds" and "29 Seconds connectivity hook" come back online for 2BHK.
- Confirm Suraj Shukla's "coming next week" promise and Rama Verma's redial actually convert.
- Watch whether contact_history revision coverage keeps degrading (4 today, 6 yesterday) — a
  3rd thin day would be worth a LEARNED RULES note.
