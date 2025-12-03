# Page: TARInbox  
**File:** TARInbox.aspx.cs  

### 1. User Purpose  
Users manage inbox items by submitting requests, filtering by criteria, and viewing detailed information.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the inbox interface and loads data for display. |  
| lbSubmit_Click | Validates user input, saves the request to the inbox, and updates the interface. |  
| lnkD1StrTARNo_Click | Filters inbox items based on specific criteria (e.g., TAR number). |  
| lnkD2StrTARNo_Click | Filters inbox items based on another set of criteria (e.g., date range). |  
| lbAppList_Click | Navigates to a list of applications or related items. |  
| gvDir1_RowDataBound | Binds data to GridView controls for display, formatting rows as needed. |  
| gvDir2_RowDataBound | Binds data to another GridView control for display, formatting rows as needed. |  

### 3. Data Interactions  
* **Reads:** Inbox, Application  
* **Writes:** Inbox  

---

# Page: TARSectorBooking  
**File:** TARSectorBooking.aspx.cs  

### 1. User Purpose  
Users submit sector booking requests, select power requirements, and manage access permissions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the booking interface and loads pre-existing data. |  
| lbSubmit_Click | Validates user input, processes the booking request, and updates the database. |  
| RBLPowerReq_SelectedIndexChanged | Updates access permissions based on selected power requirements. |  
| cbDir1All_CheckedChanged | Toggles selection for all items in a directory list. |  
| cbDir2All_CheckedChanged | Toggles selection for all items in another directory list. |  
| gvDir1_RowDataBound | Binds data to GridView controls for display, formatting rows as needed. |  
| gvDir2_RowDataBound | Binds data to another GridView control for display, formatting rows as needed. |  
| lbAppList_Click | Navigates to a list of applications or related items. |  
| lbBack_Click | Returns to a previous screen or step in the booking process. |  

### 3. Data Interactions  
* **Reads:** SectorBooking, PowerRequirement, AccessPermission  
* **Writes:** SectorBooking, AccessPermission  

---

# Page: TARViewDetails  
**File:** TARViewDetails.aspx.cs  

### 1. User Purpose  
Users view detailed information about track access requests, including power sectors and additional details.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the view interface and loads detailed application data. |  
| dgOR_ItemDataBound | Binds data to DataGrid controls for displaying related records. |  
| gvPossAddPL_RowDataBound | Binds data to GridView controls for displaying power line details. |  
| gvPossAddWL_RowDataBound | Binds data to GridView controls for displaying work location details. |  
| gvPossAddOO_RowDataBound | Binds data to GridView controls for displaying operational override details. |  
| dgPossPowerSector_ItemDataBound | Binds data to DataGrid controls for displaying power sector details. |  
| lbBack_Click | Returns to a previous screen or step in the application process. |  

### 3. Data Interactions  
* **Reads:** FormApp, PowerSector, OperationalOverride  
* **Writes:** None  

---

# Page: TOA.Master  
**File:** TOA.Master.cs  

### 1. User Purpose  
Users interact with a common layout for track access management pages.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- |