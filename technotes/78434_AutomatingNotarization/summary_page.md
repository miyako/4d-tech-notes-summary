# Tech Note 20-04: Automating Notarization

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** March 25, 2020 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78434
**Download:** https://kb.4d.com/DLTN/TN/2020/20-04_AutomatingNotarization.zip

## Proposition
Manually notarizing a macOS app build-by-build is time consuming. This note packages the whole notarization workflow — DMG creation, signing, upload, status polling, and stapling — into a single Bash script, after first teaching the shell-scripting fundamentals needed to understand and customize it.

## Key Points
- **Shell scripting primer**: shebang (`#!/bin/bash`), comments, `echo`, variables, parameter substitution, `sleep`, command substitution, arithmetic expansion, if/else, while loops, case statements — framed for 4D developers new to terminal scripting.
- **DMG creation & signing**: `hdiutil create -format UDBZ` builds the DMG; `codesign` signs it using a certificate auto-detected via `security find-identity -p codesigning`.
- **Upload to notary service**: `xcrun altool --notarize-app --file ... --primary-bundle-id ...` uploads the DMG and returns a `RequestUUID`, parsed from an XML plist output using `PlistBuddy`.
- **Polling loop**: a `while` loop calls `xcrun altool --notarization-info` every 60 seconds, using a `case` statement on status ("success" / "in progress" / other) to decide whether to staple, keep waiting, or exit with failure.
- **Stapling & verification**: on success, `xcrun stapler staple` attaches the notarization ticket and `spctl -at open` verifies the result.
- **Script parameters**: the finished script takes two arguments — source folder/app path and bundle ID — with Apple ID credentials configured as variables at the top.

## Featured Technology
- Bash shell scripting
- `xcrun altool` (Apple notary service, 2020-era)
- `hdiutil`, `codesign`, `stapler`, `spctl`
- `PlistBuddy` for plist parsing

## Best Practices Highlighted
1. Auto-detect the signing certificate rather than hardcoding it, so the script adapts to different developer machines.
2. Poll notarization status on a fixed interval with clear success/in-progress/failure branches rather than blocking indefinitely.
3. Track and display elapsed time during polling to give visibility into how long notarization is taking.

## Context / Positioning
Published as Catalina's notarization requirement made manual per-build notarization untenable, this note fits 4D's practice of teaching adjacent platform/OS skills (here, Bash scripting) that 4D developers increasingly needed as Apple tightened distribution security requirements — complementing 4D's own app-signing features.

## Historical Commentary
**Status:** Partially superseded

The Bash scripting fundamentals and overall automation pattern (build → sign → upload → poll → staple) are still exactly how notarization automation is done today and remain fully valid teaching material. However, the specific tool automated here, `xcrun altool` with `--notarize-app`/`--notarization-info`, was deprecated by Apple and has been fully replaced by `xcrun notarytool`, which is mandatory on current Xcode/macOS toolchains (Apple shut down the old notarization API in late 2023). A developer automating notarization today would need to rewrite the upload/poll/staple commands around `notarytool` (which also simplifies credential handling via keychain profiles), but the script's overall structure and teaching value carry over directly.
