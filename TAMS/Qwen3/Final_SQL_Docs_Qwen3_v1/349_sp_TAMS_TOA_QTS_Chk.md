# Procedure: sp_TAMS_TOA_QTS_Chk

### Purpose
This stored procedure checks if a person has a valid qualification for a specific line of service, based on their access date and status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric		NVARCHAR(50) | The National Registration Identity Card number. |
| @qualdate	NVARCHAR(20) | The qualification date to check against. |
| @line	NVARCHAR(20) | The line of service for which the qualification is being checked. |
| @QualCode	NVARCHAR(20) | The qualification code to match with the person's qualifications. |

### Logic Flow
1. The procedure starts by declaring variables and setting up temporary tables.
2. It then selects the relevant data from the QTS_Personnel, QTS_Personnel_Qualification, and QTS_Qualification tables based on the input parameters.
3. If no matching records are found, the procedure sets a status of 'InValid'.
4. If matching records are found, it checks if the qualification date is within the valid access period.
5. Based on this check, the procedure sets a status of either 'Valid' or 'InValid'.
6. Finally, it returns the person's name, line of service, qualification date, qualification code, and status.

### Data Interactions
* **Reads:** QTS_Personnel, QTS_Personnel_Qualification, QTS_Qualification tables.
* **Writes:** None