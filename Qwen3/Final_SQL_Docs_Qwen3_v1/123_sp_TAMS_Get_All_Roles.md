# Procedure: sp_TAMS_Get_All_Roles

The procedure retrieves all roles from the TAMS_Role table based on various conditions.

### Parameters
| Name | Type | Purpose |
| @IsExternal | BIT | Indicates whether to include external roles or not |

### Logic Flow
1. The procedure first selects all roles from the TAMS_Role table where Line = 'DTL' AND Module = 'TAR' and TrackType = 'Mainline'.
2. If @IsExternal is 0, it then selects all roles from the TAMS_Role table where Line = 'DTL' AND Module = 'OCC' and TrackType = 'Mainline'.
3. The procedure repeats steps 1 and 2 for the lines 'NEL', 'SPLRT', and their respective modules.
4. It also selects roles from the TAMS_Role table where Line is 'DTL', 'NEL', or 'SPLRT' AND Module = 'TAR' with TrackType = 'Depot'.
5. Finally, it selects roles from the TAMS_Role table where Line = 'NEL' AND Module = 'DCC' and TrackType = 'Depot'.

### Data Interactions
* **Reads:** TAMS_Role (explicitly selected tables)
* **Writes:** None