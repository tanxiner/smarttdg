# Procedure: sp_Generate_Ref_Num

### Purpose
This stored procedure generates a unique reference number based on the provided form type, line, track type, and year.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @FormType	| NVARCHAR(20) | The type of form being generated. |
| @Line	| NVARCHAR(20) | The line number associated with the form. |
| @TrackType	| NVARCHAR(50) | The track type for the form. |
| @RefNum	| NVARCHAR(20) | Output parameter to store the generated reference number. |
| @Message	| NVARCHAR(500) | Output parameter to store any error message. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag and checking if a transaction is already in progress.
2. If no transaction is present, it sets the internal transaction flag and begins a new transaction.
3. It then checks if a record exists in the TAMS_RefSerialNumber table for the given form type, line, track type, and year. If no record exists, it inserts a new record with the current date and maximum number value.
4. If a record does exist, it retrieves the current maximum number value from the record and increments it by 1 to generate the next unique reference number.
5. The procedure then updates the TAMS_RefSerialNumber table with the new maximum number value.
6. Depending on the track type, it appends 'D' to the line number if it's a Depot track type.
7. Finally, it generates the reference number by concatenating the updated line number, form type, year, and maximum number value.

### Data Interactions
* Reads: TAMS_RefSerialNumber table
* Writes: TAMS_RefSerialNumber table