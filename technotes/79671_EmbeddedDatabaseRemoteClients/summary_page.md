# Tech Note 25-03: Embedded Database Structures with Built Remote Clients

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** March 27, 2025 | **Product/Version:** 4D v20 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79671
**Download:** https://kb.4d.com/DLTN/TN/2025/25-03_4DEmbeddedDB.zip

## Proposition
A built 4D Remote Client normally can't run any custom code until it successfully connects to its 4D Server — a hard limitation for scenarios like connection portals, pre-connection checks, or automatic failover. This note explains 4D's embedded database feature, which lets a compiled standalone structure run first inside the built client, executing code independently before any server connection is made.

## Key Points
- **Two structures are required:** A client-server structure and a separate standalone structure (compiled to .4DC/.4DZ) that gets embedded into the built Remote Client.
- **Manual Build XML configuration:** The embedding option isn't exposed in the Build Wizard UI; developers must hand-edit the generated buildApp.4DSettings XML to add DatabaseToEmbedInClientMacFolder or DatabaseToEmbedInClientWinFolder under `<CS>`.
- **No data file needed for the embedded DB:** The embedded standalone structure runs without a data file and transitions to the server via OPEN DATABASE with a .4dlink file.
- **Plugin duplication requirement:** Plugins (like 4D Internet Commands) must be present both in the embedded database (to compile) and separately added to the built client (since client-server plugin loading normally relies on server-side caching).
- **Automatic failover demo:** The embedded database scans numbered .4dlink files in a Resources/Servers folder in priority order, UDP-pings each with 4D Internet Commands, and connects to the first available server.
- **Fallback and error handling:** If no configured server is reachable, the demo attempts the default port 19813 before displaying an error.
- **Single-structure approach discouraged:** Using one structure for both standalone and client-server roles increases client footprint unnecessarily; separate structures are recommended.
- **Build settings for Client/Server:** Standard Build Wizard tabs configure server/client build settings and destination paths, generated first via "Save settings" before the manual XML edit.

## Featured Technology
- **Embedded compiled standalone database** — a .4DC/.4DZ structure merged into a built Remote Client via Build XML.
- **Build XML (buildApp.4DSettings)** — manually edited to add the DatabaseToEmbedInClient*Folder keys.
- **OPEN DATABASE** — command used to transition from the embedded standalone structure to the 4D Server via a .4dlink file.
- **.4dlink files** — server address/priority definitions parsed to determine connection order.
- **4D Internet Commands plugin** — used for UDP-based server availability checks (pingServer).

## Best Practices Highlighted
1. Keep standalone and client-server structures separate rather than merging both roles into one structure.
2. Always add required plugins to both the embedded database and the built client package.
3. Use sorted numeric .4dlink filenames (1.4dlink, 2.4dlink, ...) to define clear failover priority.

## Context / Positioning
Published as part of 4D's continued investment in robust client-server deployment tooling, this note extends the platform's flexibility for enterprise-grade, high-availability deployments — an increasingly relevant capability as more 4D applications are deployed remotely (e.g., home office scenarios) where network resilience and graceful failover matter.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
