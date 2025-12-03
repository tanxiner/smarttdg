# Page: TOABookOut  
**File:** TOABookOut.aspx.cs  

### 1. User Purpose  
Users manage track booking requests and track surrender processes.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads booking data into the interface. |  
| lbNextV1_Click | Advances the user through multi-step booking process. |  
| Tab1_Click | Switches to the first tab for booking details. |  
| Tab2_Click | Switches to the second tab for party information. |  
| lbPrevV2_Click | Returns to the previous step in the booking process. |  
| lbAddParties_Click | Opens a dialog to add additional parties to the booking. |  
| gvParties_RowDataBound | Formats grid row data for party information display. |  
| gvParties_RowCommand | Handles user actions (e.g., edit/delete) on party records. |  
| lbSurrender_Click | Triggers the surrender process for a booked track. |  
| LogError | Records error messages for debugging purposes. |  

### 3. Data Interactions  
* **Reads:** TOAReg, Parties, TrackDetails  
* **Writes:** TOAReg, Parties, TrackDetails  

---

# Page: TOAError  
**File:** TOAError.aspx.cs  

### 1. User Purpose  
Users view error messages or system alerts related to track operations.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Displays error details to the user. |  

### 3. Data Interactions  
* **Reads:** ErrorLogs  
* **Writes:** None  

---

# Page: TOAGenURL  
**File:** TOAGenURL.aspx.cs  

### 1. User Purpose  
Users generate encoded or decoded URLs for track access.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the URL generation interface. |  
| lblGen_Click | Triggers URL encoding or decoding based on user input. |  
| ToEncode | Converts input string to an encoded URL format. |  
| ToDecode | Converts an encoded URL back to its original string. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: TVFAcknowledgement  
**File:** TVFAcknowledgement.aspx.cs  

### 1. User Purpose  
Users view acknowledgment records for TVF (Track Vehicle Form) submissions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the acknowledgment interface and binds grid data. |  
| BindGrid | Populates the grid with TVF acknowledgment records. |  
| LoadOCCTVF_AckCtrl | Fetches specific acknowledgment details based on user ID. |  

### 3. Data Interactions  
* **Reads:** TVFAcknowledgement, OCCTVF  
* **Writes:** None