# Tech Note: Using LDAP with 4D

- **Asset ID:** 25595
- **Tech Note #:** 02-54
- **Published:** November 30, 2002
- **Product / Version:** 4D Open 6.8
- **Platform:** Mac
- **Author:** Christian Cypert
- **Page URL:** https://kb.4d.com/assetid=25595
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_51-55_(NOV)/02-54_Using_LDAP_with_4D.hqx

## Overview

Christian Cypert explains how to build a custom compiled 4D plug-in that authenticates a user against an LDAP directory server, at a time (4D 6.8, 2002) before 4D had any native LDAP support. The note covers LDAP fundamentals (directories/entries as analogs of 4D tables/fields, and Distinguished Names such as `username=Christian Cypert, c=US` used to locate an entry), then walks through scaffolding a new plug-in command (`ldap_Authentication`) with the 4D Plug-in Wizard, including its six parameters (port, server address, username, password, security type, return code). It documents the C-level implementation using the OpenLDAP client library -- `ldap_init`/`ldap_sslinit` to open a session, `ldap_simple_bind_s` to authenticate by binding with a constructed DN, and `ldap_unbind_s` to close the connection -- and supplies downloadable Mac (CodeWarrior) and Windows (Visual C++) plug-in project source.

## Key Points

- Frames LDAP concepts for 4D developers: an LDAP 'directory' maps to a 4D table and its 'entries' map to fields; common LDAP operations are searching, adding/updating/deleting entries, and renaming entries.
- Explains Distinguished Names (DNs) as the string used to locate/authenticate an entry, e.g. `username=Christian Cypert, c=US`, noting many servers instead use Common Name (`cn=`), and that the DN format must be adapted to the target LDAP server's schema.
- Uses the 4D Plug-in Wizard to scaffold a new 'LDAP Log-in' theme and an `ldap_Authentication` command with parameters PortNum, Ldap_Addr, Username, Password, SecurityType, and a Return Type (0=valid user, 1 otherwise).
- Details the required C build setup: include `LDAP.h` from the OpenLDAP headers folder, link against `WLDAP32.lib` on Windows (from the Microsoft Platform SDK) or a Netscape-provided library on Mac.
- Documents the four-step LDAP client flow in C: `ldap_init`/`ldap_sslinit(host, port, 1)` to open a session (SSL or non-SSL), build the DN with `sprintf(dn, "username=%s, c=US", UserName)`, call `ldap_simple_bind_s(ld, dn, Password)` to authenticate (returns `LDAP_SUCCESS` on success), then `ldap_unbind_s(ld)` to close and free the connection.
- Provides full downloadable Macintosh (CodeWarrior Pro8) and Windows (Visual C++ v6) plug-in project source (ldap4D.c/ldap4D.h) plus a compiled plug-in and a sample 4D database method calling it, along with links to OpenLDAP, Netscape, and Microsoft LDAP documentation.

## Featured Technology

- LDAP (Lightweight Directory Access Protocol)
- 4D Plug-in Wizard
- ldap_init / ldap_simple_bind_s / ldap_unbind_s (OpenLDAP C API)
- Distinguished Names (DN)
- Custom 4D plug-in command (ldap_Authentication)
- OpenLDAP / WLDAP32.lib libraries

## Historical Commentary

**Status:** superseded

Christian Cypert (billed as 4D & WebSTAR Plug-in Evangelist) shows how to build a custom compiled 4D plug-in from scratch, using the 4D Plug-in Wizard and the OpenLDAP C client API (ldap_init, ldap_simple_bind_s, ldap_unbind_s), to authenticate a 4D user against an LDAP directory by binding with a constructed Distinguished Name. LDAP itself remains a widely deployed enterprise directory protocol, so the underlying authentication need is still real, but building a bespoke compiled plug-in to speak LDAP is now unnecessary: 4D has since added native LDAP support directly in the 4D language, and many modern applications favor SSO/OAuth-based identity providers over direct LDAP binds altogether.

References to newer/updated information:
- 4D has since added native LDAP commands directly in the 4D language (LDAP LOGIN and related commands), removing the need to hand-write a compiled C plug-in as described in this note
- Many modern applications now favor SSO/OAuth-based identity providers over direct LDAP bind authentication, though LDAP remains in wide enterprise use
