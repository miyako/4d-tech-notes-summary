# Tech Note 24-02: Visualize Real-Time Data with WebSocket Client & 4D View Pro

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** January 23, 2024 | **Product/Version:** 4D View Pro v19 R3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79367
**Download:** https://kb.4d.com/DLTN/TN/2024/24-02_WebSocketClientVPDashboard.zip

## Proposition
Real-time data sources like stock or cryptocurrency exchanges push a constant stream of updates that are difficult to visualize with polling-based approaches. With WebSocket client support added in 4D v20 R3, developers can subscribe directly to third-party live feeds; this note shows how to route that live data into 4D View Pro to build a self-updating visual dashboard.

## Key Points
- **4D.WebSocket client class:** Introduced in v20 R3 (complementing the v20 "4D.WebSocketServer" class), created via `4D.WebSocket.new($url; handlerInstance)` and stored in a Form variable to persist the connection.
- **Connection handler class pattern:** A dedicated class (`WSConnectionHandler`) implements `onOpen` (sends a JSON subscribe message) and `onMessage` (parses incoming JSON) to manage the WebSocket lifecycle.
- **Coinbase ticker feed:** Connects to the free, no-auth "wss://ws-feed.exchange.coinbase.com" endpoint and subscribes to the BTC-USD ticker channel.
- **Rolling price buffer:** Incoming prices are maintained in a 10-element collection using `.shift()` to drop the oldest value and `.push()` to add the newest, providing a moving window for charting.
- **Feeding View Pro cells:** `VP Cell` and `VP SET VALUE` write the rolling price data into a spreadsheet row on a recurring `On Timer` event (`SET TIMER`), keeping the sheet continuously current.
- **SpreadJS chart creation via JavaScript:** `WA Evaluate JavaScript` executes SpreadJS API calls (`sheet.charts.add(...)`) to programmatically create and title a line chart sourced from the price row.
- **Dashboard styling and cleanup:** `VP SET DEFAULT STYLE` and `VP SET CELL STYLE` set a color theme, while exporting/re-importing the area's config object (`VP Export to object` / `VP IMPORT FROM OBJECT`) hides scrollbars and the tab strip for a clean dashboard look.

## Featured Technology
- **4D.WebSocket:** Native class for creating WebSocket client connections to external servers.
- **JSON Parse:** Converts incoming WebSocket message payloads into 4D objects.
- **4D View Pro (VP commands):** `VP Cell`, `VP SET VALUE`, `VP SET DEFAULT STYLE`, `VP SET CELL STYLE`, `VP Export to object`/`VP IMPORT FROM OBJECT` for spreadsheet-based dashboard construction and styling.
- **SpreadJS JavaScript API:** Accessed via `WA Evaluate JavaScript` to create and configure charts beyond what native VP commands expose directly.
- **Form timer events:** `SET TIMER`/"On Timer" drive the periodic refresh cycle for the live dashboard.

## Best Practices Highlighted
1. Persist the WebSocket client reference in a Form variable so the connection survives across form events.
2. Use a rolling shift/push collection to bound memory and keep charts focused on the most recent data window.
3. Disable unneeded View Pro UI chrome (toolbar, ribbon, scrollbars, tab strip) when building a dashboard so it looks purpose-built rather than like a spreadsheet.

## Context / Positioning
Published shortly after 4D v20 R3 introduced WebSocket client support, this note showcases 4D's growing real-time and integration capabilities alongside its established 4D View Pro spreadsheet/reporting component, reflecting a broader trend of pairing modern native APIs (WebSocket, classes) with rich UI components to build live business dashboards without external tooling.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
