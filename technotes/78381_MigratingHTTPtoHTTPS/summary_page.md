# Tech Note 19-23: 4D Migrating from HTTP to HTTPS

**Author:** Sofia BACKEIKH, Quality Support Engineer, 4D Morocco
**Published:** December 30, 2019 | **Product/Version:** 4D v17 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78381
**Download:** https://kb.4d.com/DLTN/TN/2019/19-23_HTTP2HTTPS.pdf

## Proposition
As HTTPS became a baseline expectation for all websites (driven by browser warnings and SEO impact), this note explains HTTPS/TLS fundamentals and walks through the concrete steps to enable HTTPS on a 4D Web Server.

## Key Points
- **Three pillars of HTTPS**: authentication (prevents man-in-the-middle attacks), encryption (protects data from eavesdroppers), and data integrity (detects tampering).
- **Hybrid encryption model**: HTTPS uses asymmetric encryption to establish a session key, then symmetric encryption for the bulk data exchange.
- **Certificate fundamentals**: digital certificates bundle a public key, owner info, metadata, and a CA's digital signature; validation levels are Domain, Organization, and Extended Validation; scope types are single-domain, multi-domain, wildcard, and multi-domain wildcard.
- **4D file placement**: `cert.pem`/`key.pem` go next to the database structure file (binary mode) or project folder (project mode), or must be manually copied to the resources folder on remote machines in remote mode.
- **Database Settings**: HTTPS is enabled via a checkbox on the Web/Configuration tab, with a configurable HTTPS port (default 443) that must be checked for conflicts.
- **Seven-step rollout checklist**: confirm HTTP works → obtain a CA certificate → verify port/file placement → check firewall → enable HTTPS setting → run over HTTPS → validate the secure connection.

## Featured Technology
- TLS/SSL (successor relationship, asymmetric + symmetric encryption)
- 4D Web Server HTTPS configuration (`cert.pem`, `key.pem`)
- `WEB SEND HTTP REDIRECT` (referenced for redirecting HTTP to HTTPS)

## Best Practices Highlighted
1. Keep the private key (`key.pem`) confined to the server machine and never share it.
2. Choose a non-default HTTPS port only after confirming it isn't already in use.
3. Validate firewall rules explicitly allow external access to the chosen HTTPS port before going live.

## Context / Positioning
Published as browsers increasingly flagged non-HTTPS sites and search engines weighted HTTPS in rankings, this note reflects 4D's ongoing effort to keep developers current on web security baselines applicable to any 4D-published web application, not just niche 4D-specific features.

## Historical Commentary
**Status:** Still relevant

Both halves of this note remain accurate today: the general HTTPS/TLS/certificate concepts are unchanged fundamentals of web security, and the 4D-specific configuration steps (placing `cert.pem`/`key.pem`, enabling HTTPS in Database Settings) are still exactly how TLS is configured for a 4D Web Server in current versions. If anything, the industry has only reinforced HTTPS-by-default practices since 2019 (e.g., broader HSTS adoption, free-certificate ecosystems like Let's Encrypt becoming mainstream), so this note's guidance remains directly applicable with no meaningful superseding changes.
