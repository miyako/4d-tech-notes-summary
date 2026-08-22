# Tech Note 17-03: Toggle Switches in 4D

**Author:** Timothy Tse, Technical Services Engineer, 4D Inc.
**Published:** February 16, 2017 | **Product/Version:** 4D v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77726
**Download:** https://kb.4d.com/DLTN/TN/2017/17-03_ToggleSwitchesIn4D.zip

## Proposition
4D v16 introduced two new picture-interaction features — the "On Mouse Up" form event and the "Is waiting mouse up" command — that make it possible to detect click-and-drag gestures on picture objects. This tech note uses them to build a modern, interactive toggle switch control (in the style of a mobile OS switch) for classic 4D forms, a UI element 4D does not provide natively.

## Key Points
- **New v16 primitives:** "On Mouse Up" fires when the left mouse button is released over a picture object; "Is waiting mouse up" reports whether the button is still held.
- **Two-picture design:** the switch is built from a container picture variable (background) and a smaller button picture variable layered on top.
- **Image loading:** images are imported programmatically via READ PICTURE FILE for the button and two container states (on/off backgrounds).
- **Drag detection:** the mouse-up event/command pair lets code distinguish a simple click from a click-and-drag gesture across the switch.
- **State encapsulation:** all toggle state (position, current value, associated variable names) is packed into a single 4D object via a `TogObj_Init` method, enabling clean creation of multiple independent switches on one form.
- **Setting/retrieving values:** dedicated methods read and write the toggle's boolean-like state through the encapsulated object.
- **Demo database:** a working example accompanies the note showing multiple toggle switches on one form.

## Featured Technology
- On Mouse Up (4D v16 form event)
- Is waiting mouse up (4D v16 command)
- Picture variables / READ PICTURE FILE
- 4D Object used for per-control state encapsulation

## Best Practices Highlighted
1. Encapsulate each control's mutable state (position, value) into a single 4D object rather than loose page/process variables, to support multiple instances cleanly.
2. Provide dedicated getter/setter methods around the encapsulated object instead of accessing its properties directly from form code.

## Context / Positioning
Published in February 2017 for 4D v16, this note is a classic example of "classic 4D" desktop form craftsmanship: hand-built UI controls using picture-swapping and object encapsulation, from an era squarely before Project Mode (v17+, 2018) and before ORDA existed as a data-access paradigm. It represents developer ingenuity working around gaps in 4D's native form-object palette of the time.

## Historical Commentary
**Status:** Still relevant

The On Mouse Up event and Is waiting mouse up command introduced in v16 remain supported in current 4D, so this toggle-switch code would still function largely unmodified. The pattern of encapsulating widget state into a 4D object is also good practice that has aged well, predating but resembling later class-based patterns available since 4D v17+/v19+ project mode.

That said, this is fundamentally a workaround for a missing native control. Later 4D releases have added more UI polish to classic forms, and — more significantly — many new UIs are now built as web pages (via Qodly or custom HTML forms) where a native or CSS-based toggle switch is trivial to add, making this specific hand-rolled technique less necessary for greenfield projects today.
