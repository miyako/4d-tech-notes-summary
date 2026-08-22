# Tech Note 15-22: Exporting the Smart Way — Using Smart Templates

**Author:** Thomas Maul, VP of Strategy – 4D Product Line, 4D Germany (edited by Charlie Vass, 4D Inc.)
**Published:** November 17, 2015 | **Product/Version:** 4D v15 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77417
**Download:** https://kb.4d.com/DLTN/TN/2015/15-22_ExportTheSmartWay.zip

## Proposition
This note presents Smart Templates, a template-driven export architecture (available since 4D v14 R5) that replaces per-report hand-coded SEND PACKET export methods with externally editable templates, so new or revised report exports (tab-delimited, HTML, Excel, Word) can be delivered without redeploying application code.

## Key Points
- **Problem addressed:** constant requests for new/changed exports traditionally required new SEND PACKET methods and a full structure redeployment.
- **Smart Templates concept:** report content, format, and formulas live in an external template executed by one generic entry point, available since v14 R5.
- **Progressive examples:** simple tab-delimited text, tab-delimited with calculated values, HTML with calculated values, HTML with images, and HTML with an embedded table.
- **Microsoft Excel output:** demonstrates conditional formatting driven through the template engine.
- **Microsoft Word output:** generates personalized documents (gift cards) as a mail-merge-like use case.
- **Decoupling benefit:** report changes can potentially be made without a new application structure deployment.
- **Authored by 4D Germany leadership,** reflecting a broader strategic push around flexible reporting/export tooling.

## Featured Technology
- 4D v14 R5+ template execution model
- SEND PACKET (classic export baseline)
- HTML/Excel/Word document generation from 4D
- Conditional formatting in generated Excel output

## Best Practices Highlighted
1. Separate report definition (template) from application code so exports can change without redeploying the structure.
2. Provide one generic execution entry point that consumes different templates rather than one method per report.
3. Use the appropriate output format (tab-delimited, HTML, Excel, Word) matched to the consumer's actual downstream need.

## Context / Positioning
This Tech Note was published in 2015, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Still Relevant

The Smart Templates architecture is a durable, still-valuable idea — decoupling report/export definitions from compiled application code so exports can be updated without a redeploy — and the specific output formats it targets (tab-delimited text, HTML, Excel, Word) are exactly what developers still need to produce. As a 4D-Germany-authored technique rather than a core 4D feature, its practical relevance today depends on whether a project actually adopted this or an equivalent templating approach, but the concept itself is not dated by the classic-to-Project-Mode transition or by ORDA.
