# Tech Note 10-36: Image Manipulation with GD

**Author:** Tom Fitch, Technical Services Team Member, 4D Inc.
**Published:** December 21, 2010 | **Product/Version:** 4D v12.1 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76234
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_34-36_(DEC)/10-36_PHP_GD_ImageManipulation.zip

## Proposition
This note explores GD, a PHP image-manipulation library made accessible to 4D developers through 4D v12's newly embedded PHP interpreter. It organizes GD's many functions into a thematic structure covering loading images, retrieving image info, saving images, drawing shapes, managing text, managing colors, performing general image manipulation, and converting between image types. A sample database is included that exercises many of these GD features via 4D wrapper methods, giving developers a practical starting point for building image-processing functionality — such as generating thumbnails, watermarks, or dynamic graphics — directly within a 4D application.

## Key Points
- Positions GD as one of the powerful libraries unlocked by 4D v12's embedded PHP interpreter.
- Organizes GD's large function set thematically: loading, image info, saving, drawing, text, colors, manipulation, and format conversion.
- Covers loading images from various sources and inspecting their properties (dimensions, format, etc.).
- Covers drawing operations and text rendering onto images via GD.
- Covers color management and general image manipulation (e.g., resizing, cropping, effects).
- Covers converting between image file types using GD.
- Includes a sample database demonstrating many of the covered GD features.

## Featured Technology
- 4D v12's embedded PHP interpreter
- GD PHP image manipulation library (loading, drawing, text, color, conversion)
- 4D wrappers for GD functions with a sample database

## Best Practices Highlighted
- Group related image-processing calls thematically to keep PHP/GD wrapper code organized and discoverable
- Test PHP interpreter/library availability early since GD support depends on the underlying PHP build

## Context / Positioning
Published at the end of 2010, shortly before 4D v12's broader PHP-related Tech Note series, to showcase server-side image processing (thumbnails, effects, format conversion) as a compelling new use of 4D's embedded PHP interpreter.

## Historical Commentary
**Status:** Partially Superseded

This PHP/GD-based image-manipulation bridge still technically works wherever 4D's PHP interpreter and a GD-enabled PHP build are available, but it is a legacy technique; 4D has since added native picture-manipulation commands directly in the 4D language (resizing, format conversion, drawing on pictures) that eliminate the need for a PHP/GD dependency for many common image tasks in modern 4D applications.
