# Tech Note 09-40: Web Account Registration

**Author:** Tom Fitch, Technical Services Team Member, 4D Inc.
**Published:** October 29, 2009 | **Product/Version:** 4D v11.4 SQL | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75932
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_38-40_(OCT)/09-40_WebAccountRegistration.zip

## Proposition
Provides a drop-in Web Account Component (WAC) that adds self-service signup, password-change, and login validation to any 4D web application, complete with SMTP confirmation emails and an administration GUI.

## Key Points
- **Motivation**: modeled on real-world account systems like Yahoo!'s, used to gate features, personalize user data, and build an email list.
- **Installation**: copy the `WebAccount_1.0.4dbase` component, `4D InternetCommands`/`4D Pack` plug-ins, and `signup.html`/`changepwd.html` pages into the host database, then wire `WAC_Initialize`/`WAC_Shutdown`/`WAC_IsOnWebConn` into the On Startup, On Exit, and On Web Connection database methods.
- **Settings GUI** covers Web Server setup (homepage URL, post-action messages), SMTP server setup (host, reply-to, optional auth credentials), Email Settings (subject/body/signature with username/password placeholders and a preview), and a User Administration list (accounts, passwords, created/last-login dates).
- **Five public methods**: `WAC_Initialize`, `WAC_IsOnWebConn` (URL routing + redirect), `WAC_Settings` (GUI), `WAC_Shutdown` (persist to disk), and `WAC_ValidateAccount` (returns a unique user ID or blank string).
- **URL routing**: `WAC_IsOnWebConn` recognizes `/wac/signup` and `/wac/changepwd` requests from the bundled HTML pages' JavaScript (`WacSignup`/`WacChangePassword` via a `makeCall` XHR helper), performs the action, and redirects per a configurable URL/path.
- **Storage**: all account and settings data is persisted in XML files outside the 4D data file (for easy import/inspection), not in database tables.

## Featured Technology
- Web Account Component (WAC) — built 4D component for account signup/login
- 4D classic Web Server / On Web Connection database method
- 4D Internet Commands plug-in (SMTP email sending)
- XML-based settings/user storage outside the data file
- Plain HTML/JavaScript signup and change-password forms

## Best Practices Highlighted
1. Package reusable server-side account logic as a compiled component with a clear, small public method surface (five entry points).
2. Centralize URL-based routing decisions in one method (`WAC_IsOnWebConn`) rather than scattering conditionals through the On Web Connection method.
3. Keep configuration (SMTP, messages, redirects) in an editable settings store separate from application code, with a GUI for non-developers to adjust it.

## Context / Positioning
Published as a practical, reusable building block for 4D's classic Web Server model, addressing a need — self-service account creation — common to essentially every consumer-facing website of the era, packaged so 4D developers wouldn't need to build the signup/login plumbing from scratch.

## Historical Commentary
**Status:** Partially Superseded

The underlying need — self-service account signup, password reset, and login validation for a web app — is timeless, and the component's overall shape (initialize/shutdown lifecycle, a settings GUI, URL-based routing) is a reasonable design for its era. However, the implementation is built entirely on 4D's original CGI-like classic Web Server and On Web Connection routing model, and persists data in flat XML files outside the data file rather than in structured tables.

A modern 4D web application would instead use 4D's built-in REST server with ORDA entities and session-based authentication (available since v16+) rather than hand-rolled URL parsing in On Web Connection, and would store user/account data as ORDA data model entities. The note also shows no evidence of salted password hashing, which would be considered a security gap by current standards; a contemporary rebuild should add proper credential hashing regardless of the transport layer used.
