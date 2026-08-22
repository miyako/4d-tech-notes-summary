# Tech Note: Downloading Email with 4D Internet Commands

**Author:** Not specified
**Published:** October 1, 1999 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11859

## Overview
This Tech Note demonstrates building a custom email client within 4D using the Internet Commands plug-in's POP3 capabilities, arguing for custom email solutions despite the availability of free email clients.

## Key Points
- Acknowledges free email clients exist (Claris Emailer Lite, Outlook Express, Eudora) but argues for custom solutions
- Use cases: custom user interfaces, sales automation integration, web order processing, scheduled/conditional email downloads
- Uses 4D Internet Commands for POP3 email retrieval
- Demonstrates database-email integration within 4D

## Featured Technology
- 4D Internet Commands (POP3 protocol)
- Custom email client development
- Database-email integration

## Historical Context
**Status:** Superseded

The full PDF could not be recovered (error: NO_DOWNLOAD_LINK_TEASER_ONLY). The 4D Internet Commands plug-in has been superseded by built-in transporter classes in modern 4D (4D.POP3Transporter, 4D.IMAPTransporter, 4D.SMTPTransporter). IMAP, which was not available via the old plug-in, is now the standard for email retrieval. The use cases described remain valid—custom email interfaces and database-integrated email processing are still common requirements—but the implementation approach has changed entirely. The mention of Claris Emailer Lite and Eudora places this note firmly in its era.
