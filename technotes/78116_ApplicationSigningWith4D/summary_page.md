# Tech Note 18-15: Application Signing with 4D

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** September 4, 2018 | **Product/Version:** 4D v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78116
**Download:** https://kb.4d.com/DLTN/TN/2018/18-15_AppSigning.pdf

## Proposition
Signed applications prove they haven't been tampered with and come from a trusted source — and on Windows, avoid the "Unknown Publisher" warning. This Tech Note walks through obtaining signing certificates and signing 4D-built applications on both macOS and Windows, including integrating signing into 4D's `BUILD APPLICATION` process.

## Key Points
- **Signing tradeoffs:** protects binary integrity and trust, but adds build time, may require a paid CA certificate, and adds a brief verification cost on first launch.
- **Windows certificate creation (demo):** `New-SelfSignedCertificate -Type Custom -Subject "..." -KeyUsage DigitalSignature -FriendlyName "..." -CertStoreLocation "Cert:\LocalMachine\My"` in an elevated PowerShell window, capturing the resulting thumbprint.
- **Exporting to PFX:** `ConvertTo-SecureString` creates a secure password, then `Export-PfxCertificate` exports the certificate using that password.
- **Production caveat:** the note explicitly recommends a certificate from a trusted Certificate Authority for real deployments, not the self-signed demo certificate.
- **macOS certificate acquisition:** a "Developer ID Application" certificate obtained via the Apple Developer website or directly in Xcode's account manager, requiring an active Apple Developer Program membership; located afterward in Keychain Access.
- **Signing during BUILD APPLICATION:** 4D can sign the application as part of its own build process, using the certificate name/identity.
- **Manual signing via Terminal:** `codesign -s "Developer ID Application: xyz (123)" -fvvvv "path"`, with troubleshooting guidance for "ambiguous" certificate name errors.
- **Windows signing tool:** `signtool` (from the Windows SDK) signs from the Command Prompt; the note also covers removing an existing signature.

## Featured Technology
- macOS `codesign` and Developer ID Application certificates
- Windows `signtool` (Windows SDK) and self-signed/CA certificates
- PowerShell (`New-SelfSignedCertificate`, `ConvertTo-SecureString`, `Export-PfxCertificate`)
- 4D `BUILD APPLICATION` signing integration

## Best Practices Highlighted
1. Use a certificate from a trusted Certificate Authority for production releases rather than a self-signed certificate (only appropriate for testing/demo purposes).
2. Record and carefully reuse the correct certificate thumbprint/name, since ambiguous or mismatched certificate names cause signing failures.
3. Prefer signing during 4D's `BUILD APPLICATION` step to keep signing integrated into the normal release pipeline rather than a separate manual step.

## Context / Positioning
Published as part of 4D's practical guidance for shipping polished, trustworthy desktop applications, this note reflects the growing importance (circa 2018) of code signing for both Windows SmartScreen trust and macOS Gatekeeper compatibility, at a stage before Apple's notarization requirement made signing alone insufficient.

## Historical Commentary
**Status:** Partially superseded

Code signing itself remains an essential, current requirement for distributing 4D-built applications on both platforms, and 4D's `BUILD APPLICATION` signing hook and the underlying `codesign`/`signtool` mechanics are still fundamentally how signing works today. However, this 2018 note predates two major shifts: Apple has since made **notarization** (an additional Apple-side scanning/approval step beyond signing) mandatory for apps to run smoothly under Gatekeeper on modern macOS, which this note does not address at all; and Windows SmartScreen reputation increasingly favors (or in some contexts requires) EV code-signing certificates over standard ones, a nuance not covered here either.

Developers following this note today should treat the certificate-acquisition and signing commands as broadly correct starting points, but must supplement them with current Apple notarization steps (`notarytool`/`xcrun altool` or successor) and check current Windows certificate/EV guidance to actually achieve trusted, warning-free distribution in 2026.
