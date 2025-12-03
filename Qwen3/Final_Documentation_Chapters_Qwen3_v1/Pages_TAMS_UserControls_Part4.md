# Page: OCCTVF_Ack_Preview  
**File:** OCCTVF_Ack_Preview.ascx.cs  

### 1. User Purpose  
Users review and submit/reject track access requests with associated operational data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the control and loads preview data into the GridView. |  
| populateOCCTVF_Ack | Loads track access request details into the GridView for display. |  
| GridView1_RowDataBound | Formats or highlights specific rows in the GridView based on data. |  
| btnSubmit_Click | Validates user input, saves the request, and confirms submission. |  
| btnReject_Click | Marks the request as rejected and updates the status in the system. |  
| ShowRemark | Displays additional notes or comments related to the track access request. |  
| btnSave_Click | Saves any edited changes to the track access request data. |  
| ShowTarTVF | Reveals detailed technical information about the track access request. |  

### 3. Data Interactions  
* **Reads:** TrackAccess, User, OperationalData, Roster  
* **Writes:** TrackAccess, User, OperationalData  

---

# Page: menu  
**File:** menu.ascx.cs  

### 1. User Purpose  
Users access a dynamic navigation menu tailored to their role and permissions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the menu structure based on user authentication and permissions. |  
| Generate_Menu | Builds the menu hierarchy using user-specific role data. |  
| Generate_Menu2 | Creates an alternative menu layout for specific user scenarios (e.g., internet users). |  

### 3. Data Interactions  
* **Reads:** User, Role, Permission  
* **Writes:** None