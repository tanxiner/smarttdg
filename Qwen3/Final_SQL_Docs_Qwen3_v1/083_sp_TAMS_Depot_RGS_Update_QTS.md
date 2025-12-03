# Procedure: sp_TAMS_Depot_RGS_Update_QTS

### Purpose
This stored procedure updates the QTS qualification status for a specific depot and track type, triggering an audit and potentially updating the TAMS TOA record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Depot ID |
| @InchargeNRIC | NVARCHAR(50) | In-charge NRIC number |
| @UserID | NVARCHAR(500) | User ID for auditing purposes |
| @TrackType | NVARCHAR(50) | Track type (Mainline or Depot) |
| @Message | NVARCHAR(500) | Output parameter to store error message |
| @QTSQCode | NVARCHAR(50) | Output parameter to store QTS qualification code |
| @QTSLine | NVARCHAR(10) | Output parameter to store track line |

### Logic Flow
1. The procedure starts by checking if a transaction is already active. If not, it sets the internal transaction flag to 1.
2. It then creates a temporary table #tmpnric to store the results of the QTS qualification check.
3. The procedure truncates the temporary table and selects the required data from TAMS_TOA and TAMS_TAR tables based on the provided TARID and track type.
4. It then checks if the QTS qualification status is valid for the selected track line. If not, it triggers an audit and potentially updates the TAMS TOA record.
5. The procedure then calls a separate stored procedure [sp_api_tams_qts_upd_accessdate] to update the QTS qualification status in the database.
6. Depending on the outcome of the QTS qualification check, the procedure sets the @Message output parameter to indicate whether the update was successful or not.
7. If an error occurs during the execution of the stored procedure, it logs the error and returns the corresponding error message.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TAR, TAMS_Parameters
* Writes: TAMS_QTS_Error_Log