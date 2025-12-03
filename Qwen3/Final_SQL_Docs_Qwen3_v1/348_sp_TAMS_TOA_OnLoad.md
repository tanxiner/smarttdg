# Procedure: sp_TAMS_TOA_OnLoad

### Purpose
This stored procedure retrieves and decrypts data from the TAMS_TOA table based on a provided TOAID, returning various fields such as InchargeNRIC, InchargeName, MobileNo, and more.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TOAID | BIGINT | The ID of the TAMS_TOA record to retrieve data for. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TOA table where the Id matches the provided TOAID.
2. It then joins this data with the TAMS_TAR table based on the TARId field, which is assumed to be linked to the Id in TAMS_TOA.
3. The selected data is then decrypted using a decryption function (QTS_MaskText) applied to the InChargeNRIC field.
4. The procedure returns various fields from the decrypted data.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR