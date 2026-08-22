# Tech Note 01-38: Exploring the Loan Tool Database

**Author:** Not specified in source
**Published:** August 31, 2001 | **Product/Version:** 4D v6.7 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=16395
**Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/Windows/TN_2001_36-40_(AUG)/01-38_Exploring_Loan_Tool.exe (dead link — see Historical Context)

## Overview

Only a short teaser paragraph for this Tech Note survives in this archive; the full PDF and its companion example database could not be
recovered. The complete text of the surviving teaser is reproduced below:

> The Loan Tool is an intermediate example database written by Tad Michael Wheeler of DataCraft. The Loan Tool database allows the user to calculate the amount of money they can afford to borrow, the type of payment (weekly, monthly, yearly, etc.), the interest rate of the loan, and the length of time it will take to pay off the loan. Once either of theses amounts has been calculated, the user can then set up their payment details by entering the date the user will be make their first payment. The Payment Details displays the due date, start balance, payment, principal, interest, cumulative interest, and ending balance for each payment date. The Quick Entry part of the demo will calculate the payment after entering the necessary information. Basically, the Quick Entry is the same as the main input form, however it does not break down the information into as much detail.

## Key Points

Based on the available teaser text, this note is: a walkthrough of the Loan Tool example database's loan/amortization calculator.

## Featured Technology

- Amortization/loan calculation logic
- Example database (Tad Michael Wheeler, DataCraft)
- Form-based financial calculators

## Historical Context

Published August 2001 for 4D v6.7, this note dates from the "4D 2001"/"4D 2000-2001" product era (the v6.5/v6.7/v6.8 lineage),
running on classic Mac OS 9 (with Mac OS X newly released in 2001) and Windows 98/2000/NT. This was years before Project Mode
(introduced 4D v17, 2018), ORDA (2018+), and 4D's own SQL engine (introduced 4D v11 SQL, ~2007) existed — development happened entirely
in binary Design Mode (.4DB/.4DC structure files) using the classic procedural/set-based 4D language.

The full archive for this note could not be recovered: the linked download was an old Windows self-extracting .exe installer that could
not be extracted in this environment (error_reason: `NO_PDF_IN_ARCHIVE_TEASER_ONLY`), so this page is necessarily based only on the short
teaser paragraph published on the Tech Note's web page, not the full PDF or its companion example database.

**Status: Still relevant**

This note walks through the Loan Tool example database, an intermediate-level demo that calculates borrowing capacity, payment schedules, and amortization details (principal, interest, cumulative interest, ending balance) from user-entered loan parameters. The underlying financial/amortization math and the general pattern of a form-driven calculator remain timeless and directly portable to a modern 4D application, even though the specific 2001-era form design and Design Mode structure shown are dated.

**What has changed since:**

- The amortization/loan-calculation logic itself is unchanged math and remains directly reusable
- Modern equivalents would present the same calculator using a Project Mode form and possibly a List Box or web/ORDA-based front end instead of the 2001-era UI
