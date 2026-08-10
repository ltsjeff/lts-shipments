import json

HASH = "570597212d7561b0cf5efac437ca4bd0831a08b5e0b38556521d9f5fe5aa3888"

# Shipment data with job names + categories
shipments = [
    {"id": "SHP-001", "mfg": "RENO Lighting", "so": "S091325", "po": "5303", "ship": "2026-06-12", "carrier": "CCT", "tracking": "MISSING", "exp": "2026-06-19", "status": "Delivered", "desc": "RENO fixtures — shipped Jun 12 (CCT, ETA 7 days). ETA elapsed; presumed delivered. Note: SO S091325/PO 5303 is a recurring stock SO — reshipped again Jun 26 (see SHP-023).", "job": "Store 9 / Stock", "flag": "Presumed delivered (ETA+, no carrier tracking #/GIT receipt); confirm with GIT"},
    {"id": "SHP-002", "mfg": "RENO Lighting", "so": "S088807", "po": "5251", "ship": "2026-06-16", "carrier": "Western Canada Express", "tracking": "WC991057", "exp": "2026-06-22", "status": "Delivered", "desc": "THE VUE order (Type L/M/Q/S, R31101/R31041) — shipped Jun 16 (WCE, ETA 7-9). GIT confirmed receipt Jun 22: 'WCE delivered three pallets from Reno.' Final partial for S088807.", "job": "THE VUE", "flag": ""},
    {"id": "SHP-003", "mfg": "RENO Lighting", "so": "S094971", "po": "5389", "ship": "2026-06-11", "carrier": "Vitran", "tracking": "MISSING", "exp": "2026-06-26", "status": "Delivered", "desc": "777 Hornby — RENO 'S094971 / PO 5389 shipped' (Jun 11, Vitran). Earlier misrouted to Powell River, rerouted ~Jun 18. GIT confirmed receipt Jun 26: 'Vitran delivered a pallet from Reno.' DELIVERED.", "job": "777 Hornby", "flag": ""},
    {"id": "SHP-004", "mfg": "Kuzco", "so": "C-ORD00067537", "po": "5299", "ship": "2026-06-10", "carrier": "K&H LTL", "tracking": "4831380", "exp": "2026-06-17", "status": "Delivered", "desc": "PARK PLACE LOBBY — custom Kuzco PD88160-BK (via Nuvo Sales), shipped Jun 10 (K&H LTL, tracking 4831380). ETA elapsed; delivered.", "job": "PARK PLACE LOBBY", "flag": ""},
    {"id": "SHP-005", "mfg": "CNA Lighting", "so": "", "po": "", "ship": "2026-06-10", "carrier": "Local pickup (Burnaby)", "tracking": "", "exp": "2026-06-12", "status": "Delivered", "desc": "CNA bankcard order #061026 placed Jun 10 ($1,630.91); CNA invoice 51763 issued. Local pickup order — presumed picked up/closed.", "job": "Canucks - Rogers Arena", "flag": ""},
    {"id": "SHP-006", "mfg": "RENO Lighting", "so": "S089014", "po": "5266", "ship": "2026-06-17", "carrier": "Western Canada Express", "tracking": "", "exp": "2026-06-17", "status": "Delivered", "desc": "GIT receipt Jun 17 — WCE delivered Reno pallet (Ravenna 7\" SM). Labeled MARCON - RAVENNA at warehouse.", "job": "MARCON - RAVENNA", "flag": ""},
    {"id": "SHP-007", "mfg": "RENO Lighting", "so": "", "po": "", "ship": "2026-06-15", "carrier": "Western Canada Express", "tracking": "", "exp": "2026-06-15", "status": "Delivered", "desc": "GIT receipt Jun 15 — 8ft pallet from Reno delivered to warehouse.", "job": "Unspecified (Reno)", "flag": "No SO/PO on GIT receipt — tag at warehouse to identify job"},
    {"id": "SHP-008", "mfg": "RENO Lighting", "so": "", "po": "", "ship": "2026-06-01", "carrier": "Western Canada Express", "tracking": "", "exp": "2026-06-01", "status": "Delivered", "desc": "GIT receipt Jun 1 — WCE delivered Reno pallet (Ark Halo series). 48x40x85\", 295 lbs. Picked up by Urban Valley.", "job": "Unspecified (Reno Ark Halo)", "flag": "No SO/PO on GIT receipt — identify job"},
    {"id": "SHP-009", "mfg": "RENO Lighting", "so": "S094264", "po": "5367", "ship": "2026-05-25", "carrier": "Western Canada Express", "tracking": "1252480110", "exp": "2026-06-03", "status": "Delivered", "desc": "BAPTIST HOUSING SAMPLES — shipped May 25 (WCE, ETA 8-9); tracking 1252480110. ETA elapsed.", "job": "BAPTIST HOUSING SAMPLES", "flag": ""},
    {"id": "SHP-010", "mfg": "RENO Lighting", "so": "S094536", "po": "5374", "ship": "2026-05-29", "carrier": "Purolator (Small Parcel)", "tracking": "MISSING", "exp": "2026-06-05", "status": "Delivered", "desc": "BCNPH M&C Samples — shipped May 29 (Purolator, ETA 5-7). Delivered.", "job": "BCNPH M&C Samples", "flag": ""},
    {"id": "SHP-011", "mfg": "RENO Lighting", "so": "S094828", "po": "5381", "ship": "2026-06-05", "carrier": "Purolator (Small Parcel)", "tracking": "MISSING", "exp": "2026-06-11", "status": "Delivered", "desc": "SOF 7823 — shipped Jun 5 (Purolator, ETA 5-6). Delivered.", "job": "SOF 7823", "flag": ""},
    {"id": "SHP-012", "mfg": "RENO Lighting", "so": "S094832", "po": "5383", "ship": "2026-06-09", "carrier": "UPS", "tracking": "MISSING", "exp": "2026-06-15", "status": "Delivered", "desc": "SHAPE UPTOWN 8\" POTS — shipped Jun 9 (UPS, ETA 4-6). Delivered.", "job": "SHAPE UPTOWN 8\" POTS", "flag": ""},
    {"id": "SHP-013", "mfg": "Kuzco", "so": "C-ORD00075625", "po": "4086-R", "ship": "2026-06-11", "carrier": "LoomisGround", "tracking": "LSHP49591980", "exp": "2026-06-12", "status": "Delivered", "desc": "Kuzco shipment 4086-R — shipped Jun 11, est. delivery Jun 12. Warranty/replacement.", "job": "Kuzco Warranty / Replacement", "flag": "Job not confirmed — verify which project this replacement belongs to"},
    {"id": "SHP-014", "mfg": "RENO Lighting", "so": "S095362", "po": "5399", "ship": "", "carrier": "", "tracking": "MISSING", "exp": "", "status": "Order Placed", "desc": "MARCON RAVENNA 7\" SM — PO issued to RENO Jun 17; order confirmed. No ship notice yet as of Jul 13 (26 days).", "job": "MARCON RAVENNA 7\" SM", "flag": "STALE: order confirmed Jun 17 — 42 days, no ship notice; escalate with RENO for ETA"},
    {"id": "SHP-015", "mfg": "RENO Lighting", "so": "", "po": "", "ship": "2026-06-22", "carrier": "Storm Electric (internal drop-off)", "tracking": "", "exp": "2026-06-22", "status": "Delivered", "desc": "GIT receipt Jun 22 — Storm Electric dropped off (2) 8ft Reno boxes at warehouse.", "job": "Unspecified (Reno 8ft via Storm)", "flag": "No SO/PO on GIT receipt — tag at warehouse to identify job"},
    {"id": "SHP-016", "mfg": "RENO Lighting", "so": "S095544", "po": "5405", "ship": "2026-06-25", "carrier": "Western Canada Express", "tracking": "MISSING", "exp": "2026-07-02", "status": "Delivered", "desc": "RENO S095544 / PO 5405 — shipped Jun 25 (WCE). GIT confirmed receipt Jul 2: 'WCE delivered two pallets from Reno'; Jeff tagged both pallets for Amacon - VUE. DELIVERED.", "job": "THE VUE (Amacon)", "flag": ""},
    {"id": "SHP-017", "mfg": "RENO Lighting", "so": "S095542", "po": "5393", "ship": "2026-06-25", "carrier": "Western Canada Express", "tracking": "MISSING", "exp": "2026-07-02", "status": "Delivered", "desc": "RENO S095542 / PO 5393 — shipped Jun 25 (WCE). GIT confirmed receipt Jul 2 (second of two pallets from Reno); tagged Amacon - VUE. DELIVERED.", "job": "THE VUE (Amacon)", "flag": ""},
    {"id": "SHP-018", "mfg": "Advant Lighting", "so": "", "po": "5404", "ship": "2026-06-23", "carrier": "Green Image Tech (local)", "tracking": "", "exp": "2026-06-23", "status": "Delivered", "desc": "MHOND CEILING ADVANT — Hazel 275 E 14th Ave. PO 5404 to GIT. GIT confirmed 'ready for pickup. Four boxes.' Jun 23.", "job": "Hazel 275 E 14th Ave (Mhond)", "flag": ""},
    {"id": "SHP-019", "mfg": "Ortech (via GIT)", "so": "", "po": "", "ship": "2026-06-23", "carrier": "Green Image Tech (receipt)", "tracking": "", "exp": "2026-06-23", "status": "Delivered", "desc": "GIT receipt Jun 23 — 'a pallet of Ortech products delivered' (packing list attached). Likely Hopehill/Baptist Ortech pots.", "job": "Hopehill / Baptist (Ortech)", "flag": "Ortech not on approved mfg list — GIT warehouse receipt; confirm job from packing slip"},
    {"id": "SHP-020", "mfg": "CSC LED", "so": "", "po": "", "ship": "2026-06-22", "carrier": "Local pickup (Burnaby)", "tracking": "", "exp": "2026-06-22", "status": "Delivered", "desc": "CSC LED 'Storm 4' Vapour Tight, 3 pcs' — ready for local pickup; invoice 4090877 Jun 23.", "job": "Storm Electric", "flag": ""},
    {"id": "SHP-021", "mfg": "EiKO", "so": "SO188866", "po": "5344", "ship": "2026-06-26", "carrier": "Canpar", "tracking": "D420604500000032986001", "exp": "2026-07-06", "status": "Delivered", "desc": "CF - 200 Burrard — EiKO order 5344 / SO188866, shipped Jun 30 (Canpar, tracking D420604500000032986001) to Fully Loaded Services (Richmond Storage). Jeff confirmed Jul 6: '200 Burrard: All products have arrived.' DELIVERED.", "job": "CF - 200 Burrard (EiKO)", "flag": ""},
    {"id": "SHP-022", "mfg": "Onlumi (Shenzhen)", "so": "", "po": "", "ship": "2026-06-25", "carrier": "DHL", "tracking": "7754899854", "exp": "2026-07-02", "status": "Overdue", "desc": "Onlumi (Shenzhen) strip/connectors — DHL waybill 7754899854 from Shenzhen Onlumi. Customs/duty paid Jun 26. Expected ~Jul 2; no warehouse receipt yet as of Jul 11. OVERDUE — follow up.", "job": "Unspecified (Onlumi strip/connectors)", "flag": "OVERDUE 27 days: overseas DHL (waybill 7754899854); customs cleared Jun 26; still no GIT receipt as of Jul 29 — confirm delivery / trace"},
    {"id": "SHP-023", "mfg": "RENO Lighting", "so": "S091325", "po": "5303", "ship": "2026-06-26", "carrier": "Western Canada Express", "tracking": "MISSING", "exp": "2026-07-03", "status": "Delivered", "desc": "Store 9 / Stock — RENO SO# S091325 / PO# 5303 reshipped Jun 26 (WCE, ETA 7-8). ETA elapsed Jul 3-4; presumed delivered (may correspond to a recent GIT Reno pallet receipt).", "job": "Store 9 / Stock", "flag": "Presumed delivered (WCE ETA elapsed); confirm with GIT / request WCE PRO"},
    {"id": "SHP-024", "mfg": "RENO Lighting", "so": "", "po": "", "ship": "2026-06-25", "carrier": "Western Canada Express", "tracking": "", "exp": "2026-06-25", "status": "Delivered", "desc": "GIT receipt Jun 25 — 'WCE delivered a pallet from Reno' (packing slip attached). Warehouse arrival.", "job": "Unspecified (Reno)", "flag": "No SO/PO on GIT receipt — tag to identify job/PO"},
    {"id": "SHP-025", "mfg": "Nedco West Canada", "so": "5974859", "po": "5406", "ship": "", "carrier": "Ships to site (via RENO)", "tracking": "MISSING", "exp": "2026-07-15", "status": "Order Placed", "desc": "MAPLE TOWERS - NEDCO — PO to Nedco Jun 25; Nedco order 5974859 placed, ships to site as directed. RENO advises R31106 out of stock till Jul 15, R31105 till Aug 31.", "job": "Maple Towers", "flag": "BACKORDER: R31106 restock ETA Jul 15 now passed (check availability), R31105 ETA Aug 31 — decide whether to partial-ship in-stock items"},
    {"id": "SHP-026", "mfg": "Artika (via Design Concepts)", "so": "", "po": "5408", "ship": "2026-07-01", "carrier": "carrier TBD (auto tracking)", "tracking": "MISSING", "exp": "2026-07-06", "status": "Overdue", "desc": "WOODLANDS ARTIKA EXTRAS TYPE G1 / N - Artika confirmed PO 5408 Jun 26 (in stock, ships 2-3 biz days, auto tracking). Presumed shipped ~Jul 1; no warehouse receipt after 3+ weeks.", "job": "Woodlands", "flag": "OVERDUE: no receipt 4+ weeks - escalate Artika/Design Concepts for auto tracking # + ETA (Artika not on approved mfg list)"},
    {"id": "SHP-027", "mfg": "CSC LED", "so": "4091094", "po": "", "ship": "2026-06-29", "carrier": "CSC prepaid (carrier TBD)", "tracking": "MISSING", "exp": "2026-07-06", "status": "Delivered", "desc": "CSC LED order 4091094 — placed Jun 25 (prepay & charge), ships from Ontario ~5 biz days. Invoice 4091094 Jun 26. ETA Jul 6 elapsed; presumed delivered.", "job": "Unspecified (CSC 4091094)", "flag": "Presumed delivered (ETA+); no tracking # on file — confirm receipt & identify job"},
    {"id": "SHP-028", "mfg": "CSC LED", "so": "", "po": "5376", "ship": "", "carrier": "Local pickup (Burnaby)", "tracking": "", "exp": "", "status": "Order Placed", "desc": "CSC LED PO 5376 — order ready at CSC; not yet picked up (CSC nudged Jun 26 'hasn't been picked up yet').", "job": "Unspecified (CSC PO 5376)", "flag": "Ready at CSC — arrange pickup; confirm job"},
    {"id": "SHP-029", "mfg": "RENO Lighting", "so": "", "po": "", "ship": "2026-06-26", "carrier": "Vitran", "tracking": "", "exp": "2026-06-26", "status": "Delivered", "desc": "GIT receipt Jun 26 — 'Vitran delivered a pallet from Reno' (packing slip attached). Storm Electric picked up some boxes from this delivery Jun 26.", "job": "Unspecified (Reno via Vitran)", "flag": "No SO/PO on GIT receipt — tag to identify job/PO"},
    {"id": "SHP-030", "mfg": "Kuzco", "so": "", "po": "", "ship": "", "carrier": "", "tracking": "MISSING", "exp": "", "status": "Order Placed", "desc": "WOODLANDS EXTRA KUZCO TYPE N3, R3 — PO to Kuzco (via Nuvo Sales) Jun 25; Sharon confirmed 'PO received & entered.' Kuzco invoice C-INV00103380 ($3,061.91) Jun 29. Awaiting ETA.", "job": "Woodlands", "flag": "PO entered Jun 25 (24 days) — request ETA/ship confirmation from Nuvo/Kuzco"},
    {"id": "SHP-031", "mfg": "Lotus", "so": "", "po": "", "ship": "", "carrier": "Local pickup (Delta)", "tracking": "", "exp": "", "status": "Order Placed", "desc": "BAPTIST SAMPLING LOTUS R1 — Lotus confirmed 1 sample processed for pickup in Delta Jun 30 (case-qty item reduced to single sample).", "job": "BAPTIST HOUSING SAMPLES", "flag": "Ready for pickup at Lotus Delta warehouse — arrange pickup"},
    {"id": "SHP-032", "mfg": "IP Lighting", "so": "", "po": "", "ship": "2026-07-03", "carrier": "Urban Valley (local courier)", "tracking": "726957", "exp": "2026-07-03", "status": "Delivered", "desc": "OM - M1 custom plate templates — IP Lighting confirmed 'templates ready for pickup' Jul 2; courier order 726957 picked up from IP Lighting to LTS Jul 3.", "job": "OM - M1 Custom Plate", "flag": ""},
    {"id": "SHP-033", "mfg": "Green Image Tech", "so": "", "po": "", "ship": "2026-07-03", "carrier": "Urban Valley (local courier)", "tracking": "727227", "exp": "2026-07-03", "status": "Delivered", "desc": "OM Bridge & Elliot rough-in plates (302 pcs) — GIT ready for pickup (13 boxes); courier order 727227 to OM - Bridge & Elliot site (Delta) Jul 3. Jeff confirmed 'rough-in plates arrived to site Friday Jul 3.'", "job": "OM - Bridge & Elliot", "flag": ""},
    {"id": "SHP-034", "mfg": "Lotus", "so": "", "po": "", "ship": "", "carrier": "Local pickup (Delta)", "tracking": "", "exp": "", "status": "Order Placed", "desc": "Baptist sampling Lotus R1 — Lotus LED processed order for pickup in Delta (sold in case qty of 28; 1 pc sample arranged for client).", "job": "BAPTIST HOUSING SAMPLES", "flag": "Sample processed for pickup in Delta"},
    {"id": "SHP-035", "mfg": "Commercial Lighting (Comlight)", "so": "1797760", "po": "5401", "ship": "2026-07-03", "carrier": "Urban Valley (local courier)", "tracking": "727226", "exp": "2026-07-03", "status": "Delivered", "desc": "200B - BASE BUILDING MR16 LED — Comlight order conf #1797760; PO 5401 (500x MR16 lamps). Courier order 727226 Comlight (Delta) to LTS Jul 3. Invoice 3771225. DELIVERED.", "job": "200B - Base Building MR16 LED", "flag": "Comlight not on approved mfg list — confirmed supplier PO"},
    {"id": "SHP-036", "mfg": "RENO Lighting", "so": "S096107", "po": "5417", "ship": "2026-07-09", "carrier": "CCT (Cross Canada Transportation)", "tracking": "CC0997981", "exp": "2026-07-13", "status": "Delivered", "desc": "OM - CASTLES RENO TYPE 1/1A/2/2B/3 — PO 5417 to RENO Jul 7 (SO S096107). RENO SHIPPED 1438 units Jul 9 (CCT, tracking CC0997981, ref WH/OUT/39244, ETA 7-8 days); remainder on back order until 08/31/26. RENO invoice IN101685 issued Jul 10. GIT (Simon) confirmed receipt Jul 13: CCT Canada delivered a pallet from Reno. DELIVERED (partial).", "job": "OM - CASTLES RENO", "flag": "PARTIAL: 1438 units delivered Jul 13 (CCT #CC0997981); remainder backordered to Aug 31 — track balance shipment."},
    {"id": "SHP-037", "mfg": "RENO Lighting", "so": "", "po": "", "ship": "2026-07-06", "carrier": "Western Canada Express", "tracking": "", "exp": "2026-07-06", "status": "Delivered", "desc": "GIT receipt Jul 6 — 'Western Canada Express delivered four pallets from Reno' = (100) GD-TRC2060 troffers, 4 pallets. Some boxes damaged; GIT signed as damaged and driver took photos. Client requested outbound pickup pushed to week of Jul 13.", "job": "Unspecified (Reno)", "flag": "DAMAGE EXCEPTION: some boxes damaged on arrival — signed as damaged, photos taken; file carrier/RENO claim & tag pallets to job/PO"},
    {"id": "SHP-038", "mfg": "CNA Lighting", "so": "", "po": "", "ship": "2026-07-03", "carrier": "Local pickup (Burnaby)", "tracking": "", "exp": "2026-07-05", "status": "Delivered", "desc": "CNA bankcard online order #070226 ($114.82) placed Jul 3; approval 06307G. Small local pickup order — presumed picked up/closed.", "job": "Unspecified (CNA order 070226)", "flag": "Small CNA order — confirm pickup & identify job"},
    {"id": "SHP-039", "mfg": "Sylvania/Ledvance", "so": "", "po": "", "ship": "", "carrier": "Ships from Maxilite (via Save More Lighting)", "tracking": "MISSING", "exp": "", "status": "Order Placed", "desc": "WOODLANDS EXTRA TYPE B VANITY — PO to Save More Lighting Jun 9 (Maxilite fulfillment); as of Jul 7 Maxilite 'has not received it yet', still awaiting ETA. Quote 3452 ($13,164.26) approved by Intergulf Jun 9.", "job": "Woodlands", "flag": "STALE ~50 days, no ETA/ship notice; Maxilite not yet in receipt — escalate for ETA (Save More/Maxilite not on approved mfg list)"},
    {"id": "SHP-040", "mfg": "CSC LED", "so": "4091537", "po": "5419", "ship": "2026-07-09", "carrier": "Split: local pickup (6 boxes) + CSC ex-AB warehouse", "tracking": "MISSING", "exp": "2026-07-14", "status": "Overdue", "desc": "MARQUEE IP — CSC LED order receipt #4091537 (Jul 9). 6 boxes ready for local pickup now; remainder shipping from CSC's Alberta warehouse for delivery by Tuesday Jul 14 (CSC 'alerted to ship for delivery by Tuesday').", "job": "MARQUEE IP", "flag": "PARTIAL: 6 boxes local pickup + balance ex-Alberta (ETA Jul 14 — now 15 days past, no receipt); CSC invoice 4091538 issued Jul 10 — confirm pickup + capture AB freight tracking #"},
    {"id": "SHP-041", "mfg": "Gescan (Sonepar)", "so": "", "po": "", "ship": "", "carrier": "", "tracking": "MISSING", "exp": "", "status": "Order Placed", "desc": "APOLLA DALS FOR 1126 EXTRAS — PO issued to Gescan (a Sonepar company) Jul 9. Awaiting order confirmation and ETA.", "job": "1126 (Apolla DALS extras)", "flag": "New PO Jul 9 (Gescan not on approved mfg list) — await confirmation/ETA"},
    {"id": "SHP-042", "mfg": "CNA Lighting", "so": "", "po": "", "ship": "", "carrier": "", "tracking": "MISSING", "exp": "", "status": "Order Placed", "desc": "WOODLANDS EXTRA TYPE B BULB — PO to CNA International re-sent Jul 9 (original Jun 9). Awaiting CNA processing/ETA.", "job": "Woodlands", "flag": "New/re-sent PO Jul 9 — confirm CNA has processed and get ETA"},
    {"id": "SHP-043", "mfg": "RENO Lighting", "so": "S096251", "po": "5420", "ship": "2026-07-22", "carrier": "Day & Ross", "tracking": "AC3129246", "exp": "2026-07-27", "status": "Overdue", "desc": "CF - 250HOWE FL16 RENO - PO 5420 (SO S096251) released and SHIPPED Jul 22 (Day & Ross, tracking AC3129246, ref WH/OUT/39835, ETA 5 days). Track at dayross.com; ETA ~Jul 27.", "job": "CF - 250HOWE FL16 RENO", "flag": "OVERDUE: Day & Ross #AC3129246 shipped Jul 22, ETA Jul 27 now 9 days elapsed and no GIT warehouse receipt logged; Jeff chased RENO/Andrew Jul 29 (was 7 days) - trace Day & Ross #AC3129246 and confirm delivery to 250 Howe"},
    {"id": "SHP-044", "mfg": "Commercial Lighting (Comlight)", "so": "1800590", "po": "", "ship": "", "carrier": "Local pickup (Delta)", "tracking": "", "exp": "2026-07-13", "status": "Delivered", "desc": "BTC - EM LIGHTING TEST — PO issued to Comlight (Sean Loban) Jul 10; Comlight order confirmation #1800590 returned same day, 'ready for pickup anytime.' Jeff confirmed pickup Monday Jul 13 (today).", "job": "BTC - EM Lighting Test", "flag": "Comlight not on approved mfg list — pickup was Jul 13 (Jeff confirmed); presumed collected as of Jul 20 — confirm at warehouse"},
    {"id": "SHP-045", "mfg": "Votatec", "so": "", "po": "", "ship": "2026-07-20", "carrier": "Fastfrate", "tracking": "CFF19787", "exp": "2026-07-20", "status": "Delivered", "desc": "BAPTIST - MT VOTATEC - PO to Votatec Jul 7; invoice 95081 ($3,748.50) Jul 10. Shipped via Fastfrate (tracking CFF19787). GIT (Simon) confirmed receipt Jul 20: Fastfrate delivered a pallet from Votatec. DELIVERED.", "job": "Baptist Housing (Votatec MT)", "flag": "Votatec not on approved mfg list - GIT warehouse receipt Jul 20; tag pallet to Baptist MT"},
    {"id": "SHP-046", "mfg": "CNA Lighting", "so": "", "po": "", "ship": "2026-07-10", "carrier": "TBD", "tracking": "MISSING", "exp": "", "status": "In Transit", "desc": "CNA International invoice 51806 issued Jul 10 (Alan Yang) — new CNA order billed this week, not yet matched to a PO/job. Distinct from the Jul 3 bankcard order (SHP-038). CNA orders are typically local pickup (Burnaby).", "job": "Unspecified (CNA inv 51806)", "flag": "NEW: CNA invoice 51806 (Jul 10) with no PO/job or tracking — identify project and pickup status"},
    {"id": "SHP-047", "mfg": "EiKO", "so": "SO195237", "po": "5425", "ship": "2026-07-15", "carrier": "Canpar", "tracking": "D433001860000008105001", "exp": "2026-07-21", "status": "Delivered", "desc": "CANUCKS - SUITE UNDERCABINET SAMPLE - EiKO Premise order 5425 / SO195237, shipped Jul 15 (Canpar, tracking D433001860000008105001) to LTS Burnaby. ETA Jul 21 elapsed - presumed delivered.", "job": "CANUCKS - SUITE UNDERCABINET SAMPLE", "flag": "Presumed delivered (Canpar ETA Jul 21 elapsed) - confirm GIT receipt"},
    {"id": "SHP-048", "mfg": "CSC LED", "so": "4091675", "po": "", "ship": "2026-07-13", "carrier": "Canpar", "tracking": "D431009160000003242004", "exp": "2026-07-16", "status": "Delivered", "desc": "CSC LED order 4091675 — order receipt confirmation Jul 13; Canpar ASN Jul 13 (4 pieces, 6 lb, ref 4091675, tracking D431009160000003242004) to LTS Canada Burnaby. Small parcel, ETA ~Jul 16 elapsed — presumed delivered.", "job": "Unspecified (CSC 4091675)", "flag": "NEW this run: Canpar tracking D431009160000003242004 captured; presumed delivered (ETA+) — confirm GIT receipt & identify job"},
    {"id": "SHP-049", "mfg": "RENO Lighting", "so": "", "po": "", "ship": "2026-07-20", "carrier": "CCT Canada", "tracking": "", "exp": "2026-07-20", "status": "Delivered", "desc": "GIT (Simon) receipt Jul 20 — CCT Canada delivered one pallet from Reno on Jul 17 and a second on Jul 20. DAMAGE: one case on the Jul 20 pallet potentially damaged — signed for as damaged. New warehouse arrivals since last run; PO/job not identified on receipt.", "job": "Unspecified (Reno via CCT)", "flag": "DAMAGE EXCEPTION: one case (Jul 20 pallet) signed as damaged — inspect, photograph, file carrier/RENO claim; tag both pallets (Jul 17 & 20) to job/PO. Most likely RAVENNA -TYPE K4/N3 (PO Jul 13); CF-250HOWE/PO 5420 shipped separately Jul 22 via Day & Ross."},
    {"id": "SHP-050", "mfg": "Green Image Tech", "so": "", "po": "", "ship": "2026-07-22", "carrier": "Green Image Tech (ready for pickup)", "tracking": "", "exp": "2026-07-22", "status": "Delivered", "desc": "710 DOGWOOD WARRANTY + EXTRAS - LTS PO to GIT (Fynn Wu) Jul 22 (QuickBooks). GIT confirmed Order is ready for pickup Jul 22. Warranty/extras for Dogwood (Berts Electric ref S0017116). Ready at GIT warehouse.", "job": "710 Dogwood Warranty + Extras", "flag": "Ready for pickup at GIT - arrange collection"},
    {"id": "SHP-051", "mfg": "IP Lighting", "so": "", "po": "", "ship": "2026-07-22", "carrier": "Urban Valley (local courier)", "tracking": "731676", "exp": "2026-07-22", "status": "Delivered", "desc": "IP Lighting -> LTS inbound - courier order 731676 (Sameday) picked up from IP Lighting (3611 Commercial St) to LTS Burnaby Jul 22. Likely BRIDGE AND ELLIOT IP LIGHTING order (active PO thread Jul 22).", "job": "Bridge & Elliot (IP Lighting)", "flag": "Confirm this courier run matches Bridge & Elliot IP PO; tag on receipt"},
    {"id": "SHP-052", "mfg": "Lotus", "so": "", "po": "", "ship": "2026-07-22", "carrier": "Urban Valley (local courier)", "tracking": "731678", "exp": "2026-07-22", "status": "Delivered", "desc": "Lotus LED -> LTS inbound - courier order 731678 picked up from Lotus LED Lights Warehouse (Delta) to LTS Burnaby Jul 22. Likely Baptist sampling Lotus order.", "job": "Unspecified (Lotus -> LTS)", "flag": "No SO/PO on courier run - tag to identify job (Baptist Lotus sample?)"},
    {"id": "SHP-053", "mfg": "CNA Lighting", "so": "", "po": "", "ship": "2026-07-22", "carrier": "Urban Valley (local courier)", "tracking": "731728", "exp": "2026-07-22", "status": "Delivered", "desc": "MAPLE TOWERS - CNA - CNA (Alan Yang) confirmed PO Jul 22; courier order 731728 (2 Hour Rush) picked up from CNA Lighting (Burnaby) direct to Maple Towers site (11841 222 St, Maple Ridge) Jul 22.", "job": "Maple Towers", "flag": ""},
    {"id": "SHP-054", "mfg": "RENO Lighting", "so": "", "po": "", "ship": "", "carrier": "", "tracking": "MISSING", "exp": "", "status": "Order Placed", "desc": "BE - RENO TYPE L1 - PO to RENO Jul 22 (QuickBooks); Yassine (RENO) acknowledged Jul 22, Jeff advised ~2-3 week lead, will email for release. Awaiting release/ETA.", "job": "Bridge & Elliot (RENO Type L1)", "flag": "New PO Jul 22 - 2-3 week lead; follow up for release date/ETA"},
    {"id": "SHP-055", "mfg": "RENO Lighting", "so": "S096887", "po": "5438", "ship": "2026-07-27", "carrier": "Day & Ross", "tracking": "A11627100", "exp": "2026-08-01", "status": "Delivered", "desc": "PFG EXTRAS T5 — RENO SO S096887 / PO 5438 SHIPPED Jul 27 (Day & Ross, ETA 4-5, tracking A11627100, ref WH/OUT/40050). Received at LTS/GIT Jul 31 as part of the 4-pallet Day & Ross + 1 Fastfrate delivery; some pallets arrived DAMAGED (joint PO 5303/5438/5439).", "job": "PFG EXTRAS T5", "flag": "DAMAGE: pallets damaged on arrival Jul 31 — photos taken; file carrier/RENO claim & capture Day & Ross PRO#"},
    {"id": "SHP-056", "mfg": "RENO Lighting", "so": "S096925", "po": "5439", "ship": "2026-07-28", "carrier": "Day & Ross", "tracking": "A11639512", "exp": "2026-08-01", "status": "Delivered", "desc": "OM CASTLE PARKADE — RENO SO S096925 / PO 5439 SHIPPED Jul 28 (Day & Ross, ETA 4, tracking A11639512, ref WH/OUT/40109). First ship notice had wrong address; RENO rerouted/corrected. Received at LTS/GIT Jul 31 (joint Day & Ross delivery); some pallets DAMAGED.", "job": "OM CASTLE PARKADE", "flag": "DAMAGE: pallets damaged on arrival Jul 31 — file claim. Address corrected mid-transit (Andrew flagged Jul 28)."},
    {"id": "SHP-057", "mfg": "RENO Lighting", "so": "S091325", "po": "5303", "ship": "2026-07-27", "carrier": "Day & Ross", "tracking": "MISSING", "exp": "2026-07-31", "status": "Delivered", "desc": "Store 9 / Stock — recurring stock SO S091325 / PO 5303 shipped Jul 27 (Day & Ross, ETA 4-5, ref WH/OUT/38817). Received at LTS/GIT Jul 31 but units arrived DAMAGED; RENO re-shipped replacement Aug 3 (see SHP-058).", "job": "Store 9 / Stock", "flag": "DAMAGE: received damaged Jul 31; replacement re-shipped Aug 3 (SHP-058) — file carrier/RENO claim"},
    {"id": "SHP-058", "mfg": "RENO Lighting", "so": "S091325", "po": "5303", "ship": "2026-08-03", "carrier": "Day & Ross", "tracking": "A11706479", "exp": "2026-08-09", "status": "Delivered", "desc": "Store 9 / Stock (REPLACEMENT) — RENO re-shipped the goods damaged in the Jul 31 delivery (SO S091325 / PO 5303) on Aug 3 (Day & Ross, tracking A11706479, ref WH/OUT/40100, ETA 5-6). GIT (Simon) confirmed receipt Aug 7: 'Day & Ross delivered a pallet from Reno' — one box may be damaged, reported to driver, photo taken.", "job": "Store 9 / Stock", "flag": "DELIVERED EARLY Aug 7 (2 days ahead of ETA). DAMAGE: one box flagged on arrival — inspect, photograph, file claim if confirmed"},
    {"id": "SHP-059", "mfg": "Kuzco", "so": "", "po": "5432", "ship": "", "carrier": "Ships via Nuvo Sales", "tracking": "MISSING", "exp": "", "status": "Order Placed", "desc": "BRIDGE AND ELLIOT KUZCO — Kuzco PO 5432 (via Nuvo Sales). Sharon @ Nuvo forwarded order confirmation with ESDs Jul 27. Awaiting ship/tracking.", "job": "Bridge & Elliot (Kuzco)", "flag": "Order confirmed w/ ESDs Jul 27 — monitor for ship notice & carrier tracking #"},
    {"id": "SHP-060", "mfg": "Kuzco", "so": "", "po": "", "ship": "", "carrier": "Ships via Nuvo Sales", "tracking": "MISSING", "exp": "", "status": "Order Placed", "desc": "INTERGULF KINSLEY SHOWROOM — PO to Kuzco (via Nuvo Sales) Jul 27; Sharon @ Nuvo confirmed 'PO received & entered' Jul 27. Awaiting order confirmation, ESDs and ship/tracking.", "job": "Intergulf Kinsley Showroom", "flag": "New PO Jul 27 (Kuzco via Nuvo) — request order confirmation + ETA"},
    {"id": "SHP-061", "mfg": "Commercial Lighting (Comlight)", "so": "1803037", "po": "", "ship": "", "carrier": "Local pickup (Delta)", "tracking": "", "exp": "", "status": "Order Placed", "desc": "JORDAN — PO to Comlight (Sean Loban); order confirmation #1803037 returned Jul 27, 'ready for pickup anytime.' Andrew coordinating collection.", "job": "Jordan", "flag": "Comlight not on approved mfg list — ready for pickup at Comlight (Delta) since Jul 27; arrange collection"},
    {"id": "SHP-062", "mfg": "Commercial Lighting (Comlight)", "so": "1803465", "po": "", "ship": "", "carrier": "Local pickup (Delta)", "tracking": "MISSING", "exp": "", "status": "Order Placed", "desc": "BTC - EM BALLAST — PO to Comlight (Sean Loban); order confirmation #1803465 returned Jul 29. Sean: 'I'll let you know when this arrives for pickup.' Not yet in stock at Comlight.", "job": "BTC - EM Ballast", "flag": "Comlight not on approved mfg list — new order Jul 29, awaiting stock arrival; monitor for pickup-ready notice"},
    {"id": "SHP-063", "mfg": "Standard Products", "so": "", "po": "", "ship": "2026-07-31", "carrier": "K&H Dispatch", "tracking": "", "exp": "2026-07-31", "status": "Delivered", "desc": "GIT (Simon) receipt ~Jul 31 — K&H Dispatch delivered 5 boxes of 3ft strip lights from Stanpro (Standard Products) earlier in the week. Warehouse arrival; no PO/job on receipt.", "job": "Unspecified (Stanpro 3ft strip)", "flag": "No SO/PO on GIT receipt — tag at warehouse to identify job/PO"},
    {"id": "SHP-064", "mfg": "Matteo Lighting", "so": "", "po": "5448", "ship": "", "carrier": "Artika fulfillment (carrier TBD)", "tracking": "MISSING", "exp": "2026-08-04", "status": "Overdue", "desc": "CHAMBER PROPERTIES FANS — PO 5448 (fan samples). Artika (Carla Torrez) advised order sent to fulfillment with ESD Aug 3-4; tracking to follow. Mfg attribution tentative (Artika fan program).", "job": "CHAMBER PROPERTIES FANS", "flag": "OVERDUE: no tracking # 6 days past ESD (Aug 3-4) — escalate Artika for auto tracking # + confirm ship/ETA"},
    {"id": "SHP-065", "mfg": "Nedco West Canada", "so": "5996235", "po": "", "ship": "2026-08-07", "carrier": "Ships to site (via RENO/Nedco)", "tracking": "MISSING", "exp": "2026-08-12", "status": "In Transit", "desc": "HALLMARK ON THE LAKE — Nedco order 5996235 (PO to Amber Larsen Jul 31). In-stock items released/shipped Fri Aug 7 per Andrew; R31104 RENO-S12R-MCCT-WH (123 pcs) backordered with ETA Aug 12.", "job": "Hallmark on the Lake", "flag": "PARTIAL/BACKORDER: in-stock portion shipped Aug 7 (capture carrier tracking#); R31104 (123 pcs) ETA Aug 12 — track balance shipment"},
    {"id": "SHP-066", "mfg": "CSC LED", "so": "4092331", "po": "5437", "ship": "2026-08-04", "carrier": "Digital Waybill (Sameday, local)", "tracking": "734114", "exp": "2026-08-04", "status": "Delivered", "desc": "WOODLANDS - R1 CSC — CSC LED order receipt 4092331 (Jul 30), invoiced Aug 5. Digital Waybill order 734114 (Sameday) picked up at CSC LED (Port Coquitlam) for delivery to Intergulf - Woodlands (2377 E 11 Ave) Aug 4.", "job": "Woodlands (R1 CSC)", "flag": "Local same-day delivery direct to Woodlands site — confirm site receipt"},
    {"id": "SHP-067", "mfg": "CSC LED", "so": "4092295", "po": "", "ship": "2026-07-30", "carrier": "Digital Waybill (Direct, local)", "tracking": "733686", "exp": "2026-07-30", "status": "Delivered", "desc": "CSC LED order receipt 4092295 (Jul 30), invoiced Jul 31. Digital Waybill order 733686 (Direct) picked up at CSC LED (Port Coquitlam) for delivery to Maple Towers (11841 222 St, Maple Ridge) Jul 30.", "job": "Maple Towers", "flag": "Local same-day delivery direct to Maple Towers site — confirm site receipt & tie to Maple Towers CSC scope"},
    {"id": "SHP-068", "mfg": "RENO Lighting", "so": "", "po": "", "ship": "2026-08-06", "carrier": "CCT Canada", "tracking": "42237565", "exp": "2026-08-06", "status": "Delivered", "desc": "GIT (Simon) receipt Aug 6 — CCT delivered a pallet from Reno. Carrier tracking 42237565; RENO internal PO 95542 on the paperwork (not an LTS QuickBooks PO). New warehouse arrival; LTS PO/job not identified on receipt.", "job": "Unspecified (Reno via CCT)", "flag": "NEW this run: RENO pallet received Aug 6 (CCT #42237565 / RENO PO 95542) — tag at warehouse to identify LTS job/PO; may cover CF-250HOWE/PO 5420 (overdue, SHP-043)"},
    {"id": "SHP-069", "mfg": "RENO Lighting", "so": "S097428", "po": "5454", "ship": "2026-08-10", "carrier": "Purolator (Small Parcel)", "tracking": "520691119819", "exp": "2026-08-17", "status": "In Transit", "desc": "OM CASTLE PK EXTRAS — LTS PO 5454 / RENO SO S097428. RENO SHIPPED today Aug 10 (Purolator Small Parcel, tracking 520691119819, ref WH/OUT/40634, ETA 5-7 days). Track at purolator.com; expected ~Aug 17.", "job": "OM Castle Parkade (Extras)", "flag": "NEW this run: shipped today Aug 10 (Purolator #520691119819, ETA 5-7) — monitor for delivery to warehouse"},
    {"id": "SHP-070", "mfg": "Gescan (Sonepar)", "so": "", "po": "", "ship": "", "carrier": "Local pickup (Coquitlam)", "tracking": "", "exp": "", "status": "Order Placed", "desc": "WOODLANDS EXTRA ARLINGTON — LTS PO issued to Gescan (a Sonepar company) Aug 7; Asif Karim returned order confirmation same day, 'Pick up after 11AM.' Ready for collection at Gescan (266 Schoolhouse St, Coquitlam).", "job": "Woodlands (Extra Arlington)", "flag": "Gescan not on approved mfg list — ready for pickup Aug 7; arrange collection"},
    {"id": "SHP-071", "mfg": "Lotus", "so": "", "po": "", "ship": "", "carrier": "Local pickup (Delta)", "tracking": "", "exp": "", "status": "Order Placed", "desc": "SAMPLES #2 — Lotus LED sample order, revised through R1/R2/R3 (order emails Aug 5-Aug 10 via QuickBooks). Small sample quantities for client review; typically pickup at Lotus Delta warehouse.", "job": "Samples #2 (Lotus)", "flag": "NEW this run: Lotus sample order (rev R3 Aug 10) — confirm final rev is processed and arrange pickup"},
    {"id": "SHP-072", "mfg": "Sylvania/Ledvance", "so": "", "po": "", "ship": "", "carrier": "Ships from Maxilite (via Save More Lighting)", "tracking": "MISSING", "exp": "", "status": "Order Placed", "desc": "WOODLANDS EXTRA TYPE B VANITY #2 — follow-up/re-order to Save More Lighting (Maxilite fulfillment) issued Aug 10 (QuickBooks). Companion to SHP-039 (original Type B Vanity order). Awaiting ETA.", "job": "Woodlands", "flag": "NEW this run: re-order Aug 10 (Save More/Maxilite not on approved mfg list) — chase for ETA/ship notice; tie to SHP-039"},
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
HTML = HTML.replace("__LAST_UPDATED__", "Aug 10, 2026")
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
