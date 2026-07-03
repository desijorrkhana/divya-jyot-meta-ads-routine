# Routine memory — read this at the start of every run, update at the end

## Watch next time (from 2026-07-03 report)
- **Reachability wall**: 16/28 leads this week stuck on repeated unanswered "Ringing" (some 7 days straight). Check next run whether this improved — did any of these (Jyothi Gowda, saumya, mittal devesh gangani, Paresh shah, Hiren Kenia, Manisha Bhagwanani, Riya R Dalvi, jai shri krishna, Mital Joshi, Chavan, Doshi Jaswant, Dilip Gawai, Anjali Warang) get picked up, or are they going cold?
- **Named warm leads to follow up**: Priya (said coming Saturday, 2BHK), Naresh Khatri (₹90L budget fits, said coming), Dhanraj (said coming Sunday), Surendra Prajapati (₹90L fits, within_3_months, but unreachable 7 days as of 7/3 — did a channel change get tried?). Check next report whether any of these actually visited.
- **Shanker Tekwani**: within_3_months lead, 1-day contact lag, budget came back marginal (₹80L vs ₹87L ask) — see if this closes or dies on budget.
- **Hitendra/Heena Dedhia**: confirmed site visit on 7/3 (arrived FB tab 7/1, 2-day contact lag). Follow up on outcome — does this convert?
- **SVD tracker data-quality gap**: it contradicted the primary Facebook log for at least one visit (Swati Wankhede — SVD shows "Not interested," FB log confirms a visit happened). Worth periodically re-checking whether this is a one-off or systemic undercount.
- **June 18 batch backlog-clear**: 17/88 leads all first-contacted on the same day after sitting 4-9 days. Confirm this was a one-time event, not a recurring monthly pattern — check if there's a similar cluster again in mid-July.
- **3 leads never logged in Facebook tab at all** (Ravi DU, Andre Brian Edward Rozario, Atul Thorat) — worth asking Keval whether these were manually handled outside the sheet or genuinely dropped.

## Hypotheses to confirm
- Is the "budget not disclose" pattern in feedback notes actually hiding location mismatches (the historically dominant quality leak), rather than the leak having genuinely disappeared this week?
- Real cost-per-visit (~₹4,843 over the last 30 days) — is 3.5% visit rate a real dip from the ~4.5% baseline, or an artifact of undercounting in the sheet? Re-derive next run with a fresh 30-day window and see if the number is stable.

## Pending recommendations (check if acted on)
- Different call-time strategy or WhatsApp/SMS nudge after 3 unanswered ringing attempts — flagged as the single highest-leverage fix on 2026-07-03.
- Budget-screen on the first call for leads with terse "budget not disclose" notes.

## Technical notes for future runs
- `fetch_all.py` was fixed on 2026-07-03: Meta Graph API v25.0 requires `action_attribution_windows` as plain strings (`"7d_click"`, `"1d_view"`), not the old `{event_type, window_days}` object form — the old form now hard-fails every insights call with HTTP 400. Also added a 25s timeout + retry to the Google Sheets client, which had no timeout and could hang the whole run indefinitely on a proxy stall.
- Facebook tab dates are DD/MM/YYYY throughout almost the entire sheet; only the very first ~18 rows (earliest entries, July 2025) are MM/DD/YYYY. Parse DD/MM first, fall back to MM/DD only if invalid.
