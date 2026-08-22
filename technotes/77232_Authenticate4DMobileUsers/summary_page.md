# Tech Note 15-04: Authenticate 4D Mobile Users in 4D and Wakanda

**Author:** Xiang Liu, Technical Services Team Member, 4D Inc.
**Published:** February 9, 2015 | **Product/Version:** 4D v14 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77232
**Download:** https://kb.4d.com/DLTN/TN/2015/15-04_Auth4DMobileUser.zip

## Proposition
This Tech Note explains how to secure the original 4D Mobile architecture — in which a separate Wakanda Enterprise Server bridges 4D Server to mobile/web clients — by walking through automatic and custom authentication both on the 4D side (4D passwords, a custom `On 4D Mobile Authentication` database method) and the Wakanda side (built-in Directory, and a custom Login Listener function), each with worked examples built on 4D v14 R4 and Wakanda Enterprise 9.

## Key Points
- **Bridge architecture:** Wakanda Enterprise Server connects to 4D Server and receives a session ticket used for all subsequent 4D Mobile client requests.
- **Automatic authentication in 4D:** reuses existing 4D password/group access control so no extra security layer is needed when simply adding 4D Mobile to an existing 4D app.
- **Manual/custom authentication in 4D:** a new `On 4D Mobile Authentication` database method lets developers validate credentials against a custom user table or via `Validate Password`.
- **Wakanda Directory:** a built-in user/group directory supporting Basic and Digest authentication modes plus a ready-made login widget.
- **Wakanda Login Listener:** a fully custom JavaScript authentication function, enabling verification against an arbitrary Wakanda data class.
- **Guidance on when to use which approach:** reuse-existing-4D-security vs. fully custom Wakanda-side authentication, depending on whether the app is new or being extended.

## Featured Technology
- 4D Mobile (Wakanda-based)
- 4D password-based authentication
- Wakanda Directory
- Wakanda Login Listener
- Basic/Digest HTTP authentication

## Context / Positioning
From 2015 (4D v14 R5), this note covers the very first generation of "4D Mobile," which actually depended on 4D's sibling product Wakanda (a separate JS/HTML5 platform) rather than being a native 4D feature. This predates the native 4D Mobile App framework, ORDA, and REST-first web/mobile architectures that came later.

## Historical Commentary
**Status:** Obsolete

This is one of the more thoroughly obsolete notes in the archive: 4D discontinued Wakanda entirely, and "4D Mobile" was subsequently rebuilt as a native on-device app framework (later itself phased down in favor of ORDA/REST + Qodly web app patterns). None of the Wakanda Directory, Login Listener, or bridge-server mechanics described here exist in current 4D products.

The only durable takeaway is conceptual: separating authentication concerns (built-in vs. custom) and issuing session tokens to mobile/web clients — ideas that carried forward into 4D's later REST/ORDA session and token-based authentication model, just implemented completely differently.
