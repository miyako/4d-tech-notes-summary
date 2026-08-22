# Tech Note 25-12: UDP Sockets: Peer-to-Peer Communication

**Author:** Anouar Moustarih, Quality Support Engineer, 4D Morocco
**Published:** December 22, 2025 | **Product/Version:** 4D v20 R10 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79895
**Download:** https://kb.4d.com/TN/2025/25-12_UPDPeerToPeer.zip

## Proposition
Peer-to-peer systems need a way for application instances on the same network to find each
other without a central rendezvous server — useful for collaborative desktop tools, local sync
services, and distributed applications. This note shows how UDP's connectionless,
broadcast-friendly nature, combined with 4D's `UDPSocket`/`UDPEvent` classes (new in 4D 20 R10),
supports a complete, dependency-free peer discovery mechanism.

## Key Points
- **Dual-socket design.** Each `PeerDiscovery` instance owns a `listener` (bound to the discovery
  port, default 54321) and a `sender` (ephemeral port) `4D.UDPSocket`, both created inside a
  worker process via `CALL WORKER("p2pworker"; ...)` and synchronized back with a `4D.Signal`.
- **Three message types.** `ANNOUNCE` (self-description broadcast), `PROBE` (request for others to
  re-announce), and `BYE` (graceful departure) are JSON-encoded, converted to Blob, and sent to
  the broadcast address `255.255.255.255`.
- **Event-driven reception.** `onData($socket; $event : 4D.UDPEvent)` parses incoming JSON,
  ignores self-originated messages, and routes by `type` to `addOrRefreshPeer`, a `PROBE` reply,
  or `removePeerById` for `BYE`.
- **TTL-based peer pruning.** Peers are stored in a shared collection with a `lastSeen` timestamp;
  a default 90-second TTL (`peerTTL`) automatically expires stale entries so the peer list stays
  accurate without explicit disconnect handling.
- **Background worker loop.** `RunPeerDiscovery` runs in its own process, alternating
  `sendProbe()`/`prunePeers()` on a signal-gated interval, publishing the current peer list and
  log text into `Storage` for the UI process to read.
- **Shared-object safety throughout.** All cross-process state (`peers`, `myInfo`, `logText`) uses
  `New shared object`/`New shared collection` with `Use()...End use` blocks to guard concurrent
  access between the discovery worker and the UI.
- **UI-friendly timestamp formatting.** `Util_formatLastSeen` converts raw millisecond timestamps
  into "N seconds/minutes/hours ago" strings for listbox column expressions.

## Featured Technology
- **`4D.UDPSocket`** — low-level UDP socket creation for both listening and sending.
- **`4D.UDPEvent`** — event object delivered to `onData` with the received datagram and sender
  address/port.
- **`4D.Signal`** — cross-process coordination for worker initialization and shutdown.
- **`CALL WORKER`** — dedicated worker process hosting the sockets and the discovery loop.
- **Shared objects/collections** — safe cross-process state sharing (`Storage.peers`,
  `Storage.logText`).
- **UDP broadcast (`255.255.255.255`)** — decentralized presence discovery with no rendezvous
  server.

## Best Practices Highlighted
1. *Use TTL pruning instead of explicit disconnect tracking* — peers age out automatically,
   tolerating crashes or network drops without special-casing them.
2. *Send a graceful `BYE` on shutdown* — reduces "ghost" peer entries even though TTL alone would
   eventually clean them up.
3. *Isolate sockets in a dedicated worker process* — keeps UDP I/O off the UI process and enables
   true asynchronous, event-driven communication.

## Context / Positioning
Published for 4D v20 R10 (late 2025), this note showcases the still-relatively-new
`UDPSocket`/`UDPEvent` classes as a foundation for native, serverless networking patterns in 4D,
complementing the platform's growing native-networking toolkit (alongside TCP messaging and
System Workers) without requiring external libraries or infrastructure.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
