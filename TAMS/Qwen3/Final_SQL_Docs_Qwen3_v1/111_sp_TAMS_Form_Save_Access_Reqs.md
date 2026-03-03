# Procedure: sp_TAMS_Form_Save_Access_Reqs

### Purpose
This stored procedure saves access requirements for a specific form, updating the TAMS_TAR_AccessReq table with selected access requirements and saving remarks to the TAMS_TAR table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line			AS NVARCHAR(10) = NULL, |
| @TrackType		AS NVARCHAR(50) = NULL, |
| @SelAccessReqs	AS NVARCHAR(200) = NULL, |
| @PowerSelVal	AS NVARCHAR(10) = NULL, |
| @PowerSelTxt	AS NVARCHAR(100) = NULL, |
| @ARRemarks		AS NVARCHAR(1000) = NULL, |
| @TARID			AS BIGINT = 0, |
| @Message		AS NVARCHAR(500) = NULL OUTPUT |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets the internal transaction flag to 1 and begins a new transaction.
2. It then checks if there are any existing access requirements for the specified TARID. If not, it inserts a new set of access requirements into TAMS_TAR_AccessReq.
3. Next, it updates the IsSelected field in TAMS_TAR_AccessReq to 1 for all access requirements that match the selected power selection value or are part of the specified access requirements list.
4. It also updates the TARRemark field in TAMS_TAR to the provided ARRemarks value for the specified TARID.
5. If any errors occur during the procedure, it sets the @Message output parameter with an error message and either commits or rolls back the transaction depending on whether an error occurred.

### Data Interactions
* **Reads:** TAMS_Access_Requirement table, TAMS_TAR_AccessReq table, TAMS_TAR table
* **Writes:** TAMS_TAR_AccessReq table, TAMS_TAR table