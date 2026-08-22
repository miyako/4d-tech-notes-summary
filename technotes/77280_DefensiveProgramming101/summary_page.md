# Tech Note 15-08: Defensive Programming 101

**Author:** Timothy Aaron Penner, Technical Services Engineer, 4D Inc.
**Published:** April 22, 2015 | **Product/Version:** 4D v14.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77280
**Download:** https://kb.4d.com/DLTN/TN/2015/15-08_DefensiveProgramming101.pdf

## Proposition
Code that works perfectly on a developer's machine often fails for customers because of unvalidated assumptions. This note catalogs common 4D pitfalls — unchecked arrays, invalid pointers, stale references, unvalidated file paths — and demonstrates the defensive checks that prevent each failure mode.

## Key Points
- **Array bounds checking:** always call `Size of array` before indexing into an array to avoid "Indice out of range" runtime errors.
- **Character reference symbols (`[[..]]`):** flags subtle pitfalls when working with these string-position references.
- **Listbox row selections:** validate that a selection actually exists before acting on it.
- **Parameter validation:** check that parameters passed into a method are actually present/valid before use.
- **Pointer type checking:** verify a pointer's type before dereferencing it to avoid runtime errors.
- **Data vs. reference distinction:** SVG, XML, Lists, and Named Selections sections each illustrate the difference between holding actual data versus a reference/handle that may have gone stale.
- **`CLEAR NAMED SELECTION` guidance:** explains when it's required to free memory versus when a selection consumed via `USE NAMED SELECTION` needs no explicit cleanup.
- **Path validation:** use `Test path name` before passing paths to commands like `Read Picture file`, `Open Document`, `DOM Parse XML Source`, `Document to Blob`/`Document to Text`.
- **Table/field number loops:** caution against assuming looped table/field numbers correspond to valid structure elements.

## Featured Technology
- `Size of array`
- `Test path name`
- `CLEAR NAMED SELECTION` / `CUT NAMED SELECTION` / `USE NAMED SELECTION`
- Pointer type validation
- Character reference symbols (`[[..]]`)

## Best Practices Highlighted
1. Always validate array size, pointer type, and parameter presence before acting on them.
2. Use `Test path name` before any file/folder-path-consuming command to avoid runtime errors on missing paths.
3. Understand whether a variable holds live data or a reference that can become stale (SVG, XML, Lists, Named Selections) and re-validate accordingly.
4. Explicitly free named selections with `CLEAR NAMED SELECTION` when they're no longer needed and weren't already consumed via `USE NAMED SELECTION`.

## Context / Positioning
Published in the classic Design Mode era (v14.3, 2015), this note is squarely about disciplined use of 4D's traditional procedural language — arrays, pointers, named selections — well before Project Mode, ORDA, or class-based 4D existed, but its guard-check mentality applies just as well to any programming paradigm.

## Historical Commentary
**Status:** Still relevant

Every command referenced here — `Size of array`, `Test path name`, `CLEAR NAMED SELECTION`, pointer typing — remains current and unchanged in modern 4D, and the underlying defensive-programming discipline (validate before you use) applies identically to Project Mode and ORDA-based codebases. This is one of the more timeless notes of the era precisely because it teaches a mindset and checklist rather than a feature tied to a specific soon-to-be-superseded API.
