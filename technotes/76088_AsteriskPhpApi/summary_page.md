# Tech Note 10-13: Asterisk and 4D via PHP in v12

**Author:** Timothy Aaron Penner, Technical Services Team Member, 4D Inc.
**Published:** April 23, 2010 | **Product/Version:** 4D v12 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=76088
**Download:** https://kb.4d.com/DLTN/TN/2010/Windows/TN_2010_11-14_(APR)/10-13_Asterisk-PHP-API.zip

## Proposition
This note shows how to integrate 4D v12 with the open-source Asterisk PBX/VoIP telephony platform by using 4D v12's new PHP scripting bridge to drive the Asterisk-PHP-API PEAR library, which in turn talks to Asterisk's Management Interface (AMI) — enabling call center-style features like queue management, SIP peer listing, and call origination directly from 4D.

## Key Points
- **4D v12 PHP architecture:** the PHP EXECUTE command runs PHP over FastCGI (as if invoked by an HTTP server), with PHP SET OPTION/PHP GET OPTION for interpreter configuration and PHP GET FULL RESPONSE for stdout, error, and HTTP header retrieval.
- **Asterisk overview:** a free, GPL-licensed, widely used open-source telephony/PBX server (also embedded in distributions like Trixbox, Elastix, and PBX-In-A-Flash).
- **Asterisk Management Interface (AMI):** a control protocol enabled and configured via `/etc/asterisk/managers.conf`, including its own user accounts and privilege groups.
- **Asterisk-PHP-API library** (by Doug Bromley, BSD-licensed, distributed via PEAR) wraps AMI calls into PHP functions.
- **Demonstrated operations:** listing/managing call queues, listing SIP/IAX peers and parked calls, originating calls, running arbitrary Asterisk CLI commands, and listing/inspecting channel status.
- **Companion example database** exposes each AMI operation through a demo form for hands-on exploration.

## Featured Technology
- PHP EXECUTE / PHP SET OPTION / PHP GET OPTION / PHP GET FULL RESPONSE (4D v12 PHP integration)
- Asterisk open-source PBX / VoIP telephony server
- Asterisk Management Interface (AMI)
- Asterisk-PHP-API PEAR library (by Doug Bromley)
- FastCGI-based PHP interpreter bridge in 4D v12

## Best Practices Highlighted
1. Configure AMI users and privilege groups deliberately in `managers.conf` rather than using default/open credentials.
2. Use PHP GET FULL RESPONSE to capture detailed error/script/line information when PHP-based AMI calls fail.
3. Wrap third-party PEAR libraries (like Asterisk-PHP-API) behind 4D method wrappers rather than calling PHP functions ad hoc throughout application code.

## Context / Positioning
Published shortly after 4D v12 introduced PHP scripting, this note showcased a practical, high-value real-world integration (telephony/PBX control) enabled by that new capability, targeting developers building call-center or click-to-dial features.

## Historical Commentary
**Status:** Partially Superseded

This note used 4D v12's brand-new PHP Execute/FastCGI bridge to reach a third-party PEAR library (Asterisk-PHP-API) that wraps the Asterisk Management Interface (AMI) for PBX/VoIP integration — telephony integration itself remains a real-world need, but routing it through 4D's PHP interpreter and an unreleased/beta PEAR package was always a fragile, indirect path.

Since then, 4D has added far more capable native networking (TCP/UDP commands, native JSON/HTTP support) and the wider VoIP ecosystem has shifted toward REST/webhook-based telephony platforms, making a direct AMI socket connection or a modern REST-based VoIP API a more idiomatic integration path today than shelling out to PHP for this purpose.
