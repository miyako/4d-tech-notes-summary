# Tech Note 18-12: SQL to ORDA

**Author:** Kristopher Merolla, Technical Services Engineer, 4D Inc.
**Published:** June 28, 2018 | **Product/Version:** 4D v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78085
**Download:** https://kb.4d.com/DLTN/TN/2018/18-12_SQL_to_ORDA.zip

## Proposition
Introduces ORDA (Object Relational Data Access), 4D v17's new dot-notation data access layer, by translating each of the four CRUD operations from classic embedded SQL into equivalent ORDA code. Positions ORDA as a third, thread-safe alternative to SQL and native QUERY-style commands.

## Key Points
- **Datastore, Dataclass, Entity Selection, Entity:** defines the four core ORDA concepts — `ds` as the datastore interface, dataclasses mapping to tables, entity selections as record collections, and entities as single rows.
- **Member functions drive ORDA:** functions like `orderBy()` on entity selections illustrate how behavior differs by object type (entity selections vs. single entities).
- **CRUD comparison:** shows `INSERT INTO ... VALUES` vs. `ds.People.new()` + field assignment + `.save()` for record creation, with similar side-by-side treatment for Read, Update, and Delete.
- **Thread safety is the headline differentiator:** the note explicitly states ORDA is thread-safe while SQL statements are not.
- **Locking model:** optimistic locking (timestamp-based) is the default; pessimistic locking is available via `lock()`/`unlock()` member functions on entities.
- **Save status checking:** `$person.save()` returns a status object used to confirm whether the save succeeded.
- **Sample application:** ships with a test structure ([People], [Job], [Company], [State]) and dedicated Create/Read/Update/Delete test forms with timing comparisons.
- **Indexing still matters:** the note reminds developers to index relation fields for performance regardless of which data-access technique is used.

## Featured Technology
- ORDA (`ds`, dataclasses, entity selections, entities)
- 4D embedded SQL (`Begin SQL`/`End SQL`)
- Optimistic/pessimistic locking (`lock()`, `unlock()`)

## Best Practices Highlighted
1. Always call `.save()` after `.new()` or field edits — otherwise changes remain memory-only.
2. Index relation fields (many-to-one/one-to-many) for performance at scale.
3. Check the status object returned from `save()` to detect update conflicts.

## Context / Positioning
Published mere weeks after 4D v17 introduced ORDA, this note reflects 4D's earliest public messaging around the new API — presented cautiously as a "third way" alongside SQL and classic commands rather than the primary recommended approach it would later become. This is squarely classic 4D-era material: no mention of REST datastores, computed attributes, or Qodly, and the sample app still uses a traditional binary structure with [Table] bracket notation.

## Historical Commentary
**Status:** Partially superseded

The core ORDA concepts explained here — Datastore, Dataclass, Entity Selection, Entity, and basic CRUD via `new()`/`save()`/`lock()` — are still accurate and form the bedrock of ORDA today, so this note remains a reasonable introduction to the basics. However, ORDA itself evolved substantially after v17: later versions added computed/alias/related attributes, dataclass and entity class functions (user-defined business logic in classes), remote datastore access over REST, and tighter integration with 4D's collection and class systems — none of which existed yet when this note was written.

The broader positioning has also shifted: in 2018 ORDA was pitched as an equally-weighted alternative to SQL for developers to "choose"; today 4D actively recommends ORDA (paired with classes) as the default, forward-looking data layer, while classic SQL and QUERY commands are maintained mainly for backward compatibility with older code. A developer reading this note today would learn correct fundamentals but should look at more recent documentation for the class-based/computed-attribute patterns considered best practice now.
