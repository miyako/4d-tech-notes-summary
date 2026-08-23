# Tech Note: Inherited Forms

- **Asset ID:** 27785
- **Tech Note #:** 02-30
- **Published:** July 31, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Steve Hartman, MCP, 4D, Inc. Information Systems
- **Page URL:** https://kb.4d.com/assetid=27785
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_30-35_(JUL)/02-30_Inherited_Forms.hqx

## Overview

Steve Hartman describes 4D 6.8's inherited-forms feature, which lets one form's objects be automatically pulled into other forms so shared UI elements -- a background, a logo, or a common set of navigation buttons -- only have to be designed and maintained once. It is likened to the existing "page 0" mechanism but scoped to the whole database's form set instead of a single form's own pages, so an inheritance form can be reused as a single shared "page 0" across many different table forms.

## Key Points

- Motivating use case: standardize OK/Cancel/Next/Previous buttons and a logo across every entry form in a database by putting them once in a dedicated inheritance form instead of copying them onto each form's page 0.
- Objects combine in a fixed load order when a form opens in the User environment or Custom menus: (1) page 0 of the inherited form, (2) page 1 of the inherited form, (3) page 0 of the open form, (4) current page of the open form.
- Only pages 0 and 1 of an inherited form can be surfaced in other forms -- other pages of the inherited form are not included.
- Object methods on inherited objects are still called, but the inherited form's own properties (window name, resizing, events) and its form method are not invoked when used via inheritance.
- Defined via the Form editor's Property List: click outside all objects to reveal the "Inherited form table" and "Inherited form name" properties, then pick the table and form to inherit from; selecting `<None>` stops inheritance.
- The inherited form's content shows as a non-editable preview in the host form's editor; to modify the inherited form's own objects, it must be opened directly in its own window.
- Inherited objects can be shown/hidden via the "Inherited form" option in the Display submenu of the Form menu or the editor's contextual menu.
- 4D detects and blocks recursive inheritance loops (e.g., a form designated as its own inherited form, directly or via a chain through a third form).
- Practical benefit called out: if a database is sold to multiple customers, only the single inheritance form's logo needs to change per customer, reducing the risk of a competitor's logo being left on a form.

## Featured Technology

- Inherited forms (Inherited form table / Inherited form name properties)
- Form page 0 / page 1 object combination order
- Form object and object-method reuse across tables
- Recursive inherited-form loop detection

## Historical Commentary

**Status:** Partially superseded

Steve Hartman explains 4D 6.8's inherited-forms mechanism, which lets a form pull in the page 0 and page 1 objects (backgrounds, common buttons, logos) of another designated "inherited" form so shared UI elements only need to be maintained in one place. The feature and its object-combination order (inherited page 0, inherited page 1, local page 0, current local page) are still present in current 4D and the technique remains directly usable as described. However, in modern Project-mode 4D development, form inheritance is now often complemented or superseded by more powerful reuse mechanisms such as components, form containers/inclusion, and class-based object composition, so it is one option among several rather than the primary reuse strategy.

References to newer/updated information:
- 4D form inheritance itself remains a supported, unchanged feature in current 4D versions
- Modern 4D projects (Project mode) offer additional reuse mechanisms -- components, included forms/objects, and ORDA/class-based composition -- that developers often prefer alongside or instead of classic form inheritance for larger applications
