# Tech Note 26-07: Modular Sort Interface for 4D (ORDA and Classic Mode)

**Author:** Olivier Marolleau, Quality Support Engineer, 4D France
**Published:** July 29, 2026 | **Product/Version:** 4D v21 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=80064
**Download:** https://kb.4d.com/TN/2026/26-07_ModularSortInterface.zip

## Proposition
ORDA's arrival changed how data is manipulated in 4D, but it left a gap: unlike classic selections,
which have always had the simple `ORDER BY`/`TRI` command, ORDA entity selections have no native
editor for building complex, multi-criteria sorts dynamically. This note presents a reusable,
no-code graphical sort editor that fills that gap for both data-access modes at once.

## Key Points
- **Modular composition.** A sort criterion is built from three categories of drag-and-drop
  modules — table, field, and sort direction — that the user assembles in a composition area
  rather than writing code.
- **Real-time structural validation.** Positioning constraints (e.g. a field module cannot follow
  another field module without an intervening table context; a direction can only follow a valid
  field) make it impossible to compose an invalid sort.
- **Single entry point, dual data modes.** Opening the editor is identical either way; only the
  argument to `orderBy()` differs — a pointer to a table in classic mode (`cs.Lib_Mod2.me.orderBy
  (Current form's table)`, driving the `TRI` command) versus a reference plus path string to an
  ORDA entity selection (`cs.Lib_Mod2.me.orderBy(Form.dataExplore.exSelection;
  "Form.dataExplore.exSelection")`).
- **Definition/execution separation.** The sort is defined as a modular structure, serialized to a
  platform-independent `.4od` file, and only later interpreted/executed against whichever selection
  type is current — improving portability and reuse.
- **Central hub class.** `Lib_Mod2` centralizes all business logic; the HTML/JS interface contains
  almost no logic of its own, limited to querying the hub, displaying responses, and forwarding
  user actions over the `$4d` bridge (JSON-serialized both ways).
- **Contextual search/filtering.** Each module category (table/field/direction) has its own
  dynamic search field, and selecting a table auto-filters the field list to that table's fields,
  reducing steps needed to build a criterion.
- **Custom web-side i18n.** Because native 4D XLIFF localization doesn't reach an embedded Web
  Area, the interface uses a separate i18n JavaScript library keyed by `data-i18n` attributes,
  auto-detecting the browser language.
- **Session persistence via `EXECUTE FORM`.** Reapplying a sort to the original calling context
  (window/process) uses `EXECUTE FORM` to reactivate and resynchronize the source form's display.

## Featured Technology
- **ORDA** — entity selections as a first-class dynamic sort target, with no native multi-criteria
  editor of their own.
- **`TRI` (ORDER BY) command** — underlying classic-selection sort execution.
- **4D Classes (`Lib_Mod2`)** — central business-logic hub coordinating UI and engine.
- **Web Area + `$4d` bridge** — HTML/JavaScript rendering layer communicating with 4D via
  serialized JSON.
- **i18n JavaScript library** — web-side localization independent of 4D's XLIFF mechanism.
- **`.4od` file format** — portable, reusable serialized sort-plan storage.

## Best Practices Highlighted
1. *Separate UI from business logic* — keep the web interface presentation-only and route all
   logic through a single hub class.
2. *Validate structurally as the user builds* — enforce module-ordering rules live rather than
   after the fact, to prevent invalid sort definitions.
3. *Serialize configuration, not just execute it* — persisting sorts as portable files enables
   reuse/sharing rather than one-off, code-bound sorts.

## Context / Positioning
Published for 4D v21 (2026), this note addresses a still-open usability gap from 4D's multi-year
ORDA transition: giving ORDA-based, object-mode applications the same dynamic, no-code sorting
convenience developers historically had with classic selections and `TRI`, while also
future-proofing the design (calculated criteria, relation-based fields) for further ORDA
modernization.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
