Here are the documented procedures:

### Procedure: sp_TAMS_Get_ChildMenuByUserRole_20231009
**Type:** Stored Procedure

Purpose: Retrieves child menu items based on user role.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The ID of the user to retrieve menu items for. |

Logic Flow:
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

Data Interactions:
* Reads: TAMS_User_Role, TAMS_User, TAMS_Role, TAMS_Menu
* Writes: None

### Procedure: sp_TAMS_Get_CompanyInfo_by_ID
**Type:** Stored Procedure

Purpose: Retrieves company information by ID.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CompanyID | NVARCHAR(100) | The ID of the company to retrieve information for. |

Logic Flow:
1. Checks if company exists.
2. Returns company information.

Data Interactions:
* Reads: TAMS_Company
* Writes: None

### Procedure: sp_TAMS_Get_CompanyListByUENCompanyName
**Type:** Stored Procedure

Purpose: Retrieves a list of companies by UEN and Company name.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @SearchUEN | NVARCHAR(100) | The search string for the UEN.
| @SearchCompanyName | NVARCHAR(200) | The search string for the company name. |

Logic Flow:
1. Searches for companies in TAMS_Company table where UEN matches @SearchUEN and Company name matches @SearchCompanyName.

Data Interactions:
* Reads: TAMS_Company
* Writes: None

### Procedure: sp_TAMS_Get_Depot_TarEnquiryResult_Header
**Type:** Stored Procedure

Purpose: Retrieves TAR enquiry result header data based on user ID, track type, and other parameters.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | INT | The ID of the user to retrieve TAR data for.
| @Line | NVARCHAR(50) | The line number to filter by.
| @TrackType | NVARCHAR(50) | The track type to filter by.
| @TarType | NVARCHAR(50) | The tar type to filter by.
| @AccessType | NVARCHAR(50) | The access type to filter by.
| @TarStatusId | INT | The TAR status ID to filter by.
| @AccessDateFrom | NVARCHAR(50) | The start date for the access period.
| @AccessDateTo | NVARCHAR(50) | The end date for the access period.
| @Department | NVARCHAR(50) | The department to filter by.

Logic Flow:
1. Checks if user has specific roles and permissions.
2. Filters TAR data based on user ID, track type, tar type, access type, TAR status ID, access dates, and department.
3. Returns the filtered TAR data with row numbers.

Data Interactions:
* Reads: TAMS_TAR, TAMS_WFStatus
* Writes: None

### Procedure: sp_TAMS_Get_External_UserInfo_by_LoginIDPWD
**Type:** Stored Procedure

Purpose: Retrieves external user information by login ID and password.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) | The login ID to retrieve user information for.
| @LoginPWD | NVARCHAR(200) | The password to verify against the stored password. |

Logic Flow:
1. Checks if external user exists with matching login ID and password.

Data Interactions:
* Reads: TAMS_User
* Writes: None

### Procedure: sp_TAMS_Get_ParaValByParaCode
**Type:** Stored Procedure

Purpose: Retrieves parameter values by para code.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @paraCode | NVARCHAR(200) | The para code to retrieve value for.
| @paraValue1 | NVARCHAR(200) | The value to filter by. |

Logic Flow:
1. Searches for parameter values in TAMS_Parameters table where para code matches @paraCode and para value matches @paraValue1.

Data Interactions:
* Reads: TAMS_Parameters
* Writes: None

### Procedure: sp_TAMS_Get_ParentMenuByUserRole
**Type:** Stored Procedure

Purpose: Retrieves parent menu items based on user role.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The ID of the user to retrieve menu items for.
| @IsInternet | NVARCHAR(1) | Whether to include internet menus. |

Logic Flow:
1. Checks if user exists and has specific roles and permissions.
2. Filters parent menu items based on user role and whether to include internet menus.

Data Interactions:
* Reads: TAMS_User_Role, TAMS_Menu
* Writes: None

### Procedure: sp_TAMS_Get_RegistrationCompanyInformationbyRegID
**Type:** Stored Procedure

Purpose: Retrieves registration company information by registration ID.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The registration ID to retrieve information for. |

Logic Flow:
1. Checks if registration exists with matching ID.
2. Returns registration information.

Data Interactions:
* Reads: TAMS_Reg_Module, TAMS_Registration
* Writes: None