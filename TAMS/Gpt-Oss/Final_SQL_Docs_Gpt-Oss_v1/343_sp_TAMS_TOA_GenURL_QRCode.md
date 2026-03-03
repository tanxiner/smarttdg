# Procedure: sp_TAMS_TOA_GenURL_QRCode

### Purpose
Retrieve URL generation details for TOA records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
|  |  |  |

### Logic Flow
1. Execute a SELECT statement that retrieves the columns `ID`, `PLine`, `PLoc`, `PType`, `EncPLine`, `EncPLoc`, `EncPType`, and `GenURL` from the table `TAMS_TOA_URL`.  
2. Return the result set to the caller.

### Data Interactions
* **Reads:** `TAMS_TOA_URL`  
* **Writes:** None

---