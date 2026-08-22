# Tech Note 13-02: Integrating Facebook with 4D

**Author:** Darrell Draper, Technical Services Team Member, 4D Inc.
**Published:** January 29, 2013 | **Product/Version:** 4D v13.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76765
**Download:** https://kb.4d.com/DLTN/TN/2013/13-02_FBIntegration.zip

## Proposition
This Tech Note demonstrates several ways to integrate a 4D application or web site with Facebook, including embedding a 'Like' button, letting users log in with their Facebook account, retrieving user profile information from Facebook, and posting content to a user's Facebook wall/timeline.

## Key Points
- Shows how to insert a Facebook 'Like' button to let users share content from a 4D-powered site.
- Implements Facebook Login so users can authenticate against their Facebook account.
- Demonstrates retrieving user information (profile data) from Facebook's API after login.
- Demonstrates posting a story/update to a user's Facebook wall from within a 4D application.
- Uses 4D's web area and HTTP-based commands to communicate with Facebook's APIs.

## Featured Technology
- Facebook Graph API / Login
- 4D Web Area
- OAuth-style login flow
- HTTP/JSON commands

## Best Practices Highlighted
1. Use Facebook's official login flow rather than storing user credentials directly.
2. Scope requested permissions to only what the feature (posting, profile read) actually needs.

## Context/Positioning
Published for 4D v13.2 at the height of Facebook Platform integration popularity, when many business applications sought social features like login and content sharing.

## Historical Commentary
**Status:** Deprecated

Facebook has repeatedly overhauled its Graph API, login flow, and permission model since 2013 (deprecating classic wall posting, changing OAuth requirements, and tightening app review), so the specific API calls and flows shown in this note no longer work unmodified against today's Facebook Platform. The general integration pattern — using a 4D web area plus HTTP/JSON commands to call a third-party REST API — remains valid, but would need to be rebuilt against Facebook's current Graph API versions and permission model, ideally using 4D's improved native REST/JSON commands.
