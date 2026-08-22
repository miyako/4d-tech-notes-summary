# Tech Note 22-02: Computed Attributes in 4D

**Author:** Tai Bui, Technical Services Engineer, 4D Inc.
**Published:** January 24, 2022 | **Product/Version:** 4D v19 R3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78859
**Download:** https://kb.4d.com/DLTN/TN/2022/22-02_ComputedAttributes.zip

## Proposition
4D introduced computed attributes to let developers expose calculated, derived values as ORDA entity attributes (not stored fields), fully queryable and sortable; this note explains the ORDA/classes background needed to use them and how to implement get/set/query/orderBy functions for them.

## Key Points
- **ORDA background**: object-notation datastore access (`ds.Table.all()`, entity selections) contrasted with the classic current-selection/array-based method.
- **Classes background**: introduced in v18R3, project-mode only, created/managed like project methods with a dedicated Classes section in the Explorer.
- **Computed attributes**: defined by extending a table's entity class ({TableName}Entity) and writing `Function get {name}()`.
- **Setters**: `Function set {name}(value)` defines what happens when a computed attribute is assigned a value.
- **Query support**: `Function query {name}(input)` translates a query on the computed attribute into a real query string + parameters.
- **Sort support**: `Function orderBy {name}(input)` translates asc/desc sort requests on the computed attribute into a real sort string.
- **Returning related entities/selections**: computed attributes can return typed entities/entity selections via {Table}Entity/{Table}Selection extended classes.
- **Performance note**: indexing the real underlying fields improves query/sort performance for computed attributes based on them.

## Featured Technology
- ORDA (Object Relational Data Access)
- 4D Classes (Class extends Entity/EntitySelection)
- Computed attributes (get/set/query/orderBy functions)
- Datastore / Entity / EntitySelection classes

## Best Practices Highlighted
1. Name entity/selection extension classes exactly as {TableName}Entity / {TableName}Selection so 4D auto-recognizes and wires the extension.
2. Define query/orderBy functions whenever a computed attribute needs to participate in .query()/.orderBy() calls, not just simple .get() reads.
3. Index the real fields that back a computed attribute to keep queries/sorts on it performant.

## Context / Positioning
This note is a core piece of 4D's ORDA/classes documentation push circa 2022, cementing computed attributes as a first-class ORDA feature and reinforcing project mode + classes as the required foundation for the platform's modern data-access model.

## Historical Commentary
**Status:** Current

This remains one of the most durable and current notes in the batch: ORDA, classes, and computed attributes are all still central, unchanged pillars of modern 4D development, and the get/set/query/orderBy pattern described here matches 4D's current official documentation almost verbatim. There is no deprecation or superseding feature to note — this is essential reading for any 4D developer using ORDA today, not merely historical context.
