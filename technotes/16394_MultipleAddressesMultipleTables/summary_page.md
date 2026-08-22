# Tech Note 01-37: Linking Multiple Addresses to Multiple Tables

**Author:** Not specified in source
**Published:** August 31, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=16394
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_36-40_(AUG)/01-37_Multiple_Addresses.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> Early contact databases usually had a fixed number of fields defined to store a single address. Later, many databases were modified to store perhaps two addresses per contact record (often a billing and shipping address).

Today it is common for a contact to perhaps have more than one address, for example it is common in the USA to have both a mailing address and a physical address. Some individuals may also have addresses that are valid at different times (home, college etc.).

This technical note explains a simple method for attaching multiple addresses to a contact record. It can also be used to allow the address table to be linked to multiple contact type tables in a database. The code and form objects can easily be copied and pasted to new forms and form methods as they are defined.

## Key Points

Based on the available teaser text, this note is: a technique for linking multiple addresses to one or more contact-type tables.

## Featured Technology

- Classic one-to-many table relations
- Reusable form objects/methods

## Historical Context

Published August 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Partially superseded**

This note presents a simple relational pattern for attaching multiple addresses (and multiple address types, e.g. home/billing/shipping) to a contact record, and for reusing an Address table across several contact-type tables, via copy-and-paste form objects/methods. The general one-to-many relational modeling concept is still exactly how you would design this in 4D today, but the copy-and-paste, hand-wired reuse technique of the classic era has been superseded by ORDA's entity-based relations and 4D's later component/class mechanisms for sharing reusable UI logic.

**What has changed since:**

- ORDA's entity relations (introduced 4D v17+) provide a more structured way to model one-to-many address relationships
- 4D classes/components now offer better code-reuse mechanisms than copy-pasting form objects and methods between forms
