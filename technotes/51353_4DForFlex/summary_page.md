# Tech Note 08-37: 4D (Is There) for Flex

**Author:** Tim Kaufman, 4D Inc. Technical Services  
**Published:** October 23, 2008 | **Product/Version:** 4D Web 2.0 Pack v11.2 | **Platform:** Mac & Win  
**Page:** https://kb.4d.com/assetid=51353  
**Download:** https://kb.4d.com/DLTN/TN/2008/Windows/TN_2008_35-39_(OCT)/08-37_4D_for_Flex.zip

## Proposition

This technical note demonstrates how to build professional Rich Internet Applications (RIAs) using Adobe Flex—a Flash-based declarative UI framework—connected to 4D Server v11.2+ for data storage and SQL query execution. The 4D Web 2.0 Pack provides Flex component libraries (SWC files) with SQL-oriented classes that enable Flex developers to declare SQL connections, execute queries, and bind results to interactive UI controls (DataGrid, ComboBox, forms) with minimal code.

## Key Points

- **Requirements:**
  - 4D Web 2.0 Pack v11 Release 2 or higher (provides Flex SWC component libraries).
  - Adobe Flex Builder (IDE for developing and compiling Flex applications).
  - 4D v11.2+ with SQL Server running.
  - Basic knowledge of Flex (MXML markup language and ActionScript 3 code).

- **4D Configuration:**
  - Enable SQL Server: Run menu → Start SQL Server (or enable startup in Preferences, SQL).
  - Create Flash security policy file: `socketpolicy.xml` in `Preferences/SQL/Flash/` folder with minimal content:
    ```xml
    <cross-domain-policy>
      <allow-access-from domain="*" to-ports="19812"/>
    </cross-domain-policy>
    ```
    (Allows Flash access to the default SQL port 19812; "*" allows any domain; can be restricted to specific domains if needed.)

- **Flex Builder Project Setup:**
  - Create a new Flex project (or import the included FlexPlanner project).
  - Configure source folder (e.g., "src") and output folder (output to 4D Webfolder for automatic deployment).
  - Add library path: Flex Build Path → Library path tab → Add SWC → reference Flex4D_SQL.swc (minimum; optionally add other 4D component libraries).
  - Declare 4D namespace in Application tag:
    ```xml
    xmlns:fourD="http://www.4d.com/2007/mxml"
    ```

- **SQLService Class (Connection & Query Execution):**
  - Declare in MXML:
    ```xml
    <fourD:SQLService
      id="fourDSQLService"
      host=""
      userName="Administrator"
      autoConnect="false"
      connect="connectHandler(event)"
      disconnect="disconnectHandler(event)"
      result="resultHandler(event)"
      fault="faultHandler(event)"/>
    ```
  - `host`: IP address of 4D machine (defaults to "localhost" if blank).
  - `userName` / password: Login credentials (no password used in example).
  - `autoConnect="false"`: Don't connect at startup; call `fourDSQLService.connect()` explicitly in application initialization.
  - Events: `connect`, `disconnect`, `result`, `fault` — each can trigger custom handler functions.
  - Execution: `SQLService.execute(sqlString)` executes a SQL query and returns an AsyncToken.

- **AsyncToken (Query Tracking):**
  - `SQLService.execute()` returns an mx.rpc.AsyncToken object.
  - Allows distinguishing between multiple queries when results arrive asynchronously (out of order).
  - Assign token.name to label queries: `_sqlServiceToken.name = "categoryToken"`.
  - In result handler, check `event.token.name` to identify which query completed:
    ```actionscript
    if(event.token.name == "categoryToken")
      _categorySQL = event.result as SQLResultSet;
    ```

- **SQLResultSet (Data Binding):**
  - Data structure representing a selection from 4D.
  - Declare as `[Bindable]` to enable data binding to UI controls.
  - Assign from result handler: `_categorySQL = event.result as SQLResultSet`.
  - Bind to DataGrid/ComboBox via data binding syntax `{_categorySQL}`:
    ```xml
    <mx:ComboBox dataProvider="{_categorySQL}" labelField="Name"/>
    <mx:DataGrid dataProvider="{_taskSQL}">
      <mx:columns>
        <mx:DataGridColumn headerText="Task" dataField="Title"/>
      </mx:columns>
    </mx:DataGrid>
    ```

