# Procedure: sp_TAMS_TOA_QTS_Chk_20230323

### Purpose
This stored procedure checks if a TAMS TOA (Training on Assignment) record is valid for a given line of rail and access type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | The National Registration Identification Number. |
| @qualdate | NVARCHAR(20) | The qualification date. |
| @line | NVARCHAR(20) | The line of rail. |
| @AccessType | NVARCHAR(20) | The access type. |

### Logic Flow
1. The procedure starts by declaring variables to store the message, EPC counter, BLC counter, RTC counter, and return value.
2. It then creates two temporary tables, #tmpqtsqc and #tmpnric, to store the qualification data and TAMS TOA records respectively.
3. The procedure truncates these tables before processing new data.
4. It selects the qualification code from the TAMS Parameters table based on the line of rail and access type.
5. For each TAMS TOA record in the #tmpnric table, it checks if there is a matching qualification record in the QTS_Personnel_Qualification and QTS_Personnel tables.
6. If no matching record is found, it updates the TAMS TOA record with an invalid status.
7. If a matching record is found, it checks if there is any suspension information for the qualification record.
8. If there is no suspension information, it updates the TAMS TOA record with a valid status.
9. The procedure then closes the cursor and deallocates resources.

### Data Interactions
* **Reads:** 
	+ TAMS_Parameters table
	+ QTS_Personnel_Qualification table
	+ QTS_Personnel table
	+ #tmpqtsqc table
	+ #tmpnric table
* **Writes:** 
	+ #tmpqtsqc table
	+ #tmpnric table