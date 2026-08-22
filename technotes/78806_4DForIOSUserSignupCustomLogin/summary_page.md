# Tech Note 21-18: 4D for iOS: User Signup & Custom Login Form

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** October 28, 2021 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78806
**Download:** https://kb.4d.com/DLTN/TN/2021/21-18_4DiOSCustomLogin.zip

## Proposition
Builds a DishDoc iOS recipe app in 4D's now-retired native mobile generator, showing secure user signup (via a web form and hashed password storage) and a custom login tied to per-user ORDA REST data filtering.

## Key Points
- **4D for iOS**: a since-discontinued native mobile app generator; DishDoc is built entirely through its Mobile Project editor.
- **Security posture**: passwords are stored as a hash (`pwhash` field), not plaintext, and the Users table/fields are explicitly excluded from REST exposure.
- **Per-user data filtering**: a Data-section filter query (`user.email = :userEmail`) restricts each authenticated user's visible recipes to their own.
- **On Mobile App Authentication**: authenticates the request's email against Users and returns a `userInfo` object (userEmail, userID) consumed by later actions.
- **On Mobile App Action**: reads `$request.userInfo.userID` to correctly attribute new records created by the authenticated user (e.g., addRecipe).
- **Web-based signup flow**: a plain HTML form served via `WEB SEND FILE`/`On Web Connection` posts to a `/4DACTION/processForm` method for parsing, validation, and secure storage of new credentials.

## Featured Technology
- 4D for iOS (4D Mobile app generator)
- On Mobile App Authentication / On Mobile App Action
- Web-based signup form (WEB SEND FILE, On Web Connection)
- Password hashing (pwhash field)

## Best Practices Highlighted
1. Never expose a Users/credentials table (or its fields) as a REST resource; keep authentication data entirely server-side.
2. Store only a password hash, never the raw password, and validate/sanitize signup form input server-side before saving.
3. Tie per-user data visibility to authenticated identity via filter queries plus the mobile authentication callback's returned context, not client-side assumptions.

## Context / Positioning
This note captures 4D's mobile strategy at a moment when native app generation (4D for iOS/Android) was still a flagship offering, paired with genuinely solid security guidance (hashed passwords, REST exposure restrictions, server-side filtering) that reflects sound practice independent of the specific mobile product used to deliver it.

## Historical Commentary
**Status:** Obsolete

The delivery mechanism is now obsolete: 4D for iOS (the native mobile app generator) was discontinued in favor of Qodly Studio and responsive ORDA/REST web apps, so the Mobile Project editor steps, On Mobile App Authentication/Action mechanics, and mobile-specific publishing workflow shown here no longer apply to current 4D development. However, the security substance of the note — hashed password storage, excluding credential tables from REST exposure, and authenticated per-user data filtering via ORDA queries — remains fully valid guidance that a developer building an equivalent REST/ORDA web app today should still follow, just without the 4D for iOS wrapper.
