# Procedure: sp_TAMS_Depot_RGS_Update_Details

### Purpose
This stored procedure updates the details of a Depot RGS (Railway Goods Storage) by checking the qualification status and updating the relevant records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID of the Depot RGS to be updated. |
| @InchargeNRIC | NVARCHAR(50) | The Incharge NRIC of the Depot RGS. |
| @MobileNo | NVARCHAR(20) | The Mobile No of the Incharge. |
| @TetraRadioNo | NVARCHAR(50) | The Tetra Radio No of the Incharge. |
| @UserID | NVARCHAR(500) | The UserID of the user updating the Depot RGS. |
| @TrackType | NVARCHAR(50)='Mainline' | The track type of the Depot RGS (default: Mainline). |

### Logic Flow
The procedure follows these steps:

1. It checks if a transaction has been started and sets an internal flag `@IntrnlTrans` accordingly.
2. It creates a temporary table `#tmpnric` to store the results of the qualification check.
3. It truncates the temporary table and then populates it with the results of the qualification check for each line in the Depot RGS.
4. It checks if there are any invalid qualifications and sets the corresponding variables accordingly.
5. If there are no invalid qualifications, it updates the relevant records in the `TAMS_TOA` table and inserts audit records into the `TAMS_TOA_Audit` and `TAMS_TOA_Parties_Audit` tables.
6. If there are invalid qualifications, it sets an error message and returns it to the caller.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_TOA_Audit, TAMS_TOA_Parties_Audit
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties_Audit