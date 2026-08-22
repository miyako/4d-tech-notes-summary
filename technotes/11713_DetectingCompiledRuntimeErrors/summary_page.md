# Tech Note 96-34: Detecting Compiled Mode Runtime Errors

**Author:** ACI US Technical Support
**Published:** July 1, 1996 | **Product/Version:** 4th Dimension Compiler v3.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11713
**Download:** https://kb.4d.com/DLTN/TN/1996/Windows/TN_1996_31-34_(JUL)/96-34_Compiled_Runtime_Errors.exe

## Overview
This Tech Note explains why certain 4D runtime errors — such as a type mismatch in an EXECUTE command's parameters — only surface after compiling an application, and presents a debug-mode workaround technique using explicitly typed process variables to catch these errors while still working in interpreted mode.

## Key Points
- **Root cause:** the 4D interpreter is more permissive about data types than compiled code, so certain type mismatches pass silently while interpreted but trigger runtime errors only after compilation.
- **Roughly a dozen categories** of compiled-mode-only runtime errors are enumerated, with the EXECUTE command's dynamic parameter passing as the primary example.
- **Workaround technique:** declare process variables with the explicit, strict types matching what a construct like EXECUTE expects, so the interpreter itself throws an error immediately rather than silently masking the mismatch.
- **Worked example:** shows a parameter type mismatch passing silently by default, then being caught immediately once the variable is given an explicit type — allowing iterative debugging without a full compile cycle.

## Featured Technology
- 4D Compiler
- EXECUTE command
- Typed process variables (debug-mode error simulation)

## Historical Context
Modern 4D's compiler produces detailed, specific type-mismatch diagnostics directly at compile time, and 4D's type system has become significantly stricter and more consistent between interpreted and compiled execution, narrowing the class of bugs this note addresses. The EXECUTE command itself is a legacy dynamic-code-execution construct rarely central to modern application design. As a result, the manual pre-compilation error-simulation workaround described here is largely superseded, though its underlying caution — that interpreted and compiled 4D code can behave differently — remains a valid general principle for developers to keep in mind.
