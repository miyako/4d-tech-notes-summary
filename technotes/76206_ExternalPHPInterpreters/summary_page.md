# Tech Note 10-32: Using External PHP Interpreters in 4D v12

**Author:** Jesse Piña, Technical Services Team Member, 4D Inc.
**Published:** November 12, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76206
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_31-35_(NOV)/10-32_External_PHP_Interpreter.zip

## Proposition
Jesse Piña's Tech Note explores 4D v12's ability to execute PHP scripts, contrasting the internal PHP interpreter built into 4D with the option of configuring an external interpreter instead.

## Key Points
- 4D v12 has an internal PHP interpreter, but developers can substitute an external one for more control
- Documents platform-specific setup steps for Windows and Mac OS
- Includes a 'failure test' procedure to confirm the external interpreter is correctly wired up
- Provides two worked examples of executing PHP functionality from 4D
- Aimed at cases needing PHP versions/extensions beyond what 4D's internal engine offers

## Featured Technology
- 4D's built-in PHP interpreter
- external PHP interpreter configuration
- PHP EXECUTE command
- Windows/Mac PHP setup

## Best Practices Highlighted
- Run the documented failure test after setup to confirm the external interpreter path works before relying on it in production

## Context/Positioning
Published shortly after 4D v12 introduced native PHP scripting, helping developers extend or replace the bundled interpreter for advanced PHP needs.

## Historical Commentary
**Status:** Deprecated

This note documents configuring an external PHP interpreter to complement 4D v12's internal PHP engine — a feature 4D has since dismantled entirely: the built-in PHP interpreter was removed in 4D v20 R3, and the PHP command set itself was formally deprecated starting in 4D v21, with 4D now recommending System Workers to run external scripts instead. The specific setup steps for the internal/external interpreter split described here no longer reflect 4D's current PHP story at all.
