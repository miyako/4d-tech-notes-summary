# Tech Note 11-27: Coding differently in 4D V12

**Author:** Christophe Keromen, Cabinet de Consultants CKTI
**Published:** November 9, 2011 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76432
**Download:** https://kb.4d.com/DLTN/TN/2011/11-27_CodingDifferentlyIn4Dv12.zip

## Proposition
This Tech Note is a curated collection of coding-style suggestions enabled by new 4D v12 editor functionality, helping developers adopt more disciplined, discoverable, and maintainable method-writing habits.

## Key Points
- **Help-tip comments:** structured comment conventions (signature line + usage notes) surface automatically as help tips when hovering over method names.
- **Comment organization:** tags in comments and code-block folding/unfolding keep long methods navigable.
- **Review comments and code examples:** conventions for flagging code that needs review.
- **Local variable blocks and error hiding:** patterns for cleanly declaring locals and suppressing routine error-handling noise.
- **Assertions:** introduces the ASSERT mechanism and its 4D v12 commands, including how to enable/disable assertions globally.
- **Refactoring tools:** eliminating unused objects, finding where an object is declared/used, searching a method's callers, Goto Definition, and safe renaming.
- **Misc tips:** reducing unnecessary typing in variable names, highlighting private component methods, hyperlinked comments, and code-block highlighting.

## Featured Technology
- Method comments and code editor help tips
- Code folding, method Explorer, and 'Goto Definition'
- Assertions (ASSERT) and code refactoring/renaming tools

## Context / Positioning
Published shortly after 4D v12's release in late 2011, this note helped developers get the most out of new editor and language features (assertions, refactoring aids) by suggesting concrete style conventions, at a time when 4D's Design Mode method editor was the sole coding environment.

## Historical Commentary
**Status:** Still Relevant

Most of the code-editor productivity techniques here (structured comments, help tips, folding, ASSERT, Goto Definition, renaming, hyperlinked comments) operate within 4D's classic binary Design Mode method editor and are still functionally present and useful in current 4D, so they remain largely valid coding hygiene practices.

However, since methods now live as plain text files under Project mode, some workflow specifics (e.g., navigating the binary Explorer, component-private-method highlighting tied to old component packaging) are dated, and text-based version control/diffing now offers additional refactoring safety nets that did not exist in 2011.
