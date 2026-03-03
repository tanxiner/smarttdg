# Procedure: sp_TAMS_Depot_Form_Update_Access_Details
**Type:** Stored Procedure

The purpose of this stored procedure is to update access details for a TAMS Depot.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Company | NVARCHAR(50) | Company name |
| @Designation | NVARCHAR(50) | Designation |

### Logic Flow
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR
* **Writes:** TAMS_TAR

# Procedure: sp_TAMS_Depot_GetBlockedTarDates
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve blocked TAR dates for a specific line.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | Line number |

### Logic Flow
1. Retrieves TAR dates from TAMS_Block_TARDate table where line matches the input and block date is specified.
2. Orders results by block date.

### Data Interactions
* **Reads:** TAMS_Block_TARDate

# Procedure: sp_TAMS_Depot_GetPossessionDepotSectorByPossessionId
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve possession depot sector details for a specific possession ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | Possession ID |

### Logic Flow
1. Retrieves possession depot sector details from TAMS_Possession_DepotSector table where possession ID matches the input.
2. Orders results by ID.

### Data Interactions
* **Reads:** TAMS_Possession_DepotSector

# Procedure: sp_TAMS_Depot_GetTarByTarId
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve TAR details for a specific TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | TAR ID |

### Logic Flow
1. Retrieves power zone and SPKS zone details from TAMS_Power_Sector and TAMS_SPKSZone tables where TAR ID matches the input.
2. Joins TAR table with power zone and SPKS zone details to retrieve additional information.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Power_Sector, TAMS_SPKSZone

# Procedure: sp_TAMS_Depot_GetEnquiryResult_Department
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve TAR enquiry result details for a specific department.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |
| @Line | nvarchar(50) | Line number |
| @TrackType | nvarchar(50) | Track type |

### Logic Flow
1. Checks if user has the required role to view TAR enquiry results.
2. Retrieves TAR details from TAMS_TAR table where line, track type, and user ID match the input.
3. Orders results by company.

### Data Interactions
* **Reads:** TAMS_TAR

# Procedure: sp_TAMS_Depot_GetTarSectorsByAccessDateAndLine
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve TAR sector details for a specific access date and line.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | Access date |

### Logic Flow
1. Retrieves TAR sector details from TAMS_Sector table where line matches the input and access date is specified.
2. Joins TAR table with sector details to retrieve additional information.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR

# Procedure: sp_TAMS_Depot_GetTarSectorsByTarId
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve TAR sector details for a specific TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | TAR ID |

### Logic Flow
1. Retrieves TAR sector details from TAMS_TAR_Sector table where TAR ID matches the input.
2. Orders results by order and sector.

### Data Interactions
* **Reads:** TAMS_TAR_Sector, TAMS_TAR