# Tech Note 05-37: HTML Emails

**Author:** Thomas Maul, General Manager, 4D Germany
**Published:** November 13, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=40331
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_37-39_(NOV)/HTML_Mail.zip

## Overview
This note shows how to send HTML-formatted emails with embedded pictures from 4D 2004 — motivated by automated sales report emails — covering both a no-code Quick Report approach and a more flexible HTML-template approach.

## Key Points
- Contrasts externally-referenced pictures (smaller, but blockable/trackable) with embedded MIME picture enclosures (larger, but reliably rendered by all mail clients) — recommending embedding for business reports.
- Sample database generates a report with customer sales stats, a ZIP-code pie chart, and product-code stats/chart, using 4D Chart to produce pictures converted to GIF.
- **Quick Report route:** no HTML knowledge needed; uses the new-in-2004 "Build 4D Code" wizard feature to auto-generate report code.
- **HTML template route:** uses the new `PROCESS HTML TAGS` command to merge dynamic data into a developer/designer-authored HTML template.
- Final report assembled as multipart MIME and sent via 4D Internet Commands; includes specific MIME-safe character-replacement steps (`=` → `=3D`).
- Provides a walkthrough for adapting the demo to a developer's own database and exposing the feature to end customers.

## Featured Technology
- PROCESS HTML TAGS (4D 2004 command)
- 4D Quick Report engine (HTML output)
- 4D Chart (picture/GIF generation)
- 4D Internet Commands (SMTP sending)
- Multipart MIME email construction

## Historical Context
Automated HTML report emails with embedded charts remain a common business need, but 4D has since added more direct native SMTP/email commands, reducing reliance on the 4D Internet Commands plug-in and hand-built MIME-boundary manipulation shown here. The "4D Email 3.0" product mentioned as then-in-beta is itself long discontinued, and the Quick-Report-to-HTML workflow has been superseded by more modern reporting and web/JSON-based approaches.
