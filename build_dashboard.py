import json

HASH = "570597212d7561b0cf5efac437ca4bd0831a08b5e0b38556521d9f5fe5aa3888"

# Shipment data with job names + categories
shipments = [
    {
        "id": "SHP-001",
        "mfg": "RENO Lighting",
        "so": "S091325",
        "po": "5303",
        "ship": "2026-06-12",
        "carrier": "CCT",
        "tracking": "MISSING",
        "exp": "2026-06-19",
        "status": "Delivered",
        "desc": "RENO fixtures — shipped Jun 12 (CCT, ETA 7 days). ETA was Jun 19; presumed delivered. Double ship-notice (Jun 9 + Jun 12).",
        "job": "Store 9 / Stock",
        "flag": "Presumed delivered (ETA+, no carrier tracking #/GIT receipt on file); confirm receipt with GIT"
    },
    {
        "id": "SHP-002",
        "mfg": "RENO Lighting",
        "so": "S088807",
        "po": "5251",
        "ship": "2026-06-16",
        "carrier": "Western Canada Express",
        "tracking": "WC991057",
        "exp": "2026-06-22",
        "status": "Delivered",
        "desc": "THE VUE order (Type L/M/Q/S, R31101/R31041) — shipped Jun 16 (WCE, tracking WC991057, ETA 7-9). GIT confirmed receipt Jun 22: 'WCE delivered three pallets from Reno Lighting.' Final partial for S088807.",
        "job": "THE VUE",
        "flag": ""
    },
    {
        "id": "SHP-003",
        "mfg": "RENO Lighting",
        "so": "S094971",
        "po": "5389",
        "ship": "2026-06-11",
        "carrier": "Vitran",
        "tracking": "MISSING",
        "exp": "2026-06-26",
        "status": "In Transit",
        "desc": "777 Hornby — RENO confirmed 'SO# S094971 / PO# 5389 has been shipped!' (Jun 11, Vitran, ETA 6-8). Earlier misrouted to Powell River, rerouted ~Jun 18 with new tracking. ETA ~Jun 26.",
        "job": "777 Hornby",
        "flag": "Was misrouted to Powell River (rerouted ~Jun 18); confirm new tracking # and corrected ETA with RENO"
    },
    {
        "id": "SHP-004",
        "mfg": "Kuzco",
        "so": "C-ORD00067537",
        "po": "5299",
        "ship": "2026-06-10",
        "carrier": "K&H LTL",
        "tracking": "4831380",
        "exp": "2026-06-17",
        "status": "Delivered",
        "desc": "PARK PLACE LOBBY — custom Kuzco PD88160-BK (via Nuvo Sales), shipped Jun 10 (K&H LTL, tracking 4831380). ETA Jun 17 elapsed; presumed delivered.",
        "job": "PARK PLACE LOBBY",
        "flag": ""
    },
    {
        "id": "SHP-005",
        "mfg": "CNA Lighting",
        "so": "",
        "po": "",
        "ship": "2026-06-10",
        "carrier": "",
        "tracking": "MISSING",
        "exp": "",
        "status": "Order Placed",
        "desc": "CNA bankcard order #061026 placed Jun 10 ($1,630.91). No carrier shipment notice; CNA orders are typically local pickup. CNA invoices Jun 12 suggest it may already be fulfilled.",
        "job": "Canucks - Rogers Arena",
        "flag": "Order placed 15 days ago, no ship/receipt confirmation — likely picked up locally; confirm and close"
    },
    {
        "id": "SHP-006",
        "mfg": "RENO Lighting",
        "so": "S089014",
        "po": "5266",
        "ship": "2026-06-17",
        "carrier": "Western Canada Express",
        "tracking": "",
        "exp": "2026-06-17",
        "status": "Delivered",
        "desc": "GIT receipt Jun 17 — WCE delivered Reno pallet (Ravenna 7\" SM). Labeled MARCON - RAVENNA at warehouse.",
        "job": "MARCON - RAVENNA",
        "flag": ""
    },
    {
        "id": "SHP-007",
        "mfg": "RENO Lighting",
        "so": "",
        "po": "",
        "ship": "2026-06-15",
        "carrier": "Western Canada Express",
        "tracking": "",
        "exp": "2026-06-15",
        "status": "Delivered",
        "desc": "GIT receipt Jun 15 — 8ft pallet from Reno delivered to warehouse.",
        "job": "Unspecified (Reno)",
        "flag": "No SO/PO on GIT receipt — tag at warehouse to identify job"
    },
    {
        "id": "SHP-008",
        "mfg": "RENO Lighting",
        "so": "",
        "po": "",
        "ship": "2026-06-01",
        "carrier": "Western Canada Express",
        "tracking": "",
        "exp": "2026-06-01",
        "status": "Delivered",
        "desc": "GIT receipt Jun 1 — WCE delivered Reno pallet (Ark Halo series). 48x40x85\", 295 lbs. Picked up by Urban Valley.",
        "job": "Unspecified (Reno Ark Halo)",
        "flag": "No SO/PO on GIT receipt — identify job"
    },
    {
        "id": "SHP-009",
        "mfg": "RENO Lighting",
        "so": "S094264",
        "po": "5367",
        "ship": "2026-05-25",
        "carrier": "Western Canada Express",
        "tracking": "1252480110",
        "exp": "2026-06-03",
        "status": "Delivered",
        "desc": "BAPTIST HOUSING SAMPLES — shipped May 25 (WCE, ETA 8-9); tracking 1252480110. ETA window elapsed.",
        "job": "BAPTIST HOUSING SAMPLES",
        "flag": ""
    },
    {
        "id": "SHP-010",
        "mfg": "RENO Lighting",
        "so": "S094536",
        "po": "5374",
        "ship": "2026-05-29",
        "carrier": "Purolator (Small Parcel)",
        "tracking": "MISSING",
        "exp": "2026-06-05",
        "status": "Delivered",
        "desc": "BCNPH M&C Samples — shipped May 29 (Purolator, ETA 5-7). ETA window elapsed, presumed delivered.",
        "job": "BCNPH M&C Samples",
        "flag": ""
    },
    {
        "id": "SHP-011",
        "mfg": "RENO Lighting",
        "so": "S094828",
        "po": "5381",
        "ship": "2026-06-05",
        "carrier": "Purolator (Small Parcel)",
        "tracking": "MISSING",
        "exp": "2026-06-11",
        "status": "Delivered",
        "desc": "SOF 7823 — shipped Jun 5 (Purolator, ETA 5-6). ETA window elapsed, presumed delivered.",
        "job": "SOF 7823",
        "flag": ""
    },
    {
        "id": "SHP-012",
        "mfg": "RENO Lighting",
        "so": "S094832",
        "po": "5383",
        "ship": "2026-06-09",
        "carrier": "UPS",
        "tracking": "MISSING",
        "exp": "2026-06-15",
        "status": "Delivered",
        "desc": "SHAPE UPTOWN 8\" POTS — shipped Jun 9 (UPS, ETA 4-6). ETA window elapsed.",
        "job": "SHAPE UPTOWN 8\" POTS",
        "flag": ""
    },
    {
        "id": "SHP-013",
        "mfg": "Kuzco",
        "so": "C-ORD00075625",
        "po": "4086-R",
        "ship": "2026-06-11",
        "carrier": "LoomisGround",
        "tracking": "LSHP49591980",
        "exp": "2026-06-12",
        "status": "Delivered",
        "desc": "Kuzco shipment 4086-R — shipped Jun 11, est. delivery Jun 12. Warranty/replacement (-R; matching credit C-CRN00013995 + invoice C-INV00101663, $180.18).",
        "job": "Kuzco Warranty / Replacement",
        "flag": "Job not confirmed — verify which project this replacement belongs to"
    },
    {
        "id": "SHP-014",
        "mfg": "RENO Lighting",
        "so": "S095362",
        "po": "5399",
        "ship": "",
        "carrier": "",
        "tracking": "MISSING",
        "exp": "",
        "status": "Order Placed",
        "desc": "MARCON RAVENNA 7\" SM — PO issued to RENO Jun 17; order confirmation received. Not yet shipped.",
        "job": "MARCON RAVENNA 7\" SM",
        "flag": "Order placed/confirmed Jun 17 — 8 days, no ship notice yet; follow up with RENO for ETA"
    },
    {
        "id": "SHP-015",
        "mfg": "RENO Lighting",
        "so": "",
        "po": "",
        "ship": "2026-06-22",
        "carrier": "Storm Electric (internal drop-off)",
        "tracking": "",
        "exp": "2026-06-22",
        "status": "Delivered",
        "desc": "GIT receipt Jun 22 — Storm Electric dropped off (2) 8ft Reno boxes at the warehouse (same day GIT received the THE VUE WCE pallets).",
        "job": "Unspecified (Reno 8ft via Storm)",
        "flag": "No SO/PO on GIT receipt — tag at warehouse to identify job"
    },
    {
        "id": "SHP-016",
        "mfg": "RENO Lighting",
        "so": "S095544",
        "po": "5405",
        "ship": "2026-06-25",
        "carrier": "RENO (carrier TBD)",
        "tracking": "MISSING",
        "exp": "2026-07-02",
        "status": "In Transit",
        "desc": "RENO SO# S095544 / PO# 5405 — confirmed Jun 23; RENO invoice issued Jun 25 (RENO invoices on shipment), so presumed shipped Jun 25. Carrier/tracking not yet provided; ETA ~6-8 days.",
        "job": "Unspecified (RENO PO 5405)",
        "flag": "Invoiced/shipped Jun 25 but no carrier or tracking # on file — request tracking + ETA from RENO; identify job"
    },
    {
        "id": "SHP-017",
        "mfg": "RENO Lighting",
        "so": "S095542",
        "po": "5393",
        "ship": "2026-06-25",
        "carrier": "RENO (carrier TBD)",
        "tracking": "MISSING",
        "exp": "2026-07-02",
        "status": "In Transit",
        "desc": "RENO SO# S095542 / PO# 5393 — confirmed Jun 23; invoice issued Jun 25, partial presumed shipped Jun 25. PARTIAL: only 62x R39208 in stock shipped; remainder backordered to 2026-07-15.",
        "job": "Unspecified (RENO PO 5393)",
        "flag": "Partial shipment (62x R39208); balance backordered to Jul 15, 2026. No carrier/tracking on file — request from RENO; identify job"
    },
    {
        "id": "SHP-018",
        "mfg": "Advant Lighting",
        "so": "",
        "po": "5404",
        "ship": "2026-06-23",
        "carrier": "Green Image Tech (local)",
        "tracking": "",
        "exp": "2026-06-23",
        "status": "Delivered",
        "desc": "MHOND CEILING ADVANT — Hazel 275 E 14th Ave. PO 5404 to Green Image Tech (Advant fixtures). GIT confirmed 'ready for pickup. Four boxes.' Jun 23 — goods at GIT warehouse.",
        "job": "Hazel 275 E 14th Ave (Mhond)",
        "flag": ""
    },
    {
        "id": "SHP-019",
        "mfg": "Ortech (via GIT)",
        "so": "",
        "po": "",
        "ship": "2026-06-23",
        "carrier": "Green Image Tech (receipt)",
        "tracking": "",
        "exp": "2026-06-23",
        "status": "Delivered",
        "desc": "GIT receipt Jun 23 — 'a pallet of Ortech products delivered' (packing list attached). Likely Hopehill/Baptist Ortech pots.",
        "job": "Hopehill / Baptist (Ortech)",
        "flag": "Ortech not on approved mfg list — included as GIT warehouse receipt; confirm job from packing slip"
    },
    {
        "id": "SHP-020",
        "mfg": "CSC LED",
        "so": "",
        "po": "",
        "ship": "2026-06-22",
        "carrier": "Local pickup (Burnaby)",
        "tracking": "",
        "exp": "2026-06-22",
        "status": "Delivered",
        "desc": "CSC LED 'Storm 4' Vapour Tight, 3 pcs' — order processed Jun 22, CSC confirmed ready for local pickup; invoice 4090877 issued Jun 23. Andrew arranging pickup.",
        "job": "Storm Electric",
        "flag": ""
    },
    {
        "id": "SHP-021",
        "mfg": "EiKO",
        "so": "SO188866",
        "po": "5344",
        "ship": "2026-06-24",
        "carrier": "Day & Ross",
        "tracking": "A11182767-0001 / -0002",
        "exp": "2026-06-29",
        "status": "In Transit",
        "desc": "EiKO PO 5344 / SO188866 (ordered Apr 29) shipped Jun 24 via Day & Ross (tracking A11182767-0001/-0002). Ship-to: Fully Loaded Services / Richmond Storage Ltd, Richmond BC. 50% deposit paid via EFT Jun 23.",
        "job": "Unspecified (EiKO PO 5344)",
        "flag": "EiKO not on approved mfg list — included as confirmed inbound PO shipment with tracking. ETA estimated (Day & Ross LTL); confirm delivery + identify job"
    },
    {
        "id": "SHP-022",
        "mfg": "Onlumi (Shenzhen)",
        "so": "",
        "po": "",
        "ship": "2026-06-25",
        "carrier": "DHL",
        "tracking": "7754899854",
        "exp": "2026-07-02",
        "status": "In Transit",
        "desc": "Onlumi (Shenzhen) LED strip/connector order — payment confirmed via FX/wire Jun 24; goods sent by DHL Jun 25, tracking 7754899854 (PL + CI attached).",
        "job": "Unspecified (Onlumi strip/connectors)",
        "flag": "Onlumi not on approved mfg list — included as confirmed inbound DHL shipment. International transit; confirm ETA + assign to job/stock"
    }
]

