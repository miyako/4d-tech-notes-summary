# Upgrades with User Created Tables

## Overview
This note tackles a practical deployment problem: preparing a 4D application to allow end users to create their own custom tables, and then safely upgrading that application to a new developer-built version without breaking or losing the user-created tables. Two sample databases are provided — one representing the developer's finished new version, the other representing an end user's modified copy with extra user-created tables — to walk through the more complex upgrade/merge process this scenario requires.

## Key Points
- Published January 17, 2008 as Technical Note 08-02.
- Targets 4D Developer v11 on Mac & Win.
- Author: Thomas Fitch, Technical Support Engineer, 4D Inc..

## Featured Technology
- 4D structure/database upgrade process
- User-extensible table schemas
- Structure merging across versions

## Historical Context
Handling structural upgrades when end users have extended a database's schema is a durable, still-relevant challenge for 4D developers; the specific binary-structure-file upgrade mechanics described here reflect the pre-Project-Mode era, and today's equivalent scenarios are also shaped by ORDA's more flexible, code-first data model.

**Status:** still relevant

**Related updates:**
- Project Mode (introduced 4D v17, 2018) changed how structure changes are tracked and merged, offering git-friendly diffs that make some aspects of this upgrade problem easier than in the binary Design Mode era described here
