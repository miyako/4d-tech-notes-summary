# Tech Note 07-06: 4D 2004 Product Registration

**Author:** Tom Fitch, Technical Support Engineer, 4D Inc.
**Published:** February 14, 2007 | **Product/Version:** 4D v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=45476
**Download:** https://kb.4d.com/DLTN/TN/2007/Windows/TN_2007_05-09_(FEB)/07-06_4D_2004_Registration.pdf

## Overview
This Tech Note is a customer-support reference explaining how to complete the activation/registration process for 4D 2004 "base products" (4th Dimension, 4D Server, 4D Runtime Single User) and "expansion products" (expansion packs and upgrades), plus troubleshooting for common registration failures.

## Key Points
- **Three registration methods:** Online (requires internet connection and a 4D Customer/Partner ID), Offline (seed file generated locally, uploaded via register.4d.com, serialization file emailed back and integrated), and Emergency (temporary 5-day activation, base products only, usable once).
- **Base product wizard flow:** Welcome screen → License Agreement → Activation Mode → Choose Account → Product Number entry → Congratulations confirmation.
- **Product number formats:** examples given for 4th Dimension Standard/Developer Edition and 4D Server Standard Edition (Mac/Win variants).
- **Expansion/upgrade registration:** initiated via the Help > "Update License…" menu from within an already-open base product; associates the expansion to a specific base product number (cannot later be moved to a different base product).
- **4D Licenses folder:** stores downloaded license files as `.html` (named by product name or product number), viewable in a browser, containing registration details.
- **Troubleshooting section:** covers "Invalid Customer Code/Password," missing product numbers in Active Licenses, "Expansion already linked to another product," orphaned expansion licenses (and how to re-link them), "No more seed credit," redirect issues on register.4d.com, and missing serialization emails — each with a resolution path and 4D support contact info.

## Featured Technology
- 4D 2004 activation/registration system (online, offline, emergency modes)
- register.4d.com web registration portal
- 4D Licenses folder and license `.html` files

## Historical Context
Published in February 2007 for 4D 2004, this note is purely administrative and predates 4D v11's SQL engine entirely. It documents an activation workflow, UI, and web portal (register.4d.com) tied specifically to that product generation.

## Historical Commentary
**Status:** Obsolete

4D's product licensing and activation systems have been redesigned multiple times since the 2004 generation, and the specific wizard screens, product-number formats, and register.4d.com offline-registration flow described here no longer exist in any current 4D product. This note has no lasting technical or conceptual value beyond illustrating 2000s-era software activation UX; it is retained here purely for historical/archival interest.
