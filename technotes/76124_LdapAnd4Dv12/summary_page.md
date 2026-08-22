# Tech Note 10-20: LDAP and 4D v12

**Author:** Jesse Pina, Technical Services Team Member, 4D Inc.
**Published:** June 29, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76124
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_17-20_(JUN)/10-20_LDAP_and_4D v12.zip

## Proposition
This Tech Note introduces LDAP directory concepts and shows how 4D v12 developers can use the version's new PHP integration to authenticate users and read/write entries against an LDAP directory (such as Active Directory), most commonly to implement a shared/centralized password system.

## Key Points
- **LDAP background:** a standards-based, cross-platform protocol for accessing hierarchical "directory" databases, commonly used for centralized user/credential storage (e.g. Active Directory).
- **No native LDAP support in 4D v12** — access is achieved entirely through the new PHP Execute command calling into PHP's built-in LDAP module.
- **Reusable wrapper syntax** is shown for calling PHP functions with parameters and using PHP GET FULL RESPONSE to extract error details on failure.
- **Shared password system example:** authenticate a username/password against an LDAP directory (Active Directory in the sample), configured via an [LDAP_Preferences] table and login dialog.
- **True single sign-on is not achievable** from 4D/PHP alone since there's no way to read an already-authenticated OS session credential — only password-sharing (with user re-entry) is demonstrated.
- **Second example** covers reading and writing LDAP entries/attributes directly.

## Featured Technology
- PHP Execute (4D v12's PHP integration)
- PHP LDAP module
- LDAP directory authentication (e.g. Active Directory)
- PHP GET FULL RESPONSE for error handling
- [LDAP_Preferences] table-driven server configuration

## Best Practices Highlighted
1. Centralize error handling using PHP GET FULL RESPONSE rather than inspecting raw PHP error codes.
2. Store LDAP server connection settings (IP, port, domain) in a dedicated preferences table rather than hard-coding them.
3. Separate credential validation (achievable) from true single sign-on (not achievable without OS-level integration).

## Context / Positioning
Published shortly after 4D v12 introduced PHP scripting support, this note showcased a headline new capability (PHP integration) by solving a very common enterprise need — centralized authentication against directory services like Active Directory.

## Historical Commentary
**Status:** Partially Superseded

This note leans on 4D v12's newly-introduced PHP Execute bridge to reach the PHP LDAP module, since 4D itself had no native LDAP or Active Directory commands at the time. That PHP-bridge approach is dated and clunky by modern standards, but LDAP/AD authentication remains a common integration need.

Today it would more likely be handled via a compiled plugin, a REST-based identity provider/SSO integration, or a scripted external process, rather than shelling out through 4D's PHP interpreter bridge; a later 4D Tech Note on "SSO with LDAP" (asset 77397) revisits this space with more current techniques.
