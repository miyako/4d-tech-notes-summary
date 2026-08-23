# Tech Note: Recursion by Example

- **Asset ID:** 16389
- **Tech Note #:** 01-33
- **Published:** July 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Cha Yang
- **Page URL:** https://kb.4d.com/assetid=16389
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_31-35_(JUL)/01-33_Recursion_by_Example.hqx

## Overview

Cha Yang (4D, Inc. Technical Engineer) provides a general overview of recursion as a 4D programming technique, explaining how the stack tracks each nested method call, then demonstrates the idea with a simple factorial method before applying it to a real, practically useful example: converting a numeric amount into its English word form.

## Key Points

- Defines recursion as a method calling itself until a condition is met, and explains that each call pushes onto 4D's stack the return address and local variable state, consuming stack space until the base case unwinds it — exceeding available stack raises "Not enough Stack Space to complete the current Method."
- Example 1, `RecursiveFactorial`, computes 3! in five lines (`$0:=$1*RecursiveFactorial($1+1)` with a base case at `$1<=3`), with a step-by-step trace of how the stack builds up through levels and unwinds multiplying values back (1→3→6→6).
- Example 2, `NumToText` (by Dave Batton, DataCraft, from a 4D NUG snippet by Kirk Brooks, part of the "Check Register" example database), recursively converts a `real` dollar amount into words — e.g., `NumToText(5432)` divides off thousands (`$dollars\1000`), recurses on the remainder, and concatenates words like "Five Thousand Four Hundred Thirty Two", useful for printing checks.
- Shows the method wired into a field's object method via `Case of : (Form event=On Data Change) Self->:=Round(Self->;2) ... vDollarsText:=NumToText(Self->)`.
- Advises recursion is well-suited to naturally self-similar problems/data structures (e.g., trees), but that an iterative loop should be preferred when available since recursion carries real stack/storage overhead.

## Featured Technology

- Recursive project methods
- Method call stack behavior in 4D
- RecursiveFactorial example method
- NumToText digit-to-words conversion (Dave Batton, DataCraft)
- Object method On Data Change event

## Historical Commentary

**Status:** Still relevant

This note's explanation of 4D's recursion mechanics and the accompanying factorial/NumToText examples remain fully applicable today: recursive method calls work the same way in current 4D versions, including in class-based, ORDA-era code, and the stack-overhead tradeoff discussed is still the same consideration developers must weigh between recursive and iterative solutions. Nothing about this fundamental, language-agnostic technique has been superseded by newer 4D features.

**References to newer/updated information:**
- Recursive method/function calls remain fully supported and largely unchanged in current 4D versions, including in 4D's class-based (ORDA/Project Mode) methods
- No newer 4D-specific construct has replaced recursion as a general control-flow technique
