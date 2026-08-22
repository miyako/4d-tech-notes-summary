# Tech Note 10-16: Rich Text in 4D v12

**Author:** Not specified
**Published:** May 21, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76106
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_15-19_(MAY)/10-16_Rich Text.zip

## Proposition
This note introduces 4D v12's new Rich Text feature, which allows different style attributes (font, size, weight, alignment, color) to be applied to individual characters within a single text object rather than requiring one uniform style per object, storing the styling as embedded HTML `<SPAN STYLE>` markup within the field/variable content itself.

## Key Points
- **New capability:** per-character styling within a text object — previously styles could only apply to the whole object.
- **Supported objects:** fields, variables (including arrays), and list box cells, restricted to Text or Alpha type.
- **Alpha field caution:** since styling adds markup characters to the content, Alpha fields (255-character limit) risk data loss/truncation when styled.
- **Storage format:** styled text is stored with the actual content including HTML `<SPAN STYLE="font-family:...; font-size:...; ...">` tags around styled runs.
- **Available style attributes:** font-family, font-size, text-align, font-weight, font-style, text-decoration, color, and background-color (ignored on Mac OS).
- **Querying/sorting/indexing** must operate against the semantic (unstyled) text so Rich Text doesn't break existing data operations.
- **Enabling display:** requires the "multi-style" form object property; also interacts with contextual menus, entry/display filters, drag-and-drop/copy-paste, and Quick Report/Labels output.

## Featured Technology
- Rich Text (per-character styling of text objects, new in 4D v12)
- HTML `<SPAN STYLE=...>` encoding of styled text
- multi-style form object property
- Entry/Display filters and Quick Report/Labels interaction with Rich Text
- List box Rich Text cell rendering

## Best Practices Highlighted
1. Avoid using Alpha-typed fields for Rich Text content given the 255-character limit and markup overhead; prefer Text type.
2. Be mindful that queries/sorts operate on content that includes embedded style markup unless handled carefully.
3. Enable the "multi-style" property explicitly wherever per-character styled rendering is required in a form.

## Context / Positioning
Published for 4D v12's initial rollout, this note highlighted a headline new UI/data feature (Rich Text) aimed at developers who previously needed to fake styled text with separate objects or accept whole-object-only styling.

## Historical Commentary
**Status:** Still Relevant

This note documents 4D v12's introduction of true per-character Rich Text styling for text/alpha fields, variables, and list box cells, storing style information as embedded HTML `<SPAN STYLE=...>` tags — a functional but somewhat idiosyncratic approach (mixing markup directly into field content) that predates 4D's later, cleaner rich-content models.

The basic Rich Text object feature described here still exists and works in current 4D versions for simple in-place styled text needs, but for substantial rich-text document editing/generation, 4D Write Pro (introduced v16, with a structured, non-HTML-embedded content model) is now the recommended tool, and purely read-only rich content is often better handled via a Web Area rendering HTML directly.
