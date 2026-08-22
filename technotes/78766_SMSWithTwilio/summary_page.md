# Tech Note 21-14: Sending & Receiving SMS in 4D with Twilio

**Author:** Bryan Yen, Technical Services Engineer, 4D Inc.
**Published:** August 26, 2021 | **Product/Version:** 4D v19 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78766
**Download:** https://kb.4d.com/DLTN/TN/2021/21-14_SMSIntegrationWithTwilio.zip

## Proposition
SMS is a valuable feature for business apps — 2FA, reminders, notifications. This note shows how to integrate Twilio's programmable SMS platform into 4D for both outbound sends and inbound reply handling, using either PHP or 4D's own native HTTP commands.

## Key Points
- **Twilio account setup:** obtaining an Account SID, Auth Token, and a trial phone number with SMS capability.
- **Two send paths:** PHP + Twilio's PHP Helper Library (via Composer), or 4D's native `HTTP Request` / `HTTP AUTHENTICATE` calling the Twilio REST endpoint directly — no external language runtime required.
- **HTTP Basic auth to Twilio:** `HTTP AUTHENTICATE(...; HTTP basic)` combined with a POST to `https://api.twilio.com/2010-04-01/Accounts/{SID}/Messages`.
- **ngrok for local webhook testing:** since the 4D web server is normally only reachable on localhost, ngrok exposes it publicly so Twilio can deliver inbound SMS webhooks during development.
- **Inbound handling via On Web Connection:** replies are captured with `WEB GET VARIABLES` and can trigger an automated response by returning TwiML (Twilio Markup Language) content.
- **Four working demos:** simple send, two-factor authentication code flow, appointment scheduling with reminders, and full bidirectional reply logging.
- **Cross-platform PHP install guidance** for both Windows and macOS is documented as a prerequisite for the PHP-based demos.

## Featured Technology
- Twilio REST API (Messages resource)
- `HTTP Request`, `HTTP AUTHENTICATE`
- 4D web server / `On Web Connection`, `WEB GET VARIABLES`, `WEB SEND FILE`
- ngrok tunnel
- PHP + Composer + Twilio PHP Helper Library (alternate path)

## Best Practices Highlighted
1. Use HTTP Basic auth with `HTTP AUTHENTICATE` for REST APIs that require it, rather than manually building Authorization headers.
2. Use ngrok (or an equivalent tunnel) to test inbound webhooks against a local development 4D web server.
3. Respond to Twilio webhooks with well-formed TwiML to control automated reply behavior.

## Context / Positioning
Published as one of a wave of "connect 4D to a popular SaaS API" tech notes (alongside OAuth2/Gmail and mailing notes from this era), this reflects 4D's positioning of its native HTTP/web-server stack as sufficient for building real integrations with third-party cloud services without needing external middleware, while acknowledging that some developers still prefer PHP-based bridges.

## Historical Commentary
**Status:** Still relevant

The fundamentals here — calling a REST API with 4D's native `HTTP Request`/`HTTP AUTHENTICATE` commands, and handling inbound webhooks in `On Web Connection` — remain the standard, still-current approach for third-party API integrations in 4D. Nothing about the Twilio REST API pattern shown has been deprecated. The PHP-based demo path is the more dated half of this note: with 4D's HTTP commands fully capable of the same job, introducing PHP, Composer, and a separate language runtime is largely unnecessary friction that a developer today would likely skip in favor of the direct REST calls shown in Demos 3 and 4.
