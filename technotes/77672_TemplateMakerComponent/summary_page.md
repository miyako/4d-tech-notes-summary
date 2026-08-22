# Tech Note 16-18: Template Maker Component

**Author:** Charlie Vass, Technical Services Engineer, 4D Inc.
**Published:** October 31, 2016 | **Product/Version:** 4D v15 R5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77672
**Download:** https://kb.4d.com/DLTN/TN/2016/16-18_TemplateMaker.zip

## Proposition
The TemplateMaker component lets a developer turn an ordinary 4D project method into a portable, security-protected template built on 4D Transformation Tags, so that new reports, exports, or graphs can be delivered to an already-deployed database with little to no downtime and no structure redeployment.

## Key Points
- **Origin:** inspired by an internal 4D engineering technique introduced in v15 R4 for adding new capabilities without core 4D code changes.
- **Two-step model:** first capture a project method as a template (wrapping it in `<!--#4DCODE-->`); second, provide a host-database interface to feed data into the template and render output.
- **Security key protection:** ensures template integrity against external tampering after export.
- **Export formats:** templates can be exported as clear text or Base64-encoded.
- **Shared hidden methods:** `4DTM_Macro`, `4DTM_Macro_Selection` (exposed as Macros v2 menu items in the project method editor), and `4DTM_Execute` (called from host code to run a saved template).
- **Installation:** drop the component into the host database's Components folder; requires 4D v15 R4 or later.
- **Related prior notes:** builds on techniques from earlier notes on "Smart Templates" and an "Enhanced Graph Component."

## Featured Technology
- 4D Transformation Tags (`<!--#4DCODE-->`)
- TemplateMaker component (4D v15 R4+)
- Macros v2 (4D Method Editor macro menus)
- BASE64-encoded template export

## Best Practices Highlighted
1. Use a security key to protect exported templates from unauthorized modification before deployment.
2. Store templates in a configurable location (not hard-coded to the default Resources/Templates folder) for deployment flexibility.

## Context / Positioning
Published October 2016 for 4D v15 R5, this note is a product of the classic, binary Design Mode era of 4D, where deploying new database code traditionally meant shipping a whole new compiled structure file. TemplateMaker exists specifically to route around that constraint by embedding executable logic in text-based transformation-tag templates instead.

## Historical Commentary
**Status:** Partially superseded

4D Transformation Tags themselves are still a supported mechanism, but the broader problem this component solves — deploying new logic to a live database without redeploying the whole structure — has been substantially addressed by 4D's move to Project Mode (v17+, 2018), where application code lives in individual text files that can be version-controlled and deployed incrementally via Git and standard CI/CD pipelines.

As a result, the macro-driven, structure-avoidance workflow TemplateMaker automates is less commonly needed in current 4D development. Teams working in Project Mode would typically just commit and deploy an updated method file directly rather than wrapping logic in a transformation-tag template purely to avoid a structure update.
