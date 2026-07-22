# Routine memory — read at the start of every run, update at the end

## Updated 2026-07-21/22 (correction session — read this before trusting the 21 Jul report)

- **RETRACTED: the "2BHK campaign is untracked by CRM" finding was wrong.** Root cause: the
  CRM Event spreadsheet (`LEADS_SHEET_ID`) has TWO tabs, one per lead form — `Sheet1` (Studio)
  and `Sheet2` (2BHK, created 2026-07-06, same day that campaign launched). `fetch_all.py`
  only ever read `Sheet1`. Fixed: `fetch_sheets()` now enumerates every tab in the spreadsheet
  via `spreadsheets().get()` instead of hardcoding a tab name, and `parse_lead_rows()` accepts
  either question-wording (`when_are_you_planning_to_purchase?` vs `when_are_you_planning_to_
  buy`) and also captures a `budget` field where present (`what_is_your_budget_for_this_
  purchase?` — only on the 2BHK form). **Every future run: sanity-check that `meta_leads_timed`
  contains every campaign_name that appears in `meta.*_campaigns` before writing anything about
  tracking gaps** — this is now also a LEARNED RULE in the main routine file.
- Corrected numbers with both tabs: 209 total CRM leads (142 Studio + 67 "2BHK"), matching
  Meta's real lifetime counts (147 / 68) closely. Facebook-tab-to-CRM match rate over the last
  30 days is **87.9% (123/140)**, not the ~49% the broken version reported.
- **2BHK product is confirmed real** (pulled the actual ad creative): 2BHK, ₹1.55 Cr onwards,
  600 sqft carpet, Mulund West, 5 min from MG Road station. Update the standing business
  context — this is a real second SKU, not a mislabeled studio ad. Most 2BHK leads self-report
  "below ₹1.55 cr" on the CRM's own budget question — worth watching whether that's a pricing
  mismatch worth flagging explicitly in a future report once there's more budget-answer volume.
- **Two CAPI-pollution cases SURVIVE the correction, still open**: Vidhi Thakkar (9820194111)
  and Payal Shah (9769884201) — checked again against BOTH CRM tabs, still no match in either.
  Keep asking the team where these two came from; don't let the correction accidentally paper
  over this — it's real and separate from the tab bug.
- **NEW live phone-typo, caught same-day (not historical):** Jigna Rathod — CRM (Sheet2) has
  9969283**3**, the Facebook tab has 9969283**2**. One digit off, same shape as the 4 Jul Atul
  Thorat case. Check next run whether it's been corrected in the sheet and whether she's been
  reached.
- **"jai shri krishna" (9664658376) is a genuine repeat lead, not a duplicate row** — a Studio
  lead 1 Jul AND a separate 2BHK lead 21 Jul, same phone, 3 weeks apart. Don't assume an
  "unmatched-today" Facebook-tab row is automatically fresh — always check the phone against
  CRM directly; a returning lead can look identical to a brand-new one from the date alone.
- **Cost-per-visit, corrected:** 12 of 16 last-30-day SVD "Facebook" visits are now
  CRM-verified (was 7) — 7 Studio + 5 "2BHK" (Deep Biren, Deepak Chaurasia, Vimesh, Kapil
  Chheda, now confirmed genuine via Sheet2, previously only "plausible"). ₹39,211 / 13
  (12 verified + Sushma Ravasia's team-annotated visit) = ₹3,016/visit, 8.0% visit rate.
- **Process note for next run:** this correction took 3 rounds of Keval pushing back (lead
  count → "no CRM" claim → two specific named leads) before the root cause surfaced. The
  original report was sent to Telegram and committed before the error was caught — both have
  now been corrected and re-sent/re-committed. Lesson: before declaring a "critical tracking
  gap," check the CRM spreadsheet's own tab list, not just the one tab already known to work.
- **Speed-to-lead still excellent:** all 9 CRM leads on 21 Jul (both campaigns) got same-day
  contact, worst case ~15h (a lead that arrived at 19:56 IST). Keep watching this holds.
- **Carried forward, unchanged:** "write call TIME next to the date" still not adopted (zero
  instances in the last 150 Facebook-tab rows). "Luxury - DJ" adset still dormant (0 spend/
  leads in 30d). The two OLD known-bad SVD visits (Hitendra/Heena Dedhia, Naveen Suvarna)
  remain unresolved in the last-30-day window.
