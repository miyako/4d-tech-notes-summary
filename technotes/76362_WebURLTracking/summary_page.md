# Tech Note 11-20: Web URL Tracking

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** June 17, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76362
**Download:** https://kb.4d.com/DLTN/TN/2011/11-20_Web_URL_Tracking.zip

## Proposition
This Tech Note presents a 4D database-driven approach for tracking marketing-campaign link clicks by storing links keyed by UUID, incrementing a counter per click, and redirecting users via 4D's Web Server, without needing access to external server logs.

## Key Points
- **Core problem:** measuring campaign link click-through when the destination page isn't hosted, or its server logs aren't accessible.
- **UUID-based obfuscation:** links are presented to end users by UUID reference rather than their real destination.
- **Click tracking:** each link is its own record with a counter field incremented on each access.
- **Transparent redirection:** the 4D database translates the UUID, bumps the counter, and redirects the user, all silently.
- **HTML source converter:** a tool included to tag campaign links with trackable UUIDs automatically.
- **Campaign statistics viewer:** provides visibility into click counts and campaign performance.

## Featured Technology
- 4D Web Server-based link redirection and UUID obfuscation
- HTML source converter for tagging campaign links
- Database-driven click-tracking and campaign statistics

## Context / Positioning
Published in mid-2011, this note gave 4D developers a self-contained, no-external-dependency way to add marketing analytics to campaigns, useful for organizations that wanted click tracking without adopting a third-party analytics platform.

## Historical Commentary
**Status:** Still Relevant

The core approach — storing links keyed by UUID in a 4D table, incrementing a counter, and redirecting via a 4D Web Server process — is a generic pattern that still works today and requires no deprecated technology, so it remains functionally valid.

That said, this exact home-grown click-tracking approach has been largely superseded in the broader industry by dedicated analytics platforms and URL shorteners with built-in tracking, and a modern 4D implementation would likely expose the redirect/tracking endpoint via 4D's REST/ORDA layer rather than the classic Web Server method-based routing shown here.
