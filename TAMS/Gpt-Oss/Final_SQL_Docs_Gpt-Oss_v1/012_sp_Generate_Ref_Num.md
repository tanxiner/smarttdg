# Procedure: sp_Generate_Ref_Num

### Purpose
Creates a unique reference number for a TAR form based on line, track type, and the current year.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @FormType | NVARCHAR(20)  | Type of form; only TAR is processed. |
| @Line     | NVARCHAR(20)  | Identifier for the line; may be modified if track type is Depot. |
| @TrackType| NVARCHAR(50)  | Category of track; used to locate the correct serial record. |
| @RefNum   | NVARCHAR(20)  | Output parameter that receives the generated reference number. |
| @Message  | NVARCHAR(500) | Output parameter that receives an error message if the procedure fails. |

### Logic Flow
1. Initialise an internal transaction flag and an error message holder.  
2. If no transaction is active, start a new transaction and mark that the procedure owns it.  
3. Set the maximum number counter to 1.  
4. If the form type is TAR:  
   1. Check whether a serial record exists for the current year, line, and track type.  
   2. If none exists, insert a new record with MaxNum set to 1.  
   3. If a record exists, read its MaxNum, increment it, and update the record with the new value.  
   4. If the track type is Depot, append the letter “D” to the line value.  
   5. Build the reference number by concatenating the (possibly modified) line, a hyphen, the form type, another hyphen, the four‑digit year, a hyphen, and the MaxNum padded to five digits with leading zeros.  
5. If any error occurs during the above steps, set @Message to “ERROR GENERATING REF NUM” and jump to the error handling section.  
6. On successful completion, commit the transaction if it was started internally and return @Message (which will be NULL).  
7. In the error handling section, roll back the transaction if it was started internally and return @Message.

### Data Interactions
* **Reads:** `[dbo].[TAMS_RefSerialNumber]` – selects the current MaxNum for the specified form type, line, track type, and year.  
* **Writes:** `[dbo].[TAMS_RefSerialNumber]` – inserts a new record when none exists for the year, or updates the MaxNum field of an existing record.