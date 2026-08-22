# Tech Note 24-07: Two Factor Authentification using TOTP

**Author:** Thomas Maul, VP 4D Product Strategy, 4D Germany
**Published:** May 29, 2024 | **Product/Version:** 4D v20 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79435
**Download:** https://kb.4d.com/DLTN/TN/2024/24-07_TwoFactorAuthUsingTOTP.zip

## Proposition
Two-Factor Authentication significantly raises password security by requiring a time-limited, device-generated code alongside the password, defeating password logging and replay attacks. This note shows 4D developers how to add TOTP-based 2FA to any application, whether protected by 4D's built-in password system or a custom/external one, using freely available open-source classes.

## Key Points
- **Base32 shared secret per user:** A random 16-character base32 secret is generated per user (via Auth_tools.Random_token_base32(16)) and stored alongside their other credentials.
- **QR code as secure secret transfer:** Rather than showing the secret as plain text, a provisioningUri (otpauth://totp/...?secret=...) is generated and rendered as a QR code for the user to scan with their authenticator app.
- **30-second time-windowed hashing:** Both client authenticator and server combine the shared secret with the current 30-second time interval to produce a hash, truncated to a user-enterable 6-digit code.
- **90-second tolerance window:** To account for clock drift and user input delay, the server checks the current, previous, and next 30-second windows (90 seconds total) when validating a submitted code.
- **verify() function is the core check:** cs.TOTP.new(secret).verify(code) returns true/false, encapsulating all the time-window comparison logic.
- **Layered with existing password auth:** The example login flow checks Verify password hash first, then TOTP.verify(), requiring both factors to succeed.
- **Version-flexible implementation:** A singleton-class-based version targets 4D 20 R5+, while a documented adaptation (replacing cs.TOTP with OTP.TOTP, avoiding singleton syntax) supports 4D 20 LTS and other older versions.
- **Credited open-source foundations:** The TOTP/HOTP/OTP classes are by Eric Marchand (4D France); the qrencode plugin (supporting many QR code types beyond OTP, like URLs and payment codes) is by Keisuke Miyako (4D Japan).

## Featured Technology
- **TOTP (Time-based One-Time Password)** — the core 2FA algorithm generating time-limited 6-digit codes.
- **cs.TOTP / cs.HOTP / cs.OTP classes** — 4D class implementations of the TOTP/HOTP algorithms (github.com/mesopelagique/OTP).
- **qrencode plugin** — generates QR codes for provisioning URIs (and other data types) (github.com/miyako/4d-plugin-qrencode-v2).
- **Auth_tools singleton class** — helper providing Random_token_base32() for secret generation.
- **otpauth:// provisioning URI** — standard URI format combining account name and secret for authenticator apps to consume via QR code.

## Best Practices Highlighted
1. Verify a newly enrolled user's 2FA setup immediately (have them enter a live code) before finalizing their account, rather than assuming the QR scan succeeded.
2. Reserve 2FA prompts for sensitive actions (password changes, high-risk operations) rather than every login, to balance security and usability.
3. Store the TOTP secret securely alongside other user credential data rather than as plain, unprotected text.

## Context / Positioning
Published as security expectations for business applications continue rising, this note reflects 4D's practice of showcasing community-contributed, open-source building blocks (Eric Marchand's OTP library, Keisuke Miyako's qrencode plugin) integrated with new language features like singleton classes (from 20 R5) — demonstrating how 4D developers can quickly adopt industry-standard security practices without building cryptographic primitives from scratch.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
