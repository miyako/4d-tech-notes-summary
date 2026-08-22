# Tech Note 07-30: Google Calendar: Downloading Future Events

**Author:** Robert Molina, Technical Support Engineer, 4D Inc.
**Published:** August 1, 2007 | **Product/Version:** 4D Internet Commands v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=47153
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_30-34_(AUG)/07-30_4DIC_Google_Calendar.zip

## Overview
This note documents building a 4D integration with Google Calendar's original GData/REST API — authenticating, listing calendars, and downloading future events — entirely via raw HTTP requests constructed and parsed using 4D Internet Commands (4DIC), since no official 4D client library existed for Google's API.

## Key Points
- **Technologies used:** XML (data format), HTTP (via 4DIC, since no 4D client library existed), REST (URL-based data exchange), and GData (Google's Atom/RSS-based protocol for reading/writing service data; no feed deletion support).
- **Authentication:** a raw HTTP POST to `/accounts/ClientLogin` with `Email`, `Passwd`, `service=cl`, and `source` parameters, hand-built with explicit `\r\n` CRLF sequences per HTTP 1.0.
- **Three-step workflow:** Authenticate → Request Calendar List → Request Future Events, each returning an Atom XML feed parsed with 4D's DOM XML commands.
- **Atom feed structure covered:** `id`, `link`, `author`, `gd:eventStatus`, `gd:visibility`, `gd:when` (start/end time), `gd:where` (location), `gd:reminder`.
- Sample database provides a login screen with "Sync Calendar List" and "Sync Calendar Event" buttons driving the full workflow.
- References companion notes 06-30 "Building a REST Client" and 07-32 "4D Deployment Options for Wide Area Networks."

## Featured Technology
- 4D Internet Commands (4DIC)
- Google Calendar Data API (GData), Atom/RSS XML
- REST architecture
- ClientLogin authentication (raw HTTP POST)

## Historical Context
Published August 2007 for 4D v2004/4D Internet Commands, illustrating early-era REST/XML web service integration from 4D — a pattern that predates 4D's later, more built-in HTTP/JSON tooling and 4D v11's native SQL engine.

## Historical Commentary
**Status:** Obsolete

Both the specific authentication mechanism (Google's ClientLogin, a plaintext username/password POST) and the GData protocol itself were deprecated and shut down by Google years ago, replaced by OAuth 2.0 and the modern Google Calendar API v3 (JSON/REST) — so none of the concrete endpoints or request formats in this note still function. The general technique of building raw HTTP requests and parsing structured (XML or JSON) responses from 4D to integrate with a third-party REST API remains valid and is still how such integrations are done, just using 4D's more modern HTTP client and JSON commands instead of hand-built request strings.
