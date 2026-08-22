# Tech Note 25-11: TCP Communication, Data Exchange Methods: Creating a Messaging System

**Author:** Olivier Marolleau, Quality Support Engineer, 4D France.
**Published:** November 29, 2025 | **Product/Version:** 4D v21 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79882
**Download:** https://kb.4d.com/TN/2025/25-11_4DMessenger.zip

## Proposition
TCP is essential for reliable client-server and inter-application data exchange, but its
low-level implementation is complex — especially now that 4D's legacy TCP commands and the
4D Internet Commands plugin are deprecated. This note demonstrates the modern replacement,
`TCPListener` and `TCPConnection`, by building a simplified but functional peer-to-peer
messaging application supporting text, images, video, and file transfer.

## Key Points
- **Peer-to-peer, no central server.** Each user runs the application as both a `TCPListener`
  (reception) and `TCPConnection` (transmission) endpoint, referencing other users by IP address
  in a local "nodes" list and grouping recipients into named "channels."
- **Web Area as the universal display/input surface.** A single web area, "zMessInput," handles
  both composing (drag-and-drop of files up to a 64MB cap, configurable in `input.js`) and
  rendering sent/received messages via HTML injected through `WA EXECUTE JAVASCRIPT FUNCTION`
  calls into `input.js`/`output.js`, styled by dedicated CSS files.
- **Compact custom binary framing.** Each network request is a BLOB: a 4-byte size, a 32-byte
  structure hash, then encrypted content (routing code, sender, recipient(s), timestamp, message
  ID, JSON "cargo"), packed/unpacked by a dedicated `Lib_Messenger_Net_Request` class
  (`requestPack`/`requestUnPack`).
- **Hash-guarded encryption.** `Encrypt data BLOB`/`Decrypt data BLOB` alone can't detect a wrong
  passphrase (it silently "decrypts" to garbage) or reliably strip padding; embedding the original
  structure size and an MD5 digest before encryption lets `requestUnPack` validate the decrypted
  content and correctly resize away the padding.
- **Address-validated connection acceptance.** `Lib_Messenger_Net_Input.onConnection` checks the
  incoming socket address against the configured "nodes" preference list before handing the
  connection to a `Lib_Messenger_Stream` instance that accumulates incoming bytes until the
  declared size arrives.
- **Byte-level acknowledgment protocol.** After receiving a full message, the receiver sends back
  a single-byte code — `0x1` (message received, triggers `CALL FORM` to update the sender's UI)
  or `0x2` (icon-request reply, followed by the icon's binary data) — over the same connection.
- **Per-machine JSON preferences.** Username, encryption key, listen address/port, avatar, node
  list, and channels persist to `Data/Messenger/<machineName>.json`, managed by a
  `Lib_Messenger_Preferences` class loaded at startup.

## Featured Technology
- **`4D.TCPListener`** — modern class for accepting inbound TCP connections, replacing legacy TCP
  commands.
- **`4D.TCPConnection`** — modern class for outbound TCP connections and data transmission.
- **`Encrypt data BLOB` / `Decrypt data BLOB`** — built-in BLOB encryption commands, used with a
  custom hash-validation layer.
- **Web Area + `WA EXECUTE JAVASCRIPT FUNCTION`** — rich multi-media message composition/display
  bridge between 4D and embedded HTML/JS/CSS.
- **MD5 digest (`Generate digest`)** — validates successful decryption and correct padding
  removal.

## Best Practices Highlighted
1. *Never trust `Decrypt data BLOB` alone to signal failure* — always pair it with an embedded
   hash/size check, since a wrong key decrypts "successfully" into garbage rather than erroring.
2. *Encapsulate binary (de)serialization in one class* — centralizing `requestPack`/`requestUnPack`
   in `Lib_Messenger_Net_Request` keeps wire-format changes isolated and maintainable.
3. *Validate peer identity before processing a connection* — checking the incoming address against
   a known-nodes list in `onConnection` prevents processing data from unreferenced sources.

## Context / Positioning
Published for 4D v21 (late 2025), this note documents the practical migration path from
deprecated legacy TCP commands and the 4D Internet Commands plugin to the modern
`TCPListener`/`TCPConnection` classes, reflecting 4D's ongoing modernization of its native
networking stack alongside other 2025–2026 notes on UDP sockets and system-worker-based process
integration.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
