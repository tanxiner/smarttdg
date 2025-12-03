# Procedure: sp_TAMS_GetTarByLineAndTarAccessDate

### Purpose
Retrieve all TAR records that match a specific line and access date.

### Parameters
| Name        | Type          | Purpose |
| :---        | :---          | :--- |
| @Line       | nvarchar(10)  | Optional line identifier to filter records. |
| @AccessDate | nvarchar(50)  | Optional date string (dd/mm/yyyy) to filter records. |

### Logic Flow
1. Accept optional @Line and @AccessDate parameters.  
2. Convert @AccessDate from a string to a datetime value using style 103 (day/month/year).  
3. Query the TAMS_TAR table for rows where the Line column equals @Line and the AccessDate column equals the converted datetime.  
4. Return all columns of the matching rows.

### Data Interactions
* **Reads:** TAMS_TAR  
* **Writes:** None