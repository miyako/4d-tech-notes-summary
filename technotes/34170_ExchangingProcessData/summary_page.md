# Tech Note 04-39: Exchanging Data Between Processes

**Author:** Not specified in source
**Published:** September 30, 2004 | **Product/Version:** 4th Dimension v2004 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=34170
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_36-40_(AUG)/04-39_Exchanging_Data.exe

## Overview
This note addresses how separate processes running within a single 4D database can communicate to retrieve or set values held in each other's process variables, a task the note warns can become a "real nightmare" if not done carefully.

## Key Points (from available teaser)
- Multi-process 4D databases often need processes to exchange values held in process variables.
- Naive inter-process communication can be error-prone if not properly synchronized.
- The note provides worked examples for retrieving and setting values across processes.
- The goal is to illustrate techniques that keep inter-process communication simple and reliably synchronized.

## Featured Technology
- Multi-process 4D application architecture
- Process variable read/write across processes
- Process communication synchronization techniques

## Historical Context
**Note:** Only the on-page teaser paragraph was recoverable for this Tech Note; the full PDF and example database were not accessible (old archive format not retrievable in this environment), so the specific synchronization patterns demonstrated cannot be detailed here. Inter-process communication remains a relevant concern in current 4D multi-process applications, though later 4D versions introduced shared objects/collections and additional process-communication commands that offer safer, more modern alternatives to manual process-variable exchange of the kind this note likely demonstrated.
