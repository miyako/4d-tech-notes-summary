# Tech Note: Pointers from Scratch

- **Asset ID:** 16396
- **Tech Note #:** 01-39
- **Published:** August 31, 2001
- **Product / Version:** 4D 6.7
- **Platform:** Mac & Win
- **Author:** Jamras Komoncharoensiri, 4D, Inc. Technical Support
- **Page URL:** https://kb.4d.com/assetid=16396
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2001/MacOS/TN_2001_36-40_(AUG)/01-39_Pointers_from_Scratch.hqx

## Overview

Jamras Komoncharoensiri (4D, Inc. Technical Support) delivers a from-scratch tutorial on 4D pointers -- referencing and dereferencing, what object/table/array/pointer types they can target, and the crucial constraint that pointers can only address fixed-location process/interprocess variables, not transient local variables.

## Key Points

- Variables are framed as named, fixed-size memory blocks (the audiocassette analogy); a pointer is then defined as a variable holding another variable's memory address, illustrated with an extended roommate/CD-player analogy for the address-vs-value distinction.
- Declaring with C_POINTER(vPointer) is mandatory in compiled mode; referencing uses vPointer:=->vString or vPointer:=Get pointer("vString"), dereferencing to read uses vPointer->, and assigning through the pointer uses vPointer->:=value.
- Unlike C, a single C_POINTER variable can point to any variable type interchangeably (integer, text, etc.) since the pointer type itself carries no target-type constraint, and 4D has no pointer arithmetic.
- A 4D pointer can reference variables, certain object types (fields, buttons, checkboxes, pop-ups, tab controls, pluggable areas, etc. -- but not TEXT, GROUP BOX, SUBFORM, RECTANGLE, LINE, OVAL, or MATRIX objects), tables (dereferenceable only inside commands, e.g. ALL RECORDS(ptrTable->), never in an assignment), fields, whole arrays, individual array elements, and pointers-to-pointers.
- The Self command returns a pointer to the current object's variable only when called from within an object method (returning a Nil pointer -> [] otherwise), and can be assigned to another pointer variable or passed as a parameter for generic object-manipulation methods like a SET_OBJECT(pointer;boolean) show/hide helper.
- Pointers can only reference fixed-address process/interprocess variables, not transient local ($) stack variables that cease to exist once their method returns; Get pointer is convenient for building pointers to many variables in a loop (e.g., a grid of 50 fields) but is noted as slower than a hard-coded -> reference.

## Featured Technology

- C_POINTER declaration and the -> reference/dereference operator
- Get pointer() command
- Pointers to variables, tables, fields, arrays, array elements, and pointers-to-pointers
- Self command for object-method pointer references
- Process vs. interprocess vs. local (stack) variable addressability

## Historical Commentary

**Status:** Still Relevant

Jamras Komoncharoensiri gives a from-first-principles tutorial on 4D pointers -- what they are, how -> reference/dereference works, what object/table/array/pointer-to-pointer types they can target, how to pass them as parameters, and the crucial caveat that pointers can only reference fixed-address process/interprocess variables, not transient local ($) variables. Classic 4D pointers, the -> operator, and Get pointer are unchanged in current 4D and this remains an accurate, still-useful primer on the concept, though modern 4D code increasingly favors object/collection references and class instances for many of the generic-programming use cases (like looping over dynamic variable sets) that this note demonstrates with raw pointers.

References to newer/updated information:
- The C_POINTER type, -> operator, and Get pointer command described here are unchanged and still core to the classic 4D language today
- Many generic-programming patterns that once relied on pointers (e.g., looping over dynamically-named variables) are now often implemented with objects, collections, and class instances instead
