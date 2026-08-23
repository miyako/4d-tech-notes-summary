# Tech Note: The 4D Business Kit v2.x IP Component

- **Asset ID:** 29724
- **Tech Note #:** 03-32
- **Published:** July 29, 2003
- **Product / Version:** 4D Business Kit 2.x
- **Platform:** Mac & Win
- **Author:** Frank Chang
- **Page URL:** https://kb.4d.com/assetid=29724
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_31-35_(JUL)/03-32_4DBK2_IP_Component.hqx

## Overview

Frank Chang documents version 2.x of the 4D Business Kit IP Component, which newly adds the ability to download Item, Customer, and Order data from a 4D Business Kit e-commerce server into an external 4D application, demonstrated end-to-end with a companion demo store and download application.

## Key Points

- The 4DBK v2.x IP Component contains 19 methods and depends on three plug-ins: 4D Internet Commands, 4D Pack, and Yapee (a 4D Business Kit-specific plug-in).
- New in this version: the ability to download Item, Customer, and Order information from the 4DBK server into a 4D application, in addition to the prior version's upload-only capability.
- Setup requires enabling '4D Component' data exchange and a shared password on the demo store's properties (Stores > ST01 > 4D Component), and configuring the companion 4D application with the server IP, port (default 8080), 4-character store code (e.g. "ST01"), and that same password.
- The driver method `Store_Demo_getOrders` uses `4DBKC_ToolsString("GET TIMESTAMP GMT"; ...)` to build a GMT-formatted incremental timestamp query (e.g. `*Ts>=20030707115635`) so previously downloaded orders are not re-fetched.
- The core download call is `4DBKC_ImportFileFrom4DBK(serverAddress; serverPort; timeOutSec; maxTimeSec; password; store; module; searchCriteria; filePath{; startFrom{; number}})`, where `module` selects the target table ("ORD", "ITM", or "CUS").
- Downloaded data files are encrypted using MD5 hashing with the shared password configured in the store's 4D Component settings, so the file contents are unreadable without that password.
- The note notes the same download logic generalizes directly to Customer and Item retrieval, not just Orders, despite the demo focusing on orders.

## Featured Technology

- 4D Business Kit (4DBK) v2.x IP Component
- 4DBKC_ImportFileFrom4DBK
- 4DBKC_ToolsString (GMT timestamp helper)
- MD5-encrypted data-file exchange
- 4D Internet Commands / 4D Pack / Yapee plug-ins

## Historical Commentary

**Status:** Obsolete

4D Business Kit, 4D Insider, 4D Pack, and the Yapee plug-in are all long-discontinued products specific to this era of 4D's e-commerce and component tooling, making this note's entire technical stack obsolete. The specific IP Component API (4DBKC_ImportFileFrom4DBK, the MD5-encrypted file exchange, the GMT timestamp helper) has no direct successor; any current 4D e-commerce integration would be built from scratch using modern REST/ORDA APIs and standard web-service authentication rather than this legacy component and file-based exchange mechanism.

**References to newer/updated information:**
- 4D Business Kit, 4D Insider, 4D Pack, and the Yapee plug-in are all discontinued legacy products with no current equivalents
- Modern 4D e-commerce integrations would use REST/ORDA-based APIs rather than the file-based, MD5-encrypted exchange mechanism described here
