# Tech Note 23-11: Updated Notarization Guide using Notary Tools

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** June 27, 2023 | **Product/Version:** 4D v19 R | **Platform:** Mac
**Page:** https://kb.4d.com/assetid=79226
**Download:** https://kb.4d.com/DLTN/TN/2023/23-11_Updated_Notarization.pdf

## Proposition
Apple stopped accepting apps notarized with `altool`/Xcode 13 or earlier starting November 1, 2023, forcing 4D Mac developers who build/engine and distribute apps over the internet to switch to the modern `notarytool` CLI. This note provides an updated, from-scratch walkthrough of the new notarization workflow.

## Key Points
- **When notarization is required:** only when the 4D app is built/engined on macOS, distributed over the internet (FTP, website, etc.), and will be opened on another Mac — interpreted/compiled databases and USB/LAN distribution are exempt.
- **Prerequisites:** an active Apple Developer Program enrollment, an app-specific password from the Apple ID account page, and a "Developer ID Application" signing certificate generated via Keychain Access' Certificate Assistant and imported after approval on the Apple Developer portal.
- **Credential storage:** Apple ID email, Team ID, and app-specific password are stored once via `xcrun notarytool store-credentials "<name>" --apple-id ... --team-id ... --password ...` and referenced afterward by keychain-profile name.
- **Submission:** `xcrun notarytool submit "<archived app>" --keychain-profile "<name>" --wait` uploads a ZIP/DMG-archived build and blocks until Apple returns Accepted or a failure status.
- **Failure diagnosis:** on failure (or even success, to check for warnings), pull the detailed report with `xcrun notarytool log "<uploadID>" --keychain-profile "<name>" developer_log.json`.
- **Stapling:** `xcrun stapler staple "<app>"` attaches the notarization ticket to the app bundle so Gatekeeper can verify it without a network connection.
- **Final packaging:** after stapling, re-archive (ZIP/DMG) the app for distribution to end users.

## Featured Technology
- **xcrun notarytool** — Apple's modern CLI for submitting apps to the notary service and retrieving results/logs (replaces `altool`).
- **Keychain Access** — used both to generate the Developer ID Application certificate and to securely store notarization credentials.
- **Developer ID Application certificate** — the code-signing certificate type required for notarizable Mac apps.
- **xcrun stapler** — attaches the notarization ticket to the app for offline Gatekeeper verification.

## Best Practices Highlighted
1. Store Apple ID/Team ID/app-specific password once in the keychain via `store-credentials` rather than passing raw credentials on every notarization call.
2. Always inspect the `developer_log.json` even after a successful submission to catch non-fatal warnings.
3. Staple the ticket after every successful notarization so the app remains verifiable without network access.

## Context / Positioning
Published as Apple tightened notarization tooling requirements ahead of its November 2023 `altool` deprecation deadline, this note reflects 4D's ongoing commitment to keeping Mac deployment guidance current with Apple's platform requirements, ensuring 4D-built and engined applications remain distributable and Gatekeeper-compliant.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
