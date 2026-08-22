# Tech Note 14-13: [3rd Party Tech Note] A Practical Approach To Record Locking and Data Entry

**Author:** Dave Terry, Pacific Data Management, Inc.
**Published:** August 1, 2014 | **Product/Version:** 4D v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77113
**Download:** https://kb.4d.com/DLTN/TN/2014/14-13_RecordLockingDataEntry.zip

## Proposition
Contributed by a partner developer (Dave Terry, Pacific Data Management), this note explains the tradeoffs between 4D's default pessimistic record locking (a record is locked from the moment it's loaded read-write until released) and the optimistic locking pattern common in more loosely-coupled database systems (compare a version/timestamp column at save time), then proposes a practical hybrid technique and example code to give users a friendlier data-entry experience within 4D's pessimistic model.

## Key Points
- **Pessimistic locking basics:** a record becomes locked as soon as it's the current record in a read-write table, and stays locked until released or reloaded, preventing others from saving changes.
- **Hidden locking risk:** related-table records can become locked as a side effect of operations even when not directly displayed in a data-entry form, requiring careful state management.
- **Read-only mitigation:** 4D provides a table read-only mode so newly loaded records aren't locked when write access isn't needed.
- **Optimistic locking explained:** a version/timestamp column is compared at save time to detect conflicting edits, common in less tightly-coupled client-server systems.
- **Hybrid approach proposed:** combines aspects of both models to reduce the UX friction of full pessimistic locking while preserving 4D's built-in consistency guarantees.
- **Example code provided** implementing the hybrid technique end to end.

## Featured Technology
- 4D pessimistic record locking
- Optimistic locking pattern (version/timestamp column comparison)
- Hybrid locking strategy for data entry UX

## Context / Positioning
Published August 2014 for 4D v14.0, this is a third-party (partner-authored) contribution from the classic Design Mode era, addressing a perennial multi-user database UX problem well before ORDA introduced native optimistic entity locking as a built-in alternative.

## Historical Commentary
**Status:** Partially Superseded

The problem this note addresses — pessimistic locking's UX friction for concurrent data entry — was significant enough that 4D itself later built native optimistic locking directly into ORDA's entity model (conflict detection on `.save()`), which largely obviates the need for the kind of hand-built hybrid workaround described here for new, ORDA-based projects.

For classic-form, non-ORDA 4D applications (which still exist in production), the pessimistic/optimistic tradeoff and hybrid technique described remain practically relevant, so this note sits in a middle ground: conceptually sound and still applicable to legacy codebases, but architecturally superseded for anyone building on 4D's modern data layer.
