# Tech Note 16-17: ACME Client Component for 4D - Part I

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** October 28, 2016 | **Product/Version:** 4D v15.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77671
**Download:** https://kb.4d.com/DLTN/TN/2016/16-17_ACMEClientComponent.zip

## Proposition
This tech note introduces the 4D-ACME-Client, an open-source 4D component implementing the ACME protocol to obtain free Domain Validated TLS certificates from Let's Encrypt for a 4D Web Server, giving developers a self-contained path to enabling HTTPS without a paid certificate authority.

## Key Points
- **Why HTTPS:** unencrypted HTTP traffic is trivially interceptable; HTTPS provides end-to-end encryption users increasingly expect.
- **What Let's Encrypt is:** a free, automated, browser-trusted certificate authority run by ISRG in collaboration with the Linux Foundation, governed by the IETF-drafted ACME protocol.
- **90-day certificates:** short duration is by design, intended to be handled through automated renewal rather than manual reissue.
- **DV vs OV vs EV certificates:** Let's Encrypt issues only Domain Validated (DV) certificates; Organization Validated (OV) and Extended Validation (EV, the historical "green bar") require more identity verification than Let's Encrypt performs.
- **Component architecture:** communicates via JSON Web Signature (JWS) objects over HTTPS using a special Base64 URL-safe encoding.
- **Public methods:** `ACME_Auto_Cert` (main automation entry point), `ACME_well_known_challenge` (handles the domain-authorization HTTP challenge in `On Web Connection`), and `ACME_Show_GUI` (interactive certificate creation/renewal UI).
- **Usage paths:** both a GUI for manual operation and a scriptable method suitable for unattended automation are provided.

## Featured Technology
- ACME (Automated Certificate Management Environment) protocol
- Let's Encrypt Certificate Authority
- 4D-ACME-Client open-source component (with public GitHub repository)
- JSON Web Signature (JWS) over HTTPS
- Base64 URL-safe encoding

## Best Practices Highlighted
1. Automate certificate renewal rather than relying on manual reissue, given Let's Encrypt's 90-day certificate lifetime.
2. Choose certificate validation level (DV/OV/EV) based on actual trust requirements — Let's Encrypt is appropriate only when DV-level validation suffices.

## Context / Positioning
Published October 2016 for 4D v15.x, this note reflects the mid-2010s push (led by Let's Encrypt, launched publicly in 2015-2016) toward free, ubiquitous HTTPS across the web, applied specifically to 4D's own web server. It predates 4D's Project Mode and ORDA, sitting within the classic Design Mode era of 4D web development.

## Historical Commentary
**Status:** Partially superseded

4D later added native Let's Encrypt/ACME certificate support directly into 4D Server's administration settings, making this hand-built, open-source component no longer the primary path most developers would use to obtain a certificate — though it remains functional and a genuinely instructive worked example of implementing ACME from first principles in 4D.

The certificate concepts explained here — DV vs. OV vs. EV validation, the 90-day Let's Encrypt lifetime, and the rationale for automated renewal — are all still accurate today and have not changed since 2016, making the conceptual half of this note more durable than its specific implementation.
