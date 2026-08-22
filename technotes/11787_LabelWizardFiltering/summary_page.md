# Tech Note: Filtering Methods and Forms in the 4D V6 Label Wizard

**Author:** Not specified
**Published:** December 1, 1997 | **Product/Version:** 4D v6.0.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11787
**Download:** Not available (no working download link archived — teaser only)

## Overview
This note addresses a developer concern introduced by 4D V6's new Label Wizard: by default, end users are shown drop-down lists of every database form and visible project method, risking accidental data corruption or confusion. Only the on-page teaser is available; the full PDF could not be recovered for this asset.

## Key Points
- The V6 Label Wizard let users design/print custom labels, name badges, or multi-column record listings, extending the older 4D Label Editor.
- New V6 features allowed selecting a database form for label output and a project method to run on each printed record.
- Default behavior exposed the entire list of database forms and visible project methods to end users via drop-down menus.
- A mistaken selection by a user could range from confusing output to serious, undesired data modifications.
- The note's purpose: show developers how to filter these lists so only intended selections are available to end users.
- No specific filtering technique, code, or configuration steps are present in the recovered teaser text.

## Featured Technology
- 4D V6 Label Wizard
- 4D Label Editor
- Database forms and project methods list filtering

## Historical Context
Published December 1997, shortly after the V6 release, this note reflects a real safety/usability concern of exposing raw internal developer artifacts (forms, methods) directly to end users without curation. The archive of the full technical content could not be recovered (no working download link exists for the original page). The specific V6-era Label Wizard and Label Editor have long since been superseded by many generations of 4D's form design and reporting/printing tools, and later concepts like Project Mode (2018) and modern component/package organization address end-user exposure control differently; the general design principle of never surfacing unfiltered internal artifacts to end users, however, remains sound.
