# Tech Note 17-24: 4D Mobile Unit Testing (Revised)

**Author:** Xiang Liu, Technical Services Team Member, 4D Inc.
**Published:** December 20, 2017 | **Product/Version:** 4D Mobile v16 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77910
**Download:** https://kb.4d.com/DLTN/TN/2017/17-24_4DMobileUnitTesting_r2.zip

## Proposition
Explains how to use Wakanda Studio's built-in Mocha/Chai unit-testing feature to write, run, and review automated server-side tests for a 4D Mobile application's exposed tables, attributes, and methods.

## Key Points
- **Mocha and Chai:** Wakanda incorporated these two JavaScript testing frameworks starting with version 2.1, alongside a new "Test" button in Studio.
- **Test workflow:** writing individual test cases, grouping them logically, executing them hands-free on the server, and reviewing results exported in JSON format.
- **Testing exposed table/attribute/method existence:** verifies that the 4D Mobile-exposed data model matches expectations.
- **Testing CRUD and query operations:** validates that create/read/update/delete and query behavior work correctly against exposed tables.
- **Testing custom method calls:** demonstrates asserting on results of a custom method (e.g., `raiseSalaries`) with Chai's `expect().to.equal()` syntax.
- **Server-side only limitation:** the note is explicit that, at the time, this testing feature only covered server-side logic, with front-end/UI testing left as future work.

## Featured Technology
- Wakanda Studio unit testing (Mocha, Chai)
- 4D Mobile table/attribute/method exposure
- JSON test result export

## Best Practices Highlighted
1. Group related test cases logically to keep growing test suites organized.
2. Test both structural existence (tables/attributes/methods) and behavioral correctness (CRUD, custom methods) rather than just one or the other.
3. Review exported JSON test results as part of a regular development/regression-checking workflow.

## Context / Positioning
This note is part of 4D's now-discontinued "4D Mobile" line, which paired classic 4D data with the separate Wakanda JavaScript server/studio platform to expose data and logic to native mobile clients. It represents 4D's mid-2010s mobile strategy, well before ORDA/REST matured as the primary data-access layer and before tools like Qodly existed.

## Historical Commentary
**Status:** Obsolete

Both 4D Mobile and the Wakanda platform underlying it (including Wakanda Studio and its Mocha/Chai test-runner integration) have been fully discontinued by 4D, so the exact tooling and workflow described in this note can no longer be used with current 4D products. Developers cannot reproduce this testing setup today because the Wakanda Studio "Test" button and its JSON test-result export no longer exist in any supported 4D offering.

The underlying testing philosophy, however, is not obsolete: unit testing exposed data operations (existence checks, CRUD, custom method behavior) using Mocha/Chai-style assertions remains standard practice in JavaScript development generally, and would now be applied against 4D's REST server (built on ORDA) using modern JS test runners rather than Wakanda Studio. The note's mention of needing separate front-end/UI testing tooling also foreshadowed a gap that was never filled before 4D Mobile itself was discontinued.
