# Tech Note 18-11: Custom 4D Write Pro Navigation Panel

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** June 21, 2018 | **Product/Version:** 4D Write Pro v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78076
**Download:** https://kb.4d.com/DLTN/TN/2018/18-11_4DWriteProNavPanel.zip

## Proposition
Presents a component ("WPNP") that adds a page-navigation subform and a full-screen presentation mode to any 4D Write Pro document, exploiting the fact that Write Pro areas are manipulable objects that can be duplicated, zoomed, and synced independently of the live editing view.

## Key Points
- **Write Pro as an object:** the whole approach hinges on 4D Write Pro documents being objects that can be copied/manipulated, a capability introduced with Write Pro in v15 and expanded through v17.
- **Two form components:** "WPForm" hosts a read-only, 25%-zoom subform for browsing pages; "FullScreenFormWP" displays a single page at a time in presentation mode.
- **Bidirectional sync:** clicking a page in the subform jumps the main document (`WPNP_pointToPage`), and scrolling the main document updates the subform's highlighted page (`WPNP_updateSubform`).
- **CALL SUBFORM CONTAINER:** used to bubble click events from the subform component back up to the parent form.
- **Storage object for state:** bookmarks and page ranges are persisted via `Storage.writeProObj` rather than process variables, enabling reload across the component's forms.
- **WP New + OB Get for page loading:** full-screen navigation reloads the correct page object using `WP New(OB Get(Storage.writeProObj;$nextWPPage))`.
- **Nine component methods:** WPNP_createBookMark, WPNP_getCurrentPageNum, WPNP_getFocusedScr, WPNP_loadWPForm, WPNP_openPreviewForm, WPNP_pointToPage, WPNP_storeRangePages, WPNP_updateCurrPages, WPNP_updateSubform form the full public API of the component.
- **Requires v17+:** explicitly noted as depending on new Write Pro object-notation page-location commands only available from v17 onward.

## Featured Technology
- 4D Write Pro (object model, WP New, WP object notation)
- Form components / Subforms
- CALL SUBFORM CONTAINER
- Storage object (shared process memory)
- Classic typed variables (C_LONGINT, C_TEXT)

## Best Practices Highlighted
1. Use a dedicated read-only, low-zoom copy of a Write Pro object for a navigation/thumbnail view rather than reusing the live editing area.
2. Use the Storage object (not process variables) to share page-range/bookmark state between sibling forms in a component.
3. Package reusable UI behavior as a form component so it can be dropped into any database.

## Context / Positioning
Published in mid-2018, this note showcases 4D Write Pro's maturing object model roughly three years after its v15 debut, at a time when 4D was actively encouraging developers to move off classic 4D Write toward Write Pro. It predates 4D's later, more built-in navigation/outline conveniences for Write Pro and reflects the "classic form component + Storage object + C_LONGINT/C_TEXT declarations" style typical of pre-class-based 4D code.

## Historical Commentary
**Status:** Partially superseded

The premise — treating a 4D Write Pro document as a manipulable object to build custom navigation UI — remains conceptually valid, and 4D Write Pro continues to be the actively developed word-processing engine (classic 4D Write is legacy/deprecated). However, later 4D versions added more native page-thumbnail, outline, and navigation conveniences to Write Pro, which may reduce the need to hand-build a component like WPNP for many use cases today.

The code style is dated: classic `C_LONGINT`/`C_TEXT` variable declarations have been superseded by typed `var` declarations (available from v19+), and the component packaging approach (classic form components dropped into a binary-structure database) predates 4D's newer project-based component architecture. A developer wanting this functionality today would likely re-implement the synchronization logic using classes and modern typed code, but the WP New/Storage-based synchronization technique itself is still a reasonable pattern.
