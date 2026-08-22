# Tech Note 12-21: Cropping in 4D

**Author:** Sonya Rackwitz, Technical Services Team Member, 4D Inc.
**Published:** December 21, 2012 | **Product/Version:** 4D v13.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76723
**Download:** https://kb.4d.com/DLTN/TN/2012/12-21_CroppingIn4D.zip

## Proposition
This Tech Note explains how to let end users interactively crop images inside a 4D application, describing two possible implementations for giving users control over the crop selection area and, notably, how to support undo/redo of cropping operations, backed by a sample database demonstrating both approaches.

## Key Points
- Explains 4D's built-in command for cropping a picture variable and the need for a UI layer on top of it.
- Presents two alternative implementations for letting users interactively define the crop region.
- Covers implementing undo and redo of crop operations in detail.
- Provides a sample database demonstrating both cropping approaches end-to-end.

## Featured Technology
- Picture variables
- CROP PICTURE command
- Undo/Redo stack implementation
- Custom crop-selection UI

## Best Practices Highlighted
1. Maintain an explicit history/state stack to support undo/redo rather than only mutating the picture in place.
2. Separate the crop-selection UI logic from the underlying picture-cropping command for flexibility between implementations.

## Context/Positioning
Published in late 2012 for 4D v13.2, addressing a common need in 4D applications handling user photos/documents (e.g., contact photos, scanned documents) where in-app cropping avoids external image editors.

## Historical Commentary
**Status:** Still Relevant

4D's picture variable model and cropping command are still present and functional in current versions, so the core technique in this note continues to work largely unchanged, and the general undo/redo design pattern remains good practice. The main consideration today is that image-heavy interactive UI could alternatively be built as a web-based component (using an HTML/JS cropping library within a 4D web area) for a more modern look-and-feel, though the native picture-variable approach shown here remains a valid, simpler option for classic-form based applications.
