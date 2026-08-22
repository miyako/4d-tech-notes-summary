# Tech Note 96-06: Modular Interface Design Using Picture Variables

**Author:** Forrest Swilling
**Published:** February 1, 1996 | **Product/Version:** 4D v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11689
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_06-10_(FEB)/96-06_Interface.exe

## Overview
This Tech Note describes how to build a responsive, modular, and memory-efficient interface in 4D by displaying **picture variables** in non-enterable active objects as backdrops for fields and other variables, in place of static 4D graphic objects (lines, rectangles) or large embedded PICT images. It backs the technique with measured disk-size and RAM comparisons.

## Key Points
- Using picture variables as shared field backdrops means all similar graphic objects reference the **same variable**, so editing the interface (or supporting different color depths) is centralized and simple.
- Measured on identical test layouts via **4D Insider** (disk size) and **MacsBug** (RAM heap size): picture variables were roughly **4x more disk-efficient** than standard 4D graphic objects and **6x more efficient** than a large embedded PICT; RAM savings were similarly dramatic (e.g. 1,440 bytes vs. 5,024–5,776 bytes for the alternatives in a single test layout).
- Applications shown include: field backgrounds (including "type-ahead" pop-ups), tiled custom layout backgrounds, "built" graphics assembled from tiled/truncated copies of a base image to fit variably sized fields, and layered check-mark/pencil-icon feedback graphics representing enabled/disabled/hidden states.
- Workflow: design a grid of standard field sizes, add graphics as **PICT resources** via ResEdit (back up the structure file first — a crash mid-edit can corrupt it), then load them into picture variables with ACI Pack's `GetPicture` command in a `Startup` procedure, and toggle states at runtime with helper procedures like `ToggleObject`/`SetPencilIcon`/`SelectRadio`.
- For 4D Server deployments, the **Update resource** must be incremented via **Customizer Plus** to force clients to redownload changed picture resources to their local `.res`/`.rex` files.
- Design caution: hiding UI elements can reduce a user's sense of stability even as it reduces visual noise — "no guideline can substitute for a tasteful designer."

## Featured Technology
- 4D Picture variables/fields (active objects)
- PICT resources loaded via ACI Pack's `GetPicture`
- 4D Insider (structure size analysis) and MacsBug (Mac low-level debugger, for RAM measurement)
- ResEdit and Customizer Plus (resource management, including the Update resource for 4D Server clients)

## Historical Context
Published February 1996 for 4D v3.x, this note reflects a period when 4D's interface toolkit was limited and every graphic on a layout consumed disk space and RAM per instance; developers needed hands-on techniques using classic Mac OS resource tools (ResEdit, PICT resources, MacsBug) and 4D-specific utilities (4D Insider, Customizer Plus, ACI Pack) to build efficient, professional-looking interfaces.

## Historical Commentary
**Status:** Obsolete

The specific toolchain this note relies on — ResEdit-edited PICT resources, ACI Pack's `GetPicture`, 4D Insider, MacsBug, and Customizer Plus's Update resource mechanism — is entirely classic Mac OS/4D v3.x-era and has no equivalent in current 4D or modern operating systems. However, the underlying design principle — reusing shared bitmap assets as backdrops instead of duplicating graphic objects across layouts to save space and improve maintainability — remains a recognizable and still-sound idea in modern UI engineering, even though today's 4D form architecture and image formats make the specific 1996 implementation unnecessary.

