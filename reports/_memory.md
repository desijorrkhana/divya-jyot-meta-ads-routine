# Routine memory — read at the start of every run, update at the end

## Updated 2026-07-21 (first run in 18 days — last update was 4 Jul, treat carefully)

- **BIGGEST OPEN ITEM: the "Divya Jyot V3 July 26 - 2BHK" campaign is 100% invisible to the
  CRM Event sheet.** All 140 leads ever in `sheet.meta_leads_timed` belong only to the Studio
  campaign ("Divya Jyot V3 June26"). The 2BHK campaign has run 30+ days, ~Rs 16k spend, 63
  leads (today alone: 5 of 7 leads) with zero arrival times, zero speed-to-lead measurement,
  zero verified site-visit link. Check every run whether this has been fixed (2BHK leads
  start appearing in `meta_leads_timed`) — if not, keep flagging it as the top item.
- **Two new suspected CAPI-pollution cases, same shape as the 4 Jul Dedhia case** — watch for
  outcomes / repeats: Vidhi Thakkar (9820194111, visited 20/7, Meta Sent pushed, not in CRM
  or the Facebook tab at all — most Dedhia-like case seen since the original) and Payal Shah
  (9769884201, visited 18/7, in the Facebook tab with a Studio-shaped ask but not in CRM,
  Meta Sent pushed anyway). Ask the team where these two actually came from; if answered,
  record the resolution here next time.
- **Open question, needs Keval's input:** is "2BHK" now real sellable inventory for this
  project (in which case update the standing business-context section of the routine file),
  or is the ad just relabeling the studio product for BHK-seekers without actually fixing the
  1BHK/2BHK mismatch flagged back on 3 Jul? Don't guess in the report until this is answered.
- **Speed-to-lead (Studio campaign) is now excellent:** 17/17 leads in the last 7 days logged
  same calendar day as arrival (100%), vs 75% on 3 Jul with one 20+-hour miss. Whatever
  changed is working — keep watching it holds as volume grows, and credit the team again if
  it's still holding next run.
- **Phone-typo watch (Atul Thorat-era problem): clear.** No orphaned/typo'd CRM leads found
  in the last 14 days. The "copy-paste phone from CRM" ask from 4 Jul appears adopted.
- **Still not adopted: writing call TIME next to the date** in feedback cells. Checked the
  last 150 Facebook-tab rows for any HH:MM/am-pm pattern — zero. Keep asking.
- **"Luxury - DJ" adset**: no longer appears in any 30-day Meta breakdown (0 spend, 0 leads)
  — looks dormant/paused rather than confirmed "folded in." Not worth chasing further unless
  it reappears with spend.
- **Sheet data-quality note:** found a literal typo in the Facebook tab's Created column —
  "02/09/2525" (should almost certainly be 2025) — caused a bad date to slip into a naive
  "last 30 days" filter. Always sanity-bound parsed dates to a plausible range (e.g.
  2024-01-01 through today) before treating them as recent.
- **18-day reporting gap (4 Jul – 20 Jul):** no report was committed in that window. Root
  cause not established this run (needed cryptography/cffi packages were broken in THIS
  session's Python env — fixed with `pip install --upgrade --ignore-installed cryptography
  cffi` — worth checking if that's also why prior scheduled runs silently failed). If this
  keeps happening, escalate it explicitly rather than quietly picking up where the data left
  off.
- **Old 3/4-Jul items, not re-verified this run (too stale to trust without re-checking):**
  Sunil Bagul's outcome, and whether the ad copy was ever made explicit about "bare-shell
  studio" — the 2BHK campaign may have superseded that recommendation entirely (see open
  question above). The two prior known-bad SVD visits (Hitendra/Heena Dedhia, Naveen Suvarna)
  are STILL sitting in the last-30-day SVD window with Meta Sent conversions never retracted
  — still unresolved, 17 and 24 days on respectively.
