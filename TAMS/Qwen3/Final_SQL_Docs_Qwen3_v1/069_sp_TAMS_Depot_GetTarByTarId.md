# Procedure: sp_TAMS_Depot_GetTarByTarId

The purpose of this stored procedure is to retrieve detailed information about a specific TAR (TAR ID) from the TAMS_TAR table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The TAR ID for which to retrieve details. |

### Logic Flow
1. The procedure starts by declaring two variables, @PowerZone and @SPKSZone, to store the Power Sector and SPKS Zone information respectively.
2. It then selects the Power Sector information from the TAMS_Power_Sector table where the TAR ID matches the input parameter @TarId. The selected data is grouped by Power Sector and the results are concatenated into the @PowerZone variable.
3. If the length of @PowerZone is greater than 0, it removes the trailing comma and space to ensure proper formatting.
4. Similarly, it selects the SPKS Zone information from the TAMS_SPKSZone table where the TAR ID matches the input parameter @TarId. The selected data is grouped by SPKS Zone and the results are concatenated into the @SPKSZone variable.
5. If the length of @SPKSZone is greater than 0, it removes the trailing comma and space to ensure proper formatting.
6. Finally, the procedure retrieves the detailed information about the TAR from the TAMS_TAR table where the ID matches the input parameter @TarId.

### Data Interactions
* **Reads:** TAMS_Power_Sector, TAMS_SPKSZone, TAMS_TAR
* **Writes:** None