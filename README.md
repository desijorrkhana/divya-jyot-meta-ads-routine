# divya-jyot-meta-ads-routine

Daily Meta Ads + sales-sheet cross-reference routine, plus a live dashboard.

## Live dashboard (`dashboard.html`)

A self-contained HTML page — no external dependencies, works offline, private as
long as this repo is private. Rebuilt automatically **every 4 hours** by the
GitHub Actions workflow in `.github/workflows/dashboard.yml` (runs
`fetch_all.py` → `build_dashboard.py` → commits the fresh `dashboard.html`).

### One-time setup (required for the auto-update to work)

Add these **Actions secrets** in GitHub → repo → Settings → Secrets and
variables → Actions:

| Secret | Value |
|---|---|
| `META_AD_ACCOUNT_ID` | the ad account id (with or without `act_`) |
| `META_ADS_TOKEN` | Meta token with `ads_read` |
| `GOOGLE_SHEET_ID` | the team sheet id |
| `GOOGLE_SA_JSON` | service-account JSON (raw or base64) |
| `LEADS_SHEET_ID` | CRM Event sheet id (optional — has a default) |

Then enable the workflow under the Actions tab (first run can be triggered
manually via "Run workflow").

### Viewing it — always-on options

The dashboard contains lead names and phone numbers, so it must never be
hosted publicly. GitHub Pages is ruled out (Pages sites are public even on
private repos on the free plan). Options, easiest first:

1. **Telegram (zero setup, works on the phone):** if `TELEGRAM_BOT_TOKEN` and
   `TELEGRAM_CHAT_ID` are added as Actions secrets, every 4-hour rebuild also
   sends `dashboard.html` to the Telegram chat as a file — tap it any time,
   it opens in the browser with the full range filter working offline.
2. **Locally:** `./serve_dashboard.sh` then open
   <http://localhost:8787/dashboard.html>. Pulls the repo every 10 minutes;
   the page refreshes itself every 15, so a left-open tab stays current.
3. **A real private URL (Cloudflare Pages + Access, free):** create a
   Cloudflare account → Workers & Pages → connect this GitHub repo → build
   command: none, output dir: `/`. Then Zero Trust → Access → add an
   application covering the `*.pages.dev` domain with an email-OTP policy for
   your address. Result: `https://<name>.pages.dev/dashboard.html`, always
   on, auto-deploys on every dashboard commit, and only you can open it.

## Daily report routine

See `CLAUDE-crossref-routine.md` for the full spec. In short: `fetch_all.py`
pulls Meta insights, the CRM Event sheet (all tabs — one per lead form), the
team's Facebook/SVD tabs and the sheet's Drive revision history into
`data.json`; the analysis is written to `reports/` and `report.md`, and
`python3 fetch_all.py --send` delivers `report.md` to Telegram.
