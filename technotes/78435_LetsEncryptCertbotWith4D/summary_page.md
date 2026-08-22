# Tech Note 20-05: Let's Encrypt CERTBOT with a 4D Web Server

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** March 25, 2020 | **Product/Version:** 4D v18 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78435
**Download:** https://kb.4d.com/DLTN/TN/2020/20-05_LetsencryptCertbotWith4D.pdf

## Proposition
The ACME protocol update broke 4D's earlier custom Let's Encrypt component (from tech notes 16-17/17-01). This note replaces it with Certbot, the official Let's Encrypt/EFF client, showing installation on both macOS (Homebrew) and Windows 10 (WSL/Ubuntu) and how to wire its output into a 4D Web Server's TLS configuration.

## Key Points
- **Protocol churn drove the switch**: rather than maintaining a bespoke ACME component that would break again with future protocol changes, 4D recommends the officially maintained Certbot tool.
- **macOS installation**: via Homebrew (`brew install letsencrypt`, `brew upgrade certbot`).
- **Windows installation**: via Windows Subsystem for Linux running Ubuntu, since Certbot targets Unix-like systems.
- **Webroot challenge**: `certbot certonly` prompts for the 4D Web Server's WebFolder path so Certbot can place the HTTP-01 challenge file where the 4D web server can serve it.
- **Certificate handoff**: Certbot's `fullchain.pem`/`privkey.pem` must be copied into the 4D database folder as `cert.pem`/`key.pem`, followed by `WEB SERVER STOP`/`WEB SERVER START` to apply.
- **Renewal**: `certbot renew` handles renewal (certs expire every 90 days); the note also covers building a renewal script and common webroot/startup error pitfalls.

## Featured Technology
- Certbot / Let's Encrypt ACME client
- 4D Web Server TLS configuration (`cert.pem`, `key.pem`)
- Homebrew, Windows Subsystem for Linux

## Best Practices Highlighted
1. Prefer an externally, actively maintained ACME client (Certbot) over an in-house component subject to protocol drift.
2. Double-check the exact WebFolder path when prompted, as an incorrect webroot causes the HTTP-01 challenge to fail.
3. Automate `certbot renew` via a scheduled script to avoid manual 90-day renewal cycles.

## Context / Positioning
This note reflects 4D's pragmatic shift away from maintaining its own small utility components for fast-moving external protocols, instead pointing developers to the authoritative open-source tool — a sensible long-term sustainability move given how often ACME/Certbot itself has evolved since.

## Historical Commentary
**Status:** Still relevant

Certbot remains the standard, actively maintained tool for obtaining free Let's Encrypt certificates, and the general workflow (obtain cert with Certbot → place cert.pem/key.pem next to the 4D database → enable HTTPS in Database Settings → restart the web server) is still exactly how TLS is configured for a 4D Web Server today. Certbot's own command-line details have evolved somewhat since 2020 (newer plugin options, updated interactive prompts), so an exact reproduction of every screen shown may differ slightly, but the core integration pattern with 4D remains valid and is still commonly recommended.
