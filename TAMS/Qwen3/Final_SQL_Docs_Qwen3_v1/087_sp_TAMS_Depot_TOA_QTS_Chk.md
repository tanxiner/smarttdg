# Procedure: sp_TAMS_Depot_TOA_QTS_Chk

### Purpose
This stored procedure checks if a person has a valid qualification for a specific depot and date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric		NVARCHAR(50) = NULL, 
| @qualdate	NVARCHAR(20) = NULL,
| @line		NVARCHAR(20) = NULL,
| @QualCode	NVARCHAR(50) = NULL |

### Logic Flow
1. The procedure starts by declaring variables to store the result of the query and initializing counters for the number of qualifications found.
2. It then truncates a temporary table #tmpqtsqc, which will be used to store the results of the qualification checks.
3. The procedure selects the personnel's name from the QTS_Personnel table based on the provided nric.
4. It inserts the decrypted access ID and other relevant information into the #tmpqtsqc table for each qualification found that matches the provided line, QualCode, and date range.
5. If no qualifications are found, the procedure sets a status to 'InValid'.
6. Otherwise, it selects the last access date, valid access date, and valid till date from the #tmpqtsqc table.
7. It checks if there is a suspended till date; if so, it sets the status to 'InValid'. If not, it checks if the provided qualification date falls within the valid access date range; if not, it sets the status to 'InValid'.
8. Finally, the procedure returns the decrypted nric, name, line, qualification date, QualCode, and status.

### Data Interactions
* **Reads:** 
	+ [flexnetskgsvr].[QTSDB].[dbo].QTS_Personnel
	+ [flexnetskgsvr].[QTSDB].[dbo].QTS_Personnel_Qualification
	+ [flexnetskgsvr].[QTSDB].[dbo].QTS_Qualification
* **Writes:** None