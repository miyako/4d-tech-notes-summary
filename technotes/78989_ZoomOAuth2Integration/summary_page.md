# Tech Note 22-16: Connecting 4D and Zoom via OAuth 2.0

**Author:** Marouane AIT SALAH, Technical Services Engineer, 4D Morocco
**Published:** August 22, 2022 | **Product/Version:** 4D v19 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78989
**Download:** https://kb.4d.com/DLTN/TN/2022/22-16_OAuth2Zoom.zip

## Proposition
4D applications can authenticate against Zoom's developer API using 4D's built-in OAuth2 provider class (available since 18 R6), then use standard HTTP Get/HTTP Request calls to list, create, update, and delete Zoom meetings, including displaying them in a web-area calendar.

## Key Points
- **New OAuth2 provider($param)** is the core 4D class handling the OAuth 2.0 authorization-code flow against any provider, configured here with Zoom's authenticateURI/tokenURI endpoints.
- **$oAuth2.getToken() returns a bearer access token**, valid for one hour, which the note caches in a shared Storage.token object to avoid re-authenticating on every CRUD call.
- **Zoom Marketplace configuration is a prerequisite**: an account-level OAuth app, an allow-listed redirect URL, and explicit scopes (e.g. meeting:read:admin, meeting:read) must be granted before the 4D side can connect.
- **Meeting CRUD uses plain HTTP Get/HTTP Request** against Zoom's REST API, with POST/DELETE method constants for create/update and delete operations respectively.
- **A 401 response triggers re-authentication**, re-invoking the OAuth flow when the cached token has expired.
- **Meeting data is serialized to Meetings.json** and rendered via the third-party 'fullcalendar' JS library inside a 4D web area for a richer calendar UI.
- **WA SET EXTERNAL LINKS FILTERS** permits Zoom's embedded meeting-join links to open externally from the web area.

## Featured Technology
- OAuth2 provider class (New OAuth2 provider, since 18 R6)
- HTTP Get / HTTP Request commands
- Zoom Marketplace OAuth apps
- Shared object token storage (Storage)
- WA SET EXTERNAL LINKS FILTERS
- fullcalendar.js web area integration

## Best Practices Highlighted
1. Cache the OAuth access token in a shared object rather than re-requesting it for every API call, and re-authenticate only on a 401 response.
2. Request only the minimal Zoom scopes actually needed by the application (e.g. meeting:read vs. meeting:read:admin) per operation.

## Context / Positioning
Published under 4D v19 R5 (August 2022), this note showcases 4D's OAuth2 provider class — introduced in 18 R6 — as a general-purpose bridge to third-party identity providers and REST APIs, positioning 4D as capable of integrating with mainstream SaaS platforms using the same modern auth protocols those platforms expect.

## Historical Commentary
**Status:** partially superseded

4D's OAuth2 provider class itself remains current and is still the standard way to perform OAuth 2.0 flows from 4D. However, Zoom's own developer platform has evolved substantially since 2022: Zoom has pushed developers toward 'Server-to-Server OAuth' apps (client-credentials, no user-facing redirect) for account-level integrations like this one, and has periodically reorganized its Marketplace app-creation flow and scope model. The specific Zoom Marketplace screenshots, scope names, and app-type selection steps in this note should be expected to differ from Zoom's current developer console, even though the 4D-side OAuth2 provider code pattern is still valid.
