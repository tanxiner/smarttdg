# Procedure: sp_TAMS_RGS_Get_UpdDets

### Purpose
Retrieve the contact and radio details for a specific TAR record.

### Parameters
| Name   | Type | Purpose |
| :----- | :--- | :------ |
| @TARID | BIGINT | Identifier used to locate the record in TAMS_TOA |

### Logic Flow
1. Accept an optional TARID value.  
2. Query the TAMS_TOA table for the row where TARId equals the supplied @TARID.  
3. For that row, decrypt the InChargeNRIC field, and return it along with MobileNo and TetraRadioNo.

### Data Interactions
* **Reads:** TAMS_TOA  
* **Writes:** None  

---