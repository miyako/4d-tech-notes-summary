# Tech Note 14-03: Database Normalization

**Author:** Timothy Tse, Technical Services Team Member, 4D Inc.
**Published:** February 20, 2014 | **Product/Version:** 4D v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76966
**Download:** https://kb.4d.com/DLTN/TN/2014/14-03_DatabaseNormalization.pdf

## Proposition
This note teaches the foundational relational-database design discipline of normalization — organizing data through primary keys, relationships, and the first three normal forms — to reduce redundancy and improve maintainability, illustrated with a worked example.

## Key Points
- Weighs normalization's pros (efficient organization, eliminated redundancy, enforced data dependencies, flexibility, easier maintenance) against its cons (harder form display, more upfront design work, potential need to rebuild existing structures).
- Establishes the two prerequisites for any relational design: unique/immutable/non-null **primary keys**, and 4D's native **one-to-many relationships** between parent and child tables.
- **1NF:** eliminate repeating groups by moving related/repeating data into its own table with its own primary key.
- **2NF:** ensure every non-key column depends on the *entire* primary key (satisfies 1NF plus full functional dependency).
- **3NF:** eliminate transitive dependencies, where a non-key column depends on another non-key column rather than directly on the key.
- A worked example progressively normalizes an un-normalized Students table (with Degree/Major/Address/City/State all in one row) through 1NF, 2NF, and 3NF, quantifying redundancy removed at each stage.
- Concludes that normalization isn't always warranted for small/stable applications — normalize first, then de-normalize selectively as needed.

## Featured Technology
- Relational database normalization theory (1NF/2NF/3NF)
- Primary keys and 4D one-to-many relationships
- Transitive dependency analysis

## Best Practices Highlighted
1. Normalize a schema first, then de-normalize deliberately only where performance or simplicity clearly justifies it.
2. Use primary keys that are unique, non-null, and stable over the life of the record.
3. Watch specifically for transitive dependencies (non-key columns depending on other non-key columns) when reaching for 3NF.

## Context/Positioning
Published as an educational, technology-agnostic primer for 4D developers, this note aimed to strengthen database design fundamentals rather than showcase a new 4D feature.

## Historical Commentary
**Status:** Current

Database normalization is foundational relational-database theory rooted in mathematics and set theory, and it has not changed in the decades since (and well before) this note was published. The 4D-specific framing — one-to-many relations as 4D's native relationship type — reflects the classic-language relational model of the era, which 4D's later ORDA layer built entity-based, dot-notation data access on top of, but the underlying normalization principles apply identically whether data is queried via classic relations or accessed as ORDA entities. This is a rare example in this era's Tech Notes of content that remains genuinely current rather than superseded by later product changes.
