# Tech Note 11-23: Dynamic Variables in 4D v12

**Author:** Christophe Keromen, Cabinet de Consultants CKTI
**Published:** July 22, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76377
**Download:** https://kb.4d.com/DLTN/TN/2011/11-23_DynamicVariables.pdf

## Proposition
This Tech Note introduces dynamic (form) variables, a new 4D v12 concept, and presents a custom XVH component that lets a form using dynamic variables communicate incoming/outgoing data cleanly with its calling process.

## Key Points
- **Why dynamic variables:** motivated by reducing memory footprint and by the "window of vulnerability" when the same form is instantiated multiple times by different components sharing variable names.
- **Evaluated expressions as a forerunner:** a clock example illustrates the earlier technique that dynamic variables build upon.
- **Declaring and using dynamic variables:** shown via OBJECT Get pointer and pointer-based handling for multiple form instances.
- **The XVH component:** a reusable component enabling form-to-process communication built on dynamic variables.
- **Binding lifecycle:** getters/setters, binding methods called before display (On Load, On Validate) and after display of the form.
- **Broader communication:** covers both inter-process communication and communication between separate 4D applications, plus supporting utility methods.

## Featured Technology
- Dynamic/form variables (introduced 4D v12)
- OBJECT Get pointer and pointer-based variable binding
- XVH component for form/process communication

## Context / Positioning
Published mid-2011 shortly after 4D v12's release, this note helped developers understand and adopt a genuinely new language feature (dynamic variables) by pairing it with a concrete, reusable component (XVH) solving a real pain point: safely reusing forms across multiple simultaneous instances.

## Historical Commentary
**Status:** Still Relevant

Dynamic form variables and OBJECT Get pointer remain part of the classic 4D language and still function in current, backward-compatible 4D applications, so the mechanism itself is still valid.

However, the specific problem this note solves — reducing memory footprint and managing multi-instantiated component forms via pointer binding — is less pressing today given far larger typical memory budgets, and 4D's newer class-based language features now offer a cleaner, more object-oriented alternative to bespoke components like XVH for encapsulating form state.
