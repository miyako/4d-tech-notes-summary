# Tech Note 16-15: Custom Shadow for Object Focus

**Author:** Add Komoncharoensiri, Director of Technical Services, 4D Inc.
**Published:** September 30, 2016 | **Product/Version:** 4D v15.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77644
**Download:** https://kb.4d.com/DLTN/TN/2016/16-15_CustomShadow.zip

## Proposition
4D's default object-focus indicator is a simple border, which looks dated next to modern shadow-based "elevation" UI design. This tech note builds a custom drop-shadow effect from composited picture assets so form objects can appear to "float" above the background, giving classic 4D forms a more contemporary look.

## Key Points
- **Default focus limitation:** the standard blue-border focus indicator has existed for a long time and still works, but looks visually dated compared to depth/shadow-based modern design.
- **Shadow concept:** a rectangle (or picture) gains a "floating" appearance by surrounding it with soft gradient shadow pieces rather than a hard border.
- **Eight-piece gradient assets:** the shadow is built from named static picture pieces (e.g., `borderShadowTopLeft`, `borderShadowTop`) covering each corner and edge of the target rectangle.
- **`showBorderShadow(ObjectName)`:** applies the border-style shadow treatment to a named object.
- **`showFloorShadow(ObjectName)`:** applies an alternate, floor-cast shadow variant.
- **`setShadowShade(ShadeLevel)` / `getShadowShade`:** control and query the intensity/shade of the shadow effect.
- **Demonstrated use cases:** rectangles, pictures, and toolbar icons all shown gaining a floating appearance from the technique.

## Featured Technology
- Composited gradient picture assets for shadow rendering
- Classic 4D form object focus properties
- Custom methods: `showBorderShadow`, `showFloorShadow`, `setShadowShade`, `getShadowShade`

## Best Practices Highlighted
1. Build reusable, parameterized shadow methods (object name + shade level) rather than hard-coding shadow assets per form.
2. Reserve shadow/elevation effects for elements that genuinely need to draw user attention (buttons, active icons) rather than applying them universally.

## Context / Positioning
Published September 2016 for 4D v15.x, this note is a classic-4D-forms UI craftsmanship piece, from an era well before Project Mode and ORDA, when achieving contemporary visual effects in 4D required manual picture compositing rather than any native styling/CSS layer.

## Historical Commentary
**Status:** Still relevant

The picture-compositing technique and its supporting methods still function unmodified in current 4D, since they rely only on ordinary picture objects and form methods that remain fully supported. As a piece of classic-form craftsmanship, it holds up well.

However, it is fundamentally a workaround for a native styling gap. The same drop-shadow effect is trivial to achieve today with a single CSS `box-shadow` declaration in any Qodly or browser-based front end, so this manual approach is largely superseded for web-facing UI work — it remains most useful specifically for classic desktop 4D forms that haven't moved to a web-based UI layer.
