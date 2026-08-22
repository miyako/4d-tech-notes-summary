# Tech Note 09-24: An Approach to Preferences

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** June 18, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75808
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_22-26_(JUN)/09-24_Preferences.zip

## Proposition
This note proposes a reusable, component-based approach for storing user and application preferences in an external, themed XML file (loaded/manipulated via 4D's DOM commands) rather than inside 4D's data engine, giving developers a portable, hand-editable, and structured preferences system.

## Key Points
- **Why external XML:** preferences stored as a file are easy to copy between installations, hand-edit, and can even let a single database behave differently by swapping preference files.
- **XML structure:** a root `Prefs4D` element containing `theme` elements (e.g. Web, Print, GUI), each holding `pref` children whose ID combines theme name + preference name (avoiding collisions across themes).
- **Core operations:** load preferences from disk into memory, save back to disk, create/delete themes, list theme names, and get/set/delete individual preference values — all implemented as DOM command wrappers.
- **Preferences Viewer GUI** included for interactively displaying, adding, and deleting themes/preferences.
- **Client/Server considerations** discussed for using the preferences system safely in a multi-user deployment.

## Featured Technology
- 4D DOM XML commands (in-memory XML preferences store)
- Custom XML preferences file format with theme support
- 4D component (reusable Preferences engine)
- Preferences Viewer GUI

## Best Practices Highlighted
1. Always code a default fallback value/action for any preference that may not be found in the file.
2. Use theme + preference name as a composite ID to safely reuse the same preference name across different contexts (e.g., "Web" vs. "Print").
3. Prefer an external, editable file for preferences that need to be portable, inspectable, or bulk-swappable across deployments.

## Context / Positioning
Published as a general-purpose architectural pattern rather than a feature walkthrough, this note gave 4D developers a ready-made, documented component for a need almost every application eventually faces: flexible, structured preference/configuration storage.

## Historical Commentary
**Status:** Partially Superseded

This note proposed a themed, XML-file-based preferences engine built on 4D's DOM commands as an alternative to storing application settings inside 4D's data engine — a sensible pattern at the time given the tooling available. The core idea (external, human-editable, easily copyable preference storage) remains sound today.

However, current 4D applications more commonly use 4D's native JSON object support (JSON Parse/Stringify, and the object/collection syntax) rather than DOM-based XML for this kind of key-value configuration store, since JSON is simpler to read/write and integrates naturally with 4D's object and collection types introduced in later versions.