- **Sample Application (FlexPlanner) Workflow:**
  - **Initial Load:** Application creationComplete event → `init()` → `fourDSQLService.connect()`.
  - **On Connect:** `connectHandler()` → Execute two SQL queries (SELECT * FROM Category; SELECT * FROM Task).
  - **On Result:** `resultHandler()` → Identify query by AsyncToken name → Populate _categorySQL and _taskSQL SQLResultSet objects.
  - **Data Binding:** Category ComboBox and Task DataGrid automatically display results via binding.
  - **User Interaction:** Category selection → Filter Task DataGrid (change handler re-queries with WHERE clause) → Select Task row → Populate detail form fields.
  - **CRUD Operations:** Save button → INSERT/UPDATE via SQL; New button → Clear form for new record; Delete button → DELETE via SQL.

- **UI States & View Switching:**
  - **Form View:** ComboBox and detail form side-by-side.
  - **Grid View:** Category DataGrid and Task DataGrid in two-column layout.
  - Toggle via ToggleButtonBar (Flex state management).
  - Filter logic works in both views (category selection limits task display).

- **Deployment Options:**
  1. **Standalone Flash Player:** Double-click FlexPlanner.swf in 4D Webfolder.
  2. **Web Browser via 4D Web Server:** Point browser to http://localhost:8080/FlexPlanner.html (serves the SWF-wrapping HTML file).

## Featured Technology

- Adobe Flex framework (MXML and ActionScript 3)
- 4D Web 2.0 Pack (Flex component libraries: Flex4D_SQL.swc)
- SQLService class for SQL connections and queries
- SQLResultSet class for data binding
- AsyncToken for asynchronous query tracking
- Flex DataGrid and ComboBox controls
- MXML declarative syntax and data binding
- ActionScript 3 event handling
- Flash security policy configuration
- 4D SQL Server over TCP/IP (default port 19812)
- 4D Web Server integration

## Historical Context

Published October 2008 for 4D Web 2.0 Pack v11.2, this note represents a significant moment in 4D's web technology strategy. Adobe Flex was at its peak as an RIA platform (circa 2008); it offered strong typing, component-based architecture, and a rich library of UI controls—a compelling alternative to HTML/AJAX for complex web applications at the time. The 4D Web 2.0 Pack positioned 4D as a backend for Flex applications, enabling developers to build sophisticated, interactive web clients backed by 4D Server. The note's detailed explanations of SQLService, data binding, and event handling reflect the pedagogical commitment to help developers adopt this new technology stack. The sample application (FlexPlanner) was practical: task/category management with filtering and CRUD operations is a real-world use case.

## Historical Commentary

**Status:** Obsolete

Adobe Flex and Flash are completely obsolete as of December 2020 (Flash Player end-of-life). Modern browsers no longer support Flash, and the Flash ecosystem is defunct. 4D's web strategy has moved entirely away from Flex toward standards-based web technologies.

**Related Updates:**
- **Adobe Flash End-of-Life (December 31, 2020):** Flash Player is no longer supported in any modern browser. All Flex applications that relied on Flash for execution are now non-functional.
- **4D Qodly (4D v17+):** 4D's modern web builder, replacing the Web 2.0 Pack entirely. Qodly uses standard web technologies (HTML5, JavaScript/TypeScript, modern frameworks) and ORDA-based REST APIs instead of Flex SWC components.
- **Modern Web Stack (4D v18+):** 4D emphasizes:
  - **Web Components:** Native web standards-based components.
  - **REST/GraphQL APIs:** Data access via standard HTTP APIs (JSON), not proprietary SQL streaming.
  - **Modern Frameworks:** Vue, React, Angular, Svelte, etc., using REST endpoints.
  - **4D Web Server:** Serves REST endpoints and static web assets; developers build UIs in standard web technologies.
- **Data Access Pattern:** Modern 4D uses REST APIs (with JSON data) for web-to-database communication, not direct SQL connections from browser-based clients (which was Flex's approach).
- **Security:** Flex's Flash sandbox and security model are obsolete; modern approaches use standard HTTP security (CORS, authentication tokens, etc.).

**Conclusion:** This note is purely historical interest. Developers requiring similar functionality today should:
1. Use 4D Qodly for low-code web UI development.
2. Use modern web frameworks (Vue, React, etc.) with 4D REST APIs for custom web applications.
3. Use 4D Web Components for server-rendered web pages with 4D integration.

No developer should attempt to build new applications with Flex/Flash; it is not executable in modern environments.
