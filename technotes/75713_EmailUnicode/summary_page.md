# Tech Note 09-17: Sending and Receiving E-Mails in Unicode

**Author:** Keisuke Miyako, 4D Japan
**Published:** April 30, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75713
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_13-17_(APR)/09-17_email_unicode.zip

## Proposition
This note explains how 4D v11 SQL's newly Unicode-capable 4D Internet Commands let developers send and receive e-mail across many languages/character sets with relative ease, grounding the practical guidance in a clear explanation of e-mail's underlying MIME encoding standards.

## Key Points
- **The 7-bit legacy:** e-mail was designed for US-ASCII; MIME encodings exist to safely transport extended characters, images, and binaries over that legacy transport.
- **Quoted-Printable** suits mostly-Latin-alphabet text with occasional special characters; **base64** suits non-Latin scripts (Chinese, Korean, Japanese) and binary attachments; **7bit/8bit** are used for already-compatible encodings.
- 4D v11 SQL's Internet Commands newly support koi8-r, ISO-8859-15, EUC-KR, Big-5, GB2312, and UTF-8, in addition to previously supported encodings — without needing to change the system language as a workaround.
- Documents the **encoding/decoding capabilities and limitations** of the `Setprefs`/`Charset` commands and UTF-8 handling.
- Covers **dissecting multipart-content e-mails** and provides worked base64/Quoted-Printable encode/decode examples.
- Bundled **4D Email Tools component** demonstrates sending, receiving, editing, and viewing Unicode-capable messages end to end.

## Featured Technology
- 4D Internet Commands (4D v11 SQL, Unicode-capable)
- MIME email encoding (Quoted-Printable, base64, 7bit, 8bit)
- Character set conversion (UTF-8, ISO-8859-x, Shift-JIS, ISO-2022-JP, EUC-KR, Big-5, GB2312, koi8-r)
- 4D Email Tools component (send/receive/edit/view messages)

## Best Practices Highlighted
1. Understand the underlying MIME/character-set model before relying on automatic encoding, since certain encodings remain unsupported and require manual handling.
2. Use base64 rather than Quoted-Printable for predominantly non-Latin-script content to avoid excessive, unreadable escaping.
3. Test multipart-content e-mail handling explicitly, since dissecting multipart messages has its own nuances beyond simple header/body encoding.

## Context / Positioning
Published to help developers take advantage of 4D v11 SQL's newly internationalized Internet Commands, this note gave both the conceptual grounding (email/MIME standards) and concrete component code needed to build genuinely international e-mail features, particularly valuable for a global 4D developer community.

## Historical Commentary
**Status:** Still Relevant

This note explained how 4D v11 SQL's newly Unicode-capable 4D Internet Commands could send and receive email across many character sets, replacing older tricks like temporarily switching the system language. The email protocol fundamentals (MIME, Quoted-Printable/base64 encoding, character set handling) described here are timeless internet standards and remain entirely accurate.

The specific 4D Internet Commands and Email Tools component have continued to evolve since (with further internationalization refinements in later 4D versions), but the conceptual grounding this note provides is still directly useful to any developer implementing internationalized email in 4D today.
