# Tech Note: Using a Map in a Form

- **Asset ID:** 29816
- **Tech Note #:** 03-42
- **Published:** September 30, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Gérald Czwiklinski
- **Page URL:** https://kb.4d.com/assetid=29816
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_40-43_(SEP)/03-42_Using_a_Map_in_a_Form.hqx

## Overview

Gérald Czwiklinski, of 4D S.A., presents a technique for detecting mouse clicks on non-rectangular shapes in a picture — demonstrated with a clickable map of the United States — by pre-converting a specially prepared grayscale 'mask' image into a 2D integer array where each cell stores the region ID for that pixel, then simply indexing the array by the click's (x, y) coordinates at runtime.

## Key Points

- Builds a hidden grayscale 'mask' picture where each clickable region (e.g., a US state) is filled with a distinct near-uniform gray value, subtly different so the mask still resembles the visible map
- Converts the mask picture to a 2D array, Pixel_State, sized ARRAY INTEGER(Pixel_State;$height;$width), populated once at startup rather than per-click
- Reads pixel values by converting the picture to an uncompressed 24-bit BMP with PICTURE TO BLOB(...;'BMPf'), then walking the BLOB in 3-byte steps starting after the 54-byte BMP header
- At click time, detection is just two operations: GET MOUSE($x;$y;$bt) followed by Pixel_State{$y}{$x} to read the region ID directly out of the precomputed array
- Maps the resulting numeric region ID to a real record via QUERY([State];[State]NumeroDepartement=$State) and RELATE ONE
- Notes the single-channel grayscale approach tops out at 256 distinct regions, but can be extended with a full RGB-encoded value (R*65536+G*256+B) for more regions
- Generalizes the technique beyond maps to any non-rectangular clickable shape, such as pie-chart wedges or arrow-shaped buttons

## Featured Technology

- Pixel-mask hit-testing via a 2D array
- GET PICTURE FROM LIBRARY / PICTURE PROPERTIES
- PICTURE TO BLOB (24-bit BMP conversion)
- Grayscale-coded region map generation
- GET MOUSE for click coordinates
- 2D ARRAY INTEGER sized to image height/width

## Historical Commentary

**Status:** Partially Superseded

The pixel-mask lookup-array technique shown here is a clever, still-technically-workable solution to a problem (detecting clicks on irregular shapes) that classic 4D forms had no direct answer for. Modern 4D applications have more options for this today — vector picture formats, SVG-based UI components, or web-based front ends (4D's web area / QODA) where client-side JavaScript and CSS clip-paths or SVG hit-testing handle irregular shapes natively — so this exact BLOB-pixel-walking approach is now more of a fallback than a first choice, though it remains valid for classic 4D form-based picture areas.

**References to newer/updated information:**
- 4D web areas and modern web-based UIs (including QODA) can use SVG or CSS-based hit testing for irregular shapes instead of a hand-built pixel mask array
- The GET MOUSE / PICTURE TO BLOB-based technique shown here remains valid and usable for classic 4D form picture objects today
