**sp_TAMS_Form_Update_Access_Details**

Purpose: Updates access details for a TAR (Terminal Access Record) based on user input.

Logic Flow:
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

Data Interactions:
* Reads: TAMS_User, TAMS_TAR
* Writes: TAMS_Audit

**sp_TAMS_GetBlockedTarDates**

Purpose: Retrieves blocked TAR dates for a specific line and track type.

Logic Flow:
1. Selects data from TAMS_Block_TARDate table where Line = @Line, TrackType = @TrackType, BlockDate = @AccessDate, and IsActive = 1.
2. Orders results by BlockDate ASC.

Data Interactions:
* Reads: TAMS_Block_TARDate

**sp_TAMS_GetDutyOCCRosterByParameters**

Purpose: Retrieves duty OCR roster data for a specific line, track type, operation date, shift, and roster code.

Logic Flow:
1. Joins TAMS_OCC_Duty_Roster with TAMS_User on DutyStaffId = Userid.
2. Filters results where Line = @Line, TrackType = @TrackType, OperationDate = @OperationDate, Shift = @Shift, RosterCode = @RosterCode, and ID = @ID.
3. Orders results by ID ASC.

Data Interactions:
* Reads: TAMS_OCC_Duty_Roster, TAMS_User
* Writes: None

**sp_TAMS_GetDutyOCCRosterCodeByParameters**

Purpose: Retrieves duty OCR roster code data for a specific user ID, line, track type, operation date, shift, and roster code.

Logic Flow:
1. Joins TAMS_OCC_Duty_Roster with TAMS_User on DutyStaffId = Userid.
2. Filters results where Line = @Line, TrackType = @TrackType, OperationDate = @OperationDate, Shift = @Shift, RosterCode <> 'SCO', and DutyStaffId = @UserId.
3. Orders results by ID ASC.

Data Interactions:
* Reads: TAMS_OCC_Duty_Roster, TAMS_User
* Writes: None

**sp_TAMS_GetDutyOCCRosterCodeByParametersForTVFAck**

Purpose: Retrieves duty OCR roster code data for a specific user ID, line, track type, operation date, shift, and roster code (excluding TC codes).

Logic Flow:
1. Joins TAMS_OCC_Duty_Roster with TAMS_User on DutyStaffId = Userid.
2. Filters results where Line = @Line, TrackType = @TrackType, OperationDate = @OperationDate, Shift = @Shift, RosterCode not like '%TC%', and DutyStaffId = @UserId.
3. Orders results by ID ASC.

Data Interactions:
* Reads: TAMS_OCC_Duty_Roster, TAMS_User
* Writes: None

**sp_TAMS_GetOCCRosterByLineAndRole**

Purpose: Retrieves OCR roster data for a specific line, track type, and role.

Logic Flow:
1. Selects data from TAMS_Roster_Role table where Line = @Line, TrackType = @TrackType, and RosterCode = @RosterCode.
2. Joins TAMS_User with TAMS_User_Role on Userid = UserID and RoleID = RoleID.
3. Filters results where u.IsActive = 1 and u.ValidTo > GETDATE().
4. Orders results by [name] ASC.

Data Interactions:
* Reads: TAMS_Roster_Role, TAMS_User, TAMS_User_Role
* Writes: None

**sp_TAMS_GetParametersByLineandTracktype**

Purpose: Retrieves parameters for a specific line and track type.

Logic Flow:
1. Selects data from TAMS_Parameters table where ParaCode = @ParaCode, ParaValue1 = @Line, and ParaValue3 = @TrackType.
2. Filters results where EffectiveDate <= GETDATE() and ExpiryDate >= GETDATE().
3. Orders results by [Order] ASC.

Data Interactions:
* Reads: TAMS_Parameters

**sp_TAMS_GetParametersByParaCode**

Purpose: Retrieves parameters for a specific parameter code.

Logic Flow:
1. Selects data from TAMS_Parameters table where ParaCode = @ParaCode.
2. Filters results where EffectiveDate <= GETDATE() and ExpiryDate >= GETDATE().
3. Orders results by [Order] ASC.

