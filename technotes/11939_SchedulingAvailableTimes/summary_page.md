# Tech Note: Storing and Searching for Available Times in a Schedule

**Author:** Not specified in source document
**Published:** January 1, 2000 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11939
**Download:** Not available (NO_DOWNLOAD_LINK_TEASER_ONLY)

## Overview
This Tech Note covers a data-modeling and search technique for storing appointment schedules in fixed time units and finding available open time slots that meet specific criteria.

## Key Points
- Its proposition is a simple, flexible approach to modeling and querying this kind of time-based availability data without requiring an overly complex data structure or search algorithm.
- The core data-modeling technique involves representing each doctor's day as a sequence of fixed-size time units (10 minutes in the example), so appointments of any duration map onto a contiguous run of one or more of these units, letting the search for available time reduce to a well-defined problem of finding sufficiently long contiguous runs of unbooked units that also satisfy any additional time-window constraints (like starting after a specific hour).
- This fixed-granularity approach trades some storage/query overhead for a much simpler and more flexible search algorithm compared to trying to work directly with arbitrary, variable-length appointment start/end timestamps.
- Featured technology is 4D's relational data modeling and query/search capabilities applied to this specific scheduling domain, likely built using sets or arrays of time-unit records associated with each doctor, though the surviving teaser text does not detail the exact table structure or search method code.
- This kind of scheduling and availability-search problem recurs constantly across many different application domains — medical offices, equipment reservations, meeting rooms, service appointments — making the note's underlying data-modeling and search technique broadly applicable and durable, independent of any particular 4D language version or feature, since the core challenge (representing and efficiently querying time-based availability) is a timeless database design problem.

## Featured Technology
- Scheduling/appointment data model
- Time-slot search algorithm
- Relational data design for time-based queries

## Historical Context
This note presents a data-modeling and search technique for appointment scheduling — dividing each day into fixed time units (e.g., 10-minute slots) and searching for open blocks matching a duration/time-window criteria, illustrated with a doctor's office scheduling example. This is a timeless database/algorithm design problem independent of any particular 4D version, and the general approach (fixed-granularity time slots plus a search/scan technique to find qualifying open runs) remains a valid, still-relevant pattern for building scheduling features in 4D or any other database platform today. Related updates since: The core data-modeling and time-slot search technique remains a valid, general approach to scheduling problems in any database platform, including current 4D applications; Modern 4D applications might implement this with collections/ORDA entity selections rather than the classic array/selection-based code likely used in the original 2000 sample database, but the underlying algorithmic approach is unchanged. The full Tech Note PDF/text could not be recovered for this archive entry because the old kb.4d.com page had no working download link at all; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
