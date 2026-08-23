# Tech Note: Exploring the Loan Tool Database

- **Asset ID:** 16395
- **Tech Note #:** 01-38
- **Published:** August 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jonathan Baltazar, 4D, Inc. Technical Support Engineer
- **Page URL:** https://kb.4d.com/assetid=16395
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_36-40_(AUG)/01-38_Loan_Tool_Database.hqx

## Overview

Jonathan Baltazar (4D, Inc. Technical Support Engineer) explores the Loan Tool example database by Tad Michael Wheeler (DataCraft), which solves for loan amount, payment, interest rate, or term length using standard amortization math, including an iterative convergence loop for interest rate and a MOVE OBJECT-based UI trick that repositions a shared result field over whichever input is currently unknown.

## Key Points

- The main input form's 4x1 button grid (vSector object method) toggles which of loan amount, payment, interest rate, or term length is being solved for; the selected button disables its own field and repositions a shared vResult display over it using MOVE OBJECT, so one form layout serves all four modes.
- LoanTool_RecalculateLoan computes an Effective Interest Rate (Annual Rate / Compounding Periods / 100) and Periodic Discount Factor (1/(1+rate)) common to all four cases, then applies the standard amortization formula algebraically to solve directly for loan amount or payment.
- When interest rate is the unknown, LoanTool_ClosestInterestRate can't invert the formula algebraically, so it computes low/high theoretical bounds and runs a 10-iteration convergence loop to approximate the effective rate (falling back to a 0% rate with an adjusted payment if the theoretical bounds go negative).
- Term length (in years or months, per a Term As Years or Months boolean) is solved via a closed-form logarithmic formula: Total Payments = -Log(1-(Amount*Rate/Payment))/Log(1+Rate).
- A separate "Quick Entry" form and LoanTool_CalculatePayment method offer a condensed, single-purpose payment calculator (Loan Amount, Interest Rate, Compounding Periods, Term, Term Basis in → Payment out) built on the same amortization math, useful when only a payment estimate is needed.
- The example database is built atop the reusable "Simple Shell" framework (Shell_Startup, Shell_PROCESS_LSpawnProcess, Shell_GEN_ModifySelection) shared across several 4D example databases of the era to give them a consistent UI shell.

## Featured Technology

- Amortization math: effective interest rate, periodic discount factor, payment formula
- Iterative interest-rate solver (LoanTool_ClosestInterestRate convergence loop)
- 4-way button-grid UI toggling calculation mode
- MOVE OBJECT for dynamically repositioning/resizing form fields
- Simple Shell example-database framework (Shell_Startup, Shell_PROCESS_LSpawnProcess)

## Historical Commentary

**Status:** Partially Superseded

This note walks through the Loan Tool example database (by Tad Michael Wheeler of DataCraft), which lets a user solve for any one of loan amount, payment, interest rate, or term length using standard amortization formulas, including an iterative convergence loop to approximate the interest rate when it's the unknown, plus a UI trick using MOVE OBJECT to reposition the calculated-value field over whichever input was deselected. The amortization math and iterative-solver technique are timeless and still valid in any language; the specific 4D implementation (Simple Shell process-spawning framework, MOVE OBJECT-based dynamic form layout) reflects classic-language, non-compiled-mode UI patterns of the era that have been partly superseded by modern 4D form objects, list boxes, and dynamic form management, though the core financial calculations remain directly reusable.

References to newer/updated information:
- The amortization formulas and iterative interest-rate solver shown are timeless math and remain directly usable in any current 4D version
- The Simple Shell process-spawning framework and manual MOVE OBJECT layout tricks reflect classic-language UI patterns that modern 4D form objects, list boxes, and forms JS/widget-based UIs have largely superseded
