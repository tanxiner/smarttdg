**sp_TAMS_OCC_GetOCCTVFAckFromTableByParameters**

Purpose: Retrieves TVF acknowledgement data from the database based on user ID, line, operation date, and access date.

Logic Flow:
1. Checks if a user exists.
2. If no user exists, inserts into Audit table.
3. Retrieves TVF data from TAMS_TAR table where AccessDate matches the provided date.
4. Iterates through each TVF record and updates the corresponding #TMP_OCCTVF_Ack table with the latest acknowledgement data.
5. Inserts new records into #TMP_OCCTVF_Ack if no matching records exist.

Data Interactions:
* Reads: TAMS_TAR, TAMS_TVF_Acknowledge
* Writes: #TMP_OCCTVF_Ack

**sp_TAMS_OCC_GetOCCTVFAckRemarkById**

Purpose: Retrieves TVF acknowledgement remark data by ID.

Logic Flow:
1. Retrieves the ID of the TVF acknowledgement to be retrieved.
2. Joins TAMS_TVF_Ack_Remark with TAMS_User to retrieve the creator and updater information.

Data Interactions:
* Reads: TAMS_TVF_Ack_Remark, TAMS_User

**sp_TAMS_OCC_GetOCCTarTVFByParameters**

Purpose: Retrieves Tar TVF data by station ID and access date.

Logic Flow:
1. Truncates temporary tables #TMP_TVF and #TMP_TAR_TVF.
2. Inserts TVF data from TAMS_TAR table into #TMP_TVF based on the provided parameters.
3. Iterates through each record in #TMP_TVF and updates the corresponding #TMP_TAR_TVF table with the latest TVF direction information.

Data Interactions:
* Reads: TAMS_TAR, TAMS_TAR_TVF
* Writes: #TMP_TAR_TVF

**sp_TAMS_OCC_GetTarSectorByLineAndTarAccessDate**

Purpose: Retrieves Tar sector data by line and access date.

Logic Flow:
1. Checks if the provided line is 'DTL' or 'NEL'.
2. If 'DTL', retrieves sector data from TAMS_TAR_Sector table where TARStatusId = 8.
3. If 'NEL', retrieves sector data from TAMS_Power_Sector table where PowerSectorId matches the corresponding sector ID.

Data Interactions:
* Reads: TAMS_TAR, TAMS_TAR_Sector, TAMS_Power_Sector

**sp_TAMS_OCC_GetTractionPowerDetailsByIdAndType**

Purpose: Retrieves traction power details by ID and type.

Logic Flow:
1. Retrieves the ID of the traction power to be retrieved.
2. Filters results to only include records with a TractionPowerType = 'Sector' and IsActive = 1.

Data Interactions:
* Reads: TAMS_Traction_Power_Detail

**sp_TAMS_OCC_GetTractionsPowerByLine**

Purpose: Retrieves traction power data by line.

Logic Flow:
1. Checks if the provided line is null.
2. If not null, retrieves traction power data from TAMS_Traction_Power table where EffectiveDate <= GETDATE() and ExpiryDate >= GETDATE() and IsActive = 1.

Data Interactions:
* Reads: TAMS_Traction_Power

**sp_TAMS_OCC_GetWorkflowByLineAndType**

Purpose: Retrieves workflow data by line and type.

Logic Flow:
1. Checks if the provided line is null.
2. If not null, retrieves workflow data from TAMS_Workflow table where Line = @Line and WorkflowType = @Type and EffectiveDate <= GETDATE() and ExpiryDate >= GETDATE() and IsActive = 1.

Data Interactions:
* Reads: TAMS_Workflow