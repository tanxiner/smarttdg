# Procedure: sp_TAMS_TOA_QTS_Chk_20230323_M

### Purpose
This stored procedure checks the validity of a TAMS TOA (Training on Assignment) record based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | The National Registration Identification Number. |
| @qualdate | NVARCHAR(20) | The qualification date. |
| @line | NVARCHAR(20) | The line number. |
| @AccessType | NVARCHAR(20) | The access type. |

### Logic Flow
1. Initialize variables to store the message, EPC counter, BLC counter, RTC counter, and return value.
2. Create temporary tables #tmpqtsqc and #tmpnric to store the qualification data and personal details, respectively.
3. Truncate the existing data in these tables.
4. Retrieve the qualification code from TAMS_Parameters based on the provided line number and date.
5. Insert a new record into #tmpnric with the provided nric, namestr, qualdate, qualcode, line, and qualstatus.
6. Create a cursor to iterate through the records in #tmpnric.
7. For each record:
   1. Check if there is any suspension information for the current record.
      - If yes, update the qualstatus to 'Valid' or 'InValid' based on the presence of suspension information.
      - If no suspension information, check if the qualification date falls within a valid period.
         - If yes, update the qualstatus to 'Valid'.
         - If not, update the qualstatus to 'InValid'.
8. Close and deallocate the cursor.
9. Select and return the updated records from #tmpnric.

### Data Interactions
* Reads: 
  + TAMS_Parameters
  + QTS_Personnel
  + QTS_Qualification
  + QTS_Personnel_Qualification
* Writes:
  + #tmpqtsqc
  + #tmpnric