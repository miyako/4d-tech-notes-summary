# Tech Note 16-13: Creating a Range Slider in 4D

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** September 12, 2016 | **Product/Version:** 4D v15.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77619
**Download:** https://kb.4d.com/DLTN/TN/2016/16-13_RangeSlider_3.zip

## Proposition
4D's built-in slider selects only a single value, but many query interfaces (e.g., price-range filtering) need a min/max pair. This tech note builds a reusable two-handle range slider entirely from native 4D form objects, with no third-party resources required.

## Key Points
- **Slider vs range slider:** a standard slider selects one value along a track; a range slider adds a second handle so both a minimum and maximum can be selected together.
- **Three-part design:** a static (optionally labeled) track plus two independent draggable slider handles.
- **Visual construction:** track and handle graphics are built as standalone picture assets, then assembled on the form.
- **Drag interaction code:** methods handle dragging each handle along the track and updating its represented value in real time.
- **Handle constraint logic:** the minimum handle is prevented from crossing past the maximum handle's position, and vice versa.
- **Value exposure:** the resulting min/max values are exposed to the rest of the application for use in queries.
- **Reusable packaging:** delivered as a sample database and a component, with guidance for reusing it in other databases.

## Featured Technology
- Custom range-slider UI component (track + two picture-based handles)
- Classic 4D form objects and drag-handling methods
- Reusable 4D component packaging

## Best Practices Highlighted
1. Enforce handle-order constraints (min ≤ max) directly in the drag-handling code to prevent invalid ranges.
2. Package the slider as a standalone, reusable component rather than embedding its logic directly in application forms.

## Context / Positioning
Published September 2016 for 4D v15.2, this is a classic-forms UI-craftsmanship note from the pre-Project-Mode, pre-ORDA era of 4D, addressing a UI gap (no native range slider) purely with form objects, picture assets, and method code rather than any data-layer technology.

## Historical Commentary
**Status:** Still relevant

Because this technique is built entirely from fundamental 4D form objects, picture assets, and drag-handling method code — none of which has been deprecated — it still works unmodified in current 4D and remains a legitimate reference for classic desktop form UI work.

That said, it is a workaround for a control 4D never added natively. For web-facing 4D applications built with Qodly or a browser-based front end today, an equivalent range-slider is a standard, readily available HTML/CSS/JS component, making a hand-built classic-form implementation the less common choice for new, web-oriented projects.
