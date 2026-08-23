# Tech Note: Sending Multi-Part emails Using 4D Internet Commands

- **Asset ID:** 13094
- **Tech Note #:** 01-12
- **Published:** March 30, 2001
- **Product / Version:** 4D Internet Commands 6.5
- **Platform:** Mac & Win
- **Author:** Hugo Fournier
- **Page URL:** https://kb.4d.com/assetid=13094
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_11-15_(MAR)/01-12_Multiple-Part_E-mails.hqx

## Overview

Hugo Fournier (Technical Support Engineer) demonstrates how to send an e-mail with both plain-text and HTML versions of the body using 4D Internet Commands' low-level SMTP command set, rather than the simpler one-line `SMTP_QuickSend`, which only supports plain text. The note covers the MIME header mechanics needed and walks through an example database that builds and sends such a message.

## Key Points

- `SMTP_QuickSend` provides basic single-statement e-mail sending but cannot specify anything beyond plain text; the low-level sequence `SMTP_New`, `SMTP_Host`, `SMTP_From`, `SMTP_Cc`, `SMTP_Bcc`, `SMTP_Subject`, `SMTP_AddHeader`, and `SMTP_Send` builds up a full mail envelope tied to one mail ID.
- Plain-text-only bodies use `Content-Type: text/plain; charset=us-ascii`; HTML-only bodies use `Content-Type: text/html;charset=us-ascii`; combined bodies use a top-level `Content-Type: multipart/alternative; boundary=myboundary` header with each part introduced by its own Content-Type line.
- Per RFC 2046, each Content-Type line must be followed by a blank line before the actual content, and content types are conventionally ordered from simplest to most complex (plain text before HTML).
- The example database's `[Emails]`/`Form1` lets users pick To/Cc/Bcc recipients from `[Contacts]`/`[Email_Table]` via three pop-up menus sharing a single `Gen_Fil_List` handler that uses a pointer parameter (`->To_Mail`, `->Cc_Mail`, `->Bcc_Mail`) to determine which scrollable area to populate.
- The header type and message body are computed dynamically based on which of `vPlainText`/`vHtmlContents` are non-empty, constructing the `--mymimeboundary` delimited body and setting `vHeaderType` to `multipart/alternative`, `text/html`, `text/plain`, or `"None"` accordingly.
- The sending routine calls the SMTP_ commands in strict sequence with error checking after each one, reporting the specific failing command (e.g. `SMTP_To`, `SMTP_Subject`, `SMTP_Send`) via `Err_Alert` and aborting on any failure, then calls `SMTP_Clear` to release the mail ID.

## Featured Technology

- 4D Internet Commands SMTP low-level commands (SMTP_New, SMTP_Host, SMTP_From, SMTP_Cc, SMTP_Bcc, SMTP_Subject, SMTP_AddHeader, SMTP_Send)
- SMTP_QuickSend (contrasted as a simpler alternative)
- MIME multipart/alternative header and boundary construction
- Content-Type headers for plain text and HTML bodies
- SMTP_Body / SMTP_Clear

## Historical Commentary

**Status:** Superseded

Hugo Fournier's note shows how to compose a MIME multipart/alternative e-mail -- one containing both a plain-text and an HTML version of the message body so mail clients can render whichever they support -- using 4D Internet Commands' low-level SMTP_ methods instead of the simpler but less flexible SMTP_QuickSend, with careful attention to the required blank line after each Content-Type header and the boundary marker syntax defined in RFC 2046. The 4D Internet Commands plug-in and its SMTP_ command set have long been superseded by 4D's native SMTP-sending commands built directly into the language, so while the underlying MIME multipart/alternative concept remains valid and necessary today, the specific plug-in commands shown in this note are obsolete for new development.

**References to newer/updated information:**
- 4D has since added native SMTP e-mail-sending commands to the core language, replacing the older 4D Internet Commands plug-in's SMTP_ methods shown in this note
- The MIME multipart/alternative technique for sending combined plain-text/HTML e-mails remains valid and is still used today, just typically constructed through 4D's newer built-in email commands or an external email-sending service
