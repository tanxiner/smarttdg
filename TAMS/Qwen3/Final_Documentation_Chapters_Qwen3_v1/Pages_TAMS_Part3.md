# Page: DepotTARApplication  
**File:** DepotTARApplication.aspx.cs  

### 1. User Purpose  
Users submit track access applications with details about possession or protection of railway lines.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, binds location data, and sets up grid views for display. |  
| btnSubmit_Click | Validates user input, saves application details to the database, and sends confirmation emails. |  
| BindLocation | Loads available railway lines and locations into dropdown controls for user selection. |  
| BindGrid | Populates grid views with sector-specific data (e.g., blocked tracks, access types). |  
| displayDates | Populates date fields based on selected track type, access type, and location. |  
| showHideControls | Toggles visibility of form sections depending on whether the user selects "Possession" or "Protection" for track access. |  
| GridView1_RowDataBound | Formats grid rows to highlight critical data (e.g., blocked tracks) for visual clarity. |  
| ddlLine_SelectedIndexChanged | Updates form controls (e.g., dates, sectors) based on the selected railway line. |  
| rbPossession_CheckedChanged | Adjusts form layout and available options when the user selects "Possession" as the access type. |  
| rbProtection_CheckedChanged | Adjusts form layout and available options when the user selects "Protection" as the access type. |  

### 3. Data Interactions  
* **Reads:** TarType, BlockedTar, DepotTarSector, DepotTar  
* **Writes:** DepotTar (application details), BlockedTar (updates to blocked track records)