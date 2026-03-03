# Procedure: sp_TAMS_Get_RegistrationInboxByUserID_hnin
**Type:** Stored Procedure

The procedure retrieves a list of registration inbox items for a given user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The user ID to retrieve registration inbox items for. |

### Logic Flow
1. Checks if the user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_Endorser, TAMS_WFStatus
* **Writes:** TAMS_Audit

# Procedure: sp_TAMS_Get_RegistrationInformationByRegModuleID
**Type:** Stored Procedure

The procedure retrieves registration information for a given reg module ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModuleID | INT | The reg module ID to retrieve registration information for. |

### Logic Flow
1. Checks if the reg module ID exists.
2. Retrieves registration data from TAMS_Registration, TAMS_Reg_Module, and TAMS_WFStatus tables.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus

# Procedure: sp_TAMS_Get_RolesByLineModule
**Type:** Stored Procedure

The procedure retrieves roles for a given line, track type, and module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(100) = NULL | The line to retrieve roles for. |
| @TrackType | NVARCHAR(50) = NULL | The track type to retrieve roles for. |
| @Module | NVARCHAR(100) = NULL | The module to retrieve roles for. |

### Logic Flow
1. Retrieves roles from TAMS_Role table.

### Data Interactions
* **Reads:** TAMS_Role

# Procedure: sp_TAMS_Get_SignUpStatusByLoginID
**Type:** Stored Procedure

The procedure retrieves sign-up status information for a given login ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) = NULL | The login ID to retrieve sign-up status information for. |

### Logic Flow
1. Checks if the login ID exists.
2. Retrieves access status data from TAMS_Registration and TAMS_Reg_Module tables.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module

# Procedure: sp_TAMS_Get_UserAccessRoleInfo_by_ID
**Type:** Stored Procedure

The procedure retrieves user access role information for a given user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) = NULL | The user ID to retrieve user access role information for. |

### Logic Flow
1. Checks if the user exists.
2. Retrieves user role data from TAMS_User_Role table.

### Data Interactions
* **Reads:** TAMS_User_Role