# Tech Note 26-04: Semantic Icon Search in 4D Using AI and Vector Embeddings

**Author:** Karim Meghraoui, Technical Services Engineer, 4D Morocco
**Published:** April 23, 2026 | **Product/Version:** 4D v21HF2 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79986
**Download:** https://kb.4d.com/TN/2026/26-04_SematicIconSearch.zip

## Proposition
Traditional icon search relies on exact keyword matching against tags/names — an icon tagged
"robot automation machine" won't surface for a search of "automated system," even though the
concepts are related. This note demonstrates how to replace that with **semantic search**:
converting both stored content and user queries into vector embeddings, then ranking results by
conceptual similarity rather than literal word overlap.

## Key Points
- **Embeddings as first-class data.** Each icon entity stores a `4D.Vector` field alongside its
  name, picture, and tags. The vector is generated once (during a "vectorization" phase) from the
  icon's tag text using OpenAI's `text-embedding-ada-002` model via the 4D AI Kit, and persisted —
  avoiding repeated API calls at query time.
- **Native vector queries in ORDA.** Similarity search is a single ORDA query:
  `ds.Icon.query("vector >= :1 order by vector desc", {vector: ...; metric: mk cosine; threshold: ...})`.
  ORDA computes cosine similarity directly against stored vectors and returns ranked results.
- **Hybrid search strategy.** Two search modes are demonstrated: (1) dynamic search, where a
  free-text query is embedded on the fly via OpenAI and compared to stored vectors; (2) local
  search, where a few predefined "quick" buttons reuse precomputed embeddings with no new API
  call. This balances flexibility against API cost/latency.
- **Secure, non-persistent API key handling.** The OpenAI key is stored only in a shared `Storage`
  object for the session (not written to disk/config), entered via a dialog pre-filled from memory,
  demonstrating a lightweight credential-handling pattern for demos (with a caveat that production
  apps need stronger persistence/security).
- **Presentation via ListBox.** Ranked results (name, picture, similarity score) are pushed into an
  object array and rendered in a 4D ListBox, which handles sorting by name or score with no extra
  code.
- **Generalizable pattern.** The author explicitly notes this technique extends beyond icon
  libraries to document repositories, knowledge bases, media libraries, and product catalogs —
  anywhere conceptual/fuzzy retrieval beats exact keyword match.

## Featured Technology
- **4D AI Kit** — simplified interface to OpenAI services (embeddings) from 4D code.
- **4D.Vector** — native vector data type for entity fields.
- **ORDA** — vector-aware `.query()` with `mk cosine` similarity metric and threshold filtering.
- **OpenAI Embeddings API** (`text-embedding-ada-002`) — converts text to semantic vectors.
- **4D Storage / shared objects** — in-memory, non-persistent credential storage.
- **4D ListBox** — built-in sorting/display of scored results.

## Best Practices Highlighted
1. *Vectorize once, use many* — precompute and store embeddings; don't recompute per query.
2. *Hybrid search* — mix dynamic (OpenAI) and local (precomputed) vector lookups to cut API cost.
3. *Extendable architecture* — the same pattern applies well beyond icon search.

## Context / Positioning
Published under 4D v21HF2 (2026), this note sits within a cluster of contemporaneous Tech Notes
on AI integration (4D AI Kit, tool calling, ORDA events) — reflecting 4D's current push toward
first-class AI/ML support (vector types, embedding APIs, agentic tool calling) built on top of its
long-standing ORDA data-access layer.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it, e.g. "superseded by TN 22-11 which
uses the built-in X instead of the manual Y workaround shown here.")*
