# Page: RGS
**File:** RGS.aspx.cs

### 1. User Purpose
Users manage track access requests, update details, and grant depot permissions through a grid interface.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and loads track access data into the grid. |
| PopOnLoad | Sets up UI elements and permissions for the user. |
| gvRGS_RowDataBound | Binds data to grid rows and formats display fields. |
| gvRGS_RowCommand | Handles user actions like editing or deleting track access records. |
| ddlLine_SelectedIndexChanged | Filters track access data based on selected line. |
| lbRefresh_Click | Reloads track access data from the database. |
| lbCancelTOA_Click | Cancels an active track access request. |
| ddlUpdTARID_SelectedIndexChanged | Updates track access details based on selected TAR ID. |
| lbUpdDets_Click | Saves changes to track access details. |
| updQTS | Updates track access status with encoded/decoded data. |
| Timer_Tick | Periodically refreshes track access data. |
| lbGrantTOADepot_Click | Grants depot access permissions to a user. |

### 3. Data Interactions
* **Reads:** User, BlockedTar, TrackAccess
* **Writes:** User, BlockedTar, TrackAccess

---

# Page: RGSAckSMS
**File:** RGSAckSMS.aspx.cs

### 1. User Purpose
Users acknowledge SMS notifications related to track access requests and confirm completion of actions.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Loads SMS acknowledgment data and initializes the page. |
| lbAck_Click | Confirms receipt of an SMS and updates the status. |
| lblComplete_Click | Marks an SMS acknowledgment as complete. |
| PopOnLoad | Sets up UI elements for SMS acknowledgment. |

### 3. Data Interactions
* **Reads:** User, BlockedTar, TrackAccess
* **Writes:** User, BlockedTar, TrackAccess