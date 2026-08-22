# Tech Note 14-01: Advanced Cropping in 4D

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc.
**Published:** January 9, 2014 | **Product/Version:** 4D v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76939
**Download:** https://kb.4d.com/DLTN/TN/2014/14-01_AdvancedCroppingIn4D.zip

## Proposition
Building on an earlier basic cropping Tech Note, this note shows how to construct a full drag-handle image cropping tool in 4D — like those in popular graphics applications — using `TRANSFORM PICTURE` alongside carefully engineered static picture objects and mouse-event tracking to simulate a resizable crop rectangle.

## Key Points
- `TRANSFORM PICTURE` modifies actual picture data (Reset, Scale, Translate, Flip, Crop, grayscale fade) — distinct from a picture object's mere display formatting.
- A resizable cropping rectangle is faked by precisely positioning four thin static "rect_" picture objects edge-to-edge so they look like one frame with a hole in the middle.
- `RepositionToolAssets` keeps all tool assets aligned on load and after each crop, accounting for images larger than the display object, scrolled images, and 4D's screen-refresh behavior.
- A central `HandleMouseEvents` method dispatches drag events to one of five handle-tracking methods (`TrackTopLeftHandle`, `TrackTopRightHandle`, `TrackBottomLeftHandle`, `TrackBottomRightHandle`, `TrackInCropRect`).
- `OBJECT MOVE` repositions the picture and crop-tool assets in real time as the user drags.
- Users get three ways to save the crop result: to the Picture Library (new ID/name), to a file on disk, or committed back to the original form's picture object.

## Featured Technology
- `TRANSFORM PICTURE` command
- Draggable-handle cropping rectangle built from static picture objects
- `OBJECT MOVE` and mouse-event handling for real-time drag UI
- Picture Library / file-on-disk saving of cropped images

## Best Practices Highlighted
1. Separate "display formatting" (picture object properties) from actual picture data manipulation (`TRANSFORM PICTURE`).
2. Keep tool-asset repositioning logic centralized (e.g., `RepositionToolAssets`) so it can be re-invoked consistently after load or crop actions.
3. Account explicitly for oversized/scrolled images and 4D's screen-update timing when building drag-based picture UI.

## Context/Positioning
Published as a sequel to an earlier basic cropping note (Dec 2012), this Tech Note pushed further into advanced, production-quality image editing UI achievable purely with native 4D form objects and commands.

## Historical Commentary
**Status:** Still relevant

The `TRANSFORM PICTURE` command central to this note still exists in current 4D versions, and hand-building a draggable crop-handle overlay from carefully positioned static picture objects and mouse-event tracking remains a valid, if labor-intensive, classic-language UI technique. It is a craftsmanship-heavy solution to a problem that a modern application might instead delegate to a Web Area hosting a JavaScript image-cropping library for smoother interaction with far less manual per-pixel object management — but the underlying picture manipulation command and overall approach remain functional and directly usable today.
