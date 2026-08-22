# Tech Note 26-05: Sentinel: A Multi-Layer Web Security Architecture Using HTTP Request Handlers and HTTP Rules

**Author:** Anouar Moustarih, Quality Support Engineer, 4D Morocco
**Published:** May 28, 2026 | **Product/Version:** 4D v21 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=80020
**Download:** https://kb.4d.com/TN/2026/26-05_MultiLayerWebSecurity.zip

## Proposition
Modern web servers face brute force, volumetric DoS, injection, and reconnaissance scanning
simultaneously; handling each ad-hoc leads to scattered, hard-to-audit code. This note shows how
two declarative 4D v21.0 LTS primitives — HTTP Request Handlers and HTTP Rules — can serve as the
structural foundation for a single, ordered, auditable defense pipeline, demonstrated end-to-end
in a demo application called Sentinel.

## Key Points
- **Eleven-gate ordered pipeline.** `DoSGuard.authenticateRequest` runs cheapest/most-decisive
  checks first (master switch, CPU/traffic panic flags, header size, allowlist, blocklist) and
  expensive checks last (honeypot match, regex WAF, per-IP then global rate limits); the first
  gate producing a verdict stops evaluation.
- **Declarative routing via `HTTPHandlers.json`.** Each entry binds a `regexPattern`, `verbs`,
  `class`, and `method` (e.g. `{"regexPattern": "^/admin/status$", "verbs": "GET", "class":
  "Sentinel", "method": "handleStatus"}`); the array is evaluated in order, first match wins,
  unmatched URLs fall through to `On Web Connection`. About 40 routes are registered this way.
- **Header policy via `HTTPRules.json`.** A regex selector maps to a `responseHeaders` bag (e.g. a
  catch-all `^/.*$` rule adding `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`,
  `Permissions-Policy`, `X-XSS-Protection`), applied without touching handler code, and both files
  hot-reload from disk with no server restart.
- **Sonar IDS/IPS scoring.** Each inbound request accumulates a 0–100 score from additive
  behavioral signals; scores ≥80 route to a one-hour-block "sniper" queue (IPS behavior), lower
  scores archive to a "drone" queue for later pattern correlation (IDS behavior).
- **Fifteen shared singleton classes with discrete ownership.** `DoSGuard` (pipeline),
  `SentinelAuth` (login/lockout), `IPManager` (allow/blocklists), `ConfigManager`, `RequestLogger`
  (2,000-entry ring buffer), `AlertManager` (threshold alerts with 60s cooldown),
  `ProcessOrchestrator` (worker lifecycle), and others each own one responsibility.
- **Background workers drive time-based defenses.** `CPUMonitor_Worker` (1s cadence) flips the CPU
  panic flag; `PanicWatchdog_Worker` (5s) auto-lifts traffic panic; `Sonar_Sniper_Worker` (1s)
  drains and blocks high-score IPs; `HoneypotSweeper_Worker` (60s) expires 24-hour honeypot bans.
- **Authentication with brute-force lockout.** `SentinelAuth` validates a bcrypt-hashed static
  passphrase or a one-shot dynamic passphrase; five failed attempts in 15 minutes triggers a
  30-minute per-IP lockout, held in memory only.
- **Atomic-write persistence.** All runtime state (IP lists, config, sonar kill/archive logs)
  persists to JSON files under the project's Data folder using an atomic write pattern, avoiding
  partial writes on crash or concurrent access.

## Featured Technology
- **HTTP Request Handlers (`HTTPHandlers.json`)** — declarative regex-to-class-function URL
  routing, decoupled from business logic.
- **HTTP Rules (`HTTPRules.json`)** — declarative response-header injection by URL pattern.
- **`On Web Authentication` database method** — pipeline entry point run before route matching.
- **Regex-based WAF** (path traversal, SQLi, XSS, eval detection) inside `DoSGuard`.
- **`4D.Signal`** — used by `ProcessOrchestrator.sleep` for coordinated worker wake/shutdown.
- **bcrypt** — static passphrase hashing for `SentinelAuth`.
- **Vanilla-JavaScript dashboard** — live telemetry, defense toggles, and attack simulators.

## Best Practices Highlighted
1. *Order checks by cost* — run cheap, decisive gates (allowlist/blocklist) before expensive ones
   (WAF regex scanning, rate limiting) to minimize wasted CPU on requests that will be rejected
   anyway.
2. *Separate routing/policy from business logic* — HTTPHandlers.json and HTTPRules.json keep
   security concerns declarative and independently editable/hot-reloadable.
3. *Persist defense state atomically* — write IP lists and config via an atomic-write pattern so a
   crash mid-write can't corrupt the security configuration.
4. *Layer detection with prevention* — combine an IDS-style scoring/archival path with an
   IPS-style immediate-block path rather than choosing only one.

## Context / Positioning
Published for 4D v21.0 LTS (2026), this note showcases how 4D's newer declarative web-server
primitives (HTTP Request Handlers, HTTP Rules) can support serious, production-style security
architecture directly in 4D code, rather than requiring an external reverse proxy or WAF appliance
— part of a broader 2026 trend of Tech Notes demonstrating 4D's web/HTTP server maturity alongside
its AI Kit and ORDA modernization efforts.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
