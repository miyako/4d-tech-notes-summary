# Tech Note 09-23: Web Security 4D v11 SQL Component

**Author:** Atanas Atanassov, Technical Services Team Member, 4D Inc.
**Published:** June 11, 2009 | **Product/Version:** 4D SQL v11 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75797
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_22-26_(JUN)/09-23_WebSecurity.zip

## Proposition
This note explains 4D v11 SQL's web security architecture and shows how to build a custom web security realm on top of the On Web Authentication and On Web Connection database methods, complete with a reusable component and sample database.

## Key Points
- **Three pillars of 4D web security:** the On Web Authentication/On Web Connection database methods, the configured web folder, and method exposure via 4DACTION/4DSCRIPT/4DCGI.
- **On Web Authentication** receives URL, HTTP header/body, client/server IP, and (if password system is on) username/password; returns a Boolean to accept or reject the request.
- **Basic vs. Digest authentication:** Basic sends credentials as plain text (and can integrate with 4D's built-in password system via "Include 4D Password"); Digest (new in v11) encrypts credentials but is incompatible with 4D's own password system.
- Switching between Basic and Digest mode requires a **database restart**.
- Methods must be explicitly marked **"Available through 4DACTION, 4DMETHOD and 4DSCRIPT"** to be invocable from web requests.
- A bundled **component and sample database** demonstrate installing and configuring a fully custom security realm.

## Featured Technology
- On Web Authentication / On Web Connection database methods
- 4D built-in Users & Groups password system
- HTTP Basic and Digest authentication
- 4DACTION / 4DSCRIPT (web method invocation)
- Custom web security realm component

## Best Practices Highlighted
1. Rename the default HTML root folder away from "WebFolder" so all incoming requests are forced through On Web Authentication rather than bypassing it for existing static pages.
2. Use Digest mode when possible for stronger credential protection, understanding the tradeoff against 4D's built-in password integration.
3. Explicitly restrict which methods are web-callable via 4DACTION/4DSCRIPT rather than leaving all methods exposed by default.

## Context / Positioning
Published as foundational security guidance for the newly introduced 4D v11 SQL web features (including Digest authentication), this note gave developers both conceptual grounding and a ready-made component for implementing custom, business-specific web access control.

## Historical Commentary
**Status:** Partially Superseded

This note explained 4D v11 SQL's web request security model — On Web Authentication/On Web Connection hooks, Basic vs. Digest authentication, and 4D's built-in password system — and provided a component for building a custom security realm. The fundamental request-authentication hooks described are still present in 4D's classic web server today, so the concepts remain broadly applicable.

However, the overall approach reflects a page/URL-oriented classic web server security model that has been complemented since by REST/ORDA's privilege and session-token based security, which is the more common approach for modern API-driven 4D web and mobile clients.
