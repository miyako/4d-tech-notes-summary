# Tech Note 17-05: Format Data For Display in 4D Mobile

**Author:** Xiang Liu, Technical Services Team Member, 4D Inc.
**Published:** March 27, 2017 | **Product/Version:** 4D Mobile v16 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77754
**Download:** https://kb.4d.com/DLTN/TN/2017/17-05_4DMobileDisplayFormat.zip

## Proposition
4D Mobile (built on the Wakanda Application Framework) supports attribute-level display formatting so that number, string, and date values are automatically formatted for web/mobile clients without ad hoc client-side code. This note documents the available format placeholders and how to apply formats both server-side (via the data model / editor) and client-side (via REST and the Dataprovider).

## Key Points
- **Number formats:** placeholders `#` (no leading/trailing zero) and `0` (force zero), `,`/`.` separators, and `0%` percentage formatting, e.g. `"$##.00"` → `$2.30`.
- **String formats:** single-character options `U`/`l`/`C`/`c` for uppercase/lowercase/capitalize-first-word/capitalize-each-word, plus `#`-wildcard wrapping like `"(#)"` → `(Mr.)`.
- **Date formats:** twelve tokens (`d`, `dd`, `o`, `oo`, `D`, `DD`, `m`, `mm`, `M`, etc.) controlling day/month/year representation and name length.
- **Server-side application:** formats can be set via `model.<Table>.<Attribute>.defaultFormat = {presentation:"text", format:"..."}` in the 4D Mobile data model.
- **Client-side access:** the `defaultFormat` property is retrievable through REST calls and the Wakanda Dataprovider so client frameworks can apply it consistently.
- **Cross-platform intent:** formatting is meant to work uniformly regardless of the client-side JS framework used to consume 4D Mobile data.

## Featured Technology
- 4D Mobile (Wakanda Application Framework)
- Wakanda Enterprise 1.1.3 data model editor
- REST API / Dataprovider
- `defaultFormat` attribute property (number/string/date)

## Best Practices Highlighted
1. Centralize formatting rules in the data model rather than duplicating format logic across every client.
2. Combine model-level formats with server-exposed methods for maximum flexibility across heterogeneous web clients.

## Context / Positioning
Published in March 2017 against 4D v16 and Wakanda Enterprise 1.1.3, this note documents 4D Mobile — 4D's native mobile/web app framework of that era, built on the bundled Wakanda server, well before ORDA (introduced ~v16 R5/R6, 2017) matured into the standard data-access layer. It is a snapshot of a parallel web/mobile stack 4D was building at the time, distinct from the classic Design Mode desktop application development most other tech notes of this period describe.

## Historical Commentary
**Status:** Obsolete

4D Mobile and its underlying Wakanda engine were discontinued as 4D shifted its web/mobile strategy toward ORDA-based REST APIs and, later, the Qodly low-code web platform. The data model editor, `defaultFormat` attribute properties, and the Wakanda Dataprovider/REST described in this note no longer exist in current 4D products.

The formatting *concepts* — number placeholders, string casing options, date tokens — are still broadly useful ideas, but a developer today would implement them either in application-layer JavaScript/TypeScript on the client, or via ORDA computed attributes/formulas on the server, rather than through any of the specific mechanisms this note describes. This is one of the clearest examples in the 2016–2017 corpus of a tech note whose entire subsystem has since been retired.
