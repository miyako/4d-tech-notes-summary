# Tech Note 15-14: Handle Date and Time through 4D Mobile

**Author:** Xiang Liu, Technical Services Engineer, 4D Inc.
**Published:** July 8, 2015 | **Product/Version:** 4D Mobile v14.x (demos require Wakanda Enterprise 10 + 4D v14 R5 or later) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77330
**Download:** https://kb.4d.com/DLTN/TN/2015/15-14_DateTimeThru4DMB.zip

## Proposition
4D stores Date and Time as two distinct field types, while JavaScript represents both as a single millisecond-based Date object. This note explains that mismatch and shows how to correctly read, query, and update 4D Date/Time data from 4D Mobile client code and the Wakanda server layer.

## Key Points
- **JavaScript Date object primer:** four constructor forms (no args, milliseconds since epoch, date string, full numeric args) and get/set accessor methods.
- **4D vs. JavaScript command mapping:** e.g., `Date()` behaves like the JS `Date()` constructor; `Date.getDay()` parallels `Day number`; `Date.getDate()` parallels `Day of`.
- **No native "time" type in JavaScript:** unlike 4D's separate Time field, JS folds time into the single Date object.
- **Wakanda vs. 4D attribute types:** contrasts Wakanda's date/duration attributes against 4D's Date/Time fields structurally.
- **Reading date/time in 4D Mobile:** formatting on the client side vs. formatting on the Wakanda server side.
- **Querying date/time:** covers both formatted client-side attributes and calculated server-side attributes.
- **Modifying date/time:** saving to formatted client-side attributes vs. calculated server-side attributes.

## Featured Technology
- JavaScript `Date` object
- Wakanda date/duration attribute types
- 4D Date and Time field types
- 4D Mobile client/server method architecture

## Best Practices Highlighted
1. Explicitly convert between 4D's separate Date/Time fields and JavaScript's single Date object rather than assuming automatic compatibility.
2. Be deliberate about whether a date/time value is formatted client-side or calculated server-side, since query and save behavior differs between the two.

## Context / Positioning
This note is deep in the original 4D Mobile era (2015): native mobile/web apps built with a Wakanda JavaScript client/server layer bridging to a 4D back end, entirely predating ORDA and Project Mode. It reflects a period when 4D Mobile depended on a separate, JavaScript-native product (Wakanda) rather than 4D's own REST server.

## Historical Commentary
**Status:** Obsolete

Both 4D Mobile (in its original native-app form) and the Wakanda product it depended on have since been fully discontinued in favor of ORDA-based REST APIs and newer web/mobile approaches like Qodly, so the specific mechanics in this note no longer apply to current 4D projects. The underlying conceptual issue — reconciling 4D's separate Date/Time fields with JavaScript's single Date object — remains a genuinely relevant consideration whenever 4D data is serialized to JSON for any JS-based client, but developers today would solve it through ORDA's REST date serialization rather than the Wakanda-specific techniques shown here.
