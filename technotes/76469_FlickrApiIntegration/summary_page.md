# Tech Note 12-02: Flickr API Integration with 4D v13

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** January 31, 2012 | **Product/Version:** 4D v13.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76469
**Download:** https://kb.4d.com/DLTN/TN/2012/12-02_FlickrIntegration.zip

## Proposition
This Tech Note demonstrates integrating the Flickr photo-sharing API into a 4D application using the brand-new 4D v13 HTTP Client feature, covering authentication, request signing, and photo upload end to end.

## Key Points
- Introduces the concept of an HTTP Client and summarizes 4D v13's five new HTTP Client commands.
- Details Flickr API integration requirements and implementation guidelines.
- Covers the Flickr authentication process, including obtaining and renewing authentication tokens.
- Explains how to sign outgoing requests as required by Flickr's API.
- Demonstrates uploading photos to Flickr via HTTP POST built with the new commands.
- Briefly surveys other available Flickr API calls beyond photo upload.

## Featured Technology
- 4D v13 new HTTP Client commands
- Flickr REST-style API
- Token-based authentication and request signing
- HTTP POST for file/photo upload

## Best Practices Highlighted
1. Handle authentication token renewal explicitly rather than assuming a token remains valid indefinitely.
2. Sign requests exactly according to the third-party API's requirements to avoid authentication failures.
3. Structure HTTP Client calls into implementation guidelines/abstractions rather than ad hoc one-off calls.

## Context/Positioning
Published alongside 4D v13's introduction of native HTTP Client commands in 2012, this note showcased a concrete, popular third-party API (Flickr) to demonstrate the new feature's real-world capability for consuming external REST-style services.

## Historical Commentary
4D's HTTP Client commands remain part of the current classic language and still work as a valid way to call external REST APIs, so the core integration technique here is still functionally usable. Modern 4D development typically pairs such HTTP calls with native JSON parsing (added years after this note) for cleaner response handling, and Flickr's actual authentication requirements may have changed independently since 2012, so the specific auth flow shown should be verified against current Flickr documentation before reuse.

**Status:** Still relevant
