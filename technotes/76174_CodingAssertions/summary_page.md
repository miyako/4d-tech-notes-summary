# Tech Note 10-28: Pinpoint Coding problems using 4D v12 Assertions

**Author:** Charles “Charlie” Vass, Technical Services Team Member, 4D Inc.
**Published:** September 10, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76174
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_28-31_(SEP)/10-28_Programming_4D_Assertions.zip

## Proposition
Charles Vass's Tech Note introduces assertions as a formal debugging discipline newly supported in 4D v12 via four commands (ASSERT, Asserted, Get assert enabled, SET ASSERT ENABLED) and two new system variables (Error method, Error line).

## Key Points
- Introduces four new 4D v12 commands: ASSERT, Asserted, Get assert enabled, SET ASSERT ENABLED
- Adds two new system variables, Error method and Error line, for building custom assert-failure handling
- Contrasts manual assumption-checking code with the new ASSERT/Asserted approach
- Shows the default v12 Assert-failed alert and how to override it with a custom alert
- Assertions are a lightweight technique for catching logic errors during development, not production error handling

## Featured Technology
- ASSERT command
- Asserted function
- SET ASSERT ENABLED
- Get assert enabled
- Error method / Error line system variables
- ON ERR CALL

## Best Practices Highlighted
- Use ASSERT to validate assumptions about program state during development, disabling assertions for production builds via SET ASSERT ENABLED
- Build a custom assert-failure handler with ON ERR CALL plus Error method/Error line for better diagnostics

## Context/Positioning
Published as 4D v12 introduced formal language-level assertion support, giving 4D developers a debugging tool long available in other programming languages.

## Historical Commentary
**Status:** Current

Assertions are a timeless, language-agnostic debugging discipline, and 4D's ASSERT/Asserted/SET ASSERT ENABLED commands introduced in v12 remain in the current 4D language largely unchanged, so this technique is still directly applicable today. This is one of the rare cases in this era where the guidance is close to evergreen: the recommended practice of validating assumptions in code with assertions has not been superseded by any newer 4D paradigm.
