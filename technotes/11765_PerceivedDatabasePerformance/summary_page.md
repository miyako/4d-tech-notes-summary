# Tech Note: Improving the Perception of Database Performance

**Author:** Not specified in source document
**Published:** June 1, 1997 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11765
**Download:** Not available (no working download link archived for this page)

## Overview

This Tech Note presents a technique for improving the perceived (not necessarily raw) performance of a specific database activity by putting otherwise-idle processor time to productive use.

## Key Points

- Frames the premise that by 1997, fast disks and CPUs meant the processor was often idle, simply waiting on user input.
- Proposes using that idle time to improve the perceived responsiveness of a specific database operation.
- Only the teaser text is available for this asset, so the exact implementation technique described is not verifiable here.

## Featured Technology

- Idle processor time utilization
- Perceived performance optimization techniques in 4D v6

## Historical Context

The full archived text for this note could not be recovered (no working download link on the archived page), so this summary is based only on the available teaser. The underlying idea — using idle time to boost perceived responsiveness — predates and outlives the specific single-threaded 4D v6 execution model it was written against; modern 4D's multi-process/worker architecture offers far richer tools for the same goal.

## Historical Commentary
**Status:** Still relevant

The core idea in this note — using otherwise-idle CPU cycles to make an application feel faster to the user, i.e. perceived-performance optimization — is a timeless UX/engineering principle still very much relevant today, even though the specific 1997-era mechanisms available in 4D (single-threaded execution, limited background processing primitives) have been superseded by 4D's modern multi-process, multi-threaded, and worker-based architecture.
