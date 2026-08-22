# Tech Note 24-13: Managing Email and Folders with 4D NetKit

**Author:** Trina Nguyen, Technical Services Engineer, 4D Inc.
**Published:** November 21, 2024 | **Product/Version:** 4D v20 R6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79587
**Download:** https://kb.4d.com/DLTN/TN/2024/24-13_4DNetKit.zip

## Proposition
As the internet standardizes on OAuth 2.0 for secure authorization, 4D applications need an easy way to authenticate against third-party services like Gmail and Office365 without manually implementing token flows. 4D NetKit (introduced in 19R3) manages this authorization process, and this note shows how to register apps with Google/Microsoft and use NetKit to send, receive, and organize email programmatically.

## Key Points
- **OAuth 2.0 token model:** Access tokens authorize API calls and expire; refresh tokens (if enabled) silently renew access without requiring the user to re-authenticate via browser.
- **App registration is a prerequisite:** Both Google Cloud Console (OAuth consent screen, test users, client secrets, Gmail API enablement) and Microsoft Entra admin center registration must be completed before using NetKit.
- **OAuth2Provider object pattern:** A cs.NetKit.OAuth2Provider is constructed with name, permission ("signedIn"), clientId/clientSecret, redirectURI, and scope, then calls .getToken() to trigger the browser consent flow.
- **Built-in local web server for redirects:** In "signedIn" mode, NetKit runs a local server on the specified redirectURI port to intercept the provider's authorization response.
- **Unified mail API across providers:** cs.NetKit.Google and cs.NetKit.Office365 both expose a `.mail` namespace with send(), getMailIds()/getMails(), and delete() (permanent vs. trash-move).
- **Gmail label management:** createLabel(), getLabel(), updateLabel(), and update() with addLabelIds/removeLabelIds let developers organize Gmail messages programmatically.
- **Microsoft folder management:** getFolderList(), createFolder(), renameFolder(), deleteFolder(), and move() manage Office365 mail folders, with a caveat that Microsoft's "recoverable items" folder may prevent permanent deletion.
- **Version/licensing requirements:** Requires 4D 20 R6+ and a Web Application Expansion license to listen for and receive OAuth tokens.

## Featured Technology
- **4D NetKit** — 4D's OAuth 2.0 connection manager for third-party web service integration.
- **OAuth 2.0** — industry-standard authorization protocol using access/refresh tokens.
- **Google Gmail API** — used for send/receive/delete/label operations on Gmail accounts.
- **Microsoft Graph API** — used for send/receive/delete/folder operations on Office365 accounts.
- **cs.NetKit.OAuth2Provider / cs.NetKit.Google / cs.NetKit.Office365** — the core 4D NetKit classes driving authentication and mail operations.

## Best Practices Highlighted
1. Keep applications in Google's "testing" status during development, adding only intended test users, before undergoing verification for sensitive scopes like email access.
2. Reference the official 4D-NetKit GitHub repository and 4D blog posts (by Fabrice Mainguené) for more advanced examples and up-to-date class documentation.

## Context / Positioning
Published as cloud services increasingly mandate OAuth 2.0 over legacy username/password authentication, this note reflects 4D's investment in first-party, standards-compliant integration tooling (4D NetKit) so developers can connect business applications to major cloud email/productivity platforms without building custom OAuth infrastructure — part of 4D's broader push toward simplified cloud service interoperability.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
