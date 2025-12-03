# Procedure: sp_Generate_Ref_Num_TOA

### Purpose
Creates a unique reference number for a TOA form and updates the serial‑number tracker for that form type, line, and operation date.

### Parameters
| Name            | Type          | Purpose |
| :-------------- | :------------ | :------ |
| @FormType       | NVARCHAR(20)  | Type of form to generate a reference for (e.g., 'TOA'). |
| @Line           | NVARCHAR(20)  | Identifier for the line (e.g., 'DTL', 'NEL'). |
| @TARID          | INT           | Primary key of the TAR record whose access date is used. |
| @OperationDate  | NVARCHAR(20)  | Date of the operation, formatted as DD/MM/YYYY. |
| @TrackType      | NVARCHAR(50)  | Track classification; defaults to 'MainLine'. |
| @RefNum         | NVARCHAR(20)  OUTPUT | Generated reference number returned to the caller. |
| @Message        | NVARCHAR(500) OUTPUT | Status or error message returned to the caller. |

### Logic Flow
1. **Transaction Setup** – If no active transaction exists, start a new one and flag that the procedure owns the transaction.  
2. **Variable Initialization** – Set default values for internal variables, including a starting serial number of 1.  
3. **Retrieve Access Date** – Query the TAMS_TAR table for the AccessDate of the record identified by @TARID.  
4. **Format Date and Time Parts** – Convert the AccessDate to DD/MM/YYYY format and the current time to HH:MM:SS, then extract DDMM and hhmm components for the reference string.  
5. **Process TOA Form** –  
   a. If @FormType equals 'TOA', check whether a row exists in TAMS_RefSerialNumber for the current year, operation date, line, and track type.  
   b. **Insert Path** – If no row exists, insert a new record with MaxNum set to 1.  
   c. **Update Path** – If a row exists, increment MaxNum by one and retrieve the updated value.  
6. **Adjust Line for Depot** – If @TrackType is 'Depot', append a trailing 'D' to @Line.  
7. **Build Reference Number** – Concatenate @Line, @FormType, DDMM, hhmm, and the serial number (MaxNum) with hyphens to form the final reference string, and assign it to @RefNum.  
8. **Error Handling** – If any error occurs, set @Message to a generic error string and jump to the error trap.  
9. **Commit or Rollback** – Commit the transaction if the procedure started it; otherwise leave the transaction unchanged. Return @Message.  

### Data Interactions
* **Reads:**  
  - TAMS_TAR (to obtain AccessDate)  
  - TAMS_RefSerialNumber (to check and retrieve MaxNum)  

* **Writes:**  
  - TAMS_RefSerialNumber (INSERT or UPDATE of MaxNum)  

---