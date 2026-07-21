DIVYA JYOT LYF REWA — DAILY SNAPSHOT
Tuesday, 21 July 2026 — today so far, midnight to ~7:10 PM IST

REPORTING GAP: last report in the repo was 3 July — 18 days missing. Treating today as a fresh baseline. Worth checking why the daily run didn't fire/commit for over two weeks.

HEADLINE
Two campaigns are running now, not one — and only one is visible to any verification tooling. "Divya Jyot V3 July 26 - 2BHK" has run real spend for 30+ days (Rs 16,129 spent, 63 leads, ~40% of all leads) and has NEVER sent a single lead into the CRM Event sheet. Zero OTP-verified arrival times, zero speed-to-lead measurement, zero verifiable site-visit link for that whole campaign. On top of that: 2 more site visits (Payal Shah, Vidhi Thakkar) got "Meta Sent" conversions pushed despite no provable Meta-lead trail — same pattern as the Dedhia case flagged 4 July, still unresolved. Meanwhile Studio-campaign execution is genuinely excellent: 100% same-day contact, 7 days straight.

THE FUNNEL (today so far)
Spend: Rs 1,224 (Rs 643 Studio + Rs 581 "2BHK")
Impressions 3,775 / Reach ~3,107 / Clicks 108 (link clicks 63)
Leads: 7 total (2 Studio, CPL Rs 322 / 5 "2BHK", CPL Rs 116). Blended CPL Rs 175. Canonical count verified, no double-count.
Contacted: 7 of 7 same-day attempt (100%). 2 became real conversations (Falguni Thakkar, Chirag Mota). Untouched: 0.
Site visits today: 0 (last one was 20/7).

AD PERFORMANCE
Studio: today CTR 2.40%, CPC Rs 13.13, CPM Rs 315, freq 1.14 — healthy, not fatiguing (7-day freq 1.68 is higher).
"2BHK": today CPL Rs 116 is its best of the last 3 windows, CTR 3.4% its highest. Frequency climbing over 7 days (2.57) vs today (1.32) — watch, not urgent.
Of the two 2BHK creatives, "57 Seconds" is basically dead (Rs 21.65 spent yesterday, 0 leads) — "36 Seconds" is carrying the whole campaign. Consider formally pausing 57s.
Delivery healthy post the June 22 account pause.

SPEED-TO-LEAD (most important section)
Today's 2 CRM-verified Studio leads, real arrival times:
- Roy Miryala, arrived 06:20 IST, within_3_months — sheet row/feedback appeared by 11:35 AM, so contacted within about 5h15m at most.
- Manoj Kumar Surana, arrived 08:19 IST, within_3_months — same bracket, contacted within about 3h16m at most.
Both still "Ringing" (attempted, not connected yet).
The other 5 leads today (the "2BHK" campaign) have NO exact arrival time at all — not in CRM. Day-level only: all logged same calendar day. That's the best precision possible right now for 40% of leads.
Last 7 days, Studio-campaign leads with real arrival time: 17 of 17 (100%) logged same calendar day as arrival — zero lag misses. Big improvement over 3 July's 75%. Credit the team.
The catch: this clean number only covers Studio. The 2BHK campaign runs at real volume with zero lag measurement — can't tell if it's being worked as fast.

LEAD QUALITY
Blended 30-day CPL Rs 243 (not the number that matters).
BHK/1RK mismatch is still the main quality leak on Studio leads — but the "2BHK" campaign looks like it might actually be the fix for that leak (a dedicated form for BHK-seekers) rather than a new problem. WORTH CONFIRMING WITH THE TEAM: is 2BHK now real sellable inventory, or does the ad route BHK-seekers into a form for a product that still doesn't exist?
Real cost-per-visit, 2BHK gap made explicit:
SVD claims 16 Facebook visits in the last 30 days.
7 are CRM-verified genuine Studio visits — Rs 21,584 / 7 = Rs 3,084/visit, 7.6% visit rate, BEATS the ~4.5% baseline.
2 are KNOWN non-V3 (carried over from 3 July, unresolved): Naveen Suvarna, Hitendra Dedhia.
7 sit in the CRM/2BHK blind spot, can't be proven: 4 look like genuine 2BHK visits, Sushma Ravasia's visit (logged under a relative's number but self-annotated by the team, likely genuine), and Payal Shah / Vidhi Thakkar — the two flagged below as the top action item.
Best-effort inclusive number (12 counted, excluding the 2 known-bad and 2 flagged-suspicious): Rs 37,713 / 12 = Rs 3,143/visit, 7.7% rate — still beats baseline, but 7 of 16 claimed visits are genuinely unverifiable. Saying so rather than picking a flattering number.

DATA INTEGRITY CROSS-CHECK
Structural gap: all 140 leads ever recorded in the CRM Event sheet belong to the Studio campaign. Zero, ever, from the "2BHK" campaign despite 30+ days of real spend and 63 leads. This is a wiring problem — the 2BHK form's webhook was never pointed at the CRM Event sheet. Top fix priority.
Two new CAPI-pollution candidates, same shape as the Dedhia case:
- Vidhi Thakkar 9820194111 — visited 20/7, Meta Sent conversion pushed, but not in CRM and not anywhere in the team's own Facebook tab. No paper trail before the visit. Ask where this lead actually came from.
- Payal Shah 9769884201 — is in the Facebook tab (Studio-shaped ask, 300 sqft/Rs 60L) but not in CRM, and her visit also got Meta Sent. Less clear-cut than Vidhi but still unverified.
Match-rate context: Facebook-tab-to-CRM match rate over 30 days looks like it dropped to ~49% (67/137) from 3 July's 93.6%, but that's almost entirely the 2BHK gap, not a new leak — Studio-only leads matched with zero orphans/typos in the last 14 days.
Phone-typo watch: none found recently — the Atul Thorat-era problem hasn't recurred.
Name-consistency: Sushma Ravasia's visit under "Jagdish Ravasia {Sushma}" was self-annotated by the team — good practice, not a problem.

DIAGNOSTIC STEPS
1. URGENT (both hats): wire the 2BHK campaign's lead form into the CRM Event sheet. This is the single highest-leverage fix — 40% of leads currently have no arrival time, no OTP verification, no visit-verification path.
2. URGENT (sales): ask the team directly where Vidhi Thakkar and Payal Shah came from — stop pushing unverified conversions to Meta if they're not real Meta leads.
3. (Agency) Confirm with Keval whether "2BHK" is now real sellable inventory for this project, or if the ad just relabels the same studio product for BHK-seekers without fixing the mismatch.
4. (Agency) Formally pause the "2BHK 57 Seconds" creative — it's dead weight next to "36 Seconds."
5. (Sales) Keep pushing the team to write call TIME next to the date — still zero adoption, would turn today's wide brackets into exact minutes.

ANYTHING ELSE
The 18-day reporting gap means a whole campaign launched and ran for weeks without anyone getting today's CRM-gap warning. Worth finding out why the daily automation didn't produce/commit a report for two-plus weeks so an 18-day blind spot on a live campaign doesn't happen again.

Match rate: 67/137 (48.9%) of last-30-day Facebook-tab entries matched to CRM by phone (see integrity section for why). 17/17 (100%) of last-7-day Studio CRM leads matched same-day. No fabricated numbers — anything not directly computable is marked as such.
