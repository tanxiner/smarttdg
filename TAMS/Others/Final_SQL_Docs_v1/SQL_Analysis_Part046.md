**sp_TAMS_Form_Save_Possession_DepotSector**

Purpose: Saves a new possession sector into the database.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sector | NVARCHAR(4000) | The sector to be saved. |
| @PowerOff | INT | The power off status of the sector. |
| @NoOFSCD | INT | The number of SCDs in the sector. |
| @BreakerOut | NVARCHAR(5) | Whether the breaker is out or not. |
| @PossID | BIGINT | The ID of the possession. |
| @Message | NVARCHAR(500) | An output parameter to store any error message. |

Logic Flow:
1. Checks if a transaction exists.
2. If no transaction, starts a new one.
3. Checks if a sector already exists for the given possession ID and sector.
4. If not found, inserts a new record into the TAMS_Possession_DepotSector table.
5. If an error occurs during insertion, rolls back the transaction and sets the @Message parameter to 'ERROR INSERTING INTO TAMS_TAR'.
6. If no errors, commits the transaction and returns the @Message parameter.

Data Interactions:
* Reads: TAMS_Possession_DepotSector
* Writes: TAMS_Possession_DepotSector

**sp_TAMS_Form_Save_Possession_Limit**

Purpose: Saves a new possession limit into the database.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TypeOfProtectionLimit | NVARCHAR(50) | The type of protection limit. |
| @RedFlashingLampsLoc | NVARCHAR(50) | The location of red flashing lamps. |
| @PossID | BIGINT | The ID of the possession. |
| @Message | NVARCHAR(500) | An output parameter to store any error message. |

Logic Flow:
1. Checks if a transaction exists.
2. If no transaction, starts a new one.
3. Checks if a limit already exists for the given possession ID and limit type and location.
4. If not found, inserts a new record into the TAMS_Possession_Limit table.
5. If an error occurs during insertion, rolls back the transaction and sets the @Message parameter to 'ERROR INSERTING INTO TAMS_TAR'.
6. If no errors, commits the transaction and returns the @Message parameter.

Data Interactions:
* Reads: TAMS_Possession_Limit
* Writes: TAMS_Possession_Limit

**sp_TAMS_Form_Save_Possession_OtherProtection**

Purpose: Saves a new possession other protection into the database.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OtherProtection | NVARCHAR(50) | The type of other protection. |
| @PossID | BIGINT | The ID of the possession. |
| @Message | NVARCHAR(500) | An output parameter to store any error message. |

Logic Flow:
1. Checks if a transaction exists.
2. If no transaction, starts a new one.
3. Checks if an other protection already exists for the given possession ID and type.
4. If not found, inserts a new record into the TAMS_Possession_OtherProtection table.
5. If an error occurs during insertion, rolls back the transaction and sets the @Message parameter to 'ERROR INSERTING INTO TAMS_TAR'.
6. If no errors, commits the transaction and returns the @Message parameter.

Data Interactions:
* Reads: TAMS_Possession_OtherProtection
* Writes: TAMS_Possession_OtherProtection

**sp_TAMS_Form_Save_Possession_PowerSector**

Purpose: Saves a new possession power sector into the database.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PowerSector | NVARCHAR(4000) | The power sector to be saved. |
| @NoOFSCD | INT | The number of SCDs in the sector. |
| @BreakerOut | NVARCHAR(5) | Whether the breaker is out or not. |
| @PossID | BIGINT | The ID of the possession. |
| @Message | NVARCHAR(500) | An output parameter to store any error message. |

Logic Flow:
1. Checks if a transaction exists.
2. If no transaction, starts a new one.
3. Checks if a power sector already exists for the given possession ID and sector.
4. If not found, inserts a new record into the TAMS_Possession_PowerSector table.
5. If an error occurs during insertion, rolls back the transaction and sets the @Message parameter to 'ERROR INSERTING INTO TAMS_TAR'.
6. If no errors, commits the transaction and returns the @Message parameter.

Data Interactions:
* Reads: TAMS_Possession_PowerSector
* Writes: TAMS_Possession_PowerSector

**sp_TAMS_Form_Save_Possession_WorkingLimit**

Purpose: Saves a new possession working limit into the database.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RedFlashingLampsLoc | NVARCHAR(50) | The location of red flashing lamps. |
| @PossID | BIGINT | The ID of the possession. |
| @Message | NVARCHAR(500) | An output parameter to store any error message. |

Logic Flow:
1. Checks if a transaction exists.
2. If no transaction, starts a new one.
3. Checks if a working limit already exists for the given possession ID and location.
4. If not found, inserts a new record into the TAMS_Possession_WorkingLimit table.
5. If an error occurs during insertion, rolls back the transaction and sets the @Message parameter to 'ERROR INSERTING INTO TAMS_TAR'.
6. If no errors, commits the transaction and returns the @Message parameter.

Data Interactions:
* Reads: TAMS_Possession_WorkingLimit
* Writes: TAMS_Possession_WorkingLimit

**sp_TAMS_Form_Save_Temp_Attachment**

Purpose: Saves a new temporary attachment into the database.

Parameters:
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARId | INTEGER | The ID of the TAR. |
| @TARAccessReqId | INTEGER | The ID of the access request. |
| @FileName | NVARCHAR(50) | The file name. |
| @FileType | NVARCHAR(50) | The file type. |
| @FileUpload | VARBINARY(MAX) | The uploaded file. |

Logic Flow:
1. Checks if a transaction exists.
2. If no transaction, starts a new one.
3. Checks if a temporary attachment already exists for the given TAR ID and access request ID.
4. If not found, inserts a new record into the TAMS_TAR_Attachment_Temp table.
5. If an error occurs during insertion, rolls back the transaction and sets the @Message parameter to 'ERROR INSERTING INTO TAMS_TAR'.
6. If no errors, commits the transaction and returns the @Message parameter.

Data Interactions:
* Reads: TAMS_TAR_Attachment_Temp
* Writes: TAMS_TAR_Attachment_Temp