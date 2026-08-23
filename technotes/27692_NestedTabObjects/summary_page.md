# Tech Note: Tab Objects within Tab Objects

- **Asset ID:** 27692
- **Tech Note #:** 03-18
- **Published:** April 16, 2003
- **Product / Version:** 4D 2003
- **Platform:** Mac & Win
- **Author:** Steve Hartman, MCP, Information Systems, 4D, Inc.
- **Page URL:** https://kb.4d.com/assetid=27692
- **Download:** https://kb.4d.com/DLTN/TN/2003/MacOS/TN_2003_16-20_(APR)/03-18_Tab_Objects.hqx

## Overview

Steve Hartman demonstrates nesting a second Tab Control object inside a page of a first Tab Control to build hierarchical multi-page navigation in a single form, using an "Employee Demo" database that restricts department-specific information (Personnel, Manager, Salary, Accounting, Information Systems data) based on the logged-in user's role.

## Key Points

- Tab Control objects (introduced in 4D v6) get their values from arrays or lists; the `Selected list item` command returns which item was clicked, and `SET LIST ITEM PROPERTIES` can enable/disable individual tabs by setting a list item's "Enterable" property.
- Example 1: a top-level tab control's `On Load` object method uses a `Case of (Current user=...)` block to call `SET LIST ITEM PROPERTIES(vTab;N;False;Plain;0)` and dim tabs a given role (Human Resources, Accounting, Manager, Information Systems) shouldn't see.
- Example 2: a second Tab Control object is placed on the Information Systems page of the first tab control, letting a single top-level tab host its own multi-page sub-navigation for Email, FTP, and database account information.
- The nested tab control's object method tracks the active tab in `LLastTab`, using `GET LIST ITEM PROPERTIES`/`SET LIST ITEM PROPERTIES` on both `On Load` (initialize first tab as active/disabled) and `On Clicked` (re-enable the previously active tab, disable the newly selected one).
- Because `SET VISIBLE` cannot act on a single grouped object, objects belonging to each nested-tab "page" are named with a shared prefix (e.g., `Group1Emp_EmailLoginCheckbox`) and then grouped into `Group 1`/`Group 2`/`Group 3` purely for editing/positioning convenience.
- Visibility switching uses wildcard `SET VISIBLE` calls: `SET VISIBLE(*;"Group@";False)` hides every group's objects, then `SET VISIBLE(*;"Group"+String(LLastTab)+"@";True)` reveals only the objects belonging to the newly selected nested tab.
- Notes that icons can be added to nested tab list items (shown in the example's Information Systems sub-tabs) to make the interface more visually distinctive.
- Concludes that tab controls, and by extension nested tab controls, are memory-efficient, fast, intuitive for users, and well suited to both page-navigation and access-restriction use cases.

## Featured Technology

- Tab control form objects (introduced 4D v6)
- SET LIST ITEM PROPERTIES command (enable/disable tabs)
- Selected list item command
- SET VISIBLE with wildcard object-name matching for page groups
- Nested tab controls for hierarchical, role-based UI navigation

## Historical Commentary

**Status:** Still relevant

Steve Hartman shows how to nest a second Tab Control object inside a page of a first Tab Control to build hierarchical, multi-level navigation, using an employee-records demo where role-based access dims certain top-level tabs (via SET LIST ITEM PROPERTIES) and a department-specific second-level tab control switches between grouped, wildcard-named form objects (via SET VISIBLE with '@' patterns). Tab Control objects remain a fully supported, still-used 4D form object today, and nesting them for hierarchical navigation is still a valid, directly applicable technique in classic 4D Forms. The specific commands shown (SET LIST ITEM PROPERTIES, Selected list item, SET VISIBLE with wildcards) are unchanged, though modern 4D form design increasingly favors object groups, subforms, and (in newer form technologies) more declarative page/panel components for some of the same multi-page use cases.

References to newer/updated information:
- Tab Control objects, SET LIST ITEM PROPERTIES, Selected list item, and SET VISIBLE with wildcard names all remain part of current 4D and work as described
- Modern 4D form design also offers subforms and other page/panel-oriented UI components that can serve some of the same hierarchical-navigation purposes as nested tab controls, giving developers more options than existed in 2003
