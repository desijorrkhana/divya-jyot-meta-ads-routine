# Routine memory — read at the start of every run, update at the end

## Updated 2026-08-11

- **Billing outage is OVER.** account_status flipped to 1 (ACTIVE), balance topped up to
  Rs 1,02,108 (direct Graph API check, see updated LEARNED RULE in CLAUDE-crossref-routine.md —
  fetch_all.py itself doesn't fetch these fields). Real delivery resumed 11 Aug: Rs 2,023.52
  spend, 6 leads, CTR/CPM/frequency all healthy, no sign of damage from the 3-day dark period.
  Next run: confirm delivery holds at a normal pace for a 2nd day — if it drops again, that's a
  new problem, not a continuation of the old one.
- **Team activity fully recovered same day**: 116 touches on 11 Aug vs 2 on 10 Aug. Worth noting
  whether this was leftover backlog-clearing or the new normal.
- **Urgent open item: Ankit (7021116501 real / 7201116501 in sheet)** — phone typo found 11 Aug,
  within_3_months, may not have been actually reached ("Ringing" logged against wrong number).
  Check next run whether this got fixed and redialed.
- **8 named/flagged leads status after 11 Aug:**
  - Redialed 11 Aug: Sandesh Padwal (still WRONG number, 18 days uncorrected), Sangeeta Rohit
    Keshariya, Bahrati Soni, Sangita Samant.
  - NOT touched 11 Aug: Jigna Rathod (21 days, wrong number), Atul Thorat (48 days, garbled
    phone), Celine (17 straight reports, zero record), Vishal Kasar (day 6, no reconfirmation,
    highest live loss risk).
- **Suspected-fake "Meta Sent" count: 6 confirmed -> 8 pending (added Ajay Gupta 2 Aug, Subhash
  Raichura 26 Jul this run, both zero-paper-trail).** Need a closer look next run — if they check
  out as real, correct the count back down; if not, they're permanent confirmed fakes.
  Also reframed Bhavin Vora: he has a genuine facebook_tab row from 13 June (not a total
  fabrication like Sunil Prajapati) but still never entered the CRM — his visit is still a
  mis-attributed conversion, just not an invented person.
- **Two unresolved reverse-check misses, no verdict yet**: "Nikita Gaurav" (9167694214, 10 Jul)
  and "Sandesh Howal" (9324595862, 21 Jul) — no CRM match, no name-similarity candidate found.
  Don't call these typos or fakes without more evidence; revisit if a matching CRM lead surfaces.
- **"2BHK 57 Seconds" — 0 leads again on real spend (Rs 81.80), 11 Aug.** This is now the 4th+
  report flagging the same zero-conversion pattern on this specific ad. Next run: check whether
  Keval acted on the reallocate/pause recommendation; if not, escalate the phrasing.
- **30-day cost-per-visit (12 Jul-11 Aug): Rs 3,333.36/visit, 10.27% visit rate, 15 verified
  visits / 146 leads / Rs 50,000.47 spend.** Essentially flat vs the pre-outage 9/10 Aug figure
  (Rs 3,288.28, 10.34%) since nothing new landed during the 3 dark days.
- **Two re-leads worth tracking**: milind (8383061069, gave up on in June, resubmitted 11 Aug,
  team already flagged "Low budget") and CS (8080820319, marked Dead in Jan, resubmitted 11 Aug
  after 6+ months) — watch whether either converts this time.
