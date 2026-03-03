# Procedure: sp_TAMS_GetTarEnquiryResult_Header_bak20230807
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve the TAR enquiry result header data based on various filter criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID used for filtering. |
| @Line | nvarchar(10) | The line number used for filtering. |
| @TrackType | nvarchar(50) | The track type used for filtering. |
| @TarType | nvarchar(50) | The TAR type used for filtering. |
| @AccessType | nvarchar(50) | The access type used for filtering. |
| @TarStatusId | integer | The TAR status ID used for filtering. |
| @AccessDateFrom | nvarchar(50) | The start date of the access period used for filtering. |
| @AccessDateTo | nvarchar(50) | The end date of the access period used for filtering. |
| @isNEL_Applicant | bit | A flag indicating whether to include NEL applicants. |
| @isDTL_Applicant | bit | A flag indicating whether to include DTL applicants. |
| @isNEL_ApplicantHOD | bit | A flag indicating whether to include NEL applicant HODs. |
| @isDTL_ApplicantHOD | bit | A flag indicating whether to include DTL applicant HODs. |
| @isNEL_PowerEndorser | bit | A flag indicating whether to include NEL power endorsers. |
| @isDTL_PowerEndorser | bit | A flag indicating whether to include DTL power endorsers. |
| @isNEL_PowerHOD | bit | A flag indicating whether to include NEL power HODs. |
| @isNEL_TAPVerifier | bit | A flag indicating whether to include NEL TAP verifiers. |
| @isNEL_TAPApprover | bit | A flag indicating whether to include NEL TAP approvers. |
| @isNEL_TAPHOD | bit | A flag indicating whether to include NEL TAPHODs. |
| @isDTL_TAPVerifier | bit | A flag indicating whether to include DTL TAP verifiers. |
| @isDTL_TAPApprover | bit | A flag indicating whether to include DTL TAP approvers. |
| @isDTL_TAPHOD | bit | A flag indicating whether to include DTL TAPHODs. |
| @isNEL_TAR_SysAdmin | bit | A flag indicating whether to include NEL TAR sysadmins. |
| @isDTL_TAR_SysAdmin | bit | A flag indicating whether to include DTL TAR sysadmins. |
| @isNEL_PFR | bit | A flag indicating whether to include NEL PFRs. |
| @isNEL_ChiefController | bit | A flag indicating whether to include NEL chief controllers. |
| @isDTL_PFR | bit | A flag indicating whether to include DTL PFRs. |
| @isDTL_ChiefController | bit | A flag indicating whether to include DTL chief controllers. |
| @isDTL_OCCScheduler | bit | A flag indicating whether to include DTL OCC schedulers. |

### Logic

The stored procedure first checks if the line number is not empty and the second line number is also not empty. If both are true, it prints "dtl" and appends a union statement to the SQL query.

Next, it constructs the SQL query by concatenating various filter criteria based on the input parameters. The query filters the TAR data based on the track type, TAR type, access type, TAR status ID, access date range, and various flags indicating whether to include specific types of users or roles.

The constructed SQL query is then executed using the EXEC statement.

### Notes

* The stored procedure uses a combination of bitwise AND and OR operators to filter the data based on the input parameters.
* The use of union statements allows for efficient filtering of multiple conditions.
* The flags used in the procedure are likely used to control the inclusion or exclusion of specific types of users or roles in the filtered results.