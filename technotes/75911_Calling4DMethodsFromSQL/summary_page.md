# Tech Note 09-37: Calling 4D Methods From SQL Statements

**Author:** Atanas Atanassov, Technical Services Team Member, 4D Inc.
**Published:** September 17, 2009 | **Product/Version:** 4D 11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75911
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_36-39_(SEP)/09-37_calling4DMethodsFromSQL.zip

## Proposition
This Tech Note shows how 4D v11 SQL lets developers call existing 4D project methods as scalar functions directly from within SQL statements, so SQL queries can leverage proven 4D code (including complex relational logic) without rewriting it or hand-building joins.

## Key Points
- Only project methods can be called from SQL, and each must have "Available through SQL" enabled in its properties (unchecked by default, for security) or the SQL call fails.
- Syntax: `{fn method_name(params) AS TYPE}` inside SELECT or WHERE clauses — `fn` marks it as callable, and `AS` declares the SQL return type, which must match the method's actual `$0` return type or the array fills with nulls.
- Because SELECT invokes the method once per scanned record, omitting a matching WHERE-clause filter produces a results array sized to the full record count (with 0/empty entries for non-matches) rather than only the matching rows.
- Parameter passing differs from standard 4D syntax: SQL uses commas (not semicolons) between arguments, and 4D variables must be prefixed with a colon (`:$var`) or wrapped in `<<$var>>`.
- Four equivalent implementations of the same "count invoices per customer" example are demonstrated: inline Begin/End SQL, dynamically built EXECUTE IMMEDIATE, SQL EXECUTE with SQL LOGIN/SQL LOAD RECORD/SQL LOGOUT, and QUERY BY SQL combined with a manual For loop.
- Variable and method names are limited to 32 characters in this context.

## Featured Technology
- 4D v11 SQL engine (Begin SQL/End SQL)
- EXECUTE IMMEDIATE
- SQL EXECUTE / SQL LOGIN / SQL LOAD RECORD / SQL LOGOUT
- QUERY BY SQL
- "Available through SQL" project method property

## Best Practices Highlighted
1. Always match the SQL `AS` return type to the method's actual return type to avoid silent null-filled results.
2. Include the method call in the WHERE clause (not just SELECT) when you want a results array limited to matching records only.
3. Use the `<<varname>>` bracket notation as an alternative to `:varname` colon-prefixing for clarity when passing 4D variables into SQL.

## Context / Positioning
Published shortly after 4D v11 introduced its embedded SQL engine, this note showcased a way to bridge two developer audiences — those fluent in 4D's procedural language and those more comfortable with SQL — by letting either reuse the other's logic without a rewrite.

## Historical Commentary
**Status:** Still Relevant

The `{fn ... AS TYPE}` bridging technique and the SQL execution commands described (Begin/End SQL, EXECUTE IMMEDIATE, SQL EXECUTE, QUERY BY SQL) remain part of 4D's classic language today and continue to function as documented, so this note is still largely usable as a reference.

The main shift since 2009 is architectural rather than technical: ORDA (4D v16 R5+, 2017) introduced an entity/object-based data access model that many developers now prefer for cross-table queries instead of hybrid SQL-plus-method approaches, though the classic SQL engine itself has only matured and remains fully supported for cases where this pattern is still the best fit.
