# Procedure: sp_TAMS_GetTarSectorsByAccessDateAndLineAndDirection_SameSector
**Type:** Stored Procedure

This stored procedure retrieves Tar Sectors data based on Access Date, Line, and Direction. It also checks if the Sector is the same as the one in the TAR Status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The access date to filter by |
| @Line | nvarchar(10) | The line to filter by (DTL or NEL) |
| @Direction | nvarchar(10) | The direction to filter by |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR
* **Writes:** #TMP table

# Procedure: sp_TAMS_GetTarSectorsByTarId
**Type:** Stored Procedure

This stored procedure retrieves Tar Sectors data based on the TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The TAR ID to filter by |

### Logic Flow
1. INNER JOINs TAMS_Sector, TAMS_TAR_Sector, and TAMS_TAR tables on Sector ID and TAR ID.
2. Filters out sectors with IsBuffer = 1.
3. Orders results by [Order] and Sector.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR

# Procedure: sp_TAMS_GetTarStationsByTarId
**Type:** Stored Procedure

This stored procedure retrieves Tar Stations data based on the TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The TAR ID to filter by |

### Logic Flow
1. INNER JOINs TAMS_Station and TAMS_TAR_Station tables on Station ID and TAR ID.
2. Orders results by [Order].

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR_Station

# Procedure: sp_TAMS_GetTarWorkingLimitByPossessionId
**Type:** Stored Procedure

This stored procedure retrieves Tar Working Limit data based on the Possession ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | The Possession ID to filter by |

### Logic Flow
1. Selects id, possessionid, and redflashinglampsloc from TAMS_Possession_WorkingLimit where possessionid = @PossessionId.
2. Orders results by id asc.

### Data Interactions
* **Reads:** TAMS_Possession_WorkingLimit

# Procedure: sp_TAMS_GetWFStatusByLine
**Type:** Stored Procedure

This stored procedure retrieves WF Status data based on the Line.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line to filter by (DTL or NEL) |

### Logic Flow
1. Selects ID, Line, WFType, WFDescription, WFStatus, WFStatusId, and [Order] from TAMS_WFStatus where Line = @Line and IsActive = 1.
2. Orders results by [Order] asc.

### Data Interactions
* **Reads:** TAMS_WFStatus

# Procedure: sp_TAMS_GetWFStatusByLineAndType
**Type:** Stored Procedure

This stored procedure retrieves WF Status data based on the Line, Track Type, and Type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line to filter by (DTL or NEL) |
| @TrackType | nvarchar(50) | The track type to filter by |
| @Type | nvarchar(50) | The type to filter by |

### Logic Flow
1. Selects ID, Line, WFType, WFDescription, WFStatus, WFStatusId, and [Order] from TAMS_WFStatus where Line = @Line and TrackType = @TrackType and WFType = @Type and IsActive = 1.
2. Orders results by [Order] asc.

### Data Interactions
* **Reads:** TAMS_WFStatus

# Procedure: sp_TAMS_Get_All_Roles
**Type:** Stored Procedure

This stored procedure retrieves all roles based on the Line, Module, and Track Type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @IsExternal | BIT | Whether to include external roles |

### Logic Flow
1. Selects * from TAMS_Role where Line = 'DTL' AND Module = 'TAR' and TrackType = 'Mainline'.
2. If @IsExternal = 0, selects * from TAMS_Role where Line = 'DTL' AND Module = 'OCC' and TrackType = 'Mainline'.
3. Selects * from TAMS_Role where Line = 'NEL' AND Module = 'TAR' and TrackType = 'Mainline'.
4. If @IsExternal = 0, selects * from TAMS_Role where Line = 'NEL' AND Module = 'OCC' and TrackType = 'Mainline'.
5. Selects * from TAMS_Role where Line = 'SPLRT' AND Module = 'TAR' and TrackType = 'Mainline'.
6. If @IsExternal = 0, selects * from TAMS_Role where Line = 'SPLRT' AND Module = 'OCC' and TrackType = 'Mainline'.

### Data Interactions
* **Reads:** TAMS_Role

# Procedure: sp_TAMS_Get_ChildMenuByUserRole
**Type:** Stored Procedure

This stored procedure retrieves child menu items based on the User Role.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The user ID to filter by |
| @MenuID | NVARCHAR(100) | The menu ID to filter by |
| @IsInternet | NVARCHAR(1) | Whether to include internet roles |

### Logic Flow
1. Creates a temporary table #RoleTbl to store the role IDs.
2. Inserts the role IDs into #RoleTbl from TAMS_User_Role, TAMS_User, and TAMS_Role tables where UserID = @UserID.
3. Selects the menu items from TAMS_Menu where Active = 1 and MenuLevel = 2 and ParentMenuID = @MenuID and (IsInternet = @IsInternet or @IsInternet = 0).
4. Orders results by ID.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User, TAMS_Role, TAMS_Menu

# Procedure: sp_TAMS_Get_ChildMenuByUserRoleID
**Type:** Stored Procedure

This stored procedure retrieves child menu items based on the User Role ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The user ID to filter by |
| @MenuID | NVARCHAR(100) | The menu ID to filter by |
| @IsInternet | NVARCHAR(1) | Whether to include internet roles |

### Logic Flow
1. Creates a temporary table #RoleTbl to store the role IDs.
2. Inserts the role IDs into #RoleTbl from TAMS_User_Role, TAMS_User, and TAMS_Role tables where UserID = @UserID.
3. Selects the menu items from TAMS_Menu where Active = 1 and MenuLevel = 2 and ParentMenuID = @MenuID and (IsInternet = @IsInternet or @IsInternet = 0).
4. Orders results by ID.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User, TAMS_Role, TAMS_Menu