# Compute category
for s in shipments:
    s["category"] = "Delivered" if s["status"] == "Delivered" else "Active"

# Counts
total = len(shipments)
active = sum(1 for s in shipments if s["category"] == "Active")
delivered = sum(1 for s in shipments if s["category"] == "Delivered")
overdue = sum(1 for s in shipments if s["status"] == "Overdue")
missing_tracking = sum(1 for s in shipments if s["tracking"] == "MISSING")
order_placed = sum(1 for s in shipments if s["status"] == "Order Placed")

# Unique jobs sorted
jobs = sorted(set(s["job"] for s in shipments))

shipments_json = json.dumps(shipments)
jobs_json = json.dumps(jobs)

HTML = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>LTS Canada – Incoming Shipments Dashboard</title>
<style>
  :root {
    --bg: #0f172a; --card: #1e293b; --card-2: #334155; --text: #e2e8f0; --muted: #94a3b8;
    --accent: #3b82f6; --green: #10b981; --amber: #f59e0b; --red: #ef4444; --blue: #3b82f6;
    --purple: #a855f7; --border: #334155;
  }
  * { box-sizing: border-box; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; background: var(--bg); color: var(--text); line-height: 1.5; }
  .container { max-width: 1500px; margin: 0 auto; padding: 24px; }
  header { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 24px; padding-bottom: 16px; border-bottom: 1px solid var(--border); flex-wrap: wrap; gap: 16px; }
  h1 { font-size: 24px; margin: 0; }
  .subtitle { color: var(--muted); font-size: 14px; margin-top: 4px; }

  .badge { display: inline-block; padding: 4px 10px; border-radius: 12px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; white-space: nowrap; }
  .badge-delivered { background: rgba(16,185,129,0.15); color: var(--green); border: 1px solid var(--green); }
  .badge-transit { background: rgba(59,130,246,0.15); color: var(--blue); border: 1px solid var(--blue); }
  .badge-overdue { background: rgba(239,68,68,0.15); color: var(--red); border: 1px solid var(--red); }
  .badge-due { background: rgba(245,158,11,0.15); color: var(--amber); border: 1px solid var(--amber); }
  .badge-pending { background: rgba(168,85,247,0.15); color: var(--purple); border: 1px solid var(--purple); }

  .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-bottom: 24px; }
  .stat-card { background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 16px; }
  .stat-card .label { color: var(--muted); font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
  .stat-card .value { font-size: 28px; font-weight: 700; margin-top: 6px; }
  .stat-card.alert .value { color: var(--red); }
  .stat-card.warn .value { color: var(--amber); }
  .stat-card.ok .value { color: var(--green); }
  .stat-card.info .value { color: var(--blue); }
  .stat-card.pending .value { color: var(--purple); }

  .flags-section { background: var(--card); border: 1px solid var(--border); border-left: 4px solid var(--amber); border-radius: 8px; padding: 16px 20px; margin-bottom: 24px; }
  .flags-section h2 { margin: 0 0 10px 0; font-size: 16px; color: var(--amber); }
  .flag-item { padding: 8px 0; border-bottom: 1px dashed var(--border); font-size: 14px; }
  .flag-item:last-child { border-bottom: none; }
  .flag-item .ship-id { font-weight: 600; color: var(--text); }

  /* Category tabs */
  .tabs { display: flex; gap: 4px; margin-bottom: 16px; background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 4px; width: fit-content; }
  .tab { background: transparent; color: var(--muted); border: none; padding: 10px 20px; border-radius: 6px; cursor: pointer; font-size: 14px; font-weight: 600; font-family: inherit; transition: all 0.15s; }
  .tab:hover { color: var(--text); }
  .tab.active { background: var(--accent); color: white; }
  .tab .count { opacity: 0.7; font-weight: 400; margin-left: 4px; }

  /* Secondary filters */
  .filters-row { display: flex; gap: 12px; align-items: center; flex-wrap: wrap; margin-bottom: 16px; background: var(--card); border: 1px solid var(--border); border-radius: 8px; padding: 12px 16px; }
  .filter-group { display: flex; align-items: center; gap: 8px; }
  .filter-group label { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
  .filter-group select, .filter-group input[type="date"] {
    background: var(--card-2); color: var(--text); border: 1px solid var(--border);
    border-radius: 6px; padding: 6px 10px; font-size: 13px; font-family: inherit;
  }
  .filter-group select:focus, .filter-group input:focus { outline: none; border-color: var(--accent); }
  .clear-btn { background: transparent; color: var(--muted); border: 1px solid var(--border); padding: 6px 14px; border-radius: 6px; cursor: pointer; font-size: 12px; font-family: inherit; }
  .clear-btn:hover { color: var(--text); border-color: var(--text); }
  .results-count { margin-left: auto; color: var(--muted); font-size: 13px; }

  .table-wrap { background: var(--card); border: 1px solid var(--border); border-radius: 8px; overflow-x: auto; }
  table { width: 100%; border-collapse: collapse; font-size: 13px; }
  thead { background: var(--card-2); }
  th { text-align: left; padding: 12px 14px; font-weight: 600; color: var(--muted); font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 1px solid var(--border); white-space: nowrap; }
  td { padding: 12px 14px; border-bottom: 1px solid var(--border); vertical-align: top; }
  tr:hover td { background: rgba(255,255,255,0.02); }
  tr:last-child td { border-bottom: none; }
  .ship-id { font-family: monospace; color: var(--muted); font-size: 12px; }
  .mfg { font-weight: 600; }
  .job { font-weight: 600; color: var(--accent); }
  .job.unspec { color: var(--muted); font-style: italic; font-weight: 400; }
  .desc { color: var(--muted); font-size: 12px; }
  .tracking { font-family: monospace; font-size: 12px; }
  .tracking.missing { color: var(--red); }
  .flag-cell { color: var(--amber); font-size: 12px; max-width: 240px; }
  .empty { padding: 40px; text-align: center; color: var(--muted); font-size: 14px; }

  footer { margin-top: 24px; padding-top: 16px; border-top: 1px solid var(--border); color: var(--muted); font-size: 12px; text-align: center; }

  /* Password gate */
  #password-gate { position: fixed; inset: 0; background: var(--bg); display: flex; align-items: center; justify-content: center; z-index: 9999; }
  #password-gate .gate-box { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 32px; width: 90%; max-width: 420px; text-align: center; }
  #password-gate h2 { margin: 0 0 8px 0; font-size: 20px; color: var(--text); }
  #password-gate .hint { color: var(--muted); font-size: 13px; margin-bottom: 20px; }
  #password-gate input { width: 100%; padding: 12px 14px; background: var(--card-2); border: 1px solid var(--border); border-radius: 6px; color: var(--text); font-size: 15px; font-family: inherit; box-sizing: border-box; }
  #password-gate input:focus { outline: none; border-color: var(--accent); }
  #password-gate button { width: 100%; margin-top: 12px; padding: 12px; background: var(--accent); color: white; border: none; border-radius: 6px; font-size: 15px; font-weight: 600; cursor: pointer; font-family: inherit; }
  #password-gate button:hover { opacity: 0.9; }
  #password-gate .error { color: var(--red); font-size: 13px; margin-top: 12px; min-height: 18px; }
  body.gate-locked .container { display: none; }
</style>
</head>
<body class="gate-locked">

<div id="password-gate">
  <div class="gate-box">
    <h2>LTS Shipments Dashboard</h2>
    <div class="hint">Internal use only. Enter the team password to continue.</div>
    <form id="gate-form" autocomplete="off">
      <input type="password" id="gate-input" placeholder="Password" autofocus />
      <button type="submit">Unlock</button>
      <div class="error" id="gate-error"></div>
    </form>
  </div>
</div>

<div class="container">
  <header>
    <div>
      <h1>Incoming Shipments — LTS Canada</h1>
      <div class="subtitle">Last updated __LAST_UPDATED__ · Filtered to approved manufacturer list</div>
    </div>
    <div><span class="badge badge-delivered">28 manufacturers monitored</span></div>
  </header>

  <div class="stats">
    <div class="stat-card info"><div class="label">Total Tracked</div><div class="value">__TOTAL__</div></div>
    <div class="stat-card warn"><div class="label">Active</div><div class="value">__ACTIVE__</div></div>
    <div class="stat-card alert"><div class="label">Overdue</div><div class="value">__OVERDUE__</div></div>
    <div class="stat-card ok"><div class="label">Delivered</div><div class="value">__DELIVERED__</div></div>
    <div class="stat-card pending"><div class="label">Order Placed</div><div class="value">__ORDER_PLACED__</div></div>
    <div class="stat-card warn"><div class="label">Missing Tracking#</div><div class="value">__MISSING_TRACKING__</div></div>
  </div>

  <div class="flags-section">
    <h2>⚠ Flags &amp; Exceptions</h2>
    <div id="flags-list"></div>
  </div>

  <div class="tabs">
    <button class="tab active" data-tab="Active">Active <span class="count" id="cnt-active">(__ACTIVE__)</span></button>
    <button class="tab" data-tab="Delivered">Delivered <span class="count" id="cnt-delivered">(__DELIVERED__)</span></button>
    <button class="tab" data-tab="All">All <span class="count" id="cnt-all">(__TOTAL__)</span></button>
  </div>

  <div class="filters-row">
    <div class="filter-group">
      <label>Job:</label>
      <select id="filter-job">
        <option value="">All jobs</option>
      </select>
    </div>
    <div class="filter-group">
      <label>From:</label>
      <input type="date" id="filter-from" />
    </div>
    <div class="filter-group">
      <label>To:</label>
      <input type="date" id="filter-to" />
    </div>
    <button class="clear-btn" id="clear-filters">Clear filters</button>
    <div class="results-count" id="results-count"></div>
  </div>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Ship ID</th><th>Job</th><th>Manufacturer / Item</th><th>PO / SO</th><th>Carrier</th>
          <th>Tracking #</th><th>Ship Date</th><th>Expected</th><th>Status</th><th>Flag</th>
        </tr>
      </thead>
      <tbody id="ship-tbody"></tbody>
    </table>
  </div>

  <footer>
    Source: Gmail (jeff@ltscanada.com) · Filtered to approved manufacturer list · Refreshed daily at 7:02 AM · Live URL: https://ltsjeff.github.io/lts-shipments/
  </footer>
</div>

<script>
const shipments = __SHIPMENTS_JSON__;
const jobs = __JOBS_JSON__;

function badgeFor(status) {
  return { "Delivered":"badge-delivered","In Transit":"badge-transit","Overdue":"badge-overdue","Due Today":"badge-due","Order Placed":"badge-pending" }[status] || "badge-transit";
}

let currentTab = "Active";
let filterJob = "";
let filterFrom = "";
let filterTo = "";

function applyFilters() {
  let list = shipments;
  if (currentTab !== "All") list = list.filter(s => s.category === currentTab);
  if (filterJob) list = list.filter(s => s.job === filterJob);
  if (filterFrom) list = list.filter(s => s.ship !== "Pending" && s.ship >= filterFrom);
  if (filterTo) list = list.filter(s => s.ship !== "Pending" && s.ship <= filterTo);
  return list;
}

function render() {
  const tbody = document.getElementById("ship-tbody");
  const list = applyFilters();
  tbody.innerHTML = "";
  document.getElementById("results-count").textContent = list.length + " shipment" + (list.length === 1 ? "" : "s") + " shown";
  if (list.length === 0) {
    tbody.innerHTML = '<tr><td colspan="10" class="empty">No shipments match these filters.</td></tr>';
    return;
  }
  list.forEach(s => {
    const trClass = s.tracking === "MISSING" ? "missing" : "";
    const jobClass = s.job === "Unspecified" ? "job unspec" : "job";
    tbody.insertAdjacentHTML("beforeend", `
      <tr>
        <td><span class="ship-id">${s.id}</span></td>
        <td><span class="${jobClass}">${s.job}</span></td>
        <td><div class="mfg">${s.mfg}</div><div class="desc">${s.desc}</div></td>
        <td>PO ${s.po}<br/><span class="desc">SO ${s.so}</span></td>
        <td>${s.carrier}</td>
        <td class="tracking ${trClass}">${s.tracking}</td>
        <td>${s.ship}</td>
        <td>${s.exp}</td>
        <td><span class="badge ${badgeFor(s.status)}">${s.status}</span></td>
        <td class="flag-cell">${s.flag || "—"}</td>
      </tr>
    `);
  });
}

// Populate job dropdown
const sel = document.getElementById("filter-job");
jobs.forEach(j => {
  const opt = document.createElement("option");
  opt.value = j; opt.textContent = j;
  sel.appendChild(opt);
});

// Tab switching
document.querySelectorAll(".tab").forEach(t => {
  t.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach(x => x.classList.remove("active"));
    t.classList.add("active");
    currentTab = t.dataset.tab;
    render();
  });
});

