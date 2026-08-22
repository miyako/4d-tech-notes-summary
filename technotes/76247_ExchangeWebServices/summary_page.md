# Tech Note 11-01: 4D v12 and Exchange Web Services

**Author:** Jesse Pina, Technical Services Team Member, 4D Inc.
**Published:** January 20, 2011 | **Product/Version:** 4D v12.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76247
**Download:** https://kb.4d.com/DLTN/TN/2011/Windows/TN_2011_01-03_(JAN)/11-01_4D_Exchange.zip

## Proposition
This note explains how to connect 4D applications to Microsoft Exchange Server using Exchange Web Services (EWS), a protocol enabling creation, updating, deletion, and retrieval of Exchange data such as email, contacts, tasks, and calendar events. It introduces the open-source php-ews PHP library as the practical bridge, explaining why it was chosen, its basic workflow and requirements, and how to wire it up using 4D v12's embedded PHP interpreter. After setting up the sample database and PHP layer, it walks through authenticating against Exchange and four concrete examples: retrieving folders, contacts, tasks, and calendar events. The note equips 4D developers with a working pattern for pulling Exchange/Outlook data into a 4D application.

## Key Points
- Introduces Exchange Web Services (EWS) as Microsoft's protocol for programmatic access to Exchange Server data.
- Chooses the open-source php-ews PHP library as the integration bridge, explaining its rationale and requirements.
- Uses 4D v12's embedded PHP interpreter to call php-ews from 4D code.
- Details sample database setup on both the PHP and 4D sides, including what data is returned to 4D.
- Walks through Exchange authentication as a prerequisite step.
- Provides four worked examples: Get Folders, Get Contacts, Get Tasks, and Get Calendar Events.

## Featured Technology
- Microsoft Exchange Web Services (EWS)
- php-ews PHP library called from 4D's embedded PHP interpreter
- 4D methods for retrieving folders, contacts, tasks, and calendar events from Exchange

## Best Practices Highlighted
- Authenticate against Exchange before attempting data retrieval calls
- Isolate EWS/php-ews integration logic behind clear 4D methods for maintainability

## Context / Positioning
Published in 2011 to help 4D developers integrate corporate Exchange/Outlook data (contacts, calendars, tasks) into 4D business applications, leveraging the then-new embedded PHP interpreter as the bridge technology.

## Historical Commentary
**Status:** Deprecated

This EWS-via-PHP integration pattern is dated: Microsoft has since deprecated EWS in favor of the Microsoft Graph API for Exchange Online/Office 365 integration, and the php-ews library is no longer actively maintained. A modern 4D integration with Exchange/Outlook data would use Microsoft Graph's REST/OAuth2 API directly from 4D's native HTTP/REST commands rather than routing through a PHP library and the legacy EWS protocol.
