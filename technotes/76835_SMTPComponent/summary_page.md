# Tech Note 13-07: SMTP Component

**Author:** Sonya Rackwitz, Technical Services Team Member, 4D Inc.
**Published:** June 17, 2013 | **Product/Version:** 4D v13.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76835
**Download:** https://kb.4d.com/DLTN/TN/2013/13-07_SMTPComponent_R2.zip

## Proposition
This Tech Note packages 4D's Internet Commands into a reusable SMTP component that handles sending email (setting host, sender, recipient, subject, and body) plus managing multiple SMTP accounts and recording sent messages via an external database.

## Key Points
- Wraps low-level 4D Internet Commands into a simple SMTP_* method API (SMTP_New, SMTP_Host, SMTP_From, SMTP_To, SMTP_Send, SMTP_Clear, SMTP_Subject, SMTP_Body).
- Uses an external database to store SMTP account configurations and a log of sent messages.
- Provides SMC_* administrative methods for managing accounts (SMC_ACCOUNT_LIST, SMC_CREATE_ACCOUNT, SMC_DELETE_ACCOUNT, SMC_CHANGE_NUM_RETRY, etc.).
- Documents installation of the component and how to integrate it into a host database.
- Covers retry configuration for handling transient send failures.

## Featured Technology
- 4D Internet Commands (SMTP)
- Custom SMTP component (SMTP_New/Host/From/To/Send/Clear/Subject/Body)
- External database for account/message storage
- Email account management (SMC_ACCOUNT_LIST, SMC_CREATE_ACCOUNT, etc.)

## Best Practices Highlighted
1. Encapsulate email-sending logic in a component to keep it reusable across projects.
2. Log sent messages externally for auditing and troubleshooting delivery issues.
3. Support configurable retry counts for unreliable network conditions.

## Context/Positioning
Published for 4D v13.3 as part of 4D's ongoing library of reusable components built atop the native 4D Internet Commands, at a time before built-in high-level email/REST libraries existed.

## Historical Commentary
**Status:** Still Relevant

4D's classic Internet Commands for SMTP remain supported and functional today, so this component-based wrapper pattern still works as-is. However, a modern implementation would more likely be built as a 4D class (introduced ~v19-20) exposing the same SMTP_* style API with object-oriented syntax and JSON-based configuration rather than an external database and classic component, and some developers now prefer third-party or cloud email-sending APIs invoked via native REST/HTTP commands.
