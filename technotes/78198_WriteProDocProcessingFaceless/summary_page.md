# Tech Note 19-01: Processing Write Pro documents (faceless)

**Author:** Vance Villanueva, Technical Services Engineer, 4D Inc.
**Published:** January 30, 2019 | **Product/Version:** 4D Write Pro v17 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78198
**Download:** https://kb.4d.com/DLTN/TN/2019/19-01_WriteProDocProcessingFaceless.zip

## Proposition
Legacy 4D Write could process documents headlessly using an offscreen area (`WR New offscreen area`), a pattern commonly used for batch mail merges and PDF/email generation. 4D Write Pro handles documents as objects without needing an offscreen area, but embedded expressions can fail to evaluate reliably without a form object present — this note provides a workaround.

## Key Points
- **Problem:** in 4D Write Pro, each character occupies exactly one document position, so multi-character embedded expressions may not evaluate correctly in a faceless (no form UI) context.
- **Expressions recap:** expressions (e.g., `Query([People];[People]firstName="Bob")`, `Current date`) are inserted via `WR INSERT EXPRESSION` or the Insert → 4D Expressions menu and evaluated at runtime.
- **EVALUATION_METHOD wrapper:** encapsulates a found expression as a call like `EVALUATION_METHOD("Query(...)")`, re-inserted at the original document location; internally it wraps the text as a `<!--4DEVAL ... -->` tag and resolves it with `PROCESS 4D TAGS`.
- **PROCESS_EXPRESSIONS traversal:** a helper method takes a pointer to the 4D Write Pro object, scans the whole document for expressions, substitutes each with the wrapped call, and returns an updated object.
- **Method registration:** `SET ALLOWED METHODS` must register `EVALUATION_METHOD`/`PROCESS_EXPRESSION` before 4D Write Pro will execute them.
- **Output paths demonstrated:** printing the processed document to paper/PDF via `WR PRINT`-family commands, and exporting to HTML for emailing.
- **Migration caveat:** documents converted from legacy 4D Write to 4D Write Pro reference tables/fields by internal numeric IDs, so the *same* database (not a copy) must be used to preserve working expressions.

## Featured Technology
- 4D Write Pro (object-based document API)
- `PROCESS 4D TAGS`
- `SET ALLOWED METHODS`
- `WR INSERT EXPRESSION` / Insert → 4D Expressions
- 4D Write Pro print/export commands (paper, PDF, HTML)

## Best Practices Highlighted
1. Always test a 4D Write-to-4D Write Pro document conversion against the original database, since expressions reference tables/fields by internal ID.
2. Register any custom evaluation methods with `SET ALLOWED METHODS` before invoking faceless document processing.
3. Read the full Tech Note before the sample database, as its inline comments assume the concepts here are understood.

## Context / Positioning
Published alongside the v17R2/v17R4 rollout of expanded 4D Write Pro capability, this note reflects 4D's effort to preserve legacy 4D Write's practical batch-processing workflows (mail merges, automated reports/emails) as customers migrated to the 64-bit-only 4D Write Pro engine, filling a gap left by the retirement of the offscreen-area API.

## Historical Commentary
**Status:** Partially superseded

Faceless/backend document generation is still a routine, fully supported 4D Write Pro use case today, and 4D Write Pro remains the current, actively developed document engine (4D Write classic has been fully retired in 64-bit 4D, so the migration guidance here is now purely historical background). However, 4D Write Pro's API for headless document manipulation has matured considerably since this v17R2-era note, and 4D's own documentation and later Tech Notes cover more direct/native ways to manipulate 4D Write Pro objects and process expressions server-side, reducing reliance on the `EVALUATION_METHOD`/`PROCESS_EXPRESSIONS` wrapper pattern shown here.

Developers building document-generation pipelines today should consult current 4D Write Pro documentation for expression handling APIs, but the underlying idea — that 4D Write Pro documents can be fully manipulated as objects without a form — remains valid and is the modern norm.
