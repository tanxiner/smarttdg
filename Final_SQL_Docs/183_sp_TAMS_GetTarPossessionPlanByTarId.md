# Procedure: sp_TAMS_GetTarPossessionPlanByTarId

### Purpose
Retrieve possession plan details for a specific TAR identified by @TarId.

### Parameters
| Name   | Type    | Purpose |
| :----- | :------ | :------ |
| @TarId | integer | Identifier of the TAR whose possession plan is requested |

### Logic Flow
1. Accept an integer @TarId, defaulting to 0 if not supplied.  
2. Query the TAMS_Possession table for rows where the tarid column equals @TarId.  
3. For each matching row, join to the TAMS_Type_Of_Work table on the typeofworkid = id relationship.  
4. Return the selected columns: tp.id, summary, workdesc, typeofwork, workwithinpossession, takepossession, giveuppossession, remarks, poweronoff, engtrainformation, engtrainarriveloc, engtrainarrivetime, engtraindepartloc, engtraindeparttime, pcnric, pcname.

### Data Interactions
* **Reads:** TAMS_Possession, TAMS_Type_Of_Work  
* **Writes:** None