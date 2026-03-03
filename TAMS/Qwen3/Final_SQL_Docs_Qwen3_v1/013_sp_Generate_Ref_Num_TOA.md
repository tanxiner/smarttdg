# Procedure: sp_Generate_Ref_Num_TOA

### Purpose
This stored procedure generates a reference number based on the provided parameters and updates the TAMS_RefSerialNumber table accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @FormType | NVARCHAR(20) | The type of form being generated (e.g. TOA, DTL). |
| @Line | NVARCHAR(20) | The line number associated with the form. |
| @TARID | Int | The ID of the TAR record to retrieve access date from. |
| @OperationDate | NVARCHAR(20) | The operation date for the form. |
| @TrackType | NVARCHAR(50) | The track type (e.g. Depot, NEL). |
| @RefNum | NVARCHAR(20) | Output parameter to store the generated reference number. |
| @Message | NVARCHAR(500) | Output parameter to store any error messages. |

### Logic Flow
1. The procedure checks if a transaction is already active and sets an internal transaction flag accordingly.
2. It retrieves the access date from the TAMS_TAR table based on the provided TARID.
3. If the form type is TOA, it checks if a record exists in the TAMS_RefSerialNumber table with the same line number, track type, year, operation date, and form type. If no record exists, it inserts a new record with the current maximum number value incremented by 1.
4. If a record already exists, it updates the MaxNum field of that record to increment its value by 1.
5. It generates the reference number based on the line number, form type, access date, and current time.
6. If an error occurs during the generation process, it sets the @Message output parameter with an error message.

### Data Interactions
* Reads: TAMS_TAR table to retrieve access date for TARID
* Writes: TAMS_RefSerialNumber table to insert or update records