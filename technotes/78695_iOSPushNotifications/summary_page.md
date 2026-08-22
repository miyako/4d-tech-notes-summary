# Tech Note 21-07: 4D for iOS: Push Notifications and Beyond

**Author:** Not specified (unavailable — full PDF could not be retrieved)
**Published:** April 29, 2021 | **Product/Version:** 4D for iOS v18 R6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78695
**Download:** https://kb.4d.com/DLTN/TN/2021/21-07_iOSPushNotification.zip

## Proposition
This note revisits 4D for iOS — 4D's tool for generating native iOS apps from a 4D database — to cover several advanced features added since the original introductory tech note: restricted queries, custom relation buttons, push notifications, and deep linking.

*(Note: full technical detail unavailable — this summary is based on the published abstract/teaser only, as the original demo download could not be retrieved due to server-side truncation of the large legacy file.)*

## Key Points
- Builds on an earlier, more basic 4D for iOS tech note that covered simple CRUD app generation.
- **Restricted queries** — likely a mechanism to scope which records a mobile user can access.
- **Custom relation buttons** — UI elements for navigating related records beyond default generated forms.
- **Push notifications** — enabling the generated native iOS app to receive alerts, presumably via APNs integration configured through 4D's mobile publishing settings.
- **Deep linking** — also covered in more depth in the companion Tech Note 21-10 from the same year.

## Featured Technology
- 4D for iOS (native app generation)
- Push Notifications (APNs, inferred)
- Restricted queries
- Custom relation buttons
- Deep linking

## Best Practices Highlighted
(Not available — full PDF content could not be retrieved to identify specific implementation guidance.)

## Context / Positioning
Published in the same wave as several other 4D for iOS tech notes in 2021 (including the deep-linking note, TN 21-10), this reflects 4D's mid-2021 investment in expanding its native mobile app generation feature with more advanced platform capabilities, aiming to make 4D for iOS competitive as a low-code mobile development option.

## Historical Commentary
**Status:** Obsolete

4D for iOS — the entire product this tech note is built around — has since been discontinued, along with the parallel 4D for Android line. 4D's mobile strategy moved to Qodly (a separate low-code platform) and to responsive ORDA/REST-based web apps usable from mobile browsers. Regardless of the specific push-notification mechanism this note originally described, the underlying product is no longer offered, so none of this guidance is directly actionable today. A developer needing mobile push notifications for a 4D-backed application now would build a native/hybrid or PWA client that calls a push service (APNs/FCM) directly, integrating with 4D purely through REST/ORDA APIs rather than through the retired native-app generator.
