# Page: TARAppList  
**File:** TARAppList.aspx.cs  

### 1. User Purpose  
Users view and manage TAR applications, submit new requests, and navigate between records.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| **Page_Load** | Initializes the page, binds TAR application data to GridViews, and displays a legend for status indicators. |  
| **lbSubmit_Click** | Validates user input, saves new TAR application data, and redirects to a confirmation or summary page. |  
| **displayLegend** | Renders a visual legend explaining status icons or colors used in the GridViews. |  
| **gvDir1_RowDataBound / gvDir2_RowDataBound** | Applies conditional formatting to GridView rows (e.g., highlights approved/rejected statuses). |  
| **lnkD1StrTARNo_Click / lnkD2StrTARNo_Click** | Opens a detailed view of a specific TAR application when a user clicks a link in the GridView. |  
| **lbBack_Click** | Returns the user to a previous page or refreshes the TAR application list. |  
| **gvDir1Child_RowDataBound / gvDir2Child_RowDataBound** | Formats child GridView rows to display related data (e.g., supporting documents or comments). |  

### 3. Data Interactions  
* **Reads:** TARApp, TARApplicationDetails, Status  
* **Writes:** TARApp (when submitting new applications)