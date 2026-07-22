# divya-jyot-meta-ads-routine

Daily Meta Ads + sales-sheet cross-reference routine, plus a live dashboard.

## Live dashboard (`dashboard.html`)

A self-contained HTML page — no external dependencies, works offline, private as
long as this repo is private. Rebuilt automatically **every hour, 9AM–7PM IST** by the
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
   `TELEGRAM_CHAT_ID` are added as Actions secrets, every hourly rebuild also
   sends `dashboard.html` to the Telegram chat as a file — tap it any time,
   it opens in the browser with the full range filter working offline.
2. **Locally:** `./serve_dashboard.sh` then open
   <http://localhost:8787/dashboard.html>. Pulls the repo every 10 minutes;
   the page refreshes itself every 15, so a left-open tab stays current.
3. **A real private URL (Cloudflare Pages + Access, free) — the chosen setup:**
   the repo is already prepared (`index.html` redirects the bare URL to the
   dashboard; `_headers` disables caching so every visit shows the newest
   build). One-time setup, ~15 minutes:

   1. Sign up at <https://dash.cloudflare.com> (free plan is enough).
   2. **Workers & Pages → Create → Pages → Connect to Git** → authorize
      GitHub → pick this repo (grant it access to the private repo).
   3. Settings: production branch **`main`**, build command **(leave
      empty)**, build output directory **`/`** → Deploy. You'll get
      `https://<project>.pages.dev`.
   4. **Before sharing/bookmarking, lock it down** — until this step the URL
      is public to anyone who guesses it: in the Pages project → **Settings →
      Enable Access policy** (protects preview URLs), then in **Zero Trust →
      Access → Applications** add/edit the application so its domain covers
      `<project>.pages.dev` itself, with a policy of **Include → Emails →
      your email**. Login method: One-time PIN (Cloudflare emails a code).
   5. Open `https://<project>.pages.dev` on the phone, log in once with the
      emailed PIN, bookmark it. Every push to `main` (including the 4-hour
      cron commits) redeploys automatically in under a minute.

## Daily report routine

See `CLAUDE-crossref-routine.md` for the full spec. In short: `fetch_all.py`
pulls Meta insights, the CRM Event sheet (all tabs — one per lead form), the
team's Facebook/SVD tabs and the sheet's Drive revision history into
`data.json`; the analysis is written to `reports/` and `report.md`, and
`python3 fetch_all.py --send` delivers `report.md` to Telegram.
