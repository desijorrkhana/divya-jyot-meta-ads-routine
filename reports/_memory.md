# Routine memory - read at the start of every run, update at the end
# Rewritten fresh each run (spec: keep under ~40 lines). Older daily blocks live in git history and in reports/*.md.

## Added 2026-11-25 (run, ~7PM IST Wed; filed as 2026-11-25 = run date per spec)
- First calls RESTARTED 25 Nov: rows 2011-2019 all got Feedback in a batch between 12:38PM and 6:10PM (lags 15-41h). Redials still zero: dated notes 19 Nov 76, 20 Nov 7, 21-25 Nov 0 (five days). Check whether any 26/11 dated notes appear.
- Manoj Thakker 9323408101 (Studio, within 3m, 25 Nov 6:20PM): no row at 7:02PM. Check row + note and lag tomorrow.
- New notes to track: Kapil Dalvi 9820767161 (2BHK, Mulund, details shared; best lead, needs visit date). Sapna Tiwari 9324577748 (wants 2BHK, "call evening" 25 Nov: was it made?). Jagdish Newalkar 9833604080 ("call after 2 days" = 27 Nov). Vipin Kulkarni 9769930080 (2BHK at 1cr, Bhandup; probably short). Unreached: Meghana Joshi 9930855319 (Out of service), Sanjay Bhavsar 9619588264, Manisha N. Kanchan 9082009254, Sadhana 9773044313, Kabita Deore 7350894162.
- Neha Dedhia re-lead closed by team: new row 2017 "time pass customer". contact_history bracket for her is the OLD row 1525: ignore it.
- 25 Nov so far: Rs 436, 2 leads (Studio 1, 1BHK 1, 2BHK 0); spend light for 7PM (603, 582 the two days before). 24 Nov full day: Rs 834, 4 leads.
- Window 26 Oct-25 Nov: Rs 21,581, 99 leads, 8 verified visits = Rs 2,698. Nov MTD Rs 17,661, 85 leads, 6 visits = Rs 2,943 (7.1%). No visit since Laxman 19 Nov (SVD row 140 still the last row); 20-25 Nov Rs 4,099, 17 leads, 0 visits.
- Promised visits not logged: Mamta Sahal 9820837510 (20/21 Nov, no call since). Jyotish Badiyani 8425873716 (23-24 Nov passed, no note since 20/11). Narendra Amratlal Shah 9892938080 ("next week" = 23-29 Nov). Piyush Kasiyani 8898090909, Nandkumar Vatare 9029952687: no second note.
- One-dial-only within-3m leads: Rajesh Pawar 8459089972, Hitesh Pandya 7977228181, Harshada Nare Gaonkar 8422074324 (since 13 Nov).
- Still open: Rikin Gandhi 9867932469 NO ROW (day 13). Ashok Thakkar no note since 11/11. Mitesh Madnani since 13/11. Ankit Rai since 17/11. Laxman post-visit one call 20/11. Vidyanand Pathak none since 16 Nov. SVD row 137 Shivdas still 9820900416.
- Ads 7d (18-24 Nov) CPL: Studio Rs 224 (CTR 2.22), 1BHK Rs 235 (CTR 3.07), 2BHK Rs 402 (CTR 2.57). 1BHK fatigue test FAILED to trigger: 24 Nov closed 2.40%, 25 Nov 2.89%; Hindi 30d freq 3.09, only 1BHK ad. 2BHK Legacy hook 30d Rs 888/lead (2 leads), starved (Rs 4), still ON; connectivity hook CTR 3.72/4.55 two days.
- Studio form keeps bringing 1BHK/2BHK asks (Vipin, Sapna asked 2BHK), nobody asking for a studio.
- Pending with Keval: 1BHK price band; budget/config question on Studio form; Legacy hook off; second 1BHK creative; first-call rule (same day before 6PM, by 11AM otherwise).
- Integrity: forward misses 4 standing (Rikin, Milind Jadhav, Latasha Parab, Vijay Gopalani typo) + Manoj tonight. Reverse 3 unchanged. Status column blank on rows 2010+. Malformed Created dates (row 2011 "23/112026", row 1979 "1111/2026") drop rows out of date-filtered scans: list recent rows by phone match or row position. Team types Created a day early on some rows.
- DASHBOARD FIX STILL NOT ON MAIN: build_dashboard.py line ~211 matches only "facebook"/"facebbok"; fuzzy fix lives on branch claude/wizardly-carson-ocsvja. Re-flagged 25 Nov.
- Revision history: 5 revisions in the 2-day window on 25 Nov (better). Yesterday's 7PM sheet reading narrows a bracket: use it.
- Setup: python3 -m pip install --ignore-installed cffi cryptography google-api-python-client google-auth google-auth-httplib2 openpyxl, then fetch (first try, ~35s). Scheduler asks yesterday's date: file under run date. CLAUDE.md = CLAUDE-crossref-routine.md. Account status via direct Graph call: 1 (active).
