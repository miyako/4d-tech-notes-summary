# Tech Note 10-11: Password Wizard

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc.
**Published:** April 9, 2010 | **Product/Version:** 4D v11.6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76079
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_11-14_(APR)/10-11_PasswordWizard.zip

## Proposition
This note explains the theory behind secure passwords (entropy, cryptographic strength, brute-force recovery time) and delivers a 4D v11 SQL component, "Password Wizard," that generates passwords by three methods and encrypts them into BLOBs for safe storage in a 4D data file.

## Key Points
- Covers **password entropy** and how to calculate it, plus the time required to recover (brute-force) a password of a given strength.
- Three password-generation techniques: **user-entered with dynamic rating**, **pattern-based generation**, and **fully random generation** from developer-defined criteria.
- Provides **encrypted BLOB storage** for passwords, using public/private key pairs kept inside the component.
- API includes methods like `PW_By_User_Rated`, `PW_By_Pattern`, `PW_By_Machine`, `PW_GenerateKeyPair`, and `PW_EncryptPassword`.
- Includes **host database callbacks** to integrate the component with a calling application.
- Demonstration database shows Password by User, Password by Pattern, and Password by Machine workflows.

## Featured Technology
- 4D v11 SQL Password Wizard component
- Password entropy calculation
- PW_GenerateKeyPair / PW_EncryptPassword
- BLOB-based encrypted password storage

## Best Practices Highlighted
1. Rate user-chosen passwords dynamically to encourage stronger choices rather than trusting users to self-select secure passwords.
2. Store passwords encrypted as BLOBs rather than in plain text, keeping keys out of easily-scanned locations.
3. Offer pattern-based or fully-random generation options for scenarios where user memorability is less critical than raw strength.

## Context / Positioning
Published as a companion tool for developers building authentication into their own 4D v11 SQL applications, addressing a perennial concern (weak user-chosen passwords) with a ready-made, drop-in component.

## Historical Commentary
**Status:** Partially Superseded

This note explains password entropy theory and provides a self-contained 4D component for generating, rating, and encrypting passwords for storage as BLOBs in a 4D data file. The underlying cryptographic and entropy concepts are timeless and the classic-language component would still technically function.

However, modern secure-password practice has moved toward standardized, vetted algorithms (bcrypt/scrypt/Argon2, or platform-provided credential/keychain APIs) rather than a bespoke home-grown key-pair/BLOB scheme, and 4D now offers built-in encryption commands unavailable in 2010. Developers building new authentication today should prefer current cryptographic libraries and 4D's built-in security features over this legacy component.
