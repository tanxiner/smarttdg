# Page: RPEAS_Admin_Menu_Mapping
**File:** RPEAS_Admin_Menu_Mapping.aspx.vb

### 1. User Purpose
This page allows administrators to map menu items to specific data records, likely for configuring a system's menu structure.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads data, and prepares the data grid for display. |
| FillInfo | Populates the data grid with menu mapping data. |
| BinddgSearch | Binds the data grid with the populated data. |
| dgSearch_ItemDataBound | Handles the event when a new item is bound to the data grid, likely for adding or editing a menu mapping. |
| btnSave_Click | Saves the current menu mapping data to the system. |
| SaveInfo | Saves the menu mapping data, potentially including error handling. |
| dgSearch_SortCommand | Sorts the data displayed in the data grid based on the selected column. |
| btnclose_Click | Closes the current window or dialog. |

---

# Page: RPEAS_ExportPDF_Summary
**File:** REAPS_ExportPDF_Summary.aspx.vb

### 1. User Purpose
This page allows users to generate a PDF summary of data, likely related to REAPS transactions.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and prepares for PDF generation. |
| PopulateData | Populates the data used for the PDF generation. |
| export_MergePDF | Merges the data into a single PDF document. |
| mergePdfs |  Merges multiple PDF files into a single PDF. |
| AddPageNumber | Adds page numbers to the generated PDF. |
| CreatePDF2 | Creates the PDF document. |
| populateloghistory | Logs the PDF generation process. |
| populateAttachment |  Handles attachments related to the PDF generation. |