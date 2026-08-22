# Tech Note 22-15: Custom Zip Utility for a 4D Solution

**Author:** Add Komoncharoensiri, Director of Technical Services, 4D Inc.
**Published:** August 22, 2022 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78988
**Download:** https://kb.4d.com/DLTN/TN/2022/22-15_ZipUtility.zip

## Proposition
4D has natively supported ZIP compression since v18 via ZIP Create archive and ZIP Read archive. This note wraps those commands into a ready-to-use compress/uncompress utility — both a drag-and-drop UI and a simple zipItems()/unzipItem() programmatic API — including optional AES-256 password protection.

## Key Points
- **Built entirely on native 4D commands** ZIP Create archive and ZIP Read archive, available since 4D v18 — no external compression tooling required.
- **zipItWindow opens a drag-and-drop Compress/Uncompress UI**; single-item compression names the ZIP after the source, multi-item compression produces Archive.zip.
- **Password protection defaults to AES 256-bit encryption**, selectable to alternate encryption methods from a dropdown.
- **zipItems(parameter : Object) -> zipPath : Text** is the headless API: parameter.files (collection of paths), parameter.password, and parameter.encryption (e.g. ZIP Encryption AES256).
- **unzipItem(parameter : Object) -> $result : Integer** is the extraction counterpart: srcPath, desPath, and optional password.
- **The Uncompress utility previews archive contents in a list box** before extracting individually or all at once, defaulting the destination to the ZIP's own folder.

## Featured Technology
- ZIP Create archive / ZIP Read archive (native commands, v18+)
- AES 256-bit password encryption
- zipItWindow utility UI
- zipItems() / unzipItem() project methods

## Best Practices Highlighted
1. Use the headless zipItems()/unzipItem() methods for automated workflows (e.g. batch export/backup) and reserve the UI utility for interactive end-user use.
2. Default to AES-256 encryption when password-protecting archives containing sensitive data.

## Context / Positioning
Published under 4D v19 (August 2022), this note is a classic 'convenience wrapper' technical note: it adds no new 4D language capability, instead packaging existing native commands (ZIP Create archive/ZIP Read archive, present since v18) into a friendlier, ready-to-integrate utility for common developer needs like data transfer and storage-space reduction.

## Historical Commentary
**Status:** current

The underlying ZIP Create archive / ZIP Read archive commands remain fully current, native 4D language features with no deprecation or replacement; this utility wrapper is simply a sample implementation on top of stable commands, so both the technique and the specific commands referenced are still valid to use today exactly as described.
