### **TARForm_App Page Functionality**  
**User Purpose**  
This form is used to manage Track Access Request (TAR) applications, allowing users to submit, modify, and track TAR requests across multiple tabs. It includes sections for attaching documents, adding buffer zones, TVF stations, and handling approval/rejection workflows.  

---

### **Key Events & Logic**  
1. **Tab Navigation (Tab1/Tab2/Tab3)**  
   - Switches between form sections (e.g., request details, attachments, or approval status).  

2. **Attachment Management (lnkDownload_Click)**  
   - Retrieves and downloads files attached to a TAR request from the `TAMS_TAR_Attachment` table.  

3. **Data Entry & Modification**  
   - **Buffer Zones/TVF Stations**: Methods like `lbtnAddBufferZone_Click` and `lbtnAddTVFStation_Click` allow users to add new entries to these sections.  
   - **Grid Actions**: `RowCommand` events for GridView controls handle actions like editing, deleting, or confirming entries (e.g., approving a buffer zone).  

4. **Status Updates**  
   - Buttons like `lbCReject_Click` and `lbEndorse_Click` update the TAR request status (e.g., reject, endorse, or process).  

5. **Form Initialization (Page_Load)**  
   - Loads default data, initializes controls, and sets up the form’s initial state.  

---

### **Data Interactions**  
- **Read Operations**:  
  - **TAMS_TAR_Attachment**: Retrieves file attachments for a specific TAR request.  
- **Write Operations**:  
  - **BufferZone/TVFStation Tables**: Stores or updates entries added via the form (e.g., new buffer zones or TVF stations).  
- **Workflow Tables**: Updates TAR request status in the database based on user actions (e.g., rejection or endorsement).  

---  
This form centralizes TAR management, ensuring seamless data flow between user actions and backend database operations.