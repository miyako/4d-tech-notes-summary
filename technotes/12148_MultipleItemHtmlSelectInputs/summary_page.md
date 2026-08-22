# Tech Note 01-08: Handling Multiple Item HTML Select Inputs with 4D 6.5

**Author:** Not specified in source document
**Published:** February 28, 2001 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=12148
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_06-10_(FEB)/01-08_HTML_Select_Inputs.exe

## Overview
A technique for correctly decoding an HTML SELECT MULTIPLE form input, where several selected values are submitted to the web server under the same field name. This Tech Note addresses a specific, easy-to-get-wrong detail of HTML forms integration with 4D's web server: an HTML SELECT input, when given the MULTIPLE keyword, allows a user to select more than one entry from a list of choices (typically by holding Control or Shift while clicking), optionally combined with a SIZE attribute controlling how many choices are visible at once.

## Key Points
- The complication is that when multiple items are selected, the browser submits each selected value to the web server under the identical field name, so the receiving 4D method must be written carefully to recognize and correctly collect all of the repeated values rather than only capturing the first (or last) one seen.
- The note explains exactly how to implement this decoding logic.
- Its featured technology is 4D's classic web-form-field decoding on the built-in web server, aimed at developers building HTML forms with multi-select inputs against a 4D-served backend during the era before structured JSON payloads made this kind of manual parsing unnecessary.

## Featured Technology
- HTML SELECT MULTIPLE form input
- 4D Web Server (form field decoding)
- Repeated-name parameter parsing

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Superseded

This note solves a specific HTML-forms decoding problem: an HTML SELECT input with the MULTIPLE keyword submits several selected values under the same field name, so a 4D web-serving method needs to be written smart enough to recognize and collect all of them rather than just the first. This entire class of manual HTML form-field parsing on 4D's classic web server has since been superseded by REST/ORDA-based web services, where structured JSON payloads (which natively support arrays of values) eliminate the need to manually decode repeated-name form fields.

**Related updates since:**
- 4D's web architecture has moved from raw HTML form field decoding on the built-in web server to REST APIs (built on ORDA) that exchange structured JSON, which natively represents multi-value fields as arrays
- Modern front-end frameworks handling multi-select inputs typically serialize the selection as a JSON array sent to a REST endpoint rather than relying on repeated same-named form fields parsed server-side

