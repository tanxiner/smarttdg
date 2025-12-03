# Page: DepotTARInbox  
**File:** DepotTARInbox.aspx.cs  

### 1. User Purpose  
Users manage and submit TAR (Track Access Request) entries from their inbox.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, binds location data, and loads TAR entries. |  
| lbSubmit_Click | Validates inputs, saves the TAR entry, and sends a confirmation email. |  
| lnkD1StrTARNo_Click | Opens a specific TAR entry for editing or viewing. |  
| lbAppList_Click | Filters TAR entries based on user permissions or search criteria. |  
| gvDir1_RowDataBound | Formats grid rows to highlight urgent or pending TAR entries. |  
| ddlLine_SelectedIndexChanged | Updates available TAR options based on the selected line. |  

### 3. Data Interactions  
* **Reads:** TAREntry, Location, UserPermissions  
* **Writes:** TAREntry, EmailLog  

---

# Page: DepotTARSectorBooking  
**File:** DepotTARSectorBooking.aspx.cs  

### 1. User Purpose  
Users book sector access for track operations and manage power request details.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads sector availability data and initializes booking form fields. |  
| lbSubmit_Click | Validates booking details, saves the sector booking, and logs the request. |  
| RBLPowerReq_SelectedIndexChanged | Updates power request options based on the selected power type. |  
| gvDir1_RowDataBound | Highlights rows with overlapping or conflicting sector bookings. |  
| lbAppList_Click | Filters bookings by date, user, or sector. |  
| cbDir1All_CheckedChanged | Toggles selection of all items in the booking grid. |  

### 3. Data Interactions  
* **Reads:** SectorAvailability, BookingHistory, PowerRequestType  
* **Writes:** SectorBooking, BookingLog  

---

# Page: ExternalLogin  
**File:** ExternalLogin.aspx.cs  

### 1. User Purpose  
Users authenticate via external login methods (e.g., SSO, federated identity).  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Checks for existing session or redirect from authentication provider. |  
| btnLogin_Click | Validates external credentials, creates a session, and redirects to the dashboard. |  
| linkB_forgetPassword_Click | Triggers a password reset workflow via email. |  

### 3. Data Interactions  
* **Reads:** UserAccount (external ID), SessionToken  
* **Writes:** LoginAttemptLog, PasswordResetToken  

---

# Page: GenQRCode  
**File:** GenQRCode.aspx.cs  

### 1. User Purpose  
Users generate QR codes for track access credentials or instructions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the QR code generation form. |  
| btnGen_Click | Generates a QR code image based on user input and displays it. |  

### 3. Data Interactions  
* **Reads:** UserInput (text/data to encode)  
* **Writes:** QRCodeImage (output to display)