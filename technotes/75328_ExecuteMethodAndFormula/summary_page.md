# Tech Note 09-15: EXECUTE METHOD and EXECUTE FORMULA

**Author:** Silvio Belini, Technical Services Team Member, 4D Inc.
**Published:** April 16, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75328
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_13-17_(APR)/09-15_Execute.zip

## Proposition
This note clarifies that 4D 2004's EXECUTE command was renamed to EXECUTE FORMULA in 4D v11 SQL (with unchanged behavior), and introduces the new, more capable EXECUTE METHOD command for dynamically invoking named methods with parameters and return values, including across host/component database boundaries.

## Key Points
- **EXECUTE (4D 2004) → EXECUTE FORMULA (4D v11 SQL):** pure rename for clarity; syntax, functionality, and limitations are unchanged — a single-line statement string (method call, 4D command, or assignment) is interpreted, not compiled.
- **Compiled-mode limitation:** local variables cannot be passed as parameters to a method call within an EXECUTE FORMULA statement when running compiled, since the statement itself is never compiled.
- **New EXECUTE METHOD command:** invokes a named project or shared component method directly, supporting parameters and a return value (`EXECUTE METHOD(methodName{;result|*{;param1...paramN}})`).
- **Cross-database calls:** EXECUTE METHOD can call methods across host and component ("matrix") database boundaries, provided the target method is shared.
- **Three-way comparison** across use cases — simple formulas/assignments, host/component method calls, and multi-line code statements — to guide which command fits which scenario.

## Featured Technology
- EXECUTE FORMULA command (renamed from EXECUTE in 4D 2004)
- EXECUTE METHOD command (new in 4D v11 SQL)
- Dynamic method/formula execution and parameter passing
- Host/component (matrix) database method calls

## Best Practices Highlighted
1. Use EXECUTE METHOD rather than EXECUTE FORMULA when the goal is genuinely calling a named method with parameters/return value, since it avoids fragile string-formula construction.
2. Remember that EXECUTE FORMULA/EXECUTE statements are always interpreted, not compiler-checked, even in a compiled application — avoid passing local variables to method calls inside them in compiled mode.
3. Mark component methods as "Shared by components and host database" when they need to be callable via EXECUTE METHOD across the host/component boundary.

## Context / Positioning
Published as a clarifying reference right after 4D v11 SQL's command rename and new EXECUTE METHOD addition, this note helped developers migrating from 4D 2004 understand the terminology change while adopting the more powerful new dynamic-execution command.

## Historical Commentary
**Status:** Still Relevant

This note clarified the rename of 4D 2004's EXECUTE command to EXECUTE FORMULA and explained the new, more capable EXECUTE METHOD command introduced in 4D v11 SQL for dynamic method invocation with parameters and return values. Both commands remain fully functional and documented in current 4D versions, and dynamic/formula-based execution is still a legitimate, commonly used technique.

4D has since added complementary modern alternatives (such as Formula objects and formula-from-string features) that can be more convenient for some dynamic-execution scenarios in newer, class-based project-mode code, but the commands described in this note remain accurate and unchanged.
