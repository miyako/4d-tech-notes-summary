# Tech Note 02-16: BasicStamp

- **Asset ID:** 23251
- **Tech Note #:** 02-16
- **Published:** April 30, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Pascal Pradier
- **Page URL:** https://kb.4d.com/assetid=23251
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_15-19_(APR)/02-16_BasicStamp.hqx

## Overview

Pascal Pradier (Program Manager, 4D S.A.) shows how to interface 4D with a Parallax BasicStamp II microcontroller and a Dallas DS1620 temperature sensor over a serial (RS-232) connection, covering both real-time data acquisition and EEPROM-buffered asynchronous acquisition.

## Key Points

- Hardware chosen for simplicity: the BasicStamp II (programmable in BASIC, 16 programmable I/O pins, 2KB EEPROM, RS-232 interface, under $50) and the Dallas Semiconductor DS1620 temperature sensor, which requires no external components and has its own instruction set (can act as sensor, thermostat, or do on-the-fly conversion).
- Real-time acquisition on the 4D side: a background process is created with `New process("recept";32000;"Recept";"vide")`, the serial port is opened with `SET CHANNEL(1;Speed 9600+Data bits 8+Stop bits One+Parity None)`, and a `While` loop calls `RECEIVE BUFFER($vtBuffer)` continuously, creating and saving a `[Table 1]` record with `Num($vtBuffer)` whenever data arrives.
- On the BasicStamp side, the PBASIC program initializes 16 I/O pins with the reserved words `outs`/`dirs`, uses `High 1` to trigger the DS1620's reset pin, and uses `Shiftout`/`Shiftin` with `lsbfirst` byte order to send the value 238 (a DS1620 "convert on the fly" instruction) and read back the converted temperature, streaming a data frame via `Debug` over RS-232 to 4D roughly once per second.
- Flags a practical weakness of the real-time approach: creating one record per second is heavy; recommends accumulating readings into a size-limited BLOB and periodically deleting obsolete records instead.
- Describes an alternate asynchronous acquisition strategy where the BasicStamp stores readings in its own EEPROM and 4D interrupts the microcontroller only periodically (e.g. weekly or monthly) to retrieve the accumulated data via a subroutine, trading real-time visibility for reduced continuous 4D-side load.
- Concludes that 4D can interface easily with simple microcontrollers like the BasicStamp, though integration complexity grows with more complex communication protocols.

## Featured Technology

- SET CHANNEL (serial port configuration)
- RECEIVE BUFFER (serial data acquisition)
- New process for background serial listening
- Parallax BasicStamp II microcontroller (BASIC/PBASIC)
- Dallas Semiconductor DS1620 temperature sensor
- RS-232 serial communication

## Historical Commentary

**Status:** Historical interest only

This note demonstrates 4D acting as a real-time serial data-acquisition host, using SET CHANNEL and RECEIVE BUFFER in a dedicated process to continuously read temperature readings streamed once per second over RS-232 from a Parallax BasicStamp II microcontroller wired to a Dallas DS1620 sensor. It is a niche but genuine hardware-integration example: real-time acquisition (poll a serial buffer in a loop, insert a record per reading) versus asynchronous/batch acquisition (store readings in the BasicStamp's onboard EEPROM and retrieve them periodically). The specific BasicStamp II hardware and its RS-232-based integration approach are now dated — modern microcontroller projects favor USB/Wi-Fi/BLE-connected boards (Arduino, ESP32, Raspberry Pi) often bridged through MQTT/HTTP/REST rather than raw serial polling from the host application — but 4D's own SET CHANNEL/RECEIVE BUFFER serial commands are still present and usable for legacy RS-232 hardware integrations today.

References to newer/updated information:
- The BasicStamp II and raw RS-232 polling approach shown here have been largely superseded in modern hardware projects by USB/Wi-Fi/BLE microcontrollers (Arduino, ESP32, Raspberry Pi) integrated via MQTT, HTTP, or REST rather than direct serial buffer polling
- 4D's SET CHANNEL and RECEIVE BUFFER commands for serial port I/O still exist in current 4D versions for legacy RS-232 device integration
