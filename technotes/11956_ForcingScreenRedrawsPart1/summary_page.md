# Tech Note: Forcing Screen Redraws: Updating a Progress Display on a Form, Part I

**Author:** Not specified in source document
**Published:** March 1, 2000 | **Product/Version:** 4D v6.5 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11956
**Download:** Not available (NO_DOWNLOAD_LINK_TEASER_ONLY)

## Overview
This Tech Note covers Part I of a two-part series showing a trick to force an immediate partial redraw of a form, useful for live progress-display updates.

## Key Points
- Its core motivation is updating a progress display in real time: without an explicit redraw trigger, changes to a progress bar or status text made during a long-running process might not visibly update until the process yields control back to the interface, leaving users looking at a seemingly frozen screen.
- The note's proposition is narrowly focused and practical — a technique, rather than a broad feature tour — meant to solve exactly this one recurring UX annoyance in classic 4D applications running in the Custom Menus/Design environment of the era.
- Because only the brief teaser text survives in this archive, the exact commands or object manipulation sequence used to force the redraw are not preserved here, but the general class of technique (toggling or nudging an object's visibility/state to force the forms engine to repaint) is consistent with other custom-UI workaround notes from this same era.
- This kind of trick mattered a great deal in classic 4D development, where long, synchronous processes (imports, calculations, batch operations) needed some visible sign of progress to reassure users the application hadn't hung.
- As the first of a two-part series, this note presumably sets up further techniques in Part II for related progress-display or redraw scenarios, though only this Part I entry is included in the present archive batch.

## Featured Technology
- Form redraw tricks
- Progress display updates
- Custom Menus environment UI

## Historical Context
This note documents a classic workaround for forcing 4D to immediately redraw a portion of a form — needed because 4D's classic forms engine did not always refresh visible objects in real time during long-running processes, making progress-indicator updates otherwise appear frozen. This specific low-level redraw trick is obsolete in the sense that 4D's forms/rendering engine has been substantially modernized since (with better native progress and redraw handling, plus web-based UI options), but the underlying UX goal of showing responsive progress during long operations remains a universally relevant design concern. Related updates since: 4D's forms rendering engine has been modernized considerably since 2000, reducing the need for manual redraw tricks to update progress displays; Progress indication in modern 4D apps is more commonly handled via built-in progress bar objects, process-based UI updates, or web-based UI rather than this era's manual redraw workaround. The full Tech Note PDF/text could not be recovered for this archive entry because the old kb.4d.com page had no working download link at all; this summary is based only on the short teaser paragraph available on the original kb.4d.com page, so it does not go beyond what that teaser describes.
