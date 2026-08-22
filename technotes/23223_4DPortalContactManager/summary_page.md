# Tech Note 02-04: The 4D Portal Contact Manager

**Author:** Not specified in source document
**Published:** January 31, 2002 | **Product/Version:** 4D v6.8 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=23223
**Download:** https://kb.4d.com/ftp://ftp.4d.com/aci_technical_notes/2002/windows/tn_2002_01-04_(jan)/02-04_4d_portal_contact_mng.exe

## Overview
A detailed Tech Note walking through the Contact Manager portlet in 4D Portal, a compact, event-driven PIM-style module whose logic is concentrated almost entirely in a single dispatch method.

## Key Points
- Documents the Contact Manager portlet: a compact, PIM-style contact-storage module accessible via the Web.
- Deliberately kept small to be easy to understand, adapt, or move into a custom web application.
- Almost all portlet logic lives in a single event-driven method, CGI_ContactStart, dispatched via URL-encoded events.

## Featured Technology
- 4D Portal
- Contact Manager portlet
- Event-driven URL dispatch

## Historical Context
Part of 4D Portal's family of modular "portlets" (alongside Auctions and Postcard, both covered elsewhere in this batch), reflecting early-2000s web portal and PIM (Palm/Windows CE-era personal information management) design trends.

*Note: only the on-page teaser paragraph for this Tech Note could be recovered in this environment; the full PDF/example database is no longer accessible (old format/archive not reachable here), so this summary is necessarily based only on that short teaser text.*

## Historical Commentary
**Status:** Obsolete

4D Portal has been discontinued for many years, making this specific portlet implementation obsolete; the general event-driven, URL-dispatch architectural pattern it demonstrates (routing different logic based on a URL/event parameter) remains a valid and still widely used web application design pattern, even though the Palm/Windows CE PIM devices it was designed to complement are themselves long obsolete.
