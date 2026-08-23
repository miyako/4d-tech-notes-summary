# Tech Note: Using Recursive Code

- **Asset ID:** 25597
- **Tech Note #:** 02-56
- **Published:** December 31, 2002
- **Product / Version:** 4D 6.8
- **Platform:** Mac & Win
- **Author:** Roland Lannuzel
- **Page URL:** https://kb.4d.com/assetid=25597
- **Download:** https://kb.4d.com/DLTN/TN/2002/MacOS/TN_2002_56-61_(DEC)/02-56_Using_Recursive_Code.hqx

## Overview

Roland Lannuzel (4D S.A.) explains what recursive code is and where it helps, using three worked examples in 4D 6.8: a classic recursive factorial method, a recursive disk-search routine built on FOLDER LIST/DOCUMENT LIST that walks nested folders looking for a matching name, and a recursive anagram generator that produces every permutation of a string (with an optimization step that sorts the input and skips duplicate letters to avoid redundant anagrams of repeated characters). It closes with a fourth, 'pseudo-recursive' pattern that spawns a NEW PROCESS running the same method instead of truly calling itself, useful for limiting the number of distinct methods while avoiding stack growth.

## Key Points

- Defines direct recursion (a method calling itself) versus harder-to-trace indirect/mutual recursion (method A calls B which calls back into A), warning that indirect recursion should generally be avoided because it is difficult to trace and maintain.
- Factorial example: `If ($1<=0) / $0:=1 / Else / $0:=$1*Factorial($1-1) / End if` illustrates that each recursive call gets its own local $1/$0 and other local variables, at the cost of stack space for each nested call.
- Recursive disk search (`FindOnVolumes`) uses `Count parameters` to detect the initial call (no parameters) versus a recursive call (a path parameter), then loops over `FOLDER LIST`/`DOCUMENT LIST` results, recursing into each subfolder and tracking nesting depth in `◊Level`/`◊LevelMax`, storing matches into a [RESULTS] table in batches of 1000 via `ARRAY TO SELECTION`.
- Recursive anagram method (`Anagrams`/`zAnagrammes`) takes a 'current string so far' and 'remaining characters' as parameters, recursing once per remaining character; an optimized version first sorts the input into an array and skips over repeated letters (using a `$Test` variable) to avoid duplicate anagrams for strings with repeated characters.
- Warns that recursion, if not bounded, can overflow 4D's stack space or the machine's memory since each call requires its own return point and local variable storage; suggests using a process/interprocess counter variable or the 4D Pack `AP_Available memory` command to guard against uncontrolled recursion depth.
- Shows a 'pseudo-recursive' pattern where a method with `Count parameters=0` spawns itself as a new process via `New process`, rather than truly recursing -- useful for keeping the method count low while avoiding actual stack-based recursion; the risk shifts from stack overflow to spawning too many processes and exhausting memory.

## Featured Technology

- Recursive method calls
- FOLDER LIST / DOCUMENT LIST recursive disk search
- Recursive anagram generator
- Count parameters for detecting initial vs. recursive calls
- NEW PROCESS as a pseudo-recursive alternative
- Stack/RAM management for deep recursion

## Historical Commentary

**Status:** still_relevant

Roland Lannuzel walks through three concrete recursion patterns still taught in CS courses today -- a factorial method, a recursive folder/file search using FOLDER LIST and DOCUMENT LIST, and a recursive anagram generator that sorts and skips duplicate letters -- plus a fourth 'pseudo-recursive' pattern using NEW PROCESS. The core guidance (indirect/mutual recursion is hard to trace, recursion consumes stack and RAM, and 4D Pack's AP_Available memory can guard against overflow) remains sound engineering advice for 4D developers writing methods or classes today. The specific disk-search commands (FOLDER LIST, DOCUMENT LIST) are still present in 4D, though Folder and File objects/ORDA-style APIs now offer more modern alternatives for filesystem traversal.

References to newer/updated information:
- FOLDER LIST and DOCUMENT LIST remain available in current 4D, though the newer Folder/File object commands provide a more modern, object-oriented way to enumerate directory contents
- The general principles about recursion, stack usage, and avoiding uncontrolled indirect recursion apply equally to modern 4D class methods and object-oriented code
