# Tech Note 10-25: PhotoAdjust Plug-in

**Author:** Thomas Maul, 4D Germany.
**Published:** August 18, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76158
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_24-28_(AUG)/10-25_PhotoAdjust.zip

## Proposition
Contributed by Thomas Maul of 4D Germany, this Tech Note documents PhotoAdjust, a cross-platform compiled plug-in that lets 4D developers adjust digital camera photos directly within a 4D application — exposure, brightness, contrast, saturation, sharpening, cropping, and resizing.

## Key Points
- PhotoAdjust is a third-party compiled plug-in for cross-platform digital photo adjustment inside 4D
- Three core commands: Photo_SetImage, Photo_GetImage, Photo_Adjust
- Includes a customizable, localizable ready-to-use adjust dialog component
- Requires Mac OS 10.5+ or Windows 7; explicitly does not support Windows XP/Vista
- Supports exposure, brightness, contrast, saturation, sharpening, cropping, and resizing

## Featured Technology
- PhotoAdjust plug-in
- Photo_SetImage/Photo_GetImage/Photo_Adjust commands
- digital camera image adjustment (exposure, sharpening, crop)
- classic compiled plug-in API

## Best Practices Highlighted
- Use the provided dialog component rather than building a custom adjustment UI from scratch
- Confirm OS version compatibility before deploying to older Windows/Mac systems

## Context/Positioning
Published to showcase a third-party 4D plug-in (from 4D Germany) addressing the then-new ability to integrate digital camera images natively into 4D applications.

## Historical Commentary
**Status:** Obsolete

PhotoAdjust is a compiled, C-based plug-in for 4D v11 SQL/v12 that required Windows 7 or Mac OS 10.5+ and predates 4D's move to fully 64-bit and Apple Silicon-native plug-ins. Since 4D's plug-in ABI and OS support requirements have moved on substantially since 2010, this specific binary is effectively obsolete for current 4D versions, even though 4D's classic plug-in API concept itself remains supported for new, actively-maintained plug-ins.
