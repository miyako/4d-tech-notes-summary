# Tech Note 15-20: Single Sign On with Lightweight Directory Access Protocol

**Author:** Tai BUI, Technical Services Engineer, 4D Inc.
**Published:** October 27, 2015 | **Product/Version:** 4D v15 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77397
**Download:** https://kb.4d.com/DLTN/TN/2015/15-20_SSO_with_LDAP.zip

## Proposition
4D v15 introduced native LDAP commands allowing a database to connect to and search a distributed directory server. This note explains LDAP basics and demonstrates using the new commands to implement a simple Single Sign On (SSO) feature that authenticates a user once and then auto-launches other applications with stored credentials.

## Key Points
- **New LDAP command theme:** covers `LDAP LOGIN`, `LDAP LOGOUT`, `LDAP Search`, and `LDAP SEARCH ALL`, including parameters for connection URL, login identity type (DN/CN/email/SAM-Account-Name), password digest, search filter, scope, and attribute formatting.
- **LDAP fundamentals explained:** entries, attributes, schemas, Distinguished Name (DN) vs. Relative Distinguished Name (RDN), illustrated with a sample org directory tree.
- **SSO defined:** reduces "password fatigue" for end users and IT support burden by centralizing authentication.
- **Two SSO patterns described:** (1) local software application SSO — auto-launching apps like Skype/FileZilla with credentials pulled from LDAP; (2) online/cloud service SSO via stored certificates.
- **Hands-on setup guide:** walks through installing Apache Directory Studio, creating a local LDAP server, and loading custom schema/user entries via generated `.ldif` files.
- **Credential handling caveat:** the author explicitly flags that the demo does not encrypt stored credentials, presenting it as a proof-of-concept rather than a production-ready security solution.
- **`LAUNCH EXTERNAL PROCESS`** is used to programmatically start and log into external desktop applications using retrieved LDAP attributes.

## Featured Technology
- `LDAP LOGIN` / `LDAP LOGOUT`
- `LDAP Search` / `LDAP SEARCH ALL`
- Apache Directory Studio (test LDAP server)
- `LAUNCH EXTERNAL PROCESS`

## Best Practices Highlighted
1. Use case-sensitive, precise attribute names when querying LDAP to avoid unexpected empty results.
2. Wrap `LDAP LOGOUT` calls with error handling (`ON ERR CALL`) since it errors if no connection exists.
3. Do not store plaintext credentials in a directory without an accompanying encryption/management strategy.

## Context / Positioning
This is a classic Design Mode-era note (v15, 2015) that predates ORDA, Project Mode, and modern web-standard SSO protocols. LDAP itself was (and remains) a mature enterprise directory standard, so this note represents 4D catching up to a long-standing integration need rather than introducing something novel to the broader industry.

## Historical Commentary
**Status:** Still relevant (core LDAP commands); dated (SSO demo pattern)

The LDAP command set introduced here has remained a stable, supported part of the 4D language for a decade, and LDAP directories (Active Directory, OpenLDAP, etc.) are still commonplace in enterprises, so the fundamentals in this note hold up well. However, the specific SSO demonstration — storing per-application credentials in LDAP attributes and shelling out to `LAUNCH EXTERNAL PROCESS` to auto-login desktop apps — reflects a pre-modern approach to SSO that would now be handled via SAML, OAuth2, or OpenID Connect integrations rather than credential-replay scripting, and would likely raise security review flags in current practice.
