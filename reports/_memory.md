# Routine memory — read at the start of every run, update at the end

## Updated 2026-07-18 (automated run, first since 4 July — 14-day gap)

- **2BHK campaign visibility (top priority to close):** "Divya Jyot V3 July 26 - 2BHK"
  (ads "2BHK 57 Seconds" / "2BHK 36 Seconds") has spent ₹12,777 over 30d, 57 leads per Meta
  Ads Manager, but 0 of them appear in `sheet.meta_leads_timed` (the OTP-verified CRM) —
  its leads land straight in the plain Facebook tab instead. Confirm with Keval whether this
  is a real second product (670–695 sqft, ~₹1.4–1.5 Cr per repeated feedback mentions) or a
  targeting mistake. Until it's wired into the CRM, every quality/speed check in this routine
  is studio-only by construction — say so explicitly every run, don't silently merge its
  Meta-account-level spend/leads into studio numbers.
- **Atul Thorat / Andre Rozario wrong-number cases — unresolved 14 days running.** CRM has
  Atul at 9819877789 (sheet: 8198777789, marked Dead off the wrong number) and Andre at
  9821266080 (sheet: 8976902153). Both trivial fixes (copy the CRM number), neither done.
  If still wrong next run, this is a process failure worth escalating past a diagnostic bullet.
- **Ravi DU — resolved, retire this one.** Sheet phone cell has both numbers
  ("9321110668 / 8369593191") — the 4-Jul "suspected" flag was a false alarm on our end
  (phone-parsing didn't handle multi-number cells), not a real team error.
- **CAPI hygiene — still a live risk, new instances found.** 4 more non-CRM visits since 12
  Jul (Deep Biren, Deepak Chaurasia, Vimesh, Kapil Chheda — all 2BHK-tagged) pushed to Meta
  as ✅ conversions. Plus a new pattern: Payal Shah (visit 18/7) has NO record anywhere
  (not CRM, not Facebook tab) despite a ✅ Meta Sent — ask the team where she came from.
  Keep verifying every ✅ against the CRM every run.
- **Real cost-per-visit trend — genuinely improving, keep tracking.** 4.4% (3 Jul, corrected)
  → 10.75% (18 Jul, last 30d) visit rate for studio, CRM-verified. ₹1,997/visit last 30d,
  ₹2,523/visit last 7d. Confirm this holds up over the next few runs before calling it a
  durable trend rather than small-sample noise (10 visits total).
- **15–16 July: zero leads logged anywhere** (sheet or CRM) — row numbers confirm no gap
  artifact, genuinely empty. Watch whether this recurs; if it does, it's a fetch/pipeline
  issue, not a quiet couple of days.
- **Status field hygiene:** 0 of 134 matched CRM leads are marked "Warm" ever, despite
  several with clearly positive feedback. Status column isn't a usable signal on its own —
  keep reading feedback text directly until the team starts using it.
- **Pending recommendations still open:** ad copy explicit about bare-shell STUDIO (BHK
  mismatch still 34% of matched leads, down from 41%); team to write call TIME next to date
  (checked last 60 rows, still zero instances).
- **Closed loops this run:** Manoj Agrawal → Dead/Broker (correctly filtered). Subhash Soni →
  4 attempts over 2 weeks, never connected, also a 1BHK mismatch — deprioritize further
  redials. "Luxury - DJ" adset → gone, fold-in recommendation was followed.
