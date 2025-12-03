### Page Functionality Reference  

---

#### **1. OCCAuthTC_DTL.ascx**  
**User Purpose**:  
Manage access requests by displaying a list of pending entries and allowing submission of new requests.  

**Key User Actions**:  
- **View Access Requests**: Load a grid of pending access entries (via `populateOCCAuth`).  
- **Submit New Request**: Save user input (e.g., access details) via `btnSubmit_Click`.  
- **Customize Grid Rows**: Modify row appearance or behavior during data binding (via `GridView1_RowDataBound`).  

**Data Flow**:  
- **Read**: Load access request data into the grid (likely from a backend service or database).  
- **Write**: Save submitted access details to a storage system (e.g., database or API endpoint).  

---

#### **2. OCCAuth_NEL.ascx**  
**User Purpose**:  
Track and manage access requests with additional roster code information.  

**Key User Actions**:  
- **View Access Requests**: Display a list of entries, including roster codes (via `populateOCCAuth`).  
- **Submit New Request**: Save user input, including roster code details (via `btnSubmit_Click`).  
- **Customize Grid Rows**: Adjust row appearance or behavior during data binding (via `GridView1_RowDataBound`).  

**Data Flow**:  
- **Read**: Load access request data and roster code details into the grid.  
- **Write**: Save submitted access details and roster code information to a storage system.  

---

#### **3. OCCAuth_NEL_bak.ascx**  
**User Purpose**:  
Legacy or backup version of access request management, likely for historical data or version control.  

**Key User Actions**:  
- **View Access Requests**: Display a list of entries, including roster codes (similar to `OCCAuth_NEL`).  
- **Submit New Request**: Save user input, including roster code details (via `btnSubmit_Click`).  
- **Customize Grid Rows**: Modify row appearance or behavior during data binding (via `GridView1_RowDataBound`).  

**Data Flow**:  
- **Read**: Load access request data and roster code details into the grid.  
- **Write**: Save submitted access details and roster code information to a storage system.  

---

#### **4. OCCTVF_Ack.ascx**  
**User Purpose**:  
Acknowledge or process TVF (likely a specific type of request) with options to approve, reject, or save remarks.  

**Key User Actions**:  
- **View TVF Requests**: Display a list of pending TVF entries (via `populateOCCTVF_Ack`).  
- **Approve/Reject Request**: Update the status of a request (via `btnSubmit_Click` or `btnReject_Click`).  
- **Save Remarks**: Store additional notes or comments (via `btnSave_Click`).  
- **View Remarks/TarTVF**: Display detailed information or remarks for a specific entry (via `ShowRemark` or `ShowTarTVF`).  

**Data Flow**:  
- **Read**: Load TVF request data and associated remarks into the grid.  
- **Write**: Update TVF request status, save remarks, or store additional details (e.g., TarTVF data).  

--- 

**Notes**:  
- All pages rely on backend services or data stores (not explicitly SQL) for data persistence.  
- Grid customization and user actions are central to the workflow, enabling dynamic data interaction.