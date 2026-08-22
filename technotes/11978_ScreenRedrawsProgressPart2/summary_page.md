# Tech Note: Forcing Screen Redraws: Updating a Progress Display on a Form, Part II

## Overview
- **Technical Note (number unavailable)**
- **Author:** Unknown / not specified
- **Published:** June 1, 2000
- **Product/Version:** 4D v6.5
- **Platform:** Mac & Win
- **Content source:** Teaser abstract only (full archive not recoverable)

## Key Points
This Tech Note is the second half of a two-part series on displaying progress feedback on a 4D form while a lengthy process is running. Part I (not itself among this archive's assigned notes) introduced a simple trick for forcing an immediate redraw of a portion of a form even while code is actively executing in that form's process, solving the common problem of a progress indicator appearing frozen because 4D wasn't refreshing the screen during a tight processing loop. This Part II builds directly on that foundation, showing how to combine the forced-redraw technique with the MESSAGE command to produce a noticeably faster-updating, lower-overhead progress display, and it includes practical tips for further reducing the processing overhead that a progress display itself can introduce into an otherwise CPU-bound loop. The featured technology is this pairing of a manual screen-redraw workaround with the MESSAGE command, a foundational pattern from an era when 4D forms did not automatically refresh mid-process and no native progress-bar object existed. Because only the teaser abstract survives for this note — its kb.4d.com page had no working download link at all, so no downloadable archive was ever available to recover — the exact code combining the redraw trick with MESSAGE could not be reconstructed here.

## Featured Technology
- Forced form redraw technique
- MESSAGE command
- Progress display optimization

## Historical Context
This note combines a manual forced-redraw trick with the MESSAGE command to build a faster, lower-overhead progress display in classic 4D forms — a real necessity in an era before native progress-bar objects and modern process/UI-thread handling existed in 4D. The specific low-level redraw-forcing workaround is superseded by later 4D releases' built-in progress indicator objects and improved automatic screen-refresh handling during long-running processes, though the general goal of giving users responsive visual feedback during long operations remains just as important today.

**Note on sources:** The full downloadable archive for this Tech Note could not be recovered in this environment. The original kb.4d.com page's linked download was an old Windows self-extracting installer (.exe) that could not be extracted in this environment, so this summary is based only on the teaser abstract.

## What's Changed Since
- Later 4D releases introduced native progress-indicator form objects and improved automatic screen-refresh behavior during long-running processes, reducing the need for manual forced-redraw tricks like this one
- The MESSAGE command and general process-status-display concepts remain part of 4D, even as the specific redraw-forcing workaround described here is no longer the recommended approach

