# Procedure: sp_TAMS_TOA_GenURL_QRCode

This stored procedure generates a URL and QR code for each record in the TAMS_TOA_URL table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ID | int | Unique identifier of the record to generate URL and QR code for |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_TOA_URL table.
2. It retrieves the ID, PLine, PLoc, PType, EncPLine, EncPLoc, EncPType, and GenURL for each record.
3. The selected data is then returned as output.

### Data Interactions
* **Reads:** [dbo].[TAMS_TOA_URL]
* **Writes:** None