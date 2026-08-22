# Tech Note 21-15: Component for Managing Server Files from 4D Remote

**Author:** Add Komoncharoensiri, Director of Technical Services, 4D Inc.
**Published:** August 26, 2021 (revised February 24, 2022) | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78767
**Download:** https://kb.4d.com/DLTN/TN/2021/21-15_FileManagerComponent_2.zip

## Proposition
Managing files on a 4D Server machine from a remote client is awkward without a mapped drive or FTP setup. This note packages a modernized, reusable File Manager component built on 4D's "Execute on Server" mechanism, giving each client dynamic, permissioned access to a server folder tree.

## Key Points
- **Execute on Server attribute:** methods with this property (prefixed `svr...` by convention) run on the server and return results to the calling remote client — the foundational trick that makes the whole component possible.
- **openFileManager({pathOnServer})** opens the file manager window, defaulting to a "Root" folder next to the structure file if no path is given.
- **fileManagerStartup** must be called from `On Startup`/`On Server Startup` to initialize shared parameters.
- **Full file operations:** new folder, delete, rename, upload/download (button and native OS drag-and-drop), refresh, up-one-level, and clickable breadcrumbs.
- **UI modernization from 2015's TN 15-07:** array-based Listbox replaced with a **collection-based Listbox**, sortable headers, a file-size column, and a footer item counter.
- **Reduced process variable footprint:** the rewrite eliminates inter-process variables entirely, using Form data objects and only 2 process variables.
- **Component-ready packaging:** the implementation is delivered as a drop-in component rather than copy-pasted code, easing reuse across host databases.

## Featured Technology
- Execute on Server method property
- Collection-based Listbox
- `Get 4D folder`, `System folder` (wrapped via server-side methods)
- 4D component packaging (`.4dbase` in Components folder)

## Best Practices Highlighted
1. Wrap all server-only commands (`Get 4D folder`, `System folder`) in small "svr"-prefixed Execute-on-Server methods for reuse.
2. Package reusable UI/logic as a component to keep host databases clean and enable version updates.
3. Prefer collection-based Listboxes and Form data objects over array/interprocess-variable patterns for new development.

## Context / Positioning
This is an explicit generational update of a 2015 tech note, reflecting how 4D's UI idioms evolved over six years — away from arrays and interprocess variables and toward collections and Form data objects — while the core server-execution architecture (a longstanding, still-current 4D feature) remained untouched.

## Historical Commentary
**Status:** Still relevant

The Execute on Server attribute is a foundational, still fully supported 4D Remote/Server feature with no successor or deprecation — this technique remains valid today. The UI-layer choices highlighted as "modern" in 2021 (collection-based Listbox, Form data objects, no inter-process variables) are also still 4D's recommended idioms in 2026, so a developer building an equivalent tool today would follow essentially the same architecture. The only likely refinement in a current build would be leaning further into 4D classes for the component's internal logic, but the core approach described here has aged well.
