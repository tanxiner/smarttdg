Here are the documented procedures:

### sp_TAMS_TOA_Add_Parties

Purpose: This stored procedure adds parties to a TAMS TOA record.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesFIN | NVARCHAR(50) | The FIN number of the party |
| @PartiesName | NVARCHAR(200) | The name of the party |
| @IsTMC | NVARCHAR(5) | Whether the party is in charge (Y/N) |
| @NoOfParties | BIGINT | The number of parties to add |
| @TOAID | BIGINT | The ID of the TAMS TOA record |
| @Message | NVARCHAR(500) | An output parameter containing a message |

Logic Flow:
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

Data Interactions:
* Reads: None
* Writes: TAMS_TOA, TAMS_TOA_Parties

### sp_TAMS_TOA_Add_Parties1

Purpose: This stored procedure adds parties to a TAMS TOA record (similar to sp_TAMS_TOA_Add_Parties).

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesFIN | NVARCHAR(50) | The FIN number of the party |
| @PartiesName | NVARCHAR(200) | The name of the party |
| @IsTMC | NVARCHAR(5) | Whether the party is in charge (Y/N) |
| @NoOfParties | BIGINT | The number of parties to add |
| @TOAID | BIGINT | The ID of the TAMS TOA record |
| @Message | NVARCHAR(500) | An output parameter containing a message |

Logic Flow:
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

Data Interactions:
* Reads: None
* Writes: TAMS_TOA, TAMS_TOA_Parties

### sp_TAMS_TOA_Add_PointNo

Purpose: This stored procedure adds a point number to a TAMS TOA record.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @pointno | NVARCHAR(200) | The point number to add |
| @toaid | BIGINT | The ID of the TAMS TOA record |
| @Message | NVARCHAR(500) | An output parameter containing a message |
| @CreatedBy | NVARCHAR(50) | The user who added the point number |

Logic Flow:
1. Inserts into TAMS_TOA_PointNo table.

Data Interactions:
* Reads: None
* Writes: TAMS_TOA_PointNo

### sp_TAMS_TOA_Add_ProtectionType

Purpose: This stored procedure adds a protection type to a TAMS TOA record.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @pointno | dbo.Point | The point number to add protection type for |
| @protectiontype | CHAR(5) | The protection type (e.g. 'Y' for yes, 'N' for no) |
| @toaid | BIGINT | The ID of the TAMS TOA record |
| @Message | NVARCHAR(500) | An output parameter containing a message |
| @CreatedBy | NVARCHAR(50) | The user who added the protection type |

Logic Flow:
1. Updates TAMS_TOA table with new protection type.
2. Deletes existing point numbers from TAMS_TOA_PointNo table.
3. Inserts new point numbers into TAMS_TOA_PointNo table.

Data Interactions:
* Reads: None
* Writes: TAMS_TOA, TAMS_TOA_PointNo

### sp_TAMS_TOA_BookOut_Parties

Purpose: This stored procedure books out parties from a TAMS TOA record.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesID | BIGINT | The ID of the party to book out |
| @TOAID | BIGINT | The ID of the TAMS TOA record |
| @Message | NVARCHAR(500) | An output parameter containing a message |

Logic Flow:
1. Updates BookOutTime and BookInStatus in TAMS_TOA_Parties table.

Data Interactions:
* Reads: None
* Writes: TAMS_TOA_Parties

### sp_TAMS_TOA_Delete_Parties

Purpose: This stored procedure deletes parties from a TAMS TOA record.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesID | BIGINT | The ID of the party to delete |
| @TOAID | BIGINT | The ID of the TAMS TOA record |
| @Message | NVARCHAR(500) | An output parameter containing a message |

Logic Flow:
1. Checks if there are at least 2 parties left in the TAMS TOA record.
2. Deletes parties from TAMS_TOA_Parties table.

Data Interactions:
* Reads: None
* Writes: TAMS_TOA_Parties

### sp_TAMS_TOA_Delete_PointNo

Purpose: This stored procedure deletes a point number from a TAMS TOA record.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @pointid | BIGINT | The ID of the point number to delete |
| @TOAID | BIGINT | The ID of the TAMS TOA record |
| @Message | NVARCHAR(500) | An output parameter containing a message |

Logic Flow:
1. Deletes point number from TAMS_TOA_PointNo table.

Data Interactions:
* Reads: None
* Writes: TAMS_TOA_PointNo

### sp_TAMS_TOA_GenURL

Purpose: This stored procedure generates URLs for TAMS TOA stations.

Logic Flow:
1. Selects station information from TAMS_Station table.

Data Interactions:
* Reads: TAMS_Station

### sp_TAMS_TOA_GenURL_QRCode

Purpose: This stored procedure generates QR codes for TAMS TOA stations.

Logic Flow:
1. Selects station information from TAMS_TOA_URL table.

Data Interactions:
* Reads: TAMS_TOA_URL

### sp_TAMS_TOA_Get_Parties

Purpose: This stored procedure retrieves parties from a TAMS TOA record.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TOAID | BIGINT | The ID of the TAMS TOA record |

Logic Flow:
1. Retrieves NoOfParties from TAMS_TOA table.
2. Retrieves party information (name, NRIC, etc.) from TAMS_TOA_Parties table.

Data Interactions:
* Reads: TAMS_TOA, TAMS_TOA_Parties

### sp_TAMS_TOA_Get_PointNo

Purpose: This stored procedure retrieves point numbers from a TAMS TOA record.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TOAID | BIGINT | The ID of the TAMS TOA record |

Logic Flow:
1. Retrieves ProtectionType from TAMS_TOA table.
2. Retrieves point numbers from TAMS_TOA_PointNo table.

Data Interactions:
* Reads: TAMS_TOA, TAMS_TOA_PointNo

### sp_TAMS_TOA_Get_Station_Name

Purpose: This stored procedure retrieves station names for a given line and station code.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the station |
| @StationName | NVARCHAR(20) | The name of the station |

Logic Flow:
1. Selects station information from TAMS_Station table.

Data Interactions:
* Reads: TAMS_Station

### sp_TAMS_TOA_Login

Purpose: This stored procedure logs in a user to access TAMS TOA data.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARNo | NVARCHAR(50) | The TAR number of the user |
| @TPOPCNRIC | NVARCHAR(50) | The POPC NRIC of the user |
| @Message | NVARCHAR(500) | An output parameter containing a message |

Logic Flow:
1. Checks if user exists.
2. Returns ID.

Data Interactions:
* Reads: None
* Writes: TAMS_TAR

### sp_TAMS_TOA_OnLoad

Purpose: This stored procedure loads data for a given TAMS TOA record.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TOAID | BIGINT | The ID of the TAMS TOA record |

Logic Flow:
1. Retrieves station information from TAMS_TAR table.
2. Retrieves point numbers and other data from TAMS_TOA_PointNo table.

Data Interactions:
* Reads: TAMS_TAR, TAMS_TOA_PointNo