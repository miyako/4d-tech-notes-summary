# Tech Note 20-20: 4D REST API: Connecting 4D with ReactJS

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** October 26, 2020 | **Product/Version:** 4D Server v18 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78577
**Download:** https://kb.4d.com/DLTN/TN/2020/20-20_4DRESTwithReactJS.zip

## Proposition
4D's v18 REST server lets developers expose a 4D database as a full HTTP/REST backend for any frontend technology. This Tech Note builds a small ReactJS reading app (Edgar Allan Poe short stories) against a 4D REST/ORDA backend to demonstrate login/session handling, entity/attribute-level data retrieval including images, and calling custom server-side logic via Entity Selection Class functions.

## Key Points
- **Database exposure**: enable "Expose as REST server" and configure CORS (wildcard domain for dev) in Structure Settings > Web tab.
- **Session-based login**: `On REST Authentication` database method validates `username-4D`/`password-4D` headers via `Validate password`; the returned session cookie must be resent (`credentials: 'include'`) to avoid burning extra license connections.
- **Entity/attribute REST calls**: `/rest/{dataClass}({key})/{attr1,attr2,...}` fetches specific fields for a specific entity.
- **Image retrieval pattern**: `?$imageformat=best&$version=N&$expand=pic` returns an image attribute whose URL is nested at `__deferred.uri`.
- **Entity Selection Class functions**: a custom `StoriesSelection` class extending the Stories entity selection exposes a `getInfo()` function callable via POST at `/rest/Stories/getInfo/`, returning a clean, minimal JSON shape instead of the verbose default Dataclass response.
- **Server-side filtering**: appending `?$filter='category=Horror'` narrows the entity selection before the class function runs.
- **License/connection awareness**: every open REST session consumes one client connection; the same user logging in from multiple browsers consumes multiple connections.

## Featured Technology
- 4D REST Server (v18)
- On REST Authentication database method
- CORS configuration in Structure Settings
- REST Dataclass API with attribute/entity filtering and image expansion
- Entity Selection Class functions exposed as POST endpoints
- ReactJS, fetch(), create-react-app, material-ui templates

## Best Practices Highlighted
1. Always include `credentials: 'include'` on cross-origin fetch calls so the session cookie is reused instead of opening a new (license-consuming) session each request.
2. Prefer Entity Selection Class functions over raw Dataclass calls when you need a clean, purpose-built JSON shape for the frontend.
3. Use `$filter` to push filtering logic to the server/entity-selection layer rather than fetching everything and filtering client-side.

## Context / Positioning
Published shortly after 4D v18's REST server matured, this note is part of a wave of Tech Notes showing 4D paired with popular JavaScript frameworks (React here, Angular in a companion note), reinforcing 4D's positioning as a capable REST/ORDA backend usable independently of the classic 4D client — a key step in 4D's strategy to stay relevant as web and SPA frontends became the default choice for new application UIs.

## Historical Commentary
**Status:** Still relevant

The core 4D-side architecture shown here — REST server exposure, `On REST Authentication` session login, Dataclass/attribute REST endpoints, and ORDA Entity Selection Class functions callable via POST with `$filter`/`$expand` — remains 4D's current, standard way to build a REST/ORDA backend, and is not superseded by anything newer; this pattern is still exactly how developers integrate 4D with modern JS frameworks today. The one part that has aged is the React tooling: `create-react-app`, used here to scaffold the frontend, was deprecated by the React team in 2023 in favor of Vite or full frameworks like Next.js/Remix, so a developer following this note today should substitute a current React scaffolding tool while keeping the 4D-side REST integration guidance intact.
