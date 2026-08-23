# Tech Note: 4D Chart

- **Asset ID:** 33153
- **Tech Note #:** 04-26
- **Published:** July 1, 2004
- **Product / Version:** 4th Dimension 2003.3
- **Platform:** Mac & Win
- **Author:** Jean-Yves Fock-Hoon
- **Page URL:** https://kb.4d.com/assetid=33153
- **Download:** https://kb.4d.com/DLTN/TN/2004/MacOS/TN_2004_26-30_(JUN)/04-26_4D_Chart.hqx

## Overview

Written by Jean-Yves Fock-Hoon, this note explains how to generate charts from the 4D language using the 4D Chart plug-in, which has been built into 4D since version 6.0 but, the note observes, is underused relative to its capability. It covers three of the four charting commands (deliberately excluding the obsolete GRAPH command) and explains, through a running sales-per-salesperson-per-month example, when each is the right choice. CT Chart arrays is best when data must first be computed (sums, counts, or other aggregation) into X, Y, and Z arrays, where the Z array's size must equal the product of the X and Y array sizes, with any 2D Z series flattened into a single plain array in row-major order before being passed in. CT Chart data is preferable when the values to chart already exist directly in table fields -- avoiding the memory and speed cost of duplicating data into arrays -- by specifying field IDs for the X (category), Y (series), and Z (value) axes directly against the current selection, with an option to group duplicate categories into fewer columns rather than one column per record. CT Chart selection is suited to charting values spread across several different fields of the same record (rather than one value field per category) by supplying an X category field ID plus an array of field IDs for the Z series, again with an optional category-grouping parameter, and the note contrasts its field-count-driven Y axis against CT Chart data's field-driven Y axis to clarify when to pick one over the other.

## Key Points

- 4D Chart has four charting commands, but the GRAPH command is obsolete; this note covers CT Chart arrays, CT Chart data, and CT Chart selection.
- CT Chart arrays requires three arrays (X categories, Y series, Z values) where the Z array size must equal X size times Y size; multi-dimensional Z data must be flattened into one plain array (row by row) before calling the command.
- CT Chart arrays is the right choice when values require prior computation (sums, counts, aggregation) into temporary variables/arrays before charting.
- CT Chart data takes field IDs directly for X (categories), Y (series), and Z (values) from the current selection, avoiding the memory/speed cost of duplicating data into arrays, and supports grouping duplicate categories into fewer columns.
- CT Chart selection is used when chart values live in several distinct fields of the same record rather than a single value field; it takes an X category field ID and a Z array of field IDs, with Y implicitly defined by however many Z fields are supplied.
- The key distinction between CT Chart data and CT Chart selection: CT Chart data's Y (series) values come from the data of a single Y field, while CT Chart selection's Y values are simply the names of the Z fields provided.
- The bundled demo database exposes CT Chart Array/CT Chart Data/CT Chart Selection menu items, each generating a different chart type (3D line, grouped column charts) to illustrate the three commands side by side.

## Featured Technology

- 4D Chart plug-in (built into 4D since version 6.0)
- CT Chart arrays command
- CT Chart data command
- CT Chart selection command

## Historical Commentary

**Status:** Partially Superseded

This note is a clear, practical decision guide for choosing among 4D's classic 4D Chart plug-in commands (CT Chart arrays/data/selection) based on where the chart's source values live -- computed arrays, direct fields, or multiple fields per record -- and that decision framework remains conceptually sound. The CT Chart-prefixed commands themselves are legacy 4D Chart plug-in commands from the classic language; 4D has since introduced newer, more visually modern charting and data-visualization options (including web-based and area-based charting components) that many current projects use instead of the original 4D Chart plug-in, making this note's specific commands still functional but increasingly superseded by newer charting approaches for new development.

**References to newer/updated information:**
- 4D has introduced newer charting and data-visualization components since 2004 that many current projects prefer over the classic 4D Chart plug-in
- The CT Chart arrays / CT Chart data / CT Chart selection commands remain part of the current 4D language for databases still using the classic 4D Chart plug-in
- The GRAPH command referenced as already obsolete in this 2004 note remains obsolete and unused in current 4D development
