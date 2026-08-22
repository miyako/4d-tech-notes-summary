# Tech Note 05-45: 4D for OCI: Error Handling

**Author:** Josh Fletcher, Technical Support Engineer, 4D Inc.
**Published:** December 22, 2005 | **Product/Version:** 4D Oracle (2004) | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=41109
**Download:** https://kb.4d.com/DLTN/TN/2005/Windows/TN_2005_40-46_(DEC)/05-45_4D_for_OCI_Errors.zip

## Overview
This note describes the two error-handling techniques available in the 4D for OCI plug-in, which gives 4D applications native Oracle client connectivity via the Oracle Call Interface (OCI), and includes a sample database demonstrating both.

## Key Points
- **Standard error handling:** manually check the return code of every 4D for OCI call (e.g., OCI_SUCCESS, OCI_ERROR, OCI_INVALID_HANDLE, OCI_NEED_DATA, OCI_STILL_EXECUTING, OCI_CONTINUE) and branch accordingly — full control, more code.
- **4D error handling:** install a centralized handler with `OCIOnErrCall("MethodName")`, similar in spirit to 4D's `ON ERR CALL` — less code, less granular control per call.
- **Error handles:** most OCI calls take an error handle used to retrieve one or more error records via `OCIErrorGet`, looping by record number until `OCI_NO_DATA` is returned.
- **Custom handler:** the note provides a full reusable `My_OCI_Error_Handler` method compatible with both techniques, showing formatted alert dialogs per return code.
- **Sample database:** a test dialog lets you connect to a live Oracle server and run both a malformed and a valid SQL statement, toggling error-handling technique.

## Featured Technology
- 4D for OCI plug-in
- Oracle Call Interface (OCI)
- OCIOnErrCall / OCIErrorGet commands
- Error handles and error records

## Historical Context
The 4D for OCI plug-in has since been discontinued as a dedicated product; 4D moved database connectivity toward its own SQL engine (introduced in 4D v11 SQL, 2007) and ODBC-based external table connections. The error-handling *pattern* this note teaches — manual return-code checks versus a centralized automatic handler — mirrors 4D's enduring ON ERR CALL mechanism and remains conceptually sound, but the specific OCI plug-in commands documented here are no longer applicable to current 4D/Oracle integration work.
