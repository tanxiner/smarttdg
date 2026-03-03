### **Page Functionality Reference**

---

#### **1. `DepotTARInbox.aspx`**  
**User Purpose**: Users manage and submit TAR (Track Access Request) entries.  

**Key Events & Logic**:  
- **`Page_Load`**: Initializes the page, binds location data, and prepares the UI for TAR entry submission.  
- **`lbSubmit_Click`**: Validates user input, saves TAR details to the system, and confirms submission.  
- **`BindLocation`**: Loads location-specific data (e.g., track segments) for dropdowns or selection fields.  

**Data Interactions**:  
- **Reads**: Location codes, TAR types, and access dates from the system.  
- **Writes**: TAR entry details (e.g., user access requests, track segments) to the database.  

---

#### **2. `DepotTARSectorBooking.aspx`**  
**User Purpose**: Users book sector access for TAR (Track Access Request) entries.  

**Key Events & Logic**:  
- **`PopOnLoad`**: Loads pre-configured sector booking parameters (e.g., access dates, line codes).  
- **`lbSubmit_Click`**: Processes sector booking requests, validates access permissions, and records bookings.  
- **`gvDir1_RowDataBound`**: Dynamically updates grid rows to reflect real-time booking status or access rules.  
- **`lbBack_Click`**: Navigates users back to previous steps in the booking workflow.  

**Data Interactions**:  
- **Reads**: Sector access rules, user permissions, and existing booking conflicts.  
- **Writes**: Sector booking details (e.g., line codes, access dates, user roles) to the system.  

---

#### **3. `ExternalLogin.aspx`**  
**User Purpose**: Users authenticate with external credentials to access the system.  

**Key Events & Logic**:  
- **`Page_Load`**: Loads the login form and checks for session expiration.  
- **`btnLogin_Click`**: Validates external login credentials (e.g., third-party SSO) and authenticates the user.  
- **`CheckAccess`**: Verifies user permissions and redirects to the appropriate dashboard or login error page.  
- **`linkB_forgetPassword_Click`**: Triggers a password reset workflow (e.g., sends a reset link to the user’s email).  

**Data Interactions**:  
- **Reads**: User credentials, session tokens, and access control policies.  
- **Writes**: Password reset tokens or temporary login keys to the system.  

---

#### **4. `GenQRCode.aspx`**  
**User Purpose**: Users generate QR codes for track access requests.  

**Key Events & Logic**:  
- **`Page_Load`**: Loads the QR code generation form and initializes parameters (e.g., TAR ID).  
- **`btnGen_Click`**: Generates a QR code based on TAR details (e.g., track segment, access date) and displays it to the user.  

**Data Interactions**:  
- **Reads**: TAR-specific data (e.g., track codes, access dates) to encode into the QR code.  
- **Writes**: QR code image data (or a link to the QR code) for download or display.  

--- 

**Note**: All interactions are mediated through a Data Access Layer (DAL) or similar abstraction, with no direct SQL usage.