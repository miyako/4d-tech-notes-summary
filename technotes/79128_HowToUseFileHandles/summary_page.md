# Tech Note 23-04: How to Use File Handles

**Author:** Shayanna Gatchalian, Technical Services Engineer, 4D Inc.
**Published:** February 23, 2023 | **Product/Version:** 4D v19 R7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79128
**Download:** https://kb.4d.com/DLTN/TN/2023/23-04_FileHandles.zip

## Proposition
4D's classic file-handling commands (OPEN DOCUMENT, RECEIVE/SEND PACKET, CLOSE DOCUMENT) are functional but verbose and error-prone — especially the requirement to manually close files, which can lock them until a restart if forgotten. 4D v19 R7's new FileHandle object provides a cleaner, object-oriented way to read and write file content, including line-by-line access.

## Key Points
- **Classic file-handling steps:** `OPEN DOCUMENT` → position via `SET/GET DOCUMENT POSITION` → read via `RECEIVE PACKET` (count or stopChar) or write via `SEND PACKET` → manually `CLOSE DOCUMENT` (or risk a locked file).
- **New FileHandle pipeline:** create a `File` object → call `.open()` in read/write/append mode to get a `FileHandle` → use dedicated read/write functions → the handle auto-closes when dereferenced or the process ends.
- **Line-aware I/O:** `.readLine()`/`.writeLine()` natively account for Mac/Windows end-of-line differences, unlike the old `stopChar`-based approach.
- **Three read functions:** `.readLine()`, `.readText()`, `.readBlob()`; three write functions: `.writeLine()`, `.writeText()`, `.writeBlob()`.
- **Offset tracking:** the `.offset` property is readable/settable and defaults differently per mode (start of file for read/write, end of file for append).
- **Whole-file shortcuts unaffected:** `Document to text`/`TEXT TO DOCUMENT`/`DOCUMENT TO BLOB`/`BLOB TO DOCUMENT` (no File object) and `.getText()`/`.setText()`/`.getContent()`/`.setContent()` (with a File object) perform identically for full-content operations.
- **Multiple simultaneous handles:** unlike the classic single-context document open, several file handles (read, write, append) can operate independently on the same file, each tracking its own offset.
- **Companion Folder object:** mirrors File's properties/functions and adds `.files()`, `.folders()`, `.file()`, `.folder()` for directory traversal, needed to build up File/FileHandle-based logic.

## Featured Technology
- **4D.FileHandle class** — new v19R7 object providing read/write/append modes with offset tracking and no manual close.
- **4D.File class** — v17R5 object representing a file on disk; the basis for creating a FileHandle via `.open()`.
- **4D.Folder class** — companion object for directory traversal and file/folder discovery.
- **RECEIVE PACKET / SEND PACKET (legacy)** — the classic packet-based commands FileHandle is designed to supersede.

## Best Practices Highlighted
1. Prefer FileHandle's `.readLine()`/`.writeLine()` over manual `stopChar` parsing to correctly handle cross-platform line endings.
2. Let FileHandle auto-close by dereferencing it (set to null) or letting the owning process terminate, rather than relying on manual close commands prone to being forgotten.
3. Use multiple independent FileHandle instances (read/write/append) when a workflow needs to read and write the same file concurrently, instead of manually juggling a single document's offset.

## Context / Positioning
Released with 4D v19R7, FileHandle continues 4D's broader migration from legacy procedural/packet-based commands toward modern, object-oriented, dot-notation APIs (File, Folder, and now FileHandle), aligning file I/O with the rest of 4D's evolving class-based standard library.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose practical value has diminished — and, where applicable, cross-references the newer/updated Tech Note, 4D version, or feature that replaced or improved on it.)*
