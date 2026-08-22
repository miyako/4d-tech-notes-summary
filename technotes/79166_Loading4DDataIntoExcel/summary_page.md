# Tech Note 23-08: Loading 4D Data into Excel using REST API

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** April 18, 2023 | **Product/Version:** 4D Server v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79166
**Download:** https://kb.4d.com/DLTN/TN/2023/23-08_4DtoExcelViaRest.zip

## Proposition
ODBC has long been the standard way to connect Excel to 4D data, but it is becoming outdated compared to modern web-based alternatives and requires installing a driver. This note shows how to load live 4D Server data directly into Excel using 4D's REST API and Excel's built-in "From Web" data connector, no ODBC driver required.

## Key Points
- **Enabling the REST server:** Database Settings > Web Section > Web Features > "Expose as REST server" (disabled by default).
- **Per-table/field exposure:** each table and field has an "Expose as REST resource" property (also stored as `hide_in_REST` in catalog.4DCatalog) controlling REST visibility independent of other settings.
- **Access control:** either the classic 4D Users/Groups Read/Write setting, or a custom `On REST Authentication` database method (which takes precedence) that authenticates sessions and returns True/False.
- **Licensing:** REST sessions consume 4D Client connections on 4D Server; single-user Developer licenses allow up to 3 REST test connections.
- **REST URL conventions:** `/rest/` checks connectivity; `/rest/<Table>` fetches all entities; `$filter=<ORDA query>` scopes results using the same syntax as `dataClass.query()`.
- **Excel "From Web":** found under Data > Get & Transform Data > From Web (or Get Data > From Other Sources > From Web), it opens a Power Query Editor around a URL-based request.
- **Auto-generated Power Query formula:** `Json.Document(Web.Contents("http://host/rest/Table"))` requires no manual Power Query scripting for the basic case, though advanced formatting benefits from Power Query knowledge.
- **End-to-end workflow:** query 4D via REST → land in Power Query Editor → format/adjust into an Excel table → interact with it like any normal spreadsheet table (sort, filter, summarize).

## Featured Technology
- **4D REST server** — exposes 4D data classes/entities over HTTP for external consumption.
- **ORDA** — underlies the REST server's query semantics, including the `$filter` syntax.
- **On REST Authentication** — custom database method for controlling REST session access beyond Users/Groups.
- **Excel Power Query / "From Web"** — Excel's built-in connector and editor for pulling and shaping external web data sources.

## Best Practices Highlighted
1. Explicitly hide sensitive tables/fields from the REST server rather than relying on default full exposure.
2. Prefer a custom `On REST Authentication` method when finer-grained or custom login logic is needed beyond built-in Users/Groups access control.
3. Use `$filter` server-side to scope the entity selection instead of pulling entire tables into Excel and filtering client-side.

## Context / Positioning
Published as 4D continued to position its REST API as the forward-looking successor to ODBC for external tool integration, this note reflects a broader shift in the ecosystem toward REST/JSON-based data interchange and away from legacy driver-based connectivity for reporting and analytics tools like Excel.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
