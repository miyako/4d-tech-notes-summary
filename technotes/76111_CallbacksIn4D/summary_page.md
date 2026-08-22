# Tech Note 10-17: How to Create and Use Callbacks in 4D

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc.
**Published:** June 8, 2010 | **Product/Version:** 4D v11.6 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76111
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_17-20_(JUN)/10-17_Callbacks.zip

## Proposition
This note explains what constitutes a callback in 4D — a method passed by name so that a component, plug-in, or subordinate process can invoke host-database logic without knowledge of its internals — and demonstrates how to build such callbacks using `EXECUTE METHOD`, since 4D lacks native function pointers.

## Key Points
- **Definition:** a callback is executable code (here, a 4D method) passed as an argument so a lower-level/external layer can call back into higher-level host logic.
- **Motivation:** enables encapsulation — a component (e.g. for shipping-document printing, TCP request routing, or serial-port hardware communication) doesn't need to know host-specific business logic, only a contracted callback signature.
- **Implementation:** since 4D has no true function pointers, `EXECUTE METHOD (methodName; result|*; params...)` is used as the mechanism to invoke a method by name.
- **Cross-component requirement:** callback methods callable from a component must have the "Shared by components and host database" property enabled.
- **Execution context matters:** a callback runs in the callee's process if no new process was launched for the caller, or in the caller's own process otherwise — this determines which process variables are in scope.
- **Native 4D examples:** `ON ERR CALL` and `ON EVENT CALL` are cited as 4D's own built-in (though differently named) uses of the callback pattern.

## Featured Technology
- 4D Method-based callbacks (passing method names as parameters)
- EXECUTE METHOD command
- Encapsulation/decoupling design pattern in 4D components
- Execution context of callback methods (host vs. component/subordinate process)

## Best Practices Highlighted
1. Design components around a published callback contract (parameter/return signature) rather than baking host-specific logic into the component.
2. Mark cross-boundary callback methods as "Shared by components and host database" so they are callable from within a component.
3. Understand and account for callback execution context (caller vs. callee process) when referencing process variables inside a callback.

## Context / Positioning
Published for 4D v11.6, this note targeted developers building or consuming 4D components, formalizing an architectural pattern (callbacks) that was already used informally via `ON ERR CALL`/`ON EVENT CALL` but not widely understood as a general-purpose technique.

## Historical Commentary
**Status:** Still Relevant

This note explains the classic-4D pattern of passing a method name as a parameter so a component or subordinate process can call back into host-database code without knowing its internals — a genuinely timeless encapsulation pattern that predates and survives 4D's later object-oriented additions.

The core concept (decoupling caller from callee via a published contract) remains valid and is still used in classic 4D code today, though modern 4D class-based programming (introduced v18/v19) offers additional ways to achieve the same decoupling via formulas, function pointers/4D.Function objects, and class methods, which are now often preferred for new component design.
