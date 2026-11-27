# Routine memory - read at the start of every run, update at the end
# Rewritten fresh each run (spec: keep under ~40 lines). Older daily blocks live in git history and in reports/*.md.

## Added 2026-11-27 (run, ~7PM IST Fri; filed as 2026-11-27 = run date per spec)
- First-call queue CLEARED 27 Nov afternoon (notes appeared 12:43PM-6:51PM): rows 2020-2026 all have Feedback. Pattern this week = one batch every second afternoon (Wed, Fri). Check whether Sat 28 Nov leads get called same day.
- Promised visit: Rakesh Dhopat 8097507202 (row 2022, Studio form, small 1BHK, budget 65L, "coming tomorrow" = Sat 28 Nov). Check SVD for a row 141. Budget is below Studio Rs 87L.
- New 27 Nov: Arvind 7506259429 (2BHK, within 3m, 600+ sqft, 1.5cr, Navi Mumbai, details shared) = best lead. Prem Sharma 9769434384 (1BHK, 1.2cr, Mulund; old row 143 from Sept 2025, "2bhk 1.70cr", never visited). Check for second notes / visit dates.
- Unreached on first dial 27 Nov: Manoj Thakker 9323408101, Vinit Soni 9167532959 (both within 3m), Chitra Fule 9594075692. Vilas Shah 9223590058 row 2024 note is "MC BC" only (4th entry, treat as dead unless rewritten).
- Redials still zero: dated notes 19 Nov 76, 20 Nov 7, 21-27 Nov 0 (seven days). Last dated SVD note 20 Nov. Check for any 28/11 notes.
- Overdue: Jagdish Newalkar 9833604080 (due 27 Nov, no note). Sapna Tiwari 9324577748 evening call. Kapil Dalvi 9820767161 visit date. Vipin Kulkarni 9769930080 (2BHK at 1cr, offer 1BHK). No second try: Meghana Joshi 9930855319, Sanjay Bhavsar 9619588264, Manisha N. Kanchan 9082009254, Sadhana 9773044313, Kabita Deore 7350894162.
- 27 Nov so far: Rs 460, 2 leads (1BHK 1, 2BHK 1, Studio 0). 26 Nov full day: Rs 616, 3 leads. 2BHK no-lead run ended at two days.
- Window 28 Oct-27 Nov: Rs 21,378, 98 leads, 7 verified visits = Rs 3,054 (7.1%). Nov MTD Rs 18,951, 91 leads, 6 visits = Rs 3,158 (6.6%). No visit since Laxman 19 Nov (SVD row 140 still last); 20-27 Nov Rs 5,389, 23 leads, 0 visits. Rajesh Bhinde 31 Oct rolls out of the 31-day window on 1 Dec.
- Promised visits not logged: Mamta Sahal 9820837510, Jyotish Badiyani 8425873716 (no note since 20/11), Narendra Amratlal Shah 9892938080 ("next week" ends Sun 29 Nov). Piyush Kasiyani 8898090909, Nandkumar Vatare 9029952687: no second note.
- One-dial-only within-3m leads: Rajesh Pawar 8459089972, Hitesh Pandya 7977228181, Harshada Nare Gaonkar 8422074324 (since 13 Nov).
- Still open: Rikin Gandhi 9867932469 NO ROW (day 15). Ashok Thakkar no note since 11/11. Mitesh Madnani since 13/11. Ankit Rai since 17/11. Laxman post-visit one call 20/11. Vidyanand Pathak none since 16 Nov. SVD row 137 Shivdas still 9820900416.
- Ads 7d (20-26 Nov) CPL: 1BHK Rs 164 (CTR 3.05), Studio Rs 250 (CTR 2.30), 2BHK Rs 384 (CTR 2.84). 27 Nov CTR: Studio 3.28, 1BHK 3.72, 2BHK 3.55; no fatigue. Hindi 30d freq 3.15, only real 1BHK ad (Gujarati Rs 14 in 30d). 2BHK Legacy hook 30d Rs 786/lead (2 leads), starved (Rs 16), still ON.
- Studio form keeps bringing 1BHK/2BHK asks, nobody asking for a studio.
- Pending with Keval: 1BHK price band; budget/config question on Studio form; Legacy hook off; second 1BHK creative; first-call rule (same day before 6PM, by 11AM otherwise).
- Integrity: forward misses 4 standing (Rikin, Milind Jadhav, Latasha Parab, Vijay Gopalani typo). Reverse 3 unchanged. Status column blank on rows 2010+. Created now filled on 2020-2023; rows 2025-2026 typed 26/11 for 27 Nov arrivals (team types Created a day early). Malformed: row 2011 "23/112026", row 1979 "1111/2026": list recent rows by phone match or row position, never by date filter.
- DASHBOARD FIX STILL NOT ON MAIN: build_dashboard.py line 211 matches only "facebook"/"facebbok"; fuzzy fix lives on branch claude/wizardly-carson-ocsvja. Re-flagged 27 Nov.
- Revision history: 4 revisions in the 2-day window on 27 Nov (last two 27 Nov 12:43PM, 6:51PM). Yesterday's 7PM sheet reading narrows a bracket: use it. contact_history brackets for repeat phones (Vilas, Prem Sharma) describe OLD rows: ignore.
- Setup: python3 -m pip install --ignore-installed cffi cryptography google-api-python-client google-auth google-auth-httplib2 openpyxl, then fetch (first try, ~34s). Scheduler asks yesterday's date: file under run date. CLAUDE.md = CLAUDE-crossref-routine.md. Account status via direct Graph call: 1 (active).
