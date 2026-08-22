# Tech Note 20-21: New Variable Declaration

**Author:** Bryan Yen, Technical Services Engineer, 4D Inc.
**Published:** November 30, 2020 | **Product/Version:** 4D v18 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78598
**Download:** https://kb.4d.com/DLTN/TN/2020/20-21_NewVariableDeclaration.zip

## Proposition
As 4D moves further into object-oriented programming, the classic `C_TEXT`/`C_OBJECT`-style variable declarations can't express that an object variable references a specific class, limiting autocomplete and readability. This Tech Note introduces the new `var` declaration syntax, explains its benefits for class-typed variables, and ships a component to convert existing databases to the new style.

## Key Points
- **New syntax**: `var $varName : Text` replaces `C_TEXT($varName)`, supporting all standard types plus class references.
- **Class-typed variables**: `var $file_o : 4D.File` or `var $obj_o : cs.myClass` let a variable point to a specific 4D or user class rather than a generic Object.
- **Autocomplete boost**: class-typed variables trigger member-function suggestions in the method editor; generic-Object variables only suggest previously-used property names.
- **Private function hiding**: functions prefixed with `_` are correctly excluded from autocomplete suggestions on class-typed variables.
- **Known limitations (as of v18R4)**: `var` does not support inter-process variables or arrays — these still require Array/Compiler theme declarations.
- **Migration tooling**: an included component provides an "Open Update Variables Form" to bulk-apply `var` declarations and re-type generic Object variables to specific classes across a database's methods.
- **Editor lock constraint**: conversion operations cannot run while the target method is open in the code editor.

## Featured Technology
- `var` keyword declaration syntax
- `4D.<className>` / `cs.<className>` typed object references
- Method editor autocomplete / type-ahead
- Private class function convention (`_` prefix)
- Bundled "Update Variables" conversion component

## Best Practices Highlighted
1. Prefer `var` with explicit class types over generic Object declarations to get better autocomplete and clearer code intent.
2. Use the underscore-prefix convention to keep internal class helper functions out of the public autocomplete surface.
3. Migrate legacy Compiler-theme declarations incrementally using the provided conversion tooling rather than manual find-and-replace.

## Context / Positioning
This note reflects a key milestone in 4D's multi-year transition to modern, class-based OOP: having introduced classes and ORDA, 4D needed a declaration syntax expressive enough to type variables against those classes, improving IDE ergonomics (autocomplete) that developers coming from other object-oriented languages expect. It's part of a broader wave of tooling and documentation aimed at helping existing 4D codebases modernize incrementally rather than through a disruptive rewrite.

## Historical Commentary
**Status:** Still relevant

The `var` declaration syntax introduced here has become 4D's standard, recommended way to declare variables, and class-typed declarations (`4D.ClassName`/`cs.ClassName`) are now routine in idiomatic 4D code — this note's core guidance remains accurate today. The old Compiler-theme (`C_TEXT`, `C_OBJECT`, etc.) declarations still work for backward compatibility but are considered legacy style for new development. The one caveat noted at the time — that arrays and inter-process variables aren't covered by `var` — has remained true, since arrays are handled as a distinct 4D language construct; developers today would still combine `var` for scalar/object/class variables with the classic `ARRAY` commands where arrays are genuinely needed.
