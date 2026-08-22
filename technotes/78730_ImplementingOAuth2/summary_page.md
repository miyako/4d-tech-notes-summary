# Tech Note 21-11: Implementing OAuth2 in 4D

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** June 21, 2021 | **Product/Version:** 4D v18 R6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78730
**Download:** https://kb.4d.com/DLTN/TN/2021/21-11_OAuth2.zip

## Proposition
OAuth 2.0 lets an app authenticate a user against a trusted third-party server (e.g. Google) without ever handling or storing the user's password. This note demonstrates implementing the full authorization-code grant flow by hand in 4D and using the resulting access token to authenticate Gmail SMTP sending.

## Key Points
- **Client secrets setup:** create a Google Cloud OAuth client ("installed" app type), producing a `client_secrets.json` with `client_id`, `client_secret`, and `redirect_uri`.
- **Authorization request:** build the auth URL from the JSON config (`JSON Parse`) and open it with `OPEN URL(...; *)` for the user to grant consent in a browser.
- **Capturing the code:** the redirect hits 4D's own web server; `On Web Connection` uses `WEB GET VARIABLES` to extract the `code` parameter and stores it via an ORDA `OAuth2` entity.
- **Token exchange:** a raw `HTTP Request` POST (`application/x-www-form-urlencoded`) to Google's token endpoint trades the auth code for an access token + refresh token pair.
- **Using the token:** `SMTP New transporter` accepts `authenticationMode: SMTP authentication OAUTH2` and `accessTokenOAuth2`, letting mail be sent without a stored password.
- **Token refresh:** access tokens expire in ~1 hour; a second POST with `grant_type=refresh_token` obtains a new one without re-prompting the user.
- **ORDA as token storage:** the OAuth2 dataclass persists auth code and token data across sessions using standard entity `.save()` calls.

## Featured Technology
- OAuth 2.0 authorization-code grant flow
- `HTTP Request`, `HTTP AUTHENTICATE`, `JSON Parse`
- `SMTP New transporter` (OAuth2 authentication mode)
- 4D web server / `On Web Connection`, `WEB GET VARIABLES`
- ORDA entities for token persistence

## Best Practices Highlighted
1. Never store the end user's raw password — use OAuth2 delegated authentication for third-party services that support it.
2. Persist and refresh tokens via ORDA rather than re-prompting users for consent every session.
3. Use 4D's own web server as the OAuth redirect target to avoid needing an external redirect handler.

## Context / Positioning
Published alongside 4D's broader push toward native SMTP/mail Transporter commands (see the mailing tech note in this same batch), this note shows 4D positioning itself as capable of implementing industry-standard security protocols using only native HTTP/JSON/web-server primitives, without external libraries.

## Historical Commentary
**Status:** Partially superseded

The general OAuth2 authorization-code flow shown here (manual client_secrets handling, browser-based consent, raw HTTP POST token exchange, ORDA-based token storage) is still a valid, functionally correct pattern for any OAuth2-protected API and hasn't been replaced by a built-in 4D command. However, for the specific mail use case this note leads with, 4D has since built out first-class OAuth2 support directly in `SMTP New transporter` (already previewed at the very end of this note), which considerably reduces the amount of hand-rolled plumbing needed for Gmail/Office365 SMTP authentication today. A developer building OAuth2-secured mail sending now would rely more heavily on that native support and reserve the manual flow shown here for non-mail REST APIs.
