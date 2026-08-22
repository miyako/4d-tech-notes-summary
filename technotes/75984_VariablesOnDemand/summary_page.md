# Tech Note 10-01: Variables On Demand

**Author:** Charles "Charlie" Vass, Technical Services Team Member, 4D Inc., and Peter Lerch, Softworks AG
**Published:** January 8, 2010 | **Product/Version:** 4D v11.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75984
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_01-04_(JAN)/10-01_VariablesOnDemand.zip

## Proposition
This note documents "Variables On Demand" (VOD), a 4D v11 SQL component that lets host databases dynamically declare, reference via pointer, and garbage-collect "anonymous" variables at runtime — even in compiled applications where variables are normally static and compile-time typed.

## Key Points
- Normal 4D variables are static: name, type, and scope are fixed at **compile time**; a VOD is created at **runtime** with an anonymous name accessed via pointer.
- Builds on a technique first introduced in **Technical Note 09-07, "4D v11 SQL Assimilator"** (asset #75182).
- Provides **cooperative garbage collection** and namespaces so the variable pool is not purely static after compilation.
- API includes **DVar4D_Startup, DVar4D_New/New2D, DVar4D_Get, DVar4D_IsDefined, DVar4D_Clear/ClearGroup**, and introspection methods like DVar4D_Declared and DVar4D_Array_Size.
- Reduces the need for developers to know the specific names of on-demand variables in the host structure.
- Demo database illustrates practical component usage.

## Featured Technology
- Variables On Demand (VOD) 4D v11 SQL component
- DVar4D_New / DVar4D_Get / DVar4D_Clear pointer-referenced variable API
- Cooperative garbage collection for dynamic variable pools

## Best Practices Highlighted
1. Use pointer-referenced, garbage-collected variable pools instead of pre-declaring large numbers of static variables "just in case" they're needed.
2. Namespace/group variables so they can be cleared together (DVar4D_ClearGroup) when no longer needed, avoiding memory bloat.
3. Prefer a well-tested shared component for this pattern rather than a bespoke, ad hoc "dynamic stack space" implementation per project.

## Context / Positioning
Published as a follow-up refinement to the "4D v11 SQL Assimilator" technique, this note packaged a long-standing developer workaround (dynamic/reusable variable pools) into a reusable, documented component.

## Historical Commentary
**Status:** Partially Superseded

This note documents a component that lets a 4D application dynamically create, reference (via pointer), and garbage-collect anonymous variables at runtime, addressing a real limitation of the classic language where variables are statically declared and scoped at compile time even in compiled applications. This runtime-variable-pool pattern is a clever workaround for a genuine 4D classic-language constraint, and it would still function today.

However, since 4D v16-17 the language has gained project-based classes, native Collection/Object types, and dynamic attribute assignment on objects, all of which give developers far more idiomatic ways to model dynamic, on-demand data than a hand-managed pool of anonymous pointer-referenced variables, making this component's technique largely superseded by more modern language features.
