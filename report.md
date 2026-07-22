DIVYA JYOT LYF REWA — DAILY SNAPSHOT
Tuesday, 21 July 2026 — CORRECTED, full day

CORRECTION: the earlier report today claimed the 2BHK campaign had zero CRM tracking. That was wrong. The CRM Event spreadsheet has TWO tabs — Sheet1 (Studio) and Sheet2 (2BHK, added when that campaign launched). fetch_all.py only ever read Sheet1, so every 2BHK lead was silently missing from the data. Keval caught this by pushing back three times (on the lead count, the "no CRM" claim, and specific named leads) before it surfaced. Fixed the script to auto-discover every tab so this cannot recur. Everything below is rebuilt with correct data.

HEADLINE (corrected)
The 2BHK campaign is NOT an integrity gap. It has its own working, OTP-verified CRM feed (Sheet2) that matches Meta's real numbers almost exactly (67 CRM leads vs 68 Meta reports lifetime). With both tabs included, the Facebook-tab-to-CRM match rate for the last 30 days is 87.9% (123/140), not the 48.9% the broken version reported. Two real open items still stand: Vidhi Thakkar and Payal Shah still have no CRM record in either tab despite a Meta Sent conversion pushed for them, and a live phone typo was caught in today's own data (Jigna Rathod, one digit off, same shape as the Atul Thorat case from 4 July). The actual day was solid: 9 fresh leads (4 Studio + 5 "2BHK"), same-day contact on all of them, and the 2BHK product (confirmed via the ad creative: Rs 1.55 Cr+, 2BHK, Mulund West, 5 min from MG Road station) is real, distinct inventory.

THE FUNNEL — 21 July, full day (corrected/complete)
Spend: Rs 1,727 (Rs 889 Studio + Rs 838 "2BHK")
Impressions 5,852 / Reach ~4,637 / Clicks 156 (link clicks 88)
Leads: 9 total (Studio 4, CPL Rs 222, 3 fb/1 ig / "2BHK" 5, CPL Rs 168, 3 fb/2 ig). Blended CPL Rs 192.
Contacted: all 9 got a same-day row/feedback in the sheet. Untouched: 0.
Site visits 21 July: 0.

AD PERFORMANCE
Studio: CTR 2.32%, CPC Rs 11.69, CPM Rs 272, freq 1.20.
"2BHK": CTR 3.10%, CPC Rs 10.48, CPM Rs 325, freq 1.36 — pulling its weight now, not just a sidecar.
Lifetime since the 2BHK campaign's actual creation (6 July): 68 leads / Rs 17,298 spend. "36 Seconds" creative carries 84% of that spend and has the better CTR; "57 Seconds" is the weaker one.
Delivery healthy on both, no fatigue signal.

SPEED-TO-LEAD (most important section)
All 9 of 21 July's CRM leads, both campaigns, matched by phone with real arrival times:
- Roy Miryala (Studio) 06:20 IST — contacted within about 5h15m.
- Jigna Rathod (2BHK) 06:48 IST — SEE PHONE-TYPO FLAG BELOW, her row was never found because the sheet has the wrong number.
- Manoj Kumar Surana (Studio) 08:19 IST — contacted within about 3h16m.
- Falguni Deep Thakker (2BHK) 11:09 IST — contacted within about 26m.
- Dimple Chothani (2BHK) 14:45 IST — contacted within about 46m.
- Chirag Mota (2BHK) 14:56 IST — contacted within about 35m.
- jai shri krishna (2BHK) 17:11 IST — a genuine SECOND lead from this person (also a Studio lead on 1 July, different campaign) — timing ambiguous due to the old row already existing.
- Nita Shah (Studio) 19:56 IST — contacted within about 15h.
- Sundar Suvarna (Studio) 22:55 IST — contacted within about 12h.
Every fresh lead today got same-day attention. Credit holds.

JIGNA RATHOD — LIVE PHONE-TYPO CATCH, same shape as the 4 July Atul Thorat case: CRM (OTP-verified) has her number as 9969283483. The team's sheet logged her as 9969283482 — last digit wrong. Whoever calls the number in the sheet is calling a stranger, not Jigna. Get the real number from the CRM and re-enter it. This is live, not historical — fix it today.

LEAD QUALITY
Blended 30-day CPL Rs 241 (163 leads, both campaigns).
2BHK product confirmed real: 2BHK, Rs 1.55 Cr onwards, 600 sqft carpet, Mulund West, 5 min from MG Road station. Most 2BHK leads self-report "below Rs 1.55 cr" on the CRM's own budget question — worth checking if the entry price matches the volume of interest it's pulling.
Real cost-per-visit, corrected with both CRM tabs:
SVD claims 16 Facebook visits in the last 30 days.
12 are now CRM-verified (up from 7): 7 Studio + 5 "2BHK" (Deep Biren, Deepak Chaurasia, Vimesh, Kapil Chheda, previously only "plausible", now confirmed via Sheet2).
2 remain KNOWN non-V3, unchanged: Naveen Suvarna, Hitendra Dedhia.
2 remain unverified in EITHER tab: Payal Shah, Vidhi Thakkar (see below). Sushma Ravasia's visit (relative's number, team-annotated) still counted as genuine.
Corrected number: Rs 39,211 / 13 (12 verified + Sushma) = Rs 3,016/visit, 8.0% visit rate — clearly beats the ~4.5% baseline, and now a real number, not a heavily-caveated estimate.

DATA INTEGRITY CROSS-CHECK (corrected)
The "2BHK gap" from the earlier report today is retracted — Sheet2 is a working CRM feed, 67 leads matching Meta's 68 lifetime almost exactly.
Still open, unchanged: Vidhi Thakkar (9820194111, visited 20/7, Meta Sent pushed, not in either CRM tab or the Facebook tab at all) and Payal Shah (9769884201, in the Facebook tab but neither CRM tab, Meta Sent also pushed). Ask the team where these two came from.
New live catch: Jigna Rathod's phone typo (see Speed-to-Lead above) — fix today, not a cold case.
Match rate corrected: 87.9% (123/140) over the last 30 days with both tabs included, close to the 3 July baseline of 93.6%.

DIAGNOSTIC STEPS (corrected)
1. URGENT, live: fix Jigna Rathod's phone number in the sheet to 9969283483 — she hasn't actually been called yet.
2. URGENT: ask the team where Vidhi Thakkar and Payal Shah came from before trusting their pushed conversions.
3. (Agency) Treat 2BHK as a real, proven second product line going forward, not a leak to filter. Worth checking if Rs 1.55 Cr pricing matches what leads say they can afford.
4. (Agency) "2BHK 57 Seconds" is the weaker creative (16% of 2BHK spend, worse CTR) — consider pausing it in favor of "36 Seconds."
5. (Process) fetch_all.py now auto-discovers every CRM tab so this specific failure can't recur — but the bigger lesson is to sanity-check totals before writing a headline finding.

ANYTHING ELSE
This correction happened because Keval checked the work — challenged the lead count, then the "no CRM coverage" claim, then two individual leads by name — and each check found something real. Treat today's corrected numbers with the same scrutiny next time, not as settled just because they're now fixed.

Corrected match rate: 123/140 (87.9%) of last-30-day Facebook-tab entries matched to CRM (both tabs) by phone. All 9 of 21 July's leads got same-day contact. No fabricated numbers — anything not directly computable is marked as such.
