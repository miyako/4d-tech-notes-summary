# Tech Note: Emulating the FileMaker Pro Book Object in 4D, Part II

## Overview
- **Technical Note (number unavailable)**
- **Author:** Unknown / not specified
- **Published:** June 1, 2000
- **Product/Version:** 4D v6.5
- **Platform:** Mac & Win
- **Content source:** Teaser abstract only (full archive not recoverable)

## Key Points
This Tech Note is the second installment in a series aimed at replicating FileMaker Pro's distinctive 'book object' record-navigation control inside 4D applications, useful for developers courting or migrating users accustomed to FileMaker's interface conventions. The book object lets users click the upper 'page' to move back one record, the lower 'page' to move forward one record, and drag a tab slider to move fluidly forwards and backwards through FileMaker's 'found set' of records. Where an earlier technical note in the series implemented a technique that precisely mimicked this behavior, this Part II proposes a simpler alternative built around 4D's own ruler form object; the trade-off is that the result isn't pixel-for-pixel identical to FileMaker's book object, but the implementation code is considerably simpler and the tab's movement feels smoother, thanks to how 4D's ruler object is natively implemented. The featured technology is 4D's ruler form object, repurposed here as a record-navigation control rather than for its typical numeric-range-selection use case. Because only the teaser abstract survives for this note — its kb.4d.com page had no working download link at all — the specific ruler-object configuration and code shown in the full note could not be recovered here.

## Featured Technology
- 4D ruler object
- Record navigation UI
- FileMaker Pro book object emulation

## Historical Context
This note shows a simpler way to emulate FileMaker Pro's iconic 'book object' record-navigation control in 4D using the 4D ruler form object, trading exact visual fidelity for simpler code and smoother tab movement compared to a prior, more literal emulation technique. Competing with FileMaker's specific UI conventions was a real concern for 4D developers migrating users from FileMaker Pro in this era; today, record-navigation UI patterns and the specific 4D ruler-object mechanics described are dated compared to modern list/table form objects, giving this note mainly historical interest, though the general idea of repurposing a slider-like object for record navigation remains conceptually approachable.

**Note on sources:** The full downloadable archive for this Tech Note could not be recovered in this environment. The original kb.4d.com page's linked download was an old Windows self-extracting installer (.exe) that could not be extracted in this environment, so this summary is based only on the teaser abstract.

## What's Changed Since
- Modern 4D form objects (list boxes, table forms) offer more contemporary ways to build record-navigation UI than repurposing a ruler object
- This note's approach was explicitly aimed at competing with FileMaker Pro's specific book-object UI convention of that era, a design pattern less commonly emulated today