Data Interactions:
* Reads: TAMS_Parameters

**sp_TAMS_GetParametersByParaCodeAndParaValue**

Purpose: Retrieves parameters for a specific parameter code and value.

Logic Flow:
1. Selects data from TAMS_Parameters table where ParaCode = @ParaCode and ParaValue1 = @ParaValue.
2. Filters results where EffectiveDate <= GETDATE() and ExpiryDate >= GETDATE().
3. Orders results by [Order] ASC.

Data Interactions:
* Reads: TAMS_Parameters

**sp_TAMS_GetParametersByParaCodeAndParaValuewithTrackType**

Purpose: Retrieves parameters for a specific parameter code, value, and track type.

Logic Flow:
1. Selects data from TAMS_Parameters table where ParaCode = @ParaCode and ParaValue1 = @ParaValue.
2. Filters results where ParaValue2 = @TrackType and EffectiveDate <= GETDATE() and ExpiryDate >= GETDATE().
3. Orders results by [Order] ASC.

Data Interactions:
* Reads: TAMS_Parameters

**sp_TAMS_GetRosterRoleByLine**

Purpose: Retrieves roster role data for a specific line, track type, operation date, shift, and roster code.

Logic Flow:
1. Checks if @Line = 'DTL' or @Line = 'NEL'.
2. If @Line = 'DTL', checks if @Count = 0.
3. If @Line = 'DTL' and @Count = 0, selects data from TAMS_Roster_Role table where Line = @Line, TrackType = @TrackType, EffectiveDate <= GETDATE(), and ExpiryDate >= GETDATE().
4. If @Line = 'NEL', checks if @Count = 0.
5. If @Line = 'NEL' and @Count = 0, selects data from TAMS_Roster_Role table where Line = @Line, TrackType = @TrackType, EffectiveDate <= GETDATE(), and ExpiryDate >= GETDATE().
6. Orders results by ID ASC.

Data Interactions:
* Reads: TAMS_Roster_Role

**sp_TAMS_GetSectorsByLineAndDirection**

Purpose: Retrieves sector data for a specific line and direction.

Logic Flow:
1. Checks if @Line = 'DTL' or @Line = 'NEL'.
2. If @Line = 'DTL', selects data from TAMS_Sector table where Line = @Line, Direction = @Direction, IsActive = 1, EffectiveDate <= GETDATE(), and ExpiryDate >= GETDATE().
3. If @Line = 'NEL', selects data from TAMS_Sector table where Line = @Line, Direction = @Direction, IsActive = 1, EffectiveDate <= GETDATE(), and ExpiryDate >= GETDATE().
4. Orders results by [Order] ASC.

Data Interactions:
* Reads: TAMS_Sector

**sp_TAMS_GetTarAccessRequirementsByTarId**

Purpose: Retrieves TAR access requirements for a specific TAR ID.

Logic Flow:
1. Joins TAMS_tar_accessreq with TAMS_Access_Requirement on OperationRequirement = id.
2. Filters results where tarid = @TarId and IsSelected = 1.
3. Orders results by [order] ASC.

Data Interactions:
* Reads: TAMS_tar_accessreq, TAMS_Access_Requirement

**sp_TAMS_GetTarApprovalsByTarId**

Purpose: Retrieves TAR approvals for a specific TAR ID.

Logic Flow:
1. Joins TAMS_TAR_Workflow with TAMS_Endorser on WorkflowId = b.WorkflowId and ActionBy = c.Userid.
2. Filters results where TARId = @TarId.
3. Orders results by ID ASC.

Data Interactions:
* Reads: TAMS_TAR_Workflow, TAMS_Endorser

**sp_TAMS_GetTarByLineAndTarAccessDate**

Purpose: Retrieves TAR data for a specific line and access date.

Logic Flow:
1. Selects data from TAMS_TAR table where Line = @Line and AccessDate = convert(datetime,@AccessDate,103).
2. Orders results by [Id] ASC.

Data Interactions:
* Reads: TAMS_TAR