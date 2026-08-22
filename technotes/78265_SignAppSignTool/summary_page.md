# Tech Note 19-08: Sign a 4D App Package using SignTool on Windows

**Author:** Karim Meghraoui, Technical Services Engineer, 4D Inc.
**Published:** May 30, 2019 | **Product/Version:** 4D v17 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78265
**Download:** https://kb.4d.com/DLTN/TN/2019/19-08_SignAppUsingSignTool.pdf

## Proposition
Digitally signing a Windows application package proves it hasn't been tampered with and confirms the developer's identity to end users and antivirus software. This note walks through generating a certificate and signing a merged 4D executable using Microsoft's SignTool.

## Key Points
- **Why sign:** an unsigned `.exe` can trigger antivirus warnings; signing guarantees the package matches what the developer originally built.
- **Generation:** `New-SelfSignedCertificate` (PowerShell, admin mode) creates a certificate with `DigitalSignature` key usage and a friendly name, stored in the local certificate store.
- **Export:** via MMC (Certificates > Personal > Certificates), export the private key as a password-protected PFX, choosing TripleDES-SHA1 or AES256-SHA256 encryption.
- **Signing:** `signtool.exe sign` with distinct syntax for SHA1 (VeriSign timestamp server) vs. SHA256 (Symantec SHA256 timestamp server).
- **Verification:** `signtool.exe verify /v "file"` checks an existing signature.
- **Default state:** 4D's own executables already ship self-signed with both SHA1 and SHA256.

## Featured Technology
- SignTool (Windows SDK)
- PowerShell `New-SelfSignedCertificate`
- Microsoft Management Console (MMC) certificate export
- SHA1/SHA256 signing algorithms

## Best Practices Highlighted
1. Always sign distributed Windows executables to avoid antivirus/SmartScreen friction and provide tamper evidence.
2. Apply a trusted timestamp during signing so the signature remains valid after the certificate itself expires.
3. Verify the signature with `signtool.exe verify` after signing to confirm correctness.

## Context / Positioning
This is a practical deployment/operations note addressing a real-world friction point (Windows security warnings on unsigned executables) for 4D developers shipping compiled Windows applications, part of 4D's ongoing series of packaging/distribution guidance alongside topics like notarization for macOS.

## Historical Commentary
**Status:** Partially superseded

SignTool remains the correct, current Windows code-signing tool, but two details have shifted since 2019: SHA1 signing is now deprecated and no longer trusted by modern Windows/browsers, making SHA256 (or newer) mandatory rather than optional; and self-signed certificates, as generated in this walkthrough, are suitable only for local testing — real-world public distribution requires a certificate issued by a trusted Certificate Authority (ideally an EV code-signing certificate) to avoid SmartScreen warnings. A developer following this note today should skip the SHA1 path entirely and obtain a CA-issued certificate rather than a self-signed one for production distribution.
