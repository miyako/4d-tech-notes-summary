# Tech Note 11-05: 4D Credentials Manager: JavaScript Injection Using Data from 4D

**Author:** Unknown
**Published:** February 24, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76266
**Download:** https://kb.4d.com/fftp://ftp.4d.com/ACI_TECHNICAL_NOTES/TN_2011/11-05_4D_Credentials_Manager.zip

## Proposition
This note explores taking 4D-stored data and injecting it directly into existing third-party websites via JavaScript, using a 4D Web Area's full control over browser-rendered content. The illustrative use case is a credentials/password manager: 4D holds login data, and JavaScript injected into the target site's page fills in credential fields either manually or automatically. The note is explicit that this technique requires the developer to think like a web developer — identifying what to inject and where — and provides step-by-step instructions plus an example database implementing the password-manager scenario. Note: only the KB page teaser text was available for this summary; the full PDF could not be retrieved.

## Key Points
- Builds on prior 4D Web Area Tech Notes but goes beyond simple public-API input/output mash-ups.
- Uses a 4D Web Area's full control over rendered browser content to inject custom JavaScript into arbitrary websites.
- Illustrative use case: a credentials/password manager that reads data from 4D and fills login fields on any website, manually or automatically.
- Explicitly requires web developer skills (JavaScript, knowing what/where to inject).
- Provides step-by-step instructions and an example database (per teaser; full technical detail unavailable).

## Featured Technology
- 4D Web Area with JavaScript injection
- 4D data feeding a browser-based credentials/password manager
- Cross-site JavaScript automation of form field fill-in

## Best Practices Highlighted
- Treat Web Area JavaScript injection as a web development task requiring JS/DOM knowledge, not just 4D scripting

## Context / Positioning
Published in 2011 to showcase creative, advanced uses of 4D Web Areas beyond simple API mashups, at a time when embedding browser control directly in a 4D form was a novel integration technique.

## Historical Commentary
**Status:** Obsolete

Injecting credentials via JavaScript into arbitrary third-party websites is a technique modern browsers and password managers have specifically hardened against (autofill protections, Content Security Policy, same-origin restrictions), and building a custom credentials manager this way would be considered a security anti-pattern today. The underlying 4D Web Area JavaScript-injection mechanism itself still exists, but this specific application is obsolete both for security reasons and because dedicated, vetted password managers (browser-native or third-party) now fill this role far better than a custom 4D solution.
