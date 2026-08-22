# Tech Note 10-26: Using External Databases for Speed, Simplicity and Security

**Author:** Charles “Charlie” Vass, Technical Services Team Member, 4D Inc.
**Published:** August 26, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76164
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_24-28_(AUG)/10-26_External_DB.zip

## Proposition
Charles Vass's Tech Note explores 4D v12's two new SQL commands, CREATE DATABASE and USE DATABASE, which let developers programmatically create and switch to external 4D databases for data segregation.

## Key Points
- CREATE DATABASE and USE DATABASE are new 4D v12 SQL commands for managing external databases
- Demonstrates a full archiving workflow: structure copy, record migration, archive read-back
- Introduces the 'Database Sandbox' pattern for per-user/per-test-runner data isolation
- Covers segregated vs. single data file storage tradeoffs
- Includes a demo with WebAccount component changes showing the pattern applied in practice

## Featured Technology
- CREATE DATABASE SQL command
- USE DATABASE SQL command
- data segregation/archiving
- Database Sandbox pattern

## Best Practices Highlighted
- Match structure exactly between host and external archive tables before migrating records
- Choose a sandbox variation (dedicated DB, schema-per-runner, partitioning) based on isolation needs vs. overhead

## Context/Positioning
Published as 4D v12 added native SQL commands for external database management, giving developers a code-driven alternative to manual multi-database architectures for archiving, security, and performance.

## Historical Commentary
**Status:** Still Relevant

This note demonstrates 4D v12's CREATE DATABASE/USE DATABASE SQL commands for splitting data across external databases (archiving, sandboxing, per-test-runner databases), a classic-language SQL data-segregation technique that still functions in current 4D. The pattern is still valid as a fallback, though ORDA's ability to work with multiple datastores/entity selections and 4D's modern multi-base architecture give developers more structured, entity-oriented alternatives for many of the same data-segregation goals today.
