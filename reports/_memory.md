# Routine memory — read at the start of every run, update at the end

## Added 2026-08-26 (evening run, ~7PM IST)

- **BIG METHODOLOGY CORRECTION this run: post-visit "stale" flags (Ushma Katira etc.) were
  wrong because the check read facebook_tab instead of the SVD row's own trailing columns**
  (per the existing 07-27 LEARNED RULE). Re-checked SVD directly and found 10 post-visit leads
  touched TODAY: Ushma Katira, Neha Joshi, Jayesh, Naresh Marpalli, Bhavin Vora, Dimple Dedhia,
  Vishal Thakkar, Urmila Salvi, Falguni Thakkar, Vaibhav Gandhi. **Next run: re-verify this
  wasn't a one-off catch-up day — check whether SVD trailing-column activity continues at this
  pace tomorrow, and keep checking SVD directly (not facebook_tab) for any post-visit lead
  status going forward.**
- **UNRESOLVED: backlog-cohort count discrepancy.** This run's from-scratch recount (every
  trailing column, same-row + linked SVD, excluding cross-row duplicate credit) found 22 of 99
  leads genuinely untouched since creation — the "11 untouched" figure carried since 24 Aug
  does NOT reconcile. Real untouched-22 list: Dhaval Shah, Punit Bhayani, Kaplesh Dedhiya,
  Vinod Panchal, Jitendra Gharat, Mahi, Pranav Shah, Subhash, Rajesh Mehta, Pooja, Ankit,
  Milind (`8383061069`, row #1513), Hitesh, Naresh (`8108784766`, row #1523), Srikant Iyer,
  Rohit Thakkar, Sanjay Tank, Jaspal Kaur Bindra, Kripal Singh, Sharayu Rane, Milind Apte,
  Mahesh Gupta (dashed phone, uncallable). Kajal Padhi and Manoj Goklani look untouched by a
  naive date-cutoff filter but actually already have real SVD visits (12 Aug, 16 Aug) — they
  are converted leads, not neglected ones. **Next run: recompute independently before trusting
  either number, and if the gap persists, this needs a documented, reproducible definition
  (ideally moved into fetch_all.py itself) rather than being re-derived ad hoc each day.**
- **Srikant Iyer (8879085434, created 12 Aug) — day 15, STILL zero contact ever.** The one
  finding that survives every correction above. Push for an explicit decision (call or write
  off), not another "still open" note.
- **Site visits: THIRD straight zero-verified-visit day** (12 CRM-verified, flat since 24 Aug).
  Real cost-per-visit now ~₹4,382, up only slightly since spend keeps accumulating against a
  flat visit count. This is happening DESPITE fast, active contact work on both fresh leads and
  the post-visit list (see correction above) — so it looks like a conversion/closing problem,
  not a contact-effort problem. Ask the team directly: are visits stalling, or happening and
  not making it into the SVD tab (a logging gap)? Watch urgently whether tomorrow breaks the
  streak.
- **NEW integrity flag: Naresh Marpalli's SVD phone (8108784706, known typo — real number
  8108784766) is ALSO the exact phone number on a completely different facebook_tab lead,
  "Himalaya Agrawal"** (created 19 Jun, active through 22 Aug "Not intertsed"), while "Naresh"
  (row #1523, created 12 Aug, 2BHK ₹1.30-1.40cr) is a distinct identity on the same number.
  Ask the team whether these are one person under two names or a real coincidence/typo
  collision — right now two different call histories are tangled under one phone.
- **1BHK Gujarati got its SECOND-ever lead today (Hemendra Doshi), one day after its first
  (Keval Savla, 25 Aug).** Two leads on two different days closes the multi-report watch on
  this variant — no longer needs tracking as "unproven."
- **Rama Verma's "coming today" (made 25 Aug) — still unconfirmed, no redial logged, no SVD
  row.** Suraj Shukla's "coming tomorrow" (made 24 Aug) — now 2 days past the promised day with
  zero follow-up call. Both need a direct redial to close the loop, not another day of waiting.
- **Kadam Snehal Prathamesh (9870543084, arrived today on 1BHK Hindi) — said "Looking for 2bhk
  budget 90 lakhs" on the call — an ad/intent mismatch,** same pattern as Parminder Suri
  yesterday. Her ₹90L ask is comfortably under the 2BHK ceiling if she's redirected properly.
- **Amit Nathani (8779448443, arrived today, 2BHK 36 Seconds) — CRM budget ₹1.5cr-1.75cr is
  ABOVE the 2BHK ceiling (~₹1.4cr).** Team's own note says "budget not disclose" — confirm on
  the call rather than writing him off on the CRM figure alone.
- **Nita Shah (7400119009, within_3_months tag) declined outright same-day** ("Not looking for
  any property") — a reminder that Meta's intent question doesn't always predict the real call
  outcome.
- **khan (8454971010) — feedback still "Muslim," day 4, no re-contact.**
- **Kamlesh Doshi (7208544065) — still not requalified**, no contact since 23 Aug (day 4).
- **Naresh Marpalli's SVD phone typo — still NOT fixed, now 7th flag** (8108784706 should be
  8108784766) — but per the correction above, the lead itself IS being worked, this is purely
  a data-cleanliness issue now.
- **Arvind Gupta duplicate (2 rows) and Mangesh Jadyal duplicate (3 rows) — still unmerged**,
  though both got touched in the 23 Aug mass redial — cleanup pending, not neglect.
- **Sikha Thakkar (9321915923) — visit still not in SVD, budget ₹1.50cr still above the 2BHK
  ceiling.** Unchanged from yesterday.
- **Studio SiteVisit pixel — reconfirmed missing again today** via direct Graph API check
  (adset "Open - DJR" still no pixel_id/custom_event_str). Cheap fix, still open, multiple
  flags now.
- **2BHK "57 Seconds" — still fully dark, several days running now.**
- **Account health confirmed via direct Graph API: ACTIVE, balance ₹61,385, no billing issue.**
- Telegram delivery: confirm this run's send succeeded before assuming the routine is done —
  check the printed line after `--send`.
