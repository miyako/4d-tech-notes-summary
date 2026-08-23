# Tech Note: Relations for Beginners in 4D

- **Asset ID:** 25596
- **Tech Note #:** 02-55
- **Published:** November 30, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Gou Yang
- **Page URL:** https://kb.4d.com/assetid=25596
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_51-55_(NOV)/02-55_RelationsForBeginners.hqx

## Overview

Gou Yang, a 4D Inc. Technical Support Engineer, introduces 4D relations to beginners using a hypothetical movie-ticket-sales database ([Movie], [Tickets], [Cashier]) to explain why relations reduce insertion/deletion anomalies and redundant data entry. The note covers creating an automatic many-to-one/one-to-many relation by drawing a relation line between key fields, the meaning of each relation-property checkbox (Auto relate one, Auto wildcard support, Prompt if related one does not exist, Auto one to many, Auto assign related value in subform), and database-property settings like Mandatory Log File, Allow Deletion Control, and Automatic Transaction during Data Entry. It then shows how to reimplement each automatic behavior manually with RELATE ONE, RELATE MANY, and a deletion-control trigger, and finally extends the pattern to many-to-many relations via a joining table, plus RELATE ONE SELECTION/RELATE MANY SELECTION for relating whole selections at once.

## Key Points

- Explains automatic many-to-one/one-to-many relation setup: drag from `[Tickets]MovieID` to `[Movie]MovieID`, then configure Many-to-One options (Auto relate one, Auto wildcard support, Prompt if related one does not exist) and One-to-Many options (Auto one to many, Auto assign related value in subform) in the relation properties dialog.
- Covers key database property checkboxes that interact with relations: Mandatory Log File, Allow Deletion Control, Automatic Transaction during Data Entry, and 'Consider @ as a character for Query and Order By'.
- Shows manual (non-automatic) many-to-one relation code: `RELATE ONE([Tickets3]CashierID)` on `On Load`, and a manual 'prompt if related one does not exist' routine that queries `[Cashier3]`, offers to create a new cashier record via `CREATE SET`/`CREATE EMPTY SET`/`USE SET`, then calls `RELATE ONE` again.
- Shows manual one-to-many relation code triggered `On Clicked` of a tab control (`RELATE MANY([Movie3]MovieID)`), and manually assigning the related key on `On Load` to simulate 'Auto assign related value in subform' (`[Tickets3]MovieID:=[Movie3]MovieID`).
- Implements manual Deletion Control via an `On Deleting Record Event` trigger that calls `RELATE MANY` and returns error code `-16002` if related child records still exist, blocking deletion of the parent.
- Extends the pattern to many-to-many relations using a joining table ([Tickets2] linking [Movie2] and [Cashier2]), and introduces `AUTOMATIC RELATIONS(bool;bool)` to toggle automatic many-to-one/one-to-many behavior at runtime, plus `RELATE ONE SELECTION`/`RELATE MANY SELECTION` to relate an entire current selection (e.g., showing all movies with a $5 ticket, or all tickets for R-rated movies) in one call.

## Featured Technology

- AUTOMATIC RELATIONS command
- RELATE ONE / RELATE MANY
- RELATE ONE SELECTION / RELATE MANY SELECTION
- Automatic vs. manual many-to-one and one-to-many relations
- Many-to-many joining tables
- Deletion Control triggers

## Historical Commentary

**Status:** superseded

Gou Yang (4D Inc. Technical Support) walks a beginner through a movie-theater/ticket-sales example database to explain automatic vs. manual relations, one-to-many and many-to-many joins, and the specific relation-property checkboxes (Auto relate one, Auto wildcard support, Auto one to many, Auto assign related value in subform) alongside the manual equivalents implemented with RELATE ONE/RELATE MANY in form and trigger events. The relational modeling concepts (avoiding insertion/deletion anomalies, joining tables for many-to-many) remain foundational and entirely valid in current 4D. However, ORDA (introduced in 4D v17+) has since provided a higher-level, object/entity-based way to navigate relationships that largely supersedes hand-written RELATE ONE/RELATE MANY calls for new development, even though the classic relation commands and structure-level relations described here still work.

References to newer/updated information:
- ORDA (introduced in 4D v17+) provides an object-based way to navigate relationships between entities, superseding the classic RELATE ONE/RELATE MANY-based approach for most new development
- The classic AUTOMATIC RELATIONS, RELATE ONE, RELATE MANY, RELATE ONE SELECTION, and RELATE MANY SELECTION commands described in this note remain part of 4D's language today for structure-level relations
