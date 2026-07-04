DIVYA JYOT LYF REWA — DAILY SNAPSHOT — THU 3 JULY 2026
Window: yesterday, full day (midnight-midnight IST). First automated run — no prior report to follow up on.

INFRA NOTE (fixed before this report could run)
Meta Ads data was 100% broken — every API call was 400ing (v25.0 changed the attribution-window format). Also fixed a Google Sheets race condition that was corrupting reads mid-fetch. Both fixed and verified. Numbers below are real.

1) HEADLINE
CPL looks mediocre (Rs 180) but the real number is good: ~Rs 2,200-2,550 per confirmed site visit, 6.7% visit rate — beating the ~4.5% V3 baseline. The problem yesterday wasn't the ad, it was sales: a 3-6mo lead (Sunil Bagul) sat unlogged and uncalled for 20+ hours, and 3 older leads from weeks ago were never entered in the sheet at all.

2) THE FUNNEL — yesterday, full day
- Spend: Rs 721.26
- Impressions: 3,583 | Reach: 2,838
- Clicks: 78 (link clicks: 50)
- Leads: 4 — canonical count verified against lead_actions_raw, no double-count. CPL: Rs 180.31
- Platform split: 2 Facebook / 2 Instagram
- Contacted by team: 3 of 4 same-day. Untouched: 1 of 4
- Site visits logged yesterday: 1 (a returning FB lead, not one of yesterday's 4 fresh leads)

3) AD PERFORMANCE (agency hat)
- Yesterday: CTR 2.18%, CPC Rs 9.25, CPM Rs 201.30, Frequency 1.26
- Last 7 days: CTR 2.48%, CPC Rs 8.32, CPM Rs 205.95, Frequency 1.80
- Last 30 days: CTR 2.78%, CPC Rs 8.48, CPM Rs 235.52, Frequency 2.73
- Not fatigue — frequency yesterday is LOWER than the 7d/30d figures, audience is turning over. CTR softening slightly alongside falling frequency is mild, not an alarm. Don't touch creative on this alone.
- Single creative, single real adset ("Studio" in "Open - DJR") carries all spend and leads. "Luxury - DJ" adset spent Rs 7.76 over 30 days for 0 leads — immaterial, but fold it in.
- Today so far (partial): Rs 570.10 spent, 4 leads, CPL Rs 142.53, CTR 2.55% — tracking fine.

4) SPEED-TO-LEAD (sales-manager hat) — most important section
Yesterday's 4 Meta leads, matched by phone to the Facebook tab:

- Doshi Jaswant | arrived 15:20 IST | just_exploring | Cold, "Ringing" (attempted, no connect) | 0-day lag (attempted same day)
- Dhanraj | arrived 15:21 IST | within_3_months | Cold, "Details shared, coming Sunday" | 0-day lag — CONNECTED
- Sunil Bagul | arrived 19:41 IST | 3-6_months | NOT IN THE SHEET AT ALL | untouched, 20+ hrs and counting
- Amey Angane | arrived 22:09 IST | within_3_months | Cold, "1RK, Rs 70L budget, coming tomorrow" | 0-day lag — CONNECTED (budget mismatch flagged below)

Precision note: the sheet has no per-call timestamps, only the row's Created date and free-text feedback — lag above is day-level, not hour-level.

Credit: 3 of 4 got a real same-day attempt, 2 of those became real conversations with budget/timeline captured. Solid work.

The miss: Sunil Bagul is exactly the case this section exists to catch — OTP-verified, phone in hand, 3-6mo intent, never called or logged. Call him first thing.

Bigger pattern: widening to the trailing 30 days (94 Meta leads, 88 matched to the sheet = 93.6% match rate), 3 of the 6 unlogged leads are WEEKS old and simply never made it into the sheet: Ravi DU (10 Jun), Andre Rozario (14 Jun), Atul Thorat (24 Jun). Not a speed problem — a logging leak. Worth checking the form-to-sheet handoff.

5) LEAD QUALITY (sales-manager hat)
- Status breakdown, last 30 days (94 leads): 76 Cold, 11 Dead, 6 never logged, 1 Warm. Most "Cold" leads are early-stage, not confirmed low quality.
- Dominant quality leak, confirmed in data: of 88 leads matched to real feedback text, 36 (41%) explicitly asked for a 1BHK/2BHK/1RK — a flat mismatch since this project is a bare-shell studio only. Zero matched leads' feedback mentions "studio" specifically. Ad/instant-form likely isn't making the product clear before people submit their number.
- Budget mismatches spotted directly: Amey Angane offered Rs 70L against the Rs 87L ask; several recent leads cited Rs 75-90L for 1BHK requests.
- Real cost-per-site-visit vs vanity CPL (the metric that matters):
  - Last 30 days: 6 confirmed visits / Rs 15,259.80 spent / 90 leads = Rs 2,543 per visit, 6.7% visit rate. Beats the ~4.5% baseline.
  - Last 7 days: 2 visits / Rs 4,384.74 / 27 leads = Rs 2,192 per visit, 7.4% visit rate. Trending better than the 30-day average.
  - Yesterday alone: 1 visit / Rs 721.26 — too small a sample to trend, noted only.
  - Bottom line: don't touch this ad on CPL. The number that matters is beating baseline.

6) DIAGNOSTIC STEPS
1. [Sales, urgent] Call Sunil Bagul (8108715063) today — untouched 3-6mo lead, 20+ hrs cold.
2. [Sales] Investigate the 3 fully-orphaned leads from weeks ago — find where they fell out between form and sheet. Also spot-check today's newest leads (Manoj Agrawal, Subhash Soni) aren't repeating the pattern.
3. [Agency] Tighten ad copy to make "bare-shell STUDIO" explicit before the click — 41% of engaged leads want a BHK layout this project doesn't have. Messaging fix, not a pause/budget call.
4. [Agency] Fold "Luxury - DJ" adset's token spend into "Open - DJR" — 0 leads for Rs 7.76 over 30 days.
5. [Sales] Screen budget in the first minute of every call (per Amey Angane, Rs 70L vs Rs 87L ask) — saves follow-up cycles on leads that can't close here.

7) ANYTHING ELSE
SVD tab's "Meta Sent" column (confirms whether a site-visit conversion event synced back to Meta via CAPI) shows failure for essentially every visit from Aug 2025 through mid-June 2026, and only starts succeeding from ~19 June 2026 onward (6 straight successes through yesterday). If that sync was broken for ~10 months, Meta's algorithm had zero real conversion signal for most of this campaign's life — it's only had usable data for about two weeks. Worth watching that it doesn't silently break again.

---
Match rate: 88/94 (93.6%) of last 30 days' Meta leads found in the sheet; 3/4 (75%) of yesterday's. No fabricated numbers.
