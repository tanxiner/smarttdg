### Procedure: SP_TAMS_Depot_SaveDTCAuthComments

**Type:** Stored Procedure

**Purpose:** Saves comments from TAMS_DTC_AUTH_COMMENTS table into TAMS_Depot_Auth_Remark table.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @str | TAMS_DTC_AUTH_COMMENTS | Table containing comments to be saved |

**Logic Flow**

1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

**Data Interactions**

* Reads: None
* Writes: TAMS_Depot_Auth_Remark table

### Procedure: SP_Test

**Type:** Stored Procedure

**Purpose:** Tests the TOA system by generating a report and checking the status of a user's qualification.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @InChargeName | NVARCHAR(500) | User name |
| @InChargeStatus | NVARCHAR(20) | Qualification status |

**Logic Flow**

1. Truncates the temporary table #tmpnric.
2. Inserts a record into #tmpnric using sp_TAMS_TOA_QTS_Chk procedure.
3. Retrieves user information from #tmpnric.
4. Waits for 10 seconds.
5. Checks if the user's qualification is valid or not.
6. If invalid, updates the user's status and generates a new report.

**Data Interactions**

* Reads: TAMS_User, TAMS_User_Role, TAMS_Role, #tmpnric
* Writes: None

### Procedure: getUserInformationByID

**Type:** Stored Procedure

**Purpose:** Retrieves user information from TAMS_User table based on the provided UserID.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | User ID |

**Logic Flow**

1. Checks if the user exists in TAMS_User table.
2. Retrieves user information from TAMS_User, TAMS_User_Role, and TAMS_Role tables.

**Data Interactions**

* Reads: TAMS_User, TAMS_User_Role, TAMS_Role
* Writes: None

### Procedure: sp_Generate_Ref_Num

**Type:** Stored Procedure

**Purpose:** Generates a reference number for a specific form type, line, and track type.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @FormType | NVARCHAR(20) | Form type |
| @Line | NVARCHAR(20) | Line |
| @TrackType | NVARCHAR(50) | Track type |
| @RefNum | NVARCHAR(20) | Output reference number |
| @Message | NVARCHAR(500) | Error message |

**Logic Flow**

1. Checks if the form type, line, and track type already exist in TAMS_RefSerialNumber table.
2. If not, inserts a new record into TAMS_RefSerialNumber table with the generated reference number.

**Data Interactions**

* Reads: None
* Writes: TAMS_RefSerialNumber table

### Procedure: sp_Generate_Ref_Num_TOA

**Type:** Stored Procedure

**Purpose:** Generates a reference number for a specific form type, line, track type, and operation date.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @FormType | NVARCHAR(20) | Form type |
| @Line | NVARCHAR(20) | Line |
| @TARID | INT | TAR ID |
| @OperationDate | NVARCHAR(20) | Operation date |
| @TrackType | NVARCHAR(50) | Track type |
| @RefNum | NVARCHAR(20) | Output reference number |
| @Message | NVARCHAR(500) | Error message |

**Logic Flow**

1. Checks if the form type, line, and track type already exist in TAMS_RefSerialNumber table for the given operation date.
2. If not, inserts a new record into TAMS_RefSerialNumber table with the generated reference number.

**Data Interactions**

* Reads: None
* Writes: TAMS_RefSerialNumber table

### Procedure: sp_Get_QRPoints

**Type:** Stored Procedure

**Purpose:** Retrieves QR code points from TAMS_TOA_QRCode table.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |

**Logic Flow**

1. Retrieves QR code points from TAMS_TOA_QRCode table.
2. Orders the results by line, URL, and station.

**Data Interactions**

* Reads: TAMS_TOA_QRCode table
* Writes: None

### Procedure: sp_Get_TypeOfWorkByLine

**Type:** Stored Procedure

**Purpose:** Retrieves type of work information from TAMS_Type_Of_Work table based on the provided line and track type.

**Parameters**

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Line |
| @TrackType | NVARCHAR(50) | Track type |

**Logic Flow**

1. Retrieves type of work information from TAMS_Type_Of_Work table.
2. Filters the results by line and track type.

**Data Interactions**

* Reads: TAMS_Type_Of_Work table
* Writes: None