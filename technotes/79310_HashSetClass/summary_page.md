# Tech Note 23-18: Hash-Based Set Class Component

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** October 30, 2023 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79310
**Download:** https://kb.4d.com/DLTN/TN/2023/23-18_HashSetClass.zip

## Proposition
Programs frequently need to track a collection of distinct values efficiently — checking membership, adding, and removing without duplicates — a job for which arrays (O(n) lookup) are poorly suited. This note builds a proper hash-based Set data structure as a native 4D class, packaged as a reusable component, while also illustrating several modern 4D class-authoring techniques along the way.

## Key Points
- **Hash table via object literal:** Set elements are stored as object property names (each valued `True`), giving O(1) average add/has/delete versus O(log n) for tree-based sets or O(n) for array scans.
- **Dual internal subsets:** Because object keys must be text, the class keeps separate `_strSet` and `_numSet` objects internally so text `"36"` and number `36` can both be tracked as distinct set members.
- **Correct type dispatch:** Functions use `Value type()` rather than `Type()` to branch on an input's actual internal type (text vs. number) rather than its declared `Variant` type.
- **Hidden internal properties:** Prefixing `_strSet`/`_numSet` with underscores hides them from code completion, keeping the class's public surface limited to `size`, `add`, `has`, `delete`, `clear`, and `collection`.
- **Chainable API:** `add`, `delete`, and `clear` all `return This` (typed `cs.Set`), enabling fluent chains like `Set.delete(x).add(y).clear().add(z)`.
- **Constructor flexibility:** `cs.Set.new()` yields an empty set; `cs.Set.new($collection)` seeds the set with a collection's distinct values by delegating to `add`.
- **Set algebra on top of the class:** `getUnion`, `getDifference`, and `getIntersection` are implemented as simple project methods composing `collection()`, `add()`, `delete()`, and `has()`; the shipped component adds `getSymmetricDifference` and `isSuperSet`.
- **Component packaging:** A dedicated namespace ("Hash") is declared in database settings so the class is referenced as `cs.Hash.Set`, avoiding collisions with other components' classes, with syntax-file generation enabled for consumer code completion.

## Featured Technology
- **4D Classes (`cs.Set`):** The core language feature used to encapsulate the set's state and behavior.
- **Object literals (`{}`) as hash tables:** Native 4D object syntax repurposed as a constant-time lookup structure.
- **Collection literals (`[]`) and `.push()`:** Used to build the return value of `collection()`.
- **OB REMOVE:** Removes a property (set element) from the internal hash objects in `delete()`.
- **Value type command:** Distinguishes real internal value types for correct dispatch, as opposed to the declared `Variant` type.
- **Component namespaces:** Prevents class name collisions when the Set class is distributed as an installable component.

## Best Practices Highlighted
1. Use `Value type()` instead of `Type()` when a parameter is typed as `Variant` and its actual runtime type must be inspected.
2. Prefix internal/implementation-only class properties with an underscore to hide them from code completion and keep the public API clean.
3. Return `This` from mutating methods to support fluent, chainable call sequences.
4. Declare a dedicated namespace for component classes to avoid naming collisions with other installed components, and enable syntax-file generation for consumer tooling support.

## Context / Positioning
This note serves as both a practical utility (a reusable Set class) and a broader tutorial on modern 4D class-authoring idioms — chainable methods, hidden properties, object/collection literals, and component namespacing — reflecting 4D's continued push toward classes and object/collection-oriented programming as the idiomatic style for v20-era development.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
