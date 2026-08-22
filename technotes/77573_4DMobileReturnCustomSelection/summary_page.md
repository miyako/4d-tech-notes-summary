# Tech Note 16-08: 4D Mobile Return Custom Selection

**Author:** Xiang Liu, Technical Services Engineer, 4D Inc.
**Published:** June 23, 2016 | **Product/Version:** 4D v15.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77573
**Download:** https://kb.4d.com/DLTN/TN/2016/16-08_MobileReturnSelection.zip

## Proposition
This note extends 4D's native "Mobile Return selection" command — limited to one table selection at a time — with a custom pattern for returning multiple table selections plus arbitrary user data as a single JSON payload to a 4D Mobile (Wakanda) client app.

## Key Points
- **Native limitation addressed:** "Mobile Return selection" only returns one selection from one table per call.
- **Custom multi-selection JSON:** the note shows building a method that bundles multiple named selections into a single JSON response.
- **Read-only constraint noted:** the native command's returned selection cannot be modified client-side, informing the custom design.
- **Selected record number command** used to retrieve and re-apply selections on demand.
- **Embedding user data:** custom fields can be included alongside record selections in the JSON payload.
- **Targets 4D Mobile/Wakanda client apps** specifically, not general REST consumers.

## Featured Technology
- 4D Mobile (Wakanda-based native client framework)
- Mobile Return selection command
- Selected record number command
- JSON entity collections

## Best Practices Highlighted
1. Design custom JSON payload structures when a native command's shape is too restrictive for the use case.
2. Bundle related data (multiple selections + metadata) into a single round-trip rather than multiple calls.

## Context / Positioning
This Tech Note was published in 2016, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Obsolete

4D Mobile — the Wakanda-derived native iOS/Android client technology this note targets — was discontinued by 4D years ago in favor of REST/ORDA-based web and mobile development, and later Qodly; the specific "Mobile Return selection" command and 4D Mobile client APIs referenced here are no longer part of any current 4D roadmap. The underlying idea of shaping custom JSON responses for a client is still valid for today's REST/ORDA APIs, but this note's concrete techniques do not transfer directly.
