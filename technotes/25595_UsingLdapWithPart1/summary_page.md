# Tech Note 02-54: Using LDAP with 4D

**Author:** Not specified in source document
**Published:** November 30, 2002 | **Product/Version:** 4D Open v6.8 | **Platform:** Mac
**Page:** https://kb.4d.com/assetid=25595
**Download:** https://kb.4d.com/DLTN/TN/2002/Windows/TN_2002_51-55_(NOV)/02-54_Using_LDAP_with_4D.exe

## Overview
Part I of a Tech Note series on integrating 4D with LDAP directory services, describing how to build a custom LDAP plug-in for user authentication.

## Key Points
- Motivated by growing enterprise LDAP adoption and the need to authenticate 4D users against it.
- Describes writing a custom LDAP plug-in for 4D, since native LDAP support did not exist at the time.
- Part I of a two-part series (Part II, also in this batch, goes deeper into LDAP technology and data organization).

## Featured Technology
- LDAP
- Custom plug-in authentication

## Historical Context
Written when LDAP was an emerging enterprise directory-service standard and 4D had no built-in LDAP support, requiring a custom plug-in; only the short teaser text for this note could be recovered here.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Superseded

LDAP remains a widely used, still-relevant directory-service protocol, but 4D has since gained more native networking/protocol capabilities that could reduce the need for a fully custom plug-in of the kind built here; modern applications also increasingly favor SSO/OAuth-based identity providers over direct LDAP integration, making this note's specific plug-in approach somewhat dated even as the underlying authentication need remains real.
