# Tech Note 25-08: Integrating 4D with Notion: Creating Pages and Databases Using the Notion API

**Author:** Al Mahdi Bakkali, Quality Support Engineer, 4D Inc.
**Published:** August 29, 2025 | **Product/Version:** 4D v20 R9 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79812
**Download:** https://kb.4d.com/TN/2025/25-08_NotionAPIIntegration.zip

## Proposition
Notion is a popular collaborative workspace platform for project management and note-taking, but
its data typically lives separately from a business's core systems. This note shows how to bridge
4D and Notion using the Notion REST API and `4D.HTTPRequest`, so operational data captured or
generated in 4D (e.g. warehouse stock updates) can flow into Notion automatically for tracking,
collaboration, and analytics — illustrated with a real-time inventory-sync demo.

## Key Points
- **Internal Integration setup.** A Notion "Internal Integration" (versus "Public," meant for
  broad/shareable use) is created via the Notion integrations dashboard, then explicitly granted
  access to a target page/database, yielding an Internal Integration Secret used as a Bearer token.
- **Pages vs. databases.** A Notion database is a collection of pages; each page is analogous to a
  4D record, with its "properties" analogous to fields — a mental model essential before making
  any API calls.
- **ID extraction from share links.** Page/database IDs are 32-character hex strings embedded in a
  Notion "Copy Link" URL, reformatted to the standard 8-4-4-4-12 UUID form for use in API calls.
- **Required headers on every call.** `Content-Type: application/json`, `Authorization: Bearer
  <secret>`, and a required `Notion-Version` header pinning API compatibility.
- **Full CRUD via HTTPRequest.** Create (`POST /v1/pages` with `parent.database_id` +
  `properties`), update (`PATCH /v1/pages/{page_id}` with only changed properties — partial
  updates), read (`POST /v1/databases/{database_id}/query`, parsing each page's typed properties
  like `.select.name`, `.date.start`, `.number`), and delete-as-archive (`PATCH` with
  `archived: true`, since Notion has no hard-delete endpoint for pages).
- **Session credential caching via `Storage`.** Bearer token and database ID are requested once
  via `Request()` prompts at startup and cached in the shared `Storage` object for reuse across
  the session.
- **Type-mapped schema.** 4D field types map explicitly to Notion property types (text →
  Title, numeric → Number, date → Date), essential for correct two-way synchronization.
- **Status-code-driven error handling.** Success is any 2xx `$dbRequest.response.status`; 401
  signals bad/expired auth, 400 signals a schema mismatch, and 403 signals a permissions problem.

## Featured Technology
- **`4D.HTTPRequest`** — 4D's native class for making the Notion API calls (GET/POST/PATCH).
- **Notion API (Internal Integration)** — Bearer-token-authenticated REST endpoints for
  pages/databases.
- **`Storage` shared object** — session-scoped caching of the bearer token and database ID.
- **Qodly Studio** — companion low-code web app reusing the same 4D classes/business logic to
  extend the inventory workflow to a browser interface.

## Best Practices Highlighted
1. *Choose Internal vs. Public integration deliberately* — pick the scope matching whether the
   integration is for private internal use or broader shareable access.
2. *Cache session credentials once* — avoid re-prompting for bearer token/database ID by storing
   them in the shared `Storage` object at startup.
3. *Send only changed properties on update* — Notion's `PATCH` endpoint supports partial updates,
   simplifying update logic versus resending the full page payload.
4. *Check HTTP status codes explicitly* — distinguish auth (401), schema (400), and permission
   (403) failures rather than treating all non-2xx responses the same way.

## Context / Positioning
Published for 4D v20 R9 (2025), this note continues 4D's pattern of demonstrating its native
`HTTPRequest`-based integration capabilities against popular third-party SaaS platforms, and pairs
this with Qodly Studio to show how the same 4D business logic can be reused across both desktop
and web-app front ends — reflecting the platform's dual emphasis on external API connectivity and
web/low-code extensibility during this period.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
