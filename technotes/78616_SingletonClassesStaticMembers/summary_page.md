# Tech Note 20-23: Implementing Singleton Classes with Static Member Functions in 4D

**Author:** Dominique Delahaye, 4D Expert, 4D SAS. (with Al Mahdi Bakkali, 4D Tech Support, 4D Morocco)
**Published:** December 29, 2020 | **Product/Version:** 4D v18 R3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78616
**Download:** https://kb.4d.com/DLTN/TN/2020/20-23_SingletonClasses.zip

## Proposition
4D v18 R3's class system did not yet have a native concept of "static" properties, so developers needed a way to instantiate a class once and share it safely across all processes. This Tech Note proposes an alternative to interprocess variables and ad hoc shared-object locking: build pseudo-static properties on top of shared collections, combined with a reference-counting scheme, to implement thread-safe singleton classes — demonstrated with a `File` class that prevents concurrent access to the same file.

## Key Points
- **Why not interprocess variables**: they don't work in a preemptive process context, ruling them out for modern 4D development.
- **Why not plain shared objects/Storage**: developers still need to manage locking manually across every process/component that touches them.
- **Pseudo-static properties**: an `Object` base class defines `has_static`/`get_static`/`remove_static` functions that lazily create a class-level property as a **Shared Object**, simulating a static member.
- **Reference counting over semaphores**: the `File` subclass implements `retain`/`release`/`owner`/`in_use`/`open` to restrict a file to one owning process at a time, deliberately choosing counting over a semaphore.
- **Concurrency safety**: all access to shared static properties is wrapped in `Use...End use` blocks.
- **Class inheritance**: `File extends Object`, reusing the constructor pattern and `_$static` property retrieved via `get_static`.
- **Validated via testing**: opening the same file from two different processes correctly fails the second `.open()` call, confirming singleton behavior.

## Featured Technology
- 4D Classes (Class Constructor, Class extends, class Function)
- Shared objects / shared collections
- Use...End use concurrency blocks
- OB Class, OB Copy, OB Remove commands
- Reference counting pattern

## Best Practices Highlighted
1. Avoid interprocess variables for cross-process shared state in preemptive/modern 4D code.
2. Wrap all shared object/collection access in `Use...End use` to guarantee thread safety.
3. Prefer reference counting over semaphores when the goal is "at most one owner" rather than strict mutual exclusion ordering.

## Context / Positioning
This note reflects the transitional period when 4D classes and OOP were newly established (introduced around v17R5–18) but still lacked some conveniences (like true static members) that OOP developers from other languages expected. 4D experts and community members were actively exploring idiomatic patterns for common OOP needs — singletons being a canonical example — using the primitives 4D provided at the time (shared collections, `Use...End use`), positioning this note as thought leadership for the emerging 4D class ecosystem.

## Historical Commentary
**Status:** Partially superseded

4D subsequently added native support for static class properties/functions directly in the language, and later versions also introduced framework-level support for shared singleton classes, which provide a more direct, built-in way to achieve what this note constructs manually via `has_static`/`get_static` and shared collections. That said, the underlying concurrency techniques — shared objects/collections, `Use...End use`, and reference counting for "single owner" semantics — remain valid, current 4D practice and are still commonly used for cases beyond simple static properties (e.g., managing exclusive access to an external resource). Developers today implementing a genuine singleton would first check 4D's native static/shared-singleton class support before building this level of custom scaffolding.
