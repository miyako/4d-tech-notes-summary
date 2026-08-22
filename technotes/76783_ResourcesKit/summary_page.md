# Tech Note 13-03: Resources Kit

**Author:** Keisuke Miyako, Sales Engineer, 4D-Japan
**Published:** March 6, 2013 | **Product/Version:** 4D v12.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76783
**Download:** https://kb.4d.com/DLTN/TN/2013/13-03_ResourcesKit.zip

## Proposition
This Tech Note introduces the Resources Kit, an open-source 4D utility database created by Keisuke Miyako of 4D-Japan (released via sources.4d.com and GitHub) that helps developers convert legacy 4D resource-based assets — pictures stored in resource files, Win4dx/Mac4dx plugin resources, and string resources/constants — into modern formats, notably converting old .rsr/.rsrc files to XLIFF.

## Key Points
- Targets developers still relying on legacy resource files (.rsr/.rsrc) or Win4dx/Mac4dx plugins for pictures, strings, and constants.
- Provides a utility database for batch-converting many types of legacy 4D resources.
- Highlights conversion of old resource files to the XLIFF localization format, useful for internationalized applications.
- Notes the source code is publicly available on GitHub for inspection and reuse.
- Developed and tested against 4D v12.

## Featured Technology
- Resource files (.rsr/.rsrc)
- Win4dx/Mac4dx plugins
- XLIFF format
- 4D Resources Kit utility database (open source, GitHub)

## Best Practices Highlighted
1. Migrate away from binary resource-file-based assets toward text-based, tool-friendly formats like XLIFF.
2. Use open-source community utilities to automate one-time migration tasks rather than hand-converting resources.

## Context/Positioning
Published for 4D v12.5 to help the developer community modernize legacy Mac/Windows resource-fork-based assets as 4D and the underlying OSes moved away from classic resource forks and toward cross-platform, text-based resource formats.

## Historical Commentary
**Status:** Obsolete

The specific legacy artifacts this tool targets — .rsr/.rsrc resource files and Win4dx/Mac4dx plugins — are themselves long obsolete, tied to classic Mac resource forks and a plugin technology 4D no longer supports, so the Resources Kit's conversion utility has little remaining practical use. Its underlying goal (moving string/constant resources into a portable, localizable format) is still valid, but is now addressed natively via 4D's built-in XLIFF-based translation tools and Design/Project mode resource management rather than this third-party conversion utility.
