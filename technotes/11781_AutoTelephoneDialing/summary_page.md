# Tech Note: Automatic Telephone Dialing from 4D

**Author:** Not specified
**Published:** January 1, 1998 | **Product/Version:** 4D v6.0 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=11781

## Overview
This Tech Note shows how to automatically dial a telephone number from a 4D database using a Hayes-compatible modem, the SET CHANNEL command (for serial port access), and the SEND PACKET command (for sending AT modem commands).

## Key Points
- **SET CHANNEL:** Opens a serial port connection to the modem.
- **SEND PACKET:** Sends Hayes AT commands to initiate dialing.
- **Hayes-compatible modem required:** The technique relies on standard AT command set.
- **Practical benefit:** Saves time and prevents misdialed numbers in CRM-style applications.
- **Non-standard modems:** Advises consulting documentation for modems that don't conform to Hayes standards.

## Featured Technology
- SET CHANNEL command (serial port communication)
- SEND PACKET command (data transmission)
- Hayes-compatible modem AT command set
- Serial port hardware integration from 4D

## Historical Context
**Status:** Historical interest only

This note is a fascinating snapshot of late-1990s computing, when external modems connected via serial ports were standard office equipment and auto-dialing from a database was a genuine productivity feature. The SET CHANNEL command used for serial communication has been deprecated in modern 4D. The entire paradigm of modem-based telephone dialing is obsolete — modern telephony integration would use VoIP protocols, cloud telephony APIs (like Twilio), or system-level telephony frameworks. The note does, however, illustrate the breadth of hardware integration that 4D's serial communication commands once enabled.

The full PDF could not be recovered — the original page has no working download link (NO_DOWNLOAD_LINK_TEASER_ONLY). This summary is based solely on the on-page teaser text.
