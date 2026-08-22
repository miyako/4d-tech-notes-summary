# Tech Note 98-14: Communicating via a serial port with 4D

**Author:** Not specified in source document
**Published:** March 1, 1998 | **Product/Version:** 4D v6.0 | **Platform:** Mac &amp; Win
**Page:** https://kb.4d.com/assetid=11797
**Download:** https://kb.4d.com/ftp://partner:54yTK3y86xBf@ftp.4d.com/Partners_Only/ACI_TECHNICAL_NOTES/Windows/TN_1998_08-10_(MAR)/98-09_Serial_Port_Comm.exe

## Proposition
This Tech Note provides a method for managing serial port communication in 4th Dimension, handling both transmission and reception of textual data of any size.

## Key Points
- Provides a reusable method for serial port data transfer
- Handles variable-size file transmission and reception
- Uses 4D's built-in serial communication commands (SET CHANNEL, SEND PACKET, RECEIVE PACKET)
- Example database provided for both Windows and Macintosh platforms

## Featured Technology
- Serial Port Communication
- 4th Dimension
- SET CHANNEL
- SEND PACKET
- RECEIVE PACKET

## Context / Positioning
Serial ports were standard hardware interfaces in the late 1990s. 4D's ability to communicate via serial ports was important for integrating with barcode scanners, laboratory instruments, POS systems, and other peripheral devices.

## Historical Commentary
**Status:** Obsolete

Serial port communication was a common hardware integration method in the late 1990s but has been almost entirely replaced by USB, Bluetooth, and network-based protocols. 4D's SET CHANNEL command for serial I/O was eventually deprecated. Modern 4D developers would use system workers, plugins, or external process calls for hardware communication.

---
*Note: The full PDF/archive for this Tech Note could not be recovered — the linked file is an old Windows self-extracting .exe installer that cannot be extracted in this environment. This summary is based solely on the on-page teaser paragraph.*
