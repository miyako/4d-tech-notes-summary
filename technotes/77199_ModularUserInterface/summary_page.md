# Tech Note 14-20: A Modular Approach to Building a User Interface

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** December 29, 2014 | **Product/Version:** 4D v14 R4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77199
**Download:** https://kb.4d.com/DLTN/TN/2014/14-20_ModularUI.zip

## Proposition
This note contrasts the traditional way of building a Tabbed Document Interface — one large form with multiple internal pages tied together by tab navigation — with a modular alternative in which each tab/page is its own independent form embedded as a subform, arguing the latter is easier to maintain, reuse, and troubleshoot, and demonstrating both the TDI and an alternative Multiple-Document-Interface layout built from the same modules.

## Key Points
- **Traditional TDI limitations:** a single form with many pages becomes harder to navigate, debug, and reuse as it grows, since all functionality is entangled in one object.
- **Modular alternative:** break the UI into one form per page/tab, each independently testable and reusable, then compose them via subforms into the parent shell.
- **Ease of design renovation:** changing one module's layout doesn't risk breaking unrelated pages, unlike editing pages within one big multi-page form.
- **Reuse across UIs:** the same page-modules used for the TDI are shown being reused to build an alternative Multiple Document Interface (MDI) layout with minimal extra work.
- **Simplified troubleshooting:** bugs are isolated to the specific module/form responsible rather than hidden inside a monolithic multi-page form.
- **Consistency benefits:** shared modules used across multiple different top-level designs enforce consistent behavior/appearance.

## Featured Technology
- Tabbed Document Interface (TDI)
- Multi-page forms vs. separate forms + subforms
- 4D's include-form/subform mechanism

## Best Practices Highlighted
1. Prefer small, single-purpose forms over one large multi-page form for maintainability.
2. Compose UI via subforms so the same module can be reused across different top-level interface designs (TDI, MDI, etc.).
3. Isolate functional concerns per module to simplify debugging.

## Context / Positioning
Published December 2014 for 4D v14 R4, in the classic Design Mode era where forms lived as binary objects inside the structure file. The modularity argument here anticipates, in spirit, the philosophy that Project Mode (v17+, 2018) later enforced structurally by making every form its own separate file on disk.

## Historical Commentary
**Status:** Still Relevant

The core software-engineering advice — decompose a large UI into small, independently maintainable, reusable modules — has aged well and is arguably even more relevant now that Project Mode makes each form a distinct file that benefits from being small and single-purpose for clean Git history and merges.

The specific UI-building mechanics (Tab Control-driven multi-page vs. subform composition) still work today essentially unchanged, so this note is not obsolete, just dated in presentation — a modern rewrite would likely also mention using 4D classes to encapsulate each module's behavior rather than relying solely on form methods.
