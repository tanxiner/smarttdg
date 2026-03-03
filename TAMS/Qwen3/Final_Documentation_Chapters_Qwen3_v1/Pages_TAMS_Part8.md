# Page: DepotTARInbox  
**File:** DepotTARInbox.aspx.cs  

### 1. User Purpose  
Users manage Track Access Request (TAR) inbox entries, including viewing, filtering, and submitting TAR applications.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, loads location data, and binds TAR entries to the grid. |  
| BindLocation | Loads location-specific data to filter TAR entries. |  
| lbSubmit_Click | Validates user input, saves the TAR application, and updates the inbox status. |  
| lnkD1StrTARNo_Click | Navigates to a specific TAR entry in the first directory. |  
| lnkD2StrTARNo_Click | Navigates to a specific TAR entry in the second directory. |  
| lbAppList_Click | Filters TAR entries based on user-selected criteria. |  
| gvDir1_RowDataBound | Formats GridView rows to highlight critical TAR details (e.g., urgency, status). |  
| ddlLine_SelectedIndexChanged | Refreshes TAR listings based on the selected line or track. |  

### 3. Data Interactions  
* **Reads:** TAREntry, Location, UserPermissions  
* **Writes:** TAREntry, UserActivityLog  

---

# Page: DepotTARSectorBooking  
**File:** DepotTARSectorBooking.aspx.cs  

### 1. User Purpose  
Users book specific sectors for Track Access Requests (TAR), specifying access details and permissions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads pre-configured sector booking data and initializes user interface elements. |  
| PopOnLoad | Fetches sector availability and populates dropdowns for access type and duration. |  
| lbSubmit_Click | Validates sector booking details, saves the request, and updates access permissions. |  
| RBLPowerReq_SelectedIndexChanged | Adjusts available sectors based on selected power request type. |  
| cbDir1All_CheckedChanged | Toggles selection of all sectors in the first directory. |  
| gvDir1_RowDataBound | Highlights sectors with pending or approved status in the GridView. |  
| lbAppList_Click | Filters sector bookings based on user role or access level. |  
| lbBack_Click | Returns to the previous TAR management page. |  
| lbDiagram_Click | Displays a visual diagram of sectors for spatial reference. |  
| chkSel_CheckedChanged | Updates sector selection state for bulk operations. |  

### 3. Data Interactions  
* **Reads:** SectorDefinition, AccessPermission, TAREntry  
* **Writes:** SectorBooking, UserAccessHistory