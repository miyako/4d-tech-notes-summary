# Tech Note 06-32: ImageMagick Plug-in

**Author:** Thomas Maul, General Manager, 4D
**Published:** August 14, 2006 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=43892
**Download:** https://kb.4d.com/DLTN/TN/2006/Windows/TN_2006_31-34_(AUG)/06-32_ImageMagick.zip

## Overview
This Tech Note presents a 4D plug-in that enhances 4D's picture-handling capabilities by wrapping the open-source ImageMagick framework. Rather than requiring users to install ImageMagick on every client computer, the plug-in statically links ImageMagick directly, so 4D's plug-in deployment mechanism automatically pushes it out to all client machines.

## Key Points
- The plug-in wraps ImageMagick's Magick++ API to expose resize, crop, rotate, enhance, and image-manipulation commands from within 4D.
- Uses a static link of ImageMagick version 6.2.7 (current as of June 2006), trading a larger plug-in binary for guaranteed availability without a separate install.
- Runs cross-platform with an identical feature set on Mac OS and Windows; QuickTime is not required.
- Supports both external documents on disk and images stored in 4D BLOB objects, enabling images to be stored directly in the 4D database and displayed via 4D commands or the Pict Container plug-in.
- Because not all format libraries are statically included (due to licensing or size), some picture formats supported by a full ImageMagick install are unavailable.
- Documents ImageMagick's free/open-source license terms and the attribution/inclusion requirements for redistributing it (license file on distribution media, credit in About dialogs).
- Describes a workflow model based on in-memory "image objects" — commands like `IM New Object`, `IM Clear Object`, and `IM Copy Object` create, clear, and copy these objects, each returning a longint error code.

## Featured Technology
- ImageMagick (statically linked, v6.2.7) / Magick++
- 4D plug-in architecture (cross-platform deployment)
- 4D BLOB and external document picture storage
- 4D picture commands / Pict Container plug-in integration

## Historical Context
Published in August 2006 for 4D 2004, this note predates 4D v11's SQL engine, Project Mode, and ORDA by years, and reflects an era when rich image processing in 4D required third-party C plug-ins bundling specific library versions. The plug-in architecture and bundling approach described here (statically embedding a fixed ImageMagick release) is a historical solution; today's 4D offers substantially more built-in picture-handling functionality, and standalone image plug-ins tied to a decade-plus-old ImageMagick version are not viable in modern deployments.

## Historical Commentary
**Status:** Obsolete

The specific plug-in binary, its static ImageMagick 6.2.7 dependency, and 4D 2004-era plug-in packaging are no longer relevant to current 4D development. The general concept — giving 4D built-in, deployable image manipulation without external installs — remains a reasonable engineering pattern, but is now addressed through 4D's expanded native picture commands and modern image libraries rather than this plug-in.
