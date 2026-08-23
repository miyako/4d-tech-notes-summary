# Tech Note: Installing Components

- **Asset ID:** 11992
- **Tech Note #:** 00-53
- **Published:** November 1, 2000
- **Product / Version:** 4D Insider 6.7
- **Platform:** Mac & Win
- **Author:** Steve Hartman
- **Page URL:** https://kb.4d.com/assetid=11992
- **Download:** https://kb.4d.com/ftp://ftp.4D.com/ACI_TECHNICAL_NOTES/2000/MacOS/TN_2000_51-55_(NOV)/00-53_Installing_Components.hqx

## Overview

Steve Hartman (4D, Inc. Technical Support) explains how to build and install a 4D v6.7 component using 4D Insider — a mechanism for deploying protected, independently updatable pieces of code into a host database — and walks through the complete workflow with a worked "Parrots" demographics example database.

## Key Points

- A component's objects fall into three attributes: **Public** (viewable and end-user modifiable, but not renameable/deletable), **Protected** (viewable but not modifiable — the method Preview area stays blank), and **Private** (neither viewable nor modifiable, invisible in both 4th Dimension and 4D Insider). Tables, fields, and menu bars can never be marked Private, and they are not removed when a component is later uninstalled.
- Component creation/installation workflow: create a new library in 4D Insider containing the objects to package, choose New from the Components menu to name the component, drag objects into it under Private/Protected/Public, click Generate on the component, then open the target database with Insider and choose Install/Update.
- Naming-conflict avoidance recommendations: use a unique prefix (developer's initials or company name) on all non-local Module objects, type Module objects with Compiler directives, use the `Get Module Resource ID` function to manage STR# and PICT resources, and keep object names to 28 characters (prefix excluded).
- Insider logs any naming conflicts encountered during installation — objects with names that collide with existing database objects will block that component's import.
- If a component includes a table it must also include a form for it, and vice versa; the installer can offer to link a component's form to an existing table in the target database.
- The "Parrots" sample database (inoculation-age statistics for male/female parrots) demonstrates the full lifecycle: build the objects in a library, generate the component, install it into a fresh database with none of the original objects, and confirm the resulting database behaves identically to the source.

## Featured Technology

- 4D Insider component creation and generation
- Public/Protected/Private component object attributes
- Get Module Resource ID function
- Component naming-conflict avoidance conventions
- Component install/update workflow
- Compiler directives for typed module objects

## Historical Commentary

**Status:** Superseded

This note walks through the mechanics of building and installing a 4D v6.7 component with 4D Insider: dragging objects into Public/Protected/Private roles, naming conventions to avoid conflicts, and the install/update step that reports conflicting object names. Its worked example (a "Parrots" database with inoculation statistics) demonstrates that a component-based database behaves identically to one with the original objects copied in directly, which was the core selling point of the technology. 4D Insider itself and this exact component workflow are long obsolete, superseded by 4D's modern, integrated component/plug-in and project-based packaging systems, though the underlying goal of deploying protected, updatable code modules remains a live concept in current 4D.

**References to newer/updated information:**
- 4D Insider, the standalone structure-documentation and component-management tool this note relies on, was retired long ago in favor of built-in tooling
- 4D's current component architecture (and 4D's move to text/project-based structures) offers a far more integrated way to package, reference, and update protected code than the Public/Protected/Private drag-and-drop workflow described here
