# Tech Note 10-04: Core Image Pack

**Author:** Thomas Maul, 4D Germany.
**Published:** February 5, 2010 | **Product/Version:** 4D v11.5 | **Platform:** Mac
**Page:** https://kb.4d.com/assetid=76018
**Download:** https://kb.4d.com/DLTN/TN/2010/MacOS/TN_2010_04-07_(FEB)/10-04_CoreImagePack.zip

## Proposition
This note introduces Core Image Pack, a Mac-only 4D plugin exposing Apple's Core Image framework (Mac OS X 10.4+) for GPU-accelerated image manipulation — color adjustment, blurring, denoising, sharpening, and blending — directly from 4D v11 SQL applications.

## Key Points
- Requires **4D v11 SQL or higher** and **Mac OS 10.5 or higher**; the plugin is Mac-only.
- Exposes **five commands**: CI_SetImage, CI_GetImage, CI_GetFilterList, CI_GetFilterAttributes, CI_ApplyFilter.
- Uses a dedicated **CI_Preview external area** that displays filtered results directly from GPU memory for near-instant previewing.
- Supports filters with **numeric sliders, colors, points, and secondary images** as parameters, each with descriptions sourced from the OS.
- Filter names/attributes/descriptions are **localized** by the system language (English, German, French, etc.).
- Example database provides both an **automatic intro slideshow** and an **interactive filter browser** with a Load button for custom images.

## Featured Technology
- Core Image Pack plugin (CI_SetImage, CI_GetImage, CI_GetFilterList, CI_GetFilterAttributes, CI_ApplyFilter)
- Mac OS X Core Image framework
- GPU-accelerated image filtering, CI_Preview external area

## Best Practices Highlighted
1. Use the CI_Preview external area for live previewing instead of round-tripping through a 4D picture variable, since final rendering is deferred until the picture is retrieved.
2. Enable graphics-card acceleration (e.g., enabling discrete GPU on laptops with switchable graphics) to get full plugin performance.
3. Use images of similar width/height when demonstrating blend/dissolve effects for best visual results.

## Context / Positioning
Contributed by 4D Germany, this note showcased a third-party plugin bringing a flagship Mac OS X imaging framework into 4D, targeting Mac-only shops wanting professional image effects without external image-editing dependencies.

## Historical Commentary
**Status:** Obsolete

This note introduces a Mac-only 4D plugin exposing Apple's Core Image framework (introduced in Mac OS X 10.4) for GPU-accelerated image filtering, color adjustment, blending, and previewing directly from 4D, requiring 4D v11 SQL and Mac OS 10.5+.

The plugin depends on specific, dated Mac OS X system frameworks and 4D external-area/plugin APIs from this era; while the classic 4D plugin architecture itself is still supported, this particular third-party plugin's continued availability/compatibility with modern macOS and current 4D versions is doubtful, and 4D now offers native picture manipulation commands and better cross-platform image APIs that reduce the need for OS-specific plugins like this one.
