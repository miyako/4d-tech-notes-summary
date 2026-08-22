# Tech Note 21-01: Managing and Encrypting 4D Data Files

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** January 25, 2021 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78634
**Download:** https://kb.4d.com/DLTN/TN/2021/21-01_DataEncryption.pdf

## Proposition
4D data files (.4DD) are, by default, stored in a proprietary but non-encrypted binary format whose field contents can be extracted with a plain hex editor. This Tech Note explains the 4D data file's lifecycle and placement best practices, then details 4D v18's new datafile encryption feature (AES + SHA-256 passphrase), covering both the UI (Maintenance and Security Center) and programmatic (`Encrypt data file`, keychains) workflows.

## Key Points
- **Data file basics**: `.4DD` files are separate from the structure/project, allow reuse of one structure across multiple data sets, and are tracked per-user via a `.4Dlink` favorites file.
- **Placement guidance**: keep data files on fast (SSD) storage; for deployed apps, consider placing them outside the app package for easier updates and, for security, off the same exposed machine.
- **Unencrypted risk demonstrated**: a hex-editor (HxD) view shows field values are human-readable in a plain data file.
- **Per-table "Encryptable" flag**: set in the Structure Editor (or via XML edits to `catalog.4DCatalog` in Project mode using DOM commands).
- **AES-256 + SHA-256 passphrase**: encryption is applied via the MSC "Encrypt" tab (with a passphrase-strength meter) or the `Encrypt data file` command.
- **Key management**: passphrases become AES keys optionally exported as `.4DKeyChain` JSON files; multi-key "Master" keychains can unlock several data files.
- **Runtime unlocking chain**: 4D tries an in-memory keychain, then a `.4DKeyChain` on a connected drive, then explicit code (`Discover data key`, `ds.provideDataKey()`, or legacy `Register data key`).
- **Re-encryption / passphrase rotation / decryption**: all performed via MSC or the `Encrypt data file` command with different parameter combinations, always producing a "Replaced Files…" backup.

## Featured Technology
- 4D Data File (.4DD) architecture and `.4Dlink` favorites
- Maintenance and Security Center (MSC) Encrypt tab
- `Encrypt data file`, `New data key`, `Discover data key`, `Register data key` commands
- `ds.provideDataKey()` datastore function
- `.4DKeyChain` JSON keychain files
- DOM XML commands for editing `catalog.4DCatalog` in Project mode

## Best Practices Highlighted
1. Keep production data files on fast local storage separate from the structure/project for both performance and update-friendliness.
2. Only mark genuinely sensitive tables as "Encryptable" since encryption/decryption overhead scales with data volume.
3. Never hardcode a decryption passphrase in source code, as this defeats the purpose of encryption.
4. Always retain the "Replaced Files…" backup produced during any encryption/re-encryption operation.

## Context / Positioning
Published right after 4D v18's release, this note documents a genuinely new security feature (at-rest datafile encryption) aimed at customers with compliance or data-sensitivity requirements (e.g., handling personal or financial data). It reflects 4D's ongoing effort to compete on enterprise-readiness by adding database-level security controls comparable to other RDBMS/embedded database products, alongside the era's broader push toward Project mode and ORDA-based data access.

## Historical Commentary
**Status:** Still relevant

4D data file encryption as introduced in v18 remains the current, supported mechanism for at-rest table-level encryption in 4D and has not been replaced by a newer feature — this Tech Note's core content (AES-256/SHA-256 design, MSC-based encryption workflow, keychain unlocking chain) is still accurate today. The one area that has aged is styling emphasis: the object-notation form `ds.provideDataKey()` has become the default idiomatic way to unlock a data file programmatically, while the older `Register data key` command shown as an alternative is now more of a legacy/compatibility option, consistent with 4D's broader multi-year shift toward ORDA/object notation. The Project-mode-only trick of editing `catalog.4DCatalog` XML to toggle "Encryptable" is still valid, and is increasingly the only mode developers use since 4D has continued to invest exclusively in Project mode over binary/Design mode.