// Filter listeners
document.getElementById("filter-job").addEventListener("change", e => { filterJob = e.target.value; render(); });
document.getElementById("filter-from").addEventListener("change", e => { filterFrom = e.target.value; render(); });
document.getElementById("filter-to").addEventListener("change", e => { filterTo = e.target.value; render(); });

document.getElementById("clear-filters").addEventListener("click", () => {
  filterJob = filterFrom = filterTo = "";
  document.getElementById("filter-job").value = "";
  document.getElementById("filter-from").value = "";
  document.getElementById("filter-to").value = "";
  render();
});

// Render flags
const flaggedShipments = shipments.filter(s => s.flag);
const flagsList = document.getElementById("flags-list");
if (flaggedShipments.length === 0) {
  flagsList.innerHTML = '<div class="flag-item" style="color: var(--muted);">No flags — everything looks healthy.</div>';
} else {
  flaggedShipments.forEach(s => {
    flagsList.insertAdjacentHTML("beforeend",
      `<div class="flag-item"><span class="ship-id">${s.id} · ${s.mfg} ${s.po !== "N/A" ? "PO " + s.po : ""} · ${s.job}</span> — ${s.flag}</div>`);
  });
}

render();
</script>

<script>
(async function() {
  const HASH = "''' + HASH + '''";
  const STORAGE_KEY = "ltsShipmentsUnlocked";
  async function sha256(text) {
    const buf = new TextEncoder().encode(text);
    const hash = await crypto.subtle.digest("SHA-256", buf);
    return Array.from(new Uint8Array(hash)).map(b => b.toString(16).padStart(2, "0")).join("");
  }
  function unlock() {
    document.body.classList.remove("gate-locked");
    const gate = document.getElementById("password-gate");
    if (gate) gate.remove();
  }
  if (localStorage.getItem(STORAGE_KEY) === HASH) { unlock(); return; }
  const form = document.getElementById("gate-form");
  const input = document.getElementById("gate-input");
  const err = document.getElementById("gate-error");
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const h = await sha256(input.value);
    if (h === HASH) { localStorage.setItem(STORAGE_KEY, HASH); unlock(); }
    else { err.textContent = "Incorrect password. Try again."; input.select(); }
  });
})();
</script>
</body>
</html>
'''

# Fill in placeholders
HTML = HTML.replace("__LAST_UPDATED__", "Jun 25, 2026")
HTML = HTML.replace("__TOTAL__", str(total))
HTML = HTML.replace("__ACTIVE__", str(active))
HTML = HTML.replace("__DELIVERED__", str(delivered))
HTML = HTML.replace("__OVERDUE__", str(overdue))
HTML = HTML.replace("__ORDER_PLACED__", str(order_placed))
HTML = HTML.replace("__MISSING_TRACKING__", str(missing_tracking))
HTML = HTML.replace("__SHIPMENTS_JSON__", shipments_json)
HTML = HTML.replace("__JOBS_JSON__", jobs_json)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML)

print("Built dashboard. Stats:")
print(f"  Total: {total}, Active: {active}, Delivered: {delivered}, Overdue: {overdue}")
print(f"  Jobs: {jobs}")
print(f"  Size: {len(HTML)} chars")
