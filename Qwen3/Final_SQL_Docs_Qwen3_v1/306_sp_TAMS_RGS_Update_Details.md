# Procedure: sp_TAMS_RGS_Update_Details

### Purpose
This stored procedure updates the details of a TAMS Record Group (RGS) by checking the qualification status of an in-charge person and updating their details if necessary.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID of the RGS to be updated. |
| @InchargeNRIC | NVARCHAR(50) | The NRIC of the in-charge person. |
| @MobileNo | NVARCHAR(20) | The mobile number of the in-charge person. |
| @TetraRadioNo | NVARCHAR(50) | The Tetra radio number of the in-charge person. |
| @UserID | NVARCHAR(50) | The ID of the user updating the RGS. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |

### Logic Flow
1. The procedure checks if a transaction has been started and sets an internal transaction flag.
2. It creates a temporary table #tmpnric to store the qualification status of the in-charge person.
3. The procedure truncates the temporary table and inserts a new record into it using a stored procedure sp_TAMS_TOA_QTS_Chk.
4. It selects the in-charge name and status from the temporary table.
5. If the in-charge status is 'InValid', the procedure checks if the access type is 'Protection'. If so, it truncates the temporary table again and inserts a new record into it using sp_TAMS_TOA_QTS_Chk with the correct qualification code.
6. The procedure then checks if the in-charge person is new or not. If they are new, it updates their details in TAMS_TOA and inserts audit records for TAMS_TOA and TAMS_TOA_Parties.
7. If the in-charge status is 'Valid', the procedure updates the mobile number and Tetra radio number of the in-charge person in TAMS_TOA.
8. The procedure then commits or rolls back the transaction based on whether an error occurred during execution.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_TOA_Audit, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties