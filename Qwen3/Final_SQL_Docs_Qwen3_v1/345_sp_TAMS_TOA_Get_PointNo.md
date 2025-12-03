# Procedure: sp_TAMS_TOA_Get_PointNo

This procedure retrieves the point number associated with a given TOA (TAMs Toa) ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TOAID | BIGINT | The ID of the TAMS Toa to retrieve the point number for. |

### Logic Flow
1. The procedure first selects the ProtectionType from the TAMS_TOA table where the Id matches the provided TOAID.
2. It then selects the Sno (point number) and PointNo columns from the TAMS_TOA_PointNo table, filtering by the same TOAID as before, and orders the results in ascending order by Sno.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TOA_PointNo tables