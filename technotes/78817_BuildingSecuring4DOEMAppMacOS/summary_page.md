# Tech Note 21-21: Building and Securing 4D OEM Application on macOS

**Author:** Karim Meghraoui, Technical Services Engineer, 4D Morocco.
**Published:** November 15, 2021 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78817
**Download:** https://kb.4d.com/DLTN/TN/2021/21-21_OEMApplication.pdf

## Proposition
Distributing a 4D OEM application on macOS requires Apple code signing and notarization to avoid Gatekeeper warnings; this note walks through certificate generation, licensing tiers, and the sign/notarize process for a v19 OEM build.

## Key Points
- **Gatekeeper requirement**: any macOS app distributed outside the Mac App Store must be code-signed (and, for full trust, notarized) or users receive a security warning.
- **Certificate workflow**: Apple Developer Program enrollment → two-factor authentication → CSR generation via Keychain Access → Developer ID Application certificate download.
- **OEM license tiers**: 4D Developer OEM v19 (compile + single-user deployment) vs. 4D OEM Desktop v19 (adds SQL engine, components, Web Services client, 4D Write/View expansions).
- **License migration**: v18 OEM license numbers (4DOE/PNDP/4DDP, 4UOE, 4DOT/4DOM/4UOS) can be auto-migrated to v19 via the License Manager's Immediate Activation.
- **Build → sign → notarize pipeline**: generate the single-user OEM app, sign it with the Developer ID certificate, then submit for Apple notarization before distribution.
- **Troubleshooting section**: dedicated guidance for common code-signing failures.

## Featured Technology
- Apple Developer Program / Developer ID certificates
- Code signing (Keychain Access / Xcode)
- Apple Notarization
- 4D OEM licenses (4D Developer OEM, 4D OEM Desktop)

## Best Practices Highlighted
1. Enable two-factor authentication on the Apple Developer account before attempting certificate generation, since Apple requires it.
2. Match Xcode/macOS versions to the target signing/notarization requirements at the time of building (version-specific, so re-verify against current Apple requirements).
3. Always notarize (not just sign) OEM apps intended for internet distribution to avoid Gatekeeper friction for end users.

## Context / Positioning
This note reflects 4D's OEM/deployment tooling adapting to Apple's steadily tightening macOS security requirements (Gatekeeper, mandatory notarization), a recurring theme 4D has had to document and re-document as Apple's own tooling and policies evolved.

## Historical Commentary
**Status:** Partially Superseded

The core requirement — code signing plus notarization for any macOS app, including 4D OEM builds — remains fully in force and, if anything, more strictly enforced today than in 2021. However, the specific tooling described (Big Sur/Xcode 12.5, and implicitly the older altool/Application Loader-era submission flow) has been superseded: Apple retired altool-based notarization submission in favor of `xcrun notarytool` in November 2023, and 4D subsequently published an updated notarization Tech Note reflecting notarytool. A developer following this note today should treat the certificate/licensing concepts as still valid but consult 4D's newer notarization-specific note (and current Apple documentation) for the actual submission commands and OS/Xcode version requirements.
