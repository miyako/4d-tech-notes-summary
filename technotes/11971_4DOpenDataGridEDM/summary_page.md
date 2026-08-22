# Tech Note: 4D Open in DataGrid's Enterprise Data Module - Beta 1

## Overview
- **Technical Note 00-39**
- **Author:** Sebastian Frey, Sextant Technologies, Inc.
- **Published:** August 1, 2000
- **Product/Version:** 4D Open v6.5
- **Platform:** Mac & Win
- **Content source:** Full PDF text recovered

## Key Points
This Tech Note is the fourth in Sebastian Frey's series on DataGrid Beta 1's architecture, this time examining the 4D Open low-level layer of the Enterprise Data Module. It identifies '4D Open for 4D' as one of three variants in the 4D Open suite (alongside 4D Open for Java and 4D Open for C++), describing it as effectively the API for 4D Server: usable from 4th Dimension standalone, 4D Runtime, or 4D Client, and notably capable of connecting a 4D Client not just to other servers but back to its own 'local' 4D Server. Through 4D Open, DataGrid's EDM layer could connect to one or many 4D Servers over a network, interrogate their data structure, query and sort records, receive results into local 4D fields, arrays, or variables, and create, update, and delete records — with the note also noting additional capabilities beyond the Beta 1 feature set, such as stored procedure execution and management of Sets and Named Selections. It candidly warns that the 4D Open API can feel awkward and its error messages unclear to newcomers, framing the EDM abstraction layer built on top of it as a way to smooth over that friction for DataGrid's own internal use. The featured technology is 4D Open (the 4D-to-4D variant) as consumed through DataGrid's EDM abstraction.

## Featured Technology
- 4D Open (4D Open for 4D)
- DataGrid Enterprise Data Module (EDM)
- Stored procedures, Sets, Named Selections

## Historical Context
This note is the fourth in Sextant Technologies' DataGrid series, describing how 4D Open (specifically its '4D Open for 4D' variant, distinct from 4D Open for Java and 4D Open for C++) was used as a low-level connectivity layer letting 4D Client connect to any 4D Server on the network, including its own 'local' server. Both DataGrid and 4D Open are long discontinued; the note's own admission that the API 'will at first seem awkward' with particular error messages underscores how much friendlier modern connectivity approaches (4D's REST/ORDA data server) are by comparison, making this purely of historical/archival interest today.

## What's Changed Since
- DataGrid and its Enterprise Data Module are long-discontinued third-party products
- 4D Open (in all its variants, including 4D Open for 4D described here) has been discontinued; 4D's REST/ORDA data server is the modern approach to similar connectivity goals

