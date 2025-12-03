# Page: RGSEnquiry
**File:** RGSEnquiry.aspx.cs

### 1. User Purpose
Users view and filter a list of RGS (Railway Goods Shipment) records, refresh the list, and request detailed views or printouts of individual shipments.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | On first load, initializes page text, header, and default filter values. Calls `loadDepotControl` to populate the depot dropdown and `PopOnLoad` to display any startup messages. |
| **loadDepotControl** | Retrieves the list of depots from the database and binds them to the depot dropdown control. |
| **PopOnLoad** | Checks for any query‑string or session flags that require a popup (e.g., success or error messages) and displays them. |
| **gvRGS_RowDataBound** | For each row in the RGS grid, formats data (e.g., date formatting, status icons) and attaches command buttons (View, Print). |
| **ddlLine_SelectedIndexChanged** | When a line is selected, updates the track dropdown to show only tracks belonging to that line and refreshes the grid to reflect the new filter. |
| **ddlTrack_SelectedIndexChanged** | Filters the RGS grid to show only shipments on the selected track. |
| **lbRefresh_Click** | Re‑queries the database with the current filter settings and rebinds the grid to show the latest data. |
| **gvRGS_RowCommand** | Handles row‑level commands such as “View” (navigates to a detail page) or “Print” (opens a print dialog). |
| **lbPrint_Click** | Opens the print view for the entire grid or selected rows, typically by redirecting to `RGSPrint.aspx` with appropriate query parameters. |

### 3. Data Interactions
* **Reads:** RGS records, Depot list, Line list, Track list.  
* **Writes:** None (the page is read‑only; actions are routed to other pages).

---

# Page: RGSPrint
**File:** RGSPrint.aspx.cs

### 1. User Purpose
Provides a printable view of RGS records, allowing users to print the list or individual shipment details.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | Loads the RGS data set based on query parameters (e.g., depot, line, track) and binds it to the grid for printing. |
| **gvRGS_RowDataBound** | Formats each row for print (e.g., removes interactive controls, sets font styles). |
| **gvRGS_RowCommand** | Handles commands such as “Print” for a single row, which may trigger a JavaScript print dialog or generate a PDF. |

### 3. Data Interactions
* **Reads:** RGS records filtered by the supplied criteria.  
* **Writes:** None (purely a print‑only view).

---

# Page: RegistrationInbox
**File:** RegistrationInbox.aspx.cs

### 1. User Purpose
Displays a list of registration requests awaiting approval or review, tailored to the logged‑in user.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| **Page_Load** | Determines the current user’s ID, then calls `SetupPage` to configure the inbox view. |
| **SetupPage** | Loads the registration requests for the specified user, applies any necessary filtering, and binds the data to the inbox grid. |
| **EncryptID** | Takes a dataset of registration records and replaces plain numeric IDs with encrypted tokens so that URLs or links do not expose raw identifiers. |

### 3. Data Interactions
* **Reads:** Registration request records belonging to the user.  
* **Writes:** None (the page only displays data; encryption is performed in memory).

---