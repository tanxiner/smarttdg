### **DepotTARApplication.aspx**  
**User Actions:**  
- Submit a Track Access Request (TAR) by selecting a track, access type (Possession/Protection), and sectors.  
- View and manage TAR details, including editing, deleting, or withdrawing requests.  
- Filter TAR data based on line selections or status updates.  
- Print TAR details for record-keeping.  

**Data Flow:**  
- **Form Submission:** User inputs are processed to create or update TAR records in the backend system.  
- **Grid Binding:** TAR data is dynamically loaded into grids for display, filtered by line or status.  
- **Status Updates:** Changes to TAR status (e.g., withdrawal confirmation) are reflected in the grid and stored.  
- **Deletion/Editing:** User actions trigger backend operations to remove or modify TAR entries.  
- **Printing:** TAR details are formatted and exported for print or download.  

---

### **DepotTAREnquiry.aspx**  
**User Actions:**  
- Search for TAR records by line, status, or date range.  
- Navigate through paginated TAR listings.  
- Edit, delete, or withdraw specific TAR entries.  
- Print TAR details for documentation.  

**Data Flow:**  
- **Search Filters:** User inputs (e.g., line selection) filter TAR data and populate the grid.  
- **Pagination:** Grid data is split into pages, with navigation controls updating the displayed records.  
- **CRUD Operations:** User actions (edit/delete) trigger backend updates to TAR records.  
- **Withdrawal Confirmation:** User confirms withdrawal of a TAR, updating its status in the system.  
- **Printing:** TAR details are formatted and exported for print or download.  

--- 

Both pages rely on dynamic data binding and user-triggered actions to manage TAR records, with clear separation between input, processing, and output workflows.