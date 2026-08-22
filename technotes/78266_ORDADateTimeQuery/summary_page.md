# Tech Note 19-09: Query and Access Date-and-Time in the era of ORDA

**Author:** Unknown (not stated in available material)
**Published:** May 30, 2019 | **Product/Version:** 4D v17 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78266
**Download:** https://kb.4d.com/DLTN/TN/2019/19-09_ORDA_AccessQuery_DateTime.zip

## Proposition
As 4D shifted developers toward ORDA's object-oriented data model, classic date-and-time querying needed a clear ORDA-native equivalent. This note (available here only via its sample-database readme) demonstrates storing and querying date/time values in ORDA objects, collections, and entities.

## Key Points
- **Storage patterns:** dedicated methods demonstrate storing date-and-time into a plain object, a collection, and an ORDA entity (`store_dateAndTimeInObject`, `store_dateAndTimeInCollection`, `store_dateAndTimeInEntity`).
- **Basic querying:** `Query_Date` and `Query_Time` show querying date and time values across collections and entity selections.
- **Filtering by month/day:** `query_DateByMonthAndDay` (with a test method) filters entity selections and collections by calendar month and day.
- **Filtering by hour/minute/second:** `query_TimeByHMS` and `query_ColTimeByHMS` (with a test method) filter by finer time granularity.
- **Environment requirement:** 4D v17.0 or later, run in 4D standalone.

## Featured Technology
- ORDA entity selections and collections
- Date/time storage and query methods in object notation

## Best Practices Highlighted
_Not available — full implementation detail could not be retrieved from the source PDF._

## Context / Positioning
Full technical detail unavailable — this summary is based on the published sample-database readme only, as the original tech note PDF could not be retrieved. The topic sits squarely within 4D's 2019 wave of ORDA-adoption guidance, helping developers translate familiar date/time query idioms into the newer object/entity-based data access model introduced in v16-17.

## Historical Commentary
**Status:** Still relevant

ORDA-based querying and filtering of date/time values on entity selections and collections remains a fully current, actively used pattern in 4D today — nothing in this topic area has been deprecated. Without the full PDF text, the precise query syntax and formula patterns used in 2019 can't be verified against today's ORDA API in detail, but the general approach (querying/filtering by date components, distinct handling for objects vs. collections vs. entities) is consistent with how ORDA date/time handling still works in current 4D versions.
