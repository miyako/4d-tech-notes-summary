# Tech Note 09-13: Pointers Revisited

**Author:** Timothy Penner, Technical Services Team Member, 4D Inc.
**Published:** April 2, 2009 | **Product/Version:** 4D v11.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75241
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_13-17_(APR)/09-13_Pointers_Revisited.zip

## Proposition
A refreshed, example-rich tutorial (updating 2001's "Pointers from Scratch") that demystifies the 4D pointer type for developers unfamiliar with the concept, covering how pointers work and everything they can reference.

## Key Points
- **Variables recap:** grounds pointers by first explaining what a typed variable and its memory allocation actually are.
- **Referencing vs. dereferencing:** `->variable` gets a pointer; `pointer->` reads/writes the pointed-to value; `Get pointer("name")` creates a pointer from a variable name string.
- **Type-agnostic pointers:** unlike C, a single 4D pointer variable (C_POINTER) can point to any variable type once declared.
- **What pointers can reference:** objects/form controls (with an explicit compatible/incompatible object type list), process/interprocess/local variables, tables, fields, arrays, array elements, and pointers-to-pointers.
- **Self command:** returns a pointer to the current object only inside an object method; returns a Nil pointer if called out of context.
- **Component/host boundary rules:** pointers are the only way to share variables across the component/host boundary; compiled code can dereference pointers built in interpreted code, but not the reverse; comparing pointers by resolved name across components is unreliable — compare pointer values directly instead.
- **Table pointers are special:** they cannot be directly dereferenced to a "value" outside of commands that explicitly accept table parameters.

## Featured Technology
- 4D Pointer type (C_POINTER) and pointer/dereference operator (->)
- Get pointer / Self / Table / Field / RESOLVE POINTER commands
- Pointers to variables, fields, tables, arrays, array elements, and pointers-to-pointers
- Passing pointers between component and host database

## Best Practices Highlighted
1. Prefer direct pointer syntax (`->variable`) over `Get pointer` when the variable name is already known, for speed and clarity.
2. Use parentheses when multiple-dereferencing pointers-to-pointers to avoid ambiguity.
3. Never compare pointers across a component boundary by resolved variable name; compare the pointers themselves.
4. Declare pointers explicitly (C_POINTER) — mandatory in compiled databases.

## Context / Positioning
Published as an accessible follow-up to the original 2001 "Pointers from Scratch" note, aimed at helping developers — especially those newer to 4D — build solid intuition for a concept many find difficult, using everyday analogies alongside code.

## Historical Commentary
**Status:** Current

This is foundational classic-language material, and 4D has preserved full backward compatibility for pointers, so essentially everything here — referencing, dereferencing, pointer scoping, and the component/host sharing rules — remains accurate today.

The one nuance is that modern 4D (object references, shared objects/collections, and classes from v16-v17+) now offers alternative, often more idiomatic, ways to share and mutate state across methods for some scenarios where pointers were historically the only option, but pointers themselves are not deprecated and continue to be a core, actively used part of the language.
