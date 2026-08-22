# Tech Note 01-12: Sending Multi-Part emails Using 4D Internet Commands

**Author:** Not specified in source document
**Published:** March 30, 2001 | **Product/Version:** 4D Internet Commands v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=13094
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_11-15_(MAR)/01-12_Multiple-Part_E-mails.exe

## Overview
A comparison of 4D Internet Commands' SMTP_QuickSend versus its low-level SMTP command sequence for constructing multi-part (non-plain-text) emails. This Tech Note compares two ways of sending email using 4D Internet Commands: SMTP_QuickSend, a single-statement command designed for basic, low-control e-mailing, versus a sequence of low-level commands (SMTP_New, SMTP_Host, SMTP_From, SMTP_Cc, SMTP_Bcc, SMTP_Subject, SMTP_AddHeader, and SMTP_Send) that together build up a complete mail envelope tied to one mail ID.

## Key Points
- It explains that the accompanying sample database deliberately uses the low-level approach, because SMTP_QuickSend is limited to plain-text content and cannot express the custom headers or mixed-content (multi-part) bodies the example requires.
- The featured technology is therefore the 4D Internet Commands plug-in's SMTP command set, specifically its low-level, multi-step API for constructing more sophisticated, multi-part emails than the convenience wrapper allows — a practical guide for developers whose e-commerce or notification emails in this era needed more than a single plain-text message body.

## Featured Technology
- 4D Internet Commands (SMTP)
- SMTP_QuickSend
- Low-level SMTP commands (SMTP_New, SMTP_Host, SMTP_From, etc.)
- MIME multi-part email construction

## Historical Context
This summary is based only on the available teaser text from the 4D Knowledgebase page; the linked download was an old Windows self-extracting .exe installer (or a Mac-native archive of the same era) that could not be extracted in this environment, so only the on-page teaser paragraph was available. No claims are made here beyond what that teaser describes, and any code, screenshots, or detailed implementation from the original Tech Note and its example database could not be reviewed.

## Historical Commentary
**Status:** Partially_superseded

This note compares two email-sending approaches offered by the 4D Internet Commands plug-in — the simple, single-statement SMTP_QuickSend versus a lower-level sequence of SMTP_New/SMTP_Host/SMTP_From/etc. commands — recommending the latter whenever an email needs more than plain-text content, such as custom headers or mixed-content bodies. The 4D Internet Commands plug-in has since been folded into 4D's core language as built-in SMTP/email commands, so while the low-level-vs-quick-send tradeoff concept remains sound, the specific plug-in and command names described here are dated relative to 4D's current, integrated email-sending API.

**Related updates since:**
- 4D Internet Commands' SMTP functionality has since been integrated into 4D's core classic language as built-in commands, rather than requiring a separate plug-in
- 4D's current SMTP/email commands offer more modern MIME/multi-part and attachment handling than the SMTP_QuickSend vs. low-level-command choice described in this 2001 note

