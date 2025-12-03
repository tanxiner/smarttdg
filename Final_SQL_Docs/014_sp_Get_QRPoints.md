# Procedure: sp_Get_QRPoints

### Purpose
Retrieve QR code point records for reporting or display.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| None | – | – |

### Logic Flow
1. Execute a SELECT statement that pulls the columns `Sno`, `Line`, `Station`, `Type`, `URL`, and `QRCode` from the table `TAMS_TOA_QRCode`.  
2. Order the result set first by the second column (`Line`), then by the fourth column (`Type`), and finally by the third column (`Station`).  
3. Return the ordered rows to the caller.

### Data Interactions
* **Reads:** `TAMS_TOA_QRCode`  
* **Writes:** None