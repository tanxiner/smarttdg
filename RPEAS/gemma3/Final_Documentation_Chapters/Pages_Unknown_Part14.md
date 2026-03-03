# Page: RPEAS_Form_View.aspx
**File:** RPEAS_Form_View.aspx.vb

### 1. User Purpose
Users view and approve data related to a transaction, likely within a financial or logistics system.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, likely loading data and setting up event handlers. |
| Check_UserViewAccess | Determines if the current user has the necessary permissions to view this form. If not, an error message is displayed. |
| PopulateData | Populates the form with data, potentially from a database or other data source. This likely involves calling a data access layer (DAL) to retrieve the data. |
| FillGroup2, FillGroup3, FillGroup4, FillGroup5, FillGroup6 | These methods likely populate specific groups of data within the form, possibly based on different transaction types or stages. They take DataTable objects as input, likely representing data retrieved from the database. |
| btncancel_Approver_Click | Allows the approver to cancel the transaction, likely triggering a rollback or cancellation process. |
| lnkFileURL_Click, lnkFileURL_Supp_Click | These links likely open files associated with the transaction, such as invoices or supporting documents. |
| btnexport_Click | Allows the user to export the data from the form, potentially to a CSV or Excel file. |

---