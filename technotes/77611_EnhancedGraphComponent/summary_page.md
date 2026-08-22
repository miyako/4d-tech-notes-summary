# Tech Note 16-12: Enhanced Graph Component

**Author:** Charlie Vass, Technical Services Engineer, 4D Inc.
**Published:** August 26, 2016 | **Product/Version:** 4D v15 R5 64-bit | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=77611
**Download:** https://kb.4d.com/DLTN/TN/2016/16-12_EnhancedGraph.zip

## Proposition
This note addresses the complexity of 4D's enhanced GRAPH command, which replaced GRAPH SETTINGS with an OBJECT parameter exposing 35+ configuration elements. It supplies a ready-made EnhancedGraph component with a visual Graph Designer so developers can build, save, and reuse graph templates without hand-coding every property.

## Key Points
- **Two-step template model:** graph templates (all display properties) are built visually and separately from the data-binding step that renders the final graph.
- **Graph Designer form:** a three-page UI (Document Basics; Scales and Legend; Colors and Opacity) covers the full surface of enhanced GRAPH's OBJECT parameter.
- **Multiple graph types supported:** bars, proportional, stacked, picture, line, scatter, and pie graphs, each with type-specific options.
- **Utility actions:** Clear, Save Graph Template, Set Graph to Pasteboard, Save SVG Image, and Display Properties List buttons streamline common tasks.
- **Macros for integration:** auto-generate the project-method code needed to wire host-database data into a graph.
- **Datasheet Editor:** lets users edit chart data directly rather than only through code.
- **Requires v15 R4 64-bit or later:** the component is explicitly tied to the enhanced (64-bit) GRAPH command, not the legacy 32-bit GRAPH SETTINGS approach.

## Featured Technology
- 4D v15 R4/R5 64-bit
- Enhanced GRAPH command
- OBJECT parameter (graph settings)
- 4D Components (Design Mode)
- SVG export

## Best Practices Highlighted
1. Separate reusable graph templates (appearance) from data binding (content) for maintainability.
2. Use macros to generate boilerplate integration code rather than writing it by hand each time.

## Context / Positioning
This Tech Note was published in 2016, during 4D's "classic" Design Mode era (v14-v16), which predates Project Mode (introduced in v17, 2018) with its text-based, Git-friendly method storage, predates the maturation of ORDA (introduced ~v16 R5/R6, 2017), and predates modern 4D Write Pro/View Pro document engines. Techniques and constraints described here should be read in that light.

## Historical Commentary
**Status:** Partially Superseded

The enhanced GRAPH command and its OBJECT parameter remain part of 4D's language today, so the underlying charting mechanism is still valid; however, this specific EnhancedGraph component is a Design Mode-era download component that predates Project Mode and has not been kept current, and 4D's later focus shifted toward View Pro/chart objects and web-based charting for many reporting scenarios.
