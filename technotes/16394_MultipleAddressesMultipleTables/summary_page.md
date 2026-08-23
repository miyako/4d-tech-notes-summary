# Tech Note: Linking Multiple Addresses to Multiple Tables

- **Asset ID:** 16394
- **Tech Note #:** 01-37
- **Published:** August 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Steve Hussey, CEO, Alto Stratus LLC
- **Page URL:** https://kb.4d.com/assetid=16394
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_36-40_(AUG)/01-37_Multiple_Addresses.hqx

## Overview

Steve Hussey (CEO, Alto Stratus LLC) shows how to attach multiple addresses to records across several unrelated tables (Contact, Doctor, etc.) using a single shared Address table keyed by table number and parent-record ID, with no 4D relations defined at all, so one address subform and one set of methods serve every parent table.

## Key Points

- Contact, Doctor, and any future parent tables each have their own indexed, unique ID field; the shared Address table carries Table_ID (the parent table's numeric table number) and Contact_ID (the parent record's ID value) as its two key fields, with no formal 4D relation defined between any of the tables.
- ADRS_Ld(pointerToTable;ContactID) uses Table($1) to derive the calling form's table number, then QUERYs [Address] on Table_ID and Contact_ID together and sorts the resulting selection by Date_From, so the same method works unmodified from any parent table's form.
- The Contact/Doctor detail form's On Load event assigns a fresh Sequence number([...]) ID to new records and calls ADRS_Ld to populate the address subform each time a record is loaded.
- ADRS_Add creates a new [Address] record, stamps it with Table($1) and the parent's ID, saves it, then reloads the address selection via ADRS_Ld -- necessary because, without a defined relation, there's no automatic "Add Subrecord" behavior to rely on.
- Despite no relation existing, the address subform's Delete button can still use the automatic Delete Subrecord action, because 4D tracks the currently selected record within the subform's active selection regardless of how that selection was built.
- The same Table_ID/foreign-key pairing technique is explicitly suggested for other repeating child data types shared across multiple parent tables, such as email addresses, phone/fax numbers, or to-do/action items.

## Featured Technology

- Table($1) to derive a table number from a form's parent table pointer
- Relationless polymorphic linking via Table_ID + Contact_ID key fields on an Address table
- Address subform reused across Contact and Doctor detail forms
- Delete Subrecord automatic action without a defined relation
- Sequence number() for unique per-record IDs across multiple tables

## Historical Commentary

**Status:** Still Relevant

Steve Hussey (Alto Stratus LLC) demonstrates linking one Address table to multiple unrelated parent tables (Contact, Doctor, etc.) without defining any 4D relations at all -- instead storing a Table_ID (from Table($1)) and a Contact_ID key on each address record and querying by both, which lets the same address subform and add/delete logic be reused across every contact-type table in the database. This relation-free, polymorphic-association pattern for one-to-many-across-many-tables data is still a legitimate and commonly needed design in 4D today; classic-language projects still use exactly this key-pair technique, though ORDA-based projects would more likely model it with related dataclasses/entity selections or a dedicated many-to-many relation defined in the data model instead of manual QUERY-based joins.

References to newer/updated information:
- The Table_ID/Contact_ID polymorphic key-pair technique shown here is still used as-is in classic-language 4D projects that need one child table shared across several parent tables
- ORDA-based projects can alternatively model this kind of shared relationship through the data model's relation attributes rather than manual QUERY-based table/ID matching
