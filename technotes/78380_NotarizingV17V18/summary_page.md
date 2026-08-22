# Tech Note 19-22: Notarizing a Built 4D Application in v17 and v18

**Author:** Erick Lui, Technical Services Engineer, 4D Inc.
**Published:** December 30, 2019 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78380
**Download:** https://kb.4d.com/DLTN/TN/2019/19-22_Notarization.zip

## Proposition
macOS Catalina's mandatory notarization hit 4D developers differently depending on version: v18's improved "Sign application" build feature made notarization nearly turnkey, while v17 required a much more manual "signing inside out" process to avoid stale nested signatures. This note documents both paths.

## Key Points
- **v18 turnkey flow**: check "Sign application" at build time, verify with `spctl -av`, zip/DMG the app, generate an app-specific Apple ID password, upload via `xcrun altool --notarize-app`, poll with `--notarization-history`/`--notarization-info`, staple with `stapler staple`, and re-verify.
- **v17 signature staleness problem**: a v17 app signed via "Sign application" retains outdated signatures on inner binaries, which fail notarization checks under Catalina's stricter rules.
- **Entitlements**: v17's manual path requires authoring an entitlements property list governing sandboxing/hardened-runtime permissions.
- **Signing inside out**: v17 requires individually re-signing, from innermost to outermost, each of Native Components, Frameworks, SASL Plugins, Resources, and finally the top-level MacOS executable.
- **Automation**: the note shows wrapping the many individual `codesign` calls required for v17's inside-out process into a single script.
- **Verification loop**: `spctl -av` before and after, plus checking `LogFileURL` output for any notarization warnings.

## Featured Technology
- macOS Gatekeeper / notarization (2019-era `xcrun altool` workflow)
- `codesign`, entitlements property lists
- `stapler`, `spctl`

## Best Practices Highlighted
1. Prefer upgrading to 4D v18 where possible, since its "Sign application" feature avoids the entire manual inside-out signing process required in v17.
2. When signing manually, always work from the innermost nested binary outward to avoid invalidating already-applied signatures.
3. Confirm both signature validity (`spctl -av`) and staple success independently after notarization completes.

## Context / Positioning
This note captures a pivotal moment where Apple's Catalina notarization mandate forced 4D to rapidly harden its own application-signing pipeline; it documents the practical gap between an older 4D version's signing capability and a newer one specifically built to meet the new OS requirement, useful context for understanding why upgrading 4D versions mattered for macOS compliance at the time.

## Historical Commentary
**Status:** Partially superseded

The `xcrun altool` notarization workflow described here (`--notarize-app`, `--notarization-info`, `--notarization-history`) is deprecated; Apple has fully retired the underlying API in favor of `xcrun notarytool`, which uses different commands and credential handling (keychain profiles instead of inline Apple ID/app-specific passwords). The v17-specific "signing inside out" manual entitlements workflow is now mostly historical, since current 4D versions build on signing improvements that trace back to the v18 approach highlighted here. The core lesson — keep 4D and its build tooling current to avoid fighting Apple's evolving security requirements — remains as true today as it was in 2019, even though the exact commands shown need updating to `notarytool` for current use.
