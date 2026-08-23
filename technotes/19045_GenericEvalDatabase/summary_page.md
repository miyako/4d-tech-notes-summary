# Tech Note: Under the Hood of the GenericEval Database

- **Asset ID:** 19045
- **Tech Note #:** 01-49
- **Published:** October 30, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Raymond Manley, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=19045
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_46-49_(OCT)/01-49_GenericEval_Database.hqx

## Overview

Raymond Manley (4D, Inc.) explains how the GenericEval database configures its own schema at runtime, parsing machine-readable [***Tag***] pairs out of incoming POP3 email into a generic 100-field table and using an alias-mapping table to relabel fields and tables with human-readable names in forms and the Query Editor.

## Key Points

- Table2 starts out as 100 generic text fields (Field1..Field100); a web registration form emails its submission as an [***Tag***] Value-delimited plain-text message to a POP3 holding mailbox, following the convention established in the companion note TN 01-36.
- MAIL_ProcessEMails, spawned as a background process on a configurable interval (default 15 minutes), logs into POP3 (POP3_Login/POP3_BoxInfo/POP3_GetMessage), scans each message for [***...***] tag pairs, and for each unseen tag creates a zStructure record assigning it to the next available generic field.
- GET FIELD PROPERTIES checks whether a target field has already been manually retyped (Alpha/Text, LongInt/Real/Integer, Date, Time, Boolean) so incoming plain text is coerced (Num, Date, Time, or a True/1/Yes boolean test) before being written via a resolved field pointer.
- ALIAS_DeployAliases reads zStructure's AliasName/AliasOrder columns and calls SET TABLE TITLES/SET FIELD TITLES so the generically-named Table2/Field7/etc. display as friendly labels like "Registrations"/"Date Purchased" throughout the UI, including the Query Editor.
- Processed messages are deleted from the mail server with POP3_Delete after each batch, and aliases are redeployed at the end of each run so newly-discovered tags are reflected immediately.
- The note explicitly notes the technique generalizes beyond email as the data source, as long as some other process supplies similarly tagged text.

## Featured Technology

- POP3_Login/POP3_GetMessage/POP3_Delete email retrieval
- Generic Table2 of 100 text fields (Field1..Field100)
- Machine-readable [***Tag***] parsing of email bodies
- GET FIELD PROPERTIES for runtime type detection
- SET TABLE TITLES / SET FIELD TITLES dynamic field/table aliasing
- zStructure alias-mapping table

## Historical Commentary

**Status:** Still Relevant

This note is the second half of a two-part series (following TN 01-36's generic web form mailer by Kent Wilbur) and explains how the GenericEval database polls a POP3 mailbox, parses incoming [***Tag***]-delimited email bodies into a generic 100-field Table2, and uses a zStructure alias table plus SET TABLE TITLES/SET FIELD TITLES to relabel those generic fields with human-readable names and retype them as needed. The general problem -- building a flexible, self-configuring data store from tagged input without knowing the schema in advance -- is still a real design challenge today, but a modern 4D implementation would represent this dynamic data with objects/collections or ORDA dynamic attributes rather than pre-allocating 100 generic text fields and aliasing them after the fact.

References to newer/updated information:
- 4D's object and collection data types (introduced circa 4D v14-16) offer a more natural way to store dynamically-tagged, schema-flexible data than a fixed pool of generically-named fields
- ORDA's dynamic attributes give an alternative to hand-rolled field-aliasing logic like the zStructure table used here
