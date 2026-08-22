# Tech Note 17-02: Colors with User Interface in 4D

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** January 26, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77710
**Download:** https://kb.4d.com/DLTN/TN/2017/17-02_ColorsAndUI.zip

## Proposition
Color choice is one of the most overlooked but impactful factors in UI design. This tech note surveys established color theory and accessibility standards — contrast ratios and color harmonies — and shows how to implement matching 4D methods for generating contrasting colors, color harmonies, and monochromatic palettes programmatically.

## Key Points
- **Color and mood/perception:** cooler colors (blue) tend toward calm, warmer colors (red) toward energy; contrasted with Microsoft's and Apple's default OS color schemes as real examples.
- **Contrast ratio standards:** ISO/ANSI/HFES set a 3:1 minimum; W3C's WCAG 2.0 SC 1.4.3 sets Level AA at 4.5:1 (normal text) / 3:1 (large text), and Level AAA at 7:1 / 4.5:1.
- **Color harmonies:** based on the color wheel; complementary colors sit 180° apart and mutually emphasize each other, with more complex 3–4 color harmony schemes also covered.
- **Generating a contrasting color:** a 4D method computes a color guaranteed to sufficiently contrast against a given background.
- **Calculating color harmonies:** methods derive complementary/harmony colors from a base color using color-wheel math.
- **Monochromatic color generation:** a method produces a range of shades/tints from a single base hue.
- **Sample database:** demonstrates the above techniques applied within a 4D form.

## Featured Technology
- WCAG 2.0 (Web Content Accessibility Guidelines) contrast criteria
- ISO/ANSI/HFES contrast-ratio standards
- Color wheel / color harmony theory
- 4D RGB/color manipulation methods

## Best Practices Highlighted
1. Target at least a 4.5:1 contrast ratio (WCAG AA) between text and background for accessible UI.
2. Base a UI's supporting palette on color-wheel harmonies rather than arbitrary color choices to keep the theme cohesive.

## Context / Positioning
Published January 2017 for 4D v16, this note predates the CSS-driven, web-based UI approaches that later became common in 4D development (via Qodly and browser-hosted front ends). It reflects an era when 4D developers implemented visual design logic directly in 4D method code for classic desktop forms, rather than delegating styling to a stylesheet layer.

## Historical Commentary
**Status:** Still relevant

The underlying color science and accessibility guidance are essentially timeless — WCAG has progressed incrementally (2.1, 2.2) with refined success criteria, but the 4.5:1/3:1/7:1 contrast thresholds cited here remain accurate reference points. The 4D-side color-generation methods (RGB manipulation, harmony calculation) still run on current 4D versions without modification.

What has shifted is *where* this logic tends to live: for modern web-facing 4D applications, the same color theory is more commonly expressed through CSS custom properties, design tokens, or a design system rather than 4D method code computing colors at runtime. This note is a solid, durable reference for classic-form UI work and for understanding the theory, even if the specific implementation pattern is less common in newer web-oriented projects.
