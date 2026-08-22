# Tech Note 09-03: 4D Plug-in Development Guide - Part 2

**Author:** Keisuke Miyako, 4D Japan
**Published:** January 21, 2009 | **Product/Version:** 4D v11.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75099
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_01-04_(JAN)/09-03_4D_Plug-in_Dev_Guide-Part_2.zip

## Proposition
The hands-on companion to Part 1's plug-in theory, providing working sample projects and C code for building cross-platform, Unicode-aware, Universal Binary 4D plug-ins that correctly handle text and picture parameters across both the 2004 and v11 SQL plug-in APIs, plus Mac OS X Apple Help Book integration.

## Key Points
- **Text parameter wrappers:** `PA_strings.c` bridges 2004's legacy/code-page text handling and v11 SQL's native Unicode, using Windows' `mlang.DLL` for broader encoding coverage.
- **Wizard workflow tips:** importing command/theme definitions from existing rsrc files, defining custom constants, and (new in v11 SQL) binding constant themes to command parameters via a generated `kmapper.xml`.
- **Picture handling transition:** moves away from legacy QuickDraw 'PICT' data toward Core Graphics types (CGImageRef/CGPDFDocumentRef) on Mac and GDI+ on Windows, with a sample plug-in exposing image conversion/export commands including a QuickLook-based file-thumbnail command.
- **Detailed Xcode configuration:** step-by-step guidance for setting architectures, deployment target, bundle identifiers, and custom test executables for a plug-in project.
- **Apple Help Book registration:** explains Carbon vs. Cocoa help registration differences, Info.plist keys, AppleTitle/AppleIcon meta tags, and the C code (`AHRegisterHelpBook`) needed to register a plug-in's help book on Mac OS X.
- **UTI Tools sample:** demonstrates working with macOS Uniform Type Identifiers to translate between file extensions, MIME types, and OS types.

## Featured Technology
- Classic C-based 4D Plug-in API (2004 and v11 SQL entry points) built with Xcode/Visual Studio
- Unicode-aware text parameter wrappers (PA_strings.c) bridging 2004 legacy encodings and v11 SQL Unicode
- Picture parameter handling transitioning from QuickDraw 'PICT'/PicHandle to CGImageRef/CGPDFDocumentRef and GDI+
- Mac OS X Carbon-based Apple Help Book registration (AHRegisterHelpBook) and UTI (Uniform Type Identifier) tooling

## Best Practices Highlighted
1. Write version-checking wrapper functions so the same plug-in source code can target both legacy and current plug-in APIs.
2. Prefer Core Graphics image types (CGImageRef) over legacy QuickDraw 'PICT' data for better performance and future compatibility.
3. Build and test plug-ins as Universal Binaries with a custom test executable pointed at the target structure's Plugins folder before wider distribution.
4. Use "UTTypeConformsTo" class-hierarchy checks rather than exact UTI string matches, for forward compatibility with future system types.

## Context / Positioning
Published as the practical follow-through to a theory-focused Part 1, giving experienced C-capable 4D developers concrete, working project templates for the API and platform transitions underway at the time.

## Historical Commentary
**Status:** Obsolete

The core 4D Plugin C API and the technique of writing version-bridging wrapper functions to support multiple plug-in API generations in one codebase remain conceptually sound and the plug-in API itself is still supported by 4D today.

However, most of this note's specific content is now defunct: it targets the Carbon/QuickDraw-to-Cocoa/Core-Graphics transition, PowerPC/Universal Binary build architectures, and Apple Help Book registration via Carbon's `AHRegisterHelpBook` — all tied to Xcode project types, macOS APIs, and CPU architectures that no longer exist. Current 4D plug-ins are built exclusively as modern 64-bit Cocoa bundles, making this note's build instructions and Carbon-specific help integration unusable as a direct guide today, useful now only as a historical record of that platform transition.
