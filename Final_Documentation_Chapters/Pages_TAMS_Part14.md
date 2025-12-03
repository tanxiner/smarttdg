# Page: RGS  
**File:** RGS.aspx.cs  

### 1. User Purpose  
Users view a list of RGS records, filter them by line, update TAR IDs, refresh the data, cancel TOA requests, and grant TOA depot approvals.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Sets up page permissions, populates the line dropdown, and loads the grid of RGS records by calling `PopOnLoad`. |
| PopOnLoad | Retrieves RGS records from the database via the `DAL` object, binds them to the `gvRGS` GridView, and configures any necessary UI elements. |
| gvRGS_RowDataBound | Adjusts the visual style of each row based on its data (e.g., highlighting pending items). |
| gvRGS_RowCommand | Handles commands issued from the grid rows such as edit, delete, or view details, invoking the appropriate data‑access methods. |
| ddlLine_SelectedIndexChanged | Filters the grid to show only records for the selected line and refreshes the display. |
| lbRefresh_Click | Forces a reload of the grid data by re‑calling `PopOnLoad`. |
| lbCancelTOA_Click | Cancels a TOA request for the selected record, updating its status in the database. |
| ddlUpdTARID_SelectedIndexChanged | Updates the TAR ID for a record and persists the change through the data‑access layer. |
| lbUpdDets_Click | Opens a detail view or edit form for the selected record. |
| updQTS | Calls the data‑access layer to update QTS information for a given NRIC, Qcode, rail, and user ID, returning a status string. |
| Timer_Tick | Periodically refreshes the grid data to keep the view current. |
| lbGrantTOADepot_Click | Grants TOA depot approval for the selected record, updating its status in the database. |
| ToDecode / ToEncode | Utility methods for encoding and decoding strings used in query strings or hidden fields. |

### 3. Data Interactions  
* **Reads:** RGS, QTS, TOA, Line (for dropdown)  
* **Writes:** RGS (TAR ID, status updates), QTS (QTS data updates), TOA (cancellation or approval status)

---

# Page: RGSAckSMS  
**File:** RGSAckSMS.aspx.cs  

### 1. User Purpose  
Users acknowledge SMS notifications related to RGS events, marking them as processed and completing the acknowledgment workflow.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Loads pending SMS acknowledgment records via the `DAL` object and displays them on the page. |
| PopOnLoad | Retrieves SMS acknowledgment data and binds it to the UI controls. |
| lbAck_Click | Marks the selected SMS record as acknowledged, updating its status in the database. |
| lblComplete_Click | Finalizes the acknowledgment process, possibly removing the record or marking it as complete. |
| ToDecode / ToEncode | Encode/Decode helper methods for handling query string values or hidden fields. |

### 3. Data Interactions  
* **Reads:** SMSAck (pending acknowledgments)  
* **Writes:** SMSAck (updates acknowledgment status, completion flag)