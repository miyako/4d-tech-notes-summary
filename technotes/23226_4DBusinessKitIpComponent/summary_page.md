# Tech Note: The 4D Business Kit IP Component

- **Asset ID:** 23226
- **Tech Note #:** 02-07
- **Published:** February 28, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Sebastian Frey, 4D Evangelist, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=23226
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2002/MacOS/TN_2002_05-09_(FEB)/02-07_4D_Business_Kit_IP.hqx

## Overview

Sebastian Frey documents the 4DBK IP Component, a compact ten-method 4D code component that opens up the otherwise closed-source 4D Business Kit (4DBK) e-commerce server, letting any 4D 6.7+ application drive it remotely via the 4DBK Tag Language over an HTTP-style session, using an accompanying demo application to walk through real integration scenarios.

## Key Points

- 4DBK is a stand-alone, double-clickable e-commerce server built on 4D 6.7.3 whose source is not public; the IP Component installs via 4D Insider into any 4D 6.7+ database and can be cleanly removed at any time, requiring the 4D Internet Commands plug-in and a small Business Kit Plug-in for BLOB text parsing.
- Setup involves configuring the demo application's Preferences (4DBK address/port, Local Web Port 8080, store code "DEMO", local email address) and creating a matching "DEMO" store manually in 4DBK, including SMTP server settings and increasing the default 10-minute session auto-logoff.
- Sessions are created or reused with `4DBKC_SessionNew("bktest.4d.com";80)` or `4DBKC_SessionOpen($t_SES;"testbk.4d.com";80)`; all subsequent work is scoped to a session ID.
- The `4DBKC_Execute($tSessionID;$tCommand)` function sends a string of 4DBK Tag Language commands and returns a BLOB result; the demo instead calls a wrapper, `APP_BKExecute`, which auto-prefixes the required `4DBKStoreSet/XXXX` command and returns a simple Longint success/failure code via an optional third pointer parameter.
- Customer sync uses `4DBKCustomerExists` to check for an existing customer (`CUS_UNK` = unknown), `4DBKRecordNew/CUS` to create one, and `4DBKFieldSet` calls (e.g. `4DBKFieldSet/CusLastName=...`) to populate fields.
- Dynamic transactional email is sent with the wrapper `APP_BkMailSend`, which builds a `4DBKMail` tag command to email a semi-dynamic 4DBK HTML page (e.g. `mail_example.htm`) to a given recipient.
- Product/item sync uses the purpose-built `4DBKC_ItemUpdateBuild`/`4DBKC_ItemUpdateSend` pair (building a BLOB that can carry binary picture data) rather than the generic Execute command, and shopping cart/checkout flows use `APP_BKItemToCart` and the `4DBKOrderValidate` tag after checking `4DBKSelectionSet`/`4DBKSelectionSize`.

## Featured Technology

- 4D Business Kit (4DBK) e-commerce server
- 4DBK IP Component (4D code component)
- 4DBKC_SessionNew / 4DBKC_SessionOpen
- 4DBKC_Execute and the 4DBK Tag Language
- 4DBKC_ItemUpdateBuild / 4DBKC_ItemUpdateSend
- APP_BKExecute wrapper method pattern
- 4D Internet Commands plug-in

## Historical Commentary

**Status:** Obsolete

Sebastian Frey explains how the 4DBK IP Component -- a small, installable 4D code component built on the 4D Internet Commands plug-in -- lets any custom 4D application drive the closed-source 4D Business Kit e-commerce server by sending its Tag Language commands over the network and parsing BLOB responses. This is a documented example of integrating with a discontinued 4D vertical product (4D Business Kit) via a session-based remote command protocol and wrapper methods like APP_BKExecute that simplified error handling and store-code management. Both 4D Business Kit and its IP Component have been discontinued for many years, making this note's specific integration technique obsolete; any e-commerce solution built with 4D today would use modern web/ORDA/REST tooling rather than this legacy tag-language-over-session-ID architecture.

References to newer/updated information:
- 4D Business Kit and its IP Component have been discontinued; modern e-commerce integrations with 4D would use current REST/ORDA/web server capabilities instead
- The session-ID-based remote command execution pattern shown here (4DBKC_SessionNew/4DBKC_Execute) has no direct modern equivalent since the product it targeted no longer exists
