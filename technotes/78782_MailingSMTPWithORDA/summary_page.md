# Tech Note 21-16: Mailing Feature: Sending and Archiving Emails with ORDA

**Author:** Marouane Ait Salah, Technical Services Engineer, 4D Morocco
**Published:** September 20, 2021 | **Product/Version:** 4D v19 R2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78782
**Download:** https://kb.4d.com/DLTN/TN/2021/21-16_IncomingAndOutgoingMail.zip

## Proposition
Sending and archiving email is a common business-app requirement. This note shows how to combine 4D's native SMTP Transporter commands with ORDA entities to send mail from both a desktop 4D Write Pro form and a web contact form, while keeping a searchable archive of every message sent.

## Key Points
- **Native Transporter commands** (`SMTP New transporter`, `IMAP New transporter`, `POP3 New transporter`) replace the older 4DIC plugin for all three mail protocols.
- **Connection validation:** `transporter.checkConnection()` returns a status object (`.success`, `.statusText`) before attempting a send.
- **4D Write Pro as an email composer:** `WP EXPORT VARIABLE(..., wk mime html)` turns a Write Pro area's contents into MIME, then `MAIL Convert from MIME` builds a proper email object with formatting intact.
- **Attachments and headers:** `MAIL New attachment()` and a custom `headers` collection (e.g. an "Importance" header) let the email object carry rich metadata.
- **ORDA archiving:** every sent (or received) message is persisted as an entity — `ds.Archives.new()`, field assignment, `.save()` — and can be listed/deleted (`.drop()`) from a simple UI.
- **Web form integration:** the same SMTP logic runs unmodified inside `On Web Connection`, triggered by a standard HTML POST form, reading fields via `WEB GET VARIABLES`.
- **Diagnostics:** `SET DATABASE PARAMETER(SMTP Log; 1)` plus a `logFile` property enables SMTP transaction logging for troubleshooting.

## Featured Technology
- SMTP New transporter / IMAP / POP3 Transporter commands
- ORDA (dataclass entities, `ds.<Table>.new()`, `.save()`, `.drop()`)
- 4D Write Pro (`WP EXPORT VARIABLE`)
- `MAIL Convert from MIME`, `MAIL New attachment`
- 4D web server (`WEB GET VARIABLES`, `On Web Connection`)

## Best Practices Highlighted
1. Validate SMTP credentials with `checkConnection()` before attempting a send to give users clear feedback.
2. Persist sent/received mail as ORDA entities rather than flat files for easy querying and auditing.
3. Enable SMTP logging during development/troubleshooting via the `SMTP Log` database parameter.

## Context / Positioning
Published shortly after ORDA had become the default data-access paradigm in 4D (v17+), this note exemplifies 4D's push to have developers combine modern building blocks — native network Transporter commands, ORDA entities, and 4D Write Pro — instead of older plugin-based tooling (4DIC) or classic array/pointer record handling.

## Historical Commentary
**Status:** Still relevant

This pattern is still exactly how you would build mail sending/archiving in current 4D versions — the Transporter commands and ORDA entity model shown here have not been superseded, only extended (e.g., native OAuth2 authentication parameters were added to `SMTP New transporter` in later releases, building on techniques like those in TN 21-11 in the same batch). The 4DIC plugin this note explicitly moves away from is now legacy and rarely seen in modern databases. A developer building this today would follow the same architecture, just with 4D Write Pro and ORDA further matured.
