# Tech Note 08-32: Using Match regex to Import CSV data

**Author:** Charles Vass (Technical Services Team Member, 4D Inc.)  
**Published:** September 4, 2008 | **Product/Version:** 4D v11.2 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=50956  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_32-35_(SEP)/08-32_Match_regex.zip

## Overview

This Technical Note addresses a long-standing data integration challenge: efficiently importing Comma-Separated Values (CSV) files into 4D databases. Prior to 4D v11 SQL, CSV parsing required extensive custom code to handle CSV's surprisingly complex edge cases. The introduction of the Match regex command in 4D v11 SQL provides a powerful pattern-matching tool that simplifies CSV parsing from dozens of lines of conditional string manipulation to a concise regular expression definition and a small parsing method.

## Key Points

**Why CSV Still Matters**
- Despite being a legacy format predated by XML, CSV remains the de facto standard for data exchange in financial software, spreadsheet applications, and legacy systems
- Billions of lines of legacy code worldwide continue to depend on CSV import/export functionality
- iPhone applications and modern enterprise systems still frequently use CSV for data transfer
- Financial reporting and data analysis workflows often mandate CSV support alongside modern formats

**CSV Complexity**
Simple field parsing (split by comma) fails when:
- Fields contain embedded commas (e.g., "New York, NY")
- Fields contain double-quote characters (e.g., "John ""The Boss"" Doe")
- Fields span multiple lines (e.g., multi-line notes or addresses)
- Fields have leading/trailing spaces that must be preserved

**CSV Rules (Complete Specification)**
1. Fields are separated by commas
2. Fields containing commas, quotes, or line breaks must be enclosed in double-quotes
3. Embedded double-quotes are represented as consecutive double-quote pairs ("" represents a single ")
4. A CSV record may span multiple lines if the entire record is enclosed in quotes
5. The first record may optionally be a header row with column names
6. Fields may always be delimited with double-quotes; delimiters are always discarded
7. Leading/trailing spaces are significant only inside quoted fields

**Regular Expression Approach**
- Traditional parsing: character-by-character iteration with complex conditional logic for each edge case
- Regex approach: define three patterns that cover all valid CSV field formats:
  - Pattern 1: Quoted string optionally followed by comma
  - Pattern 2: Unquoted string optionally followed by comma
  - Pattern 3: Empty field optionally followed by comma
- Match regex can identify and extract each field using a single pattern definition

**Practical Impact**
- Without regex: comprehensive CSV parsing typically requires ~12+ lines of complex string manipulation code per field
- With regex: same functionality achieved with 2-3 lines using a single regex pattern
- Dramatically reduces debugging complexity and code maintenance burden

**Sample Method**
The note includes a working 4D method that:
1. Accepts a complete CSV record as input
2. Uses Match regex to parse fields according to CSV specification
3. Returns parsed fields as an array
4. Handles all CSV edge cases (quoted fields, embedded commas, line breaks, etc.)

**Limitations of Other Approaches**
- Manual field splitting by comma alone fails for quoted fields
- Excel and some spreadsheet tools strip leading/trailing spaces even when CSV specifies they should be preserved
- Some CSV writers violate the specification, requiring application-level normalization

## Featured Technology

- Match regex command
- Regular expressions
- CSV parsing patterns
- Comma-Separated Values data format
- Pattern-based field extraction
- Data import automation

## Historical Context

Published in September 2008, this note reflects a significant capability addition to 4D v11 SQL: native regular expression support via the Match regex command. At the time, regex support was a major feature enabling 4D developers to tackle text processing and data validation tasks that previously required custom algorithmic code. The note positions regex as a practical tool for solving real-world data integration problems that 4D developers encountered regularly.

## Historical Commentary

**Status:** Still Relevant

While CSV remains a legacy format and modern data integration increasingly favors REST APIs and JSON payloads, CSV import continues to be a necessary capability in enterprise applications, particularly in financial services, ERP systems, and data analytics. The Match regex command and the regex patterns described in this note continue to work in all modern versions of 4D (through ORDA and current releases). However, dedicated CSV libraries and standardized CSV parsing frameworks have become ubiquitous across all platforms, and many developers today would reach for a purpose-built CSV library rather than implement regex-based parsing from scratch. The conceptual value of this note—demonstrating how powerful pattern matching can simplify complex parsing tasks—remains valid even if the specific implementation is no longer the first choice for most new CSV import projects.
