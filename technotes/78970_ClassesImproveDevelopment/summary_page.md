# Tech Note 22-14: Getting Acquainted with Classes to Improve Development in 4D

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** July 19, 2022 | **Product/Version:** 4D v19 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78970
**Download:** https://kb.4d.com/DLTN/TN/2022/22-14_ClassesAndDev.zip

## Proposition
Classes are a project-mode-only 4D feature that extends object notation into full user-defined data types with attributes, functions, and constructors. This note introduces class fundamentals and shows how adopting them — together with related code-editor improvements — can meaningfully improve day-to-day 4D development.

## Key Points
- **Classes require project mode** — they are not available in a binary/.4DB structure-file database.
- **The cs command exposes the class store**; a typed instance is declared as `var $x : cs.ClassName`, and object-notation access to class members is case-sensitive.
- **Class structure = attributes + functions**, illustrated with a worked Rectangle class exposing Length/Width attributes and Perimeter()/Area() functions (functions always require parentheses, even with no parameters).
- **Four equivalent ways to create a class**: File > New > Class menu, toolbar, keyboard shortcut, or the Explorer window — mirroring how project methods are created.
- **Constructors and computed properties are supported** via Class constructor(...) and Function get/Function set pairs (e.g. Length_cm as a computed unit-converted property).
- **4D ships built-in class-store classes** (documented separately from user classes) offering benefits over generic Object variables, notably around the 4D Datastore/ORDA object model.
- **Early ORDA usage patterns over-assigned explicit datastore/dataclass variables**; the note notes simplifications available once developers are comfortable with the built-in classes.
- **Code editor gains multiple class-aware features**: object-notation autocompletion, project-method detail tooltips, a code-navigation dropdown, and direct debugging of class functions.

## Featured Technology
- 4D Classes (project mode only)
- cs command (class store)
- Object notation / var declarations
- Getters/setters (Function get / Function set)
- 4D Datastore / ORDA built-in classes
- Code editor autocompletion for classes

## Best Practices Highlighted
1. Declare typed class instances (`var $x : cs.ClassName`) rather than generic objects wherever possible, to get correct-casing autocompletion and better tooling support.
2. Use getters/setters for computed properties instead of ad hoc conversion methods scattered through calling code.

## Context / Positioning
Published under 4D v19 R (July 2022), this note reflects 4D's broader multi-year push to bring true object-oriented, class-based programming to the 4D language — a feature that only became possible once project mode (introduced ~v17-18) replaced the older binary structure-file model, and one that underpins 4D's modern ORDA data-access layer.

## Historical Commentary
**Status:** current

User-defined classes are now a foundational, thoroughly current part of the 4D language — arguably more central today than in 2022, since they underpin ORDA data model classes, singleton/shared classes, worker classes, and most modern component architecture. The note's core teaching (class structure, cs, constructors, getters/setters) remains fully accurate. The only aging detail is incidental: the note itself flags C_TEXT-style compiler directives as an 'Older Deprecated Declaration' in favor of the `var $x : Type` syntax, confirming that by 2022 4D had already fully pivoted new code style toward typed variable declarations, which remains best practice today.
