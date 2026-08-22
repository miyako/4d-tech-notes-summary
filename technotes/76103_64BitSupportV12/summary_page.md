# Tech Note 10-15: Understanding 64-bit Support in 4D v12

**Author:** Josh Fletcher, Technical Services Team Member, 4D Inc.
**Published:** May 14, 2010 | **Product/Version:** 4D v12 | **Platform:** Win
**Page:** https://kb.4d.com/assetid=76103
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_15-19_(MAY)/10-15_4D-v12-64-bit-Support.pdf

## Proposition
Published ahead of 4D v12's release, this note explains what 4D Server v12's newly announced 64-bit Windows executable actually means in practice — chiefly removing the ~4GB practical memory ceiling to enable a much larger server cache and more concurrent clients — while cautioning that it is not a general performance "magic bullet."

## Key Points
- **Expectation management:** 64-bit support is presented as valuable mainly for scalability (memory addressing), not as an automatic speed boost.
- **Beta status disclosed:** 4D Server v12 x64 would not ship with 4D v12.0's initial release and would remain in beta afterward.
- **Platform limitation at the time:** requires 64-bit Windows Vista or Windows Server 2003 or later; Mac OS X was not supported for 64-bit at that time.
- **Historical framing:** brief history of 64-bit adoption (64-bit instruction sets ~2003, 64-bit Windows XP 2005) to contextualize why 4D was introducing this now.
- **Core benefit:** breaking the ~4GB memory limit enables a substantially larger 4D Server cache.
- **Secondary benefit:** larger addressable memory supports significantly more concurrent client connections.
- **Related tuning resources:** 4STK resources and database parameters 53 and 61 are cited for further cache/connection configuration.

## Featured Technology
- 4D Server v12 x64 (Windows-only, beta at v12 launch)
- 64-bit memory addressing and larger server cache
- Increased maximum concurrent client connections
- 4STK resources and database parameters 53 and 61

## Best Practices Highlighted
1. Don't expect 64-bit support alone to resolve unrelated performance problems — plan cache/connection sizing around it specifically.
2. Verify OS-level 64-bit prerequisites (Windows Vista/Server 2003 64-bit or later) before planning a 64-bit deployment.
3. Consult database parameters 53 and 61 when tuning cache behavior on a 64-bit server.

## Context / Positioning
Published as pre-release guidance ahead of 4D v12, this note set realistic expectations for a headline marketing feature (64-bit support) so developers and administrators could plan server capacity decisions accurately.

## Historical Commentary
**Status:** Obsolete

This note pre-announced 4D Server v12's first 64-bit executable (Windows-only, still in beta at v12's release) and carefully managed expectations that 64-bit support is chiefly about breaking the ~4GB memory ceiling for larger caches and more concurrent clients, not a general performance "magic bullet."

64-bit 4D Server is now the sole, standard deployment target across both Mac and Windows — 32-bit 4D Server was discontinued long ago — so while the note's underlying explanation of why 64-bit matters (larger cache, more clients) remains conceptually accurate, its framing of 64-bit as a new, optional, Windows-only, beta-stage feature is entirely obsolete history; current 4D server sizing/cache documentation supersedes this note's forward-looking guidance.
