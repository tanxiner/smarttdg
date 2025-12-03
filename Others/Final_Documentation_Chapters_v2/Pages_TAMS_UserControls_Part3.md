# Page: OCCTVF_Ack_Preview  
**File:** OCCTVF_Ack_Preview.ascx.cs  

### 1. User Purpose  
Users review and approve or reject track access requests.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads data into the GridView. |  
| populateOCCTVF_Ack | Loads data into the GridView for review. |  
| GridView1_RowDataBound | Formats rows in the GridView to highlight critical information. |  
| btnSubmit_Click | Submits the request for approval and updates the status. |  
| btnReject_Click | Rejects the request, updates the status, and notifies the user. |  
| ShowRemark | Displays additional remarks for a specific entry. |  
| btnSave_Click | Saves any changes made to the form fields. |  
| ShowTarTVF | Displays related track information for context. |  

### 3. Data Interactions  
* **Reads:** OCCTVF_Ack, Track, Roster  
* **Writes:** OCCTVF_Ack, User  

---

# Page: menu  
**File:** menu.ascx.cs  

### 1. User Purpose  
Users access the main navigation menu for the application.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the menu and initializes user-specific settings. |  
| Generate_Menu | Builds the menu based on user role and internet access status. |  
| Generate_Menu2 | Generates an alternative menu layout for specific user roles. |  

### 3. Data Interactions  
* **Reads:** User  
* **Writes:** None