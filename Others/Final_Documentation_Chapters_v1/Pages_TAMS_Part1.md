### Page Logic Documentation: User Actions and Data Flow

---

#### **1. `AddTAR.aspx.cs` (Main TAR Management Page)**  
**Purpose**: Allow users to add, edit, save, or delete TAR (Tracking and Reporting) records.  

**User Actions & Data Flow**:  
- **Authentication Check**:  
  - On `Page_Load`, the system checks if the user is authenticated. If not, they are redirected to the login page.  
  - **Data Flow**: `Page_Load` → Authentication Check → Redirect if unauthenticated.  

- **Display Existing TARs**:  
  - The `GridView` control is populated with existing TAR records using the `BindTARData()` method (via the DAL).  
  - **Data Flow**: `BindTARData()` → DAL → Database Query → GridView.  

- **Add New TAR**:  
  - User clicks "Add New TAR" button → Triggers `AddTAR()` method.  
  - **Data Flow**: `AddTAR()` → DAL → Database Insert → Redirect to TAR details page.  

- **Save TAR**:  
  - User fills form and clicks "Save" → Triggers `SaveTAR()` method.  
  - **Data Flow**: `SaveTAR()` → DAL → Database Update → Redirect to TAR list.  

- **Edit TAR**:  
  - User clicks a row in the `GridView` → Triggers edit mode (e.g., populates form fields).  
  - **Data Flow**: GridView Row Click → Load TAR data → Form fields populated.  

- **Delete TAR**:  
  - User clicks "Delete" → Triggers `DeleteTAR()` method.  
  - **Data Flow**: `DeleteTAR()` → DAL → Database Delete → Refresh GridView.  

---

#### **2. `BasePage.aspx.cs` (Shared Utility Logic)**  
**Purpose**: Provide common functionality like session management and SQL command creation.  

**User Actions & Data Flow**:  
- **Session Management**:  
  - `SessionExpire()` method handles session timeout events (e.g., redirecting users if their session expires).  
  - **Data Flow**: Session Timeout → `SessionExpire()` → Redirect to login or home page.  

- **SQL Command Creation**:  
  - `GetSqlCommand()` method generates SQL commands for database interactions.  
  - **Data Flow**: `GetSqlCommand()` → DAL → SQL Query Execution → Database.  

---

#### **3. `DepotTARAppList.aspx.cs` (TAR Application List Page)**  
**Purpose**: Display and manage TAR applications for depot staff.  

**User Actions & Data Flow**:  
- **Load TAR Applications**:  
  - `Page_Load` triggers `BindLocation()` and `BindTARData()` to populate GridView controls.  
  - **Data Flow**: `BindLocation()` → DAL → Database Query → Dropdown list.  
  - `BindTARData()` → DAL → Database Query → GridView.  

- **Filter by Line**:  
  - User selects a line from a dropdown → Triggers `ddlLine_SelectedIndexChanged()` to filter TAR applications.  
  - **Data Flow**: Dropdown Selection → `ddlLine_SelectedIndexChanged()` → DAL → Filtered Query → GridView.  

- **Row Data Binding**:  
  - `gvDir1_RowDataBound()` and `gvDir1Child_RowDataBound()` customize GridView rows (e.g., highlight status).  
  - **Data Flow**: GridView Row Binding → DAL → Data Formatting → UI Display.  

---

#### **4. `DTCAuth.aspx.cs` (Authentication Page)**  
**Purpose**: Handle user authentication and token generation for secure access.  

**User Actions & Data Flow**:  
- **Token Generation**:  
  - `GenerateToken()` creates a session token for authenticated users.  
  - **Data Flow**: `GenerateToken()` → Token Storage → Session.  

- **Session Expiry Handling**:  
  - `SessionExpire()` ensures users are logged out if their session expires.  
  - **Data Flow**: Session Timeout → `SessionExpire()` → Redirect to login.  

---

#### **5. `Default.aspx.cs` (Home Page)**  
**Purpose**: Serve as the default landing page for authenticated users.  

**User Actions & Data Flow**:  
- **Load Home Page**:  
  - `Page_Load` initializes the home page without direct database interaction.  
  - **Data Flow**: No direct data flow; UI rendering only.  

---

### **Shared Data Access Layer (DAL)**  
- **Role**: Acts as an intermediary between UI pages and the database.  
- **Key Methods**:  
  - `BindTARData()`: Fetches TAR records for display.  
  - `SaveTAR()`: Updates TAR records in the database.  
  - `DeleteTAR()`: Deletes TAR records from the database.  
- **Data Flow**:  
  - UI Actions → DAL Methods → SQL Commands (via `GetSqlCommand()`) → Database → Data Returned to UI.  

---

### **Security & Session Management**  
- **Authentication**: All pages check user authentication in `Page_Load` (e.g., `AddTAR.aspx.cs`).  
- **Session Expiry**: Handled by `SessionExpire()` in `DTCAuth.aspx.cs` to prevent unauthorized access.  
- **Tokenization**: `GenerateToken()` ensures secure session management for authenticated users.  

---

### **Summary of Data Flow**  
1. **User Action** → UI Control (e.g., Button, GridView)  
2. **Event Trigger** → Code-Behind Method (e.g., `Save