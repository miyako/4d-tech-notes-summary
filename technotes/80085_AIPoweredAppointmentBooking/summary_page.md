# Tech Note 26-08: AI-Powered Appointment Booking with Tool Calling in 4D AIKit

**Author:** Soukaina Bachikh, Customer Success Engineer, 4D Inc.
**Published:** August 19, 2026 | **Product/Version:** 4D v21 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=80085
**Download:** https://kb.4d.com/TN/2026/26-08_BookingWithAI.zip

## Proposition
Traditional chatbot logic in business apps relies on the developer anticipating every phrasing a
user might type — matching keywords and hand-coding intent detection — which breaks on typos,
synonyms, and multi-turn context, and doesn't scale as capabilities grow. This note shows how
"tool calling" (OpenAI's function-calling mechanism) delegates intent recognition and argument
extraction to the LLM itself, using a demo clinic-booking application, demoAPT, as the working
example.

## Key Points
- **Tools as JSON Schema.** Each callable action (checkAvailability, createAppointment,
  cancelAppointment, etc. — twelve total) is defined with `cs.AIKit.OpenAITool.new()`, giving a
  name, a model-facing description, and a parameters schema (types, required fields, expected
  formats like `YYYY-MM-DD`).
- **Synchronous request/dispatch loop.** A browser posts one message per turn to
  `/rest/$catalog/chat` (an ORDA REST-exposed `chat` function); `APT_WebChat_RunTurn` calls
  `chat.completions.create(...; {stream: False})`, routes any `finish_reason: "tool_calls"`
  response through `APT_Tool_Dispatch`, appends the JSON result as a `role: "tool"` message, and
  repeats up to 6 rounds before returning the final reply.
- **Two front doors, one business logic.** The same `APT_Tool_*` ORDA methods are called both by
  the AI dispatcher and directly by a native Admin form for clinic staff, guaranteeing the AI and
  staff workflows can never fall out of sync.
- **Sequencing via descriptions.** Preconditions like "findClient must be called first" (before
  createAppointment) are embedded directly in the tool description text, since that description is
  the model's only signal for correct sequencing.
- **Multi-tool chaining and proactive suggestions.** Tools like `getWeekAvailability` are described
  to encourage the model to proactively suggest alternate slots instead of just reporting failure,
  and results can be rendered as clickable `<slots>` buttons in the chat UI.
- **Manual dispatch vs. `registerTools()`.** demoAPT dispatches manually via `APT_Tool_Dispatch`
  rather than using AIKit's built-in `registerTools()`/`handler` convenience, specifically because
  business methods must also be directly callable from the Admin form.
- **Hard safety caps.** The tool-calling loop is capped at 6 rounds per visitor turn to prevent a
  confused model from looping indefinitely on a single HTTP request.

## Featured Technology
- **4D AIKit (`cs.AIKit.OpenAI`, `cs.AIKit.OpenAITool`)** — unified OpenAI-compatible client and
  tool-definition class.
- **OpenAI Chat Completions API / tool calling** — `finish_reason: "tool_calls"`, `role: "tool"`
  messages.
- **ORDA** — indexed queries powering each tool's business logic (Staff, Client, Appointment,
  Availability, Conversation tables).
- **4D built-in Web Server / REST** — `/rest/$catalog/chat` endpoint and `fetch()`-based
  webchat.html client.
- **Provider configuration file** (`Resources/AIProvider.json`) — runtime-configurable, gitignored
  credential storage.

## Best Practices Highlighted
1. *One tool, one responsibility* — keep actions like cancel vs. reschedule as separate tools so
   model choice is unambiguous.
2. *Write descriptions for the model, not the developer* — descriptions are the sole signal used
   for tool selection and sequencing.
3. *Cap tool-calling loops explicitly* — even server-side, to avoid runaway request cycles.
4. *Never trust stale system state* — refresh the system prompt (date, rules) every turn rather
   than relying on what was cached when a conversation began.

## Context / Positioning
Published under 4D v21 (2026) alongside several other AI Kit-focused notes (semantic search, ORDA
events, AIKit fundamentals), this note reflects 4D's ongoing push to make agentic AI patterns
(tool/function calling) a first-class, well-documented capability built directly on ORDA and the
built-in web server, rather than something developers must wire up from raw HTTP calls.

## Historical Commentary
**Status:** current — N/A, too recent for hindsight assessment.

*(This section is populated as older notes are processed, going backward through history. It flags
APIs/patterns that are now deprecated, technology superseded by later 4D features, or content whose
practical value has diminished — and, where applicable, cross-references the newer/updated Tech
Note, 4D version, or feature that replaced or improved on it.)*
