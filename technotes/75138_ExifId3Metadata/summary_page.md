# Tech Note 09-04: Exif and ID3 Metadata

**Author:** Thomas Maul, 4D Germany
**Published:** January 28, 2009 | **Product/Version:** 4D v11 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75138
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_01-04_(JAN)/09-04_EXIF_Example.zip

## Proposition
Introduces a 4D component wrapping the open-source ExifTool console application to let a 4D database read and write EXIF (and read ID3) metadata tags across a broad range of image, audio, and video files.

## Key Points
- **Built on ExifTool:** wraps Phil Harvey's GPL/Artistic-licensed, platform-independent command-line tool supporting EXIF, GPS, IPTC, XMP, and many camera-specific maker notes, plus ID3.
- **Exif_ReadAllTags:** returns all discovered tags as two parallel text arrays (names and values) for a given file path.
- **Exif_WriteTags:** adds, modifies, or removes specified tags via a numeric Action parameter, with an optional flag to skip creating a backup file.
- **Date/time shifting semantics:** special tags (AllDates, DateTimeOriginal, CreateDate, ModifyDate) support adding, setting, or subtracting time values — useful for fixing camera clock/time-zone discrepancies.
- **Documented error codes:** both commands return specific negative error codes for missing parameters, invalid paths, or invalid pointer types.
- **Mac OS X gotcha:** unzipping the package on Windows before copying to Mac can strip the bundled `exiftool` binary's Unix-executable permission, breaking the component until reset (chmod or native Mac extraction).
- **Test dialog included:** a development-only `Exif_test` method helps explore a file's tags but should not ship in a deployed application.

## Featured Technology
- Exif_Component wrapping the open-source ExifTool console application (Phil Harvey, GPL/Artistic license)
- Exif_ReadAllTags / Exif_WriteTags component commands returning parallel text arrays of tag names/values
- LAUNCH EXTERNAL PROCESS-based bridge to a bundled command-line binary
- Date/time tag shifting semantics (AllDates/DateTimeOriginal/CreateDate/ModifyDate)

## Best Practices Highlighted
1. Wrap capable, well-maintained open-source command-line tools (like ExifTool) rather than re-implementing complex binary metadata formats in 4D.
2. Preserve automatic backups when writing tags unless you already maintain your own backup strategy.
3. Re-extract cross-platform-transferred packages natively on the target OS to avoid losing Unix executable permissions on bundled binaries.
4. Remove development-only test/debug dialogs before shipping a final application.

## Context / Positioning
Written to give 4D developers turnkey access to rich photo/media metadata (useful for photo management, digital asset workflows, etc.) by leaning on a proven external open-source tool rather than building parsing logic from scratch.

## Historical Commentary
**Status:** Still Relevant

The core approach — wrapping an external command-line utility like ExifTool via LAUNCH EXTERNAL PROCESS to gain metadata capability 4D doesn't natively provide — remains a valid and still-used integration pattern, and ExifTool itself continues to be actively maintained today.

The main thing that has changed is macOS's security model: modern code-signing, notarization, and Gatekeeper requirements now govern how a bundled external executable must be packaged and launched, well beyond the simple Unix-executable-permission fix described in this 2009-era note, so developers reusing this pattern today need to account for those additional OS-level requirements.
