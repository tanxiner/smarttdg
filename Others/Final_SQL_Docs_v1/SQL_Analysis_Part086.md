# Procedure: sp_TAMS_OCC_Generate_Authorization_Trace
**Type:** Stored Procedure

The purpose of this stored procedure is to generate an authorization trace for a given line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number for which the authorization trace is being generated. |
| @AccessDate | NVARCHAR(20) | The access date for which the authorization trace is being generated. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** [dbo].[TAMS_Traction_Power], [dbo].[TAMS_OCC_Auth], [dbo].[TAMS_Endorser], [dbo].[TAMS_Workflow]
* **Writes:** [dbo].[TAMS_OCC_Auth]

The procedure starts by setting the current date and time. It then checks if an access date has been provided, and if so, sets the derived operation date and access date accordingly.

Next, it retrieves the workflow ID for the given line and access date from the TAMS_Workflow table. If no workflow ID is found, it returns an empty result set.

The procedure then retrieves the endorser ID for the workflow ID from the TAMS_Endorser table. It also checks if the endorser has a level of 1 and if their effective date and expiry date are within the current date range.

If the endorser is found, the procedure creates two temporary tables: #TmpTARSectors and #TmpOCCAuth. The first table stores information about the traction power sectors for each line, while the second table stores information about the OCC authentication status for each line.

The procedure then inserts data into these temporary tables based on the given line and access date. It also updates the IsBuffer and PowerOn columns in the #TmpOCCAuth table based on the presence of a buffer and power-on status in the #TmpTARSectors table.

After populating the temporary tables, the procedure retrieves the ID, Line, OperationDate, AccessDate, TractionPowerId, Remark, PFRRemark, OCCAuthStatusId, IsBuffer, PowerOn, PowerOffTime, RackedOutTime from the #TmpOCCAuth table and inserts them into the TAMS_OCC_Auth table.

Finally, the procedure creates a temporary table for the OCC authentication workflow and inserts data into it based on the retrieved endorser ID. It also updates the FISTestResult column in the #TmpOCCAuthWorkflow table.

The procedure ends by dropping the temporary tables and returning the result set from the TAMS_OCC_Auth table.

# Procedure: sp_TAMS_OCC_GetEndorserByWorkflowId
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve an endorser for a given workflow ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ID | INT | The workflow ID for which the endorser is being retrieved. |

### Logic Flow
1. Retrieves the endorser ID from the TAMS_Endorser table based on the given workflow ID.
2. Returns the endorser data.

### Data Interactions
* **Reads:** [dbo].[TAMS_Endorser]
* **Writes:** None

The procedure simply retrieves the endorser ID for the given workflow ID from the TAMS_Endorser table and returns the corresponding endorser data.

# Procedure: sp_TAMS_OCC_GetOCCAuthByLineAndAccessDate
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve OCC authentication data for a given line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number for which the OCC authentication data is being retrieved. |
| @AccessDate | NVARCHAR(50) | The access date for which the OCC authentication data is being retrieved. |

### Logic Flow
1. Retrieves the OCC authentication ID from the TAMS_OCC_Auth table based on the given line and access date.
2. Returns the OCC authentication data.

### Data Interactions
* **Reads:** [dbo].[TAMS_OCC_Auth]
* **Writes:** None

The procedure simply retrieves the OCC authentication ID for the given line and access date from the TAMS_OCC_Auth table and returns the corresponding OCC authentication data.