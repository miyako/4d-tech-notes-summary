# Tech Note 16-09: Sliding Tab in 4D

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** August 11, 2016 | **Product/Version:** 4D v15.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77596
**Download:** https://kb.4d.com/DLTN/TN/2016/16-09_SlidingTabIn4D.zip

## Proposition
This note shows how to build a mobile-style sliding tab (swipeable carousel) control for classic 4D forms using a subform, manual object positioning/resizing, and On Timer-driven animation — a fully custom UI component built from primitive form-object manipulation.

## Key Points
- **Motivation:** recreate an app-like sliding tab interface within 4D's classic (non-web) form toolkit.
- **Subform-based architecture:** the sliding tab lives inside a reusable subform integrated via variable/round-rectangle objects.
- **Animation via On Timer:** manual timer-driven object shifting produces the sliding transition effect.
- **Extensive method library:** dozens of stc_ prefixed methods handle initialization, loading, resizing, event handling, and JSON-based configuration.
- **JSON property storage:** component configuration/state is serialized via stc_getJSONSubformProperties.
- **Event handler management:** stc_setEventInfoTab/unsetEventInfoTab attach and detach custom event behavior dynamically.
- **Demo database provided** to illustrate integration and configuration.

## Featured Technology
- 4D Subforms (classic Design Mode)
- 4D form object events (On Load, On Bound Variable Change, On Timer)
- JSON for component configuration
- Manual pixel-based object animation

## Best Practices Highlighted
1. Encapsulate reusable UI behavior in a subform + dedicated method library rather than duplicating logic per form.
2. Store component configuration as JSON to keep the API flexible without many discrete parameters.

## Context / Positioning
This Tech Note was published in 2016, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Obsolete

This is a textbook example of classic-4D-era custom UI engineering that modern 4D development would rarely reproduce this way: today's equivalent would typically be built with CSS/JS transitions in a web area or a fully web-based (Qodly/ORDA-REST) front end, which handle sliding/carousel effects natively and far more efficiently than manual pixel-shifting timers on classic form objects. The component would still run technically, but the approach is superseded by web UI techniques.
