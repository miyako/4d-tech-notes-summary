# Tech Note: Making Labels More Dynamic

- **Asset ID:** 37622
- **Tech Note #:** 05-23
- **Published:** June 20, 2005
- **Product / Version:** 4D
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=37622
- **Download:** https://kb.4d.com/DLTN/TN/2005/MacOS/TN_2005_21-24_(JUN)/05-23_Dynamic_Labels.hqx

## Overview

Jean-Yves Fock-Hoon (QA Manager, 4D) presents a lightweight technique for giving visual feedback on failed entry-rule validation by making a field's label blink between red and white, built from 4D Chart-rendered pictures layered over the label rather than a modal Alert dialog.

## Key Points

- Each of four labels to be made dynamic is paired with an overlapping picture button (pb_text01–04, variables pb01–04, source pictures ppb01–04) precisely positioned on top of the corresponding static text label.
- On the form's On Load event, 4D Chart's offscreen drawing commands (`CT New offscreen area`, `CT Draw text`, `CT SET TEXT ATTRIBUTES`, `CT Area to picture`) render the label's text once in red and once in white using the object's actual on-screen dimensions (via `GET OBJECT RECT`).
- The red and white pictures are concatenated into a single two-frame picture (`$pictRed/$pictWhite`) assigned to the picture button, whose Animation object properties are set to cycle the frames, producing a blinking effect with zero custom animation code.
- The Validate button's object method checks four entry rules (Name not blank, guest count ≥ 1, a real reservation date, a real reservation time); for each failing field it uses `SET VISIBLE` to hide the plain label and show the blinking picture button in its place, and vice-versa for passing fields.
- If any rule fails, the method issues `REJECT` and `REDRAW WINDOW` to keep the record open for the user to fix, rather than saving.
- The technique is explicitly presented as generic and reusable for any label needing a blinking-attention effect, requiring only the 4D Chart plug-in and matching picture-button placement.

## Featured Technology

- 4D Chart offscreen area drawing (CT New offscreen area, CT Draw text, CT Area to picture)
- Picture button Animation frame-cycling
- Overlapping picture-button/label UI pattern
- SET VISIBLE-driven show/hide validation feedback
- REJECT / REDRAW WINDOW validation flow

## Historical Commentary

**Status:** Still relevant

The underlying goal here — clear, in-context visual feedback for a failed entry rule, rather than an interruptive modal Alert — is timeless and still a common UX requirement in 4D forms today. The specific implementation, however, is a product of its era: it depends on the 4D Chart plug-in to rasterize label text into red/white picture frames and on the classic Animation picture-button property to cycle them. Modern 4D form design would more likely achieve the same attention-drawing effect with colored field borders, inline error text, or icon badges driven by object formatting properties, without needing a plug-in-rendered picture at all.

**References to newer/updated information:**
- Modern form UX generally favors inline validation messages, colored field borders, or icons over blinking pictures for drawing attention to invalid fields
- 4D Chart-based offscreen text rendering is a legacy technique; current form object formatting/conditional-style properties can achieve similar visual feedback without generating pictures
