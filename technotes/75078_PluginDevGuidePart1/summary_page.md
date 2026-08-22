# Tech Note 09-02: 4D Plug-in Development Guide – Part 1

## Proposition
Teach 4D developers how to build cross-platform, Unicode-aware, Universal Binary plug-ins for 4D 2004/v11 SQL, covering the theoretical foundations before Part 2's hands-on examples.

## Key Points
- Plug-ins let developers extend 4D beyond its standard language using open-source libraries or direct system calls.
- Over-reliance on plug-ins can compromise 4D's cross-platform RAD (rapid application development) benefits — use judiciously.
- 4D v11 SQL introduced substantial plug-in API changes: Unicode support, endianness awareness, and native picture handling.
- The Altura library (used to port Mac code to Windows) and QuickDraw graphics were being phased out, directly affecting plug-in architecture.
- The Plug-in Wizard generates starter C source and project files for Xcode (Mac) and Visual Studio (Windows).
- Solid C programming skills, including manual memory management, are a prerequisite.

## Featured Technology
- 4D Plug-in API (C-based)
- Xcode and Visual Studio IDEs
- Unicode / endianness handling
- Universal Binary (PowerPC + Intel)
- Plug-in Wizard code generator
- Altura (Mac→Windows porting library, being retired)
- QuickDraw (being retired)

## Best Practices Highlighted
- Use the Plug-in Wizard to bootstrap cross-platform project structure.
- Design plug-in commands to handle text/picture/numeric data uniformly across Mac and Windows.
- Weigh the maintenance cost of plug-ins against the flexibility they provide.

## Context/Positioning
Published just as 4D v11 SQL modernized its internals (Unicode, 64-bit-adjacent architecture shifts, Universal Binary), 4D needed to guide its plug-in developer community through breaking API and platform changes.

## Historical Commentary
This note captures a genuine technology inflection point — the shift away from QuickDraw and the Altura porting layer toward Unicode-native, Universal Binary plug-ins. The core C-based plug-in API and toolchain (Xcode/Visual Studio) it describes are still valid today, making the material **still_relevant** as an introduction to plug-in fundamentals. However, many simpler cross-platform extension needs that once required a compiled plug-in can now be met with 4D's project-based language classes (introduced ~v18-19, 2019-2020) or direct REST/process calls, reducing (but not eliminating) the need for native plug-in development for common tasks.
