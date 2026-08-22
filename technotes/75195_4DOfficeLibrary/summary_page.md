# Tech Note 09-08: 4D Office Library

**Author:** Silvio Belini, Technical Services Team Member, 4D Inc.
**Published:** February 26, 2009 | **Product/Version:** 4D v11 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75195
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_05-08-(FEB)/09-08_4D_Office_Library.zip

## Proposition
Introduces the 4D Office Library component, which generates Word/Excel documents in the new Office Open XML format and synchronizes contacts/appointments with Outlook (Windows) or Address Book (Mac), directly from a 4D v11 SQL output form.

## Key Points
- **Office Open XML generation:** builds the required XML "parts" (document.xml, sheet1.xml, styles.xml, relationship files, etc.) with 4D DOM commands, following the documented Office 2007/2008 file format.
- **ZIP packaging via external process:** compresses the generated parts using the Mac `zip` command or bundled 7-zip on Windows via `LAUNCH EXTERNAL PROCESS`, then renames the archive to .docx/.xlsx.
- **Drag-and-drop field binding:** a GUI on output forms lets users drag table fields onto the target Word/Excel/Outlook area to bind data, with options for titles, watermarks, backgrounds, logos, and colors.
- **Outlook/Address Book bridge:** dynamically generates and runs VBScript (`cscript`) or AppleScript (`osascript`) files to import/export contacts and import appointments within a date range, parsing tab/line-delimited standard output back into 4D records.
- **Platform-specific requirements:** needs Office 2007 (Win) / 2008 (Mac), or the MS Compatibility Pack for older Office; 7-zip is bundled for Windows.
- **Simple installation:** drop the compiled component into the host database's Components folder next to the structure file.

## Featured Technology
- 4D Office Library component generating Office Open XML (.docx/.xlsx) via DOM XML commands
- Command-line zip (Mac) / 7-zip (Windows) invoked via LAUNCH EXTERNAL PROCESS to package OOXML containers
- VBScript (cscript) / AppleScript (osascript) bridges for Outlook and Address Book contact/appointment import-export
- Drag-and-drop field-binding GUI on output forms for Word/Excel/Outlook integration

## Best Practices Highlighted
1. Reuse the zip container's pre-existing (non-generated) XML parts rather than recreating every Office XML file from scratch, to minimize component complexity.
2. Route Outlook/Address Book automation through generated scripts and standard output parsing rather than direct COM/AppleEvent calls, for portability across the two OS scripting environments.
3. Provide the Microsoft Compatibility Pack path for users on older, non-OOXML-native Office versions.

## Context / Positioning
Positioned as the v11 SQL successor to the 4D 2004 Office Object Library, updated for the industry's shift to the ZIP/XML-based Office Open XML formats adopted by Office 2007/2008.

## Historical Commentary
**Status:** Obsolete

This component's core techniques — hand-assembling Office Open XML parts with DOM commands, shelling out to zip/7-zip, and generating VBScript/AppleScript files to talk to Outlook/Address Book — reflect the workaround-heavy integration style of the pre-native-document-generation era.

4D has since introduced native document and spreadsheet generation (4D Write Pro and 4D View Pro, roughly v16-18+), eliminating the need to hand-build OOXML containers, and OS-level scripting bridges to desktop mail/calendar clients have been largely superseded industry-wide by REST/Graph-based calendar and contacts APIs. A developer implementing this functionality today would very likely use 4D's native document tools and a modern API-based integration rather than this component's approach.
