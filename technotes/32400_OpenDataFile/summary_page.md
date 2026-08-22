# Tech Note 04-17: Open Data File

**Author:** Not specified in source teaser
**Published:** April 29, 2004 | **Product/Version:** 4D v2003.3 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=32400
**Download:** https://kb.4d.com/DLTN/TN/2004/Windows/TN_2004_16-20_(APR)/04-17_Open_Data_File.exe

## Overview
This Tech Note shows how to programmatically open different 4D data files from within a 4D application, so end users can switch between multiple personalized data sets that share the same structure (application) file, without manually quitting and relaunching 4D themselves.

## Key Points
- Motivates the need for personalized/multiple data files as 4D applications became more end-user-oriented.
- The example database presents a list of available data files for the user to pick from.
- Selecting a data file automatically relaunches 4D bound to that data file under the same structure file.
- Removes the manual, error-prone process of quitting, locating, and reopening a structure file with a chosen data file.

## Featured Technology
- 4D structure file / data file architecture (Design Mode era, .4DB/.4DD split)
- Programmatic relaunch / data file switching

## Historical Context
Only the on-page teaser paragraph for this asset could be recovered (the full archived PDF was not accessible in this environment), so this summary reflects the note's stated purpose only, not its exact code listing. The underlying architecture — a single binary structure file paired with a user-selectable external data file — is specific to 4D's pre-Project-Mode Design Mode era. The general concept of supporting multiple data sets per application definition remains relevant, but the specific structure/data file relaunch mechanics described here have been superseded by 4D's modern Project Mode and more flexible data source options.
