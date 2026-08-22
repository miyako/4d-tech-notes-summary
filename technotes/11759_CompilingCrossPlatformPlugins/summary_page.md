# Tech Note: Compiling Cross-Platform with Plug-ins

**Author:** Not specified in source document
**Published:** April 1, 1997 | **Product/Version:** 4D Transporter v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11759
**Download:** Not available (no working download link archived for this page)

## Overview

This Tech Note explains how to successfully compile a 4D database cross-platform (Macintosh/Windows) when third-party plug-ins are involved, even when those plug-ins were built for a platform different from the one performing the compilation.

## Key Points

- Addresses compiling with Windows plug-ins on a Mac, Macintosh plug-ins on Windows, or plug-ins available for both platforms.
- States that cross-platform compilation with mixed-platform plug-ins is problem-free as long as certain constraints are observed.
- Positioned as practical guidance for developers/integrators managing multi-platform 4D deployments that rely on plug-ins.

## Featured Technology

- 4D Compiler
- Cross-platform (Mac/Windows) plug-in compilation
- 4D Transporter
- Classic (pre-modern) 4D plugin API

## Historical Context

Reflects the realities of 4D's classic-era cross-platform story, where compiled 4D databases ran natively on both Mac and Windows but third-party plug-ins were platform-specific binaries built against the older 4D plugin API; both the specific compilation constraints and the 4D Transporter product line this note is filed under are long retired from 4D's current lineup.

## Historical Commentary
**Status:** Obsolete

This note addresses the constraints of compiling 4D databases cross-platform (Mac/Windows) when third-party plug-ins built for the older, pre-modern 4D plugin API are involved; this exact class of Mac/Windows binary plug-in cross-compilation concern is tied to the classic 4D Compiler and legacy plugin architecture of the era and has limited direct applicability to modern 4D's build and plugin/component ecosystem.
