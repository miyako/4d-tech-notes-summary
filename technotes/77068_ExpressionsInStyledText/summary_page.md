# Tech Note 14-10: Using Expressions in 4D Styled Text

**Author:** Timothy Tse, Technical Services Team Member, 4D Inc.
**Published:** June 12, 2014 | **Product/Version:** 4D v14.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77068
**Download:** https://kb.4d.com/DLTN/TN/2014/14-10_ExpressionInStyledText.zip

## Proposition
4D v14 lets developers embed live 4D expressions (fields, variables, commands, methods) directly inside Multi-style styled text variables, enabling template-driven letters, emails, and reports without generating one document per record manually.

## Key Points
- Styled text variables are created by checking "Multi-style" in a variable's Property List; formatting is stored as inline HTML span tags with CSS.
- `ST INSERT EXPRESSION` inserts a reference to a field/variable/command/method at the cursor or over the selected text.
- `ST SET OPTIONS` toggles whether inserted expressions display as computed **values** or as raw **references**.
- `ST COMPUTE EXPRESSIONS` refreshes dynamic expressions (e.g., when the current record changes); `ST FREEZE EXPRESSIONS` permanently converts them to static text.
- `ST GET PLAIN TEXT` and `ST GET TEXT` extract the content without or with styling tags, respectively.
- The bundled sample database combines a rich text editor with an Email form supporting templates, saved documents, and direct sending via 4D Internet Commands (SMTP).

## Featured Technology
- Multi-style styled text variables
- `ST INSERT EXPRESSION`, `ST SET OPTIONS`, `ST COMPUTE EXPRESSIONS`, `ST FREEZE EXPRESSIONS`, `ST GET PLAIN TEXT`, `ST GET TEXT`
- 4D Internet Commands (SMTP) for sending the resulting styled/HTML content as email

## Best Practices Highlighted
1. Use expression references (not frozen values) for reusable templates; freeze only the final version sent/saved for a specific record.
2. Combine `ST COMPUTE EXPRESSIONS` with record navigation to keep mail-merge templates in sync with the current selection.
3. Reserve picture/blob content out of styled text expressions, since expressions cannot be picture-typed.

## Context/Positioning
Published soon after v14 shipped, this note showcased a small but practical new language capability aimed at automating repetitive document/email personalization tasks for business applications.

## Historical Commentary
**Status:** Partially superseded

The underlying `ST_` command family for embedding expressions in styled text variables still exists and works in current 4D versions, so the specific techniques shown remain technically valid. However, for serious mail-merge and rich-document generation, 4D has since introduced 4D Write Pro (v16+), a considerably more capable word-processing engine with its own references/formulas mechanism and a more open document format — making it the modern recommended tool for the kind of templated-letter and email-generation use case this note targets, while classic styled text variables remain a lighter-weight fallback for simple in-form rich text.
