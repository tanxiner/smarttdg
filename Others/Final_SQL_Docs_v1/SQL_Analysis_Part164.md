# Procedure: sp_TAMS_TOA_Register_20230107_M
**Type:** Stored Procedure

### Purpose
This stored procedure performs the business task of registering a new TOA (TAR Management System) record, including validating user information and updating TAR status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line number for validation purposes |
| @Type | NVARCHAR(20) | Type of TOA (e.g., NEL, etc.) |
| @Loc | NVARCHAR(20) | Location of the TAR station |
| @TARNo | NVARCHAR(30) | TAR number to be registered |
| @NRIC | NVARCHAR(20) | National Registration Identity Card number |
| @TOAID | BIGINT OUTPUT | ID of the newly created TOA record |
| @Message | NVARCHAR(500) OUTPUT | Error message or success message |

### Logic Flow
1. Checks if user exists by comparing NRIC with InChargeNRIC in TAMS_TOA table.
2. Inserts into Audit table for TARId = @TARID.
3. Validates TAR status and updates OperationDate accordingly.
4. If TAR status is valid, inserts new TOA record into TAMS_TOA table.
5. Updates TAR station count for selected TAR.
6. Checks if user information matches with InChargeNRIC in TAMS_TOA table.

### Data Interactions
* **Reads:** 
	+ TAMS_TAR
	+ TAMS_TAR_Station
	+ TAMS Parameters
	+ TAMS_TOA
	+ TAMS_TOA_Audit
	+ TAMS_TOA_Parties
* **Writes:**
	+ TAMS_TOA table
	+ TAMS_TOA_Audit table
	+ TAMS_TOA_Parties table