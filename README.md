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

### Viewing it

- **Locally (recommended):** `./serve_dashboard.sh` then open
  <http://localhost:8787/dashboard.html>. The script pulls the repo every 10
  minutes and the page refreshes itself every 15, so a left-open tab stays
  current with each 4-hour rebuild.
- **Anywhere:** open the repo on GitHub → `dashboard.html` → Raw, or just pull
  and double-click the file. (GitHub Pages is NOT used — Pages sites are public
  even on private repos on the free plan.)

## Daily report routine

See `CLAUDE-crossref-routine.md` for the full spec. In short: `fetch_all.py`
pulls Meta insights, the CRM Event sheet (all tabs — one per lead form), the
team's Facebook/SVD tabs and the sheet's Drive revision history into
`data.json`; the analysis is written to `reports/` and `report.md`, and
`python3 fetch_all.py --send` delivers `report.md` to Telegram.
