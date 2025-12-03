# Procedure: sp_TAMS_GetTarAccessRequirementsByTarId

### Purpose
Retrieve all selected access requirements for a specific TAR ID.

### Parameters
| Name   | Type    | Purpose |
| :----- | :------ | :------ |
| @TarId | integer | Identifier of the TAR whose access requirements are requested; defaults to 0 if omitted. |

### Logic Flow
1. Accept the @TarId parameter (default 0).  
2. Perform an implicit join between `tams_tar_accessreq` (alias `tta`) and `TAMS_Access_Requirement` (alias `tar`) where `tta.OperationRequirement = tar.id`.  
3. Filter the joined rows to those where `tta.tarid` equals the supplied @TarId and `tta.IsSelected` equals 1.  
4. Return the columns `tta.id`, `tarid`, `tar.operationrequirement`, `tta.ispower`, `tta.isselected`, and `tta.[order]` for each matching row.

### Data Interactions
* **Reads:** `tams_tar_accessreq`, `TAMS_Access_Requirement`  
* **Writes:** None