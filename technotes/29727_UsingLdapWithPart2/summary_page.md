# Tech Note: Using LDAP with 4D part II

- **Asset ID:** 29727
- **Tech Note #:** 03-29
- **Published:** June 26, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Pierre Bonnais
- **Page URL:** https://kb.4d.com/assetid=29727
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_26-30_(JUN)/03-29_Using_LDAP_in_4D_Pt_2.hqx

## Overview

Pierre Bonnais (4D Inc.) follows up on an earlier LDAP overview by documenting exactly how to port an existing Windows LDAP authentication plug-in to Mac OS X's Mach-O runtime architecture using CodeWarrior and the 4D Plug-in Wizard, then shows how to wire the resulting plug-in into 4D's web authentication flow.

## Key Points

- Recaps LDAP as a tree-structured (Directory Information Tree), Distinguished-Name-addressed directory protocol per the x500 standard, faster for reads than an RDBMS but without transaction support -- context inherited from Christian Cypert's earlier note (TN 02-54).
- Explains Mach-O as the only executable format the Mac OS X kernel loads directly, with 4D plug-ins packaged as Mach-O bundles; the 4D Plug-in Wizard generates the required CodeWarrior project skeleton.
- Shows transferring the Windows plug-in's resource fork to Mac OS using 4D Transporter: drag the `.rsr` file onto Transporter, choose PC-to-Mac, and hold Command while clicking Move to generate the `.rsrc` file containing the '4BNX' command resource and matching 'STR#' routine names.
- Demonstrates conditional compilation to select platform-specific headers (`#ifdef WIN32` pulling in `winsock2.h`/`winldap.h`, versus `ldap4D.h`/`ldap.h` on OS X located under `/usr/include`), and linking against `/usr/lib/libldap.dylib`.
- Documents a specific linker gotcha: a missing `dyld_stub_bindin_helper` symbol is resolved by adding the `bundle1.o` object file (from `/usr/lib`) to the CodeWarrior project.
- Shows building a debug version (generating a `.xsym` symbol file) and pointing CodeWarrior's runtime settings at the 4D 2003 executable as the host application, with plug-in output directed to the Mac4DX folder.
- Concludes with a practical 4D web integration example: the `On Web Authentication` method (triggered by an incoming 4DAction request) calls `ldap_Authentication` with a Distinguished Name built from the supplied username/password to authenticate against an LDAP server before allowing the 4DAction to run.

## Featured Technology

- LDAP (Lightweight Directory Access Protocol)
- Mach-O plug-in architecture (Mac OS X)
- CodeWarrior plug-in porting
- 4D Plug-in Wizard / 4D Transporter
- On Web Authentication / 4DAction

## Historical Commentary

**Status:** Partially Superseded

This note captures a very real, era-specific pain point: porting native C/C++ 4D plug-ins from the classic Mac OS resource-fork/CFM world to Mac OS X's then-new Mach-O runtime, including obscure linker fixes like the dyld_stub_bindin_helper/bundle1.o issue. That porting problem itself is now purely of historical interest since 4D plug-in development has moved on from CodeWarrior-era Mach-O bundle mechanics entirely. LDAP as a directory protocol, however, remains genuinely still relevant today (e.g., via Active Directory), though modern 4D applications more often authenticate through SSO/OAuth identity providers or later, higher-level LDAP libraries rather than a custom Mach-O plug-in and On Web Authentication bind as shown here.

**References to newer/updated information:**
- 4D plug-in development has long since moved past the CodeWarrior/Mach-O-bundle porting mechanics described in this note
- LDAP directory services remain in wide enterprise use today, though many modern web applications now favor SSO/OAuth-based identity providers over direct LDAP binds in On Web Authentication
