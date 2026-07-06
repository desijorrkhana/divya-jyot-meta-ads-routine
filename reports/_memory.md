# Routine memory — read at the start of every run, update at the end

## Updated 2026-07-06 (run covering yesterday, 5 July — routine had a 2-day gap, 4→6 July)

- **Correction carried forward:** the 3-Jul report's "3 fully orphaned leads" claim was
  overstated — **Ravi DU (9321110668) is actually in the sheet**, called 5x through 21 June;
  the phone cell holds two numbers ("9321110668 / 8369593191") and naive last-10-digit
  matching on the whole cell grabbed the wrong one. Real orphan count (10 Jun–today) is **2**,
  both wrong-number entries: **Andre Rozario** (CRM 9821266080, sheet has 8976902153, 14 Jun,
  22 days stale) and **Atul Thorat** (CRM 9819877789, sheet has 98198777789, 24 Jun, 12 days
  stale, marked Dead off the wrong number). True match rate is 98.0% (97/99), not 93.6%.
- **Watch: redial Rozario and Atul Thorat at their CRM numbers.** Neither has been correctly
  dialed since they were first (mis)logged. If still uncorrected next run, this is now a
  multi-week miss on two within/3-6-month leads — escalate harder.
- **NEW campaign to watch: "Divya Jyot V3 July 26 - 2BHK"** (adset "Open - DJR - 2BHK", ad
  "2BHK 36 Seconds") started spending 6 July — first appearance ever in the data. Directly
  cuts against the standing "clarify studio-only" recommendation. Check next run: did Keval
  confirm/pause it? Did it scale spend? Is it producing more BHK-mismatch leads?
  Also check whether its leads are landing in the CRM Event sheet at all — two 6-Jul
  Facebook-tab entries (Suvi & Sanvi, Abhishek Tiwari) weren't in the CRM sheet as of this run;
  could be ingestion lag or could be this new campaign posting to a different lead form
  (fetch_all.py fix needed if confirmed).
- **Jinal Shah (9820477153, arrived 5 Jul 13:20, within_3_months)** said she's coming Tuesday
  7 July for a visit — check next run whether that visit happened / was logged in SVD.
- **Speed-to-lead still strong:** all 4 of 5 July's fresh leads contacted same day, 3 of 4
  within an hour (Gautam Ray ≤38m, Nitin Patkar ≤21m, Rajesh Shah ≤52m, Jinal Shah ≤2h39m —
  slowest of the batch despite being highest-intent, still same-day).
- **Subhash Soni (9224597069, 4 Jul, within_3_months)** — logged and contacted, but slower:
  bracket shows 2h23m–16h44m lag (crossed overnight). Not urgent now (he's Cold/being
  pursued) but a real, if smaller, response-time gap worth noting if the pattern repeats.
- **Cost-per-visit back above baseline:** 2 new CRM-verified visits (Vipul Rakhasia, Christina
  Dias, both June-arrival leads converting 5 July) push 30-day to 6 visits/₹16,960.41 →
  ₹2,826.74/visit, 6.1% rate — beats the ~4.5% V3 baseline again (had dipped to ~4.4% as of
  3 Jul's corrected figure).
- **Pending recommendations, still not acted on (now 2+ days):** (1) ad copy should say bare-
  shell STUDIO explicitly (40.6% of this week's leads still ask for a BHK/RK — same rate as
  last report); (2) fold "Luxury - DJ" adset into "Open - DJR" (still ₹7.76/0 leads, unchanged);
  (3) team still not writing call TIME next to the date (checked recent rows, none found);
  (4) team still not copy-pasting phone numbers from the CRM sheet (both typo cases unfixed).
- **CAPI hygiene:** clean since ~19 Jun except the known Hitendra Dedhia non-CRM push (3
  Jul, unresolved, no new development this run) — watch for repeats, none seen.
- **Routine health:** no run happened 4 or 5 July (gap since the 4 Jul evening session) —
  confirm the schedule/cron is actually active if this recurs.
