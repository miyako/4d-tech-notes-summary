# Tech Note: Three-State Checkboxes

- **Asset ID:** 33418
- **Tech Note #:** 04-30
- **Published:** July 29, 2004
- **Product / Version:** 4th Dimension 2003.3
- **Platform:** Mac & Win
- **Author:** Sati Hillyer (4D Evangelist, 4D Inc.)
- **Page URL:** https://kb.4d.com/assetid=33418
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_26-30_(JUN)/04-30_3-State_Checkboxes.hqx

## Overview

Written by Sati Hillyer, this note introduces the three-state checkbox object new to 4D 2004, contrasting it with the laborious pre-2004 approach of simulating three states using three separate images stored in an array and displayed through a picture button. With the native feature, a checkbox can now be enabled directly in the Form Editor to cycle through unchecked (0), checked (1), and an intermediate 'don't care' state (2), each represented by a distinct value the developer can read in code. The note builds a practical scenario: a custom Find dialog over a Tasks table where users search by person, task, or description, plus a Completed (boolean) and Due (date) field. With ordinary two-state checkboxes, a user could search completed-or-incomplete tasks but never 'either, I don't care' at the same time as other filters; adding a third, intermediate state to the Completed and Due checkboxes solves this. The included ExecuteFind method demonstrates the resulting logic: a Case of block builds the base QUERY by search field, then two further Case of blocks branch on each checkbox's value (0/1/2) to append a True, False, or no additional QUERY condition (using the '&' combination operator) for Completed and Due, respectively, before a closing QUERY call finalizes the search.

## Key Points

- Prior to 4D 2004, three-state checkbox behavior required three images in an array driven by a picture button; 4D 2004 makes this a standard, directly enabled Form Editor object property.
- The three checkbox values are 0 (unchecked), 1 (checked), and 2 (intermediate/'don't care'), directly readable by the developer's code.
- The scenario builds a custom Find dialog for a Tasks table (fields Person, Task, Description, Completed, Due) where basic two-state checkboxes cannot express 'match either state.'
- The ExecuteFind method chains QUERY calls: an initial Case of picks the base search field (Person/Task/Description), then two Case of blocks on cCom and cDue append QUERY([Tasks];&;[Tasks]Completed=True/False;*) or skip the condition entirely when the checkbox is in the intermediate state.
- The '&' parameter combines successive QUERY calls into one compound search; the trailing '*' parameter keeps the query open for further conditions until the final QUERY call without '*' executes it.
- The technique lets a single dialog express filters ranging from fully specific (must be completed, must have a due date) to fully permissive (don't care about completion or due status) without separate dialogs.

## Featured Technology

- Three-state checkbox form object (4D 2004)
- Form Editor checkbox state activation
- Building a custom Find dialog with 'don't care' search criteria
- Conditional QUERY construction based on checkbox state (0/1/2)

## Historical Commentary

**Status:** Still Relevant

This note demonstrates a genuinely useful new 4D 2004 UI feature -- the native three-state checkbox -- applied to a practical query-building problem (letting users express 'don't care' alongside true/false filters in a single Find dialog), replacing a much clunkier three-image workaround from earlier 4D versions. Three-state checkboxes remain part of the current 4D form object model and the conditional QUERY-construction pattern shown is still a standard technique for building flexible search interfaces, so this note's core content is still directly applicable, though 4D's List Box and modern form object properties now offer additional ways to expose similar tri-state controls.

**References to newer/updated information:**
- Three-state checkboxes remain a standard 4D form object property and are unchanged in concept from what this note describes
- The QUERY-with-'&'-and-'*' pattern for building compound, conditionally-included search criteria is still a standard 4D language technique
- Modern 4D List Box and form object properties provide additional ways to expose tri-state or multi-value filter controls beyond the basic checkbox shown here
