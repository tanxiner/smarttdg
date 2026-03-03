# Procedure: SP_TAMS_Depot_GetDTCRoster

### Purpose
Retrieve the roster details for depot duties on a specified date, including shift, roster code, staff name, and login ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @date | Date | The operation date used to filter duty roster entries. |

### Logic Flow
1. Disable row‑count messages to keep the result set clean.  
2. Identify all unique roster codes that belong to depot track types by querying the duty roster table.  
3. For each of those roster codes, attempt to find a matching duty roster entry that also matches the supplied operation date and depot track type.  
4. Join the found duty roster entry to the user table using the duty staff identifier.  
5. Return a row for each roster code containing the shift, roster code, user name, and login ID. If no matching duty roster entry exists for a roster code on the given date, the shift, name, and login ID fields will be null.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_User  
* **Writes:** None