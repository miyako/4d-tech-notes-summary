# Tech Note 25-01: Using Apple's "notarytool" to Notarize Applications

**Author:** Brianna Rentfrow, Technical Services Engineer, 4D Inc.
**Published:** January 16, 2025 | **Product/Version:** 4D v20 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79622
**Download:** https://kb.4d.com/DLTN/TN/2025/25-01_Notarization.pdf

## Proposition
Apple requires notarization for any macOS application distributed outside the App Store — without it, users see "can't be opened because Apple cannot check it for malicious software" errors. This note shows 4D developers how to use Apple's newer, faster "notarytool" to sign, notarize, and staple built 4D applications with minimal friction.

## Key Points
- **Requirements are specific:** macOS 11.3+, 4D 18+, Xcode 13+, and an Apple Developer account with a Developer ID Application Certificate and App-Specific Password.
- **Build and sign first:** Compile via Design → Compiler, then Build Application with the "Sign Application" checkbox enabled and the exact certificate name pasted in under Licenses and Certificate.
- **One-time keychain profile setup:** `xcrun notarytool store-credentials --apple-id "EMAIL" --team-id "TEAMID"` stores credentials under a named profile (e.g., "notaryTN") so future commands avoid re-entering the app-specific password.
- **Extra files need manual signing:** For files not automatically signed by 4D's build (e.g., added resources), a bundled shell script using `codesign --options=runtime --timestamp --entitlements` plus a LAUNCH EXTERNAL PROCESS call handles the extra signing pass.
- **Compiled databases need a manual dylib signing step:** "lib4d-arm64.dylib" inside a Compiled Database isn't signed correctly by 4D and must be signed directly with `codesign -s [IDENTITY] -o library`.
- **Single-command notarization:** `xcrun notarytool submit "[ZIP]" --keychain-profile "notaryTN" --wait` handles the full submission and polling.
- **Log inspection for failures:** `xcrun notarytool log "[ID]" --keychain-profile "notaryTN" developer_log.json` reveals rejection reasons or warnings.
- **Stapling finalizes distribution:** `xcrun stapler staple [PATH]` attaches the notarization ticket to .app/.dmg/.pkg files (not supported for .4dbase components) so the app can run offline on first launch.

## Featured Technology
- **xcrun notarytool** — Apple's modern CLI tool for submitting apps for notarization and querying logs.
- **codesign** — command-line code signing tool, used both automatically by 4D and manually for extra files/libraries.
- **Apple Developer ID Application Certificate** — the certificate required to sign apps for distribution outside the App Store.
- **Keychain profile credentials** — securely stored Apple ID/team ID/app-specific password referenced by name in later commands.
- **xcrun stapler** — attaches the notarization ticket to the built application for offline Gatekeeper validation.
- **LAUNCH EXTERNAL PROCESS** — 4D command used to invoke the custom signing shell script from within the application.

## Best Practices Highlighted
1. Set up the keychain profile once so it can be reused for every future notarization without re-entering credentials.
2. Manually sign the lib4d-arm64.dylib library inside compiled databases, since 4D does not sign it correctly by default.
3. Always check the notarization log when a submission fails, as it contains the specific rejection reason.
4. Re-zip and resubmit compiled database packages after manual dylib signing before notarization.

## Context / Positioning
Published as Apple continues tightening macOS security requirements (including newer wording on macOS Sequoia), this note keeps 4D's build/deployment guidance current with Apple's latest notarization tooling, reflecting 4D's ongoing commitment to smooth, secure desktop deployment workflows for both new and legacy compiled database projects.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
