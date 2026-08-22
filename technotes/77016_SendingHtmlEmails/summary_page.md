# Tech Note 14-06: [3rd Party Tech Note] Sending HTML Emails

**Author:** Dave Terry, Pacific Data Management, Inc.
**Published:** April 9, 2014 | **Product/Version:** 4D Internet Commands v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77016
**Download:** https://kb.4d.com/DLTN/TN/2014/14-06_SendingHTMLEmail.pdf

## Proposition
This third-party note shows how to reliably send professional HTML-formatted emails with embedded images from 4D, using 4D Internet Commands (4DIC) v14's improved capabilities and MIME's `cid:` attachment mechanism, so images render inline rather than as broken/blocked external links.

## Key Points
- SMTP transmits only 7-bit ASCII; MIME extends it to encode richer content like HTML bodies and binary attachments.
- Externally-hosted images in HTML emails are unreliable: many clients block external image loading, and hosted images can move or disappear over time.
- The fix is to embed images as MIME attachments referenced via `cid:myKey` URIs in the HTML, so clients display them inline.
- Implementation steps: scan HTML `<img>` tags for sources, replace each with a unique `cid:` reference, attach the corresponding local files with the matching key, then send.
- A regex (`Match regex`) locates and rewrites image tag sources programmatically; duplicate image sources are de-duplicated to a single `cid:` reference.
- The `SMTP_` command family (`SMTP_New`, `SMTP_Host`, `SMTP_From`, `SMTP_Subject`, `SMTP_To`, `SMTP_Body`, `SMTP_Attachment`, `SMTP_Send`) composes and sends the message with both HTML and plain-text bodies for compatibility.
- A parallel HTML variant with full local paths is generated for previewing the email inside a 4D Web Area before sending.

## Featured Technology
- 4D Internet Commands (4DIC) SMTP_ command family
- MIME multipart HTML emails with `cid:` inline image attachments
- Regex-based HTML rewriting (`Match regex`)
- 4D Web Area for HTML preview

## Best Practices Highlighted
1. Never rely on externally-hosted images in transactional/marketing HTML emails; embed them as MIME attachments instead.
2. Always supply a plain-text body alongside the HTML body for clients that don't render HTML.
3. De-duplicate repeated image references to avoid attaching the same image multiple times.

## Context/Positioning
Published as 4DIC's v14 update simplified HTML email support, this third-party note gave developers a concrete, ready-to-adapt implementation for a very common business requirement: professional-looking customer communications.

## Historical Commentary
**Status:** Still relevant

The core technique — rewriting image tags to `cid:` references and attaching the corresponding images via MIME so HTML emails render reliably — reflects standard email engineering practice that has not fundamentally changed since 2014. 4D Internet Commands (4DIC) remains 4D's supported plug-in for SMTP email sending, so this note's approach continues to work essentially as written; a modern implementation might use 4D's newer JSON/text-handling commands for tidier string manipulation, but no replacement technology has superseded 4DIC's role for this task.
