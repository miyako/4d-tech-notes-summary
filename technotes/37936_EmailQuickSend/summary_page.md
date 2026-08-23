# Tech Note: Email_QuickSend

- **Asset ID:** 37936
- **Tech Note #:** 05-24
- **Published:** July 11, 2005
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Melinda Gallo
- **Page URL:** https://kb.4d.com/assetid=37936
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_21-24_(JUN)/05-24_Email_QuickSend.hqx

## Overview

Melinda Gallo, with code by Dave Batton, shows how to send SMTP-authenticated email from 4D by wrapping the low-level SMTP_Auth command from the 4D Internet Commands plug-in in a custom Email_QuickSend method — a near drop-in replacement for the plug-in's own SMTP_QuickSend, which does not support authentication.

## Key Points

- `Email_QuickSend(hostname; sender; recipient; subject; message; password)` mirrors the parameter order of `SMTP_QuickSend` but adds a required password parameter to support authenticated relays.
- The Send button's object method prompts for the sender's password at send time via `Request("Enter your password: ")`, only after validating that all other fields are filled in.
- Internally, Email_QuickSend sequences the low-level 4D Internet Commands SMTP_New, SMTP_Host, SMTP_Auth, SMTP_From, SMTP_To, SMTP_Subject, and SMTP_Body, followed by SMTP_Send and SMTP_Clear.
- Each low-level call is wrapped in `Email_HandleSMTPError("CommandName"; ErrorCode)`, a boolean-returning helper that sets the system `Error` variable and shows an Alert naming both the failing command and its error number.
- The note contrasts this with the simpler SMTP_Send command, noting that avoiding authentication implies the mail server operates as an open relay — a configuration with real security implications.

## Featured Technology

- 4D Internet Commands plug-in
- SMTP_Auth command for authenticated SMTP
- SMTP_New / SMTP_Host / SMTP_From / SMTP_To / SMTP_Subject / SMTP_Body / SMTP_Send sequence
- Custom error-wrapper pattern (Email_HandleSMTPError)
- Request() for runtime password prompting

## Historical Commentary

**Status:** Obsolete

This note shows a practical wrapper around a little-known but long-present 4D Internet Commands feature, letting developers add SMTP authentication to outgoing mail with a one-parameter change to their existing SMTP_QuickSend calls. The 4D Internet Commands plug-in and this exact low-level SMTP command sequence have since been superseded by native SMTP support in the core 4D language, and — more fundamentally — the simple username/password SMTP authentication model this note demonstrates predates the OAuth2-based authentication that Gmail, Microsoft 365, and most modern mail providers now require, making the technique itself obsolete for current mail servers even where the plug-in still runs.

**References to newer/updated information:**
- 4D Internet Commands (a separate plug-in in this era) has been superseded by native 4D language commands for email/network protocols in later 4D versions
- Most major email providers (Gmail, Microsoft 365, etc.) have since deprecated simple username/password SMTP authentication in favor of OAuth2, which this note's technique does not address
- Modern 4D applications typically use 4D's native SMTP-related commands or third-party REST-based transactional email APIs rather than 4D Internet Commands' SMTP_Auth
