# Tech Note: DataGrid's Enterprise Data Module - Beta 1

## Overview
- **Technical Note 00-34**
- **Author:** Sebastian Frey, Sextant Technologies, Inc.
- **Published:** July 1, 2000
- **Product/Version:** 4D v6.5
- **Platform:** Mac & Win
- **Content source:** Full PDF text recovered

## Key Points
This Tech Note is the third in Sebastian Frey's series documenting DataGrid Beta 1, and it is the architectural centerpiece of the whole series: it explains the Enterprise Data Module (EDM), the core module underlying the entire DataGrid application (which itself is built from several modules, including APP, GRD, and CAL for its spreadsheet functionality). The note introduces two foundational EDM concepts: the data model, a representation of a database table or view (its name, columns, and column attributes) created at design time via 4th Dimension forms, and the query, a runtime representation of a selection of a model's rows on a server, always dependent on an existing model. Because 4D's classic language of that era lacked true object-oriented constructs, EDM simulates model and query 'objects' using arrays plus a set of accessor methods (such as EDM_ModelInt, EDM_ModelText, and EDM_QueryInteger) that both simplify working with the array-based data and hide the underlying array implementation so it could later be swapped out. The featured technology is this accessor-method, pseudo-object-oriented architecture pattern as applied to database model/query abstractions, an instructive example of how developers approximated OOP patterns in a language that didn't natively support them.

## Featured Technology
- DataGrid Enterprise Data Module (EDM)
- Model and Query conceptual objects
- Accessor method array pattern

## Historical Context
This note is the core architectural entry in Sextant Technologies' DataGrid series, explaining the Enterprise Data Module's foundational 'Model' and 'Query' conceptual objects and the accessor-method pattern used to simulate object-oriented behavior over array-based storage in classic 4D. DataGrid, the third-party application this describes, is long defunct, and 4D's own language has since gained genuine object/class support, making this array-based object-simulation technique an interesting historical artifact rather than a pattern developers would reach for today.

## What's Changed Since
- DataGrid, the Sextant Technologies application whose architecture this note documents, is a long-discontinued third-party product
- 4D's language has since gained native object/class support, reducing the need for the array-based 'accessor method' object-simulation pattern described here

