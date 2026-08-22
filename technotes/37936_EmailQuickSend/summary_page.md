# Tech Note 05-24: Email_QuickSend

**Author:** Not specified in available source
**Published:** July 11, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=37936
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_21-24_(JUN)/05-24_Email_QuickSend.exe

## Overview
This Tech Note shows how to send authenticated SMTP email from 4D using the little-known SMTP_Auth command from 4D Internet Commands, wrapped in a drop-in Email_QuickSend replacement method.

## Key Points
- SMTP_Auth (from 4D Internet Commands) supports SMTP servers requiring authentication; SMTP_QuickSend does not.
- SMTP_Auth had shipped in multiple 4D Internet Commands releases but remained little known.
- The Email_QuickSend method mirrors SMTP_QuickSend's calling convention with one extra password parameter, giving an easy migration path for existing SMTP_QuickSend call sites.

## Featured Technology
- 4D Internet Commands plug-in
- SMTP_Auth / SMTP_QuickSend commands
- Custom wrapper method pattern for incremental API migration

## Historical Context
**Status:** Obsolete

4D Internet Commands as a distinct plug-in and its specific SMTP command set have been superseded by native email/network capabilities in later 4D versions, and just as importantly, the simple username/password SMTP authentication this note addresses has itself been phased out by most major email providers in favor of OAuth2-based authentication, which this technique does not support. The core idea — wrapping a limited command with a small compatible method to add a missing capability — remains a sound general programming pattern, but the specific SMTP_Auth-based solution is no longer a viable way to send authenticated email through most modern mail servers. Note: only the on-page teaser paragraph for this note survived in this archive — the full PDF and example database could not be recovered (old download-archive format not accessible in this environment), so this summary is necessarily limited to that teaser text.
