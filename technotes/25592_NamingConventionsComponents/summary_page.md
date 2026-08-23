# Tech Note: Naming Conventions to Simplify Component Development and Use

- **Asset ID:** 25592
- **Tech Note #:** 02-51
- **Published:** November 30, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** David Adams
- **Page URL:** https://kb.4d.com/assetid=25592
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_51-55_(NOV)/02-51_Naming_Conventions.hqx

## Overview

David Adams addresses a usability problem in classic 4D Insider component development: a method's assigned protection level (private, protected, or public) is only visible within 4D Insider itself, not while editing code in 4D, so a developer can unknowingly write a public method that calls a forbidden private method, an error only caught later when 4D Insider regenerates the component. He proposes a structured naming convention -- `<Component prefix><protection indicator><Descriptive name>` -- where private methods get no special character, protected methods get a leading underscore, and public methods get a leading space, so that within both the source-code database and any target database, methods visually sort together by protection level and their status is legible directly from the method name. He illustrates the scheme with a hypothetical 'LogManager' component and shows how it also makes it trivial to spot when a method has been assigned to the wrong folder in 4D Insider.

## Key Points

- Explains 4D Insider's three component protection levels: private (invisible in the target database), protected (name visible, cannot be renamed/deleted/edited, but callable from other component code), and public (visible, editable, cannot itself call private methods).
- Identifies the core problem: within the source-code database, there is no in-editor indication of a method's assigned protection level, so nothing prevents writing a public method that calls a private one -- a mistake 4D Insider only flags after regenerating the component, and even then the target-database Explorer's visual cue for protected methods is small and easy to miss.
- Proposes the naming scheme `Component prefix + {Protection indicator} + Descriptive name`, with a worked example for a 'LogManager' component: private = `LogManagerCloseLog`/`LogManagerOpenLog` (no separator), protected = `LogManager_Initialize`/`LogManager_Start` (underscore), public = `LogManager Setup` (space).
- Notes that this scheme causes public methods to sort to the top of the method list in the target database (since a space sorts before other characters), making it easier for component users to quickly find the routines they're permitted to edit.
- Points out an additional benefit: because the naming convention encodes the intended protection level, a developer can visually cross-check the 4D Insider folder assignment for each method and immediately spot when a method (e.g., `LogManager_Start`) has been placed in the wrong folder.

## Featured Technology

- 4D Insider component packaging (public/protected/private folders)
- Method naming conventions for visual sorting
- Component prefix + protection-indicator naming scheme
- 4D Explorer window visual cues for protected methods

## Historical Commentary

**Status:** superseded

David Adams tackles a real usability gap in the classic 4D Insider component system: a method's public/protected/private status is only visible in 4D Insider itself, not in the 4D language editor, so nothing stops a developer from accidentally calling a private method from a public one until 4D Insider later flags the error. His fix is a structured naming scheme -- component prefix, then a protection indicator (no special character for private, underscore for protected, a space for public), then a descriptive name -- so methods sort together by protection level and their status is visible at a glance in both the source and target databases. 4D Insider and its public/protected/private folder mechanics have since been superseded by 4D's modern native component architecture, making the specific mechanics obsolete, but the broader naming-convention principle for signaling a component's intended API surface remains sound advice applicable to today's 4D components and classes.

References to newer/updated information:
- 4D Insider and its public/protected/private folder-based component packaging have been superseded by 4D's modern native component architecture
- The underlying naming-convention principle -- visually distinguishing a component's public API from its internal implementation -- remains valid practice for today's 4D components and classes
