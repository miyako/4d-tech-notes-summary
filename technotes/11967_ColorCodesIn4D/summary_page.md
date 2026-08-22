# Tech Note: Color Codes in 4D, 4D Chart, and the 4D Productivity Modules

## Overview
- **Technical Note 00-19**
- **Author:** Unknown / not specified
- **Published:** April 1, 2000
- **Product/Version:** 4D Draw v6.5
- **Platform:** Mac & Win
- **Content source:** Full PDF text recovered

## Key Points
This Tech Note by Tim Tonooka explains the three distinct but interrelated color-coding systems available across 4D proper, 4D Chart, and the 4D Productivity Modules (4D Calc, 4D Draw, and 4D Write): each application's own native color code representation, the direct specification of a color's individual RGB (red/green/blue) components, and reference to a color as an index into 4D's built-in 256-color palette. It notes an important platform caveat — 4D Write is the one exception unable to use 4D's indexed color-palette codes, while 4D Chart and the other Productivity Modules can use all three systems — and grounds the whole discussion in a brief review of color theory, contrasting subtractive color mixing (as used in printing, combining cyan, magenta, yellow, and black inks) with additive color mixing (as used for light emitted directly from a computer monitor). All three systems ultimately address the same underlying 24-bit color space of 16,777,216 possible colors, though the number actually displayable depends on the monitor's color-depth setting and video card capability at the time. An accompanying example database provides an interactive visual demonstration, letting developers experiment with constructing colors across the full spectrum using each of the three coding systems. The featured technology spans 4D's native and indexed color systems as consumed across the entire 4D Productivity Modules product line of that era.

## Featured Technology
- 4D native color codes
- RGB color components
- 4D indexed color palette (256 colors)
- 4D Chart / 4D Productivity Modules (4D Calc, 4D Draw, 4D Write)

## Historical Context
This note explains the three parallel color-coding systems 4D, 4D Chart, and the 4D Productivity Modules used to describe 24-bit RGB colors: native color codes, individual RGB components, and 4D's 256-color indexed palette, along with a grounding in additive vs. subtractive color theory. 4D Chart, 4D Draw, and 4D Write (the original 4D Productivity Modules) have all been discontinued or superseded by newer tools (notably 4D Write Pro), and while RGB color theory itself is timeless, the specific native/indexed color-code systems these discontinued modules relied on are now obsolete alongside the modules themselves.

## What's Changed Since
- 4D Chart, 4D Draw, and the original 4D Write have all been discontinued; 4D Write Pro is the modern successor for document/word-processing needs
- Modern 4D development expresses colors primarily via standard RGB/CSS-style color values rather than the native 4D or 256-color indexed palette systems described in this note

