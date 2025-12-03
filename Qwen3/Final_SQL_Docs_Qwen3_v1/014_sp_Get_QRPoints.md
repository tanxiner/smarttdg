# Procedure: sp_Get_QRPoints

The purpose of this stored procedure is to retrieve a list of QR code points from the TAMS_TOA_QRCode table, ordered by line number, QR code type, and station.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | Not specified |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_TOA_QRCode table.
2. It orders the results by line number, QR code type, and station.

### Data Interactions
* **Reads:** [dbo].[TAMS_TOA_QRCode]