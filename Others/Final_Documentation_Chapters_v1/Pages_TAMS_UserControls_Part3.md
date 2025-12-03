# Page: OCCTVF_Ack_Preview  
**File:** OCCTVF_Ack_Preview.ascx.cs  

### 1. User Purpose  
Users preview and submit/reject track access requests.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads the track access preview data. |  
| populateOCCTVF_Ack | Loads track access request details into the GridView for display. |  
| GridView1_RowDataBound | Formats or highlights specific rows in the GridView based on user roles or status. |  
| btnSubmit_Click | Submits the track access request, updates the status, and notifies relevant parties. |  
| btnReject_Click | Rejects the track access request, updates the status, and records the rejection reason. |  
| ShowRemark | Displays additional remarks or notes related to the track access request. |  
| btnSave_Click | Saves any edited remarks or updates to the track access request. |  
| ShowTarTVF | Displays related tariff or tracking information for the request. |  

### 3. Data Interactions  
* **Reads:** TrackAccessRequest, UserRoles, Remarks  
* **Writes:** TrackAccessRequestStatus, Remarks  

---

# Page: menu  
**File:** menu.ascx.cs  

### 1. User Purpose  
Users navigate the application via a dynamic menu tailored to their role.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the menu structure based on user permissions and session data. |  
| Generate_Menu | Builds the primary navigation menu using user-specific roles and access levels. |  
| Generate_Menu2 | Builds a secondary or contextual menu for specific application sections. |  

### 3. Data Interactions  
* **Reads:** UserRoles, MenuItems  
* **Writes:** None