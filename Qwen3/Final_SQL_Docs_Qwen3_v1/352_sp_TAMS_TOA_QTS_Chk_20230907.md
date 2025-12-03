# Procedure: sp_TAMS_TOA_QTS_Chk_20230907

### Purpose
This stored procedure checks if a TAMS TOA (Trainee On Assignment) record is valid based on the provided qualification date, line, and access type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | The National Registration Identification Number of the trainee. |
| @qualdate | NVARCHAR(20) | The qualification date of the trainee. |
| @line | NVARCHAR(20) | The line number of the trainee's assignment. |
| @AccessType | NVARCHAR(20) | The access type of the trainee's assignment. |

### Logic Flow
The procedure follows these steps:

1. It initializes several variables to store the results and sets up temporary tables to store intermediate data.
2. It checks if a record exists in the TAMS Parameters table with the specified line number and qualification code, and updates the @QualCode variable accordingly.
3. It inserts a new record into the #tmpnric table with the provided nric, qualdate, line, and access type.
4. It creates a cursor to iterate over the records in the #tmpnric table, starting from the first record.
5. For each record, it checks if there is any suspension information available for the trainee's assignment. If not, it updates the qualstatus column to 'InValid'.
6. If suspension information is available, it checks if the qualification date falls within a valid period (between pq_validaccess_date and pq_validtill_date). If so, it updates the qualstatus column to 'Valid'; otherwise, it updates it to 'InValid'.
7. After iterating over all records, it selects the final values from the #tmpnric table and returns them.

### Data Interactions
* **Reads:** 
	+ TAMS_Parameters table
	+ QTS_Personnel_Qualification table
	+ QTS_Personnel table
* **Writes:**
	+ #tmpnric table
	+ #tmpqtsqc table