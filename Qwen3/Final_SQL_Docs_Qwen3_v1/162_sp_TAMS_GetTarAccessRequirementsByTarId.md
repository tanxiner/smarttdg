# Procedure: sp_TAMS_GetTarAccessRequirementsByTarId

### Purpose
This stored procedure retrieves access requirements for a specific Tar (Transportation Asset Management System) ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the Tar for which to retrieve access requirements. |

### Logic Flow
1. The procedure starts by selecting data from two tables: `tams_tar_accessreq` and `TAMS_Access_Requirement`.
2. It filters the results to only include rows where the `OperationRequirement` in `tams_tar_accessreq` matches the ID of the corresponding row in `TAMS_Access_Requirement`.
3. The procedure then further filters the results to only include rows where the `tarid` in `tams_tar_accessreq` matches the provided `@TarId`.
4. Finally, it selects specific columns from the filtered data and returns them.

### Data Interactions
* **Reads:** `tams_tar_accessreq`, `TAMS_Access_Requirement`
* **Writes:** None