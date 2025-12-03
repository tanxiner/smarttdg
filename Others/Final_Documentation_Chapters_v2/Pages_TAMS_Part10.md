# Page: RGS  
**File:** RGS.aspx.cs  

### 1. User Purpose  
Users manage track access requests and related actions through a grid interface.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, loads data, and sets up UI state. |  
| PopOnLoad | Sets initial page configurations and default values. |  
| gvRGS_RowDataBound | Binds data to grid rows and applies formatting. |  
| gvRGS_RowCommand | Handles user actions like editing, deleting, or updating records in the grid. |  
| ddlLine_SelectedIndexChanged | Filters grid data based on selected line. |  
| lbRefresh_Click | Reloads grid data to reflect current state. |  
| lbCancelTOA_Click | Cancels a track access request and updates the record. |  
| ddlUpdTARID_SelectedIndexChanged | Updates TAR details based on selected TAR ID. |  
| lbUpdDets_Click | Saves changes to TAR details. |  
| updQTS | Processes encoded/decoded data for TAR updates. |  
| Timer_Tick | Periodically refreshes grid data or updates. |  
| lbGrantTOADepot_Click | Grants depot access and updates the record. |  

### 3. Data Interactions  
* **Reads:** TAR, User, BlockedTar, Track  
* **Writes:** TAR, BlockedTar  

---

# Page: RGSAckSMS  
**File:** RGSAckSMS.aspx.cs  

### 1. User Purpose  
Users acknowledge SMS messages related to track access requests.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads SMS acknowledgment data and initializes the page. |  
| lbAck_Click | Processes acknowledgment of an SMS message. |  
| lblComplete_Click | Finalizes the SMS acknowledgment process. |  
| PopOnLoad | Sets up initial page state for SMS acknowledgment. |  

### 3. Data Interactions  
* **Reads:** SMSMessage  
* **Writes:** SMSMessage  

---

# Page: RGSEnquiry  
**File:** RGSEnquiry.aspx.cs  

### 1. User Purpose  
Users search and view track access request details.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads initial data and sets up the enquiry interface. |  
| loadDepotControl | Populates depot-specific dropdowns or controls. |  
| PopOnLoad | Initializes page state for enquiry mode. |  
| gvRGS_RowDataBound | Binds data to grid rows and applies formatting. |  
| ddlLine_SelectedIndexChanged | Filters grid data based on selected line. |  
| ddlTrack_SelectedIndexChanged | Filters grid data based on selected track. |  
| lbRefresh_Click | Reloads grid data to reflect current state. |  
| gvRGS_RowCommand | Handles user actions like editing or deleting records in the grid. |  
| lbPrint_Click | Generates a printable version of the grid data. |  

### 3. Data Interactions  
* **Reads:** TAR, User, BlockedTar, Track  
* **Writes:** None