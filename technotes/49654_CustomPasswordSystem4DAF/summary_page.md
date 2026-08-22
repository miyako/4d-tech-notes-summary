# Custom Password System with 4D Ajax Framework

## Overview
By default the 4D Ajax Framework ships wired to 4D's built-in Password System for user authentication, but this note walks through swapping in a fully custom authentication scheme instead — covering which framework configuration hooks and login-flow methods must be overridden so a database can use its own user/password table and validation logic rather than 4D's native password system.

## Key Points
- Published April 30, 2008 as Technical Note 08-16.
- Targets 4D Web 2.0 Pack v11.1 on Mac & Win.
- Author: Unknown (4D Technical Services team).

## Featured Technology
- 4D Ajax Framework (4DAF)
- Authentication / custom password systems
- 4D Password System (native)
- Framework configuration hooks

## Historical Context
Authentication customization is a perennial need, but this specific implementation is tied to swapping out 4DAF's login plumbing, which no longer exists. Modern 4D applications handle custom authentication via ORDA/REST session tokens, and web-facing apps typically use standard web auth patterns (JWT, OAuth) rather than 4DAF-specific hooks.

**Status:** obsolete

**Related updates:**
- 4D Ajax Framework (4DAF) has been discontinued; modern custom-authentication approaches in 4D use REST/ORDA session management or JWT-based schemes
- 4D's built-in Password System has itself evolved substantially through later 4D versions
