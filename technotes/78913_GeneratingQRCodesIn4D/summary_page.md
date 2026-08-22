# Tech Note 22-07: Generating QR Codes in 4D (Revised on Aug 4th, 2023)

**Author:** Nhat Do, Technical Services Engineer, 4D Inc.
**Published:** April 26, 2022 | **Product/Version:** 4D v19 R | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=78913
**Download:** https://kb.4d.com/DLTN/TN/2022/22-07_GenerateQRCode_r2.zip

## Proposition
Since 4D has no built-in QR code generator, this note demonstrates using a Web Area and a JavaScript library to produce QR codes for URLs, vCard contacts, emails, and phone numbers, either rendered live or converted to a static picture.

## Key Points
- **No native QR command**: 4D relies on an external JavaScript library (qr-code-styling) rendered inside a Web Area.
- **PROCESS 4D TAGS / $4DTEXT**: used to inject 4D data (text, base64 images) into the HTML template before display.
- **Two output modes**: live display in a Web Area via WA OPEN URL, or conversion to a static picture via an offscreen Web Area.
- **vCard format**: BEGIN:VCARD/VERSION/N/EMAIL/TEL/ADR/END:VCARD used to encode contact-adding QR codes.
- **Offscreen area + OffscreenArea class**: captures canvas.toDataURL() output via WA EXECUTE JAVASCRIPT FUNCTION, then BASE64 DECODE + BLOB TO PICTURE convert it to a 4D picture.
- **Customization**: logo images, dot shapes, and dimensions are all configurable via the JS library's options object.
- **Reusable method**: getQRPicture(text) -> picture, ready to embed anywhere a QR picture is needed.

## Featured Technology
- Web Area
- PROCESS 4D TAGS / 4DTEXT tags
- qr-code-styling JavaScript library
- WA EXECUTE JAVASCRIPT FUNCTION
- BASE64 DECODE / BLOB TO PICTURE

## Best Practices Highlighted
1. Bundle the JavaScript library locally so QR generation works offline.
2. Use vCard formatting rules strictly (BEGIN/VERSION first, END last) to ensure phone compatibility.
3. Prefer the offscreen-area + picture-conversion approach when the QR code needs to be stored, printed, or emailed rather than just viewed.

## Context / Positioning
This note fits 4D's ongoing pattern of empowering developers to combine native 4D code with modern web technology through the Web Area component, rather than adding narrow built-in features for every possible use case — a pragmatic 'bring your own JS library' philosophy that predates and postdates this specific note.

## Historical Commentary
**Status:** Still Relevant

The technique is still current and commonly used; the Web Area / PROCESS 4D TAGS / WA EXECUTE JAVASCRIPT FUNCTION toolchain has not changed materially in 4D since this was published, and there's still no native QR-generation command in 4D. The fact that 4D itself revised this note in 2023 (per its title) to fix the download link suggests continued developer interest and validity. Developers today would follow the same approach, possibly swapping in a different or newer JS QR library, but the underlying 4D mechanics remain accurate.
