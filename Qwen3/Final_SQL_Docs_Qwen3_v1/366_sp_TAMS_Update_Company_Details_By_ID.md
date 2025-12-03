# Procedure: sp_TAMS_Update_Company_Details_By_ID

### Purpose
This stored procedure updates company details for a specific company ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CompID | INT | The ID of the company to be updated. |

### Logic Flow
1. The procedure starts by attempting to begin a transaction.
2. It then checks if a record exists in the TAMS_Company table with the specified ID (@CompID).
3. If a record is found, it updates the corresponding record in the TAMS_Company table with the new company details.
4. After updating the record, it commits the transaction.

### Data Interactions
* **Reads:** TAMS_Company
* **Writes:** TAMS_Company