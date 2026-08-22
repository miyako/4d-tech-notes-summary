# Tech Note 05-23: Making Labels More Dynamic

**Author:** Not specified in available source
**Published:** June 20, 2005 | **Product/Version:** 4D 2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=37622
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_21-24_(JUN)/05-23_Dynamic_Labels.exe

## Overview
This Tech Note describes a simple, generic technique for using flashing labels to visually draw a user's attention to a field that must be re-entered due to a failed entry rule.

## Key Points
- Addresses the usability challenge of directing users back to invalid fields, especially as forms grow more complex.
- Proposes flashing/blinking labels as a lightweight, generic visual cue technique.
- Positioned as reusable across any input form enforcing entry rules, not tied to one specific example.

## Featured Technology
- Form entry-rule enforcement and re-entry handling
- Flashing/blinking label visual cue technique
- Likely timer-driven (On Timer) form object property changes

## Historical Context
**Status:** Still relevant

The core UX goal of clearly directing a user's attention to invalid form fields remains just as important today as in 2005, so this note's underlying concern is timeless. However, the specific implementation approach (blinking text labels) has fallen out of favor relative to modern conventions like colored field borders, inline error messages, or tooltip-style hints, which are generally considered clearer and less distracting. The classic 4D mechanism for driving such timed visual effects (timers and form object property changes) remains available in current 4D forms regardless. Note: only the on-page teaser paragraph for this note survived in this archive — the full PDF and example database could not be recovered (old download-archive format not accessible in this environment), so this summary is necessarily limited to that teaser text.
