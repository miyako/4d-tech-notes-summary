# Tech Note 23-14: Exploring 4D ORDA Classes and Class Functions

**Author:** MOUSTARIH Anouar, Technical Services Engineer, 4D Morocco
**Published:** August 24, 2023 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79266
**Download:** https://kb.4d.com/DLTN/TN/2023/23-14_ExploringORDAClasses.zip

## Proposition
Business applications built around forms often need the same data queries and per-record computations repeated in multiple places, which hurts maintainability. This note shows how to encapsulate that logic directly inside 4D's ORDA-generated Dataclass and Entity classes as named functions, aligning form-driven development with modern object-oriented practices.

## Key Points
- **ORDA class family:** Datastore (database connection), Dataclass (maps to a table and its relationships), Entity (a single record), and Entity Selection (a group of records) form the foundation of ORDA's object model.
- **Auto-generated classes since v20:** Every project table automatically gets a corresponding Dataclass class (e.g., "Contact") and Entity class ("ContactEntity") that developers can extend with custom functions (available since v18R5, automatic in v20).
- **Dataclass query functions:** Functions like `getAllMales`, `getContactsFromUSA`, and `searchByName($searchText)` each wrap a parameterized `ds.Contact.query("attribute = :1"; value)` call, returning a typed `4D.EntitySelection` — centralizing common queries as named, reusable methods.
- **Boolean/status-based queries:** `getActiveContact` demonstrates querying on a boolean-like attribute (`isActive = :1`, "true"), showing the same query pattern extends to any indexed attribute.
- **Entity-level computed properties:** `Class extends Entity` functions like `getFullName` (concatenating and uppercasing name parts) and `getLastConnectionDate` (casting a stored value to `Date`) show how to derive presentation-ready values from raw entity attributes accessed via `This`.
- **Country-aware formatting logic:** `getFormattedAddress` uses a `Case of` on `This.countryCode` to assemble differently-ordered address strings for US, French, and other addresses from nested `This.address.street.*` properties — demonstrating conditional business logic embedded in entity methods.
- **Parameterized queries over string concatenation:** All dataclass query functions use the `:1` placeholder syntax rather than building query strings by concatenation, a safer and clearer querying pattern.

## Featured Technology
- **ORDA (Datastore/Dataclass/Entity/EntitySelection):** 4D's object-relational data access model, the core subject of the note.
- **Class extends DataClass / Class extends Entity:** Class inheritance syntax used to attach custom behavior to auto-generated ORDA classes.
- **ds.<Table>.query():** Parameterized query method returning an `4D.EntitySelection`.
- **This:** Entity-context reference used inside Entity class functions to access the current record's attributes.

## Best Practices Highlighted
1. Encapsulate common or repeated queries as named Dataclass functions rather than duplicating `ds.<Table>.query(...)` calls throughout the application.
2. Use parameterized query placeholders (`:1`) instead of manual string concatenation for clarity and safety.
3. Push per-record derived/formatted values (full names, formatted dates, localized addresses) into Entity class functions so presentation logic lives alongside the data model rather than scattered across forms.

## Context / Positioning
Published as ORDA class extension became a first-class, automatically available feature in 4D v20, this note serves as an onboarding example for developers transitioning from classic table/field-based coding toward ORDA's object-oriented data model, reinforcing 4D's broader strategic direction toward class-based, object/collection-driven application architecture.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
