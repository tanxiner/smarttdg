# Procedure: sp_TAMS_TOA_QTS_Chk
**Type:** Stored Procedure

The purpose of this stored procedure is to check if a user has valid access to a specific line and qualification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | The National Registration Identity Number (NRIC) of the user. |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** [FLEXNETSKGSVR].[QTSDB].[dbo].QTS_Personnel, [FLEXNETSKGSVR].[QTSDB].[dbo].QTS_Personnel_Qualification, [FLEXNETSKGSVR].[QTSDB].[dbo].QTS_Qualification
* **Writes:** [FLEXNETSKGSVR].[QTSDB].[dbo].QTS_Personnel_Audit

---

# Procedure: sp_TAMS_TOA_QTS_Chk_20230323
**Type:** Stored Procedure

The purpose of this stored procedure is to check if a user has valid access to a specific line and qualification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | The National Registration Identity Number (NRIC) of the user. |
| @qualdate | NVARCHAR(20) | The date of the qualification. |
| @line | NVARCHAR(20) | The line number. |
| @AccessType | NVARCHAR(20) | The access type. |

### Logic Flow
1. Retrieves the access code for the specified line.
2. Checks if a record exists in the #tmpnric table with the same NRIC and qualification date.
3. If no record is found, updates the record with the user's name and sets the qualification status to 'InValid'.
4. If a record is found, checks if there is any suspension information for the user.
5. If no suspension information is found, checks if the qualification date is within the valid access period.
6. If the qualification date is within the valid access period, updates the record with the user's name and sets the qualification status to 'Valid'.
7. If the qualification date is not within the valid access period, updates the record with the user's name and sets the qualification status to 'InValid'.

### Data Interactions
* **Reads:** [FLEXNETSKGSVR].[QTSDB].[dbo].TAMS_Parameters, [FLEXNETSKGSVR].[QTSDB].[dbo].QTS_Personnel, [FLEXNETSKGSVR].[QTSDB].[dbo].QTS_Personnel_Qualification, [FLEXNETSKGSVR].[QTSDB].[dbo].QTS_Qualification
* **Writes:** [FLEXNETSKGSVR].[QTSDB].[dbo].QTS_Personnel_Audit