# Tech Note: Emulating the FileMaker Pro Book Object in 4D

**Author:** Not specified in source document
**Published:** May 1, 2000 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11965
**Download:** Not available (NO_DOWNLOAD_LINK_TEASER_ONLY)

## Overview
This Tech Note covers a technique for recreating FileMaker Pro's page-flipping "book" record navigator as a custom 4D form control.

## Key Points
- It frames the underlying problem as deceptively complex: although it looks like a simple record-navigation button, faithfully reproducing FileMaker's exact visual behavior (or any custom behavior desired) requires careful control of object visibility and click handling.
- The note's core proposition is that the general technique of toggling form objects' visibility in response to clicks and drags is broadly reusable, not just for a book control but for constructing other custom widgets such as sliding volume controls or rotating radio dials.
- Featured technology centers on 4D's classic form-object model: show/hide logic, object layering, and coordinate-based click detection used to fake animation and drag behavior without any specialized plug-in or picture-animation feature.
- The note positions this as a foundational UI technique note, useful to developers building any kind of custom, non-standard interface control in the Design/Custom Menus environment of that era.
- Because only the teaser text survives in this archive, the exact method code and sample database mechanics are not available, but the described approach follows a recognizable, then-common 4D interface trick of layering static and swapped visibility objects to simulate motion.
- This kind of note reflects the pre-Web-Area, pre-rich-graphics period of 4D UI development, where developers had to build convincing custom controls entirely from the classic form object toolkit.

## Featured Technology
- Form object show/hide logic
- Custom UI controls
- Object visibility techniques

## Historical Context
This note tackles a classic cross-product UI-parity problem: reproducing FileMaker Pro's book/page-turn navigator using only 4D's object show/hide and click-tracking primitives, a technique class that was common in the pre-plugin, pre-Web-Area era of custom 4D interfaces. The specific FileMaker-emulation goal is dated, but the underlying object-visibility trick for building slider/dial/animated custom controls remains a conceptually valid (if now largely superseded) UI technique. Modern 4D development would typically achieve this kind of custom control via richer picture/animation objects, web areas, or simply different UX conventions, making the specific implementation obsolete while the general trick is of historical interest. Related updates since: 4D's forms engine has since gained richer picture, list box, and web area objects that make bespoke show/hide record-navigation controls unnecessary for most modern UIs; Contemporary 4D UIs rarely emulate other products' widgets pixel-for-pixel via manual object toggling. The full Tech Note PDF/text could not be recovered for this archive entry because the old kb.4d.com page had no working download link at all; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
