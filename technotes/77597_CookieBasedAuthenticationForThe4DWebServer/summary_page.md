# Tech Note 16-10: Cookie-Based Authentication for the 4D Web Server

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** August 11, 2016 | **Product/Version:** 4D v15.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77597
**Download:** https://kb.4d.com/DLTN/TN/2016/16-10_CookieBaseWebAuth.zip

## Proposition
This note presents a full DIY cookie-based login system for the 4D Web Server, addressing the customization and logout limitations of built-in Web Password (BASIC/DIGEST) authentication. It includes a sample Bootstrap-based site with user creation, Ajax validation, password management, and session invalidation.

## Key Points
- **Motivation:** built-in Web Password (BASIC/DIGEST) auth cannot customize the login UI and lacks a clean logout mechanism.
- **Built on Automatic Session Management:** leverages 4D's native HTTP session/cookie handling rather than reinventing session tracking.
- **Full user lifecycle:** includes user creation (with Ajax username-availability checks), account/profile updates, and salted password validation.
- **Session invalidation for remote logout:** demonstrates explicitly killing sessions so users can truly log out.
- **Password-protected pages:** shows how to gate specific web pages behind the custom authentication.
- **Bootstrap-based sample UI** demonstrates a realistic, styled login/registration flow.
- **Comparison section:** contrasts cookie-based auth against native HTTP Authentication trade-offs.

## Featured Technology
- 4D Web Server
- 4D Automatic Session Management
- HTTP cookies
- Ajax
- Bootstrap CSS framework
- Salted password hashing

## Best Practices Highlighted
1. Use salted password hashes rather than storing plaintext or unsalted hashes.
2. Provide explicit session invalidation logic to support real remote logout, not just cookie deletion.
3. Validate usernames asynchronously (Ajax) during registration to improve UX.

## Context / Positioning
This Tech Note was published in 2016, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Partially Superseded

The session/cookie mechanics and salted-password approach described here are still conceptually valid, but the broader context has shifted: modern 4D web development increasingly uses REST + ORDA with token-based or session-cookie auth patterns wired through 4D's built-in REST authentication, and front ends are more often built with modern JS frameworks than server-rendered Bootstrap pages. Developers today would likely reach for 4D's REST API session/authentication support rather than hand-rolling the entire flow shown here.
