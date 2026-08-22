# Tech Note 17-01: ACME Client Component for 4D - Part II

**Author:** Timothy Aaron Penner, Senior Technical Services Engineer, 4D Inc.
**Published:** January 19, 2017 | **Product/Version:** 4D v15.x | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77708
**Download:** https://kb.4d.com/DLTN/TN/2017/17-01_ACMEClientComp_Part2_R2.zip

## Proposition
This is the second half of a two-part tech note extending the 4D-ACME-Client component (introduced in TN 16-17) that obtains free Let's Encrypt TLS certificates for a 4D Web Server. Part II adds certificate-expiration-checking utilities and reworks internal implementation details to be thread-safe under 4D v16's Preemptive Web Server.

## Key Points
- **KEYS_get_expiration:** returns the ISO-format expiration date of the certificate currently in use, checking the appropriate location depending on whether it runs on 4D Server or 4D Client.
- **KEYS_cert_expires_in_x_days:** returns True if the certificate expires within N days (or doesn't exist), enabling a simple automated renewal-check loop that avoids Let's Encrypt rate limits given the 90-day certificate lifetime.
- **Thread-safety rewrite:** domain authorization and the well-known-challenge handler were rewritten to use disk files instead of Inter-Process Variables, making them compatible with 4D v16's Preemptive Web Server.
- **Base64 URL-safe encoder updates:** both the text and blob encoder methods gained decode capability in addition to encode.
- **GUI enhancements:** the certificate's expiration status is now shown color-coded (green = safe, red = expiring soon or missing) both on load and after a renewal run.
- **New Account Key option:** a checkbox lets the user force regeneration of the ACME account key, useful when a prior registration attempt left it in a bad state.

## Featured Technology
- ACME (Automated Certificate Management Environment) protocol
- Let's Encrypt Certificate Authority
- 4D-ACME-Client open-source component
- 4D v16 Preemptive Web Server
- Base64 URL-safe encoding

## Best Practices Highlighted
1. Check certificate expiration proactively (e.g., "expires within 30 days") rather than waiting for expiry, to stay within Let's Encrypt rate limits.
2. Avoid Inter-Process Variables for anything that must work correctly under a preemptive (multi-threaded) web server — use disk-based files instead.

## Context / Positioning
Published January 2017 targeting 4D v15.x/v16, this note reflects the transitional period when 4D introduced its Preemptive Web Server, requiring existing web-server-adjacent code (like this ACME client) to be reworked away from thread-unsafe constructs. It predates Project Mode and ORDA, sitting in the classic binary-database era of 4D development.

## Historical Commentary
**Status:** Partially superseded

4D subsequently added native, built-in Let's Encrypt/ACME certificate management directly into 4D Server's administration settings, which is now the standard, supported way most 4D developers obtain and renew TLS certificates — making this hand-built component largely unnecessary for typical use cases today.

The component remains available on GitHub and still functions as a working example of implementing ACME protocol logic and certificate lifecycle checks in 4D, and the underlying concepts (DV/OV/EV certificate types, 90-day Let's Encrypt lifetimes, rate-limit-aware renewal) are all still accurate. But for production use, native 4D features or standard reverse-proxy tooling (e.g., Caddy, certbot) would be the more current choice.
