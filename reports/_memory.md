# Routine memory — read at the start of every run, update at the end

## Updated 2026-08-08

- **URGENT, top priority next run: check whether the account billing hold is resolved.** Today
  (8 Aug) the account showed `account_status: 3` (UNSETTLED) via a direct Meta Graph API query —
  zero spend/impressions/leads all day despite campaigns showing "Active." ~Rs 7,141.85 balance
  outstanding, VISA ending 0005. First thing next run: query account_status again; if still 3, this
  is now a multi-day outage and needs escalated language.
- **A real fetch bug was found and fixed today** — `fetch_all.py` read `Facebook!A1:N2000` and
  `SVD!A1:O500`, missing the sheets' 5th-8th follow-up columns (real range needed: through col AG/AF).
  Fixed to `Facebook!A1:AG2500` / `SVD!A1:AF1200`. This means multiple PAST reports' "lead X abandoned
  for N days" claims may be wrong (confirmed wrong for Viren, Sandesh Padwal, Jagdish Ravasia on 7 Aug).
  Don't re-litigate old reports, but trust today's (8 Aug) figures as the first fully-correct read.
- **Vishal Kasar's promised visit slipped a SECOND time** — was "coming Saturday" (8 Aug), today's
  entry says "coming tomorrow" (9 Aug, Sunday). Check tomorrow whether it finally happens. 1BHK,
  Rs 1.10cr, on-budget — a real loss risk if this keeps sliding.
- **Bhavin Vora — claimed site visit today (8 Aug, "Visit done" in Facebook tab) but NOT in SVD yet,
  and his phone (9601341394, 13 Jun lead) has never matched CRM.** Check next run whether SVD logs it
  and whether it gets tagged "Meta Sent" — if so, that's a 5th fake, same pattern as Payal/Vidhi/
  Subhash/Ajay.
- **Bahrati Soni, Sangita Samant, Sangeeta Rohit Keshariya — all 3 sitting 2+ days on one unanswered
  "Ringing" with zero retry as of 8 Aug.** Check tomorrow whether they were finally retried.
- **Atul Thorat (9819877789, within_3mo, 24 Jun) — STILL uncorrected, 45 days.** Sheet phone still
  `98198777789`. Oldest, easiest, most-repeated fix in this routine.
- **Jigna Rathod (real 9969283483) and Sandesh Padwal (real 9819910669)** — both actively dialed
  (7 and 8 touches respectively over 15-18 days) but never corrected to the right number. Not neglect,
  just an uncorrected typo blocking real contact.
- **Celine (9967446816, within_3mo) — 14 straight reports, still zero record anywhere**, reconfirmed
  even against the full unrestricted column range today (this one is real, not a fetch artifact).
- **4 confirmed fake "Meta Sent" visits still uncorrected** (Payal Shah, Vidhi Thakkar, Subhash
  Raichura, Ajay Gupta) — re-verified today with the wider column range, unchanged, now 7+ days.
- **30-day cost-per-visit (9 Jul-7 Aug): Rs 3,131.95/visit, 10.63% visit rate, 17 verified visits /
  160 leads.** Lead count reconciled cleanly against CRM (160 vs 159) this run — the earlier
  163-vs-182 mismatch flagged 7 Aug remains unresolved and unrelated to this window.
