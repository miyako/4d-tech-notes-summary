# Tech Note 25-04: Introduction to Shared Singleton Class: Dynamic Global Variables

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** April 28, 2025 | **Product/Version:** 4D v20 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79699
**Download:** https://kb.4d.com/DLTN/TN/2025/25-04_SharedSingletonClass.zip

## Proposition
Applications often need global state — configuration, session data, caches — that is readable and writable across processes. Historically 4D used interprocess variables, but these are incompatible with preemptive (thread-safe) processes. This note shows how shared singleton classes, introduced with 4D 20 R5, provide a modern, thread-safe alternative with a single guaranteed instance per application.

## Key Points
- **Shared objects require Use...End use:** Any object created via New shared object (or from a shared class) must be modified within a Use/End use block to safely lock it against concurrent process access.
- **Shared classes add the "shared" keyword:** Prepending "shared" to a class constructor or function makes instances shared objects and lets functions implicitly wrap This in Use/End use, eliminating boilerplate.
- **Singleton classes guarantee one instance per process:** Using the "singleton" keyword restricts instantiation; .new() or the .me property both return the same instance once created.
- **Shared singleton = best of both worlds:** Combining "shared singleton" in the class constructor produces a single shared-object instance visible and consistent across every process in the application.
- **GlobalVars class pattern:** A minimal shared singleton constructor plus a shared assign($name;$value) function is enough to implement dynamic, safely-shared global variables.
- **Variadic assign via parameter indirection:** Using `For ($i;1;Count parameters;2) This[${$i}]:=${$i+1}` lets one call set multiple global variables at once.
- **Type-validation guard pattern:** The assign function can check Value type() before overwriting an existing global to prevent unintended type changes and alert the developer.
- **Shared objects/collections need explicit shared creation:** Object or collection values stored as globals must be created via New shared object / New shared collection, since a shared singleton cannot hold non-shared child objects.

## Featured Technology
- **Shared Classes** — user classes whose instances are shared objects usable across processes.
- **Singleton Classes** — classes restricted to a single instance per process (.new()/.me).
- **Shared Singleton Classes** — combination enabling one process-wide shared instance.
- **Use...End use** — mandatory locking structure for safe shared-object mutation.
- **New shared object / New shared collection** — commands to create shared child values.
- **CALL WORKER** — used in the demo to spawn processes and demonstrate cross-process global visibility.

## Best Practices Highlighted
1. Prefer shared singleton classes over legacy interprocess variables for any thread-safe, cross-process global state.
2. Add type validation in setter functions to catch accidental type drift on shared global variables.
3. Always wrap direct mutations of a shared object/collection in Use...End use unless using the "shared" function shortcut.

## Context / Positioning
This note continues 4D's post-2018 shift toward object-oriented, thread-safe language constructs (ORDA in v17, classes in 18 R3, shared/singleton classes in 20 R5), reinforcing the platform's move away from legacy interprocess variables toward patterns compatible with modern multi-core, preemptive-process application architectures.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
