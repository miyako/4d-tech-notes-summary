# Tech Note 19-15: Custom User Login

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** August 30, 2019 | **Product/Version:** 4D v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78310
**Download:** https://kb.4d.com/DLTN/TN/2019/19-15_CustomUserLogin.zip

## Proposition
4D's built-in login dialog cannot be customized for branding or business logic. This note shows how to build a fully custom login window on top of 4D's native Password System, using a no-password default user to run pre-login code.

## Key Points
- **Reasons for a custom login:** custom branding, custom messages, and business logic (e.g., logging failed attempts with IP address).
- **4D Password System is a prerequisite:** it gates Structure Design Access, the 4D Server Admin Window, the Runtime Explorer, Backup abort controls, and Plug-In license groups — all wide open if disabled.
- **Enabling it:** assign the Designer a password via the Toolbox GUI or `CHANGE PASSWORD("newPassword")`.
- **Default User trick:** create a password-less "default user" and set it in Database Settings > Security so the app auto-connects and can run developer code (including displaying the custom login form) before any real login.
- **Login validation flow:** `GET USER LIST` + `Find in array` to check the username exists, then `Validate password` to check credentials, then `CHANGE CURRENT USER` + `ACCEPT`.
- **Password field security:** use the `%password` font to mask input.
- **Cancel handling:** simply calls `QUIT 4D` to exit if the user doesn't log in.

## Featured Technology
- 4D Password System, Users/Groups (Toolbox)
- `CHANGE PASSWORD`, `GET USER LIST`, `Validate password`, `CHANGE CURRENT USER`
- Database Settings > Security (Default User)

## Best Practices Highlighted
1. Always enable the Password System in production databases — leaving it disabled grants everyone Designer-level access to sensitive features.
2. Use a password-less default user purely as a bootstrap mechanism, never as a real production account.
3. Validate credentials via `Validate password` before calling `CHANGE CURRENT USER`, rather than trusting user input directly.

## Context / Positioning
This note reflects an evergreen concern in 4D's classic desktop/client-server application model — first-impression UX and access control — rather than a new feature announcement, showing 4D's ongoing "practical recipes" series aimed at rounding out gaps in built-in UI customization for native forms-based applications.

## Historical Commentary
**Status:** Still relevant

The classic 4D Password/User/Group system, along with commands like `CHANGE PASSWORD`, `GET USER LIST`, `Validate password`, and `CHANGE CURRENT USER`, are unchanged in current 4D versions and this technique remains a valid way to build a custom login screen for native 4D Remote/Server or standalone apps. It's worth noting this note is scoped to classic desktop-style login; for modern web/ORDA/REST-based 4D applications, additional and different authentication mechanisms (session-based REST auth, OAuth2 flows) have since been documented separately and would be the more relevant approach for web app login rather than form-based desktop login.
