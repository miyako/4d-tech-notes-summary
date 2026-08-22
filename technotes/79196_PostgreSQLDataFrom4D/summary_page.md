# Tech Note 23-09: Manipulating PostgreSQL Data from 4D

**Author:** EL BHIOUI Chaima, Technical Services Engineer, 4D Morocco.
**Published:** May 22, 2023 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79196
**Download:** https://kb.4d.com/DLTN/TN/2023/23-09_4DToPostgreSQLViaRest.zip

## Proposition
Businesses increasingly need to move data reliably between heterogeneous systems, and connecting 4D directly to a non-4D database like PostgreSQL isn't always straightforward. This note shows how to bridge 4D and PostgreSQL using REST, letting 4D read/write external relational data with standard HTTP requests instead of a native driver.

## Key Points
- **PostgREST as a bridge:** a standalone binary that auto-generates a REST API directly from a PostgreSQL schema, avoiding the need to hand-write a REST layer.
- **Environment setup:** PostgreSQL 14.7, Docker (used to spin up a containerized Postgres instance on port 5433), and PostgREST v10.1.2 must all be installed and configured together on macOS.
- **Shared library fix:** missing `libpq.so`/`.dylib` errors when running `postgrest` are resolved by copying the required libraries into `/usr/local/lib`.
- **Least-privilege role:** a dedicated PostgreSQL role with only select/insert/update/delete grants is created for the REST connection, instead of using the privileged `postgres` superuser role.
- **Configuration file:** PostgREST is launched with a `.cfg` config file (created by renaming a text file's extension) pointing at the target database and role.
- **4D HTTP Request drives CRUD:** all four operations — GET, POST, DELETE, PUT — are performed with 4D's `HTTP Request` command against the PostgREST-exposed table URL.
- **PostgREST filter syntax:** row-targeted operations (DELETE, PUT) use a query-string filter like `?id=eq.1` appended to the endpoint URL.
- **JSON handling:** request bodies are built with `JSON Parse`/`New object`, and responses are cleaned of brackets/newlines with `Replace string` before use.

## Featured Technology
- **PostgREST** — auto-generates a REST API from a PostgreSQL schema; the core bridge technology in this note.
- **HTTP Request** — 4D's native command for issuing GET/POST/PUT/DELETE calls to the REST endpoint.
- **PostgreSQL** — the external relational database being manipulated.
- **Docker** — used to run a portable, isolated PostgreSQL instance for the demo environment.
- **JSON Parse / JSON Stringify** — converts between 4D objects and the JSON payloads PostgREST expects/returns.

## Best Practices Highlighted
1. Create a dedicated, minimally-privileged database role for REST connections rather than exposing the superuser role.
2. Use PostgREST's URL filter syntax (`?field=eq.value`) to target specific rows for update/delete instead of fetching and filtering client-side.
3. Validate the PostgREST binary and shared library setup (`./postgrest -h`) before attempting any 4D-side HTTP calls.

## Context / Positioning
Published as part of 4D's continued emphasis on REST-based interoperability (alongside 4D's own REST server), this note shows 4D positioning itself as a flexible integration hub capable of talking to non-4D backends like PostgreSQL, reflecting broader industry trends toward REST/JSON as a lingua franca for cross-database data exchange.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
