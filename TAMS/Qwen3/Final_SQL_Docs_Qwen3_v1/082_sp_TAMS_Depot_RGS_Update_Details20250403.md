# Procedure: sp_TAMS_Depot_RGS_Update_Details20250403

### Purpose
This stored procedure updates the details of a Depot RGS (Railway Goods Storage) by checking the qualification status and updating the relevant records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | TAR ID to update |
| @InchargeNRIC | NVARCHAR(50) | In charge NRIC |
| @MobileNo | NVARCHAR(20) | Mobile number of in charge |
| @TetraRadioNo | NVARCHAR(50) | Tetra radio number of in charge |
| @UserID | NVARCHAR(500) | User ID for auditing purposes |
| @TrackType | NVARCHAR(50) | Track type (Mainline or Depot) |

### Logic Flow
1. The procedure starts by checking if a transaction has been started. If not, it sets the internal transaction flag to 1 and begins a new transaction.
2. It then creates a temporary table #tmpnric to store the results of the qualification checks.
3. The procedure truncates the temporary table and selects the relevant data from TAMS_TOA and TAMS_TAR tables based on the TAR ID provided.
4. It then performs two string aggregation operations using STRING_AGG function to get the QTSQualCode and QTSQualCodeProt values for each line.
5. The procedure then checks if there are any valid qualifications for the in charge NRIC. If not, it sets the qualification status to 'InValid' and updates the relevant records accordingly.
6. If there are valid qualifications, it updates the in charge name, mobile number, tetra radio number, and other relevant fields based on the QTSQualCode and QTSQualCodeProt values.
7. The procedure then checks if any new in charges need to be added or existing ones updated. If so, it performs the necessary insertions, updates, and deletions.
8. Finally, the procedure commits or rolls back the transaction depending on whether an error occurred during execution.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_TOA_Audit, TAMS_TOA_Parties_Audit, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties