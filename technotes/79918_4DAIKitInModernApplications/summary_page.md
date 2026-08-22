# Tech Note 26-01: Using 4D AIKit in Modern 4D Applications

**Author:** Soukaina BACHIKH, Customer Success Engineer, 4D Inc.
**Published:** January 29, 2026 | **Product/Version:** 4D v21 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=79918
**Download:** https://kb.4d.com/TN/2026/26-01_AIKitInModernApp.zip

## Proposition
For 4D developers, integrating powerful AI services (text generation, vision, image creation) has
historically meant managing external dependencies and complex infrastructure. 4D AIKit, a
built-in component since 4D 20 R9, provides a native, unified interface to OpenAI and
OpenAI-compatible providers, and this note establishes the architectural foundations —
configuration, message handling, async patterns, cost/security practices — for building on it.

## Key Points
- **Three functional areas under `cs.AIKit`.** Text generation/chat (`OpenAIChatCompletionsAPI`),
  vision/image analysis (`OpenAIVision`/`OpenAIVisionHelper` for OCR, object detection, visual
  Q&A), and image generation (`OpenAIImagesAPI`, e.g. via `dall-e-3`).
- **Unified client entry point.** `cs.AIKit.OpenAI.new("api-key"; $config)` accepts an optional
  config object (`model`, `temperature`, `maxTokens`, `timeout`) and works across any supported
  OpenAI-compatible provider.
- **Message-role-based conversation context.** Conversations are built as collections of
  `{role; content}` objects (`system` sets behavior/context, `user` carries queries, `assistant`
  holds prior AI replies), preserved across turns to maintain state.
- **Structured error handling.** Every API call returns a `$result.success` flag; on failure,
  `$result.errors` is an `OpenAIError` collection with detailed messages, avoiding silent failures.
- **Centralized singleton configuration.** An `AIConfig` shared singleton class, instantiated in
  `On Startup` (`cs.AIConfig.me`), centralizes API keys, model preferences, and defaults as a
  single source of truth.
- **Async via worker processes for multi-process cases.** AIKit's native callback-based async
  pattern only works within the calling process; multi-process UIs must dispatch AI calls through
  `CALL WORKER` or `CALL FORM` and poll for results to keep the UI responsive.
- **Demo architecture (Demo-AIKit).** `DocumentAnalyzer` (GPT-4o vision extraction),
  `SummaryGenerator` (GPT-4o-mini summarization into brief/detailed/executive/key-points
  formats), and `ConversationManager` (document-aware chat) each encapsulate one AI domain,
  backed by a Document/ExtractedData/Summaries/Conversation schema.
- **Cost-aware model selection.** Reserve GPT-4o for vision/complex reasoning; use the
  cheaper GPT-4o-mini for routine summarization and chat, and set `maxTokens` to bound
  response length/cost.

## Featured Technology
- **`cs.AIKit.OpenAI`** — main client class for authentication/configuration.
- **`OpenAIChatCompletionsAPI`** — `chat.completions.create()` for multi-turn text generation.
- **`OpenAIVisionHelper`** — `chat.vision.fromFile()` + `.prompt()` for document/image analysis.
- **`OpenAIImagesAPI`** — `images.generate()` for text-to-image generation.
- **`OpenAIError`** — structured error object surfaced on failed API calls.
- **`CALL WORKER` / `CALL FORM`** — multi-process async dispatch for long-running AI calls.

## Best Practices Highlighted
1. *Organize AI logic by class, one domain per class* — improves testability and maintainability.
2. *Centralize configuration in a singleton, loaded at startup* — avoids scattered credential
   handling across the app.
3. *Never embed API keys in code or version control* — use secure config files, environment
   variables, or encrypted storage, with separate keys per environment.
4. *Optimize for token cost* — pick the cheapest sufficient model, trim prompts, and always set
   `maxTokens`.

## Context / Positioning
Published as TN 26-01 at the start of 2026, this note serves as the foundational reference for
4D's broader AI Kit initiative that year, underpinning subsequent, more specialized notes on
semantic vector search and OpenAI tool calling — reflecting 4D's strategic push to make
LLM/vision integration a native, first-class capability rather than a bolt-on requiring external
infrastructure.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
