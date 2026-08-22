# Tech Note 09-06: File Transfers using Execute on Server

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** February 11, 2009 | **Product/Version:** 4D v11.2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75177
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_05-08-(FEB)/09-06_Server_File_Transfers.zip

## Proposition
Explains 4D v11 SQL Release 2's new Execute on Server method property and applies it to a practical use case — a chunked file-transfer system (GFFS) for pulling documents from a 4D Server machine down to clients regardless of file size or network location.

## Key Points
- **Property vs. command:** the Execute on Server command always spawns a new process; the method property instead runs in a "twin" process of the calling client, with parameters and dereferenced pointer values synchronized automatically in both directions.
- **Stored-procedure restrictions:** methods with Execute on Server checked follow the same rules as stored procedures — interface/dialog commands should not be used.
- **GFFS overview:** lets any connected 4D Client download files from a server-defined folder hierarchy (`<>gffs_DocRoot`), independent of geographic location, up to 2GB per file.
- **Chunked transfer protocol:** files larger than `<>gffs_FileLimit` are split using `READ PACKET` on the server, each returned blob carrying custom header bytes (multipart flag, chunk number, total chunks) so the client reassembles them via `SEND PACKET` in a loop.
- **File Browser sample:** a GUI for browsing shared folders/files, viewing folder sizes, and downloading with pause/cancel support and automatic cleanup of partial downloads.
- **Type/creator reset:** downloaded files have their Mac type/creator codes reset to prevent auto-opening in the creating application.

## Featured Technology
- Execute on Server method property (4D v11 SQL Release 2), a 'twin process' alternative to the Execute on Server command
- GFFS (Get Files from Server) sample: chunked BLOB file transfer using READ PACKET/SEND PACKET
- Manual multipart BLOB protocol with custom header bytes for chunk numbering
- 4D Client/Server automatic parameter and dereferenced-pointer synchronization

## Best Practices Highlighted
1. Avoid interface/dialog commands in any method with the Execute on Server property checked, since it runs in a stored-procedure-like context.
2. Check file size before initiating a transfer and branch into a chunked protocol only when needed, rather than always transferring in one piece.
3. Run file transfers in their own process so users can pause/cancel without blocking the rest of the application.
4. Clean up partially downloaded files if a transfer is cancelled.

## Context / Positioning
Written to spotlight a developer-facing simplification (the Execute on Server method property) newly added in 4D v11 SQL R2, using file transfer as a concrete, high-value illustration of when and how to apply it.

## Historical Commentary
**Status:** Partially Superseded

The Execute on Server method property described here remains a current, unchanged 4D Server feature for delegating method execution to the server side of a Client/Server application.

However, the GFFS sample's hand-rolled chunked-BLOB transfer protocol — manually tagging blobs with header bytes for multipart reassembly — was a workaround for the practical limits of client/server data transfer at the time. 4D's client/server networking and document/blob handling have improved substantially since 2009, and REST server + ORDA (4D v16 R5+, 2017) now offers an additional modern channel for moving files and data between tiers, making the specific GFFS implementation a technique of historical rather than current best-practice interest.
