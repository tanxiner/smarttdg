# Procedure: sp_TAMS_Get_All_Roles

### Purpose
Retrieve all role records from **TAMS_Role** for specified lines, modules, and track types, optionally including OCC module roles when the caller is not external.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @IsExternal | BIT | Determines whether OCC module roles are included (0 = include, 1 = exclude). |

### Logic Flow
1. Return all roles where **Line = 'DTL'**, **Module = 'TAR'**, and **TrackType = 'Mainline'**.  
2. If **@IsExternal = 0**, also return roles where **Line = 'DTL'**, **Module = 'OCC'**, and **TrackType = 'Mainline'**.  
3. Return all roles where **Line = 'NEL'**, **Module = 'TAR'**, and **TrackType = 'Mainline'**.  
4. If **@IsExternal = 0**, also return roles where **Line = 'NEL'**, **Module = 'OCC'**, and **TrackType = 'Mainline'**.  
5. Return all roles where **Line = 'SPLRT'**, **Module = 'TAR'**, and **TrackType = 'Mainline'**.  
6. If **@IsExternal = 0**, also return roles where **Line = 'SPLRT'**, **Module = 'OCC'**, and **TrackType = 'Mainline'**.  
7. Return all roles where **Line = 'DTL'**, **Module = 'TAR'**, and **TrackType = 'Depot'**.  
8. Return all roles where **Line = 'NEL'**, **Module = 'TAR'**, and **TrackType = 'Depot'**.  
9. Return all roles where **Line = 'SPLRT'**, **Module = 'TAR'**, and **TrackType = 'Depot'**.  
10. Return all roles where **Line = 'NEL'**, **Module = 'DCC'**, and **TrackType = 'Depot'**.  

Each step issues a separate SELECT; the combined result set contains all matching rows.

### Data Interactions
* **Reads:** TAMS_Role  
* **Writes:** None

---