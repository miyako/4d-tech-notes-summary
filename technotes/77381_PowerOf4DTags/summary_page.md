# Tech Note 15-17: Exploring the Power and Versatility of 4D Tags

**Author:** Charles "Charlie" Vass, Technical Services Engineer, 4D Inc.
**Published:** September 28, 2015 | **Product/Version:** 4D v15 (tag engine enhanced in v14 R4) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77381
**Download:** https://kb.4d.com/DLTN/TN/2015/15-17_ExploringPowerOf4DTags.zip

## Proposition
`PROCESS 4D TAGS` (renamed from `PROCESS HTML TAGS`) is far more capable than its historical association with web pages suggests. This note explains the full 4D Tags vocabulary and demonstrates using it for classic dynamic web serving as well as general document templating, report generation, and automation scripting.

## Key Points
- **Renaming and scope expansion:** `PROCESS HTML TAGS` became `PROCESS 4D TAGS` to reflect that it processes text files, variables, and BLOBs — not just HTML.
- **Classic web-serving patterns:** semi-dynamic HTML (SHTML) templates, tag-embedded HTML served via `4DACTION`, `4DCGI`, or custom URLs.
- **Non-web templating:** building report templates, inserting raw HTML with `4DHTML`, and embedding one HTML document's body inside another.
- **Core tag vocabulary:** `4DBASE` (base reference), `4DELSEIF` (conditionals), `4DEVAL` (inline expression evaluation), `4DSCRIPT` (calling 4D commands/methods), `4DLOOP` (iteration, enhanced in v14 R4, supports recursion).
- **Creative applications:** generating end-user automation scripts, hierarchical lists, and even SVG output using the same tag engine.
- **Security section:** explicit guidance on preventing malicious code injection when processing tags against user-supplied content, plus precautions and editor tooling suggestions.
- **Common pitfalls documented:** context mismatches, `4DEVAL` variable scope quirks, whitespace sensitivity, and styled-text interactions.

## Featured Technology
- `PROCESS 4D TAGS` (formerly `PROCESS HTML TAGS`)
- Tag vocabulary: `4DHTML`, `4DBASE`, `4DELSEIF`, `4DEVAL`, `4DSCRIPT`, `4DLOOP`
- `4DACTION` / `4DCGI` (classic 4D web server request handlers)

## Best Practices Highlighted
1. Match the input template's structure/context to the intended output context to avoid malformed results.
2. Sanitize or restrict user-supplied content before running it through `PROCESS 4D TAGS` to prevent code injection.
3. Use recursive tag processing carefully and test debugging paths, since tag errors can be hard to trace.
4. Watch for stray whitespace in templates, which can silently break tag parsing.

## Context / Positioning
This note reflects classic Design-Mode-era 4D (v14 R4/v15, 2015) where the built-in 4D web server and its proprietary tag-templating dialect were still central to how 4D developers built dynamic web content — years before Project Mode, ORDA, and the modern expectation of separate JS-based front ends talking to 4D over REST.

## Historical Commentary
**Status:** Partially superseded

`PROCESS 4D TAGS` and its tag vocabulary still exist in current 4D for backward compatibility, but the broader pattern of using 4D's built-in web server with proprietary template tags to generate dynamic HTML has been largely superseded by REST/JSON APIs (via ORDA) feeding modern JavaScript front ends. The non-web templating use cases shown here (reports, document generation, automation scripts) remain conceptually valid, though 4D Write Pro's merge-field/expression system now offers a more modern, less proprietary alternative for document templating specifically.
