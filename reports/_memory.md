# Routine memory — read at the start of every run, update at the end

## Updated 2026-07-07 (run covering 6 July, after a 3-day reporting gap)

- **BIGGEST OPEN ITEM: "Divya Jyot V3 July 26 - 2BHK" campaign launched 6 July.** Cheap
  (Rs 90 CPL) but its leads never touch the CRM Event sheet (that sheet is hardwired to the
  "Studio" ad only) — no OTP verification, no timestamps, no intent tags, no speed-to-lead
  measurement possible. Ask Keval directly: does this project actually have 2BHK inventory,
  or is this campaign mistargeted? If leads keep asking for 2bhk against a studio-only
  product, that's the same mismatch as before but now with zero visibility into it. Watch
  for its first site visit — it WILL look exactly like a Dedhia-style "unverified Facebook
  visit" in the integrity check even if it's completely legitimate; don't cry wolf on it.
- **Atul Thorat (9819877789), Andre Rozario (9821266080):** both still open after 13 and 23
  days. Atul's wrong number (8198777789) is still the only entry in the sheet and got
  marked Dead off an unrelated ₹30L 1RK call. Andre still isn't in the sheet at all. Keep
  escalating until closed — this is now a repeated miss, not a one-off.
- **Ravi DU (9321110668) — CLOSED, was a false alarm.** His row exists; a dual-phone-number
  cell (`"9321110668 / 8369593191"`) broke matching. Fixed in fetch_all.py's normalize_phone
  (7 July). Real story: 5 attempts over 11 days, zero connects — one more try, not urgent.
- **Sunil Bagul — CLOSED.** Got called 3/7 ("Busy"). No longer a live miss.
- **Duplicate/re-lead entries (new pattern to watch):** Anant R (8779546600) and Shradha
  Mhamunkar (9987326564) both got fresh rows on 6/7 despite already being logged CRM leads
  from 11 June / 24 June+24 Sept 2025. Watch whether this recurs with other returning leads
  once the 2BHK campaign remarkets to the existing audience.
- **BHK-mismatch / "studio" ad-copy fix: still not landed, 3rd report flagging it.** 45% of
  matched Studio leads want a BHK unit, 0% mention "studio". If this doesn't move next run,
  say so more bluntly — recommending the same fix 3 times with zero movement is worth
  naming as a stalled recommendation, not just repeating politely.
- **Cost-per-visit trending better:** 30-day now Rs 3,120/visit at 5.56% (up from the
  corrected 4 July figure of Rs 3,813/4.4%) — clearly beating the 4.5% baseline now. Keep
  tracking whether this holds as more V3 leads mature into visits.
- **CAPI/Dedhia watch:** no new non-CRM ✅ conversions this run beyond the two already known
  (Naveen Suvarna, Hitendra Dedhia). Keep checking every run, especially once 2BHK visits
  start (see above — they'll all look like this pattern by default).
- **Reporting gap:** no dated reports exist for 4/5/6 July even though _memory.md was
  updated 4 July. If this happens again, note the gap explicitly rather than assuming
  continuity — this run had to reconstruct the last-known state from _memory.md alone.
