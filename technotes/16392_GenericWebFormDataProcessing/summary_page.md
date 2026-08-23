# Tech Note: Creating a Generic Web Form Data Processing System

- **Asset ID:** 16392
- **Tech Note #:** 01-36
- **Published:** August 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Kent D. Wilbur, Manager of Information Systems, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=16392
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_36-40_(AUG)/01-36_Generic_Web_Form.hqx

## Overview

Kent D. Wilbur (Manager of Information Systems, 4D, Inc.) builds the first half of a two-part generic web-form intake system: a set of hidden HTML control fields plus GET WEB FORM VARIABLES let one 4D backend validate, e-mail, and template-reply to any HTML form without hard-coding its field names, encoding submissions as machine-readable tagged text for a companion parsing database.

## Key Points

- GET WEB FORM VARIABLES (new in 4D 6.7) returns parallel name/value text arrays for every submitted form field without requiring each one to be individually declared, forming the backbone of the system's genericity.
- Hidden control fields on every HTML form -- tFormName, tReplyFormName, tErrorForm, tMandatoryFields (a '/'-delimited list), tMailTo, tMailSubject, tMailFields, and optionally tMailBody -- tell the shared WEB_HandleForm backend method how to validate, route, and mail that specific form's submission.
- Routing goes through the 4DCGI mechanism (On Web Connection dispatching on a /4DCGI/WEB_HandleForm URL) rather than 4DACTION, which the note calls out as more secure since it only allows explicitly-programmed dispatch targets.
- WEB_fCompleteForm checks every field named in tMandatoryFields against the submitted arrays (via Find in array), builds a human-readable "the following mandatory field(s) are missing" message using a GEN_sFriendlyName helper that expands CamelCase/underscore variable names into spaced, capitalized words, and returns pass/fail via a pointer parameter.
- On success, MAIL_AddMailMessage queues a record in a zMailMessages table (sent asynchronously by a separate process to avoid delaying the browser response), with the payload built by MAIL_tFields2Text as [***Friendly Field Name***]\nValue blocks -- the exact tag format the companion GenericEval database (TN 01-49) later parses back out of the mailbox.
- An optional tMailBody template mechanism (MAIL_tFields2Block) sends the form submitter a personalized reply by substituting <!--#1-->, <!--#2-->, etc. positional placeholders in a stored zHTMLBlocks template record with the submitted field values; a more advanced "AlmostGeneric" variant additionally declares fields in COMPILER_WEB to support default values, error-preserving redisplay, and chaining several forms together into a multi-page survey.

## Featured Technology

- GET WEB FORM VARIABLES for undeclared/generic form field handling
- 4DCGI (On Web Connection) form routing instead of 4DACTION
- Hidden control fields: tFormName/tReplyFormName/tErrorForm/tMandatoryFields/tMailTo/tMailFields/tMailBody
- MAIL_AddMailMessage / MAIL_tFields2Text machine-readable [***Tag***] email encoding
- COMPILER_WEB variable declaration workaround for compiled-mode web forms
- Template-based reply emails via MAIL_tFields2Block token substitution

## Historical Commentary

**Status:** Superseded

Kent Wilbur (4D, Inc.) designs a genuinely generic web-form intake system: a set of hidden HTML control fields (tMandatoryFields, tMailTo, tMailFields, tMailBody, etc.) plus GET WEB FORM VARIABLES let a single 4D backend validate, e-mail, and template-reply to any HTML form without hard-coding its field names, with the collected data encoded into machine-readable [***Tag***] emails for a companion parsing database (covered in TN 01-49, the GenericEval database, released two months later). This generic-intake-via-email-relay architecture was a clever way to sidestep direct database writes and firewall exposure in 2001, but it has been thoroughly superseded: modern 4D web development handles form submission and validation directly through REST/ORDA endpoints or server-side web forms, with structured JSON payloads and direct database writes replacing the mail-relay-and-tag-parsing round trip described here.

References to newer/updated information:
- Modern 4D web applications submit form data directly to REST/ORDA endpoints rather than relaying it through e-mail as machine-readable tagged text
- GET WEB FORM VARIABLES-based generic form handling has been largely superseded by structured JSON request bodies parsed by 4D's native JSON commands
