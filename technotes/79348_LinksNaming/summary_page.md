# Tech Note 23-23: Links Naming

**Author:** Abdelhafid Elhour, PS 4D and PS Web/mobile manager, 4D Morocco
**Published:** December 27, 2023 | **Product/Version:** 4D v20 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79348
**Download:** https://kb.4d.com/DLTN/TN/2023/23-22_LinksNaming.pdf

## Proposition
Many long-lived 4D databases carry link names left at their unused defaults ("Lien_55", "Link_78_retour", etc.), which was harmless before ORDA but becomes a maintainability and readability problem once ORDA exposes those link attributes directly as entity properties in code. This note establishes a clear, consistent naming convention for tables, fields, and especially links, and shows how to find and fix bad names at scale.

## Key Points
- **Historical default names:** Undefined links inherited generic, localized default names ("Lien_@", "Link_@", "Verknüpfung_@") that were rarely renamed because they had little practical use until ORDA.
- **Inventory script:** A `For each` scan over `ds` dataclasses and attributes flags `relatedEntity`-kind attributes whose `.name`/`.inverseName` still match default patterns, tallying correct vs. incorrect links and listing affected tables via the pasteboard.
- **Table naming rule:** Name tables in the singular with a capital letter (e.g., "Company"), since a table represents the schema of one record, not a collection of records.
- **Field naming rule:** Use lower-case for fields, except primary keys such as ID/UUID.
- **Link naming rule (N-to-1):** Name the many-to-one link singular and lower-case (e.g., an Employee entity's "company"), matching the one-associated-entity semantics and staying consistent with field naming.
- **Link naming rule (1-to-N):** Name the one-to-many return link plural and lower-case (e.g., a Company entity's "employees"), reflecting the multiple-entities semantics.
- **Avoid directional link names:** Names like "Company_to_Employee" make code more verbose and redundant (`$company.Company_to_Employee` vs. the cleaner `$company.employees`) without adding real clarity.
- **Bulk renaming via catalog.4DCatalog:** In project mode, the `name_Nto1`/`name_1toN` attributes inside `<relation>` XML elements in `Project/Sources/catalog.4DCatalog` can be edited directly and take effect after restarting the project, avoiding slow one-by-one renames in the structure editor.

## Featured Technology
- **ORDA relatedEntity attributes:** The underlying mechanism exposing links as named entity properties in code.
- **ds (datastore) introspection:** Used to enumerate dataclasses and attributes programmatically for the inventory script.
- **Collection.distinct()/.join():** Used to deduplicate and format the list of affected tables for reporting.
- **catalog.4DCatalog (project mode XML):** Direct-edit target for renaming many links at once without the structure editor UI.

## Best Practices Highlighted
1. Name tables in the singular, capitalized, to reflect that a table is a record schema.
2. Name N-to-1 links in the singular and 1-to-N links in the plural, both lower-case, to mirror how they read through ORDA entities.
3. Avoid encoding table names or direction into link names; let the conceptual role of each end of the relationship drive the name instead.
4. Run an automated inventory of default-named links before doing a global rename, and use the catalog.4DCatalog XML file for efficient bulk edits in project-mode databases.

## Context / Positioning
This note reflects 4D's ongoing push toward ORDA-first development, where naming conventions that were cosmetic in classic 4D coding now directly affect the ergonomics and readability of ORDA entity-based code. It fits alongside other 4D guidance encouraging developers modernizing legacy databases to clean up structural metadata (table/field/link names) as part of adopting ORDA and project mode.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
