# TAMS Technical Documentation

## Table of Contents

### System Documentation
- [AddCompany.aspx](#system-documentation-addcompanyaspx)
- [Default.aspx](#system-documentation-defaultaspx)
- [DepotTARApplication](#system-documentation-depottarapplication)
- [DepotTAREnquiry](#system-documentation-depottarenquiry)
- [DepotTAREnquiry_Print](#system-documentation-depottarenquiry-print)
- [DepotTARForm](#system-documentation-depottarform)
- [DepotTARForm_App](#system-documentation-depottarform-app)
- [DepotTARInbox](#system-documentation-depottarinbox)
- [ExternalLogin](#system-documentation-externallogin)
- [MaintainCompany](#system-documentation-maintaincompany)
- [NewUserSignUp](#system-documentation-newusersignup)
- [OCCUpdate_Roster](#system-documentation-occupdate-roster)
- [OCC_HoursAuthorisation_Preview](#system-documentation-occ-hoursauthorisation-preview)
- [RGS](#system-documentation-rgs)
- [RGSEnquiry](#system-documentation-rgsenquiry)
- [RegistrationRequest](#system-documentation-registrationrequest)
- [SignUpNewSystem](#system-documentation-signupnewsystem)
- [TARAppList](#system-documentation-tarapplist)
- [TARApplication](#system-documentation-tarapplication)
- [TARBlockDate](#system-documentation-tarblockdate)
- [TAREnquiry](#system-documentation-tarenquiry)
- [TAREnquiry_Print](#system-documentation-tarenquiry-print)
- [TARForm](#system-documentation-tarform)
- [TARForm_App](#system-documentation-tarform-app)
- [TARInbox](#system-documentation-tarinbox)
- [TARViewDetails](#system-documentation-tarviewdetails)
- [TOAApplication](#system-documentation-toaapplication)
- [TOABookIn](#system-documentation-toabookin)
- [TOABookOut](#system-documentation-toabookout)
- [TVFAcknowledgement_Enquiry](#system-documentation-tvfacknowledgement-enquiry)
- [ViewProfile](#system-documentation-viewprofile)
- [OCCAuthCC_DTL](#system-documentation-occauthcc-dtl)
- [OCCAuthPreview_NEL](#system-documentation-occauthpreview-nel)
- [OCCAuth_NEL](#system-documentation-occauth-nel)
- [OCCTVF_Ack_Preview](#system-documentation-occtvf-ack-preview)

### Database Reference (SQL)
- [EAlertQ_EnQueue](#database-reference-sql-ealertq-enqueue)
- [EAlertQ_EnQueue_External](#database-reference-sql-ealertq-enqueue-external)
- [SMSEAlertQ_EnQueue](#database-reference-sql-smsealertq-enqueue)
- [SMTP_GET_Email_Attachments](#database-reference-sql-smtp-get-email-attachments)
- [SMTP_GET_Email_Lists](#database-reference-sql-smtp-get-email-lists)
- [SMTP_GET_Email_Lists_Frm](#database-reference-sql-smtp-get-email-lists-frm)
- [SMTP_Update_Email_Lists](#database-reference-sql-smtp-update-email-lists)
- [SP_Call_SMTP_Send_SMSAlert](#database-reference-sql-sp-call-smtp-send-smsalert)
- [SP_CheckPagePermission](#database-reference-sql-sp-checkpagepermission)
- [SP_SMTP_SMS_NetPage](#database-reference-sql-sp-smtp-sms-netpage)
- [SP_SMTP_Send_SMSAlert](#database-reference-sql-sp-smtp-send-smsalert)
- [SP_TAMS_Depot_GetDTCAuth](#database-reference-sql-sp-tams-depot-getdtcauth)
- [SP_TAMS_Depot_GetDTCAuthEndorser](#database-reference-sql-sp-tams-depot-getdtcauthendorser)
- [SP_TAMS_Depot_GetDTCAuthPowerzone](#database-reference-sql-sp-tams-depot-getdtcauthpowerzone)
- [SP_TAMS_Depot_GetDTCAuthSPKS](#database-reference-sql-sp-tams-depot-getdtcauthspks)
- [SP_TAMS_Depot_GetDTCRoster](#database-reference-sql-sp-tams-depot-getdtcroster)
- [SP_TAMS_Depot_GetParameters](#database-reference-sql-sp-tams-depot-getparameters)
- [SP_TAMS_Depot_GetUserAccess](#database-reference-sql-sp-tams-depot-getuseraccess)
- [SP_TAMS_Depot_GetWFStatus](#database-reference-sql-sp-tams-depot-getwfstatus)
- [SP_TAMS_Depot_SaveDTCAuthComments](#database-reference-sql-sp-tams-depot-savedtcauthcomments)
- [SP_Test](#database-reference-sql-sp-test)
- [getUserInformationByID](#database-reference-sql-getuserinformationbyid)
- [sp_Generate_Ref_Num](#database-reference-sql-sp-generate-ref-num)
- [sp_Generate_Ref_Num_TOA](#database-reference-sql-sp-generate-ref-num-toa)
- [sp_Get_QRPoints](#database-reference-sql-sp-get-qrpoints)
- [sp_Get_TypeOfWorkByLine](#database-reference-sql-sp-get-typeofworkbyline)
- [sp_TAMS_Applicant_List_Child_OnLoad](#database-reference-sql-sp-tams-applicant-list-child-onload)
- [sp_TAMS_Applicant_List_Child_OnLoad_20220303](#database-reference-sql-sp-tams-applicant-list-child-onload-20220303)
- [sp_TAMS_Applicant_List_Child_OnLoad_Hnin](#database-reference-sql-sp-tams-applicant-list-child-onload-hnin)
- [sp_TAMS_Applicant_List_Child_OnLoad_20220303_M](#database-reference-sql-sp-tams-applicant-list-child-onload-20220303-m)
- [sp_TAMS_Applicant_List_Master_OnLoad](#database-reference-sql-sp-tams-applicant-list-master-onload)
- [sp_TAMS_Applicant_List_OnLoad](#database-reference-sql-sp-tams-applicant-list-onload)
- [sp_TAMS_Approval_Add_BufferZone](#database-reference-sql-sp-tams-approval-add-bufferzone)
- [sp_TAMS_Approval_Add_TVFStation](#database-reference-sql-sp-tams-approval-add-tvfstation)
- [sp_TAMS_Approval_Del_BufferZone](#database-reference-sql-sp-tams-approval-del-bufferzone)
- [sp_TAMS_Approval_Del_TVFStation](#database-reference-sql-sp-tams-approval-del-tvfstation)
- [sp_TAMS_Approval_Endorse](#database-reference-sql-sp-tams-approval-endorse)
- [sp_TAMS_Approval_Endorse20250120](#database-reference-sql-sp-tams-approval-endorse20250120)
- [sp_TAMS_Approval_Endorse_20220930](#database-reference-sql-sp-tams-approval-endorse-20220930)
- [sp_TAMS_Approval_Endorse_20230410](#database-reference-sql-sp-tams-approval-endorse-20230410)
- [sp_TAMS_Approval_Get_Add_BufferZone](#database-reference-sql-sp-tams-approval-get-add-bufferzone)
- [sp_TAMS_Approval_Get_Add_TVFStation](#database-reference-sql-sp-tams-approval-get-add-tvfstation)
- [sp_TAMS_Approval_OnLoad](#database-reference-sql-sp-tams-approval-onload)
- [sp_TAMS_Approval_OnLoad_bak20230531](#database-reference-sql-sp-tams-approval-onload-bak20230531)
- [sp_TAMS_Approval_Proceed_To_App](#database-reference-sql-sp-tams-approval-proceed-to-app)
- [sp_TAMS_Approval_Proceed_To_App_20220930](#database-reference-sql-sp-tams-approval-proceed-to-app-20220930)
- [sp_TAMS_Approval_Proceed_To_App_20231009](#database-reference-sql-sp-tams-approval-proceed-to-app-20231009)
- [sp_TAMS_Approval_Proceed_To_App_20240920](#database-reference-sql-sp-tams-approval-proceed-to-app-20240920)
- [sp_TAMS_Approval_Reject](#database-reference-sql-sp-tams-approval-reject)
- [sp_TAMS_Approval_Reject_20220930](#database-reference-sql-sp-tams-approval-reject-20220930)
- [sp_TAMS_Batch_DeActivate_UserAccount](#database-reference-sql-sp-tams-batch-deactivate-useraccount)
- [sp_TAMS_Batch_HouseKeeping](#database-reference-sql-sp-tams-batch-housekeeping)
- [sp_TAMS_Batch_InActive_ResignedStaff](#database-reference-sql-sp-tams-batch-inactive-resignedstaff)
- [sp_TAMS_Batch_Populate_Calendar](#database-reference-sql-sp-tams-batch-populate-calendar)
- [sp_TAMS_Block_Date_Delete](#database-reference-sql-sp-tams-block-date-delete)
- [sp_TAMS_Block_Date_OnLoad](#database-reference-sql-sp-tams-block-date-onload)
- [sp_TAMS_Block_Date_Save](#database-reference-sql-sp-tams-block-date-save)
- [sp_TAMS_CancelTarByTarID](#database-reference-sql-sp-tams-canceltarbytarid)
- [sp_TAMS_Check_UserExist](#database-reference-sql-sp-tams-check-userexist)
- [sp_TAMS_Delete_RegQueryDept_SysOwnerApproval](#database-reference-sql-sp-tams-delete-regquerydept-sysownerapproval)
- [sp_TAMS_Delete_UserQueryDeptByUserID](#database-reference-sql-sp-tams-delete-userquerydeptbyuserid)
- [sp_TAMS_Delete_UserRoleByUserID](#database-reference-sql-sp-tams-delete-userrolebyuserid)
- [sp_TAMS_Depot_Applicant_List_Child_OnLoad](#database-reference-sql-sp-tams-depot-applicant-list-child-onload)
- [sp_TAMS_Depot_Applicant_List_Master_OnLoad](#database-reference-sql-sp-tams-depot-applicant-list-master-onload)
- [sp_TAMS_Depot_Approval_OnLoad](#database-reference-sql-sp-tams-depot-approval-onload)
- [sp_TAMS_Depot_Form_OnLoad](#database-reference-sql-sp-tams-depot-form-onload)
- [sp_TAMS_Depot_Form_Save_Access_Details](#database-reference-sql-sp-tams-depot-form-save-access-details)
- [sp_TAMS_Depot_Form_Submit](#database-reference-sql-sp-tams-depot-form-submit)
- [sp_TAMS_Depot_Form_Update_Access_Details](#database-reference-sql-sp-tams-depot-form-update-access-details)
- [sp_TAMS_Depot_GetBlockedTarDates](#database-reference-sql-sp-tams-depot-getblockedtardates)
- [sp_TAMS_Depot_GetPossessionDepotSectorByPossessionId](#database-reference-sql-sp-tams-depot-getpossessiondepotsectorbypossessionid)
- [sp_TAMS_Depot_GetTarByTarId](#database-reference-sql-sp-tams-depot-gettarbytarid)
- [sp_TAMS_Depot_GetTarEnquiryResult_Department](#database-reference-sql-sp-tams-depot-gettarenquiryresult-department)
- [sp_TAMS_Depot_GetTarSectorsByAccessDateAndLine](#database-reference-sql-sp-tams-depot-gettarsectorsbyaccessdateandline)
- [sp_TAMS_Depot_GetTarSectorsByTarId](#database-reference-sql-sp-tams-depot-gettarsectorsbytarid)
- [sp_TAMS_Depot_Inbox_Child_OnLoad](#database-reference-sql-sp-tams-depot-inbox-child-onload)
- [sp_TAMS_Depot_Inbox_Master_OnLoad](#database-reference-sql-sp-tams-depot-inbox-master-onload)
- [sp_TAMS_Depot_RGS_AckSurrender](#database-reference-sql-sp-tams-depot-rgs-acksurrender)
- [sp_TAMS_Depot_RGS_GrantTOA](#database-reference-sql-sp-tams-depot-rgs-granttoa)
- [sp_TAMS_Depot_RGS_OnLoad](#database-reference-sql-sp-tams-depot-rgs-onload)
- [sp_TAMS_Depot_RGS_OnLoad_Enq](#database-reference-sql-sp-tams-depot-rgs-onload-enq)
- [sp_TAMS_Depot_RGS_Update_Details](#database-reference-sql-sp-tams-depot-rgs-update-details)
- [sp_TAMS_Depot_RGS_Update_Details20250403](#database-reference-sql-sp-tams-depot-rgs-update-details20250403)
- [sp_TAMS_Depot_RGS_Update_QTS](#database-reference-sql-sp-tams-depot-rgs-update-qts)
- [sp_TAMS_Depot_SectorBooking_OnLoad](#database-reference-sql-sp-tams-depot-sectorbooking-onload)
- [sp_TAMS_Depot_SectorBooking_QTS_Chk](#database-reference-sql-sp-tams-depot-sectorbooking-qts-chk)
- [sp_TAMS_Depot_TOA_QTS_Chk](#database-reference-sql-sp-tams-depot-toa-qts-chk)
- [sp_TAMS_Depot_TOA_Register](#database-reference-sql-sp-tams-depot-toa-register)
- [sp_TAMS_Depot_TOA_Register_1](#database-reference-sql-sp-tams-depot-toa-register-1)
- [sp_TAMS_Depot_UpdateDTCAuth](#database-reference-sql-sp-tams-depot-updatedtcauth)
- [sp_TAMS_Depot_UpdateDTCAuthBatch](#database-reference-sql-sp-tams-depot-updatedtcauthbatch)
- [sp_TAMS_Depot_UpdateDTCAuthBatch20250120](#database-reference-sql-sp-tams-depot-updatedtcauthbatch20250120)
- [sp_TAMS_Email_Apply_Late_TAR](#database-reference-sql-sp-tams-email-apply-late-tar)
- [sp_TAMS_Email_Apply_Urgent_TAR](#database-reference-sql-sp-tams-email-apply-urgent-tar)
- [sp_TAMS_Email_Apply_Urgent_TAR_20231009](#database-reference-sql-sp-tams-email-apply-urgent-tar-20231009)
- [sp_TAMS_Email_Cancel_TAR](#database-reference-sql-sp-tams-email-cancel-tar)
- [sp_TAMS_Email_CompanyRegistrationLinkByRegID](#database-reference-sql-sp-tams-email-companyregistrationlinkbyregid)
- [sp_TAMS_Email_Late_TAR](#database-reference-sql-sp-tams-email-late-tar)
- [sp_TAMS_Email_Late_TAR_OCC](#database-reference-sql-sp-tams-email-late-tar-occ)
- [sp_TAMS_Email_PasswordResetLinkByRegID](#database-reference-sql-sp-tams-email-passwordresetlinkbyregid)
- [sp_TAMS_Email_SignUpStatusLinkByLoginID](#database-reference-sql-sp-tams-email-signupstatuslinkbyloginid)
- [sp_TAMS_Email_SignUpStatusLinkByLoginID_20231009](#database-reference-sql-sp-tams-email-signupstatuslinkbyloginid-20231009)
- [sp_TAMS_Email_Urgent_TAR](#database-reference-sql-sp-tams-email-urgent-tar)
- [sp_TAMS_Email_Urgent_TAR_20231009](#database-reference-sql-sp-tams-email-urgent-tar-20231009)
- [sp_TAMS_Email_Urgent_TAR_OCC](#database-reference-sql-sp-tams-email-urgent-tar-occ)
- [sp_TAMS_Email_Urgent_TAR_OCC_20231009](#database-reference-sql-sp-tams-email-urgent-tar-occ-20231009)
- [sp_TAMS_Form_Cancel](#database-reference-sql-sp-tams-form-cancel)
- [sp_TAMS_Form_Delete_Temp_Attachment](#database-reference-sql-sp-tams-form-delete-temp-attachment)
- [sp_TAMS_Form_OnLoad](#database-reference-sql-sp-tams-form-onload)
- [sp_TAMS_Form_Save_Access_Details](#database-reference-sql-sp-tams-form-save-access-details)
- [sp_TAMS_Form_Save_Access_Reqs](#database-reference-sql-sp-tams-form-save-access-reqs)
- [sp_TAMS_Form_Save_Possession](#database-reference-sql-sp-tams-form-save-possession)
- [sp_TAMS_Form_Save_Possession_DepotSector](#database-reference-sql-sp-tams-form-save-possession-depotsector)
- [sp_TAMS_Form_Save_Possession_Limit](#database-reference-sql-sp-tams-form-save-possession-limit)
- [sp_TAMS_Form_Save_Possession_OtherProtection](#database-reference-sql-sp-tams-form-save-possession-otherprotection)
- [sp_TAMS_Form_Save_Possession_PowerSector](#database-reference-sql-sp-tams-form-save-possession-powersector)
- [sp_TAMS_Form_Save_Possession_WorkingLimit](#database-reference-sql-sp-tams-form-save-possession-workinglimit)
- [sp_TAMS_Form_Save_Temp_Attachment](#database-reference-sql-sp-tams-form-save-temp-attachment)
- [sp_TAMS_Form_Submit](#database-reference-sql-sp-tams-form-submit)
- [sp_TAMS_Form_Submit_20220930](#database-reference-sql-sp-tams-form-submit-20220930)
- [sp_TAMS_Form_Submit_20250313](#database-reference-sql-sp-tams-form-submit-20250313)
- [sp_TAMS_Form_Update_Access_Details](#database-reference-sql-sp-tams-form-update-access-details)
- [sp_TAMS_GetBlockedTarDates](#database-reference-sql-sp-tams-getblockedtardates)
- [sp_TAMS_GetDutyOCCRosterByParameters](#database-reference-sql-sp-tams-getdutyoccrosterbyparameters)
- [sp_TAMS_GetDutyOCCRosterCodeByParameters](#database-reference-sql-sp-tams-getdutyoccrostercodebyparameters)
- [sp_TAMS_GetDutyOCCRosterCodeByParametersForTVFAck](#database-reference-sql-sp-tams-getdutyoccrostercodebyparametersfortvfack)
- [sp_TAMS_GetOCCRosterByLineAndRole](#database-reference-sql-sp-tams-getoccrosterbylineandrole)
- [sp_TAMS_GetParametersByLineandTracktype](#database-reference-sql-sp-tams-getparametersbylineandtracktype)
- [sp_TAMS_GetParametersByParaCode](#database-reference-sql-sp-tams-getparametersbyparacode)
- [sp_TAMS_GetParametersByParaCodeAndParaValue](#database-reference-sql-sp-tams-getparametersbyparacodeandparavalue)
- [sp_TAMS_GetParametersByParaCodeAndParaValuewithTrackType](#database-reference-sql-sp-tams-getparametersbyparacodeandparavaluewithtracktype)
- [sp_TAMS_GetRosterRoleByLine](#database-reference-sql-sp-tams-getrosterrolebyline)
- [sp_TAMS_GetSectorsByLineAndDirection](#database-reference-sql-sp-tams-getsectorsbylineanddirection)
- [sp_TAMS_GetTarAccessRequirementsByTarId](#database-reference-sql-sp-tams-gettaraccessrequirementsbytarid)
- [sp_TAMS_GetTarApprovalsByTarId](#database-reference-sql-sp-tams-gettarapprovalsbytarid)
- [sp_TAMS_GetTarByLineAndTarAccessDate](#database-reference-sql-sp-tams-gettarbylineandtaraccessdate)
- [sp_TAMS_GetTarByTarId](#database-reference-sql-sp-tams-gettarbytarid)
- [sp_TAMS_GetTarEnquiryResult](#database-reference-sql-sp-tams-gettarenquiryresult)
- [sp_TAMS_GetTarEnquiryResult_Department](#database-reference-sql-sp-tams-gettarenquiryresult-department)
- [sp_TAMS_GetTarEnquiryResult_Header](#database-reference-sql-sp-tams-gettarenquiryresult-header)
- [sp_TAMS_GetTarEnquiryResult_Header_20220120](#database-reference-sql-sp-tams-gettarenquiryresult-header-20220120)
- [sp_TAMS_GetTarEnquiryResult_Header_20220529](#database-reference-sql-sp-tams-gettarenquiryresult-header-20220529)
- [sp_TAMS_GetTarEnquiryResult_Header_20221018](#database-reference-sql-sp-tams-gettarenquiryresult-header-20221018)
- [sp_TAMS_GetTarEnquiryResult_Header_20240905](#database-reference-sql-sp-tams-gettarenquiryresult-header-20240905)
- [sp_TAMS_GetTarEnquiryResult_Header_ToBeDeployed](#database-reference-sql-sp-tams-gettarenquiryresult-header-tobedeployed)
- [sp_TAMS_GetTarEnquiryResult_Header_20220529_M](#database-reference-sql-sp-tams-gettarenquiryresult-header-20220529-m)
- [sp_TAMS_GetTarEnquiryResult_Header_20221018_M](#database-reference-sql-sp-tams-gettarenquiryresult-header-20221018-m)
- [sp_TAMS_GetTarEnquiryResult_Header_bak20230807](#database-reference-sql-sp-tams-gettarenquiryresult-header-bak20230807)
- [sp_TAMS_GetTarEnquiryResult_User](#database-reference-sql-sp-tams-gettarenquiryresult-user)
- [sp_TAMS_GetTarEnquiryResult_User20240905](#database-reference-sql-sp-tams-gettarenquiryresult-user20240905)
- [sp_TAMS_GetTarEnquiryResult_User20250120](#database-reference-sql-sp-tams-gettarenquiryresult-user20250120)
- [sp_TAMS_GetTarForPossessionPlanReport](#database-reference-sql-sp-tams-gettarforpossessionplanreport)
- [sp_TAMS_GetTarOtherProtectionByPossessionId](#database-reference-sql-sp-tams-gettarotherprotectionbypossessionid)
- [sp_TAMS_GetTarPossessionLimitByPossessionId](#database-reference-sql-sp-tams-gettarpossessionlimitbypossessionid)
- [sp_TAMS_GetTarPossessionPlanByTarId](#database-reference-sql-sp-tams-gettarpossessionplanbytarid)
- [sp_TAMS_GetTarPossessionPowerSectorByPossessionId](#database-reference-sql-sp-tams-gettarpossessionpowersectorbypossessionid)
- [sp_TAMS_GetTarSectorsByAccessDateAndLine](#database-reference-sql-sp-tams-gettarsectorsbyaccessdateandline)
- [sp_TAMS_GetTarSectorsByAccessDateAndLineAndDirection](#database-reference-sql-sp-tams-gettarsectorsbyaccessdateandlineanddirection)
- [sp_TAMS_GetTarSectorsByAccessDateAndLineAndDirection_SameSector](#database-reference-sql-sp-tams-gettarsectorsbyaccessdateandlineanddirection-samesector)
- [sp_TAMS_GetTarSectorsByTarId](#database-reference-sql-sp-tams-gettarsectorsbytarid)
- [sp_TAMS_GetTarStationsByTarId](#database-reference-sql-sp-tams-gettarstationsbytarid)
- [sp_TAMS_GetTarWorkingLimitByPossessionId](#database-reference-sql-sp-tams-gettarworkinglimitbypossessionid)
- [sp_TAMS_GetWFStatusByLine](#database-reference-sql-sp-tams-getwfstatusbyline)
- [sp_TAMS_GetWFStatusByLineAndType](#database-reference-sql-sp-tams-getwfstatusbylineandtype)
- [sp_TAMS_Get_All_Roles](#database-reference-sql-sp-tams-get-all-roles)
- [sp_TAMS_Get_ChildMenuByUserRole](#database-reference-sql-sp-tams-get-childmenubyuserrole)
- [sp_TAMS_Get_ChildMenuByUserRoleID](#database-reference-sql-sp-tams-get-childmenubyuserroleid)
- [sp_TAMS_Get_ChildMenuByUserRole_20231009](#database-reference-sql-sp-tams-get-childmenubyuserrole-20231009)
- [sp_TAMS_Get_CompanyInfo_by_ID](#database-reference-sql-sp-tams-get-companyinfo-by-id)
- [sp_TAMS_Get_CompanyListByUENCompanyName](#database-reference-sql-sp-tams-get-companylistbyuencompanyname)
- [sp_TAMS_Get_Depot_TarEnquiryResult_Header](#database-reference-sql-sp-tams-get-depot-tarenquiryresult-header)
- [sp_TAMS_Get_External_UserInfo_by_LoginIDPWD](#database-reference-sql-sp-tams-get-external-userinfo-by-loginidpwd)
- [sp_TAMS_Get_ParaValByParaCode](#database-reference-sql-sp-tams-get-paravalbyparacode)
- [sp_TAMS_Get_ParentMenuByUserRole](#database-reference-sql-sp-tams-get-parentmenubyuserrole)
- [sp_TAMS_Get_RegistrationCompanyInformationbyRegID](#database-reference-sql-sp-tams-get-registrationcompanyinformationbyregid)
- [sp_TAMS_Get_RegistrationInboxByUserID](#database-reference-sql-sp-tams-get-registrationinboxbyuserid)
- [sp_TAMS_Get_RegistrationInboxByUserID_20231009](#database-reference-sql-sp-tams-get-registrationinboxbyuserid-20231009)
- [sp_TAMS_Get_RegistrationInboxByUserID_hnin](#database-reference-sql-sp-tams-get-registrationinboxbyuserid-hnin)
- [sp_TAMS_Get_RegistrationInformationByRegModuleID](#database-reference-sql-sp-tams-get-registrationinformationbyregmoduleid)
- [sp_TAMS_Get_RolesByLineModule](#database-reference-sql-sp-tams-get-rolesbylinemodule)
- [sp_TAMS_Get_SignUpStatusByLoginID](#database-reference-sql-sp-tams-get-signupstatusbyloginid)
- [sp_TAMS_Get_UserAccessRoleInfo_by_ID](#database-reference-sql-sp-tams-get-useraccessroleinfo-by-id)
- [sp_TAMS_Get_UserAccessStatusInfo_by_LoginID](#database-reference-sql-sp-tams-get-useraccessstatusinfo-by-loginid)
- [sp_TAMS_Get_UserInfo](#database-reference-sql-sp-tams-get-userinfo)
- [sp_TAMS_Get_UserInfo_by_ID](#database-reference-sql-sp-tams-get-userinfo-by-id)
- [sp_TAMS_Get_UserInfo_by_LoginID](#database-reference-sql-sp-tams-get-userinfo-by-loginid)
- [sp_TAMS_Get_User_List_By_Line](#database-reference-sql-sp-tams-get-user-list-by-line)
- [sp_TAMS_Get_User_List_By_Line_20211101](#database-reference-sql-sp-tams-get-user-list-by-line-20211101)
- [sp_TAMS_Get_User_RailLine](#database-reference-sql-sp-tams-get-user-railline)
- [sp_TAMS_Get_User_RailLine_Depot](#database-reference-sql-sp-tams-get-user-railline-depot)
- [sp_TAMS_Get_User_TrackType](#database-reference-sql-sp-tams-get-user-tracktype)
- [sp_TAMS_Get_User_TrackType_Line](#database-reference-sql-sp-tams-get-user-tracktype-line)
- [sp_TAMS_Inbox_Child_OnLoad](#database-reference-sql-sp-tams-inbox-child-onload)
- [sp_TAMS_Inbox_Child_OnLoad_20230406](#database-reference-sql-sp-tams-inbox-child-onload-20230406)
- [sp_TAMS_Inbox_Child_OnLoad_20230706](#database-reference-sql-sp-tams-inbox-child-onload-20230706)
- [sp_TAMS_Inbox_Child_OnLoad_20240925](#database-reference-sql-sp-tams-inbox-child-onload-20240925)
- [sp_TAMS_Inbox_Child_OnLoad_20230406_M](#database-reference-sql-sp-tams-inbox-child-onload-20230406-m)
- [sp_TAMS_Inbox_Master_OnLoad](#database-reference-sql-sp-tams-inbox-master-onload)
- [sp_TAMS_Inbox_Master_OnLoad_20230406](#database-reference-sql-sp-tams-inbox-master-onload-20230406)
- [sp_TAMS_Inbox_Master_OnLoad_20230406_M](#database-reference-sql-sp-tams-inbox-master-onload-20230406-m)
- [sp_TAMS_Inbox_OnLoad](#database-reference-sql-sp-tams-inbox-onload)
- [sp_TAMS_Insert_ExternalUserRegistration](#database-reference-sql-sp-tams-insert-externaluserregistration)
- [sp_TAMS_Insert_ExternalUserRegistrationModule](#database-reference-sql-sp-tams-insert-externaluserregistrationmodule)
- [sp_TAMS_Insert_ExternalUserRegistrationModule_20231009](#database-reference-sql-sp-tams-insert-externaluserregistrationmodule-20231009)
- [sp_TAMS_Insert_InternalUserRegistration](#database-reference-sql-sp-tams-insert-internaluserregistration)
- [sp_TAMS_Insert_InternalUserRegistrationModule](#database-reference-sql-sp-tams-insert-internaluserregistrationmodule)
- [sp_TAMS_Insert_InternalUserRegistrationModule_20231009](#database-reference-sql-sp-tams-insert-internaluserregistrationmodule-20231009)
- [sp_TAMS_Insert_InternalUserRegistrationModule_bak20230112](#database-reference-sql-sp-tams-insert-internaluserregistrationmodule-bak20230112)
- [sp_TAMS_Insert_RegQueryDept_SysAdminApproval](#database-reference-sql-sp-tams-insert-regquerydept-sysadminapproval)
- [sp_TAMS_Insert_RegQueryDept_SysOwnerApproval](#database-reference-sql-sp-tams-insert-regquerydept-sysownerapproval)
- [sp_TAMS_Insert_UserQueryDeptByUserID](#database-reference-sql-sp-tams-insert-userquerydeptbyuserid)
- [sp_TAMS_Insert_UserRegRole_SysAdminApproval](#database-reference-sql-sp-tams-insert-userregrole-sysadminapproval)
- [sp_TAMS_Insert_UserRoleByUserIDRailModule](#database-reference-sql-sp-tams-insert-userrolebyuseridrailmodule)
- [sp_TAMS_OCC_AddTVFAckRemarks](#database-reference-sql-sp-tams-occ-addtvfackremarks)
- [sp_TAMS_OCC_Generate_Authorization](#database-reference-sql-sp-tams-occ-generate-authorization)
- [sp_TAMS_OCC_Generate_Authorization_20230215](#database-reference-sql-sp-tams-occ-generate-authorization-20230215)
- [sp_TAMS_OCC_Generate_Authorization_Trace](#database-reference-sql-sp-tams-occ-generate-authorization-trace)
- [sp_TAMS_OCC_Generate_Authorization_20230215_M](#database-reference-sql-sp-tams-occ-generate-authorization-20230215-m)
- [sp_TAMS_OCC_Generate_Authorization_20230215_PowerOnIssue](#database-reference-sql-sp-tams-occ-generate-authorization-20230215-poweronissue)
- [sp_TAMS_OCC_GetEndorserByWorkflowId](#database-reference-sql-sp-tams-occ-getendorserbyworkflowid)
- [sp_TAMS_OCC_GetOCCAuthByLineAndAccessDate](#database-reference-sql-sp-tams-occ-getoccauthbylineandaccessdate)
- [sp_TAMS_OCC_GetOCCAuthPreviewByParameters](#database-reference-sql-sp-tams-occ-getoccauthpreviewbyparameters)
- [sp_TAMS_OCC_GetOCCAuthPreviewByParameters_NEL](#database-reference-sql-sp-tams-occ-getoccauthpreviewbyparameters-nel)
- [sp_TAMS_OCC_GetOCCAuthPreviewByParameters_NEL_bak20230728](#database-reference-sql-sp-tams-occ-getoccauthpreviewbyparameters-nel-bak20230728)
- [sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL](#database-reference-sql-sp-tams-occ-getoccauthorisationbyparameters-nel)
- [sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL_001](#database-reference-sql-sp-tams-occ-getoccauthorisationbyparameters-nel-001)
- [sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL_bak20230727](#database-reference-sql-sp-tams-occ-getoccauthorisationbyparameters-nel-bak20230727)
- [sp_TAMS_OCC_GetOCCAuthorisationCCByParameters](#database-reference-sql-sp-tams-occ-getoccauthorisationccbyparameters)
- [sp_TAMS_OCC_GetOCCAuthorisationPFRByParameters](#database-reference-sql-sp-tams-occ-getoccauthorisationpfrbyparameters)
- [sp_TAMS_OCC_GetOCCAuthorisationPFRByParameters_bak20230727](#database-reference-sql-sp-tams-occ-getoccauthorisationpfrbyparameters-bak20230727)
- [sp_TAMS_OCC_GetOCCAuthorisationTCByParameters](#database-reference-sql-sp-tams-occ-getoccauthorisationtcbyparameters)
- [sp_TAMS_OCC_GetOCCAuthorisationTCByParameters_20230216](#database-reference-sql-sp-tams-occ-getoccauthorisationtcbyparameters-20230216)
- [sp_TAMS_OCC_GetOCCAuthorisationTCByParameters_20230216_M](#database-reference-sql-sp-tams-occ-getoccauthorisationtcbyparameters-20230216-m)
- [sp_TAMS_OCC_GetOCCTVFAckByParameters](#database-reference-sql-sp-tams-occ-getocctvfackbyparameters)
- [sp_TAMS_OCC_GetOCCTVFAckByParameters_Preview](#database-reference-sql-sp-tams-occ-getocctvfackbyparameters-preview)
- [sp_TAMS_OCC_GetOCCTVFAckFromTableByParameters](#database-reference-sql-sp-tams-occ-getocctvfackfromtablebyparameters)
- [sp_TAMS_OCC_GetOCCTVFAckRemarkById](#database-reference-sql-sp-tams-occ-getocctvfackremarkbyid)
- [sp_TAMS_OCC_GetOCCTarTVFByParameters](#database-reference-sql-sp-tams-occ-getocctartvfbyparameters)
- [sp_TAMS_OCC_GetTarSectorByLineAndTarAccessDate](#database-reference-sql-sp-tams-occ-gettarsectorbylineandtaraccessdate)
- [sp_TAMS_OCC_GetTractionPowerDetailsByIdAndType](#database-reference-sql-sp-tams-occ-gettractionpowerdetailsbyidandtype)
- [sp_TAMS_OCC_GetTractionsPowerByLine](#database-reference-sql-sp-tams-occ-gettractionspowerbyline)
- [sp_TAMS_OCC_GetWorkflowByLineAndType](#database-reference-sql-sp-tams-occ-getworkflowbylineandtype)
- [sp_TAMS_OCC_InsertTVFAckByParameters](#database-reference-sql-sp-tams-occ-inserttvfackbyparameters)
- [sp_TAMS_OCC_InsertToDutyOCCRosterTable](#database-reference-sql-sp-tams-occ-inserttodutyoccrostertable)
- [sp_TAMS_OCC_InsertToDutyOCCRosterTable_20221116](#database-reference-sql-sp-tams-occ-inserttodutyoccrostertable-20221116)
- [sp_TAMS_OCC_InsertToDutyOCCRosterTable_20221116_M](#database-reference-sql-sp-tams-occ-inserttodutyoccrostertable-20221116-m)
- [sp_TAMS_OCC_InsertToOCCAuthTable](#database-reference-sql-sp-tams-occ-inserttooccauthtable)
- [sp_TAMS_OCC_InsertToOCCAuthWorkflowTable](#database-reference-sql-sp-tams-occ-inserttooccauthworkflowtable)
- [sp_TAMS_OCC_RejectTVFAckByParameters_PFR](#database-reference-sql-sp-tams-occ-rejecttvfackbyparameters-pfr)
- [sp_TAMS_OCC_UpdateOCCAuthorisationCCByParameters](#database-reference-sql-sp-tams-occ-updateoccauthorisationccbyparameters)
- [251_sp_TAMS_OCC_UpdateOCCAuthorisationNELByParameters.md](#database-reference-sql-251-sp-tams-occ-updateoccauthorisationnelbyparametersmd)
- [sp_TAMS_OCC_UpdateOCCAuthorisationNELByParameters_bak20230711](#database-reference-sql-sp-tams-occ-updateoccauthorisationnelbyparameters-bak20230711)
- [sp_TAMS_OCC_UpdateOCCAuthorisationNELRemark](#database-reference-sql-sp-tams-occ-updateoccauthorisationnelremark)
- [sp_TAMS_OCC_UpdateOCCAuthorisationPFRByParameters](#database-reference-sql-sp-tams-occ-updateoccauthorisationpfrbyparameters)
- [sp_TAMS_OCC_UpdateOCCAuthorisationPFRByParameters_bak20230711](#database-reference-sql-sp-tams-occ-updateoccauthorisationpfrbyparameters-bak20230711)
- [sp_TAMS_OCC_UpdateOCCAuthorisationTCByParameters](#database-reference-sql-sp-tams-occ-updateoccauthorisationtcbyparameters)
- [sp_TAMS_OCC_UpdateTVFAckByParameters_CC](#database-reference-sql-sp-tams-occ-updatetvfackbyparameters-cc)
- [sp_TAMS_OCC_UpdateTVFAckByParameters_PFR](#database-reference-sql-sp-tams-occ-updatetvfackbyparameters-pfr)
- [sp_TAMS_OPD_OnLoad](#database-reference-sql-sp-tams-opd-onload)
- [sp_TAMS_RGS_AckReg](#database-reference-sql-sp-tams-rgs-ackreg)
- [sp_TAMS_RGS_AckReg_20221107](#database-reference-sql-sp-tams-rgs-ackreg-20221107)
- [sp_TAMS_RGS_AckReg_20230807](#database-reference-sql-sp-tams-rgs-ackreg-20230807)
- [sp_TAMS_RGS_AckReg_20230807_M](#database-reference-sql-sp-tams-rgs-ackreg-20230807-m)
- [sp_TAMS_RGS_AckSMS](#database-reference-sql-sp-tams-rgs-acksms)
- [sp_TAMS_RGS_AckSMS_20221107](#database-reference-sql-sp-tams-rgs-acksms-20221107)
- [sp_TAMS_RGS_AckSMS_20221214](#database-reference-sql-sp-tams-rgs-acksms-20221214)
- [sp_TAMS_RGS_AckSMS_M](#database-reference-sql-sp-tams-rgs-acksms-m)
- [sp_TAMS_RGS_AckSMS_20221214_M](#database-reference-sql-sp-tams-rgs-acksms-20221214-m)
- [sp_TAMS_RGS_AckSurrender](#database-reference-sql-sp-tams-rgs-acksurrender)
- [sp_TAMS_RGS_AckSurrender_20221107](#database-reference-sql-sp-tams-rgs-acksurrender-20221107)
- [sp_TAMS_RGS_AckSurrender_20230308](#database-reference-sql-sp-tams-rgs-acksurrender-20230308)
- [sp_TAMS_RGS_AckSurrender_OSReq](#database-reference-sql-sp-tams-rgs-acksurrender-osreq)
- [sp_TAMS_RGS_AckSurrender_20230209_AllCancel](#database-reference-sql-sp-tams-rgs-acksurrender-20230209-allcancel)
- [sp_TAMS_RGS_Cancel](#database-reference-sql-sp-tams-rgs-cancel)
- [sp_TAMS_RGS_Cancel_20221107](#database-reference-sql-sp-tams-rgs-cancel-20221107)
- [sp_TAMS_RGS_Cancel_20230308](#database-reference-sql-sp-tams-rgs-cancel-20230308)
- [sp_TAMS_RGS_Cancel_20250403](#database-reference-sql-sp-tams-rgs-cancel-20250403)
- [sp_TAMS_RGS_Cancel_OSReq](#database-reference-sql-sp-tams-rgs-cancel-osreq)
- [sp_TAMS_RGS_Cancel_20230209_AllCancel](#database-reference-sql-sp-tams-rgs-cancel-20230209-allcancel)
- [sp_TAMS_RGS_Get_UpdDets](#database-reference-sql-sp-tams-rgs-get-upddets)
- [sp_TAMS_RGS_GrantTOA](#database-reference-sql-sp-tams-rgs-granttoa)
- [sp_TAMS_RGS_GrantTOA_001](#database-reference-sql-sp-tams-rgs-granttoa-001)
- [sp_TAMS_RGS_GrantTOA_20221107](#database-reference-sql-sp-tams-rgs-granttoa-20221107)
- [sp_TAMS_RGS_GrantTOA_20221214](#database-reference-sql-sp-tams-rgs-granttoa-20221214)
- [sp_TAMS_RGS_GrantTOA_20230801](#database-reference-sql-sp-tams-rgs-granttoa-20230801)
- [sp_TAMS_RGS_GrantTOA_20230801_M](#database-reference-sql-sp-tams-rgs-granttoa-20230801-m)
- [sp_TAMS_RGS_OnLoad](#database-reference-sql-sp-tams-rgs-onload)
- [sp_TAMS_RGS_OnLoad_20221107](#database-reference-sql-sp-tams-rgs-onload-20221107)
- [sp_TAMS_RGS_OnLoad_20221118](#database-reference-sql-sp-tams-rgs-onload-20221118)
- [sp_TAMS_RGS_OnLoad_20230202](#database-reference-sql-sp-tams-rgs-onload-20230202)
- [sp_TAMS_RGS_OnLoad_20230707](#database-reference-sql-sp-tams-rgs-onload-20230707)
- [sp_TAMS_RGS_OnLoad_20250128](#database-reference-sql-sp-tams-rgs-onload-20250128)
- [sp_TAMS_RGS_OnLoad_AckSMS](#database-reference-sql-sp-tams-rgs-onload-acksms)
- [sp_TAMS_RGS_OnLoad_AckSMS_20221107](#database-reference-sql-sp-tams-rgs-onload-acksms-20221107)
- [sp_TAMS_RGS_OnLoad_Enq](#database-reference-sql-sp-tams-rgs-onload-enq)
- [sp_TAMS_RGS_OnLoad_Enq_20221107](#database-reference-sql-sp-tams-rgs-onload-enq-20221107)
- [sp_TAMS_RGS_OnLoad_Enq_20230202](#database-reference-sql-sp-tams-rgs-onload-enq-20230202)
- [sp_TAMS_RGS_OnLoad_Enq_20230202_M](#database-reference-sql-sp-tams-rgs-onload-enq-20230202-m)
- [sp_TAMS_RGS_OnLoad_M](#database-reference-sql-sp-tams-rgs-onload-m)
- [sp_TAMS_RGS_OnLoad_Trace](#database-reference-sql-sp-tams-rgs-onload-trace)
- [sp_TAMS_RGS_OnLoad_YD_TEST_20231208](#database-reference-sql-sp-tams-rgs-onload-yd-test-20231208)
- [sp_TAMS_RGS_OnLoad_20221118_M](#database-reference-sql-sp-tams-rgs-onload-20221118-m)
- [sp_TAMS_RGS_OnLoad_20230202_M](#database-reference-sql-sp-tams-rgs-onload-20230202-m)
- [sp_TAMS_RGS_Update_Details](#database-reference-sql-sp-tams-rgs-update-details)
- [sp_TAMS_RGS_Update_QTS](#database-reference-sql-sp-tams-rgs-update-qts)
- [sp_TAMS_RGS_Update_QTS_20230907](#database-reference-sql-sp-tams-rgs-update-qts-20230907)
- [sp_TAMS_RGS_Update_QTS_bak20221229](#database-reference-sql-sp-tams-rgs-update-qts-bak20221229)
- [sp_TAMS_RGS_Update_QTS_test](#database-reference-sql-sp-tams-rgs-update-qts-test)
- [sp_TAMS_Reject_UserRegistrationRequestByRegModID](#database-reference-sql-sp-tams-reject-userregistrationrequestbyregmodid)
- [sp_TAMS_Reject_UserRegistrationRequestByRegModID_20231009](#database-reference-sql-sp-tams-reject-userregistrationrequestbyregmodid-20231009)
- [sp_TAMS_SectorBooking_OnLoad](#database-reference-sql-sp-tams-sectorbooking-onload)
- [sp_TAMS_SectorBooking_OnLoad_bak20230605](#database-reference-sql-sp-tams-sectorbooking-onload-bak20230605)
- [sp_TAMS_SectorBooking_QTS_Chk](#database-reference-sql-sp-tams-sectorbooking-qts-chk)
- [sp_TAMS_SectorBooking_Special_Rule_Chk](#database-reference-sql-sp-tams-sectorbooking-special-rule-chk)
- [sp_TAMS_SectorBooking_SubSet_Chk](#database-reference-sql-sp-tams-sectorbooking-subset-chk)
- [sp_TAMS_SummaryReport_OnLoad](#database-reference-sql-sp-tams-summaryreport-onload)
- [sp_TAMS_SummaryReport_OnLoad_20230713](#database-reference-sql-sp-tams-summaryreport-onload-20230713)
- [sp_TAMS_SummaryReport_OnLoad_Trace](#database-reference-sql-sp-tams-summaryreport-onload-trace)
- [sp_TAMS_SummaryReport_OnLoad_20240112_M](#database-reference-sql-sp-tams-summaryreport-onload-20240112-m)
- [sp_TAMS_SummaryReport_OnLoad_bak20230712](#database-reference-sql-sp-tams-summaryreport-onload-bak20230712)
- [sp_TAMS_SummaryReport_OnLoad_bak20240223](#database-reference-sql-sp-tams-summaryreport-onload-bak20240223)
- [sp_TAMS_TAR_View_Detail_OnLoad](#database-reference-sql-sp-tams-tar-view-detail-onload)
- [sp_TAMS_TB_Gen_Report](#database-reference-sql-sp-tams-tb-gen-report)
- [sp_TAMS_TB_Gen_Report_20230904](#database-reference-sql-sp-tams-tb-gen-report-20230904)
- [sp_TAMS_TB_Gen_Report_20230911](#database-reference-sql-sp-tams-tb-gen-report-20230911)
- [sp_TAMS_TB_Gen_Report_20230915](#database-reference-sql-sp-tams-tb-gen-report-20230915)
- [sp_TAMS_TB_Gen_Report_20231009](#database-reference-sql-sp-tams-tb-gen-report-20231009)
- [sp_TAMS_TB_Gen_Report_20230904_M](#database-reference-sql-sp-tams-tb-gen-report-20230904-m)
- [sp_TAMS_TB_Gen_Report_20230911_M](#database-reference-sql-sp-tams-tb-gen-report-20230911-m)
- [sp_TAMS_TB_Gen_Report_20230915_M](#database-reference-sql-sp-tams-tb-gen-report-20230915-m)
- [sp_TAMS_TB_Gen_Summary](#database-reference-sql-sp-tams-tb-gen-summary)
- [sp_TAMS_TB_Gen_Summary20250120](#database-reference-sql-sp-tams-tb-gen-summary20250120)
- [sp_TAMS_TB_Gen_Summary_20230904](#database-reference-sql-sp-tams-tb-gen-summary-20230904)
- [sp_TAMS_TB_Gen_Summary_20230904_M](#database-reference-sql-sp-tams-tb-gen-summary-20230904-m)
- [sp_TAMS_TOA_Add_Parties1](#database-reference-sql-sp-tams-toa-add-parties1)
- [sp_TAMS_TOA_Add_Parties](#database-reference-sql-sp-tams-toa-add-parties)
- [sp_TAMS_TOA_Add_PointNo](#database-reference-sql-sp-tams-toa-add-pointno)
- [sp_TAMS_TOA_Add_ProtectionType](#database-reference-sql-sp-tams-toa-add-protectiontype)
- [sp_TAMS_TOA_BookOut_Parties](#database-reference-sql-sp-tams-toa-bookout-parties)
- [sp_TAMS_TOA_Delete_Parties](#database-reference-sql-sp-tams-toa-delete-parties)
- [sp_TAMS_TOA_Delete_PointNo](#database-reference-sql-sp-tams-toa-delete-pointno)
- [sp_TAMS_TOA_GenURL](#database-reference-sql-sp-tams-toa-genurl)
- [sp_TAMS_TOA_GenURL_QRCode](#database-reference-sql-sp-tams-toa-genurl-qrcode)
- [sp_TAMS_TOA_Get_Parties](#database-reference-sql-sp-tams-toa-get-parties)
- [sp_TAMS_TOA_Get_PointNo](#database-reference-sql-sp-tams-toa-get-pointno)
- [sp_TAMS_TOA_Get_Station_Name](#database-reference-sql-sp-tams-toa-get-station-name)
- [sp_TAMS_TOA_Login](#database-reference-sql-sp-tams-toa-login)
- [sp_TAMS_TOA_OnLoad](#database-reference-sql-sp-tams-toa-onload)
- [sp_TAMS_TOA_QTS_Chk](#database-reference-sql-sp-tams-toa-qts-chk)
- [sp_TAMS_TOA_QTS_Chk_20230323](#database-reference-sql-sp-tams-toa-qts-chk-20230323)
- [sp_TAMS_TOA_QTS_Chk_20230907](#database-reference-sql-sp-tams-toa-qts-chk-20230907)
- [sp_TAMS_TOA_QTS_Chk_20230323_M](#database-reference-sql-sp-tams-toa-qts-chk-20230323-m)
- [sp_TAMS_TOA_Register](#database-reference-sql-sp-tams-toa-register)
- [sp_TAMS_TOA_Register_20221117](#database-reference-sql-sp-tams-toa-register-20221117)
- [sp_TAMS_TOA_Register_20230107](#database-reference-sql-sp-tams-toa-register-20230107)
- [sp_TAMS_TOA_Register_20230801](#database-reference-sql-sp-tams-toa-register-20230801)
- [sp_TAMS_TOA_Register_20221117_M](#database-reference-sql-sp-tams-toa-register-20221117-m)
- [sp_TAMS_TOA_Register_20230107_M](#database-reference-sql-sp-tams-toa-register-20230107-m)
- [sp_TAMS_TOA_Register_20230801_M](#database-reference-sql-sp-tams-toa-register-20230801-m)
- [sp_TAMS_TOA_Register_bak20230801](#database-reference-sql-sp-tams-toa-register-bak20230801)
- [sp_TAMS_TOA_Save_ProtectionType](#database-reference-sql-sp-tams-toa-save-protectiontype)
- [sp_TAMS_TOA_Submit_Register](#database-reference-sql-sp-tams-toa-submit-register)
- [sp_TAMS_TOA_Surrender](#database-reference-sql-sp-tams-toa-surrender)
- [sp_TAMS_TOA_Update_Details](#database-reference-sql-sp-tams-toa-update-details)
- [sp_TAMS_TOA_Update_TOA_URL](#database-reference-sql-sp-tams-toa-update-toa-url)
- [sp_TAMS_Update_Company_Details_By_ID](#database-reference-sql-sp-tams-update-company-details-by-id)
- [sp_TAMS_Update_External_UserPasswordByUserID](#database-reference-sql-sp-tams-update-external-userpasswordbyuserid)
- [sp_TAMS_Update_External_User_Details_By_ID](#database-reference-sql-sp-tams-update-external-user-details-by-id)
- [sp_TAMS_Update_UserRegModule_ApplicantRegisterCompany](#database-reference-sql-sp-tams-update-userregmodule-applicantregistercompany)
- [sp_TAMS_Update_UserRegModule_ApplicantRegisterCompany_20231009](#database-reference-sql-sp-tams-update-userregmodule-applicantregistercompany-20231009)
- [sp_TAMS_Update_UserRegModule_SysAdminApproval](#database-reference-sql-sp-tams-update-userregmodule-sysadminapproval)
- [sp_TAMS_Update_UserRegModule_SysAdminApproval_20231009](#database-reference-sql-sp-tams-update-userregmodule-sysadminapproval-20231009)
- [sp_TAMS_Update_UserRegModule_SysAdminApproveCompany](#database-reference-sql-sp-tams-update-userregmodule-sysadminapprovecompany)
- [sp_TAMS_Update_UserRegModule_SysAdminApproveCompany_20231009](#database-reference-sql-sp-tams-update-userregmodule-sysadminapprovecompany-20231009)
- [sp_TAMS_Update_UserRegModule_SysOwnerApproval](#database-reference-sql-sp-tams-update-userregmodule-sysownerapproval)
- [sp_TAMS_Update_UserRegModule_SysOwnerApproval_20230112](#database-reference-sql-sp-tams-update-userregmodule-sysownerapproval-20230112)
- [sp_TAMS_Update_UserRegModule_SysOwnerApproval_20231009](#database-reference-sql-sp-tams-update-userregmodule-sysownerapproval-20231009)
- [sp_TAMS_Update_UserRegRole_SysOwnerApproval](#database-reference-sql-sp-tams-update-userregrole-sysownerapproval)
- [sp_TAMS_Update_User_Details_By_ID](#database-reference-sql-sp-tams-update-user-details-by-id)
- [sp_TAMS_User_CheckLastEmailRequest](#database-reference-sql-sp-tams-user-checklastemailrequest)
- [sp_TAMS_User_CheckLastUserRegistration](#database-reference-sql-sp-tams-user-checklastuserregistration)
- [sp_TAMS_UsersManual](#database-reference-sql-sp-tams-usersmanual)
- [sp_TAMS_WithdrawTarByTarID](#database-reference-sql-sp-tams-withdrawtarbytarid)
- [sp_api_send_sms](#database-reference-sql-sp-api-send-sms)
- [uxp_cmdshell](#database-reference-sql-uxp-cmdshell)

<br>


<a id='system-documentation-addcompanyaspx'></a>
# Page: AddCompany.aspx
**File:** AddCompany.aspx.cs

### 1. User Purpose
Users fill out this form to request track access.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and loads user-specific data. |
| setupPage | Prepares the UI for the current user by setting up form fields. |
| btn_externalSave_Click | Saves the company information to the database and redirects the user. |
| btn_externalCancel_Click | Cancels the current action and returns the user to the previous page. |

### 3. Data Interactions
* **Reads:** User
* **Writes:** Company

---

# Page: AnonymousSite.Master
**File:** AnonymousSite.Master.cs

### 1. User Purpose
Sets up the layout for anonymous user access.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the master page layout and loads common elements. |

### 3. Data Interactions
* **Reads:** None
* **Writes:** None

---

# Page: BasePage.aspx
**File:** BasePage.aspx.cs

### 1. User Purpose
Provides common functionality for all pages, including database access.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the base page and sets up database connection parameters. |
| GetSqlConnection | Establishes a connection to the database. |
| GetSqlCommand | Creates a SQL command for database operations. |
| GetSqlDataAdapter | Prepares data adapters for retrieving or updating data. |

### 3. Data Interactions
* **Reads:** User, Company, Track
* **Writes:** User, Company, Track

---

# Page: DTCAuth.aspx
**File:** DTCAuth.aspx.cs

### 1. User Purpose
Manages user authentication and session token generation.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the authentication page and checks session validity. |
| SessionExpire | Handles session expiration by redirecting the user. |
| GenerateToken | Creates a secure session token for authenticated users. |

### 3. Data Interactions
* **Reads:** User, Session
* **Writes:** Session, Token

---


<a id='system-documentation-defaultaspx'></a>
# Page: Default.aspx  
**File:** Default.aspx.cs  

### 1. User Purpose  
Users access this page to navigate the application's main interface.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads default user settings. |  

### 3. Data Interactions  
* **Reads:** UserPreferences  
* **Writes:** None  

---

# Page: DepotTARAppList.aspx  
**File:** DepotTARAppList.aspx.cs  

### 1. User Purpose  
Users manage and view depot TAR applications, including filtering and navigating through records.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the application list and binds data to UI controls. |  
| BindLocation | Populates location-based filters for the application list. |  
| lbSubmit_Click | Submits user input to filter or update the application list. |  
| displayLegend | Shows visual indicators for application statuses or categories. |  
| gvDir1_RowDataBound | Customizes grid rows to highlight specific application details. |  
| lnkD1StrTARNo_Click | Navigates to a detailed view for a specific TAR number. |  
| lbBack_Click | Returns to the previous navigation level (e.g., from a detail view). |  
| gvDir1Child_RowDataBound | Renders child grid rows for nested application data. |  
| ddlLine_SelectedIndexChanged | Filters the application list based on selected line or category. |  

### 3. Data Interactions  
* **Reads:** DepotApp, Location, TAR, Line  
* **Writes:** TAR (updates status or notes)

---


<a id='system-documentation-depottarapplication'></a>
# Page: DepotTARApplication  
**File:** DepotTARApplication.aspx.cs  

### 1. User Purpose  
Users submit track access applications with details about possession or protection of railway lines.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, binds location data, and sets up grid views for display. |  
| btnSubmit_Click | Validates user input, saves application details to the database, and sends confirmation emails. |  
| BindLocation | Loads available railway lines and locations into dropdown controls for user selection. |  
| BindGrid | Populates grid views with sector-specific data (e.g., blocked tracks, access types). |  
| displayDates | Populates date fields based on selected track type, access type, and location. |  
| showHideControls | Toggles visibility of form sections depending on whether the user selects "Possession" or "Protection" for track access. |  
| GridView1_RowDataBound | Formats grid rows to highlight critical data (e.g., blocked tracks) for visual clarity. |  
| ddlLine_SelectedIndexChanged | Updates form controls (e.g., dates, sectors) based on the selected railway line. |  
| rbPossession_CheckedChanged | Adjusts form layout and available options when the user selects "Possession" as the access type. |  
| rbProtection_CheckedChanged | Adjusts form layout and available options when the user selects "Protection" as the access type. |  

### 3. Data Interactions  
* **Reads:** TarType, BlockedTar, DepotTarSector, DepotTar  
* **Writes:** DepotTar (application details), BlockedTar (updates to blocked track records)

---


<a id='system-documentation-depottarenquiry'></a>
# Page: DepotTAREnquiry  
**File:** DepotTAREnquiry.aspx.cs  

### 1. User Purpose  
Users search and manage Track Access Request (TAR) records, including submitting new requests, resetting filters, and performing actions like printing or deleting records.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, binds data on first load, and sets up default filters. |  
| bindGrid | Loads TAR records into the grid based on a filter indicator (e.g., active/inactive status). |  
| ddlLine_SelectedIndexChanged | Updates the grid to display TAR records for the selected line. |  
| btnSubmit_Click | Validates user input, saves new TAR data, and triggers confirmation logic. |  
| btnReset_Click | Clears all filters and resets the form to its initial state. |  
| btnPrint_Click | Generates a printable view of the TAR records in the grid. |  
| GridView1_RowCommand | Handles user actions like approving or withdrawing a TAR from the grid. |  
| GridView1_RowDeleting | Confirms and deletes a TAR record from the database. |  
| btnWithdrawTARConfirm_Click | Confirms the withdrawal of a TAR and updates its status in the system. |  

### 3. Data Interactions  
* **Reads:** Track Access Request (TAR) records, Line information, TAR status details  
* **Writes:** Updates TAR status, deletes TAR records, saves new TAR submissions  

---

# Page: DepotTAREnquiry_Detail  
**File:** DepotTAREnquiry_Detail.aspx.cs  

### 1. User Purpose  
Users view detailed information about a specific Track Access Request (TAR), including related operational and power requirements, and approve or modify TAR details.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads detailed TAR information into the page controls. |  
| gvOperationReq_RowDataBound | Formats and displays operational requirements for the TAR. |  
| gvPowerReq_RowDataBound | Formats and displays power requirements for the TAR. |  
| lvTarApproval_ItemDataBound | Populates approval status and related details for TAR records. |  
| Button1_Click | Approves the TAR, updates its status, and triggers confirmation logic. |  

### 3. Data Interactions  
* **Reads:** Track Access Request (TAR) details, Operational requirements, Power requirements, Approval status  
* **Writes:** Updates TAR approval status

---


<a id='system-documentation-depottarenquiry-print'></a>
# Page: DepotTAREnquiry_Print  
**File:** DepotTAREnquiry_Print.aspx.cs  

### 1. User Purpose  
Users view a print-friendly version of a TAREnquiry record.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page for printing, possibly loading data into controls for display. |  

### 3. Data Interactions  
* **Reads:** TAREnquiry  
* **Writes:** None

---


<a id='system-documentation-depottarform'></a>
# Page: DepotTARForm  
**File:** DepotTARForm.aspx.cs  

### 1. User Purpose  
Users manage TAR (Track Access Request) forms, including uploading documents, configuring access settings, and submitting requests.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| **Page_Load** | Initializes the form, loads default data, and sets up UI state based on user permissions. |  
| **Tab1_Click / Tab2_Click / Tab3_Click** | Navigates between form sections (tabs) and initializes tab-specific fields. |  
| **PopOnLoad** | Pre-fills form fields with existing TAR data or default values. |  
| **chkOR_CheckedChanged** | Toggles visibility of related fields based on checkbox selection. |  
| **btnUploadOR_Click** | Handles file uploads for attachments, saves metadata to the database. |  
| **lnkDelete_Click / lnkDownload_Click** | Deletes or retrieves attachments from the TAMS_TAR_Attachment_Temp table. |  
| **lbtnPossAPLAdd_Click / lbtnPossWLAdd_Click / lbtnPossOPAdd_Click** | Adds entries to access lists (e.g., approved users, watchlist, operators). |  
| **gvPossAddPL_RowCommand / gvPossAddWL_RowCommand / gvPossAddOO_RowCommand** | Manages row-level actions (e.g., edit/delete) for access lists. |  
| **lbNextV1_Click / lbNextV2_Click / lbNextV3_Click** | Advances users through form validation stages. |  
| **lbSubmitV2_Click** | Validates all form data, saves TAR details to the database, and finalizes the request. |  
| **valAccDets** | Validates access configuration details (e.g., roles, permissions) before submission. |  

### 3. Data Interactions  
* **Reads:** TARAccessReq, TARId, TARAccessReqId, UserRoles, AttachmentMetadata (TAMS_TAR_Attachment_Temp)  
* **Writes:** TARAccessReq, TARId, TARAccessReqId, UserRoles, AttachmentMetadata (TAMS_TAR_Attachment_Temp)

---


<a id='system-documentation-depottarform-app'></a>
# Page: DepotTARForm_App  
**File:** DepotTARForm_App.aspx.cs  

### 1. User Purpose  
Users manage TAR (Track Access Request) forms, including viewing details, adding buffer zones, and handling approval/rejection actions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, loads default data, and sets up UI state. |  
| Tab1_Click | Switches the interface to the "Request Details" tab for form input. |  
| Tab2_Click | Switches to the "Attachments" tab to display or download files. |  
| Tab3_Click | Switches to the "Conflict Check" tab to review overlapping TAR requests. |  
| PopOnLoad | Preloads data such as user permissions or existing TAR records. |  
| lnkDownload_Click | Retrieves and downloads an attachment file from the database using the TARAccessReqId. |  
| dgOR_ItemDataBound | Binds data to DataGrid controls for displaying TAR-related records. |  
| gvPossAddPL_RowDataBound | Populates GridView rows for power line additions during TAR processing. |  
| gvPossAddWL_RowDataBound | Populates GridView rows for water line additions during TAR processing. |  
| gvPossAddOO_RowDataBound | Populates GridView rows for overhead line additions during TAR processing. |  
| dgPossPowerSector_ItemDataBound | Binds data to DataGrid for power sector-specific TAR details. |  
| lbtnAddBufferZone_Click | Triggers the addition of a buffer zone entry for conflict mitigation. |  
| gvAddBufferZone_RowDataBound | Displays buffer zone entries in a GridView for review. |  
| gvAddBufferZone_RowCommand | Handles user actions (e.g., editing/deleting) on buffer zone entries. |  
| lbCReject_Click | Marks a TAR request as rejected and updates its status in the system. |  
| lbProcToApp_Click | Moves a TAR request to the "Processing" stage for further review. |  
| lbNReject_Click | Notes a rejection reason and finalizes the TAR request closure. |  
| lbEndorse_Click | Approves a TAR request and initiates the access granting process. |  
| lbtnTARID_Click | Filters or searches TAR records by specific identifier (e.g., TARAccessReqId). |  
| gvConflictTAR_RowDataBound | Displays conflicting TAR records in a GridView for resolution. |  

### 3. Data Interactions  
* **Reads:** TARAccessReqId, FileName, FileType, FileUpload (from TAMS_TAR_Attachment)  
* **Writes:** TARAccessReqId (for status updates, buffer zone entries, and conflict records)

---


<a id='system-documentation-depottarinbox'></a>
# Page: DepotTARInbox  
**File:** DepotTARInbox.aspx.cs  

### 1. User Purpose  
Users manage Track Access Request (TAR) inbox entries, including viewing, filtering, and submitting TAR applications.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, loads location data, and binds TAR entries to the grid. |  
| BindLocation | Loads location-specific data to filter TAR entries. |  
| lbSubmit_Click | Validates user input, saves the TAR application, and updates the inbox status. |  
| lnkD1StrTARNo_Click | Navigates to a specific TAR entry in the first directory. |  
| lnkD2StrTARNo_Click | Navigates to a specific TAR entry in the second directory. |  
| lbAppList_Click | Filters TAR entries based on user-selected criteria. |  
| gvDir1_RowDataBound | Formats GridView rows to highlight critical TAR details (e.g., urgency, status). |  
| ddlLine_SelectedIndexChanged | Refreshes TAR listings based on the selected line or track. |  

### 3. Data Interactions  
* **Reads:** TAREntry, Location, UserPermissions  
* **Writes:** TAREntry, UserActivityLog  

---

# Page: DepotTARSectorBooking  
**File:** DepotTARSectorBooking.aspx.cs  

### 1. User Purpose  
Users book specific sectors for Track Access Requests (TAR), specifying access details and permissions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads pre-configured sector booking data and initializes user interface elements. |  
| PopOnLoad | Fetches sector availability and populates dropdowns for access type and duration. |  
| lbSubmit_Click | Validates sector booking details, saves the request, and updates access permissions. |  
| RBLPowerReq_SelectedIndexChanged | Adjusts available sectors based on selected power request type. |  
| cbDir1All_CheckedChanged | Toggles selection of all sectors in the first directory. |  
| gvDir1_RowDataBound | Highlights sectors with pending or approved status in the GridView. |  
| lbAppList_Click | Filters sector bookings based on user role or access level. |  
| lbBack_Click | Returns to the previous TAR management page. |  
| lbDiagram_Click | Displays a visual diagram of sectors for spatial reference. |  
| chkSel_CheckedChanged | Updates sector selection state for bulk operations. |  

### 3. Data Interactions  
* **Reads:** SectorDefinition, AccessPermission, TAREntry  
* **Writes:** SectorBooking, UserAccessHistory

---


<a id='system-documentation-externallogin'></a>
# Page: ExternalLogin  
**File:** ExternalLogin.aspx.cs  

### 1. User Purpose  
Users log in using an external authentication provider.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and checks if the user is already authenticated. |  
| btnLogin_Click | Triggers the external login process and redirects the user. |  
| CheckAccess | Validates if the user has access to the system based on external provider data. |  
| linkB_forgetPassword_Click | Sends a password reset link to the user's registered email address. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: GenQRCode  
**File:** GenQRCode.aspx.cs  

### 1. User Purpose  
Users generate a QR code for a specified URL or data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the QR code generation interface. |  
| btnGen_Click | Generates a QR code image based on user input and displays it. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: Login  
**File:** Login.aspx.cs  

### 1. User Purpose  
Users authenticate with a username and password or LAN credentials.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the login form and checks for existing session data. |  
| btnLogin_Click | Validates user credentials and redirects to the dashboard. |  
| InternalLoginCheck | Performs core authentication logic and checks user permissions. |  
| CheckAccess | Verifies if the user has access to the system based on role or permissions. |  
| GenerateToken | Creates a secure token for authenticated sessions. |  
| CheckLANAuthentication | Authenticates user via LAN network credentials and returns a token. |  
| Encrypt | Encrypts sensitive data before storing or transmitting. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: Logout  
**File:** Logout.aspx.cs  

### 1. User Purpose  
Users log out of their session.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Ends the user's session and redirects to the login page. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None

---


<a id='system-documentation-maintaincompany'></a>
# Page: MaintainCompany  
**File:** MaintainCompany.aspx.cs  

### 1. User Purpose  
Users manage company information, including searching, clearing, and viewing company data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads company data dynamically. |  
| SetupPage | Configures UI elements and prepares the interface for user interaction. |  
| btn_search_Click | Filters and displays company records based on user input criteria. |  
| btn_clear_Click | Resets all input fields and clears displayed data. |  

### 3. Data Interactions  
* **Reads:** Company, SystemSelection  
* **Writes:** Company  

---

# Page: MaintainCompanyDetails  
**File:** MaintainCompanyDetails.aspx.cs  

### 1. User Purpose  
Users update specific company details based on a preselected company ID.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads company details into the form for editing. |  
| setupPage | Fetches and populates company data using the provided companyID. |  
| btn_updateCompany_Click | Saves modified company information to the database. |  
| btn_back_Click | Navigates back to the company listing view. |  

### 3. Data Interactions  
* **Reads:** Company  
* **Writes:** Company  

---

# Page: MaintainUser  
**File:** MaintainUser.aspx.cs  

### 1. User Purpose  
Users manage user information, including searching, clearing, and viewing user data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads user data dynamically. |  
| SetupPage | Configures UI elements and prepares the interface for user interaction. |  
| btn_search_Click | Filters and displays user records based on user input criteria. |  
| btn_clear_Click | Resets all input fields and clears displayed data. |  

### 3. Data Interactions  
* **Reads:** User, SystemSelection  
* **Writes:** User  

---

# Page: MaintainUserDetails  
**File:** MaintainUserDetails.aspx.cs  

### 1. User Purpose  
Users update specific user details based on a preselected user ID.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads user details into the form for editing. |  
| setupPage | Fetches and populates user data using the provided userID. |  
| btn_updateUser_Click | Saves modified user information to the database. |  
| btn_back_Click | Navigates back to the user listing view. |  

### 3. Data Interactions  
* **Reads:** User  
* **Writes:** User

---


<a id='system-documentation-newusersignup'></a>
# Page: NewUserSignUp
**File:** NewUserSignUp.aspx.cs

### 1. User Purpose
Users create new user accounts with internal or external access options.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and sets up UI elements based on user type. |
| ResetPage | Clears form fields to start a new entry. |
| SetupPage | Configures the page layout or options depending on internal/external flag. |
| buildSystemSelectiondata | Populates dropdowns or selection lists for system options. |
| btn_internalNewSave_Click | Validates user input, saves the new user to the database, and redirects to a confirmation page. |
| btn_internalNewCancel_Click | Cancels the operation, resets the form, and returns to the previous page. |
| btn_externalSave_Click | Validates user input, saves the external user to the database, and redirects to a confirmation page. |
| btn_externalCancel_Click | Cancels the operation, resets the form, and returns to the previous page. |

### 3. Data Interactions
* **Reads:** User, BlockedTar
* **Writes:** User, BlockedTar

---

# Page: OCCSearch_Roster
**File:** OCCSearch_Roster.aspx.cs

### 1. User Purpose
Users search and view employee rosters filtered by line or track.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Loads initial data and sets up the search criteria. |
| bindSearchCriteria | Populates dropdowns or filters for searching. |
| bindFirstShift | Loads data for the first shift into a grid. |
| bindSecondShift | Loads data for the second shift into a grid. |
| bindThirdShift | Loads data for the third shift into a grid. |
| btnSearchRoster_Click | Executes the search based on selected criteria and updates the grids. |
| ddlLine_SelectedIndexChanged | Filters the search based on the selected line and updates the data. |
| ddlTrack_SelectedIndexChanged | Filters the search based on the selected track and updates the data. |
| btnRefresh_Click | Reloads the data without changing the search criteria. |
| gvFirstShift_RowDataBound | Formats the grid rows for the first shift. |
| gvSecondShift_RowDataBound | Formats the grid rows for the second shift. |
| gvThirdShift_RowDataBound | Formats the grid rows for the third shift. |

### 3. Data Interactions
* **Reads:** Shift, User, Line, Track
* **Writes:** None

---


<a id='system-documentation-occupdate-roster'></a>
# Page: OCCUpdate_Roster  
**File:** OCCUpdate_Roster.aspx.cs  

### 1. User Purpose  
Users update and manage shift assignments for track operations.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, loads default data, and sets up event handlers. |  
| bindSearchCriteria | Loads filter options for line, track, and shift selection. |  
| loadTrackType | Populates track type dropdown with available track types. |  
| bindFirstShift | Binds first shift data to the corresponding GridView. |  
| bindSecondShift | Binds second shift data to the corresponding GridView. |  
| bindThirdShift | Binds third shift data to the corresponding GridView. |  
| ddlLine_SelectedIndexChanged | Refreshes shift data based on selected line. |  
| ddlTrack_SelectedIndexChanged | Refreshes shift data based on selected track. |  
| gvFirstShift_RowDataBound | Formats rows in the first shift GridView (e.g., highlights status). |  
| gvSecondShift_RowDataBound | Formats rows in the second shift GridView (e.g., highlights status). |  
| gvThirdShift_RowDataBound | Formats rows in the third shift GridView (e.g., highlights status). |  
| btnUpdateRoster_Click | Saves changes to shift assignments and updates the roster. |  
| btnRefresh_Click | Reloads shift data to reflect the latest changes. |  

### 3. Data Interactions  
* **Reads:** Shift, Employee, Track, Line, ShiftAssignment  
* **Writes:** ShiftAssignment, EmployeeShift, TrackAssignment  

---

# Page: OCC_HoursAuthorisation  
**File:** OCC_HoursAuthorisation.aspx.cs  

### 1. User Purpose  
Users submit or preview authorized hours for operational duties.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads user-specific data and initializes the hours grid. |  
| BindGrid | Populates the hours grid with authorization records. |  
| LoadOCCAuthCtrl_DTL | Loads detailed authorization data for a specific user. |  
| LoadOCCAuthCtrl_NEL | Loads nested authorization data (e.g., duty roster details). |  
| GridView1_RowDataBound | Formats rows in the hours grid (e.g., highlights approval status). |  
| GridView1_RowCreated | Sets up row templates for dynamic content in the hours grid. |  
| btnSubmit_Click | Submits authorized hours for approval and saves the record. |  
| ddlLine_SelectedIndexChanged | Filters hours data based on selected line. |  
| btnPreview_Click | Generates a preview of authorized hours for review. |  

### 3. Data Interactions  
* **Reads:** HoursAuthorization, DutyRoster, User, AuthorizationDetail  
* **Writes:** HoursAuthorization, AuthorizationDetail, DutyRoster

---


<a id='system-documentation-occ-hoursauthorisation-preview'></a>
# Page: OCC_HoursAuthorisation_Preview  
**File:** OCC_HoursAuthorisation_Preview.aspx.cs  

### 1. User Purpose  
Users preview authorized OCC hours and manage duty roster data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes page controls and loads default data. |  
| BindGrid | Loads and displays authorized OCC hours data in a grid. |  
| LoadDutyRoster_Ctrl | Populates duty roster details for the current user. |  
| LoadOCCAuthPreviewCtrl_DTL | Loads detailed authorization data for the preview. |  
| LoadOCCAuthPreviewCtrl_NEL | Loads non-essential line data for the preview. |  
| ddlLine_SelectedIndexChanged | Filters data based on selected line and updates the grid. |  
| btnSearchOCC_Preview_Click | Triggers a search for specific OCC hours and refreshes the grid. |  
| btnBackToOCCAuth_Click | Navigates the user back to the main authorization interface. |  

### 3. Data Interactions  
* **Reads:** DutyRoster, OCCAuthorization, User  
* **Writes:** OCCAuthorization (updates or saves changes)  

---

# Page: OPD  
**File:** OPD.aspx.cs  

### 1. User Purpose  
Users manage operational data and refresh line information.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes page controls and loads default line data. |  
| PopOnLoad | Populates initial operational data and line details. |  
| ddlLine_SelectedIndexChanged | Filters operational data based on selected line. |  
| lbRefresh_Click | Reloads and updates line information from the database. |  

### 3. Data Interactions  
* **Reads:** Line, OperationalData  
* **Writes:** OperationalData (updates or saves changes)

---


<a id='system-documentation-rgs'></a>
# Page: RGS
**File:** RGS.aspx.cs

### 1. User Purpose
Users manage track access requests, update details, and grant depot permissions through a grid interface.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and loads track access data into the grid. |
| PopOnLoad | Sets up UI elements and permissions for the user. |
| gvRGS_RowDataBound | Binds data to grid rows and formats display fields. |
| gvRGS_RowCommand | Handles user actions like editing or deleting track access records. |
| ddlLine_SelectedIndexChanged | Filters track access data based on selected line. |
| lbRefresh_Click | Reloads track access data from the database. |
| lbCancelTOA_Click | Cancels an active track access request. |
| ddlUpdTARID_SelectedIndexChanged | Updates track access details based on selected TAR ID. |
| lbUpdDets_Click | Saves changes to track access details. |
| updQTS | Updates track access status with encoded/decoded data. |
| Timer_Tick | Periodically refreshes track access data. |
| lbGrantTOADepot_Click | Grants depot access permissions to a user. |

### 3. Data Interactions
* **Reads:** User, BlockedTar, TrackAccess
* **Writes:** User, BlockedTar, TrackAccess

---

# Page: RGSAckSMS
**File:** RGSAckSMS.aspx.cs

### 1. User Purpose
Users acknowledge SMS notifications related to track access requests and confirm completion of actions.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Loads SMS acknowledgment data and initializes the page. |
| lbAck_Click | Confirms receipt of an SMS and updates the status. |
| lblComplete_Click | Marks an SMS acknowledgment as complete. |
| PopOnLoad | Sets up UI elements for SMS acknowledgment. |

### 3. Data Interactions
* **Reads:** User, BlockedTar, TrackAccess
* **Writes:** User, BlockedTar, TrackAccess

---


<a id='system-documentation-rgsenquiry'></a>
# Page: RGSEnquiry  
**File:** RGSEnquiry.aspx.cs  

### 1. User Purpose  
Users view and filter RGS data by line and track, refresh results, and print reports.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, loads dropdowns, and sets up the grid view. |  
| loadDepotControl | Populates depot selection options for filtering. |  
| PopOnLoad | Sets default values for line and track filters. |  
| gvRGS_RowDataBound | Formats grid rows for display (e.g., highlights status). |  
| ddlLine_SelectedIndexChanged | Filters RGS data based on selected line. |  
| ddlTrack_SelectedIndexChanged | Filters RGS data based on selected track. |  
| lbRefresh_Click | Reloads RGS data with current filters. |  
| gvRGS_RowCommand | Handles user actions like editing or deleting RGS records. |  
| lbPrint_Click | Triggers printing of the RGS grid in a formatted layout. |  

### 3. Data Interactions  
* **Reads:** RGS, Line, Track  
* **Writes:** None  

---

# Page: RGSPrint  
**File:** RGSPrint.aspx.cs  

### 1. User Purpose  
Users print RGS data in a formatted layout.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads RGS data into the grid for printing. |  
| gvRGS_RowDataBound | Applies formatting to grid rows for print (e.g., bold headers). |  
| gvRGS_RowCommand | Handles print-related actions (e.g., exporting to PDF). |  

### 3. Data Interactions  
* **Reads:** RGS  
* **Writes:** None  

---

# Page: RegistrationInbox  
**File:** RegistrationInbox.aspx.cs  

### 1. User Purpose  
Users manage registration inbox items, view encrypted data, and set up user pages.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads user-specific inbox data and initializes the grid. |  
| SetupPage | Configures page settings based on the logged-in user. |  
| EncryptID | Applies encryption to data identifiers for security. |  

### 3. Data Interactions  
* **Reads:** User, Message  
* **Writes:** None

---


<a id='system-documentation-registrationrequest'></a>
# Page: RegistrationRequest  
**File:** RegistrationRequest.aspx.cs  

### 1. User Purpose  
Users manage registration requests by approving, rejecting, or modifying access for new users.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads user data based on the request context. |  
| SetupPage | Prepares the interface with specific registration details and permissions. |  
| BuildPage | Constructs the UI elements for editing or viewing a registration request. |  
| ResetPage | Clears form fields and resets the user interface to a default state. |  
| btn_back_Click | Navigates the user back to a previous step in the registration workflow. |  
| btn_assignAccess_Click | Grants or modifies access rights for the requested user. |  
| btn_rejectRequest_Click | Marks the registration request as rejected and updates its status. |  
| btn_approveCompany_Click | Approves a company's registration request and finalizes the process. |  
| btn_rejectCompany_Click | Rejects a company's registration request and updates its status. |  
| btn_resendLink_Click | Sends a new confirmation link to the user's registered email address. |  
| btn_deleteRequest_Click | Removes the registration request from the system. |  

### 3. Data Interactions  
* **Reads:** UserRegistration, Company, SystemRole  
* **Writes:** UserRegistration, Company, SystemRole  

---

# Page: ResetPassword  
**File:** ResetPassword.aspx.cs  

### 1. User Purpose  
Users reset their password by entering a new one and confirming it.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the password reset form and initializes user-specific data. |  
| setupPage | Populates the form with user details based on the provided UserRegID. |  
| btn_externalSave_Click | Validates the new password, updates the user's credentials, and confirms the change. |  
| btn_externalCancel_Click | Cancels the password reset process and redirects the user to a previous page. |  

### 3. Data Interactions  
* **Reads:** UserRegistration  
* **Writes:** UserRegistration

---


<a id='system-documentation-signupnewsystem'></a>
# Page: SignUpNewSystem  
**File:** SignUpNewSystem.aspx.cs  

### 1. User Purpose  
Users register a new system by providing details and selecting system types.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads system data for display. |  
| SetupPage | Configures the form layout and pre-fills fields based on user context. |  
| ResetPage | Clears form inputs and resets the UI state. |  
| buildSystemSelectiondata | Generates a dataset of system options for dropdowns or grids. |  
| UpdateGVRows | Populates grid rows with system details and formatting. |  
| gv_internalNewSystem_RowDataBound | Applies conditional styling or labels to grid rows. |  
| btn_externalNext_Click | Advances the user to the next step in the external system registration flow. |  
| btn_internalNewSave_Click | Validates inputs, saves the new system record, and confirms completion. |  

### 3. Data Interactions  
* **Reads:** System, User, BlockedTar  
* **Writes:** System, User  

---

# Page: SiteMaster  
**File:** Site.Master.cs  

### 1. User Purpose  
Provides navigation and user-specific actions for the main application layout.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| linkB_signUpNewSystem_Click | Redirects the user to the `SignUpNewSystem` page. |  
| Page_Load | Loads user-specific data (e.g., profile links) into the master page. |  

### 3. Data Interactions  
* **Reads:** User, System  
* **Writes:** None  

---

# Page: SummaryReport  
**File:** SummaryReport.aspx.cs  

### 1. User Purpose  
Users generate and filter summary reports based on system or line selections.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads default report parameters and initializes the UI. |  
| lbSearch_Click | Triggers report generation based on user input. |  
| ddlLine_SelectedIndexChanged | Updates available report options based on selected line. |  
| PopOnLoad | Pre-fills dropdowns or filters with default values. |  

### 3. Data Interactions  
* **Reads:** ReportData, Line, System  
* **Writes:** None

---


<a id='system-documentation-tarapplist'></a>
# Page: TARAppList  
**File:** TARAppList.aspx.cs  

### 1. User Purpose  
Users view and manage TAR applications, submit new requests, and navigate between records.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| **Page_Load** | Initializes the page, binds TAR application data to GridViews, and displays a legend for status indicators. |  
| **lbSubmit_Click** | Validates user input, saves new TAR application data, and redirects to a confirmation or summary page. |  
| **displayLegend** | Renders a visual legend explaining status icons or colors used in the GridViews. |  
| **gvDir1_RowDataBound / gvDir2_RowDataBound** | Applies conditional formatting to GridView rows (e.g., highlights approved/rejected statuses). |  
| **lnkD1StrTARNo_Click / lnkD2StrTARNo_Click** | Opens a detailed view of a specific TAR application when a user clicks a link in the GridView. |  
| **lbBack_Click** | Returns the user to a previous page or refreshes the TAR application list. |  
| **gvDir1Child_RowDataBound / gvDir2Child_RowDataBound** | Formats child GridView rows to display related data (e.g., supporting documents or comments). |  

### 3. Data Interactions  
* **Reads:** TARApp, TARApplicationDetails, Status  
* **Writes:** TARApp (when submitting new applications)

---


<a id='system-documentation-tarapplication'></a>
# Page: TARApplication  
**File:** TARApplication.aspx.cs  

### 1. User Purpose  
Users submit track access requests, select lines and access types, and view associated dates and sector information.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| **Page_Load** | Initializes the page by binding grid views and setting up UI elements based on user session data. |  
| **BindGrid** | Loads and displays track sector data into grid views for user review. |  
| **btnSubmit_Click** | Validates user input, saves track access request details to the database, and sends confirmation notifications. |  
| **displayDates** | Formats and displays date ranges for specific track sectors based on access type and line selection. |  
| **showHideControls** | Toggles visibility of UI elements (e.g., date pickers) depending on the selected access type. |  
| **GridView1_RowDataBound** | Highlights rows in the main grid based on access type (e.g., possession vs. protection). |  
| **ddlLine_SelectedIndexChanged** | Updates displayed data and date ranges when the user selects a different track line. |  
| **rbPossession_CheckedChanged / rbProtection_CheckedChanged** | Adjusts UI visibility and data bindings based on whether the user selects possession or protection access. |  

### 3. Data Interactions  
* **Reads:** TarSector, BlockedTar, User  
* **Writes:** TarSector, BlockedTar

---


<a id='system-documentation-tarblockdate'></a>
# Page: TARBlockDate  
**File:** TARBlockDate.aspx.cs  

### 1. User Purpose  
Users manage block date records, including viewing, searching, and modifying block dates associated with rail lines.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads block date data when the page is first accessed. |  
| ReloadRecs | Refreshes the grid view with updated block date records based on current filters. |  
| gvBlockDate_RowDataBound | Formats grid rows to highlight specific block date details or apply conditional styling. |  
| gvBlockDate_RowCommand | Handles user actions like editing or deleting a block date record from the grid. |  
| lbSearch_Click | Triggers a search for block dates based on user input criteria. |  
| lbNew_Click | Opens a new block date entry form for user input. |  
| ddlRail_SelectedIndexChanged | Filters block date records dynamically based on the selected rail line. |  

### 3. Data Interactions  
* **Reads:** BlockDate, Rail  
* **Writes:** BlockDate  

---

# Page: TARBlockDate_Add  
**File:** TARBlockDate_Add.aspx.cs  

### 1. User Purpose  
Users create new block date records by entering details such as dates, rail lines, and associated track information.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the form with default values and initializes controls for new record entry. |  
| lbtnAddBlockDate_Click | Validates user input, saves the new block date to the database, and redirects to the main block date list. |  
| lbtnAddCancel_Click | Closes the form and returns the user to the main block date management page. |  

### 3. Data Interactions  
* **Writes:** BlockDate

---


<a id='system-documentation-tarenquiry'></a>
# Page: TAREnquiry  
**File:** TAREnquiry.aspx.cs  

### 1. User Purpose  
Users view and manage Track Access Requests (TAR) by filtering, paginating, and performing actions like submission, deletion, or withdrawal.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page, binds data, and sets up UI controls. |  
| bindGrid | Loads TAR data into the grid based on a filter indicator (e.g., active/inactive status). |  
| ddlLine_SelectedIndexChanged | Refreshes the TAR grid when the user selects a different line from the dropdown. |  
| btnSubmit_Click | Validates user input, saves the TAR request, and triggers confirmation logic. |  
| btnReset_Click | Clears all form fields and resets filters. |  
| btnPrint_Click | Generates a printable version of the TAR grid data. |  
| GridView1_RowCommand | Handles user actions like editing or deleting a TAR entry. |  
| GridView1_RowDataBound | Formats grid rows (e.g., highlights status, displays additional details). |  
| GridView1_RowDeleting | Confirms deletion of a TAR record before removing it. |  
| btnWithdrawTARConfirm_Click | Confirms withdrawal of a TAR request and updates its status. |  

### 3. Data Interactions  
* **Reads:** TAR, Line, User, BlockedTar  
* **Writes:** TAR, BlockedTar  

---

# Page: TAREnquiry_Detail  
**File:** TAREnquiry_Detail.aspx.cs  

### 1. User Purpose  
Users view and edit detailed Track Access Request (TAR) information, including possession limits and operational requirements.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads TAR details, possession limits, and operational requirements into the form. |  
| BindPossessionLimit | Populates possession limit data for the selected TAR. |  
| gvOperationReq_RowDataBound | Formats operational requirement rows (e.g., displays timestamps, status). |  
| gvPowerReq_RowDataBound | Formats power requirement rows with conditional styling. |  
| lvTarApproval_ItemDataBound | Customizes approval status display in list views. |  
| Button1_Click | Saves changes to possession limits or operational requirements. |  
| gvPossLimit_PageIndexChanging | Updates possession limit data when the user navigates pages. |  

### 3. Data Interactions  
* **Reads:** TAR, PossessionLimit, OperationReq, PowerReq  
* **Writes:** PossessionLimit, OperationReq

---


<a id='system-documentation-tarenquiry-print'></a>
# Page: TAREnquiry_Print  
**File:** TAREnquiry_Print.aspx.cs  

### 1. User Purpose  
Users view a print-friendly version of a TAREnquiry form.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page for print display, loads necessary data into controls |  

### 3. Data Interactions  
* **Reads:** {No specific entities/tables mentioned}  
* **Writes:** {No specific entities/tables mentioned}

---


<a id='system-documentation-tarform'></a>
# Page: TARForm
**File:** TARForm.aspx.cs

### 1. User Purpose
Users complete a multi-tab form to request track access, manage attachments, and define access permissions.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes page state, loads base data, and sets up UI elements |
| Tab1_Click | Navigates to the first tab section of the form |
| Tab2_Click | Navigates to the second tab section of the form |
| Tab3_Click | Navigates to the third tab section of the form |
| PopOnLoad | Preloads data and sets initial form state |
| chkOR_CheckedChanged | Updates UI based on checkbox selection for OR documents |
| dgOR_ItemDataBound | Binds OR document data to DataGrid controls |
| btnUploadOR_Click | Handles file upload for OR documents |
| lnkDelete_Click | Deletes selected OR document entries |
| lnkDownload_Click | Retrieves and displays attachment metadata from the database |
| lbtnPossAPLAdd_Click | Adds access permission entries to the application list |
| lbtnPossWLAdd_Click | Adds access permission entries to the worklist |
| lbtnPossOPAdd_Click | Adds access permission entries to the operations list |
| gvPossAddPL_RowDataBound | Binds data to GridView controls for permission lists |
| gvPossAddPL_RowCommand | Handles row-level actions in permission list GridView |
| ddlDeptComp_SelectedIndexChanged | Updates form based on selected department/component |
| lbCancelV1_Click | Cancels form submission at validation step 1 |
| lbNextV1_Click | Proceeds to validation step 2 |
| lbCancelV2_Click | Cancels form submission at validation step 2 |
| lbNextV2_Click | Proceeds to validation step 3 |
| lbCancelV3_Click | Cancels form submission at final validation step |
| lbNextV3_Click | Proceeds to final submission confirmation |
| lbSubmitV2_Click | Submits form data for processing |
| dgPossPowerSector_ItemDataBound | Binds power sector data to DataGrid controls |
| ddlBreakersOut_SelectedIndexChanged | Updates form based on selected breaker configuration |
| valAccDets | Validates access details before allowing form submission |

### 3. Data Interactions
* **Reads:** TAMS_TAR_Attachment_Temp (attachment metadata), User (access permissions), BlockedTar (blocked track records)
* **Writes:** TAMS_TAR_Attachment_Temp (attachment storage), TARAccessReq (access request records), TARAccess (permission definitions)

---


<a id='system-documentation-tarform-app'></a>
# Page: TARForm_App  
**File:** TARForm_App.aspx.cs  

### 1. User Purpose  
Users manage TAR (Track Access Request) applications, including viewing attachments, adding buffer zones/TVF stations, and approving/rejecting requests.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes page state and loads default data (e.g., TAR details, attachments). |  
| Tab1_Click | Switches to the main TAR request view. |  
| Tab2_Click | Switches to the buffer zone management section. |  
| Tab3_Click | Switches to the TVF station management section. |  
| PopOnLoad | Loads initial data (e.g., user permissions, TAR status) when the page loads. |  
| lnkDownload_Click | Retrieves and displays TAR attachments from the database. |  
| dgOR_ItemDataBound | Binds data to DataGrid controls for displaying TAR-related records. |  
| gvPossAddPL_RowDataBound | Formats GridView rows for adding power line entries. |  
| gvPossAddWL_RowDataBound | Formats GridView rows for adding work location entries. |  
| gvPossAddOO_RowDataBound | Formats GridView rows for adding operational override entries. |  
| dgPossPowerSector_ItemDataBound | Binds power sector data to DataGrid for display. |  
| lbtnAddBufferZone_Click | Triggers adding a new buffer zone entry. |  
| gvAddBufferZone_RowDataBound | Formats GridView rows for buffer zone management. |  
| gvAddBufferZone_RowCommand | Handles user actions (e.g., delete) on buffer zone entries. |  
| lbtnAddTVFStation_Click | Triggers adding a new TVF station entry. |  
| gvAddTVF_RowDataBound | Formats GridView rows for TVF station management. |  
| gvAddTVF_RowCommand | Handles user actions (e.g., delete) on TVF station entries. |  
| lbCReject_Click | Rejects a TAR request and updates the status. |  
| lbProcToApp_Click | Processes a TAR request for approval. |  
| lbNReject_Click | Rejects a TAR request with additional notes. |  
| lbEndorse_Click | Endorses a TAR request for final approval. |  
| lbtnTARID_Click | Searches or filters TAR records by ID. |  
| gvConflictTAR_RowDataBound | Formats GridView rows to show conflicting TAR entries. |  
| rblTVFRunMode_SelectedIndexChanged | Updates TVF run mode settings based on user selection. |  

### 3. Data Interactions  
* **Reads:** TARAccessReq, TARAccess, BlockedTar, User, TAMS_TAR_Attachment  
* **Writes:** TARAccessReq, TARAccess, BlockedTar, User

---


<a id='system-documentation-tarinbox'></a>
# Page: TARInbox  
**File:** TARInbox.aspx.cs  

### 1. User Purpose  
Users manage and interact with tracking requests in their inbox.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads inbox data into grids and initializes user interface elements. |  
| lbSubmit_Click | Submits a new tracking request, validates inputs, and updates the inbox. |  
| lnkD1StrTARNo_Click | Filters or navigates to a specific tracking request in the first directory grid. |  
| lnkD2StrTARNo_Click | Filters or navigates to a specific tracking request in the second directory grid. |  
| lbAppList_Click | Opens or modifies a selected tracking request from the list. |  
| gvDir1_RowDataBound | Formats rows in the first directory grid (e.g., highlights status, adds action buttons). |  
| gvDir2_RowDataBound | Formats rows in the second directory grid (e.g., displays additional metadata). |  

### 3. Data Interactions  
* **Reads:** TAR, User, BlockedTar  
* **Writes:** TAR, User  

---

# Page: TARSectorBooking  
**File:** TARSectorBooking.aspx.cs  

### 1. User Purpose  
Users book sectors for track access, specifying power requirements and access details.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads sector booking form and initializes data for available sectors. |  
| PopOnLoad | Sets up default values or pre-fills fields based on user context. |  
| lbSubmit_Click | Processes the sector booking request, validates inputs, and saves the booking. |  
| ChkSeq | Validates sequence numbers for sector selection to prevent duplicates. |  
| RBLPowerReq_SelectedIndexChanged | Updates power requirement details based on user selection. |  
| cbDir1All_CheckedChanged | Toggles selection of all items in the first directory grid. |  
| cbDir2All_CheckedChanged | Toggles selection of all items in the second directory grid. |  
| gvDir1_RowDataBound | Formats rows in the first directory grid (e.g., highlights availability, adds action buttons). |  
| gvDir2_RowDataBound | Formats rows in the second directory grid (e.g., displays additional metadata). |  
| lbAppList_Click | Opens or modifies a selected sector booking from the list. |  
| lbBack_Click | Navigates back to the previous page or cancels the booking process. |  

### 3. Data Interactions  
* **Reads:** Sector, Booking, User  
* **Writes:** Booking, Sector

---


<a id='system-documentation-tarviewdetails'></a>
# Page: TARViewDetails  
**File:** TARViewDetails.aspx.cs  

### 1. User Purpose  
Users view detailed information about a Track Access Request (TAR) and related party data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads TAR data into controls. |  
| PopOnLoad | Sets up data bindings for grids and lists on the page. |  
| dgOR_ItemDataBound | Formats or highlights specific data rows in the OR grid. |  
| gvPossAddPL_RowDataBound | Customizes display of Power Line data in the grid. |  
| gvPossAddWL_RowDataBound | Formats data for Work Locations in the grid. |  
| gvPossAddOO_RowDataBound | Adjusts display for Ownership data in the grid. |  
| dgPossPowerSector_ItemDataBound | Applies styling or logic to Power Sector data rows. |  
| lbBack_Click | Navigates users back to the previous TAR listing or overview. |  

### 3. Data Interactions  
* **Reads:** TAR, BlockedTar, Parties, PowerLine, WorkLocation, Ownership, PowerSector  
* **Writes:** None (data is read-only for this page)  

---

# Page: TOAAddParties  
**File:** TOAAddParties.aspx.cs  

### 1. User Purpose  
Users manage parties (e.g., individuals or organizations) associated with a Track Ownership Agreement (TOA).  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads TOA data and binds party information to grids. |  
| bindPoints | Populates dropdowns or lists with relevant points based on TOA ID. |  
| lbNextV1_Click | Advances to the next step in the party addition workflow. |  
| Tab1_Click / Tab2_Click | Switches between tabs for different party types or views. |  
| lbPrevV2_Click | Returns to the previous step in the workflow. |  
| lbAddParties_Click | Triggers logic to add a new party to the TOA. |  
| gvParties_RowDataBound | Customizes display of party data in the grid. |  
| gvParties_RowCommand | Handles user actions like editing or deleting a party entry. |  

### 3. Data Interactions  
* **Reads:** TOA, Parties, Points  
* **Writes:** Parties (adds or updates party records)  

---

# Page: TOA.Master  
**File:** TOA.Master.cs  

### 1. User Purpose  
Provides a shared layout and navigation structure for TOA-related pages.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes master page controls like navigation menus or headers. |  

### 3. Data Interactions  
* **Reads:** None (master page does not directly interact with data)  
* **Writes:** None

---


<a id='system-documentation-toaapplication'></a>
# Page: TOAApplication  
**File:** TOAApplication.aspx.cs  

### 1. User Purpose  
Users submit application forms and authenticate to access tracking services.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes page controls and checks user authentication status. |  
| lbtnSubmit_Click | Validates form inputs, encodes data using ToEncode, saves application details, and redirects to a confirmation page. |  
| getLoginResponse | Verifies user credentials against the database and returns a login status message. |  
| LogError | Records error messages to a static log file for troubleshooting. |  

### 3. Data Interactions  
* **Reads:** User, ApplicationRegistry  
* **Writes:** ApplicationRegistry

---


<a id='system-documentation-toabookin'></a>
# Page: TOABookIn  
**File:** TOABookIn.aspx.cs  

### 1. User Purpose  
Users navigate through tabs to book in a TOA (Track Access) request, add parties, and submit the form.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| **Page_Load** | Initializes the page, loads default data, and sets up UI state. |  
| **loadProtectionType** | Loads protection type options into a dropdown list for user selection. |  
| **BindWitness** | Binds witness-related data to a grid or list control for display. |  
| **Tab1_Click / Tab2_Click / Tab3_Click** | Switches the user between different sections (tabs) of the booking form. |  
| **lbNextV1_Click / lbNextV2_Click / lbPrevV2_Click / lbPrevV3_Click** | Navigates through form steps or views (e.g., next/previous pages in a multi-step process). |  
| **lbSubmit_Click** | Validates form data, saves the TOA request, and processes submission. |  
| **gvParties_RowCommand** | Handles user actions (e.g., edit/delete) on rows in the parties grid. |  
| **lbAddParties_Click** | Opens a dialog or form to add new parties associated with the TOA request. |  
| **saveProtectionType** | Saves the selected or edited protection type configuration. |  
| **GVProtectionType_RowCommand** | Manages row-level actions (e.g., delete or edit) for protection type entries. |  
| **rBtnProtectionList_SelectedIndexChanged** | Updates the UI or data based on the selected protection type in a radio button list. |  

### 3. Data Interactions  
* **Reads:** ProtectionType, Witness, Party, TOA  
* **Writes:** TOA, Party, ProtectionType

---


<a id='system-documentation-toabookout'></a>
# Page: TOABookOut  
**File:** TOABookOut.aspx.cs  

### 1. User Purpose  
Users manage track booking requests and track surrender processes.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads booking data into the interface. |  
| lbNextV1_Click | Advances the user through multi-step booking process. |  
| Tab1_Click | Switches to the first tab for booking details. |  
| Tab2_Click | Switches to the second tab for party information. |  
| lbPrevV2_Click | Returns to the previous step in the booking process. |  
| lbAddParties_Click | Opens a dialog to add additional parties to the booking. |  
| gvParties_RowDataBound | Formats grid row data for party information display. |  
| gvParties_RowCommand | Handles user actions (e.g., edit/delete) on party records. |  
| lbSurrender_Click | Triggers the surrender process for a booked track. |  
| LogError | Records error messages for debugging purposes. |  

### 3. Data Interactions  
* **Reads:** TOAReg, Parties, TrackDetails  
* **Writes:** TOAReg, Parties, TrackDetails  

---

# Page: TOAError  
**File:** TOAError.aspx.cs  

### 1. User Purpose  
Users view error messages or system alerts related to track operations.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Displays error details to the user. |  

### 3. Data Interactions  
* **Reads:** ErrorLogs  
* **Writes:** None  

---

# Page: TOAGenURL  
**File:** TOAGenURL.aspx.cs  

### 1. User Purpose  
Users generate encoded or decoded URLs for track access.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the URL generation interface. |  
| lblGen_Click | Triggers URL encoding or decoding based on user input. |  
| ToEncode | Converts input string to an encoded URL format. |  
| ToDecode | Converts an encoded URL back to its original string. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: TVFAcknowledgement  
**File:** TVFAcknowledgement.aspx.cs  

### 1. User Purpose  
Users view acknowledgment records for TVF (Track Vehicle Form) submissions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the acknowledgment interface and binds grid data. |  
| BindGrid | Populates the grid with TVF acknowledgment records. |  
| LoadOCCTVF_AckCtrl | Fetches specific acknowledgment details based on user ID. |  

### 3. Data Interactions  
* **Reads:** TVFAcknowledgement, OCCTVF  
* **Writes:** None

---


<a id='system-documentation-tvfacknowledgement-enquiry'></a>
# Page: TVFAcknowledgement_Enquiry  
**File:** TVFAcknowledgement_Enquiry.aspx.cs  

### 1. User Purpose  
Users search and view acknowledgment records related to TVF (Traffic Violation Form) submissions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads default data for the user interface. |  
| BindGrid | Loads acknowledgment records into a grid for display. |  
| LoadOCCTVF_AckCtrl | Populates a control with user-specific acknowledgment details based on a provided user ID. |  
| btnSearch_Click | Filters and displays acknowledgment records based on user input criteria. |  

### 3. Data Interactions  
* **Reads:** TVFAcknowledgement, User, BlockedTar  
* **Writes:** None  

---

# Page: Test  
**File:** Test.aspx.cs  

### 1. User Purpose  
Users interact with a test page to verify basic functionality or display static content.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads initial data or sets up the test environment. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None  

---

# Page: TrafficBulletin  
**File:** TrafficBulletin.aspx.cs  

### 1. User Purpose  
Users generate and export traffic bulletin reports, including possession and summary reports.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads default report parameters. |  
| btnGeneratePossessionReport_Click | Triggers the generation of a possession report and exports it as a PDF. |  
| ddlLine_SelectedIndexChanged | Filters report data based on selected line or route. |  
| btnGenerateSummaryReport_Click | Generates a summary report based on user-selected criteria. |  
| btnGenerateReport_Click | Initiates the report generation process for custom parameters. |  

### 3. Data Interactions  
* **Reads:** Tar, Line, ReportTemplate  
* **Writes:** None  

---

# Page: UserDetailView  
**File:** UserDetailView.aspx.cs  

### 1. User Purpose  
Users view detailed information about a user and request email access to their account.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads user details and displays them in the interface. |  
| btn_requestViewEmail_Click | Sends an email request to grant view access to the user's account. |  

### 3. Data Interactions  
* **Reads:** User, EmailRequest  
* **Writes:** EmailRequest  

---

# Page: UserDetailViewFrmEmail  
**File:** UserDetailViewFrmEmail.aspx.cs  

### 1. User Purpose  
Users fill out a form to request email access to a user's account, selecting system options for the request.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the email request form and initializes system selection options. |  
| buildDummySystemSelectiondata | Generates placeholder data for system selection dropdowns. |  

### 3. Data Interactions  
* **Reads:** System, EmailRequest  
* **Writes:** EmailRequest

---


<a id='system-documentation-viewprofile'></a>
# Page: ViewProfile  
**File:** ViewProfile.aspx.cs  

### 1. User Purpose  
Users view and manage their profile information, including system selections and access settings.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads user data into the interface. |  
| SetupPage | Configures the UI based on user role (internal/external) and preloads system options. |  
| ResetPage | Clears form fields and resets the interface to its initial state. |  
| btn_externalNext_Click | Advances the external user through the profile setup workflow. |  
| btn_internalNewSave_Click | Saves internal user profile changes to the database. |  

### 3. Data Interactions  
* **Reads:** User, SystemSelection, AccessSettings  
* **Writes:** User, AccessSettings  

---

# Page: ViewSignUpStatus  
**File:** ViewSignUpStatus.aspx.cs  

### 1. User Purpose  
Users check the status of their registration request and manage resend options for verification links.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Displays user registration status based on provided dataset. |  
| SetupPage | Populates UI elements with user-specific registration details. |  
| btn_resendRegistrationLink_Click | Triggers a resend of the verification link to the user’s email. |  

### 3. Data Interactions  
* **Reads:** User, RegistrationStatus  
* **Writes:** RegistrationStatus  

---

# Page: ViewSwitcher  
**File:** ViewSwitcher.ascx.cs  

### 1. User Purpose  
Users switch between different views (e.g., internal vs. external) within the application.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Dynamically loads and displays the appropriate view based on user permissions. |  

### 3. Data Interactions  
* **Reads:** None  
* **Writes:** None

---


<a id='system-documentation-occauthcc-dtl'></a>
# Page: OCCAuthCC_DTL  
**File:** OCCAuthCC_DTL.ascx.cs  

### 1. User Purpose  
Users view and manage access records for specific tracks.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads access records into the grid. |  
| populateOCCAuth | Loads track access data into the user interface. |  
| GridView1_RowDataBound | Formats grid rows (e.g., highlights specific entries). |  
| btnSubmit_Click | Saves changes to the selected access record. |  

### 3. Data Interactions  
* **Reads:** Access records, TrackType  
* **Writes:** Updated access records  

---

# Page: OCCAuthPFR_DTL  
**File:** OCCAuthPFR_DTL.ascx.cs  

### 1. User Purpose  
Users review and submit access requests for specific track types.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads track type access data. |  
| populateOCCAuth | Loads track type access data into the user interface. |  
| GridView1_RowDataBound | Formats grid rows (e.g., highlights specific entries). |  
| btnSubmit_Click | Submits the access request for approval. |  

### 3. Data Interactions  
* **Reads:** Track type access records  
* **Writes:** Submitted access requests  

---

# Page: OCCAuthPreview  
**File:** OCCAuthPreview.ascx.cs  

### 1. User Purpose  
Users preview grouped access records for review.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the page and loads grouped access data. |  
| populateOCCAuthPreview | Loads and groups access records for display. |  
| ShowingGroupingDataInGridView | Organizes grid rows into grouped sections. |  
| GridView1_RowDataBound | Formats grid rows (e.g., applies styling to grouped headers). |  
| GridView1_RowCreated | Sets up grouping headers for the grid. |  

### 3. Data Interactions  
* **Reads:** Access records, TrackType  
* **Writes:** None (data is only viewed)

---


<a id='system-documentation-occauthpreview-nel'></a>
# Page: OCCAuthPreview_NEL
**File:** OCCAuthPreview_NEL.ascx.cs

### 1. User Purpose
Users view authorization details for a specific line and operation date.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the control and loads authorization data into the GridView |
| populateOCCAuthPreview | Binds authorization records to the GridView for display |
| GridView1_RowDataBound | Formats GridView rows to highlight specific data or apply styling |
| GridView1_RowCreated | Sets up initial row structure for the GridView |

### 3. Data Interactions
* **Reads:** [Authorization Records]
* **Writes:** []

---

# Page: OCCAuthPreview_Roster
**File:** OCCAuthPreview_Roster.ascx.cs

### 1. User Purpose
Users view duty roster assignments for specific lines and operation dates.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the control and binds duty roster data to the GridView sections |
| bindFirstShift | Loads first shift assignments into the corresponding GridView |
| bindSecondShift | Loads second shift assignments into the corresponding GridView |
| bindThirdShift | Loads third shift assignments into the corresponding GridView |
| searchDutyRoster | Filters and updates the GridView sections based on user input criteria |
| gvFirstShift_RowDataBound | Formats first shift GridView rows to highlight specific data |
| gvSecondShift_RowDataBound | Formats second shift GridView rows to highlight specific data |
| gvThirdShift_RowDataBound | Formats third shift GridView rows to highlight specific data |

### 3. Data Interactions
* **Reads:** [Duty Roster Assignments]
* **Writes:** []

---

# Page: OCCAuthTC_DTL
**File:** OCCAuthTC_DTL.ascx.cs

### 1. User Purpose
Users submit track access requests and view detailed authorization records.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the control and loads authorization records into the GridView |
| populateOCCAuth | Binds detailed authorization data to the GridView for display |
| GridView1_RowDataBound | Formats GridView rows to highlight specific data or apply styling |
| btnSubmit_Click | Validates user input, saves the access request, and updates the authorization records |

### 3. Data Interactions
* **Reads:** [Authorization Records]
* **Writes:** [Authorization Records]

---


<a id='system-documentation-occauth-nel'></a>
# Page: OCCAuth_NEL  
**File:** OCCAuth_NEL.ascx.cs  

### 1. User Purpose  
Users submit access requests for track operations by providing details like user ID, line, track type, access date, and roster code.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the control and loads user data into the interface. |  
| populateOCCAuth | Loads a list of access requests into a grid for review. |  
| GridView1_RowDataBound | Applies formatting or additional logic to individual grid rows. |  
| btnSubmit_Click | Validates user input, saves the access request to the database, and confirms submission. |  

### 3. Data Interactions  
* **Reads:** User, AccessRequest  
* **Writes:** AccessRequest  

---

# Page: OCCAuth_NEL_bak  
**File:** OCCAuth_NEL_bak.ascx.cs  

### 1. User Purpose  
Users submit access requests for track operations using a legacy interface with similar functionality to the active version.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the control and loads user data into the interface. |  
| populateOCCAuth | Loads a list of access requests into a grid for review. |  
| GridView1_RowDataBound | Applies formatting or additional logic to individual grid rows. |  
| btnSubmit_Click | Validates user input, saves the access request to the database, and confirms submission. |  

### 3. Data Interactions  
* **Reads:** User, AccessRequest  
* **Writes:** AccessRequest  

---

# Page: OCCTVF_Ack  
**File:** OCCTVF_Ack.ascx.cs  

### 1. User Purpose  
Users review, approve, reject, or modify access requests by interacting with a grid of pending requests and associated remarks.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the control and loads pending access requests into the interface. |  
| populateOCCTVF_Ack | Loads a list of access requests into a grid for review. |  
| GridView1_RowDataBound | Applies formatting or additional logic to individual grid rows. |  
| btnSubmit_Click | Approves an access request and updates the status in the database. |  
| btnReject_Click | Rejects an access request and updates the status in the database. |  
| ShowRemark | Displays additional remarks or notes related to a specific request. |  
| btnSave_Click | Saves changes to remarks or other metadata associated with an access request. |  
| ShowTarTVF | Displays related track or TVF (Train Vehicle File) data for a specific request. |  

### 3. Data Interactions  
* **Reads:** AccessRequest, Remark, Track, TVF  
* **Writes:** AccessRequest, Remark

---


<a id='system-documentation-occtvf-ack-preview'></a>
# Page: OCCTVF_Ack_Preview  
**File:** OCCTVF_Ack_Preview.ascx.cs  

### 1. User Purpose  
Users review and submit/reject track access requests with associated operational data.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Initializes the control and loads preview data into the GridView. |  
| populateOCCTVF_Ack | Loads track access request details into the GridView for display. |  
| GridView1_RowDataBound | Formats or highlights specific rows in the GridView based on data. |  
| btnSubmit_Click | Validates user input, saves the request, and confirms submission. |  
| btnReject_Click | Marks the request as rejected and updates the status in the system. |  
| ShowRemark | Displays additional notes or comments related to the track access request. |  
| btnSave_Click | Saves any edited changes to the track access request data. |  
| ShowTarTVF | Reveals detailed technical information about the track access request. |  

### 3. Data Interactions  
* **Reads:** TrackAccess, User, OperationalData, Roster  
* **Writes:** TrackAccess, User, OperationalData  

---

# Page: menu  
**File:** menu.ascx.cs  

### 1. User Purpose  
Users access a dynamic navigation menu tailored to their role and permissions.  

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |  
| :--- | :--- |  
| Page_Load | Loads the menu structure based on user authentication and permissions. |  
| Generate_Menu | Builds the menu hierarchy using user-specific role data. |  
| Generate_Menu2 | Creates an alternative menu layout for specific user scenarios (e.g., internet users). |  

### 3. Data Interactions  
* **Reads:** User, Role, Permission  
* **Writes:** None

---


<a id='database-reference-sql-ealertq-enqueue'></a>
# Procedure: EAlertQ_EnQueue

### Purpose
This stored procedure enqueues an email alert by inserting a new record into the EAlertQ table and creating corresponding records in the EAlertQTo, EAlertQCC, and EAlertQBCC tables for recipients, CC, and BCC respectively.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sender | nvarchar(100) | The sender's email address. |
| @Subject | nvarchar(500) | The subject of the email alert. |
| @Sys | nvarchar(100) | System information. |
| @Greetings | ntext | Greetings message. |
| @AlertMsg | nvarchar(max) | The main content of the email alert. |
| @UserId | nvarchar(50) | The user ID of the sender. |
| @SendTo | ntext | The recipient's email address separated by a separator. |
| @CC | ntext | The CC recipients' email addresses separated by a separator. |
| @BCC | ntext | The BCC recipients' email addresses separated by a separator. |
| @Separator | nvarchar(1) | The separator used to separate recipient, CC, and BCC email addresses. |
| @AlertID | decimal(18, 0) output | The ID of the newly created alert record. |
| @From | nvarchar(250) = null | The sender's full name (optional). |

### Logic Flow
1. Check if the `@SendTo` parameter is null; if so, exit the procedure.
2. Insert a new record into the EAlertQ table with the provided data.
3. Extract the recipient email addresses from the `@SendTo` parameter using the separator and insert corresponding records into the EAlertQTo table.
4. Repeat step 3 for CC recipients in the `@CC` parameter.
5. Repeat step 3 for BCC recipients in the `@BCC` parameter.
6. Drop temporary tables created during the procedure.

### Data Interactions
* **Reads:** EAlertQ, EAlertQTo, EAlertQCC, EAlertQBCC
* **Writes:** EAlertQ

---


<a id='database-reference-sql-ealertq-enqueue-external'></a>
# Procedure: EAlertQ_EnQueue_External

### Purpose
This stored procedure enqueues an external alert, which includes sending emails to recipients specified in the CC and BCC fields.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @From	| nvarchar(250) | The sender's email address. |
| @Sender	| nvarchar(100) | The sender's name. |
| @Subject	nvarchar(500) | The subject of the email. |
| @Sys	| nvarchar(100) | System information. |
| @Greetings	ntext | Greeting message for the email. |
| @AlertMsg	ntext | Alert message for the email. |
| @UserId	| nvarchar(50) | User ID who created the alert. |
| @SendTo	| ntext | Email addresses to send the alert to. |
| @CC		| ntext | Email addresses in the CC field. |
| @BCC		| ntext | Email addresses in the BCC field. |
| @Attachment	nvarchar(500) | Attachment file for the email. |
| @Separator	nvarchar(1) | Separator used to split email addresses. |
| @AlertID	decimal(18, 0)	output | Unique ID of the enqueued alert. |

### Logic Flow
The procedure follows these steps:

1. It inserts a new record into the `EAlertQ` table with the provided sender information.
2. If an Alert ID is generated, it inserts another record into the `EAlertQAtt` table to mark the alert as active.
3. It creates temporary tables for CC and BCC recipients and reads their email addresses from the ntext fields.
4. For each recipient in the CC and BCC lists, it inserts a new record into the `EAlertQTo`, `EAlertQCC`, or `EAlertQBCC` table, depending on whether they are in the CC or BCC field.
5. After processing all recipients, it drops the temporary tables.

### Data Interactions
* **Reads:** EAlertQ, EAlertQAtt, EAlertQTo, EAlertQCC, EAlertQBCC

---


<a id='database-reference-sql-smsealertq-enqueue'></a>
# Procedure: SMSEAlertQ_EnQueue

### Purpose
This stored procedure enqueues a new SMS alert by inserting data into several tables, including SMSEAlertQ, EAletQTo, EAletQCC, and EAletQBCC.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sender | nvarchar(100) | The sender's name. |
| @Subject | nvarchar(500) | The subject of the SMS alert. |
| @Sys | nvarchar(100) | System information. |
| @Greetings | ntext | Greetings message. |
| @AlertMsg | ntext | Alert message. |
| @UserId | nvarchar(50) | User ID. |
| @SendTo | ntext | Recipient's email address. |
| @CC | ntext | CC recipient's email address. |
| @BCC | ntext | BCC recipient's email address. |
| @Separator | nvarchar(1) | Separator character used in the email addresses. |
| @AlertID | decimal(18, 0) output | The ID of the newly created alert. |
| @From | nvarchar(250) = null | Optional sender's name (default is null). |

### Logic Flow
The procedure follows these steps:

1. It checks if the `@SendTo` parameter is null and returns immediately if it is.
2. It inserts a new record into the `SMSEAlertQ` table with the provided data.
3. It creates temporary tables `#tsendto`, `#tcc`, and `#tbcc` to store the recipient's email addresses, CC recipients' email addresses, and BCC recipients' email addresses, respectively.
4. For each type of recipient (SendTo, CC, and BCC), it reads the email address from the temporary table using a pointer to the ntext data type.
5. It inserts new records into the corresponding tables (`EAletQTo`, `EAletQCC`, and `EAletQBCC`) with the alert ID and recipient's email address.
6. After processing all recipients, it drops the temporary tables.
7. Finally, it commits the transaction and returns.

### Data Interactions
* Reads: SMSEAlertQ, EAletQTo, EAletQCC, EAletQBCC
* Writes: SMSEAlertQ, EAletQTo, EAletQCC, EAletQBCC

---


<a id='database-reference-sql-smtp-get-email-attachments'></a>
# Procedure: SMTP_GET_Email_Attachments

The purpose of this stored procedure is to retrieve the file path of email attachments associated with a specific alert.

### Parameters
| Name | Type | Purpose |
| @AlertID | int | Identifies the unique identifier for the alert whose attachments are to be retrieved. |

### Logic Flow
1. The procedure starts by selecting data from the EAlertQAtt table.
2. It filters the results based on two conditions: the Active flag must be set to 1, and the AlertID parameter passed in must match the one stored in the database for the current alert.
3. Once filtered, the procedure returns only the FPath column, which presumably contains the file path of the email attachment.

### Data Interactions
* **Reads:** EAlertQAtt table

---


<a id='database-reference-sql-smtp-get-email-lists'></a>
# Procedure: SMTP_GET_Email_Lists

### Purpose
This procedure is used to send email alerts using SMTP by retrieving a list of email recipients and their corresponding alert messages.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | Inferred usage |

### Logic Flow
The procedure starts by deleting any stale data from the EAlertQBCC, EAlertQCC, and EAlertQTo tables. It then retrieves a list of active alerts with no message assigned (AlertMsg IS NULL) and deletes these records.

Next, it selects a subset of records from the EALERTQ table where the status is 'Q' and Active = 1, along with their corresponding alert messages, senders, IDs, and recipient lists. The recipient list is generated by joining the EALERTQTO table on ALERTID and filtering out inactive recipients.

Finally, it orders the results by AlertID and returns a list of greetings, subjects, alert messages, senders, system information, CC recipients, BCC recipients, and the actual recipient for each active alert.

---


<a id='database-reference-sql-smtp-get-email-lists-frm'></a>
# Procedure: SMTP_GET_Email_Lists_Frm

### Purpose
This procedure retrieves email lists for sending alerts using SMTP, filtering active and queued alerts.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | Retrieves the ALERTID parameter. |

### Logic Flow
1. The procedure starts by setting the transaction isolation level to SERIALIZABLE.
2. It then selects data from several tables, including EALERTQ and EALERTQTO, based on specific conditions (status='Q' and Active=1).
3. For each ALERTID in the selected data, it retrieves the corresponding RECIPIENT list by joining EALERTQTO with a subquery that filters out inactive recipients.
4. The procedure then selects additional data from EALERTQ for each ALERTID, including GREETINGS, SUBJECT, AlertMsg, SENDER, and FROM fields.
5. Finally, it orders the results by ALERTID.

### Data Interactions
* **Reads:** EALERTQ, EALERTQTO

---


<a id='database-reference-sql-smtp-update-email-lists'></a>
# Procedure: SMTP_Update_Email_Lists

### Purpose
This procedure updates the status of an alert in the EALERTQ table and sends an email notification using SMTP.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_AlertID | int | The ID of the alert to be updated. |
| @p_SysID | varchar(50) | The system ID of the user updating the alert. |
| @p_Status | varchar(1) | The new status of the alert. |
| @p_ErrorMsg | varchar(255) OUTPUT | An output parameter to store any error messages. |

### Logic Flow
The procedure starts by setting an initial value for the @p_ErrorMsg parameter. It then updates the EALERTQ table with the provided @p_AlertID, @p_Status, and @p_SysID values. The LASTUPDATEDON field is also updated to the current date and time. If any errors occur during this process, they are stored in the @p_ErrorMsg parameter.

### Data Interactions
* **Reads:** EALERTQ table (specifically, the AlertID column)
* **Writes:** EALERTQ table (specifically, the Status, LASTUPDATEDON, and LASTUPDATEDBY columns)

---


<a id='database-reference-sql-sp-call-smtp-send-smsalert'></a>
# Procedure: SP_Call_SMTP_Send_SMSAlert

### Purpose
This stored procedure sends SMS alerts using SMTP for a list of recipients.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Message | NVARCHAR(500) | Output parameter containing the result message |

### Logic Flow
1. The procedure starts by checking if there are any open transactions, and if not, it sets a flag to indicate that an internal transaction has started.
2. It then initializes variables for storing the alert ID, sender, recipient, alert message, and system name.
3. A cursor is opened to iterate over the SMSEAlertQ table where the status is 'Q', which indicates that the alert needs to be sent.
4. For each row in the cursor, another cursor is opened to retrieve the recipients for the current alert ID.
5. The procedure then executes a stored procedure (SP_SMTP_SMS_NetPage) to send SMS alerts to the recipients using SMTP.
6. After sending the SMS alerts, the status of the SMSEAlertQ table is updated to 'S' to indicate that the alert has been sent successfully.
7. If any errors occur during the process, an error message is stored in the @Message variable and the procedure returns it.

### Data Interactions
* **Reads:** dbo.SMSEAlertQ
* **Writes:** dbo.SMSEAlertQ

---


<a id='database-reference-sql-sp-checkpagepermission'></a>
# Procedure: SP_CheckPagePermission

### Purpose
This stored procedure checks if a user has permission to access a specific menu.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @userid | nvarchar(50) | The ID of the user to check permissions for. |
| @menuid | nvarchar(50) | The ID of the menu to check permissions against. |
| @res | bit OUTPUT | A flag indicating whether the user has permission (1) or not (0). |

### Logic Flow
The procedure first checks if a user exists in the system and if they have been assigned a role that includes access to the specified menu. It does this by joining multiple tables: TAMS_Menu_Role, TAMS_Role, TAMS_User_Role, and TAMS_User. If a match is found, it sets @res to 1; otherwise, it sets @res to 0.

### Data Interactions
* **Reads:** TAMS_Menu_Role, TAMS_Role, TAMS_User_Role, and TAMS_User

---


<a id='database-reference-sql-sp-smtp-sms-netpage'></a>
# Procedure: SP_SMTP_SMS_NetPage

### Purpose
This stored procedure sends an SMS alert using NetPage, a third-party service that allows for sending SMS messages programmatically.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @From | varchar(100) | The sender's email address. |
| @To | varchar(max) | The recipient's mobile number. |
| @ActualMsg | varchar(max) | The actual message to be sent in the SMS. |
| @AlertiD | int | A unique identifier for the alert. |
| @SysName | varchar(100) | The system name (e.g., SMTP). |

### Logic Flow
1. The procedure starts by declaring variables for the state ID, PC number, and SQL command.
2. It sets the state ID to the recipient's mobile number and concatenates the actual message with a prefix to create the PC number.
3. It deletes any SMS alerts from the database that are older than 60 days.
4. It inserts a new record into the SMTP_SMSAlertQ table, which logs the sent SMS alert, including the sender's email address, recipient's mobile number, alert ID, message, system name, and timestamp.
5. If an error occurs during this process, it raises an error with a specific message.
6. Finally, it executes a command to send the SMS using the NetPage service, which involves executing a batch file that takes the state ID and PC number as arguments.

### Data Interactions
* Reads: None explicitly stated; however, it is assumed that the procedure interacts with the database tables SMTP_SMSAlertQ.
* Writes: 
  * SMTP_SMSAlertQ table (inserting new records)

---


<a id='database-reference-sql-sp-smtp-send-smsalert'></a>
# Procedure: SP_SMTP_Send_SMSAlert

### Purpose
This stored procedure sends SMS alerts using SMTP for all pending alerts in the SMSEAlertQ table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @p_Alertid | int | Alert ID of the alert to be sent |
| @p_from | varchar(100) | Sender's email address |
| @p_To | varchar(100) | Recipient's email address |
| @p_Alertmsg | varchar(max) | SMS message content |
| @p_sysname | varchar(50) | System name |

### Logic Flow
1. The procedure starts by declaring variables for the alert ID, sender's email, recipient's email, SMS message, and system name.
2. It then opens a cursor to iterate over all pending alerts in the SMSEAlertQ table where the status is 'Q'.
3. For each alert, it opens another cursor to retrieve the recipient's email address from the SMSEAlertTo table matching the current alert ID.
4. The procedure then executes the SP_SMTP_SMS_NetPage stored procedure for each recipient, passing in the sender's email, recipient's email, SMS message, alert ID, and system name as parameters.
5. After sending the SMS alert, the procedure updates the status of the alert in the SMSEAlertQ table to 'S' and sets the LastUpdatedOn and LastUpdatedBy fields accordingly.
6. The process repeats for all pending alerts until there are no more records to fetch.

### Data Interactions
* **Reads:** SMSEAlertQ, SMSEAlertTo
* **Writes:** SMSEAlertQ

---


<a id='database-reference-sql-sp-tams-depot-getdtcauth'></a>
# Procedure: SP_TAMS_Depot_GetDTCAuth

The purpose of this stored procedure is to retrieve a list of depot authentication details for a given access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The access date for which the depot authentication details are required. |

### Logic Flow
1. The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then joins multiple tables, including TAMS_TAR, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Remark, and TAMS_WFStatus, on various conditions based on the provided access date.
3. The procedure filters the results to include only rows where the AccessDate matches the specified @accessDate parameter.
4. Finally, it orders the results by DepotAuthStatusId in ascending order.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Remark, and TAMS_WFStatus

---


<a id='database-reference-sql-sp-tams-depot-getdtcauthendorser'></a>
# Procedure: SP_TAMS_Depot_GetDTCAuthEndorser

The purpose of this stored procedure is to retrieve a list of DTCAuth Endorsers for a specific depot, filtered by access date and user role.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date range for which to filter the endorser data. |
| @lanid | nvarchar(50) | The login ID of the user to retrieve endorser data for. |

### Logic Flow
1. The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then declares a variable `@workflowid` and selects its value from the TAMS_Workflow table, where WorkflowType is 'OCCAuth' and TrackType is 'Depot'.
3. Next, it selects data from the TAMS_Endorser table, joining it with the TAMS_WFStatus table on the WFStatusId column.
4. The procedure filters the endorser data based on the `@accessDate` parameter, selecting only rows where EffectiveDate is greater than or equal to and ExpiryDate is less than or equal to the specified date range.
5. It also filters the data by user role, selecting only rows where the RoleID matches the value in the TAMS_OCC_Duty_Roster table for the specified `@lanid` parameter.
6. The procedure returns a list of DTCAuth Endorsers, including their WorkflowId, Title, RoleId, and Access status.

### Data Interactions
* **Reads:** TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_OCC_Duty_Roster, TAMS_User

---


<a id='database-reference-sql-sp-tams-depot-getdtcauthpowerzone'></a>
# Procedure: SP_TAMS_Depot_GetDTCAuthPowerzone

The purpose of this stored procedure is to retrieve a list of depot authentication power zones, filtered by access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date for which to filter the results |

### Logic Flow
1. The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then selects all columns from a subquery that filters data from several tables based on the provided access date and active status in the TAMS_Power_Sector table.
3. The subquery joins multiple tables, including TAMS_Depot_Auth, TAMS_Depot_Auth_Powerzone, TAMS_Power_Sector, TAMS_WFStatus, and TAMS_User, to retrieve various authentication power zone details.
4. The results are ordered by AuthID and ID in ascending order.

### Data Interactions
* **Reads:** TAMS_Depot_Auth, TAMS_Depot_Auth_Powerzone, TAMS_Power_Sector, TAMS_WFStatus, TAMS_User

---


<a id='database-reference-sql-sp-tams-depot-getdtcauthspks'></a>
# Procedure: SP_TAMS_Depot_GetDTCAuthSPKS

### Purpose
This stored procedure retrieves data from various tables to provide a comprehensive view of DTCAuth SPK SID information, filtered by access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @accessDate | Date | The date for which to retrieve the data |

### Logic Flow
1. The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then selects data from several tables: TAMS_Depot_Auth, TAMS_Depot_DTCAuth_SPKS, Z (TAMS_WFStatus), ProtectOffActionBy (TAMS_User), and ProtectOnActionBy (TAMS_User).
3. The procedure joins these tables based on their respective IDs and filters the results to only include data where the AccessDate matches the specified @accessDate parameter.
4. Finally, it returns the selected data, including AuthID, SPKSID, protect-related fields, StatusID, ProtectOffActionBy and ProtectOnActionBy names, and workflow ID.

### Data Interactions
* **Reads:** TAMS_Depot_Auth, TAMS_Depot_DTCAuth_SPKS, TAMS_WFStatus, TAMS_User (ProtectOffActionBy and ProtectOnActionBy)

---


<a id='database-reference-sql-sp-tams-depot-getdtcroster'></a>
# Procedure: SP_TAMS_Depot_GetDTCRoster

### Purpose
This stored procedure retrieves a roster of depot personnel for a specific date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @date | Date | The date for which to retrieve the roster. |

### Logic Flow
The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements. It then selects distinct RosterCode values from TAMS_OCC_Duty_Roster where TrackType is 'depot'. This step retrieves a list of unique depot personnel codes.

Next, it performs a LEFT OUTER JOIN with the same table but filtered by OperationDate and TrackType='depot' to match the @date parameter. This step ensures that only roster codes for the specified date are included in the results.

The procedure then performs another LEFT OUTER JOIN with TAMS_User on DutyStaffId to retrieve the names and login IDs of the personnel associated with each roster code.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_User

---


<a id='database-reference-sql-sp-tams-depot-getparameters'></a>
# Procedure: SP_TAMS_Depot_GetParameters

### Purpose
This stored procedure retrieves specific parameters from the TAMS_Parameters table based on a date range and parameter value.

### Parameters
| Name | Type | Purpose |
| @EffectiveDate | datetime | The start of the date range to filter parameters. |
| @ExpiryDate | datetime | The end of the date range to filter parameters. |
| @ParamValue2 | nvarchar(50) | The specific parameter value to filter by. |

### Logic Flow
1. The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then selects distinct values from the TAMS_Parameters table where the EffectiveDate is between the specified date range and ParaValue2 equals 'Depot'.
3. The selected parameters are returned based on these conditions.

### Data Interactions
* **Reads:** TAMS_Parameters
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-depot-getuseraccess'></a>
# Procedure: SP_TAMS_Depot_GetUserAccess

### Purpose
This stored procedure retrieves access information for a specified user at a depot.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @username | nvarchar(50) | The username to check for access. |

### Logic Flow
1. The procedure checks if the provided username exists in the TAMS_User table.
2. If the user exists, it sets the output parameter @res to 1, indicating that the user has access.
3. If the user does not exist, it sets the output parameter @res to 0, indicating that the user does not have access.

### Data Interactions
* **Reads:** TAMS_User table

---


<a id='database-reference-sql-sp-tams-depot-getwfstatus'></a>
# Procedure: SP_TAMS_Depot_GetWFStatus

### Purpose
This stored procedure retrieves the workflow status for a specific type of work order ('DTCAuth') from the TAMS_WFStatus table.

### Parameters
| Name | Type | Purpose |
| @ID | int | The ID of the work order to retrieve the workflow status for |

### Logic Flow
1. The procedure sets NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then selects the ID and WFStatusId columns from the TAMS_WFStatus table where the WFType is 'DTCAuth'.

### Data Interactions
* **Reads:** TAMS_WFStatus

---


<a id='database-reference-sql-sp-tams-depot-savedtcauthcomments'></a>
# Procedure: SP_TAMS_Depot_SaveDTCAuthComments

### Purpose
This stored procedure saves comments for a given authentication ID in the TAMS Depot Authorization module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @str | TAMS_DTC_AUTH_COMMENTS | A table variable containing the comments to be saved. |

### Logic Flow
1. The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements.
2. It then checks if a transaction is already in progress and sets an internal transaction flag accordingly.
3. If no transaction is active, it begins a new transaction.
4. The procedure then opens a cursor on the @str table variable, which contains the comments to be saved.
5. It fetches each row from the cursor and processes it:
	* For each comment, it checks if a remark ID already exists in the TAMS_Depot_Auth table for the corresponding authentication ID.
	* If a remark ID exists, it updates the remark in the TAMS_Depot_Auth_Remark table with the new comment.
	* If no remark ID exists, it inserts a new record into the TAMS_Depot_Auth_Remark table with the comment and sets the remark ID for the corresponding authentication ID in the TAMS_Depot_Auth table.
6. After processing all comments, the procedure closes the cursor and deallocates its resources.
7. If any errors occur during the process, it rolls back the transaction and sets a success flag to 0.
8. Otherwise, it commits the transaction, sets the success flag to 1, and returns.

### Data Interactions
* **Reads:** TAMS_DTC_AUTH_COMMENTS (table variable)
* **Writes:** TAMS_Depot_Auth_Remark (table), TAMS_Depot_Auth (table)

---


<a id='database-reference-sql-sp-test'></a>
# Procedure: SP_Test

### Purpose
This stored procedure performs a quality control check on a specific National Registration Identity Card (NRIC) number, verifying its validity and updating its status accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | NRIC Number |

### Logic Flow
1. The procedure starts by setting up temporary tables and variables to store the results of the quality control check.
2. It then calls another stored procedure, `sp_TAMS_TOA_QTS_Chk`, with specific parameters to perform the quality control check on the provided NRIC number.
3. If the result is invalid, the procedure truncates the temporary table, updates the status, and calls the same stored procedure again with different parameters to recheck the validity of the NRIC number.
4. The procedure continues this process until it determines whether the NRIC number is valid or not.
5. Finally, it drops the temporary table and prints the final result.

### Data Interactions
* **Reads:** #tmpnric table (temporary table created during the procedure)
* **Writes:** #tmpnric table (temporary table), as well as other tables involved in the quality control check process

---


<a id='database-reference-sql-getuserinformationbyid'></a>
# Procedure: getUserInformationByID

### Purpose
This stored procedure retrieves user information, including roles, for a specified user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The unique identifier of the user to retrieve information for. |

### Logic Flow
1. Check if a user with the provided UserID exists in the TAMS_User table.
2. If the user exists, perform a join operation on the TAMS_User_Role and TAMS_Role tables to retrieve the user's roles.
3. Filter the results to only include the user with the specified UserID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Role

---


<a id='database-reference-sql-sp-generate-ref-num'></a>
# Procedure: sp_Generate_Ref_Num

### Purpose
This stored procedure generates a unique reference number based on the provided form type, line, track type, and year.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @FormType	| NVARCHAR(20) | The type of form being generated. |
| @Line	| NVARCHAR(20) | The line number associated with the form. |
| @TrackType	| NVARCHAR(50) | The track type for the form. |
| @RefNum	| NVARCHAR(20) | Output parameter to store the generated reference number. |
| @Message	| NVARCHAR(500) | Output parameter to store any error message. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag and checking if a transaction is already in progress.
2. If no transaction is present, it sets the internal transaction flag and begins a new transaction.
3. It then checks if a record exists in the TAMS_RefSerialNumber table for the given form type, line, track type, and year. If no record exists, it inserts a new record with the current date and maximum number value.
4. If a record does exist, it retrieves the current maximum number value from the record and increments it by 1 to generate the next unique reference number.
5. The procedure then updates the TAMS_RefSerialNumber table with the new maximum number value.
6. Depending on the track type, it appends 'D' to the line number if it's a Depot track type.
7. Finally, it generates the reference number by concatenating the updated line number, form type, year, and maximum number value.

### Data Interactions
* Reads: TAMS_RefSerialNumber table
* Writes: TAMS_RefSerialNumber table

---


<a id='database-reference-sql-sp-generate-ref-num-toa'></a>
# Procedure: sp_Generate_Ref_Num_TOA

### Purpose
This stored procedure generates a reference number based on the provided parameters and updates the TAMS_RefSerialNumber table accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @FormType | NVARCHAR(20) | The type of form being generated (e.g. TOA, DTL). |
| @Line | NVARCHAR(20) | The line number associated with the form. |
| @TARID | Int | The ID of the TAR record to retrieve access date from. |
| @OperationDate | NVARCHAR(20) | The operation date for the form. |
| @TrackType | NVARCHAR(50) | The track type (e.g. Depot, NEL). |
| @RefNum | NVARCHAR(20) | Output parameter to store the generated reference number. |
| @Message | NVARCHAR(500) | Output parameter to store any error messages. |

### Logic Flow
1. The procedure checks if a transaction is already active and sets an internal transaction flag accordingly.
2. It retrieves the access date from the TAMS_TAR table based on the provided TARID.
3. If the form type is TOA, it checks if a record exists in the TAMS_RefSerialNumber table with the same line number, track type, year, operation date, and form type. If no record exists, it inserts a new record with the current maximum number value incremented by 1.
4. If a record already exists, it updates the MaxNum field of that record to increment its value by 1.
5. It generates the reference number based on the line number, form type, access date, and current time.
6. If an error occurs during the generation process, it sets the @Message output parameter with an error message.

### Data Interactions
* Reads: TAMS_TAR table to retrieve access date for TARID
* Writes: TAMS_RefSerialNumber table to insert or update records

---


<a id='database-reference-sql-sp-get-qrpoints'></a>
# Procedure: sp_Get_QRPoints

The purpose of this stored procedure is to retrieve a list of QR code points from the TAMS_TOA_QRCode table, ordered by line number, QR code type, and station.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | Not specified |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_TOA_QRCode table.
2. It orders the results by line number, QR code type, and station.

### Data Interactions
* **Reads:** [dbo].[TAMS_TOA_QRCode]

---


<a id='database-reference-sql-sp-get-typeofworkbyline'></a>
# Procedure: sp_Get_TypeOfWorkByLine

### Purpose
This stored procedure retrieves data from the TAMS_Type_Of_Work table based on a specified line and track type, filtering for active records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter by. |
| @TrackType | nvarchar(50) | The track type to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Type_Of_Work table.
2. It filters the results based on the provided @Line and @TrackType parameters, ensuring only active records are returned.
3. The filtered data is then ordered by the [Order] column in ascending order.

### Data Interactions
* **Reads:** TAMS_Type_Of_Work

---


<a id='database-reference-sql-sp-tams-applicant-list-child-onload'></a>
# Procedure: sp_TAMS_Applicant_List_Child_OnLoad

### Purpose
This stored procedure generates a list of applicants for a specific sector, filtered by access date and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the sector by. |
| @TrackType | NVARCHAR(50) | The track type to filter the applicants by. |
| @ToAccessDate | NVARCHAR(20) | The start date for access filtering. |
| @FromAccessDate | NVARCHAR(20) | The end date for access filtering. |
| @TARType | NVARCHAR(20) | The TAR type to filter the applicants by. |
| @SectorID | INT | The ID of the sector to retrieve applicants for. |

### Logic Flow
1. The procedure starts by setting a current date variable.
2. It creates a temporary table #TmpAppList to store the filtered applicant data.
3. The procedure truncates the existing data in #TmpAppList and inserts new data from TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, and TAMS_Sector tables based on the provided parameters.
4. It filters the applicants by sector ID and access date range.
5. The procedure groups the filtered data by TARID and returns a list of applicant details.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, TAMS_Sector tables.
* **Writes:** #TmpAppList table.

---


<a id='database-reference-sql-sp-tams-applicant-list-child-onload-20220303'></a>
# Procedure: sp_TAMS_Applicant_List_Child_OnLoad_20220303

### Purpose
This stored procedure generates a list of applicants for a specific sector, based on access dates and TAR type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @ToAccessDate | NVARCHAR(20) | The end date for access. |
| @FromAccessDate | NVARCHAR(20) | The start date for access. |
| @TARType | NVARCHAR(20) | The TAR type to filter by. |
| @SectorID | INT | The sector ID to filter by. |

### Logic Flow
1. The procedure starts by setting the current date and truncating two temporary tables: #TmpSector and #TmpAppList.
2. It then inserts data into #TmpSector, which contains information about sectors, including their order and direction.
3. Next, it inserts data into #TmpAppList, which contains information about applicants, including their TAR ID, access date, and sector ID.
4. The procedure then selects data from #TmpAppList where the sector ID matches the input @SectorID, and orders the results by TAR ID.
5. Finally, it drops the temporary tables.

### Data Interactions
* Reads: TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus
* Writes: None

---


<a id='database-reference-sql-sp-tams-applicant-list-child-onload-hnin'></a>
# Procedure: sp_TAMS_Applicant_List_Child_OnLoad_Hnin

### Purpose
This stored procedure generates a list of applicant records for a specific sector, filtered by access date and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the sector records. |
| @TrackType | NVARCHAR(50) | The track type to filter the applicant records. |
| @ToAccessDate | NVARCHAR(20) | The start date for access filtering. |
| @FromAccessDate | NVARCHAR(20) | The end date for access filtering. |
| @TARType | NVARCHAR(20) | The TAR type to filter the applicant records. |
| @SectorID | INT | The ID of the sector to retrieve the applicant records for. |

### Logic Flow
1. The procedure starts by setting a current date variable.
2. It creates a temporary table #TmpAppList to store the filtered applicant records.
3. The procedure truncates the existing data in #TmpAppList and inserts new data based on the following conditions:
	* The sector ID matches the specified @SectorID.
	* The access date falls within the range defined by @ToAccessDate and @FromAccessDate.
	* The track type matches the specified @TARType or is empty (default).
4. It selects the required columns from #TmpAppList and groups them by TARID, TARNo, TARType, AccessDate, AccessType, Company, WFStatus, and ColorCode.
5. The procedure sorts the results in ascending order by TARID.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, TAMS_Sector
* Writes: #TmpAppList

---


<a id='database-reference-sql-sp-tams-applicant-list-child-onload-20220303-m'></a>
# Procedure: sp_TAMS_Applicant_List_Child_OnLoad_20220303_M

### Purpose
This stored procedure generates a list of applicant records for a specific sector, filtered by access date and TAR type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the sector records. |
| @ToAccessDate | NVARCHAR(20) | The end of the access date range (inclusive). |
| @FromAccessDate | NVARCHAR(20) | The start of the access date range (inclusive). |
| @TARType | NVARCHAR(20) | The TAR type to filter the applicant records. |
| @SectorID | INT | The ID of the sector for which to retrieve the applicant records. |

### Logic Flow
1. The procedure starts by declaring a variable `@CurrDate` with the current date and time.
2. It creates two temporary tables, `#TmpSector` and `#TmpAppList`, to store the filtered sector and applicant data, respectively.
3. The procedure truncates both temporary tables before inserting new data.
4. For the `#TmpSector` table, it selects rows from `TAMS_Sector` where the line number matches the input parameter `@Line`, the record is active, and the access date falls within the specified range. It also orders the results by sector order.
5. For the `#TmpAppList` table, it joins multiple tables (`TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_WFStatus`, and `TAMS_Sector`) to filter the applicant records based on the input parameters. The join conditions include matching the TAR ID with the sector ID, accessing the correct record within the specified access date range, and filtering by TAR type.
6. After populating both temporary tables, the procedure selects the relevant columns from `#TmpAppList` where the sector ID matches the input parameter `@SectorID`. It groups the results by TAR ID and orders them in ascending order.
7. Finally, the procedure drops both temporary tables to clean up.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, TAMS_Sector
* **Writes:** #TmpSector, #TmpAppList

---


<a id='database-reference-sql-sp-tams-applicant-list-master-onload'></a>
# Procedure: sp_TAMS_Applicant_List_Master_OnLoad

### Purpose
This stored procedure generates a list of applicants for a specific sector, filtered by track type, access dates, and TAR type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter the sector by. |
| @TrackType | NVARCHAR(50) | The track type to filter the sector by. |
| @ToAccessDate | NVARCHAR(20) | The start date of access for filtering applicants. |
| @FromAccessDate | NVARCHAR(20) | The end date of access for filtering applicants. |
| @TARType | NVARCHAR(20) | The TAR type to filter the sector by. |

### Logic Flow
1. The procedure starts by setting the current date and truncating any temporary tables.
2. It then inserts data into a temporary table (#TmpSector) from TAMS_Sector, filtering by the specified line number, track type, and access dates.
3. The procedure then selects data from #TmpSector, grouping by sector order and direction (BB or NB), and ordering by sector order.
4. Finally, it drops the temporary tables.

### Data Interactions
* Reads: TAMS_Sector table
* Writes: #TmpSector table

---


<a id='database-reference-sql-sp-tams-applicant-list-onload'></a>
# Procedure: sp_TAMS_Applicant_List_OnLoad

### Purpose
This stored procedure retrieves a list of applicants for a specific line, sector, and access date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to retrieve applicants for. |

### Logic Flow
1. The procedure starts by determining the current date.
2. It then truncates two temporary tables, #TmpSector and #TmpAppList, which will be used to store sector data and applicant information, respectively.
3. The procedure inserts data into #TmpSector from TAMS_Sector table based on the specified line number, track type, and access date range.
4. Next, it inserts data into #TmpAppList from TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, and TAMS_Sector tables based on the same criteria as #TmpSector.
5. The procedure then selects applicant information from #TmpAppList and joins it with #TmpSector to retrieve sector data for each applicant.
6. Finally, the procedure drops the temporary tables.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, and TAMS_Sector tables.
* **Writes:** #TmpSector and #TmpAppList tables.

---


<a id='database-reference-sql-sp-tams-approval-add-bufferzone'></a>
# Procedure: sp_TAMS_Approval_Add_BufferZone

### Purpose
This stored procedure adds a new buffer zone to a TAMS TAR record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS TAR record. |
| @SectorID | BIGINT | The ID of the sector to be added as a buffer zone. |

### Logic Flow
1. The procedure checks if a transaction has already been started and sets an internal flag accordingly.
2. It then checks if a sector with the specified ID already exists in the TAMS_TAR_Sector table for the given TARID. If not, it proceeds to add the sector as a buffer zone.
3. To determine the colour code for the buffer zone, it queries the TAMS_Type_Of_Work table based on the line from the TAMS_TAR record with the matching ID.
4. It then inserts a new row into the TAMS_TAR_Sector table with the specified TARID, sector ID, and colour code.

### Data Interactions
* **Reads:** [dbo].[TAMS_TAR], [dbo].[TAMS_TAR_Sector], [dbo].[TAMS_Type_Of_Work], [dbo].[TAMS_Sector]
* **Writes:** [dbo].[TAMS_TAR_Sector]

---


<a id='database-reference-sql-sp-tams-approval-add-tvfstation'></a>
# Procedure: sp_TAMS_Approval_Add_TVFStation

The procedure is used to add a new TVF station for a given TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The TAR ID associated with the TVF station. |
| @StationID	| BIGINT | The ID of the TVF station to be added. |
| @Direction	| NVARCHAR(20) | The direction of the TVF station. |
| @Message	| NVARCHAR(500) | An output parameter that stores an error message if any. |

### Logic Flow
1. The procedure starts by setting a flag `@IntrnlTrans` to 0, indicating that no internal transaction is currently in progress.
2. It then checks if there are any active transactions in the current session. If not, it sets `@IntrnalTrans` to 1 and begins a new transaction.
3. The procedure then checks if a TVF station with the given TAR ID, Station ID, and direction already exists in the TAMS_TAR_TVF table. If no such record is found, it inserts a new record into this table.
4. After inserting or updating the record, the procedure checks for any errors that may have occurred during this process. If an error occurs, it sets the `@Message` output parameter to an error message and exits the transaction.
5. If no errors occur, the procedure commits the transaction and returns the `@Message` output parameter.

### Data Interactions
* **Reads:** [dbo].[TAMS_TAR_TVF]
* **Writes:** [dbo].[TAMS_TAR_TVF]

---


<a id='database-reference-sql-sp-tams-approval-del-bufferzone'></a>
# Procedure: sp_TAMS_Approval_Del_BufferZone

### Purpose
This stored procedure deletes a buffer zone from the TAMS_TAR_Sector table based on the provided TARID and SectorID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR to delete the sector from. |
| @SectorID | BIGINT | The ID of the sector to delete. |
| @Message | NVARCHAR(500) | An output parameter that stores an error message if any. |

### Logic Flow
1. The procedure starts by setting a flag to indicate whether a transaction has been started.
2. It then checks if a transaction is already in progress and sets the flag accordingly.
3. If no transaction is in progress, it begins a new transaction.
4. The procedure then deletes the specified sector from the TAMS_TAR_Sector table based on the provided TARID and SectorID.
5. After deletion, it checks for any errors that may have occurred during this process.
6. If an error occurs, it sets the @Message parameter with an error message and skips to the TRAP_ERROR label.
7. If no errors occur, it commits the transaction if one was started and returns the @Message parameter.
8. If an error occurred, it rolls back the transaction and also returns the @Message parameter.

### Data Interactions
* **Reads:** TAMS_TAR_Sector table
* **Writes:** TAMS_TAR_Sector table

---


<a id='database-reference-sql-sp-tams-approval-del-tvfstation'></a>
# Procedure: sp_TAMS_Approval_Del_TVFStation

The purpose of this stored procedure is to delete a TVF station from the TAMS_TAR table based on the provided TARID and TVFID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR record to be deleted. |
| @TVFID | BIGINT | The ID of the TVF station to be deleted. |
| @Message | NVARCHAR(500) | An output parameter that stores any error message generated during the procedure execution. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag (@IntrnlTrans) to 0.
2. It then checks if there is an active transaction. If not, it sets @IntrnlTrans to 1 and begins a new transaction.
3. The procedure then deletes the specified TVF station from the TAMS_TAR table based on the provided TARID and TVFID.
4. After deletion, it checks for any errors that may have occurred during the process. If an error is found, it sets @Message to an error message and jumps to the TRAP_ERROR label.
5. If no errors are found, the procedure commits the transaction if one was started (@IntrnlTrans = 1) and returns the value of @Message.
6. If an error occurred, the procedure rolls back the transaction if one was started (@IntrnlTrans = 1) and also returns the value of @Message.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** TAMS_TAR table

---


<a id='database-reference-sql-sp-tams-approval-endorse'></a>
# Procedure: sp_TAMS_Approval_Endorse

### Purpose
This stored procedure is used to endorse a TAR (Technical Approval Request) and update its status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR being endorsed. |
| @TARWFID | INTEGER | The current workflow ID associated with the TAR. |
| @EID | INTEGER | The ID of the endorser who is endorsing the TAR. |
| @ELevel | INTEGER | The level of the endorser who is endorsing the TAR. |
| @Remarks | NVARCHAR(1000) = NULL | Remarks for the TAR (optional). |
| @TVFRunMode | NVARCHAR(50) = NULL | New TVF run mode value (optional). |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF run mode or not (optional). |
| @UserLI | NVARCHAR(100) = NULL | User login ID. |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message for the procedure. |

### Logic Flow
1. The procedure checks if a transaction is already in progress and sets an internal transaction flag accordingly.
2. It retrieves the user's ID and name from the TAMS_User table based on the provided login ID.
3. It checks if the TAR has already been approved by another user with the same workflow ID, and if so, it sets an error message and exits the procedure.
4. If not, it updates the TAR's workflow status to 'Approved', sets the action by and action on fields, and inserts a new record into the TAMS_TAR_Workflow table.
5. It then checks the next level of endorser for the TAR and performs actions based on the TAR type (Urgent or Not Urgent).
6. If the TAR is urgent, it sends an email to the current endorser and any additional recipients specified in the TAMS_Parameters table.
7. After completing all steps, it logs the action in the TAMS_Action_Log table.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Endorser, TAMS Paramaters
* Writes: TAMS_TAR, TAMS_TAR_Workflow

---


<a id='database-reference-sql-sp-tams-approval-endorse20250120'></a>
# Procedure: sp_TAMS_Approval_Endorse20250120

### Purpose
This stored procedure is used to approve and endorse a TAR (Technical Approval Request) form, which involves updating the workflow status, assigning an endorser, and sending notifications to relevant parties.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current WF ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) = NULL | Remarks (Mandatory for Reject, Optional for Approved/Endorse) |
| @TVFRunMode | NVARCHAR(50) = NULL | New Column to be confirmed with Adeline |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to Update TVF Run Mode or Not |
| @UserLI | NVARCHAR(100) = NULL | User Login ID |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message |

### Logic Flow
1. The procedure checks if the TAR has already been approved by the current user, and if so, it sets an error message and exits.
2. It updates the workflow status to 'Approved' and assigns the current user as the action by.
3. If the TVF Run Mode update indicator is set to 1, it updates the TAR's TVF mode.
4. The procedure retrieves the next endorser for the current level and checks if there are any pending approvals for that level. If not, it inserts a new workflow record with the next endorser assigned.
5. It updates the TAR status ID based on the line number (NEL or LRT).
6. If the TAR type is 'Urgent', it sends an urgent email to the current user and the next endorser.
7. The procedure logs the approval action in the TAMS_Action_Log table.
8. If any errors occur during the process, it rolls back the transaction and returns an error message.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_Parameters, TAMS_Workflow, TAMS_Role, TAMS_Action_Log
* **Writes:** TAMS_TAR_Workflow, TAMS_TAR

---


<a id='database-reference-sql-sp-tams-approval-endorse-20220930'></a>
# Procedure: sp_TAMS_Approval_Endorse_20220930

### Purpose
This stored procedure performs the approval and endorsement process for a TAR (Trade Agreement) form, updating its status to "Approved" and assigning an endorser.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR form being approved. |
| @TARWFID | INTEGER | The current workflow ID for the TAR form. |
| @EID | INTEGER | The ID of the endorser assigning approval. |
| @ELevel | INTEGER | The level of the endorser (e.g., 1, 2, etc.). |
| @Remarks | NVARCHAR(1000) = NULL | Remarks for the approved TAR form (mandatory for reject, optional for approve or endorse). |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline. |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF Run Mode or Not. |
| @UserLI | NVARCHAR(50) = NULL | User login ID. |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message for the procedure. |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets an internal transaction flag to 1.
2. It updates the TAR form's status to "Approved" and assigns the current endorser as the action by and on dates.
3. If the TVF Run Mode update indicator is set to 1, it updates the TAR form's TVF mode.
4. The procedure then selects the next level endorser based on the current endorser's level.
5. If there is no next level endorser (i.e., this is the last level), it updates the TAR form's status and sends an email to the NEL approved role if applicable.
6. Otherwise, it inserts a new workflow record for the next level endorser and updates the TAR form's status.
7. It then selects all emails where the role ID matches the next level endorser and sends an email to these roles using the sp_TAMS_Email_Apply_Late_TAR procedure.
8. The procedure logs the approval action in the TAMS_Action_Log table.
9. If any errors occur during execution, it rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_Role, TAMS_Workflow
* Writes: TAMS_TAR, TAMS_TAR_Workflow

---


<a id='database-reference-sql-sp-tams-approval-endorse-20230410'></a>
# Procedure: sp_TAMS_Approval_Endorse_20230410

### Purpose
This stored procedure performs the approval and endorsement process for a TAR (Task Assignment Request) form. It updates the TAR status, assigns the next level of endorser, and sends notifications to relevant parties.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR form being approved. |
| @TARWFID | INTEGER | The current workflow ID associated with the TAR form. |
| @EID | INTEGER | The ID of the current endorser. |
| @ELevel | INTEGER | The level of the current endorser. |
| @Remarks | NVARCHAR(1000) = NULL | Remarks for the approval process (mandatory for reject, optional for approved or endorse). |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline. |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF run mode or not. |
| @UserLI | NVARCHAR(100) = NULL | User login ID. |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message for the procedure. |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If so, it sets an internal flag to 1 and begins a new transaction.
2. It updates the TAR form status to 'Approved' and assigns the current endorser's ID as the action by and on dates.
3. If the TVF run mode update indicator is set to 1, it updates the TAR form with the new TVF run mode value.
4. The procedure retrieves the next level of endorser from the TAMS_Endorser table based on the current endorser's level.
5. If there is no next level of endorser, it updates the TAR form status to a specific value (9 for NEL approved or 8 for DTL or LRT).
6. It sends an email notification to relevant parties (e.g., the next level of endorser) if the TAR form type is 'Urgent'.
7. The procedure logs the approval action in the TAMS_Action_Log table.
8. If any errors occur during the process, it rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_Role
* Writes: TAMS_TAR, TAMS_Action_Log

---


<a id='database-reference-sql-sp-tams-approval-get-add-bufferzone'></a>
# Procedure: sp_TAMS_Approval_Get_Add_BufferZone

The purpose of this stored procedure is to retrieve additional buffer zone information for a given TARID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TARID for which to retrieve the buffer zone information |

### Logic Flow
1. The procedure starts by selecting data from two tables: TAMS_Sector and TAMS_TAR_Sector.
2. It filters the results to only include rows where the sector ID matches the TARID's associated sector ID, and the IsBuffer flag is set to 1.
3. The results are ordered by the sector ID.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector

---


<a id='database-reference-sql-sp-tams-approval-get-add-tvfstation'></a>
# Procedure: sp_TAMS_Approval_Get_Add_TVFStation

### Purpose
This stored procedure retrieves information about TVF stations associated with a given TAR ID, including station names and directions, as well as the TVF run mode.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to retrieve TVF station information for. |

### Logic Flow
1. The procedure starts by selecting data from two tables: TAMS_Station and TAMS_TAR_TVF.
2. It joins these tables based on the ID of the TVF station and the TAR ID provided as a parameter.
3. The selected data is ordered by the ID of the TVF station.
4. Next, it retrieves the TVF run mode from the TAMS_TAR table where the ID matches the TAR ID provided as a parameter.

### Data Interactions
* **Reads:** TAMS_Station, TAMS_TAR_TVF, and TAMS_TAR tables.
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-approval-onload'></a>
# Procedure: sp_TAMS_Approval_OnLoad

### Purpose
This stored procedure performs a series of checks and operations on a TAMS TAR record, including retrieving relevant data from other tables, performing calculations, and updating records as necessary.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS TAR record to process. |

### Logic Flow
The procedure follows these steps:

1. Retrieve relevant data from the TAMS_TAR table based on the provided @TARID.
2. Calculate and retrieve additional data from other tables, including TAMS_TAR_Sector, TAMS_Access_Requirement, TAMS_Possession, and TAMS_Type_Of_Work.
3. Perform calculations to determine if there are any sector conflicts or exceptions that need to be addressed.
4. Update records in the #TmpExc table based on the results of the calculations.
5. Retrieve additional data from the #TmpExc table to identify any sector conflicts or exceptions that require attention.
6. If necessary, update records in the TAMS_TAR_Sector table to resolve sector conflicts.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_Sector, TAMS_Access_Requirement, TAMS_Possession, TAMS_Type_Of_Work, #TmpExc
* **Writes:** #TmpExc

---


<a id='database-reference-sql-sp-tams-approval-onload-bak20230531'></a>
# Procedure: sp_TAMS_Approval_OnLoad_bak20230531

### Purpose
This stored procedure performs a series of checks and operations on a TAMS TAR record, including validation, data extraction, and approval processes.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS TAR record to process. |

### Logic Flow
The procedure follows these steps:

1. Retrieves relevant data from the TAMS_TAR table based on the provided TARID.
2. Extracts sector information and checks for sector conflicts.
3. Iterates through a list of sectors, checking if each sector is in conflict with another sector.
4. For each sector, it checks if there are any existing exceptions or conflicts that need to be addressed.
5. If a conflict is found, the procedure inserts an exception record into the #TmpExc table.
6. After processing all sectors, the procedure retrieves additional data from related tables (e.g., TAMS_TAR_Attachment, TAMS_Possession).
7. It then iterates through a list of workflow records associated with the TARID and checks for pending or approved workflows.
8. For each workflow record, it checks if there are any exceptions or conflicts that need to be addressed.
9. If an exception is found, the procedure inserts an exception record into the #TmpExc table.
10. Finally, the procedure retrieves a list of access requirements for the TARID and displays them.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR_Attachment, TAMS_Possession, TAMS_Type_Of_Work, TAMS_Access_Requirement, TAMS_Endorser, TAMS_User.
* **Writes:** #TmpExc, #TmpExcSector.

---


<a id='database-reference-sql-sp-tams-approval-proceed-to-app'></a>
# Procedure: sp_TAMS_Approval_Proceed_To_App

### Purpose
This stored procedure performs the approval process for a TAR (Technical Approval Request) and updates the TAR status accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current Workflow ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) | Remarks (Mandatory for Reject, Optional for Approved/Endorse) |
| @TVFRunMode | NVARCHAR(50) | New Column to be confirmed with Adeline (Optional) |
| @TVFRunModeUpdInd | NVARCHAR(5) | Indicator to Update TVF Run Mode or Not (Optional) |
| @UserLI | NVARCHAR(100) | User Login ID |
| @Message | NVARCHAR(500) | Output message |

### Logic Flow
1. The procedure checks if the TAR has already been approved by the current user. If yes, it sets an error message and exits.
2. It updates the TVF Run Mode column in the TAR table if specified.
3. It retrieves the current level endorser's details from the TAMS_Endorser table.
4. It creates two temporary tables (#TmpExc and #TmpExcSector) to store exceptions (sector conflicts) for each TAR.
5. It iterates through the exceptions and checks if there are any sector conflicts. If yes, it inserts the exception into the #TmpExcSector table.
6. It retrieves the next level endorser's details from the TAMS_Endorser table.
7. If the next level endorser is not found or has already been approved, it updates the TAR status to 'Approved' and sends an email notification if required.
8. If the next level endorser is found and has not been approved, it inserts a new record into the TAMS_TAR_Workflow table.
9. It checks for any urgent after notifications and sends an email notification if required.
10. Finally, it updates the TAR status to 'Approved' and logs the approval action.

### Data Interactions
* Reads: TAMS_User, TAMS_Endorser, TAMS_TAR, TAMS_TAR_Workflow, TAMS Paramaters
* Writes: TAMS_TAR, TAMS_TAR_Workflow

---


<a id='database-reference-sql-sp-tams-approval-proceed-to-app-20220930'></a>
# Procedure: sp_TAMS_Approval_Proceed_To_App_20220930

### Purpose
This stored procedure performs the approval process for a TAR (Technical Approval Request) form. It checks if the current endorser has approved or rejected the request, and updates the TAR status accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current WF ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) = NULL | Remarks (mandatory for reject, optional for approved or endorse) |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF Run Mode or Not |
| @UserLI | NVARCHAR(50) = NULL | User Login ID |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets the internal transaction flag to 1.
2. It then retrieves the current endorser's details from the TAMS_User table based on the provided User Login ID.
3. Next, it retrieves the TAR details from the TAMS_TAR table and updates the TAR Status ID if necessary.
4. The procedure then creates two temporary tables, #TmpExc and #TmpExcSector, to store the exception TARs (sector conflicts) for each sector.
5. It iterates through the sectors and checks if there are any exceptions. If so, it inserts them into the temporary tables.
6. After that, it retrieves the next level endorser's details from the TAMS_Endorser table based on the current endorser's ID and level.
7. If the next level endorser is not found, it updates the TAR status to 'Approved' or 'Rejected' based on the current endorser's decision.
8. The procedure then checks if there are any late TARs that need to be approved. If so, it sends an email notification to the relevant users and updates the TAR status accordingly.
9. Finally, it commits or rolls back the transaction depending on whether an error occurred during the execution of the procedure.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR, TAMS_Endorser, TAMS_TAR_Workflow, TAMS_Sector, TAMS_Role
* Writes: TAMS_TAR, TAMS_TAR_Workflow

---


<a id='database-reference-sql-sp-tams-approval-proceed-to-app-20231009'></a>
# Procedure: sp_TAMS_Approval_Proceed_To_App_20231009

### Purpose
This stored procedure performs the business task of proceeding with a TAR (Technical Approval Request) approval process. It checks for any exceptions, updates the TAR status, and sends notifications as required.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current WF ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) | Remarks (Mandatory for Reject, Optional for Approved/Endorse) |
| @TVFRunMode | NVARCHAR(50) | New Column to be confirmed with Adeline (Optional) |
| @TVFRunModeUpdInd | NVARCHAR(5) | Indicator to Update TVF Run Mode or Not (Optional) |
| @UserLI | NVARCHAR(100) | User Login ID |
| @Message | NVARCHAR(500) | Output message |

### Logic Flow
1. The procedure starts by checking if the transaction count is 0, indicating a new transaction.
2. It then checks for any exceptions in the TAR workflow and updates the TAR status accordingly.
3. If there are no exceptions, it proceeds with the approval process.
4. For each level of endorsement, it checks if the next level's endorser has been approved or not.
5. If the next level's endorser is not approved, it sends an email notification to the relevant stakeholders.
6. Once all levels have been checked and exceptions handled, it updates the TAR status to 'Approved' and inserts a new record into the TAMS_TAR_Workflow table.
7. Finally, it commits or rolls back the transaction based on whether any errors occurred during the procedure.

### Data Interactions
* Reads: TAMS_User, TAMS_Endorser, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Sector, TAMS_Role
* Writes: TAMS_TAR, TAMS_TAR_Workflow

---


<a id='database-reference-sql-sp-tams-approval-proceed-to-app-20240920'></a>
# Procedure: sp_TAMS_Approval_Proceed_To_App_20240920

### Purpose
This stored procedure performs the approval process for a TAR (Technical Approval Request) by checking if it has already been approved, updating the TAR status and workflow, and sending notifications to relevant parties.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current Workflow ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) = NULL | Remarks (mandatory for Reject, optional for Approved/Endorse) |
| @TVFRunMode | NVARCHAR(50) = NULL | New column to be confirmed with Adeline |
| @TVFRunModeUpdInd | NVARCHAR(5) = NULL | Indicator to update TVF Run Mode or Not |
| @UserLI | NVARCHAR(100) = NULL | User Login ID |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message |

### Logic Flow
1. The procedure checks if the TAR has already been approved by the current user, and if so, sets an error message.
2. It updates the TAR status to 'Approved' or 'Cancelled' based on the line value (@Line).
3. If @TVFRunModeUpdInd = 1, it updates the TVF mode in the TAMS_TAR table.
4. The procedure retrieves the current level endorser and checks if there are any sector conflicts (i.e., exceptions) that need to be addressed.
5. It creates two temporary tables (#TmpExc and #TmpExcSector) to store the exception TARs and their corresponding sector IDs.
6. The procedure iterates through the exception TARs, checking for sector conflicts and sending notifications to relevant parties.
7. If there are no sector conflicts, it updates the TAR status to 'Approved' and sends an email notification to the next level endorser.
8. If there are sector conflicts, it cancels the TAR and sends a notification to the current user.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_Sector, TAMS_Parameters
* Writes: TAMS_TAR, TAMS_TAR_Workflow

---


<a id='database-reference-sql-sp-tams-approval-reject'></a>
# Procedure: sp_TAMS_Approval_Reject

### Purpose
This stored procedure performs a rejection of a TAR (Task Assignment Record) form, updating its status and sending notifications to relevant parties.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current Workflow ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) = NULL | Remarks (mandatory for Reject, optional for Approved/Endorse) |
| @UserLI | NVARCHAR(100) = NULL | User Login ID |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets the internal transaction flag to 1 and begins a new transaction.
2. It updates the TAR form's status to 'Rejected' and records the rejection remarks.
3. It retrieves the endorser title and current level from the TAMS_Endorser table based on the provided Endorser ID and Level.
4. Depending on the TAR type, it determines whether to send an urgent email or not. If urgent, it sets the TAR status to 'Rejected' and sends a notification using the sp_TAMS_Email_Urgent_TAR procedure.
5. It logs the rejection action in the TAMS_Action_Log table.
6. If any errors occur during the process, it rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_User, TAMS_Endorser, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Action_Log, TAMS_Parameters
* Writes: TAMS_TAR, TAMS_TAR_Workflow

---


<a id='database-reference-sql-sp-tams-approval-reject-20220930'></a>
# Procedure: sp_TAMS_Approval_Reject_20220930

### Purpose
This stored procedure performs a rejection of a TAR (Task Assignment Request) form, updating its status and sending notifications to relevant parties.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | TAR ID |
| @TARWFID | INTEGER | Current WF ID |
| @EID | INTEGER | Current Endorser ID |
| @ELevel | INTEGER | Current Endorser Level |
| @Remarks | NVARCHAR(1000) = NULL | Remarks (Mandatory for Reject, Optional for Approved/Endorse) |
| @UserLI | NVARCHAR(50) = NULL | User Login ID |
| @Message | NVARCHAR(500) = NULL OUTPUT | Output message |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets the internal transaction flag to 1 and begins a new transaction.
2. It retrieves the user's details from TAMS_User based on the provided User Login ID.
3. The procedure updates the TAR form's status to 'Rejected' and sets the remark field with the provided remarks.
4. It selects the endorser title, TAR type, line, email, company, and access date from TAMS_TAR based on the TAR ID.
5. If the TAR type is 'Late', it sends a rejection email using sp_TAMS_Email_Late_TAR.
6. The procedure updates the TAR form's status to reflect the current level endorser title.
7. It checks if the workflow type is 'LateAfter' and involves power 1 with the current endorser level being 2. If true, it sends an email using sp_TAMS_Email_Late_TAR_OCC.
8. The procedure commits or rolls back the transaction based on whether any errors occurred during execution.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR, TAMS_Endorser, TAMS_Workflow, TAMS_Role, TAMS_User_Role
* Writes: TAMS_TAR (status and remark fields)

---


<a id='database-reference-sql-sp-tams-batch-deactivate-useraccount'></a>
# Procedure: sp_TAMS_Batch_DeActivate_UserAccount

### Purpose
This procedure deactivates a user account based on the number of days since their last login.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @DeAct | BIGINT | The number of days since the user's last login |

### Logic Flow
1. The procedure starts by declaring a variable `@DeAct` to store the number of days since the user's last login.
2. It then selects the value of `ParaValue1` from the `TAMS_Parameters` table where `ParaCode` is 'DeActivateAcct' and the current date falls within the range of `EffectiveDate` and `ExpiryDate`.
3. The selected value is assigned to the `@DeAct` variable.
4. The procedure then updates the `IsActive`, `UpdatedBy`, and `UpdatedOn` columns in the `TAMS_User` table for users who have had their account inactive for at least `@DeAct` days since their last login.

### Data Interactions
* **Reads:** TAMS_Parameters, TAMS_User
* **Writes:** TAMS_User

---


<a id='database-reference-sql-sp-tams-batch-housekeeping'></a>
# Procedure: sp_TAMS_Batch_HouseKeeping

### Purpose
This stored procedure performs a batch housekeeping operation on various TAMS tables, updating and deleting records as necessary.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | Inferred usage |

### Logic Flow
1. The procedure starts by declaring a variable `@DeAct` to store the value of a parameter.
2. It then selects the value of `ParaValue1` from the `TAMS_Parameters` table where `ParaCode` is 'DeActivateAcct' and the current date falls within the specified effective and expiry dates.
3. Based on this value, it updates or deletes records in various TAMS tables, including `TAMS_TAR_AccessReq`, `TAMS_TAR_Attachment`, `TAMS_TAR_Power_Sector`, `TAMS_TAR_Sector`, `TAMS_TAR_Station`, `TAMS_TAR_TVF`, and others.
4. The procedure also selects records from tables like `TAMS_Block_TARDate`, `TAMS_OCC_Auth`, `TAMS_OCC_Auth_Workflow`, `TAMS_OCC_Duty_Roster`, `TAMS_Possession`, `TAMS_Possession_Limit`, `TAMS_Possession_OtherProtection`, `TAMS_Possession_PowerSector`, and `TAMS_Possession_WorkingLimit`.
5. Additionally, it selects records from tables like `TAMS_TOA`, `TAMS_TOA_Parties`, `TAMS_TVF_Ack_Remark`, and `TAMS_TVF_Acknowledge`.

### Data Interactions
* **Reads:** 
	+ TAMS_Parameters
	+ TAMS_TAR_AccessReq
	+ TAMS_TAR_Attachment
	+ TAMS_TAR_Power_Sector
	+ TAMS_TAR_Sector
	+ TAMS_TAR_Station
	+ TAMS_TAR_TVF
	+ TAMS_Block_TARDate
	+ TAMS_OCC_Auth
	+ TAMS_OCC_Auth_Workflow
	+ TAMS_OCC_Duty_Roster
	+ TAMS_Possession
	+ TAMS_Possession_Limit
	+ TAMS_Possession_OtherProtection
	+ TAMS_Possession_PowerSector
	+ TAMS_Possession_WorkingLimit
	+ TAMS_TOA
	+ TAMS_TOA_Parties
	+ TAMS_TVF_Ack_Remark
	+ TAMS_TVF_Acknowledge
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-batch-inactive-resignedstaff'></a>
# Procedure: sp_TAMS_Batch_InActive_ResignedStaff

### Purpose
This stored procedure updates the status of active users to inactive and moves them to a separate table for inactive staff, based on their last login date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |

### Logic Flow
1. The procedure starts by updating the `IsActive` column in the `TAMS_User` table to 0 (inactive) for users who are currently active and have a login ID present in the `ResignedStaff` table.
2. It then inserts new records into the `TAMS_User_InActive` table, which includes all the columns from the original `TAMS_User` table, but with some differences (e.g., `ValidFrom`, `ValidTo`, `IsExternal`, etc.).
3. Finally, it deletes users from the `TAMS_User` table who have a login ID present in the `ResignedStaff` table.

### Data Interactions
* **Reads:** VMSDBSVR.ACRS.dbo.ResignedStaff
* **Writes:** TAMS_User, TAMS_User_InActive

---


<a id='database-reference-sql-sp-tams-batch-populate-calendar'></a>
# Procedure: sp_TAMS_Batch_Populate_Calendar

### Purpose
This stored procedure populates the TAMS_Calendar table with data from the TR_CALENDAR_REF table for a specified year.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Year | NVARCHAR(4) | The year to populate the calendar for. If not provided, it defaults to the current year. |
| @YrFlag | INT | A flag indicating whether to add a specific number of years to the default year. |

### Logic Flow
1. The procedure starts by setting up variables and checking if the input parameters are provided.
2. It truncates the TAMS_TR_CALENDAR_REF temporary table, which is used as a reference for the calendar data.
3. It selects all rows from the TR_CALENDAR_REF table, ordered by date, and inserts them into the TAMS_TR_CALENDAR_REF table.
4. It counts the number of days in the specified year that are already populated in the TAMS_Calendar table.
5. If there are existing calendar entries for the specified year, it deletes those entries.
6. It inserts new rows into the TAMS_Calendar table with data from the TAMS_TR_CALENDAR_REF table.

### Data Interactions
* **Reads:** TR_CALENDAR_REF, TAMS_Calendar
* **Writes:** TAMS_TR_CALENDAR_REF, TAMS_Calendar

---


<a id='database-reference-sql-sp-tams-block-date-delete'></a>
# Procedure: sp_TAMS_Block_Date_Delete

### Purpose
This stored procedure deletes a record from the TAMS_Block_TARDate table based on the provided BlockID and logs the deletion in the TAMS_Block_TARDate_Audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @BlockID | INTEGER | The ID of the block to be deleted. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag and beginning a new transaction if no existing one is found.
2. It then inserts a record into the TAMS_Block_TARDate_Audit table with the current date, 'D' (deletion), and all columns from the TAMS_Block_TARDate table where ID matches @BlockID.
3. Next, it deletes the record from the TAMS_Block_TARDate table where ID equals @BlockID.
4. If any error occurs during deletion, an error message is set in @Message and the procedure jumps to the TRAP_ERROR label.
5. After successful deletion or if an error occurred, the procedure checks the internal transaction flag. If it's 1 (meaning a new transaction was started), it commits the transaction and returns the value of @Message. If it's 0 (no new transaction), it rolls back the transaction and also returns the value of @Message.

### Data Interactions
* **Reads:** TAMS_Block_TARDate, TAMS_Block_TARDate_Audit
* **Writes:** TAMS_Block_TARDate

---


<a id='database-reference-sql-sp-tams-block-date-onload'></a>
# Procedure: sp_TAMS_Block_Date_OnLoad

### Purpose
This stored procedure retrieves data from the TAMS_Block_TARDate table based on specified parameters, filtering by line number, track type, and block date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		| NVARCHAR(20) | The line number to filter by. If NULL, all lines are included. |
| @TrackType  | NVARCHAR(50) | The track type to filter by. If NULL, all track types are included. |
| @BlockDate	| NVARCHAR(20) | The block date to filter by. If NULL, all dates are included. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Block_TARDate table.
2. It filters the results based on the provided parameters: line number (@Line), track type (@TrackType), and block date (@BlockDate).
3. The filter conditions use OR operators to include rows that match any of the specified values, or NULL if no value is provided.
4. The procedure orders the filtered results by the block date in descending order (newest dates first).

### Data Interactions
* **Reads:** TAMS_Block_TARDate table

---


<a id='database-reference-sql-sp-tams-block-date-save'></a>
# Procedure: sp_TAMS_Block_Date_Save

### Purpose
This stored procedure saves a new block date record to the TAMS_Block_TARDate table, ensuring that the block date is within a certain timeframe and not already existing.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line			| NVARCHAR(20) | The line number associated with the block. |
| @TrackType		| NVARCHAR(50) | The type of track being blocked. |
| @BlockDate		| NVARCHAR(20) | The date for which the block is being applied. |
| @BlockReason	| NVARCHAR(100) | The reason for the block. |
| @UserLI			| NVARCHAR(50) | The login ID of the user performing the action. |
| @Message		| NVARCHAR(500) | An output parameter containing a message indicating the result of the operation. |

### Logic Flow
1. The procedure first checks if a transaction has already been started, and if not, it sets an internal flag to indicate that a new transaction is beginning.
2. It then retrieves the user ID from the TAMS_User table based on the provided login ID.
3. The procedure calculates the week number for both the current date and the block date, taking into account leap years and month boundaries.
4. If the block date is within 5 weeks of the current date in the same year, it proceeds to check if a record already exists for this combination of line, track type, and block date.
5. If a record does not exist, the procedure inserts a new record into the TAMS_Block_TARDate table with the provided data.
6. It also inserts an audit record into the TAMS_Block_TARDate_Audit table to track changes made to this record.
7. Finally, if any errors occur during the insertion process, the procedure rolls back the transaction and returns an error message; otherwise, it commits the transaction and returns a success message.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Block_TARDate, TAMS_Block_TARDate_Audit
* **Writes:** TAMS_Block_TARDate

---


<a id='database-reference-sql-sp-tams-canceltarbytarid'></a>
# Procedure: sp_TAMS_CancelTarByTarID

The purpose of this stored procedure is to cancel a TAR (TARWFStatus) by updating its status and logging the action.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the TAR to be cancelled. |
| @UID | integer | The user ID who is cancelling the TAR. |

### Logic Flow

1. The procedure starts by declaring variables for the line, status ID, and name.
2. It then attempts to start a transaction and begins a new block of code within it.
3. Within this block, it selects the line from TAMS_TAR where the Id matches @TarId.
4. It then selects the status ID from TAMS_WFStatus where the line matches the one selected in step 3, and the WFType is 'TARWFStatus' and the WFStatus is 'Cancel'.
5. Next, it selects the name of the user who is cancelling the TAR from TAMS_User where the userid matches @UID.
6. The procedure then updates the TAR status ID in TAMS_TAR to match the one selected in step 4, where the Id is @TarId.
7. After updating the TAR status, it inserts a new log entry into TAMS_Action_Log with details of the cancellation action.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User
* **Writes:** TAMS_TAR, TAMS_Action_Log

---


<a id='database-reference-sql-sp-tams-check-userexist'></a>
# Procedure: sp_TAMS_Check_UserExist

### Purpose
This stored procedure checks if a user exists in the TAMS_User table based on either their LoginID or SAPNo.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @SapNo | NVARCHAR(100) | The SAP number of the user to check for existence. |
| @LoginID | NVARCHAR(200) | The login ID of the user to check for existence. |

### Logic Flow
The procedure first checks if both @LoginID and @SapNo are provided. If they are, it checks if a record exists in the TAMS_User table where LoginID matches @LoginID and SAPNo matches @SapNo. If this condition is met, it returns 1 (indicating existence). 

If only @LoginID is provided, it checks if a record exists in the TAMS_User table where LoginID matches @LoginID. If this condition is met, it returns 1.

If neither @LoginID nor @SapNo are provided, the procedure does not perform any checks and returns no result.

### Data Interactions
* **Reads:** TAMS_User

---


<a id='database-reference-sql-sp-tams-delete-regquerydept-sysownerapproval'></a>
# Procedure: sp_TAMS_Delete_RegQueryDept_SysOwnerApproval

The procedure deletes a record from TAMS_Reg_QueryDept based on the provided RegModID and RegRoleID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the module to be deleted. |
| @RegRoleID | INT | The ID of the role to be deleted. |

### Logic Flow
1. The procedure starts by beginning a transaction.
2. It then retrieves the RegId, Line, Module, and RegStatus from TAMS_Reg_Module for the provided RegModID.
3. The RegStatus is decremented by 1.
4. The procedure checks if there exists a record in TAMS_Reg_QueryDept with the same RegModID and RegRoleID as the current record.
5. If such a record exists, it is deleted from TAMS_Reg_QueryDept.
6. Finally, the transaction is committed.

### Data Interactions
* **Reads:** TAMS_Reg_Module
* **Writes:** TAMS_Reg_QueryDept

---


<a id='database-reference-sql-sp-tams-delete-userquerydeptbyuserid'></a>
# Procedure: sp_TAMS_Delete_UserQueryDeptByUserID

### Purpose
This stored procedure deletes all user query departments associated with a specified user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user whose query departments are to be deleted. |

### Logic Flow
1. The procedure starts by beginning a transaction.
2. It then checks if there exists any record in the TAMS_User_QueryDept table where the UserID matches the input parameter @UserID.
3. If such a record exists, it deletes all records from the TAMS_User_QueryDept table where the UserID is equal to @UserID.
4. After deleting the records, the procedure commits the transaction.

### Data Interactions
* **Reads:** TAMS_User_QueryDept
* **Writes:** TAMS_User_QueryDept

---


<a id='database-reference-sql-sp-tams-delete-userrolebyuserid'></a>
# Procedure: sp_TAMS_Delete_UserRoleByUserID

### Purpose
This stored procedure deletes a user role from the TAMS_User_Role table for a specified user ID, ensuring that only roles with an ID of 1 are deleted.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user whose role is to be deleted. |

### Logic Flow
The procedure starts by attempting to begin a transaction. If successful, it checks if a row exists in the TAMS_User_Role table for the specified user ID and RoleID not equal to 1. If such a row exists, it deletes this row from the table.

### Data Interactions
* **Reads:** TAMS_User_Role
* **Writes:** TAMS_User_Role

---


<a id='database-reference-sql-sp-tams-depot-applicant-list-child-onload'></a>
# Procedure: sp_TAMS_Depot_Applicant_List_Child_OnLoad

### Purpose
This stored procedure retrieves a list of applicant details for a specific depot, filtered by access date and sector ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Depot line number |
| @TrackType | NVARCHAR(50) | Track type filter |
| @ToAccessDate | NVARCHAR(20) | To access date filter (inclusive) |
| @FromAccessDate | NVARCHAR(20) | From access date filter (inclusive) |
| @TARType | NVARCHAR(20) | TAR type filter |
| @SectorID | INT | Sector ID filter |

### Logic Flow
1. The procedure starts by setting the current date to a variable.
2. It creates two temporary tables: `#TmpAppList` and `#TmpSector`.
3. The `#TmpAppList` table is populated with applicant details from `TAMS_TAR`, `TAMS_TAR_Sector`, `TAMS_WFStatus`, and `TAMS_Sector`. The data is filtered by the input parameters, including depot line number, track type, access dates, TAR type, sector ID, and WF status.
4. The procedure then selects specific columns from the `#TmpAppList` table based on the sector ID filter.
5. Finally, it drops both temporary tables.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_Sector, TAMS_WFStatus, TAMS_Sector

---


<a id='database-reference-sql-sp-tams-depot-applicant-list-master-onload'></a>
# Procedure: sp_TAMS_Depot_Applicant_List_Master_OnLoad

### Purpose
This stored procedure generates a list of depot applicants based on specific criteria, including line, track type, access date range, and TAR type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line to filter by. |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by. |
| @ToAccessDate | NVARCHAR(20) | Specifies the end date of the access range. |
| @FromAccessDate | NVARCHAR(20) | Specifies the start date of the access range. |
| @TARType | NVARCHAR(20) | Specifies the TAR type to filter by. |

### Logic Flow
1. The procedure starts by setting the current date and time.
2. It creates a temporary table, #TmpSector, to store the filtered sector data based on the provided line, track type, and access date range.
3. The procedure then truncates any existing data in #TmpSector.
4. It inserts data into #TmpSector from TAMS_Sector, filtering by the specified line, track type, and active status within the current date range.
5. The procedure groups the data in #TmpSector by sector order and orders the results accordingly.
6. Finally, it drops the temporary table.

### Data Interactions
* **Reads:** TAMS_Sector
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-depot-approval-onload'></a>
# Procedure: sp_TAMS_Depot_Approval_OnLoad

### Purpose
This stored procedure performs a series of checks and operations on a TAMS Depot Approval, including verifying sector conflicts, checking access requirements, and updating workflow statuses.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS Depot to be approved. |

### Logic Flow

1. The procedure starts by selecting relevant data from the TAMS_TAR table based on the provided TARID.
2. It then performs a series of checks and operations, including:
	* Verifying sector conflicts using the TAMS_Sector table.
	* Checking access requirements for traction power and other operations.
	* Updating workflow statuses for approved and pending workflows.
3. The procedure also updates the #TmpExc table to track any sector conflicts or exceptions that need to be addressed.

### Data Interactions
* **Reads:** 
	+ TAMS_TAR
	+ TAMS_Sector
	+ TAMS_Power_Sector
	+ TAMS_SPKSZone
	+ TAMS_TAR_Sector
	+ TAMS_Access_Requirement
	+ TAMS_Type_Of_Work
	+ TAMS_User
	+ TAMS_TAR_Workflow
	+ TAMS_Endorser
* **Writes:** 
	+ #TmpExc (temporary table to track sector conflicts and exceptions)
	+ #TmpExcSector (temporary table to store sector data)

---


<a id='database-reference-sql-sp-tams-depot-form-onload'></a>
# Procedure: sp_TAMS_Depot_Form_OnLoad

### Purpose
This stored procedure performs a series of checks and calculations to determine the availability of depot access for a given line, track type, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number being processed. |
| @TrackType | NVARCHAR(50) | The track type of the line. |
| @AccessDate | NVARCHAR(20) | The access date for which depot access is being checked. |
| @AccessType | NVARCHAR(20) | The access type (e.g., Possession, Protection). |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sector IDs. |
| @PowerSelTxt | NVARCHAR(100) | The power selection text. |

### Logic Flow
1. The procedure first checks if the selected sectors are DW only by comparing them with the DWSectors value from TAMS_Parameters.
2. It then retrieves the Company name and other relevant information for the given line, access date, and track type.
3. Next, it selects the Access Requirement records based on the line, track type, and access date.
4. Depending on the access type, it either retrieves or filters the Access Requirement records further.
5. The procedure then calculates the availability of depot access by checking if there are any approved TARs for the selected sectors in TAMS_TAR_Sectors.
6. If the access is for a weekend or PH, it checks if there are any approved TARs for the selected sectors in TAMS_TAR_Sectors and returns 'false' otherwise.
7. Finally, the procedure creates a temporary table to store the power sector information and executes a query to retrieve the power on/off status.

### Data Interactions
* Reads: 
	+ TAMS_Parameters
	+ TAMS_Access_Requirement
	+ TAMS_Sector
	+ TAMS_Power_Sector
	+ TAMS_Track_Power_Sector
	+ TAMS_TAR
	+ TAMS_TAR_Sector
	+ TAMS_User
	+ TAMS_User_Role
	+ TAMS_Role
* Writes: 
	+ #TmpPossPowSector (temporary table)

---


<a id='database-reference-sql-sp-tams-depot-form-save-access-details'></a>
# Procedure: sp_TAMS_Depot_Form_Save_Access_Details

### Purpose
This stored procedure saves access details for a depot form, including user information and TAR (Traction and Maintenance System) data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Depot line number |
| @TrackType | NVARCHAR(50) | Track type of the depot form |
| @AccessDate | NVARCHAR(20) | Date of access to the depot form |
| @AccessTimeSlot | NVARCHAR(50) | Time slot for accessing the depot form |
| @AccessType | NVARCHAR(20) | Type of access (e.g., user, admin) |
| @TARType | NVARCHAR(10) | Type of TAR data being saved |
| @Company | NVARCHAR(50) | Company name associated with the TAR data |
| @Designation | NVARCHAR(50) | Designation or role of the user accessing the depot form |
| @Name | NVARCHAR(50) | Name of the user accessing the depot form |
| @OfficeNo | NVARCHAR(50) | Office number of the user accessing the depot form |
| @MobileNo | NVARCHAR(50) | Mobile number of the user accessing the depot form |
| @Email | NVARCHAR(50) | Email address of the user accessing the depot form |
| @AccessTimeFrom | NVARCHAR(50) | Start time of access to the depot form |
| @AccessTimeTo | NVARCHAR(50) | End time of access to the depot form |
| @AccessLocation | NVARCHAR(50) | Location where the depot form was accessed |
| @IsNeutralGap | INT | Flag indicating whether a neutral gap is involved |
| @IsExclusive | INT | Flag indicating whether exclusive access is required |
| @DescOfWork | NVARCHAR(100) | Description of work being done on the depot form |
| @ARRemark | NVARCHAR(1000) | Additional remarks or comments about the TAR data |
| @InvolvePower | INT | Flag indicating whether power involvement is required |
| @PowerOn | INT | Flag indicating whether power-on is required |
| @Is13ASocket | INT | Flag indicating whether 13A socket is involved |
| @CrossOver | INT | Flag indicating whether cross-over is involved |
| @UserID | NVARCHAR(100) | User ID of the user accessing the depot form |
| @ProtectionType | NVARCHAR(50) | Type of protection required for the TAR data |
| @TARID | BIGINT OUTPUT | Unique identifier for the saved TAR data |
| @Message | NVARCHAR(500) OUTPUT | Error message if any |

### Logic Flow
1. The procedure starts by setting the initial internal transaction counter to 0.
2. It checks if there is an active transaction and sets the internal transaction counter accordingly.
3. If the user ID is provided, it retrieves the corresponding user ID from the TAMS_User table.
4. The procedure then inserts a new record into the TAMS_TAR table with the provided data.
5. After inserting the record, it retrieves the newly generated TAR ID using the SCOPE_IDENTITY() function.
6. If any errors occur during the insertion process, it sets an error message and exits the procedure.
7. Finally, if no errors occurred, it commits the transaction and returns the error message.

### Data Interactions
* Reads: TAMS_User table (for retrieving user ID)
* Writes: TAMS_TAR table (for inserting new record)

---


<a id='database-reference-sql-sp-tams-depot-form-submit'></a>
# Procedure: sp_TAMS_Depot_Form_Submit

### Purpose
This stored procedure is used to submit a Depot Form for Urgent TAR (Track Access Management System) and update the relevant records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the track type |
| @TrackType | NVARCHAR(50) | The track type of the depot form |
| @AccessDate | NVARCHAR(20) | The access date of the depot form |
| @AccessType | NVARCHAR(20) | The access type of the depot form |
| @TARType | NVARCHAR(10) | The type of TAR (Track Access Management System) |

### Logic Flow
The procedure follows these steps:

1. It checks if a transaction is already in progress and sets an internal transaction flag.
2. It retrieves the user ID from the TAMS_User table based on the provided login ID.
3. It determines the sector color code for the depot form based on the access type and exclusive status.
4. It inserts the sector data into the TAMS_TAR_Sector table.
5. It inserts the station data into the TAMS_TAR_Station table.
6. It inserts the power sector data into the TAMS_TAR_Power_Sector table, first for non-buffer zones and then for buffer zones.
7. It inserts the SPKS zone data into the TAMS_TAR_SPKSZone table.
8. It inserts the attachment data from the TAMS_TAR_Attachment_Temp table into the TAMS_TAR_Attachment table.
9. If the TAR type is 'Urgent', it checks if Saturday, Sunday, and PH are included in the effective date range and updates the workflow status accordingly.
10. It generates a reference number for the depot form using the sp_Generate_Ref_Num stored procedure.
11. It updates the TAMS_TAR table with the new values.
12. If an error occurs during the insertion process, it rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_User, TAMS_Sector, TAMS_Track_Power_Sector, TAMS_Power_Sector, TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_SPKSZone, TAMS_TAR_Attachment_Temp, TAMS_TAR_AccessReq, TAMS_Workflow, TAMS_Endorser, TAMS Paramaters
* Writes: TAMS_User, TAMS_Sector, TAMS_Track_Power_Sector, TAMS_Power_Sector, TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_SPKSZone, TAMS_TAR_Attachment_Temp, TAMS_TAR_AccessReq, TAMS_Workflow, TAMS_Endorser

---


<a id='database-reference-sql-sp-tams-depot-form-update-access-details'></a>
# Procedure: sp_TAMS_Depot_Form_Update_Access_Details

### Purpose
This stored procedure updates access details for a depot form, including company, designation, name, and other relevant information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Company | NVARCHAR(50) | Company name to be updated |
| @Designation | NVARCHAR(50) | Designation to be updated |
| @Name | NVARCHAR(50) | Name to be updated |
| @OfficeNo | NVARCHAR(50) | Office number to be updated |
| @MobileNo | NVARCHAR(50) | Mobile number to be updated |
| @Email | NVARCHAR(50) | Email address to be updated |
| @AccessTimeFrom | NVARCHAR(50) | Access time from to be updated |
| @AccessTimeTo | NVARCHAR(50) | Access time to be updated |
| @IsExclusive | INT | Flag indicating exclusive access (0 or 1) |
| @DescOfWork | NVARCHAR(100) | Description of work to be updated |
| @ARRemark | NVARCHAR(1000) | Additional remarks to be updated |
| @InvolvePower | INT | Flag indicating involvement with power (0 or 1) |
| @PowerOn | INT | Flag indicating power on status (0 or 1) |
| @Is13ASocket | INT | Flag indicating 13A socket usage (0 or 1) |
| @CrossOver | INT | Flag indicating cross-over usage (0 or 1) |
| @UserID | NVARCHAR(20) | User ID to be updated |
| @ProtectionType | NVARCHAR(50) | Protection type to be updated |
| @TARID | BIGINT | ID of the TAR record to be updated |
| @Message | NVARCHAR(500) | Error message output |

### Logic Flow
1. The procedure starts by setting an internal transaction flag and beginning a transaction if no transactions are already active.
2. It retrieves the user ID from the TAMS_User table based on the provided login ID.
3. The procedure then updates the specified fields in the TAMS_TAR table with the provided values, including the updated user ID.
4. If any errors occur during the update process, an error message is set and the transaction is rolled back.
5. Otherwise, the transaction is committed, and the procedure returns the error message.

### Data Interactions
* **Reads:** TAMS_User table (for retrieving user ID)
* **Writes:** TAMS_TAR table (for updating records)

---


<a id='database-reference-sql-sp-tams-depot-getblockedtardates'></a>
# Procedure: sp_TAMS_Depot_GetBlockedTarDates

### Purpose
This stored procedure retrieves blocked TAR dates for a specific line from the TAMS_Block_TARDate table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to retrieve blocked TAR dates for. |
| @AccessDate | date | The access date to filter blocked TAR dates by. |

### Logic Flow
1. The procedure starts by selecting the ID, Line, BlockDate, and BlockReason columns from the TAMS_Block_TARDate table.
2. It filters the results based on the provided Line (@Line) and AccessDate (@AccessDate).
3. Only records with IsActive = 1 are included in the results.
4. The results are ordered by BlockDate in ascending order.

### Data Interactions
* **Reads:** TAMS_Block_TARDate table

---


<a id='database-reference-sql-sp-tams-depot-getpossessiondepotsectorbypossessionid'></a>
# Procedure: sp_TAMS_Depot_GetPossessionDepotSectorByPossessionId

This procedure retrieves data from the TAMS_Possession_DepotSector table based on a specified PossessionId.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | The ID of the possession for which to retrieve depot sector information |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_Possession_DepotSector table.
2. It filters the results to only include rows where the PossessionId matches the input parameter.
3. The results are ordered in ascending order by the ID column.

### Data Interactions
* **Reads:** TAMS_Possession_DepotSector

---


<a id='database-reference-sql-sp-tams-depot-gettarbytarid'></a>
# Procedure: sp_TAMS_Depot_GetTarByTarId

The purpose of this stored procedure is to retrieve detailed information about a specific TAR (TAR ID) from the TAMS_TAR table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The TAR ID for which to retrieve details. |

### Logic Flow
1. The procedure starts by declaring two variables, @PowerZone and @SPKSZone, to store the Power Sector and SPKS Zone information respectively.
2. It then selects the Power Sector information from the TAMS_Power_Sector table where the TAR ID matches the input parameter @TarId. The selected data is grouped by Power Sector and the results are concatenated into the @PowerZone variable.
3. If the length of @PowerZone is greater than 0, it removes the trailing comma and space to ensure proper formatting.
4. Similarly, it selects the SPKS Zone information from the TAMS_SPKSZone table where the TAR ID matches the input parameter @TarId. The selected data is grouped by SPKS Zone and the results are concatenated into the @SPKSZone variable.
5. If the length of @SPKSZone is greater than 0, it removes the trailing comma and space to ensure proper formatting.
6. Finally, the procedure retrieves the detailed information about the TAR from the TAMS_TAR table where the ID matches the input parameter @TarId.

### Data Interactions
* **Reads:** TAMS_Power_Sector, TAMS_SPKSZone, TAMS_TAR
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-depot-gettarenquiryresult-department'></a>
# Procedure: sp_TAMS_Depot_GetTarEnquiryResult_Department

### Purpose
This stored procedure retrieves a list of companies associated with a specific TAR (Tracking and Reporting) status, filtered by various parameters such as track type, access date range, and user role.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The ID of the user making the enquiry. |
| @Line | nvarchar(50) | The line number to filter by (optional). |
| @TrackType | nvarchar(50) | The track type to filter by (e.g., 'NEL', 'PFR', etc.). |
| @TarType | nvarchar(50) | The TAR type to filter by (optional). |
| @AccessType | nvarchar(50) | The access type to filter by (optional). |
| @TarStatusId | integer | The TAR status ID to filter by. |
| @AccessDateFrom | nvarchar(50) | The start date of the access period (optional). |
| @AccessDateTo | nvarchar(50) | The end date of the access period (optional). |

### Logic Flow
1. The procedure first checks if the user has a specific role that allows them to view TARs for all track types.
2. If not, it then checks if the user has a power endorser or power HOD role, which grants them access to TARs with InvolvePower = 1.
3. Next, it checks if the user is an applicant HOD and can view TARs under their own department.
4. Finally, if none of the above conditions are met, the procedure filters the TARs based on the specified track type, access date range, and user ID.

### Data Interactions
* Reads: TAMS_TAR, TAMS_WFStatus, TAMS_User_QueryDept, TAMS_User_Role
* Writes: None

---


<a id='database-reference-sql-sp-tams-depot-gettarsectorsbyaccessdateandline'></a>
# Procedure: sp_TAMS_Depot_GetTarSectorsByAccessDateAndLine

### Purpose
This stored procedure retrieves Tar Sectors from TAMS Depot by Access Date and Line.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The access date to filter the results. |
| @Line | nvarchar(10) = NULL | The line to filter the results (optional). |

### Logic Flow
1. A temporary table #TMP is created with various columns.
2. If the @Line parameter is 'NEL', the procedure inserts data into #TMP from TAMS_Sector, TAMS_TAR_Sector, and TAMS_TAR tables based on the specified Access Date and conditions.
3. The procedure updates the ColourCode column in #TMP by selecting a value from another row with matching SameSector, TarNo, and ColourCode.
4. Finally, the procedure selects all data from #TMP ordered by [Order] ASC.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR tables.
* **Writes:** #TMP table.

---


<a id='database-reference-sql-sp-tams-depot-gettarsectorsbytarid'></a>
# Procedure: sp_TAMS_Depot_GetTarSectorsByTarId

### Purpose
This stored procedure retrieves a list of sectors associated with a specific TAR (TAR stands for Tariff Area Management System Sector) ID, excluding buffer sectors.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The TAR ID to retrieve sectors for. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Sector table.
2. It then joins this table with the TAMS_TAR_Sector table on the SectorId column, and further joins it with the TAMS_TAR table on the TARId column.
3. The procedure filters out buffer sectors (where IsBuffer = 1) based on the provided TAR ID.
4. Finally, the results are ordered by Order and Sector in ascending order.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR

---


<a id='database-reference-sql-sp-tams-depot-inbox-child-onload'></a>
# Procedure: sp_TAMS_Depot_Inbox_Child_OnLoad

### Purpose
This stored procedure populates the inbox for a specific depot by retrieving TARs that are pending and have not been processed yet, based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter TARs by. |
| @TrackType | NVARCHAR(50) | The track type to filter TARs by. |
| @AccessDate | NVARCHAR(20) | The access date to filter TARs by. |
| @TARType | NVARCHAR(20) | The TAR type to filter TARs by. |
| @LoginUser | NVARCHAR(50) | The login user ID to filter TARs by. |
| @SectorID | INT | The sector ID to filter TARs by. |

### Logic Flow
1. The procedure starts by selecting the current date and time.
2. It then truncates three temporary tables: #TmpSector, #TmpInbox, and #TmpInboxList.
3. Next, it inserts data into #TmpSector from TAMS_Sector table based on the provided line number and track type.
4. After that, it inserts data into #TmpInbox from TAMS_TAR table based on the provided TAR type, access date, and sector ID. The data is filtered to include only TARs with a pending status and not processed yet.
5. The procedure then creates two cursors: @Cur01 and @Cur02. 
6. The first cursor fetches all TARs from #TmpInboxList that have not been processed yet (i.e., ActionByChk = 0).
7. For each TAR, the procedure checks if the user ID matches the provided login user ID. If it does, it increments the ActionByChk counter.
8. If ActionByChk is still 0 after checking all actions for a TAR, it inserts the TAR into #TmpInboxList.
9. The second cursor fetches the action by which a TAR should be processed from TAMS_TAR_Workflow table based on the TAR ID.
10. For each action, the procedure checks if the user ID matches the provided login user ID. If it does, it increments the ActionByChk counter.
11. After checking all actions for a TAR, the procedure inserts the TAR into #TmpInboxList only if ActionByChk is still 0.
12. Finally, the procedure selects and groups the data from #TmpInboxList based on the sector ID and returns the result.

### Data Interactions
* Reads: TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Endorser, TAMS_User_Role, TAMS_USER
* Writes: #TmpSector, #TmpInbox, #TmpInboxList

---


<a id='database-reference-sql-sp-tams-depot-inbox-master-onload'></a>
# Procedure: sp_TAMS_Depot_Inbox_Master_OnLoad

### Purpose
This stored procedure loads depot inbox data into temporary tables for further processing, ensuring that only pending tasks are included and filtered by user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Depot line number to filter tasks by. |
| @TrackType | NVARCHAR(50) | Track type to filter tasks by. |
| @AccessDate | NVARCHAR(20) | Access date to filter tasks by. |
| @TARType | NVARCHAR(20) | Task type to filter tasks by. |
| @LoginUser | NVARCHAR(50) | User ID to filter tasks by. |

### Logic Flow
1. The procedure starts by selecting the user ID from the TAMS_USER table based on the provided login user.
2. It then creates temporary tables (#TmpSector, #TmpInbox, and #TmpInboxList) to store sector data, inbox data, and a list of tasks, respectively.
3. The procedure truncates these temporary tables before populating them with data from the TAMS_Sector and TAMS_TAR tables.
4. It filters the tasks based on the provided parameters (line number, track type, access date, and task type) and only includes pending tasks that match the user ID.
5. For each task, it checks if there are any workflows associated with it. If not, it inserts the task into the #TmpInboxList table.
6. If there are workflows, it fetches the action by from the TAMS_TAR_Workflow table and checks if the user ID matches. If it does, it increments a counter to track the number of actions by the user.
7. After processing all tasks, it groups the sector data by line, sector ID, sector name, and sector order and returns this data.

### Data Interactions
* Reads: TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_USER
* Writes: #TmpSector, #TmpInbox, #TmpInboxList

---


<a id='database-reference-sql-sp-tams-depot-rgs-acksurrender'></a>
# Procedure: sp_TAMS_Depot_RGS_AckSurrender

### Purpose
This stored procedure performs the business task of acknowledging a surrender for a TAR (TAR ID) and updating the relevant records in the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID to be acknowledged. |
| @UserID | NVARCHAR(500) | The user ID of the person performing the action. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that will contain a message indicating the result of the operation. |

### Logic Flow
1. The procedure first checks if there is an open transaction. If not, it sets a flag to indicate that an internal transaction has been started.
2. It then retrieves the user ID from the TAMS_User table based on the provided @UserID parameter.
3. Next, it checks the TOA status of the TAR sector associated with the @TARID parameter. If the status is 4 (pending), it proceeds to update the TOA status to 5 (acknowledged) and sets the AckSurrenderTime to the current date and time.
4. It then inserts an audit record into the TAMS_TOA_Audit table for the updated TAR sector.
5. The procedure then checks if the line is 'NEL'. If so, it generates a message indicating that the surrender has been acknowledged by NEL DCC.
6. It then sends an SMS to the mobile number associated with the TAR sector using the sp_api_send_sms stored procedure.
7. If any errors occur during this process, the procedure will display an error message in the @Message output parameter.

### Data Interactions
* Reads: TAMS_User, TAMS_TAR, TAMS_TOA, TAMS_Depot_Auth, TAMS_WFStatus, TAMS_Depot_Auth_Workflow, TAMS_TOA_Audit
* Writes: TAMS_TOA (TOA status), TAMS_Depot_Auth_Workflow (workflow updates), TAMS_Depot_Auth (DepotAuthStatusId)

---


<a id='database-reference-sql-sp-tams-depot-rgs-granttoa'></a>
# Procedure: sp_TAMS_Depot_RGS_GrantTOA

### Purpose
This stored procedure grants a Temporary Authorization (TOA) to a Road Geographical Section (RGS) for a specific TAR ID, based on the provided parameters and business rules.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID for which TOA is being granted. |
| @EncTARID | NVARCHAR(250) | The Encoded TAR ID. |
| @UserID | NVARCHAR(500) | The user ID of the person performing the action. |
| @toacallbacktiming | datetime | The callback timing for the TOA grant. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message to be sent via SMS. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets an internal flag and begins a new transaction.
2. It then retrieves the TAR ID, Line, Operation Date, Access Type, Mobile No, and TOA Status from the TAMS_TAR and TAMS_TOA tables based on the provided @TARID.
3. If the TOA status is 2 (Pending), it generates a reference number for the TOA grant using the sp_Generate_Ref_Num_TOA stored procedure.
4. It updates the TOA status to 3 (Granted) in the TAMS_TOA table, sets the TOANo, GrantTOATime, and UpdatedOn fields accordingly.
5. It inserts an audit record into the TAMS_TOA_Audit table for the updated TAR ID.
6. Based on the Access Type, it constructs a message to be sent via SMS to the user's mobile number.
7. If the @HPNo field is not empty, it sends the SMS using the sp_api_send_sms stored procedure.
8. If any errors occur during the process, it sets an error message and either commits or rolls back the transaction depending on whether an error occurred.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-depot-rgs-onload'></a>
# Procedure: sp_TAMS_Depot_RGS_OnLoad

### Purpose
This stored procedure performs a series of operations to retrieve and process data for Depot RGS (Railway Group Standard) on-load events.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used to filter the data. |
| @TrackType | NVARCHAR(50) | The track type used to filter the data. |
| @accessDate | DATETIME | The access date used to filter the data. |

### Logic Flow
The procedure starts by declaring several variables and setting their initial values. It then retrieves the necessary parameters from the TAMS_Parameters table based on the provided line number.

Next, it calculates the operation date and cutoff time for the current day. It then selects the required data from various tables, including TAMS_TAR, TAMS_TOA, and TAMS_Depot_Auth, using a series of joins and subqueries.

The procedure then applies several conditions to filter the data, such as checking if the TOA status is not equal to 0, 5, or 6. It also orders the results by access type, TAR number, and ID.

Finally, it returns the processed data in a specific format, including the operation date, access date, and various other fields.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Depot_Auth, TAMS_Parameters

---


<a id='database-reference-sql-sp-tams-depot-rgs-onload-enq'></a>
# Procedure: sp_TAMS_Depot_RGS_OnLoad_Enq

### Purpose
This stored procedure is used to retrieve data for a Depot RGS (Railway Grouping System) on-load inquiry.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to query. |
| @TrackType | nvarchar(50) | The track type to filter by. |
| @accessDate | Date | The access date to filter by. |

### Logic Flow
1. The procedure starts by setting the current date and time, as well as a cutoff time for the operation.
2. It then retrieves the possession, protection, and cancellation background values from the TAMS_Parameters table based on the line number provided.
3. Next, it selects data from the TAMS_TAR and TAMS_TOA tables where the access date matches the provided value, the track type is 'DEPOT', and the line number matches the provided value.
4. The procedure then calculates various times (PowerOffTime, CircuitBreakOutTime, RadioMsgTime, LineClearMsgTime) based on the retrieved data.
5. It also retrieves additional information such as parties involved, work description, contact numbers, TOA status, and remarks for each TAR and TOA record.
6. Finally, the procedure orders the results by access type, TAR number, and then by other fields.

### Data Interactions
* **Reads:** TAMS_Parameters, TAMS_TAR, TAMS_TOA

---


<a id='database-reference-sql-sp-tams-depot-rgs-update-details'></a>
# Procedure: sp_TAMS_Depot_RGS_Update_Details

### Purpose
This stored procedure updates the details of a Depot RGS (Railway Goods Storage) by checking the qualification status and updating the relevant records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID of the Depot RGS to be updated. |
| @InchargeNRIC | NVARCHAR(50) | The Incharge NRIC of the Depot RGS. |
| @MobileNo | NVARCHAR(20) | The Mobile No of the Incharge. |
| @TetraRadioNo | NVARCHAR(50) | The Tetra Radio No of the Incharge. |
| @UserID | NVARCHAR(500) | The UserID of the user updating the Depot RGS. |
| @TrackType | NVARCHAR(50)='Mainline' | The track type of the Depot RGS (default: Mainline). |

### Logic Flow
The procedure follows these steps:

1. It checks if a transaction has been started and sets an internal flag `@IntrnlTrans` accordingly.
2. It creates a temporary table `#tmpnric` to store the results of the qualification check.
3. It truncates the temporary table and then populates it with the results of the qualification check for each line in the Depot RGS.
4. It checks if there are any invalid qualifications and sets the corresponding variables accordingly.
5. If there are no invalid qualifications, it updates the relevant records in the `TAMS_TOA` table and inserts audit records into the `TAMS_TOA_Audit` and `TAMS_TOA_Parties_Audit` tables.
6. If there are invalid qualifications, it sets an error message and returns it to the caller.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_TOA_Audit, TAMS_TOA_Parties_Audit
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties_Audit

---


<a id='database-reference-sql-sp-tams-depot-rgs-update-details20250403'></a>
# Procedure: sp_TAMS_Depot_RGS_Update_Details20250403

### Purpose
This stored procedure updates the details of a Depot RGS (Railway Goods Storage) by checking the qualification status and updating the relevant records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | TAR ID to update |
| @InchargeNRIC | NVARCHAR(50) | In charge NRIC |
| @MobileNo | NVARCHAR(20) | Mobile number of in charge |
| @TetraRadioNo | NVARCHAR(50) | Tetra radio number of in charge |
| @UserID | NVARCHAR(500) | User ID for auditing purposes |
| @TrackType | NVARCHAR(50) | Track type (Mainline or Depot) |

### Logic Flow
1. The procedure starts by checking if a transaction has been started. If not, it sets the internal transaction flag to 1 and begins a new transaction.
2. It then creates a temporary table #tmpnric to store the results of the qualification checks.
3. The procedure truncates the temporary table and selects the relevant data from TAMS_TOA and TAMS_TAR tables based on the TAR ID provided.
4. It then performs two string aggregation operations using STRING_AGG function to get the QTSQualCode and QTSQualCodeProt values for each line.
5. The procedure then checks if there are any valid qualifications for the in charge NRIC. If not, it sets the qualification status to 'InValid' and updates the relevant records accordingly.
6. If there are valid qualifications, it updates the in charge name, mobile number, tetra radio number, and other relevant fields based on the QTSQualCode and QTSQualCodeProt values.
7. The procedure then checks if any new in charges need to be added or existing ones updated. If so, it performs the necessary insertions, updates, and deletions.
8. Finally, the procedure commits or rolls back the transaction depending on whether an error occurred during execution.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_TOA_Audit, TAMS_TOA_Parties_Audit, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties

---


<a id='database-reference-sql-sp-tams-depot-rgs-update-qts'></a>
# Procedure: sp_TAMS_Depot_RGS_Update_QTS

### Purpose
This stored procedure updates the QTS qualification status for a specific depot and track type, triggering an audit and potentially updating the TAMS TOA record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Depot ID |
| @InchargeNRIC | NVARCHAR(50) | In-charge NRIC number |
| @UserID | NVARCHAR(500) | User ID for auditing purposes |
| @TrackType | NVARCHAR(50) | Track type (Mainline or Depot) |
| @Message | NVARCHAR(500) | Output parameter to store error message |
| @QTSQCode | NVARCHAR(50) | Output parameter to store QTS qualification code |
| @QTSLine | NVARCHAR(10) | Output parameter to store track line |

### Logic Flow
1. The procedure starts by checking if a transaction is already active. If not, it sets the internal transaction flag to 1.
2. It then creates a temporary table #tmpnric to store the results of the QTS qualification check.
3. The procedure truncates the temporary table and selects the required data from TAMS_TOA and TAMS_TAR tables based on the provided TARID and track type.
4. It then checks if the QTS qualification status is valid for the selected track line. If not, it triggers an audit and potentially updates the TAMS TOA record.
5. The procedure then calls a separate stored procedure [sp_api_tams_qts_upd_accessdate] to update the QTS qualification status in the database.
6. Depending on the outcome of the QTS qualification check, the procedure sets the @Message output parameter to indicate whether the update was successful or not.
7. If an error occurs during the execution of the stored procedure, it logs the error and returns the corresponding error message.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TAR, TAMS_Parameters
* Writes: TAMS_QTS_Error_Log

---


<a id='database-reference-sql-sp-tams-depot-sectorbooking-onload'></a>
# Procedure: sp_TAMS_Depot_SectorBooking_OnLoad

### Purpose
This stored procedure performs a one-time load of sector booking data for depot sectors, including power zone and SPKS zone information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to process. |
| @TrackType | NVARCHAR(50) | The track type to process. |
| @AccessDate | NVARCHAR(20) | The access date for the sector booking data. |
| @TARType | NVARCHAR(20) | The TAR type to use for color code determination. |
| @AccessType | NVARCHAR(20) | The access type to determine operation requirements. |

### Logic Flow
1. The procedure starts by truncating a temporary table #ListES.
2. It then declares several variables, including @CurID, @CurLine, @CurSector, and @CurOrderID, which will be used to iterate through the sector booking data.
3. If the @Line parameter is 'NEL', it inserts data into #ListES from TAMS_Sector table based on the @TrackType parameter.
4. A cursor (@Cur01) is created to iterate through the sector booking data in TAMS_Sector table, filtering by Line and TrackType.
5. For each iteration, the procedure extracts power zone and SPKS zone information from TAMS_SPKSZone and TAMS_Power_Sector tables based on the SectorID.
6. It then determines the color code for the sector booking data using TAMS_TAR and TAMS_TAR_Sector tables.
7. If the @ColorCode is empty, it updates #ListES with the power zone and SPKS zone information. Otherwise, it updates #ListES with the existing color code.
8. Depending on the @AccessType parameter, it determines operation requirements from TAMS_Access_Requirement table.
9. Finally, it selects data from #ListES and returns it.

### Data Interactions
* **Reads:** 
	+ TAMS_Sector table
	+ TAMS_SPKSZone table
	+ TAMS_Power_Sector table
	+ TAMS_TAR table
	+ TAMS_TAR_Sector table
	+ TAMS_Access_Requirement table
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-depot-sectorbooking-qts-chk'></a>
# Procedure: sp_TAMS_Depot_SectorBooking_QTS_Chk

### Purpose
This stored procedure checks if a person's qualification status is valid for a specific depot sector booking.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(MAX) | The person's ID number. |
| @qualdate | NVARCHAR(MAX) | The date of the qualification. |
| @line | NVARCHAR(MAX) | The line number. |
| @TrackType | NVARCHAR(50) | The track type. |

### Logic Flow
The procedure follows these steps:

1. It initializes several variables to keep track of the results.
2. It creates temporary tables to store the qualification data and the person's details.
3. It loops through each row in the #tmpnric table, which contains the person's details.
4. For each row, it checks if there is a matching record in the #tmpqtsqc table, which contains the qualification status for each person.
5. If no matching record is found, it updates the person's status to "InValid".
6. If a matching record is found, it checks if the person has any suspension information. If not, it updates the person's status to "Valid". If there is suspension information, it checks if the qualification date is within the valid period. If it is, it updates the person's status to "Valid". Otherwise, it updates the person's status to "InValid".
7. Finally, it returns the updated person's details.

### Data Interactions
* **Reads:** #tmpnric, #tmpqtsqc
* **Writes:** #tmpnric

---


<a id='database-reference-sql-sp-tams-depot-toa-qts-chk'></a>
# Procedure: sp_TAMS_Depot_TOA_QTS_Chk

### Purpose
This stored procedure checks if a person has a valid qualification for a specific depot and date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric		NVARCHAR(50) = NULL, 
| @qualdate	NVARCHAR(20) = NULL,
| @line		NVARCHAR(20) = NULL,
| @QualCode	NVARCHAR(50) = NULL |

### Logic Flow
1. The procedure starts by declaring variables to store the result of the query and initializing counters for the number of qualifications found.
2. It then truncates a temporary table #tmpqtsqc, which will be used to store the results of the qualification checks.
3. The procedure selects the personnel's name from the QTS_Personnel table based on the provided nric.
4. It inserts the decrypted access ID and other relevant information into the #tmpqtsqc table for each qualification found that matches the provided line, QualCode, and date range.
5. If no qualifications are found, the procedure sets a status to 'InValid'.
6. Otherwise, it selects the last access date, valid access date, and valid till date from the #tmpqtsqc table.
7. It checks if there is a suspended till date; if so, it sets the status to 'InValid'. If not, it checks if the provided qualification date falls within the valid access date range; if not, it sets the status to 'InValid'.
8. Finally, the procedure returns the decrypted nric, name, line, qualification date, QualCode, and status.

### Data Interactions
* **Reads:** 
	+ [flexnetskgsvr].[QTSDB].[dbo].QTS_Personnel
	+ [flexnetskgsvr].[QTSDB].[dbo].QTS_Personnel_Qualification
	+ [flexnetskgsvr].[QTSDB].[dbo].QTS_Qualification
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-depot-toa-register'></a>
# Procedure: sp_TAMS_Depot_TOA_Register

### Purpose
This stored procedure registers a new TOA (Train Operations Authority) for a specific TAR (Train Access Request). It validates various parameters, including the line, track type, and TAR status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line of the train. |
| @TrackType | NVARCHAR(50) | The type of track (e.g., Depot or Mainline). |
| @Type | NVARCHAR(20) | The type of TOA registration. |
| @Loc | NVARCHAR(20) | The location of the TAR. |
| @TARNo | NVARCHAR(30) | The unique identifier for the TAR. |
| @NRIC | NVARCHAR(20) | The National Registration Identity Card number. |
| @TOAID | BIGINT OUTPUT | The unique identifier for the TOA registration. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the outcome of the procedure. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets an internal flag and begins a new transaction.
2. It creates a temporary table to store the results of the qualification checks for each QTS (Qualification Testing System) code.
3. The procedure then retrieves the cut-off time for the current day based on the line and track type.
4. It selects the QTS codes that apply to the current line and track type, as well as the corresponding protection types.
5. If the TAR is not found or does not match the expected status, the procedure sets an error message and returns without inserting into the TOA table.
6. The procedure then checks if the TAR has a valid QTS code and if the qualification status is valid. If not, it sets an error message and returns without inserting into the TOA table.
7. If the TAR has a valid QTS code and qualification status, the procedure inserts a new record into the TOA table with the required information.
8. The procedure then updates the TAR status to reflect the new TOA registration.
9. Finally, it logs the registration in the TAMS_TOA_Registration_Log table.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TAMs_Station, TAMS_Parameters, TAMS_TOa, TAMS_TOA_Audit, TAMS_TOA_Parties
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-depot-toa-register-1'></a>
# Procedure: sp_TAMS_Depot_TOA_Register_1

### Purpose
This stored procedure registers a TAR (Train Access Record) for Depot TOA (Train Operations Authority) purposes, updating relevant records and logging the registration.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Line number of the train |
| @TrackType | nvarchar(50) | Track type (DEPOT or Mainline) |
| @Type | NVARCHAR(20) | Type of TAR registration |
| @Loc | NVARCHAR(20) | Location of the station |
| @TARNo | NVARCHAR(30) | Number of the train access record |
| @NRIC | NVARCHAR(20) | National Registration Identity Card number |
| @TOAID | BIGINT OUTPUT | Unique ID for the TAR registration |
| @Message | NVARCHAR(500) OUTPUT | Error message or success message |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets an internal flag to indicate that a new transaction has started.
2. It then creates a temporary table #tmpnric to store the results of the QTS (Qualification Testing System) checks for each line number.
3. The procedure truncates the temporary table and sets up variables for the execution string, qualification date, in-charge name, and in-charge status.
4. It retrieves the cut-off time for the current day based on the track type and line number.
5. The procedure then performs QTS checks for each line number using the STRING_AGG function to concatenate the results into a single string.
6. If the line number is 'DTL', it counts the number of TAR records with the same status ID as the line number.
7. It sets up variables for the TAR ID, TAR line, TAR access date, and access type based on the line number.
8. The procedure then checks if the TAR record exists in the database and updates the operation date if necessary.
9. If the TAR record does not exist or has an invalid status, it performs additional checks to determine the reason for the error.
10. Finally, the procedure inserts a new log entry into the TAMS_TOA_Registration_Log table with the registration details.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TAMs_Station, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Registration_Log
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-depot-updatedtcauth'></a>
# Procedure: sp_TAMS_Depot_UpdateDTCAuth

### Purpose
This stored procedure updates the DTCAuth status for a given user and workflow ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @username | nvarchar(50) | The username of the user being updated. |
| @authid | int | The ID of the authentication being updated. |
| @workflowid | int | The ID of the workflow being updated. |
| @statusid | int | The current status ID. |
| @val | bit | The new value for the DTCAuth status (NULL for no change). |
| @valstr | nvarchar(50) | The string representation of the new value for the DTCAuth status (NULL for no change). |
| @powerzoneid | int | The ID of the power zone being updated. |
| @success | bit | Output parameter indicating whether the update was successful. |
| @type | int | The type of update (1 for checkbox, 2 for dropdown). |
| @spksid | int | The ID of the SPKSID being updated. |
| @Message | nvarchar(500) | Output parameter containing any error messages. |

### Logic Flow
The procedure follows these steps:

1. It checks if the user has access to update the information by checking if the username exists in the TAMS_Endorser table with the specified workflow ID.
2. If the user does not have access, it sets an error message and skips the rest of the procedure.
3. It checks if the workflow is already updated by checking if there is a record in the TAMS_Depot_Auth_Workflow table with the same authentication ID and workflow ID.
4. If the workflow is not already updated, it updates the current workflow by setting the WFStatus field to the new value based on the @type parameter.
5. It gets the next status ID from the TAMS_WFStatus table based on the current status ID.
6. It inserts a new record into the TAMS_Depot_Auth_Workflow table with the updated workflow ID and authentication ID.
7. Depending on the workflow ID, it updates other tables such as TAMS_Depot_DTCAuth_SPKS, TAMS_Depot_Auth_Powerzone, or TAMS_Depot_Auth to update the status ID.

### Data Interactions
* Reads: TAMS_Endorser, TAMS_User_Role, TAMS_User, TAMS_WFStatus, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth, TAMS_Depot_DTCAuth_SPKS, TAMS_Depot_Auth_Powerzone.
* Writes: TAMS_Depot_Auth_Workflow.

---


<a id='database-reference-sql-sp-tams-depot-updatedtcauthbatch'></a>
# Procedure: sp_TAMS_Depot_UpdateDTCAuthBatch

### Purpose
This stored procedure updates the status of a Depot Authorization batch.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @success | bit | Output parameter indicating success or failure |
| @Message | NVARCHAR(500) | Output parameter containing error message if any |

### Logic Flow
The procedure starts by checking the transaction count. If it's 0, it begins a new transaction. It then opens a cursor to iterate over the Depot Authorization data.

For each row in the cursor:
1. Check if the user has access to update the information.
2. Validate the workflow ID and status ID.
3. Check for conflicts with other TARs or power zones.
4. Update the workflow status based on the new values.
5. Insert a new workflow if necessary.
6. Update the Depot Authorization data.

If any errors occur during this process, the procedure rolls back the transaction and sets @success to 0. Otherwise, it commits the transaction and sets @success to 1.

### Data Interactions
* Reads: TAMS_Depot_Auth, TAMS_WFStatus, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Powerzone, TAMS_Track_Power_Sector, TAMS_Track_SPKSZone, TAMS_Power_Sector, TAMS_User, TAMS_Endorser
* Writes: TAMS_Depot_Auth, TAMS_WFStatus, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Powerzone

---


<a id='database-reference-sql-sp-tams-depot-updatedtcauthbatch20250120'></a>
# Procedure: sp_TAMS_Depot_UpdateDTCAuthBatch20250120

### Purpose
This stored procedure updates the Depot Authorization module for a batch of users.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @success | bit | Output parameter indicating success or failure |
| @Message | NVARCHAR(500) | Output parameter containing error message if any |

### Logic Flow

1. The procedure starts by setting the transaction count to 0 and declaring a variable `@IntrnlTrans` to track whether an internal transaction is being performed.
2. It then checks if there are any open transactions, and if not, sets `@IntrnlTrans` to 1.
3. The procedure opens a cursor `C` that selects the required columns from the `TAMS_DTC_AUTH` table.
4. The cursor fetches each row one by one, and for each row:
   - It checks if the user has access to update the information by checking if they are in the roster role or have the necessary permissions.
   - If not, it sets an error message and skips to the next iteration of the loop.
   - It then updates the workflow status based on the current status ID.
   - Depending on the new status ID, it performs different actions such as updating the power zone status, setting the protect off timing, or inserting a new workflow.
5. If any errors occur during this process, the procedure rolls back the transaction and sets `@success` to 0.
6. Finally, if no errors occurred, the procedure commits the transaction, sets `@success` to 1, and returns.

### Data Interactions
* **Reads:** TAMS_DTC_AUTH, TAMS_WFStatus, TAMS_Roster_Role, TAMS_OCC_Duty_Roster, TAMS_User, TAMS_Endorser, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Powerzone, TAMS_Depot_DTCAuth_SPKS
* **Writes:** TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow, TAMS_Depot_Auth_Powerzone, TAMS_Depot_DTCAuth_SPKS

---


<a id='database-reference-sql-sp-tams-email-apply-late-tar'></a>
# Procedure: sp_TAMS_Email_Apply_Late_TAR

### Purpose
This stored procedure applies a late TAR (Track Access Management System) email to an applicant or department, depending on the specified actor.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @EType | INTEGER | Specifies whether the email is for an Applicant HOD Acceptance or another type of endorsement. |
| @AppDept | NVARCHAR(200) | The department that applied for the late TAR. |
| @TARNo | NVARCHAR(50) | The unique identifier for the late TAR. |
| @Actor | NVARCHAR(100) | The actor who is being notified (e.g., Applicant HOD Endorsement, TAP HOD Endorsement, etc.). |
| @ToSend | NVARCHAR(1000) | The list of recipients to send the email to. |
| @CCSend | NVARCHAR(1000) | The list of CC recipients for the email. |
| @Message | NVARCHAR(500) | Output parameter that stores the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has already been started and sets an internal flag accordingly.
2. It initializes several variables to store the sender, system ID, subject, greetings, list of recipients, CC list, BCC list, separator, alert message, and alert ID.
3. Based on the specified @EType and @Actor values, it generates a unique subject for the email.
4. The procedure constructs three tables (body1, body2, body3) to format the email content, including a table with department information, a link to access the TAR Form, and a signature.
5. It executes an external stored procedure [dbo].EAlertQ_EnQueue to send the email, passing in the generated message, sender, system ID, subject, greetings, alert message, recipients, CC list, BCC list, separator, and alert ID as parameters.
6. If any errors occur during execution, it sets a message variable with an error message and exits the procedure.
7. Otherwise, it commits or rolls back the transaction based on the internal flag and returns the generated email message.

### Data Interactions
* Reads: None explicitly selected from tables.
* Writes:
	+ TAMS_TAR (inserting or updating)
	+ EAlertQ_EnQueue (inserting)

---


<a id='database-reference-sql-sp-tams-email-apply-urgent-tar'></a>
# Procedure: sp_TAMS_Email_Apply_Urgent_TAR

### Purpose
This stored procedure applies an urgent TAR (Track Access Management System) email to various stakeholders, including Applicant HOD Acceptance, TAP HOD Endorsement, Power Endorsement, and others. It generates a personalized email with the required details and sends it to the specified recipients.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @EType | INTEGER | The type of email being sent (e.g., Urgent TAR for Applicant HOD Acceptance) |
| @AppDept | NVARCHAR(200) | The department of the applicant |
| @TARNo | NVARCHAR(50) | The TAR number |
| @Actor | NVARCHAR(100) | The actor performing the action (e.g., Applicant HOD Endorsement) |
| @ToSend | NVARCHAR(1000) | The list of recipients to send the email to |
| @CCSend | NVARCHAR(1000) | The list of CC recipients to send the email to |
| @Message | NVARCHAR(500) | The output parameter that stores the generated email message |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets an internal transaction flag and begins a new transaction.
2. It initializes several variables, including the sender's name, system ID, subject line, greetings, and body content.
3. Based on the @EType parameter, it generates the subject line and body content for the email. The subject line includes the TAR number and the actor performing the action.
4. It populates the body content with tables containing relevant information, such as the applicant's department and a link to access the TAR Form via Intranet or Internet.
5. It executes an external stored procedure (EAlertQ_EnQueue) to send the email to the specified recipients.
6. If any errors occur during the execution of EAlertQ_EnQueue, it rolls back the transaction and returns an error message.
7. Otherwise, it commits the transaction and returns the generated email message.

### Data Interactions
* Reads: TAMS_Parameters table (to retrieve the URL parameter value)
* Writes: TAMS_TAR table (to insert or update a new TAR record)

---


<a id='database-reference-sql-sp-tams-email-apply-urgent-tar-20231009'></a>
# Procedure: sp_TAMS_Email_Apply_Urgent_TAR_20231009

### Purpose
This stored procedure applies an urgent TAR (Track Access Management System) email to various stakeholders, including the applicant HOD acceptance, TAP HOD endorsement, power endorsement, TAP authority verification, and OCC approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @EType	| INTEGER | The type of email being sent (1 for urgent TAR) |
| @AppDept	| NVARCHAR(200) | The department of the applicant |
| @TARNo	| NVARCHAR(50) | The TAR number |
| @Actor	| NVARCHAR(100) | The actor performing the action (e.g. Applicant HOD Endorsement) |
| @ToSend	| NVARCHAR(1000) | The list of recipients to send the email to |
| @CCSend	| NVARCHAR(1000) | The list of CC recipients to send the email to |
| @Message	| NVARCHAR(500) | The output message |

### Logic Flow
1. The procedure starts by checking if a transaction has been started. If not, it sets a flag and begins a new transaction.
2. It then initializes variables for the sender, system ID, subject, greetings, list of recipients, CC list, BCC list, separator, alert message, and alert ID.
3. Based on the email type (@EType), it sets the subject accordingly.
4. It constructs the body of the email by concatenating three tables: one with the applicant's department information, another with login instructions, and a third with a disclaimer.
5. The procedure then executes an EAlertQ_EnQueue stored procedure to send the email to the specified recipients.
6. If any errors occur during this process, it rolls back the transaction and returns an error message.
7. Otherwise, it commits the transaction and returns the output message.

### Data Interactions
* Reads: TAMS_Parameters table (to retrieve the URL parameter value)
* Writes: TAMS_TAR table (to insert or update a new email)

---


<a id='database-reference-sql-sp-tams-email-cancel-tar'></a>
# Procedure: sp_TAMS_Email_Cancel_TAR

### Purpose
This stored procedure sends an email notification to a list of recipients when a TAR (Track Access Management System) record is cancelled.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR record being cancelled. |
| @TARStatus | NVARCHAR(20) | The status of the TAR record (e.g., "CANCELLED"). |
| @TARNo | NVARCHAR(50) | The number associated with the TAR record. |
| @ToSend | NVARCHAR(1000) | The list of recipients to send the email to. |
| @Message | NVARCHAR(500) | Output parameter that stores the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has already been started. If not, it starts one.
2. It initializes an internal transaction flag and sets the output parameter @Message to an empty string.
3. The procedure declares several variables to store email content, including sender information, subject, body, and links.
4. It populates these variables with default values or user-provided input (if available).
5. The procedure executes a stored procedure [dbo].EAlertQ_EnQueue to send the email notification to the specified recipients.
6. If any errors occur during this process, it rolls back the internal transaction and returns an error message.
7. Otherwise, it commits the internal transaction and returns the generated email message.

### Data Interactions
* Reads: None explicitly listed; however, the procedure interacts with the [dbo].EAlertQ_EnQueue stored procedure, which likely reads data from a database table to retrieve recipient information.
* Writes: The procedure writes data to the following tables:
	+ TAMS_TAR (to update the TAR record)
	+ [dbo].EAlertQ_EnQueue (to insert or update email notification records)

---


<a id='database-reference-sql-sp-tams-email-companyregistrationlinkbyregid'></a>
# Procedure: sp_TAMS_Email_CompanyRegistrationLinkByRegID

### Purpose
This stored procedure generates an email link for a company registration, which can be used to register the company details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | NVARCHAR(200) | The ID of the registered company. |

### Logic Flow
1. The procedure checks if a record exists in the TAMS_Registration table with the provided RegID.
2. If a record is found, it retrieves various parameters such as sender information, subject, greetings, and email list from the database.
3. It constructs an email body by combining three parts: a link to register the company details, a login page URL, and system-generated text.
4. The procedure then sends the email using the EAlertQ_EnQueue stored procedure.

### Data Interactions
* **Reads:** TAMS_Registration table
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-email-late-tar'></a>
# Procedure: sp_TAMS_Email_Late_TAR

### Purpose
This stored procedure sends an email notification to stakeholders regarding a late TAR (Track Access Management System) status update.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the late TAR being notified. |
| @TARStatus | NVARCHAR(20) | The current status of the late TAR (e.g., Approved, Rejected, Cancelled). |
| @TARNo | NVARCHAR(50) | The number associated with the late TAR. |
| @Remarks | NVARCHAR(1000) | Additional remarks about the late TAR. |
| @Actor | NVARCHAR(100) | The actor who endorsed or approved the late TAR (e.g., Applicant HOD Endorsement, TAP HOD Endorsement). |
| @ToSend | NVARCHAR(1000) | The list of stakeholders to whom the email should be sent. |
| @Message | NVARCHAR(500) | Output parameter that stores the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has already been started. If not, it begins a new transaction.
2. It initializes an internal transaction flag and sets the output parameter @Message to an empty string.
3. The procedure declares several variables to store sender information, system ID, subject, greetings, list of recipients, CC list, BCC list, separator, alert message, and alert ID.
4. Based on the value of @Actor, it updates the subject line accordingly.
5. It constructs the email body by concatenating three tables: one for remarks, another for a link to access the TAR Form, and a third with a disclaimer.
6. The procedure executes an external stored procedure [dbo].EAlertQ_EnQueue to enqueue the alert message and send it to the specified stakeholders.
7. If any errors occur during this process, it sets @Message to an error message and exits the transaction.
8. Otherwise, it commits the transaction if an internal transaction was started.

### Data Interactions
* Reads: None explicitly selected from tables.
* Writes:
	+ TAMS_TAR (for storing the alert message)
	+ TAMS_TARID (for storing the TAR ID)

---


<a id='database-reference-sql-sp-tams-email-late-tar-occ'></a>
# Procedure: sp_TAMS_Email_Late_TAR_OCC

### Purpose
This stored procedure sends an email notification to users regarding a late TAR (Track Access Management System) that has been approved, rejected, or cancelled by CC.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the late TAR. |
| @TARStatus | NVARCHAR(20) | The status of the late TAR (Approved, Rejected, or Cancelled). |
| @TARNo | NVARCHAR(50) | The number of the late TAR. |
| @Remarks | NVARCHAR(1000) | Any remarks about the late TAR. |
| @ToSend | NVARCHAR(1000) | The list of users to send the email to. |
| @Message | NVARCHAR(500) | Output parameter that stores the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has already started and sets an internal flag accordingly.
2. It initializes variables for the sender, system ID, subject, greetings, list of users to send to, CC list, BCC list, separator, alert message, and alert ID.
3. Based on the TAR status, it generates three parts of the email body: a table with remarks, a link to access the TAR form, and a signature.
4. The procedure executes an external stored procedure `EAlertQ_EnQueue` to send the email notification using the generated message.
5. If any errors occur during execution, it rolls back the transaction and returns an error message.
6. Otherwise, it commits the transaction and returns the generated email message.

### Data Interactions
* Reads: None explicitly selected from tables.
* Writes: Inserts/updates data in the `TAMS_TAR` table (not shown in this code snippet).

---


<a id='database-reference-sql-sp-tams-email-passwordresetlinkbyregid'></a>
# Procedure: sp_TAMS_Email_PasswordResetLinkByRegID

### Purpose
This stored procedure generates an email with a password reset link for a specified user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(200) | The ID of the user to generate the email for. |

### Logic Flow
1. The procedure checks if a user with the specified ID exists in the TAMS_User table.
2. If the user exists, it sets various variables such as the sender's name, system ID, subject, greetings, and body content for the email.
3. It constructs the password reset link using the provided cipher value.
4. The procedure then executes an external stored procedure, EAlertQ_EnQueue, to send the email with the constructed body content.

### Data Interactions
* **Reads:** TAMS_User table (to retrieve user data)
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-email-signupstatuslinkbyloginid'></a>
# Procedure: sp_TAMS_Email_SignUpStatusLinkByLoginID

### Purpose
This stored procedure generates an email link for a user to view their sign-up status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(200) | The login ID of the user. |

### Logic Flow
1. The procedure checks if a registration record exists for the given login ID.
2. If a record is found, it retrieves the email addresses associated with that login ID.
3. It constructs an email body with a link to view the sign-up status and other relevant information.
4. The procedure then sends this email using the EAlertQ_EnQueue stored procedure.

### Data Interactions
* **Reads:** TAMS_Registration table (to retrieve registration records for the given login ID)
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-email-signupstatuslinkbyloginid-20231009'></a>
# Procedure: sp_TAMS_Email_SignUpStatusLinkByLoginID_20231009

### Purpose
This stored procedure generates an email link for a user to view their sign-up status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(200) | The login ID of the user. |

### Logic Flow
1. The procedure checks if a registration record exists for the given login ID.
2. If a record is found, it retrieves the email addresses associated with that login ID.
3. It constructs an email body with a link to view the sign-up status and other relevant information.
4. The procedure then sends this email using the EAlertQ_EnQueue stored procedure.

### Data Interactions
* **Reads:** TAMS_Registration table (to retrieve registration record for the given login ID)
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-email-urgent-tar'></a>
# Procedure: sp_TAMS_Email_Urgent_TAR

### Purpose
This stored procedure sends an urgent email to stakeholders regarding a TAR (Track Access Management System) status update.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR being updated. |
| @TARStatus | NVARCHAR(20) | The current status of the TAR. |
| @TARNo | NVARCHAR(50) | The number associated with the TAR. |
| @Remarks | NVARCHAR(1000) | Additional remarks about the TAR update. |
| @Actor | NVARCHAR(100) | The actor who performed the action on the TAR. |
| @ToSend | NVARCHAR(1000) | The list of recipients to send the email to. |
| @Message | NVARCHAR(500) | Output parameter that stores the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has been started and sets an internal flag accordingly.
2. It initializes variables for the sender, system ID, subject, greetings, list of recipients, CC list, BCC list, separator, alert message, and body parts.
3. Based on the actor who performed the action, it updates the subject line with the corresponding title (e.g., "Applicant HOD" or "TAP Verifier").
4. It constructs the email body by combining three table elements: a remark section, a login link section, and a closing message section.
5. The procedure executes an external stored procedure `EAlertQ_EnQueue` to enqueue the alert message with the specified sender, system ID, subject, greetings, alert message, recipients, CC list, BCC list, separator, and alert ID output parameter.
6. If any errors occur during execution, it rolls back the transaction and returns an error message.
7. Otherwise, it commits the transaction and returns the generated email message.

### Data Interactions
* Reads: TAMS_Parameters table to retrieve the URL parameter value.
* Writes: TAMS_TAR table (not explicitly mentioned in the procedure but implied by the context).

---


<a id='database-reference-sql-sp-tams-email-urgent-tar-20231009'></a>
# Procedure: sp_TAMS_Email_Urgent_TAR_20231009

### Purpose
This stored procedure sends an urgent email notification to stakeholders regarding a TAR (Track Access Management System) status update.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| INTEGER | The ID of the TAR being updated. |
| @TARStatus	| NVARCHAR(20) | The current status of the TAR (e.g., Approved, Rejected, Cancelled). |
| @TARNo	| NVARCHAR(50) | The number associated with the TAR. |
| @Remarks	| NVARCHAR(1000) | Additional remarks about the TAR update. |
| @Actor	| NVARCHAR(100) | The actor who performed the action (e.g., Applicant HOD Endorsement, TAP HOD Endorsement). |
| @ToSend	| NVARCHAR(1000) | The list of stakeholders to send the email to. |
| @Message	| NVARCHAR(500) | Output parameter that stores the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has already started and sets an internal flag accordingly.
2. It initializes variables for the sender, system ID, subject, greetings, list of stakeholders, CC list, BCC list, separator, alert message, and alert ID.
3. Based on the actor performing the action, it updates the subject line to include the actor's name.
4. The procedure generates the email body by concatenating three tables: a remark table, a login link table, and an alert message table.
5. It executes the EAlertQ_EnQueue stored procedure to enqueue the email notification.
6. If any errors occur during execution, it rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_Parameters (to retrieve the URL parameter value)
* Writes: None

---


<a id='database-reference-sql-sp-tams-email-urgent-tar-occ'></a>
# Procedure: sp_TAMS_Email_Urgent_TAR_OCC

### Purpose
This stored procedure sends an urgent email to a list of recipients regarding a TAR (Track Access Management System) occurrence.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR occurrence. |
| @TARStatus | NVARCHAR(20) | The status of the TAR occurrence (e.g., Approved, Rejected, Cancelled). |
| @TARNo | NVARCHAR(50) | The number of the TAR occurrence. |
| @Remarks | NVARCHAR(1000) | Additional remarks about the TAR occurrence. |
| @ToSend | NVARCHAR(1000) | The list of recipients to send the email to. |
| @Message | NVARCHAR(500) | The output parameter that will contain the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has already been started and sets an internal flag accordingly.
2. It initializes variables for the sender, system ID, subject, greetings, list of recipients, CC list, BCC list, separator, alert message, and alert ID.
3. It retrieves the login page URLs from the TAMS parameters table based on the 'TAMS URL' parameter code.
4. The procedure generates the email body by concatenating three tables: one for the TAR occurrence status, another for the login page links, and a third for the system greetings and disclaimers.
5. It executes an EAlertQ_EnQueue stored procedure to enqueue the alert message with the specified sender, subject, and recipients.
6. If any errors occur during the execution of the EAlertQ_EnQueue procedure, it sets the output parameter @Message to an error message and exits the transaction.
7. Otherwise, it commits the transaction if one was started and returns the generated email message.

### Data Interactions
* Reads: TAMS_Parameters table (to retrieve login page URLs)
* Writes: TAMS_TAR table (not explicitly mentioned in the procedure, but implied by the use of TARID)

---


<a id='database-reference-sql-sp-tams-email-urgent-tar-occ-20231009'></a>
# Procedure: sp_TAMS_Email_Urgent_TAR_OCC_20231009

### Purpose
This stored procedure sends an urgent email notification to stakeholders regarding a TAR (Track Access Management System) occurrence.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | INTEGER | The ID of the TAR occurrence. |
| @TARStatus | NVARCHAR(20) | The status of the TAR occurrence (e.g., Approved, Rejected, Cancelled). |
| @TARNo | NVARCHAR(50) | The number associated with the TAR occurrence. |
| @Remarks | NVARCHAR(1000) | Additional remarks about the TAR occurrence. |
| @ToSend | NVARCHAR(1000) | The list of recipients to send the email to. |
| @Message | NVARCHAR(500) | The output parameter that will contain the generated email message. |

### Logic Flow
1. The procedure checks if a transaction has been started and sets an internal flag (@IntrnlTrans) accordingly.
2. It initializes variables for the sender, system ID, subject, greetings, list of recipients (ToList), CC list, BCC list, separator, alert message, and alert ID.
3. It retrieves the login page URLs from the TAMS Parameters table based on the 'TAMS URL' parameter code.
4. The procedure generates the email body by concatenating three tables: one for the TAR occurrence details, another for the login page links, and a third for the system greetings and disclaimers.
5. It executes the EAlertQ_EnQueue stored procedure to enqueue the alert message with the specified sender, subject, greetings, and recipients.
6. If an error occurs during the execution of the EAlertQ_EnQueue procedure, it sets the @Message output parameter to an error message and exits the transaction.
7. Otherwise, it commits the transaction if a transaction was started.

### Data Interactions
* Reads: TAMS_Parameters table (for retrieving login page URLs)
* Writes: TAMS_TAR table (not explicitly mentioned in the procedure, but implied by the email notification)

---


<a id='database-reference-sql-sp-tams-form-cancel'></a>
# Procedure: sp_TAMS_Form_Cancel

### Purpose
This stored procedure cancels a TAMS form by deleting its associated records from the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS form to be cancelled. |

### Logic Flow
1. The procedure starts by setting default values for the TARID and error message variables.
2. It then checks if a transaction is already in progress, and if not, it begins a new transaction.
3. The procedure deletes the records from the TAMS_TAR table where the Id matches the provided TARID.
4. Next, it deletes the temporary attachment records for the same TARID.
5. If any errors occur during this process, an error message is set and the procedure jumps to the TRAP_ERROR label.
6. If no errors occurred, the procedure commits the transaction (if one was started) and returns the error message.
7. If an error did occur, the procedure rolls back the transaction and also returns the error message.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** TAMS_TAR table, TAMS_TAR_Attachment_Temp table

---


<a id='database-reference-sql-sp-tams-form-delete-temp-attachment'></a>
# Procedure: sp_TAMS_Form_Delete_Temp_Attachment

### Purpose
This stored procedure deletes a temporary attachment record from the TAMS_TAR_Attachment_Temp table based on the provided TARId and TARAccessReqId.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARId | INTEGER | The ID of the attachment to be deleted. |
| @TARAccessReqId | INTEGER | The access request ID associated with the attachment to be deleted. |

### Logic Flow
1. The procedure starts by declaring a variable @ret to store the return value.
2. It then attempts to begin a transaction, which will ensure that either all changes are committed or none are if an error occurs.
3. Within the transaction block, it deletes the specified attachment record from the TAMS_TAR_Attachment_Temp table based on the provided TARId and TARAccessReqId.
4. If the deletion is successful, the procedure commits the transaction, making the changes permanent.
5. If any errors occur during the deletion process, the procedure catches the exception, prints an error message, rolls back the transaction to maintain data consistency, and sets @ret to 'Error'.
6. Finally, the procedure selects the value of @ret as the return value.

### Data Interactions
* **Reads:** TAMS_TAR_Attachment_Temp table
* **Writes:** TAMS_TAR_Attachment_Temp table

---


<a id='database-reference-sql-sp-tams-form-onload'></a>
# Procedure: sp_TAMS_Form_OnLoad

### Purpose
This stored procedure performs a series of tasks to prepare data for form loading, including retrieving parameters, access requirements, and sector information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number. |
| @TrackType | NVARCHAR(50) | The track type. |
| @AccessDate | NVARCHAR(20) | The access date. |
| @AccessType | NVARCHAR(20) | The access type. |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sector IDs. |
| @PowerSelTxt | NVARCHAR(100) | The power selection text. |

### Logic Flow
1. Retrieve parameters from TAMS_Parameters based on the line number and access date.
2. Retrieve access requirements from TAMS_Access_Requirement based on the line number, track type, and access date.
3. If the access type is 'Protection', retrieve additional access requirements with specific conditions.
4. Otherwise, retrieve all access requirements without the protection condition.
5. Retrieve sector information from TAMS_Type_Of_Work based on the line number and track type.
6. Declare variables to store selected sectors that are not gaps and those that are gaps.
7. Populate these variables by selecting sectors from TAMS_Sector where the ID is in the list of provided sector IDs.
8. Select entry stations from TAMS_Station where the sector ID is in the list of provided sector IDs.
9. Create a temporary table to store power sector information and populate it with selected sectors.
10. Retrieve power on/off information for each sector.

### Data Interactions
* Reads: 
	+ TAMS_Parameters
	+ TAMS_Access_Requirement
	+ TAMS_Type_Of_Work
	+ TAMS_Sector
	+ TAMS_Station
* Writes: None

---


<a id='database-reference-sql-sp-tams-form-save-access-details'></a>
# Procedure: sp_TAMS_Form_Save_Access_Details

### Purpose
This stored procedure saves access details for a TAMS form, including user information and form submission data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the form being submitted. |
| @TrackType | NVARCHAR(50) | The type of track for the form. |
| @AccessDate | NVARCHAR(20) | The date and time the form was accessed. |
| @AccessType | NVARCHAR(20) | The type of access granted to the user. |
| @TARType | NVARCHAR(10) | The type of TAMS TAR being submitted. |
| @Company | NVARCHAR(50) | The company associated with the TAMS TAR. |
| @Designation | NVARCHAR(50) | The designation for the TAMS TAR. |
| @Name | NVARCHAR(50) | The name of the user submitting the form. |
| @OfficeNo | NVARCHAR(50) | The office number of the user submitting the form. |
| @MobileNo | NVARCHAR(50) | The mobile number of the user submitting the form. |
| @Email | NVARCHAR(50) | The email address of the user submitting the form. |
| @AccessTimeFrom | NVARCHAR(50) | The start time of the access period. |
| @AccessTimeTo | NVARCHAR(50) | The end time of the access period. |
| @AccessLocation | NVARCHAR(50) | The location where the form was accessed. |
| @IsNeutralGap | INT | A flag indicating whether a neutral gap is present. |
| @IsExclusive | INT | A flag indicating whether the TAMS TAR is exclusive. |
| @DescOfWork | NVARCHAR(100) | A description of the work being done. |
| @ARRemark | NVARCHAR(1000) | Additional remarks for the TAMS TAR. |
| @InvolvePower | INT | A flag indicating whether power involvement is required. |
| @PowerOn | INT | A flag indicating whether power on is required. |
| @Is13ASocket | INT | A flag indicating whether a 13A socket is present. |
| @CrossOver | INT | A flag indicating whether there is a crossover. |
| @UserID | NVARCHAR(100) | The ID of the user submitting the form. |
| @TARID | BIGINT OUTPUT | The ID of the newly created TAMS TAR. |
| @Message | NVARCHAR(500) OUTPUT | An error message if an issue occurs during submission. |

### Logic Flow
1. The procedure begins by setting the initial internal transaction count to 0.
2. It then checks if a transaction is already in progress and sets the internal transaction count accordingly.
3. If no transaction is present, it starts a new transaction.
4. The procedure retrieves the user ID from the TAMS_User table based on the provided login ID.
5. It inserts a new record into the TAMS_TAR table with the provided form data, including the current date and time as the submission date.
6. After inserting the record, it selects the newly generated TAMS TAR ID from the database.
7. If an error occurs during insertion, it sets an error message and exits the procedure.
8. Otherwise, it commits the transaction if one was started or returns a success message.

### Data Interactions
* Reads: TAMS_User table (for user ID retrieval)
* Writes: TAMS_TAR table (for form submission data)

---


<a id='database-reference-sql-sp-tams-form-save-access-reqs'></a>
# Procedure: sp_TAMS_Form_Save_Access_Reqs

### Purpose
This stored procedure saves access requirements for a specific form, updating the TAMS_TAR_AccessReq table with selected access requirements and saving remarks to the TAMS_TAR table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line			AS NVARCHAR(10) = NULL, |
| @TrackType		AS NVARCHAR(50) = NULL, |
| @SelAccessReqs	AS NVARCHAR(200) = NULL, |
| @PowerSelVal	AS NVARCHAR(10) = NULL, |
| @PowerSelTxt	AS NVARCHAR(100) = NULL, |
| @ARRemarks		AS NVARCHAR(1000) = NULL, |
| @TARID			AS BIGINT = 0, |
| @Message		AS NVARCHAR(500) = NULL OUTPUT |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it sets the internal transaction flag to 1 and begins a new transaction.
2. It then checks if there are any existing access requirements for the specified TARID. If not, it inserts a new set of access requirements into TAMS_TAR_AccessReq.
3. Next, it updates the IsSelected field in TAMS_TAR_AccessReq to 1 for all access requirements that match the selected power selection value or are part of the specified access requirements list.
4. It also updates the TARRemark field in TAMS_TAR to the provided ARRemarks value for the specified TARID.
5. If any errors occur during the procedure, it sets the @Message output parameter with an error message and either commits or rolls back the transaction depending on whether an error occurred.

### Data Interactions
* **Reads:** TAMS_Access_Requirement table, TAMS_TAR_AccessReq table, TAMS_TAR table
* **Writes:** TAMS_TAR_AccessReq table, TAMS_TAR table

---


<a id='database-reference-sql-sp-tams-form-save-possession'></a>
# Procedure: sp_TAMS_Form_Save_Possession

### Purpose
This stored procedure saves a possession record for a train (TAMs) into the database, including various details such as work description, type of work, and possession status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the train (TAMs) for which the possession record is being saved. |
| @Summary | NVARCHAR(1000) | A summary of the work description. |
| @WorkDesc | NVARCHAR(1000) | The detailed work description. |
| @TypeOfWorkId | INT | The ID of the type of work being performed. |
| @WorkWithinPossession | NVARCHAR(1000) | Information about the work within possession. |
| @TakePossession | NVARCHAR(1000) | Details about taking possession. |
| @GiveUpPossession | NVARCHAR(1000) | Details about giving up possession. |
| @Remarks | NVARCHAR(1000) | Any additional remarks or comments. |
| @PowerOnOff | INT | The power on/off status of the train. |
| @EngTrainFormation | NVARCHAR(50) | Information about the engine train formation. |
| @EngTrainArriveLoc | NVARCHAR(50) | Location of the engine train arrival. |
| @EngTrainArriveTime | NVARCHAR(10) | Time of engine train arrival. |
| @EngTrainDepartLoc | NVARCHAR(50) | Location of the engine train departure. |
| @EngTrainDepartTime | NVARCHAR(10) | Time of engine train departure. |
| @PCNRIC | NVARCHAR(50) | The PCNRIC (Personal Computerized National Registration Identification Card) number. |
| @PCName | NVARCHAR(100) | The name associated with the PCNRIC number. |
| @PossID | BIGINT OUTPUT | The ID of the newly saved possession record. |
| @Message | NVARCHAR(500) OUTPUT | Any error message or success message to be returned. |

### Logic Flow
1. Initialize variables and set the output parameter `@PossID` to 0.
2. Check if a transaction has already been started. If not, start a new transaction.
3. Insert the possession record into the `TAMS_Possession` table with all provided details.
4. Retrieve the ID of the newly saved possession record from the database using `SCOPE_IDENTITY()`.
5. Check for any errors during insertion. If an error occurs, set the output parameter `@Message` to an error message and exit the procedure.
6. If no errors occurred, commit the transaction and return the success message.
7. If an error occurred, roll back the transaction and return the error message.

### Data Interactions
* **Reads:** None explicitly selected from tables.
* **Writes:** The `TAMS_Possession` table is inserted with all provided details.

---


<a id='database-reference-sql-sp-tams-form-save-possession-depotsector'></a>
# Procedure: sp_TAMS_Form_Save_Possession_DepotSector

### Purpose
This stored procedure saves a possession depot sector record to the database, updating or inserting it based on whether a matching record already exists.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Sector	| NVARCHAR(4000) | The sector value to be saved. |
| @PowerOff	| INT | The power off status of the possession depot sector. |
| @NoOFSCD	| INT | The number of SCDs in the possession depot sector. |
| @BreakerOut	| NVARCHAR(5) | The breaker out status of the possession depot sector. |
| @PossID			| BIGINT | The ID of the possession to be associated with the depot sector. |
| @Message		| NVARCHAR(500) | An output parameter containing a message indicating whether the operation was successful or not. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag to 0.
2. If no transactions are currently active, it sets the flag to 1 and begins a new transaction.
3. It then checks if a matching record for the given possession ID and sector already exists in the TAMS_Possession_DepotSector table.
4. If no matching record is found, it inserts a new record into the table with the provided values.
5. If an error occurs during insertion, it sets the @Message parameter to an error message and rolls back the transaction if one was active.
6. Otherwise, it commits the transaction and returns the @Message parameter.

### Data Interactions
* **Reads:** [dbo].[TAMS_Possession_DepotSector]
* **Writes:** [dbo].[TAMS_Possession_DepotSector]

---


<a id='database-reference-sql-sp-tams-form-save-possession-limit'></a>
# Procedure: sp_TAMS_Form_Save_Possession_Limit

### Purpose
This stored procedure saves a new possession limit record to the TAMS_Possession_Limit table if no existing record is found for the specified PossID, TypeOfProtectionLimit, and RedFlashingLampsLoc.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TypeOfProtectionLimit | NVARCHAR(50) | The type of protection limit to be saved. |
| @RedFlashingLampsLoc | NVARCHAR(50) | The location of the red flashing lamps. |
| @PossID | BIGINT | The ID of the possession for which the limit is being saved. |
| @Message | NVARCHAR(500) | An output parameter that contains an error message if any. |

### Logic Flow
1. The procedure checks if a transaction has already been started by checking the @@TRANCOUNT system variable.
2. If no transaction exists, it starts a new one and sets a flag to indicate this.
3. It then checks if an existing record is found in the TAMS_Possession_Limit table for the specified PossID, TypeOfProtectionLimit, and RedFlashingLampsLoc.
4. If no record is found, it inserts a new record into the TAMS_Possession_Limit table with the provided values.
5. If an error occurs during the insertion process, it sets the @Message parameter to an error message and jumps to the TRAP_ERROR label.
6. After successfully inserting or not finding a record, the procedure checks if any errors occurred. If so, it rolls back the transaction and returns the error message. Otherwise, it commits the transaction and returns the saved @Message value.

### Data Interactions
* **Reads:** [dbo].[TAMS_Possession_Limit]
* **Writes:** [dbo].[TAMS_Possession_Limit]

---


<a id='database-reference-sql-sp-tams-form-save-possession-otherprotection'></a>
# Procedure: sp_TAMS_Form_Save_Possession_OtherProtection

### Purpose
This stored procedure saves a new possession with other protection details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OtherProtection | NVARCHAR(50) | The value of the other protection detail. |
| @PossID | BIGINT | The ID of the possession to be saved. |
| @Message | NVARCHAR(500) | An output parameter that stores any error message. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started.
2. If not, it sets a flag indicating that a transaction is in progress and begins a new transaction.
3. It then checks if the possession with the specified ID and other protection detail already exists in the database.
4. If no record is found, it inserts a new record into the TAMS_Possession_OtherProtection table with the provided possession ID and other protection detail.
5. After inserting or updating the record, it checks for any errors that may have occurred during this process.
6. If an error occurs, it sets the @Message parameter to indicate that there was an error inserting into TAMS_TAR.
7. Finally, if no errors occurred, it commits the transaction and returns the message in the @Message parameter.

### Data Interactions
* **Reads:** [dbo].[TAMS_Possession_OtherProtection]
* **Writes:** [dbo].[TAMS_Possession_OtherProtection]

---


<a id='database-reference-sql-sp-tams-form-save-possession-powersector'></a>
# Procedure: sp_TAMS_Form_Save_Possession_PowerSector

The procedure saves a new possession power sector record to the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PowerSector | NVARCHAR(4000) | The power sector value to be inserted. |
| @NoOFSCD | INT | The number of SCDs associated with this possession power sector. |
| @BreakerOut | NVARCHAR(5) | A flag indicating whether the breaker is out (Y) or not (N). |
| @PossID | BIGINT | The ID of the possession to which this power sector belongs. |
| @Message | NVARCHAR(500) | An output parameter containing an error message if any. |

### Logic Flow
1. The procedure checks if a transaction has already started by checking the @@TRANCOUNT variable.
2. If no transaction is in progress, it starts a new transaction and sets the internal transaction flag (@IntrnlTrans) to 1.
3. It then checks if a record with the same possession ID and power sector value already exists in the TAMS_Possession_PowerSector table.
4. If no such record exists, it inserts a new record into the table with the provided values.
5. After inserting or updating the record, it checks for any errors that may have occurred during the process.
6. If an error occurs, it sets the @Message parameter to an error message and exits the procedure.
7. If no errors occur, it commits the transaction (if one was started) and returns the @Message parameter.

### Data Interactions
* **Reads:** [dbo].[TAMS_Possession_PowerSector]
* **Writes:** [dbo].[TAMS_Possession_PowerSector]

---


<a id='database-reference-sql-sp-tams-form-save-possession-workinglimit'></a>
# Procedure: sp_TAMS_Form_Save_Possession_WorkingLimit

### Purpose
This stored procedure saves a new possession working limit record to the TAMS_Possession_WorkingLimit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RedFlashingLampsLoc | NVARCHAR(50) | The location of the red flashing lamps. |
| @PossID | BIGINT | The ID of the possession being saved. |
| @Message | NVARCHAR(500) | An output parameter that stores an error message if one occurs. |

### Logic Flow
1. The procedure checks if a transaction has already been started by checking the @@TRANCOUNT variable.
2. If no transaction is in progress, it starts a new transaction and sets the internal transaction flag to 1.
3. It then checks if a record with the same possession ID and red flashing lamps location already exists in the TAMS_Possession_WorkingLimit table.
4. If no such record exists, it inserts a new record into the table with the provided possession ID and red flashing lamps location.
5. After inserting or updating the record, the procedure checks if an error occurred during this process.
6. If an error did occur, it sets the @Message output parameter to an error message and exits the transaction.
7. If no errors occurred, the procedure commits the transaction and returns the @Message output parameter.
8. If an error did occur but a transaction was already in progress, the procedure rolls back the transaction and returns the @Message output parameter.

### Data Interactions
* **Reads:** [dbo].[TAMS_Possession_WorkingLimit]
* **Writes:** [dbo].[TAMS_Possession_WorkingLimit]

---


<a id='database-reference-sql-sp-tams-form-save-temp-attachment'></a>
# Procedure: sp_TAMS_Form_Save_Temp_Attachment

### Purpose
This stored procedure saves a temporary attachment to the TAMS database, creating a new record if one does not already exist for the specified TARId and TARAccessReqId.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARId | INTEGER | The ID of the TAR (Temporary Attachment Record) to save. |
| @TARAccessReqId | INTEGER | The ID of the access request for which the attachment is being saved. |
| @FileName | NVARCHAR(50) | The name of the file being uploaded. |
| @FileType | NVARCHAR(50) | The type of file being uploaded (e.g., image, document). |
| @FileUpload | VARBINARY(MAX) | The binary data of the file being uploaded. |

### Logic Flow
1. The procedure checks if a record already exists in TAMS_TAR_Attachment_Temp for the specified TARId and TARAccessReqId.
2. If no record exists, it inserts a new record into TAMS_TAR_Attachment_Temp with the provided file information.
3. Regardless of whether a new record is inserted or not, the procedure commits the transaction.
4. If any error occurs during the execution of the stored procedure, it prints an error message and rolls back the transaction.

### Data Interactions
* **Reads:** TAMS_TAR_Attachment_Temp table
* **Writes:** TAMS_TAR_Attachment_Temp table

---


<a id='database-reference-sql-sp-tams-form-submit'></a>
# Procedure: sp_TAMS_Form_Submit

### Purpose
This stored procedure submits a new TAR (Track Access Request) form for approval and updates the associated records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the track. |
| @TrackType | NVARCHAR(50) | The type of track. |
| @AccessDate | NVARCHAR(20) | The access date. |
| @AccessType | NVARCHAR(20) | The access type (e.g., Protection, Possession). |
| @TARType | NVARCHAR(10) | The type of TAR (e.g., Urgent). |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sector IDs. |
| @PowerSelVal | NVARCHAR(10) | The selected power value. |
| @PowerSelTxt | NVARCHAR(100) | The text description of the power selection. |
| @IsExclusive | INT | A flag indicating whether the TAR is exclusive. |
| @HODForApp | NVARCHAR(20) | The HOD login ID for the application. |
| @UserID | NVARCHAR(100) | The user ID submitting the form. |
| @TARID | BIGINT | The ID of the new TAR to be created. |
| @Message | NVARCHAR(500) | An output parameter containing a message about the result of the procedure. |

### Logic Flow
1. The procedure checks if there are any open transactions and sets an internal transaction flag accordingly.
2. It retrieves the user ID from the TAMS_User table based on the provided user ID.
3. If the access type is 'Protection' and the TAR is exclusive, it selects the sector color code from the TAMS_Type_Of_Work table.
4. The procedure inserts a new record into the TAMS_TAR_Sector table with the selected sector color code and other relevant details.
5. It inserts records into the TAMS_TAR_Station table based on the station IDs in the Sectors input parameter.
6. The procedure checks if there are any power sectors that need to be inserted, either for non-buffer or buffer zones, and inserts them accordingly.
7. If the TAR type is 'Urgent', it determines whether Saturday, Sunday, or PH should be considered and updates the workflow status accordingly.
8. It generates a reference number for the new TAR using the sp_Generate_Ref_Num stored procedure.
9. The procedure updates the TAMS_TAR table with the generated reference number, TAR type, and other relevant details.
10. If there are any errors during the process, it rolls back the transaction and returns an error message.

### Data Interactions
* Reads: TAMS_User, TAMS_Type_Of_Work, TAMS_Sector, TAMS_Station, TAMS_Power_Sector, TAMS_TAR, TAMS_Buffer_Zone, TAMS_Calendar, TAMS Paramaters, TAMS_Access_Requirement, TAMS_Endorser, TAMS_Workflow
* Writes: TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_Attachment, TAMS_TAR_Workflow

---


<a id='database-reference-sql-sp-tams-form-submit-20220930'></a>
# Procedure: sp_TAMS_Form_Submit_20220930

### Purpose
This stored procedure is used to submit a TAR (Track Access Management System) form for approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the TAR form being submitted. |

### Logic Flow
The procedure follows these steps:

1. It checks if a transaction has already been started, and if not, it starts one.
2. It retrieves the user ID from the TAMS_User table based on the provided @UserID parameter.
3. It determines the sector color code for the TAR form being submitted, depending on the access type and exclusive status.
4. It inserts new records into the TAMS_TAR_Sector table for each sector in the @Sectors parameter.
5. It inserts new records into the TAMS_TAR_Station table based on the stations associated with the TAR form.
6. It determines if a power sector is involved, and if so, it inserts a record into the TAMS_TAR_Power_Sector table.
7. It checks if the TAR form type is 'Late' and if so, it determines the workflow ID to use for approval.
8. It updates the TAR form with the determined workflow ID, TAR status ID, and other relevant information.
9. It inserts a new record into the TAMS_TAR_Workflow table to track the submission of the TAR form.
10. If the TAR form type is 'Late', it sends an email to the HOD (Head of Department) user with a link to access the TAR form.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Sector, TAMS_Station, TAMS_Power_Sector, TAMS_TAR, TAMS_Buffer_Zone, TAMS_Calendar, TAMS_Workflow, TAMS_Endorser, TAMS Paramaters.
* **Writes:** TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_Workflow.

---


<a id='database-reference-sql-sp-tams-form-submit-20250313'></a>
# Procedure: sp_TAMS_Form_Submit_20250313

### Purpose
This stored procedure is used to submit a new TAMS (Track Access Management System) form for review and approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the track. |
| @TrackType | NVARCHAR(50) | The type of track (e.g., NEL, OCC). |
| @AccessDate | NVARCHAR(20) | The access date of the track. |
| @AccessType | NVARCHAR(20) | The access type (e.g., Protection, Possession). |
| @TARType | NVARCHAR(10) | The type of TAMS form (e.g., Urgent, Standard). |

### Logic Flow
The procedure follows these steps:

1. It checks if a transaction has already started and sets the internal transaction flag accordingly.
2. It retrieves the user ID from the TAMS_User table based on the provided @UserID parameter.
3. It determines the sector color code for the track based on the access type and exclusive status.
4. It inserts new records into the TAMS_TAR_Sector table, which includes the sector ID, buffer flag, and color code.
5. It inserts new records into the TAMS_TAR_Station table, which includes the station ID.
6. It determines whether to insert non-buffer power sector or buffer power sector based on the power selection value.
7. It inserts new records into the TAMS_TAR_Power_Sector table, which includes the power sector ID and power section.
8. It retrieves the attachment files from the TAMS_TAR_Attachment_Temp table and inserts them into the TAMS_TAR_Attachment table.
9. If the access type is 'Possession', it determines whether to add a buffer zone or not based on the cross-over indicator.
10. It updates the TAMS_TAR table with the new values, including the TAR ID, track type, status ID, and power on value.
11. It inserts a new record into the TAMS_TAR_Workflow table, which includes the workflow ID, endorser ID, user ID, and workflow status.
12. If the access type is 'Urgent', it sends an email to the HOD (Head of Department) with a link to access the TAR form.

### Data Interactions
* Reads: TAMS_User, TAMS_Sector, TAMS_Track_Power_Sector, TAMS_Power_Sector, TAMS_TAR_Attachment_Temp, TAMS_TAR_Attachment, TAMS_Buffer_Zone, TAMS_TAMs, TAMS_Access_Requirement, TAMS_Workflow, TAMS Paramaters
* Writes: TAMS_TAR_Sector, TAMS_TAR_Station, TAMS_TAR_Power_Sector, TAMS_TAR_Attachment, TAMS_TAR, TAMS_TAR_Workflow

---


<a id='database-reference-sql-sp-tams-form-update-access-details'></a>
# Procedure: sp_TAMS_Form_Update_Access_Details

### Purpose
This stored procedure updates access details for a TAMS TAR record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Company | NVARCHAR(50) | Company name |
| @Designation | NVARCHAR(50) | Designation of the user |
| @Name | NVARCHAR(50) | User's name |
| @OfficeNo | NVARCHAR(50) | Office number of the user |
| @MobileNo | NVARCHAR(50) | Mobile number of the user |
| @Email | NVARCHAR(50) | Email address of the user |
| @AccessTimeFrom | NVARCHAR(50) | Start time of access |
| @AccessTimeTo | NVARCHAR(50) | End time of access |
| @IsExclusive | INT | Flag indicating exclusive access |
| @DescOfWork | NVARCHAR(100) | Description of work |
| @ARRemark | NVARCHAR(1000) | Additional remarks |
| @InvolvePower | INT | Flag indicating involvement with power |
| @PowerOn | INT | Flag indicating power on status |
| @Is13ASocket | INT | Flag indicating 13A socket usage |
| @CrossOver | INT | Flag indicating cross-over status |
| @UserID | NVARCHAR(100) | Login ID of the user |
| @TARID | BIGINT | ID of the TAMS TAR record to update |

### Logic Flow
1. The procedure starts by initializing a transaction flag and checking if a transaction is already in progress.
2. It then retrieves the Userid from the TAMS_User table based on the provided UserID.
3. The procedure updates the specified fields of the TAMS_TAR table with the new values, including the updated timestamp and user ID.
4. If any errors occur during the update process, an error message is set and the transaction is rolled back.
5. Otherwise, the transaction is committed and the procedure returns the error message.

### Data Interactions
* **Reads:** TAMS_User table (to retrieve Userid)
* **Writes:** TAMS_TAR table (to update access details)

---


<a id='database-reference-sql-sp-tams-getblockedtardates'></a>
# Procedure: sp_TAMS_GetBlockedTarDates

### Purpose
This stored procedure retrieves blocked TAR dates for a specific line, track type, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to retrieve blocked TAR dates for. |
| @TrackType | nvarchar(50) | The track type to filter by. |
| @AccessDate | date | The access date to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Block_TARDate table.
2. It filters the data based on the provided line number, track type, and access date.
3. Only records with an IsActive flag set to 1 are included in the results.
4. The selected data is ordered by BlockDate in ascending order.

### Data Interactions
* **Reads:** TAMS_Block_TARDate table

---


<a id='database-reference-sql-sp-tams-getdutyoccrosterbyparameters'></a>
# Procedure: sp_TAMS_GetDutyOCCRosterByParameters

### Purpose
This stored procedure retrieves a duty OCR roster by providing various parameters such as line, track type, operation date, shift, roster code, and ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter the roster by. |
| @TrackType | nvarchar(50) | The track type to filter the roster by. |
| @OperationDate | date | The operation date to filter the roster by. |
| @Shift | nvarchar(1) | The shift to filter the roster by. |
| @RosterCode | nvarchar(50) | The roster code to filter the roster by. |
| @ID | int | The ID of the duty OCR roster to retrieve. |

### Logic Flow
The procedure starts by selecting data from two tables: TAMS_OCC_Duty_Roster and TAMS_User. It filters the data based on the provided parameters, including line number, track type, operation date, shift, roster code, and ID. The procedure also checks if the duty OCR roster is active (IsActive = 1) before returning the results.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster and TAMS_User tables

---


<a id='database-reference-sql-sp-tams-getdutyoccrostercodebyparameters'></a>
# Procedure: sp_TAMS_GetDutyOCCRosterCodeByParameters

### Purpose
This stored procedure retrieves a list of duty OCR roster codes for a specific user, filtered by line, track type, operation date, shift, and active status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user to retrieve duty OCR roster codes for. |
| @Line | nvarchar(10) | The line number to filter by (optional). |
| @TrackType | nvarchar(50) | The track type to filter by (optional). |
| @OperationDate | date | The operation date to filter by. |
| @Shift | nvarchar(1) | The shift to filter by (optional). |

### Logic Flow
The procedure starts by selecting data from the TAMS_OCC_Duty_Roster and TAMS_User tables based on the provided parameters. It filters the results to include only active records with a non-'SCO' roster code.

1. The procedure begins by joining the TAMS_OCC_Duty_Roster table with the TAMS_User table on the DutyStaffId column.
2. It then applies the filter conditions for line, track type, operation date, shift, and user ID.
3. The results are limited to only include active records (IsActive = 1) and exclude any records with a roster code of 'SCO'.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_User

---


<a id='database-reference-sql-sp-tams-getdutyoccrostercodebyparametersfortvfack'></a>
# Procedure: sp_TAMS_GetDutyOCCRosterCodeByParametersForTVFAck

This procedure retrieves a list of duty roster codes for a specific TVF (Training and Verification Facility) based on provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user to filter by. |
| @Line | nvarchar(10) = NULL | The line number to filter by. |
| @TrackType | nvarchar(50) = NULL | The track type to filter by. |
| @OperationDate | date | The operation date to filter by. |
| @Shift | nvarchar(1) = NULL | The shift to filter by. |

### Logic Flow
The procedure starts by selecting data from the TAMS_OCC_Duty_Roster and TAMS_User tables based on the provided parameters. It filters the results to include only active records with a roster code that does not contain 'TC'. The final result set includes columns such as ID, Line, OperationDate, Shift, RosterCode, DutyStaffId, and DutyStaffName.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_User

---


<a id='database-reference-sql-sp-tams-getoccrosterbylineandrole'></a>
# Procedure: sp_TAMS_GetOCCRosterByLineAndRole

### Purpose
This stored procedure retrieves a list of users assigned to specific roles within the OCC (Operations Control Center) module, filtered by line and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter results by. |
| @TrackType | nvarchar(50) | The track type to filter results by. |
| @Role | nvarchar(50) | The role to filter results by. |

### Logic Flow
1. The procedure first determines the RoleID associated with the specified @Role.
2. It then selects users (u.userid, ur.Line, [name]) from TAMS_User and TAMS_User_Role, joined on UserID and RoleID, where the user is active and valid until the current date.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Roster_Role, TAMS_Role

---


<a id='database-reference-sql-sp-tams-getparametersbylineandtracktype'></a>
# Procedure: sp_TAMS_GetParametersByLineandTracktype

This procedure retrieves parameters from the TAMS_Parameters table based on a specific ParaCode, Line value, and TrackType.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParaCode | nvarchar(50) | The code of the parameter to retrieve. |
| @Line | nvarchar(350) | The line value associated with the parameter. |
| @TrackType | nvarchar(350) | The track type associated with the parameter. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Parameters table.
2. It filters the results based on the provided ParaCode, Line, and TrackType values.
3. The EffectiveDate and ExpiryDate columns are used to ensure that only parameters within their effective period are returned.
4. The results are ordered by the [Order] column in ascending order.

### Data Interactions
* **Reads:** TAMS_Parameters table

---


<a id='database-reference-sql-sp-tams-getparametersbyparacode'></a>
# Procedure: sp_TAMS_GetParametersByParaCode

### Purpose
This stored procedure retrieves parameters from the TAMS_Parameters table based on a provided ParaCode, filtering by effective and expiry dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | nvarchar(50) | The code of the parameter to retrieve |

### Logic Flow
1. The procedure starts by selecting all columns from the TAMS_Parameters table.
2. It filters the results to only include rows where the ParaCode matches the provided @ParaCode.
3. Additionally, it applies two date-based filters: EffectiveDate must be less than or equal to the current date, and ExpiryDate must be greater than or equal to the current date.
4. The final result is ordered by the [Order] column in ascending order.

### Data Interactions
* **Reads:** TAMS_Parameters table

---


<a id='database-reference-sql-sp-tams-getparametersbyparacodeandparavalue'></a>
# Procedure: sp_TAMS_GetParametersByParaCodeAndParaValue

This procedure retrieves parameters from the TAMS_Parameters table based on a provided ParaCode and ParaValue.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | nvarchar(50) | Specifies the ParaCode to filter by. |

### Logic Flow
1. The procedure starts by selecting all columns from the TAMS_Parameters table.
2. It filters the results based on the provided @ParaCode and @ParaValue, ensuring that both conditions are met.
3. Additionally, it applies date constraints: EffectiveDate must be less than or equal to the current date, and ExpiryDate must be greater than or equal to the current date.
4. The final step is to sort the results in ascending order by the [Order] column.

### Data Interactions
* **Reads:** TAMS_Parameters table

---


<a id='database-reference-sql-sp-tams-getparametersbyparacodeandparavaluewithtracktype'></a>
# Procedure: sp_TAMS_GetParametersByParaCodeAndParaValuewithTrackType

### Purpose
This stored procedure retrieves parameters from the TAMS_Parameters table based on a provided ParaCode, ParaValue, and TrackType.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | nvarchar(50) | Specifies the ParaCode to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Parameters table.
2. It filters the results based on the provided @ParaCode, ensuring that only rows with matching values are returned.
3. Additionally, it filters by the value of @TrackType, which must match a specific column in the table.
4. The results are further filtered to include only records where the EffectiveDate is less than or equal to the current date and the ExpiryDate is greater than or equal to the current date.
5. Finally, the results are ordered by the [Order] column in ascending order.

### Data Interactions
* **Reads:** TAMS_Parameters table

---


<a id='database-reference-sql-sp-tams-getrosterrolebyline'></a>
# Procedure: sp_TAMS_GetRosterRoleByLine

### Purpose
This stored procedure retrieves roster roles for a specific line, track type, operation date, and shift.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line to retrieve roster roles for. |
| @TrackType | nvarchar(50) | The track type to filter by. |
| @OperationDate | nvarchar(10) | The operation date to filter by. |
| @Shift | nvarchar(1) | The shift to filter by. |

### Logic Flow
The procedure first checks if the input line is 'DTL'. If it is, it retrieves a count of records from TAMS_OCC_Duty_Roster where the line, track type, and operation date match. If no records are found, it retrieves roster roles from TAMS_Roster_Role where the line, track type, and effective/expiry dates match. If records are found for 'DTL', it then checks if a shift is specified. If a shift is specified, it retrieves roster roles from TAMS_OCC_Duty_Roster with the matching shift. If no shift is specified or no records were found for 'DTL', it retrieves roster roles from TAMS_Roster_Role without the SCO code.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_Roster_Role

---


<a id='database-reference-sql-sp-tams-getsectorsbylineanddirection'></a>
# Procedure: sp_TAMS_GetSectorsByLineAndDirection

### Purpose
This stored procedure retrieves sectors from the TAMS_Sector table based on a specified line and direction, filtering by active status and effective dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter by. |
| @Direction | nvarchar(10) | The direction to filter by. |

### Logic Flow
1. The procedure checks if the provided line is 'DTL' or 'NEL'.
2. If either condition is met, it selects data from the TAMS_Sector table where the specified line and direction match.
3. The selected data is filtered to only include active records with effective dates within the current date range (EffectiveDate <= GETDATE() and ExpiryDate >= GETDATE).
4. The results are ordered by the [Order] column in ascending order.

### Data Interactions
* **Reads:** TAMS_Sector table

---


<a id='database-reference-sql-sp-tams-gettaraccessrequirementsbytarid'></a>
# Procedure: sp_TAMS_GetTarAccessRequirementsByTarId

### Purpose
This stored procedure retrieves access requirements for a specific Tar (Transportation Asset Management System) ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the Tar for which to retrieve access requirements. |

### Logic Flow
1. The procedure starts by selecting data from two tables: `tams_tar_accessreq` and `TAMS_Access_Requirement`.
2. It filters the results to only include rows where the `OperationRequirement` in `tams_tar_accessreq` matches the ID of the corresponding row in `TAMS_Access_Requirement`.
3. The procedure then further filters the results to only include rows where the `tarid` in `tams_tar_accessreq` matches the provided `@TarId`.
4. Finally, it selects specific columns from the filtered data and returns them.

### Data Interactions
* **Reads:** `tams_tar_accessreq`, `TAMS_Access_Requirement`
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-gettarapprovalsbytarid'></a>
# Procedure: sp_TAMS_GetTarApprovalsByTarId

### Purpose
This stored procedure retrieves a list of approvals for a specific TarId, including the ID, title, name, remark, and workflow status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the Tar to retrieve approvals for. |

### Logic Flow
1. The procedure starts by selecting data from three tables: TAMS_TAR_Workflow, TAMS_Endorser, and TAMS_User.
2. It filters the data based on the TARId, WorkflowId, ActionBy, and EndorserId columns.
3. The selected data is ordered by the ID column in ascending order.

### Data Interactions
* **Reads:** TAMS_TAR_Workflow, TAMS_Endorser, and TAMS_User

---


<a id='database-reference-sql-sp-tams-gettarbylineandtaraccessdate'></a>
# Procedure: sp_TAMS_GetTarByLineAndTarAccessDate

### Purpose
This stored procedure retrieves data from the TAMS_TAR table based on a specific line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter by. |
| @AccessDate | nvarchar(50) | The access date to filter by. |

### Logic Flow
1. The procedure starts by selecting all columns from the TAMS_TAR table.
2. It then filters the results based on two conditions:
	* The line number must match the value of the @Line parameter.
	* The access date must be equal to the converted datetime value of the @AccessDate parameter, using a specific format (103).
3. If both conditions are met, the procedure returns the corresponding row from the TAMS_TAR table.

### Data Interactions
* **Reads:** TAMS_TAR table

---


<a id='database-reference-sql-sp-tams-gettarbytarid'></a>
# Procedure: sp_TAMS_GetTarByTarId

### Purpose
This stored procedure retrieves detailed information about a specific TAR (TAR No.) by its ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the TAR to be retrieved. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table where the Id column matches the provided TarId.
2. It retrieves various columns, including line number, TAR No., type, company, designation, name, office number, mobile number, email, submit date, access date and time, access location, access type, neutral gap status, exclusive status, description of work, remark, 13A socket status, cross-over status, protection type, withdrawal remark, and the corresponding TAR status.

### Data Interactions
* **Reads:** TAMS_TAR table

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult

### Purpose
This stored procedure retrieves and displays the TAR enquiry results based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID used to filter the results. |

### Logic Flow
The procedure starts by checking if any of the input parameters are not null or empty. It then constructs a SQL query string based on the values of these parameters.

If the line number is provided, it checks for specific conditions and constructs different parts of the SQL query string accordingly. For example, if the line number is 'NEL', it checks for certain flags to determine which part of the query to use.

The procedure then combines all the parts of the SQL query string using a union operator and executes the resulting query.

### Data Interactions
* **Reads:** TAMS_TAR_Test table, TAMS_WFStatus table, TAMS_User_QueryDept table.
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-department'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_Department

### Purpose
This stored procedure retrieves a list of TAR (Traffic Accident Report) companies that match the specified criteria, including track type, line, and access date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID to filter by. |

### Logic Flow
1. The procedure first checks if the user has a specific role that allows them to view TARs for all track types.
2. If not, it then checks if the user has a power endorser or power HOD role, which grants access to TARs involving power.
3. Next, it checks if the user has an applicant HOD or applicant role, which allows them to view TARs under their own department.
4. The procedure then constructs a SQL query using the `ROW_NUMBER()` function to order the results by company name.
5. The query filters the TARs based on the specified track type, line, and access date range.
6. Finally, the procedure executes the constructed SQL query and prints it for debugging purposes.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-header'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_Header

### Purpose
This stored procedure retrieves a header result for TAMS TAR enquiry, based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |
| @Line | nvarchar(50) | Line number |
| @TrackType | nvarchar(50) | Track type |
| @TarType | nvarchar(50) | Tar type |
| @AccessType | nvarchar(50) | Access type |
| @TarStatusId | integer | Tar status ID |
| @AccessDateFrom | nvarchar(50) | Access date from |
| @AccessDateTo | nvarchar(50) | Access date to |
| @Department | nvarchar(50) | Department |
| @Userid | nvarchar(50) | User ID |

### Logic Flow
The procedure first checks the user's role and permissions based on the provided parameters. It then constructs a SQL query using the `ROW_NUMBER()` function to retrieve the required data.

1. The procedure starts by checking if the user has any roles that match the specified track type. If they do, it sets the `@IsAll` variable to 1.
2. Next, it checks if the user has any roles that involve power or are power endorser. If they do, it sets the `@IsPower` variable to 1.
3. Then, it checks if the user has any roles that involve department or are applicant HOD. If they do, it sets the `@IsDep` variable to 1.
4. The procedure then constructs a SQL query using the `ROW_NUMBER()` function to retrieve the required data. It uses the `@cond` variable to filter the results based on the provided parameters.
5. Finally, it executes the constructed SQL query and prints the result.

### Data Interactions
* Reads: TAMS_TAR, TAMS_WFStatus, TAMS_User
* Writes: None

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-header-20220120'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20220120

### Purpose
This stored procedure retrieves a header result for TAMS Tar Enquiry.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID. |

### Logic Flow
1. The procedure starts by declaring variables and setting conditions based on the input parameters.
2. It then checks if the `@Line` parameter is not empty, and if so, it prints the first three characters of the line number (`@Line1`) to identify the type of inquiry (NEL or DTL).
3. Based on the value of `@Line1`, the procedure selects the corresponding status ID from TAMS_WFStatus.
4. It then constructs a SQL query using the `@sql` variable, which includes conditions based on the input parameters and the selected status ID.
5. The procedure executes the constructed SQL query to retrieve the required data.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User_QueryDept
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-header-20220529'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20220529

### Purpose
This stored procedure retrieves a header result for TAMS Tar Enquiry, which includes various filter criteria such as Line, TarType, AccessType, and more.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |
| @Line | nvarchar(10) | Line number |
| @TarType | nvarchar(50) | Tar type |
| @AccessType | nvarchar(50) | Access type |
| ... | ... | Additional filter criteria |

### Logic Flow
The procedure starts by checking the values of various parameters and setting a condition string (@cond). It then constructs a SQL query using this condition string to select rows from TAMS_TAR and TAMS_WFStatus tables. The query is based on the value of @Line, which determines whether it's 'NEL' or 'DTL'. For each line, it checks various conditions (e.g., TarType, AccessType) and applies them to the condition string (@cond). If the conditions are met, it includes the corresponding table in the SQL query. The procedure then prints the constructed SQL query and executes it.

### Data Interactions
* Reads: TAMS_TAR, TAMS_WFStatus tables
* Writes: None

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-header-20221018'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20221018

### Purpose
This stored procedure retrieves a header for TAMS Tar Enquiry Result based on user input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |

### Logic Flow
The procedure starts by declaring variables and setting conditions. It then checks the value of `@Line1` and sets a condition string `@cond`. Based on the values of `@TarType`, `@AccessType`, `@TarStatusId`, `@AccessDateFrom`, and `@AccessDateTo`, it appends conditions to `@cond`.

Next, it checks if `@Line1` is 'NEL' or 'DTL'. If it's 'NEL', it executes a query with specific conditions. If it's 'DTL', it executes another query with different conditions.

The procedure then constructs an SQL string `@sql` by concatenating the query and setting the row number column. Finally, it prints the SQL string and executes it using the `EXEC` statement.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus tables.
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-header-20240905'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20240905

### Purpose
This stored procedure retrieves a header result for TAMS TAR enquiry, based on user input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |
| @Line | nvarchar(50) | Line number |
| @TrackType | nvarchar(50) | Track type |
| @TarType | nvarchar(50) | Tar type |
| @AccessType | nvarchar(50) | Access type |
| @TarStatusId | integer | Tar status ID |
| @AccessDateFrom | nvarchar(50) | Access date from |
| @AccessDateTo | nvarchar(50) | Access date to |
| @Department | nvarchar(50) | Department |
| @Userid | nvarchar(50) | User ID |

### Logic Flow
The procedure follows these steps:

1. It checks if the user has a role in the specified track type and if they are an administrator, power endorser, or chief controller.
2. Based on the user's role, it sets three flags: @IsAll, @IsPower, and @IsDep.
3. If the user is not an external user, it sets all flags to 0.
4. It constructs a SQL query string (@cond) based on the input parameters and flags.
5. The procedure then executes the constructed SQL query using the ROW_NUMBER() function to retrieve the TAR results.

### Data Interactions
* Reads: TAMS_TAR, TAMS_WFStatus, TAMS_User

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-header-tobedeployed'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_Header_ToBeDeployed

### Purpose
This stored procedure retrieves a header for a TAR enquiry result to be deployed, based on various parameters such as user ID, line number, tar type, access date range, and applicant status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |
| @Line | nvarchar(10) | Line number |
| @TarType | nvarchar(50) | Tar type |
| @AccessType | nvarchar(50) | Access type |
| @TarStatusId | integer | Tar status ID |
| @AccessDateFrom | nvarchar(50) | Start access date |
| @AccessDateTo | nvarchar(50) | End access date |
| ... | ... | Various applicant statuses |

### Logic Flow
The procedure first checks the line number and sets a condition based on it. If the line number is 'NEL', it retrieves the status ID from TAMS_WFStatus table for the specified WFType and WFStatus. It then constructs an SQL query to select rows with ROW_NUMBER() over (ORDER BY t.tarno desc) as sno, and various other columns.

If the line number is not 'NEL' but is 'DTL', it performs a similar process as above. However, if the line number is neither 'NEL' nor 'DTL', it simply prints 'dtl'.

The procedure then constructs an SQL query with UNION ALL to combine results from both 'NEL' and 'DTL' lines.

Finally, it executes the constructed SQL query using EXEC (@sql).

### Data Interactions
* Reads: TAMS_TAR, TAMS_WFStatus tables.
* Writes: None.

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-header-20220529-m'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20220529_M

### Purpose
This stored procedure retrieves a list of TAR (TAR Status) enquiry results for a given set of parameters, including user ID, line number, tar type, access date range, and applicant status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | User ID |
| @Line | nvarchar(10) | Line Number |
| @TarType | nvarchar(50) | TAR Type |
| @AccessType | nvarchar(50) | Access Type |
| @TarStatusId | integer | TAR Status ID |
| @AccessDateFrom | nvarchar(50) | Access Date From |
| @AccessDateTo | nvarchar(50) | Access Date To |
| ... | ... | Applicant Status |

### Logic Flow
The procedure starts by declaring variables and setting conditions based on the input parameters. It then constructs a SQL query using these conditions to retrieve the required data from the TAMS_TAR and TAMS_WFStatus tables.

1. The procedure first checks if the line number is 'NEL' or 'DTL'. If it's 'NEL', it sets up a condition for the TAR type, access type, and TAR status ID.
2. If the line number is not 'NEL', but is 'DTL', it sets up conditions based on the applicant status.
3. The procedure then constructs the SQL query using these conditions and executes it to retrieve the required data.

### Data Interactions
* Reads: TAMS_TAR, TAMS_WFStatus tables
* Writes: None

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-header-20221018-m'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_Header_20221018_M

### Purpose
This stored procedure retrieves a list of TAR (TARWFStatus) enquiry results for a given set of parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID to filter the results by. |

### Logic Flow
The procedure starts by declaring variables and setting conditions based on the input parameters. It then constructs a SQL query using these conditions and executes it.

1. If `@Line1` is not empty, the procedure checks if it's 'NEL' or 'DTL'. Depending on this value, it selects rows from either `TAMS_TAR` table with specific conditions.
2. For each line (either `@Line1` or `@Line2`), the procedure constructs a SQL query using the input parameters and executes it.
3. The results are stored in a temporary result set named 't'.
4. Finally, the procedure prints the constructed SQL query and executes it.

### Data Interactions
* **Reads:** `TAMS_TAR`, `TAMS_WFStatus`
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-header-bak20230807'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_Header_bak20230807

### Purpose
This stored procedure retrieves a header result for TAMS Tar Enquiry.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID. |

### Logic Flow
The procedure starts by checking the values of various parameters, such as `@Line1` and `@Line2`, to determine which type of Tar Enquiry to retrieve (NEL or DTL). It then constructs a SQL query using these parameters and executes it.

Here's a step-by-step explanation:

1. The procedure checks if `@Line1` is not empty, and if so, prints the value of `@Line1`.
2. If `@Line1` is 'NEL', it retrieves the status ID from TAMS_WFStatus where Line = @Line1 and WFType = 'TARWFStatus' and WFStatus = 'Cancel'.
3. It then constructs a SQL query using the parameters, including conditions based on the values of various flags (e.g., `@isNEL_Applicant`, `@isDTL_Applicant`).
4. The procedure checks if `@Line2` is not empty, and if so, appends another condition to the SQL query.
5. Finally, it executes the constructed SQL query.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User_QueryDept
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-user'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_User

### Purpose
This stored procedure retrieves TAR (TAR Status) enquiry results for a specific user, filtered by various parameters such as track type, tar type, access date range, and more.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The ID of the user for whom to retrieve TAR enquiry results. |

### Logic Flow
1. The procedure first checks if the user has a specific role that allows them to view TARs under their department or as a power endorser, power HOD, or power endorser.
2. If the user meets these conditions, it filters the TARs based on the specified track type and additional parameters such as tar type, access date range, and more.
3. The procedure then selects distinct TAR records from the TAMS_TAR table, along with the createdBy field, which represents the ID of the user who created the TAR record.
4. Finally, it executes the selected query to retrieve the TAR enquiry results.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, and TAMS_User tables.

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-user20240905'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_User20240905

### Purpose
This stored procedure retrieves TAR (TARWFStatus) data for a specific user, filtered by various parameters such as track type, tar type, access date range, and more.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The ID of the user to retrieve TAR data for. |
| @Line | nvarchar(50) | The line number to filter by (optional). |
| @TrackType | nvarchar(50) | The track type to filter by (e.g., 'NEL_DCC', 'DTL_TAPApprover'). |
| @TarType | nvarchar(50) | The tar type to filter by (optional). |
| @AccessType | nvarchar(50) | The access type to filter by (optional). |
| @TarStatusId | integer | The TAR status ID to filter by. |
| @AccessDateFrom | nvarchar(50) | The start date of the access date range (optional). |
| @AccessDateTo | nvarchar(50) | The end date of the access date range (optional). |

### Logic Flow
1. The procedure first checks if the user has a specific role or combination of roles that allow them to view TAR data.
2. Based on the user's role, it sets flags (`@IsAll`, `@IsPower`, and `@IsDep`) to determine which filter conditions to apply.
3. It then constructs a SQL query string using these flags and additional filter parameters (e.g., line number, tar type, access date range).
4. The procedure executes the constructed SQL query and prints it for debugging purposes.
5. Finally, it executes the query to retrieve the TAR data.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User

---


<a id='database-reference-sql-sp-tams-gettarenquiryresult-user20250120'></a>
# Procedure: sp_TAMS_GetTarEnquiryResult_User20250120

### Purpose
This stored procedure retrieves TAR (Tracking and Analysis Report) data for a specific user, filtered by various parameters such as track type, tar type, access date range, and more.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The ID of the user for whom to retrieve TAR data. |

### Logic Flow
1. The procedure first checks if the user has a specific role (e.g., NEL_DCC, NEL_ChiefController) and if they have access to the desired track type.
2. If the user has multiple roles with different levels of access, it determines which level applies based on the provided parameters.
3. It then constructs a SQL query using the `ROW_NUMBER()` function to assign a unique number to each TAR record, ordered by the user's name.
4. The query joins the TAMS_TAR table with the TAMS_User table to retrieve the user's name and ID.
5. Depending on the user's role and access level, it filters the TAR data based on specific conditions (e.g., involvePower = 1 for PFR/PowerHOD roles).
6. Finally, it executes the constructed SQL query to retrieve the filtered TAR data.

### Data Interactions
* Reads: TAMS_TAR, TAMS_User, TAMS_WFStatus tables.
* Writes: None

---


<a id='database-reference-sql-sp-tams-gettarforpossessionplanreport'></a>
# Procedure: sp_TAMS_GetTarForPossessionPlanReport

### Purpose
This stored procedure retrieves data from the TAMS_TAR table for a possession plan report, filtering by line number, track type, access type, and date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter by. |
| @TrackType | nvarchar(50) | The track type to filter by. |
| @AccessType | nvarchar(50) | The access type to filter by. |
| @AccessDateFrom | nvarchar(50) | The start date of the access date range (inclusive). |
| @AccessDateTo | nvarchar(50) | The end date of the access date range (inclusive). |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table.
2. It filters the results based on the provided line number, track type, and access type.
3. Additionally, it applies a date filter to only include records where the access date falls within the specified range (from @AccessDateFrom to @AccessDateTo).
4. The filtered data is then returned as part of the procedure's output.

### Data Interactions
* **Reads:** TAMS_TAR table

---


<a id='database-reference-sql-sp-tams-gettarotherprotectionbypossessionid'></a>
# Procedure: sp_TAMS_GetTarOtherProtectionByPossessionId

### Purpose
This stored procedure retrieves a list of other protection details for a specified possession ID from the TAMS_Possession_OtherProtection table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | The ID of the possession for which to retrieve other protection details. |

### Logic Flow
1. The procedure starts by selecting all columns (id, possessionid, and otherprotection) from the TAMS_Possession_OtherProtection table.
2. It filters the results to only include rows where the possessionid matches the provided @PossessionId parameter.
3. The resulting data is ordered in ascending order by the id column.

### Data Interactions
* **Reads:** TAMS_Possession_OtherProtection

---


<a id='database-reference-sql-sp-tams-gettarpossessionlimitbypossessionid'></a>
# Procedure: sp_TAMS_GetTarPossessionLimitByPossessionId

### Purpose
This stored procedure retrieves and returns the possession limit details for a specified possession ID from the TAMS_Possession_Limit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | The unique identifier of the possession for which to retrieve the limit details. |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_Possession_Limit table.
2. It filters the results to only include rows where the possession ID matches the input parameter @PossessionId.
3. The retrieved data is ordered in ascending order based on the ID column.

### Data Interactions
* **Reads:** TAMS_Possession_Limit

---


<a id='database-reference-sql-sp-tams-gettarpossessionplanbytarid'></a>
# Procedure: sp_TAMS_GetTarPossessionPlanByTarId

### Purpose
This stored procedure retrieves a possession plan for a specific TarId from the TAMS_Possession and TAMS_Type_Of_Work tables.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the Tar to retrieve the possession plan for. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Possession and TAMS_Type_Of_Work tables.
2. It filters the results to only include rows where the typeofworkid in TAMS_Possession matches the id in TAMS_Type_Of_Work, and the tarid in TAMS_Possession matches the provided @TarId parameter.
3. The procedure then returns a list of columns from the selected data.

### Data Interactions
* **Reads:** TAMS_Possession, TAMS_Type_Of_Work

---


<a id='database-reference-sql-sp-tams-gettarpossessionpowersectorbypossessionid'></a>
# Procedure: sp_TAMS_GetTarPossessionPowerSectorByPossessionId

### Purpose
This stored procedure retrieves and displays information about a specific power sector associated with a possession ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | The unique identifier of the possession for which to retrieve the corresponding power sector details. |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_Possession_PowerSector table based on the provided PossessionId.
2. It filters the results to only include rows where the PossessionId matches the input parameter.
3. The selected data is then ordered in ascending order by the ID column.

### Data Interactions
* **Reads:** TAMS_Possession_PowerSector

---


<a id='database-reference-sql-sp-tams-gettarsectorsbyaccessdateandline'></a>
# Procedure: sp_TAMS_GetTarSectorsByAccessDateAndLine

### Purpose
This stored procedure retrieves tar sectors by access date and line, filtering based on specific conditions.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The access date to filter by. |
| @Line | nvarchar(10) | The line to filter by (DTLD or NELD). |

### Logic Flow
1. A temporary table #TMP is created with various columns.
2. If the specified line (@Line) is 'DTLD', the procedure inserts data from TAMS_Sector, TAMS_TAR_Sector, and TAMS_TAR tables into #TMP based on the access date (@AccessDate), TARStatusId, and other conditions.
3. If the specified line (@Line) is 'NELD', a similar insertion process occurs for NELD lines.
4. After inserting data, the procedure updates the ColourCode column in #TMP by selecting from itself where SameSector, TarNo, and ColourCode are not null.
5. Finally, the procedure selects all columns from #TMP ordered by [Order] ASC.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR tables
* **Writes:** #TMP table

---


<a id='database-reference-sql-sp-tams-gettarsectorsbyaccessdateandlineanddirection'></a>
# Procedure: sp_TAMS_GetTarSectorsByAccessDateAndLineAndDirection

### Purpose
This stored procedure retrieves a list of tar sectors by access date, line, and direction.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The access date to filter the results by. |
| @Line | nvarchar(10) = NULL | The line number to filter the results by. If NULL, all lines are included. |
| @TrackType | nvarchar(50) = NULL | The track type to filter the results by. If NULL, all track types are included. |
| @Direction | nvarchar(10) = NULL | The direction to filter the results by. |

### Logic Flow
1. A temporary table #TMP is created with columns for sector ID, line number, same sector flag, direction, sector name, tar number, access date, access type, sector ID, buffer flag, colour code, gap flag, and order.
2. If @Line is 'DTL', the procedure inserts data into #TMP by selecting from TAMS_Sector, TAMS_TAR_Sector, and TAMS_TAR tables based on the specified filter criteria (access date, track type, direction). The results are ordered by [Order] ASC.
3. If @Line is 'NEL', a similar insertion process occurs as in step 2, but with different filter criteria for TAMS_TAR_Sector and TAMS_TAR tables.
4. After inserting data into #TMP, the procedure updates the colour code column to the top value from #TMP where same sector, tar number, and colour code are not null.
5. The final result is selected from #TMP and ordered by [Order] ASC.
6. Finally, the temporary table #TMP is dropped.

### Data Interactions
* Reads: TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR tables

---


<a id='database-reference-sql-sp-tams-gettarsectorsbyaccessdateandlineanddirection-samesector'></a>
# Procedure: sp_TAMS_GetTarSectorsByAccessDateAndLineAndDirection_SameSector

### Purpose
This stored procedure retrieves tar sectors by access date, line, and direction for a specific sector.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessDate | date | The access date to filter the results by. |
| @Line | nvarchar(10) | The line number to filter the results by. (Default: NULL). |
| @Direction | nvarchar(10) | The direction to filter the results by. (Default: NULL). |

### Logic Flow
1. A temporary table #TMP is created with columns for sector ID, line, same sector, and other relevant information.
2. If the specified line (@Line) is 'DTL', the procedure inserts data from TAMS_Sector and TAMS_TAR tables into #TMP based on the access date (@AccessDate), TARStatusId, and direction (@Direction).
3. If the specified line (@Line) is 'NEL', a similar insertion process occurs for TAMS_Sector and TAMS_TAR_Test tables.
4. The procedure updates the ColourCode column in #TMP by selecting the ColourCode from the same row where SameSector is not null and TarNo is not null and ColourCode is not null.
5. Finally, the procedure selects all columns from #TMP.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Test

---


<a id='database-reference-sql-sp-tams-gettarsectorsbytarid'></a>
# Procedure: sp_TAMS_GetTarSectorsByTarId

### Purpose
This stored procedure retrieves a list of sectors associated with a specific TAR (TAR stands for Tariff Area Management System Sector) ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The TAR ID to retrieve sectors for. |

### Logic Flow
The procedure starts by joining three tables: TAMS_Sector, TAMS_TAR_Sector, and TAMS_TAR. It filters the results to only include sectors where the TAR ID matches the input parameter (@TarId) and the sector is not a buffer (IsBuffer = 0). The results are then ordered by Order and Sector in ascending order.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR_Sector, and TAMS_TAR tables.

---


<a id='database-reference-sql-sp-tams-gettarstationsbytarid'></a>
# Procedure: sp_TAMS_GetTarStationsByTarId

### Purpose
This stored procedure retrieves a list of stations associated with a specific TAR ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The TAR ID for which to retrieve associated stations |

### Logic Flow
The procedure starts by joining the TAMS_Station table with the TAMS_TAR_Station table on two conditions: the station's ID matches the TAR Station ID, and the TAR ID in the join condition matches the provided @TarId parameter. It then selects specific columns from both tables and orders the results by a column named [Order] in ascending order.

### Data Interactions
* **Reads:** TAMS_Station table, TAMS_TAR_Station table

---


<a id='database-reference-sql-sp-tams-gettarworkinglimitbypossessionid'></a>
# Procedure: sp_TAMS_GetTarWorkingLimitByPossessionId

### Purpose
This stored procedure retrieves the working limit details for a specific possession ID from the TAMS_Possession_WorkingLimit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PossessionId | integer | The unique identifier of the possession for which to retrieve the working limit. |

### Logic Flow
1. The procedure starts by selecting all columns (id, possessionid, and redflashinglampsloc) from the TAMS_Possession_WorkingLimit table.
2. It filters the results to only include rows where the possessionid matches the provided @PossessionId parameter.
3. The results are ordered in ascending order by the id column.

### Data Interactions
* **Reads:** TAMS_Possession_WorkingLimit

---


<a id='database-reference-sql-sp-tams-getwfstatusbyline'></a>
# Procedure: sp_TAMS_GetWFStatusByLine

### Purpose
This stored procedure retrieves the workflow status information for a specific line from the TAMS_WFStatus table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to retrieve workflow status information for. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_WFStatus table.
2. It filters the results to only include rows where the Line column matches the input @Line parameter and the IsActive flag is set to 1.
3. The selected columns are then ordered in ascending order based on the [Order] column.

### Data Interactions
* **Reads:** TAMS_WFStatus table

---


<a id='database-reference-sql-sp-tams-getwfstatusbylineandtype'></a>
# Procedure: sp_TAMS_GetWFStatusByLineAndType

This procedure retrieves the workflow status information for a specific line and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to retrieve workflow status for. |
| @TrackType | nvarchar(50) | The track type to filter by. |
| @Type | nvarchar(50) | The workflow type to filter by. |

### Logic Flow
1. The procedure starts by selecting the required columns from the TAMS_WFStatus table.
2. It filters the results based on the provided line number, track type, and workflow type.
3. Only records with an IsActive flag set to 1 are included in the results.
4. The results are ordered by the Order column in ascending order.

### Data Interactions
* **Reads:** TAMS_WFStatus table

---


<a id='database-reference-sql-sp-tams-get-all-roles'></a>
# Procedure: sp_TAMS_Get_All_Roles

The procedure retrieves all roles from the TAMS_Role table based on various conditions.

### Parameters
| Name | Type | Purpose |
| @IsExternal | BIT | Indicates whether to include external roles or not |

### Logic Flow
1. The procedure first selects all roles from the TAMS_Role table where Line = 'DTL' AND Module = 'TAR' and TrackType = 'Mainline'.
2. If @IsExternal is 0, it then selects all roles from the TAMS_Role table where Line = 'DTL' AND Module = 'OCC' and TrackType = 'Mainline'.
3. The procedure repeats steps 1 and 2 for the lines 'NEL', 'SPLRT', and their respective modules.
4. It also selects roles from the TAMS_Role table where Line is 'DTL', 'NEL', or 'SPLRT' AND Module = 'TAR' with TrackType = 'Depot'.
5. Finally, it selects roles from the TAMS_Role table where Line = 'NEL' AND Module = 'DCC' and TrackType = 'Depot'.

### Data Interactions
* **Reads:** TAMS_Role (explicitly selected tables)
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-get-childmenubyuserrole'></a>
# Procedure: sp_TAMS_Get_ChildMenuByUserRole

### Purpose
This stored procedure retrieves child menu items based on a user's role.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The ID of the user for whom to retrieve child menu items. |
| @MenuID | NVARCHAR(100) | The ID of the parent menu item. |
| @IsInternet | NVARCHAR(1) | A flag indicating whether to include internet-based menu items (1) or not (0). |

### Logic Flow
The procedure first checks if a user is logged in and has roles assigned. If so, it creates a temporary table to store the role IDs and then selects the corresponding child menu items from the TAMS_Menu_Role table based on the user's role. If no user is logged in or does not have any roles, it directly retrieves the child menu items for the specified parent menu item.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User, TAMS_Role, TAMS_Menu, TAMS_Menu_Role

---


<a id='database-reference-sql-sp-tams-get-childmenubyuserroleid'></a>
# Procedure: sp_TAMS_Get_ChildMenuByUserRoleID

### Purpose
This stored procedure retrieves child menu items based on a user's role ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The user ID to retrieve roles for. |
| @MenuID | NVARCHAR(100) | The parent menu ID to retrieve child menu items for. |
| @IsInternet | NVARCHAR(1) | A flag indicating whether to include internet menus or not. |

### Logic Flow
The procedure first creates a temporary table to store the user's role IDs. It then inserts these roles into the table and selects the corresponding role codes. The procedure concatenates these role codes into a single string, which is used to filter menu items.

If the concatenated role code is not empty, the procedure generates a SQL query to retrieve child menu items based on the role ID. This query includes filters for the parent menu ID, menu level, and module ID. If the @IsInternet parameter is 1, the query includes internet menus; otherwise, it excludes them.

The procedure prints the generated SQL query and executes it using the EXECUTE statement. Finally, it drops the temporary table used to store role IDs.

### Data Interactions
* Reads: TAMS_User_Role, TAMS_User, TAMS_Role, TAMS_Menu, TAMS_Menu_Role, Menu
* Writes: None

---


<a id='database-reference-sql-sp-tams-get-childmenubyuserrole-20231009'></a>
# Procedure: sp_TAMS_Get_ChildMenuByUserRole_20231009

### Purpose
This stored procedure retrieves child menus based on a user's role.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The ID of the user to retrieve child menus for. |
| @MenuID | NVARCHAR(100) | The ID of the parent menu to retrieve child menus from. |

### Logic Flow
1. The procedure first creates a temporary table #RoleTbl to store unique role codes.
2. It then inserts distinct role codes into the #RoleTbl based on the user's ID, their corresponding roles in TAMS_User_Role and TAMS_Role tables, and the user's login ID.
3. If the user has at least one assigned role, it constructs a SQL query to retrieve child menus by concatenating the role code with 'IN(' and ')'.
4. The procedure executes this constructed query using the EXEC function.
5. After executing the query, it drops the temporary table #RoleTbl.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User, TAMS_Role, TAMS_Menu, TAMS_Menu_Role, Menu tables.
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-get-companyinfo-by-id'></a>
# Procedure: sp_TAMS_Get_CompanyInfo_by_ID

### Purpose
This stored procedure retrieves company information from the TAMS_Company table based on a provided CompanyID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CompanyID | NVARCHAR(100) | The ID of the company to retrieve information for. |

### Logic Flow
1. The procedure checks if a record exists in the TAMS_Company table with the specified CompanyID.
2. If a record is found, it selects all columns from the TAMS_Company table where the ID matches the provided CompanyID.
3. If no record is found, it returns an empty result set (i.e., no data is returned).

### Data Interactions
* **Reads:** TAMS_Company

---


<a id='database-reference-sql-sp-tams-get-companylistbyuencompanyname'></a>
# Procedure: sp_TAMS_Get_CompanyListByUENCompanyName

### Purpose
This stored procedure retrieves a list of companies from the TAMS_Company table based on a search for UENNo and CompanyName.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @SearchUEN | NVARCHAR(100) | The UENNo to search for in the company names. |
| @SearchCompanyName | NVARCHAR(200) | The CompanyName to search for in the UENNo values. |

### Logic Flow
1. The procedure starts by selecting all columns (*) from the TAMS_Company table.
2. It then applies two conditions to filter the results:
   - The company name must match the @SearchUEN parameter (case-insensitive).
   - The UENNo value must match the @SearchCompanyName parameter (case-sensitive).
3. If both conditions are met, the procedure returns the selected columns for the matching company.

### Data Interactions
* **Reads:** TAMS_Company table

---


<a id='database-reference-sql-sp-tams-get-depot-tarenquiryresult-header'></a>
# Procedure: sp_TAMS_Get_Depot_TarEnquiryResult_Header

### Purpose
This stored procedure retrieves a header result for depot TAR enquiry, filtering by various parameters such as track type, tar type, access type, and date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | integer | The user ID to filter results by. |

### Logic Flow
1. The procedure first checks if the user has a specific role (NEL_ApplicantHOD, NEL_PowerEndorser, or NEL_PowerHOD) that grants access to TAR enquiry.
2. Based on the user's role, it sets flags (@IsAll, @IsPower, and @IsDep) to determine which conditions should be applied to filter results.
3. It then constructs a SQL query string (@sql) by concatenating various conditions based on the flags set earlier.
4. The query string is executed using the EXEC function.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus

---


<a id='database-reference-sql-sp-tams-get-external-userinfo-by-loginidpwd'></a>
# Procedure: sp_TAMS_Get_External_UserInfo_by_LoginIDPWD

### Purpose
This stored procedure retrieves external user information from the TAMS database based on a provided login ID and password.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) | The login ID of the user to retrieve information for. |
| @LoginPWD | NVARCHAR(200) | The encrypted password of the user to verify. |

### Logic Flow
The procedure first checks if a TAMS User record exists with an active and external status matching the provided LoginID. If such a record is found, it then decrypts the stored password using the dbo.DecryptString function and compares it to the provided LoginPWD. If the decryption and comparison are successful, the procedure returns all columns from the TAMS_User table where the LoginID matches.

### Data Interactions
* **Reads:** TAMS_User table

---


<a id='database-reference-sql-sp-tams-get-paravalbyparacode'></a>
# Procedure: sp_TAMS_Get_ParaValByParaCode

### Purpose
This stored procedure retrieves parameters from the TAMS_Parameters table based on a provided ParaCode and ParaValue1.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @paraCode | NVARCHAR(200) | The code of the parameter to retrieve. |
| @paraValue1 | NVARCHAR(200) | A value used to filter parameters with a specific ParaValue1. |

### Logic Flow
The procedure starts by selecting all columns from the TAMS_Parameters table where the ParaCode matches the provided @paraCode, and the EffectiveDate is within or before the current date, the ExpiryDate is within or after the current date, and the ParaValue1 matches the provided @paraValue1. The results are then ordered by ParaValue1, ParaValue2, and [Order].

### Data Interactions
* **Reads:** TAMS_Parameters table

---


<a id='database-reference-sql-sp-tams-get-parentmenubyuserrole'></a>
# Procedure: sp_TAMS_Get_ParentMenuByUserRole

### Purpose
This stored procedure retrieves the parent menu for a given user role, considering whether the user is accessing the application from an internet connection.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The ID of the user to retrieve the parent menu for. |
| @IsInternet | NVARCHAR(1) | A flag indicating whether the user is accessing the application from an internet connection (0 = no, 1 = yes). |

### Logic Flow
The procedure first checks if a valid user exists with the provided ID and active status. If a valid user is found, it then determines whether to retrieve the parent menu based on the value of @IsInternet. If @IsInternet is 0, it retrieves the parent menu for all roles assigned to the user; if @IsInternet is 1, it retrieves the parent menu only for roles assigned to the user and accessible from an internet connection.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User, TAMS_Role, TAMS_Menu, TAMS_Menu_Role

---


<a id='database-reference-sql-sp-tams-get-registrationcompanyinformationbyregid'></a>
# Procedure: sp_TAMS_Get_RegistrationCompanyInformationbyRegID

This procedure retrieves registration company information for a given registration ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The unique identifier of the registration to retrieve information for. |

### Logic Flow
1. The procedure checks if there exists a record in the TAMS_Reg_Module table where the RegID matches the input parameter and the RegStatus is either 1, 8, or 15.
2. If such a record exists, it means the registration ID has reached a specific stage (Applicant Company Registration Stage) and the procedure proceeds to retrieve the corresponding registration information from the TAMS_Registration table where the ID matches the input parameter.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_Registration

---


<a id='database-reference-sql-sp-tams-get-registrationinboxbyuserid'></a>
# Procedure: sp_TAMS_Get_RegistrationInboxByUserID

### Purpose
This stored procedure retrieves a list of registration inbox items for a specified user ID, including relevant workflow status and details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user for whom to retrieve registration inbox items. |

### Logic Flow
The procedure follows these steps:

1. It initializes a temporary table, #RegistrationTable, to store the retrieved data.
2. It opens two cursors: one for roles with 'SysAdmin' and another for roles with 'SysApprover'.
3. For each role, it iterates through the registration items that match the current role's track type and line.
4. If the item is pending approval by a SysAdmin or SysApprover, it inserts the relevant data into #RegistrationTable.
5. It then fetches the next row from the cursor for the same role and repeats the process until all rows are processed.
6. After processing both cursors, it closes them and deallocates their resources.
7. Finally, it selects distinct registration items from #RegistrationTable and drops the temporary table.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_User_Role

---


<a id='database-reference-sql-sp-tams-get-registrationinboxbyuserid-20231009'></a>
# Procedure: sp_TAMS_Get_RegistrationInboxByUserID_20231009

### Purpose
This stored procedure retrieves a list of registration inbox items for a specified user ID, including relevant details such as registration status and workflow information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user for whom to retrieve registration inbox items. |

### Logic Flow
The procedure follows these steps:

1. It initializes a temporary table, #RegistrationTable, to store the retrieved data.
2. It opens two cursors: one for roles with 'SysAdmin' and another for roles with 'SysApprover'. The cursors iterate through the relevant rows in the TAMS_User_Role table based on the user ID provided.
3. For each role, it checks if the corresponding registration status is pending. If so, it inserts a new row into the #RegistrationTable for that status.
4. For roles with 'SysApprover', it further filters the registration statuses to only include those that require approval by the approver. It then iterates through these filtered rows and updates the #RegistrationTable accordingly.
5. After processing all relevant rows, it closes both cursors and selects distinct rows from the #RegistrationTable for final output.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus

---


<a id='database-reference-sql-sp-tams-get-registrationinboxbyuserid-hnin'></a>
# Procedure: sp_TAMS_Get_RegistrationInboxByUserID_hnin

### Purpose
This stored procedure retrieves a list of registration inbox items for a specific user ID, including relevant workflow statuses and details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user for whom to retrieve registration inbox items. |

### Logic Flow
The procedure follows these steps:

1. It first checks if the user has a role that includes 'SysAdmin' or 'SysApprover'. If so, it retrieves and inserts relevant data into a temporary table.
2. For roles with 'SysAdmin', it filters for pending company registration and system admin approval workflows, inserting data into the temporary table.
3. For roles with 'SysApprover', it uses a cursor to iterate through the registration items, checking if each item has been updated by the user or not. If not, it inserts the relevant data into the temporary table.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_User_Role

---


<a id='database-reference-sql-sp-tams-get-registrationinformationbyregmoduleid'></a>
# Procedure: sp_TAMS_Get_RegistrationInformationByRegModuleID

### Purpose
This stored procedure retrieves registration information for a specific module ID, including relevant details from TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_Reg_Role, and TAMS_Reg_QueryDept tables.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModuleID | INT | The ID of the module for which to retrieve registration information. |

### Logic Flow
1. Check if a record exists in TAMS_Reg_Module with the specified RegModuleID.
2. If a record exists, select relevant details from TAMS_Registration, TAMS_WFStatus, and TAMS_Reg_Module tables based on the RegId, Line, Module, and RegStatus columns.
3. Extract specific values from TAMS_Reg_Module for use in subsequent steps.
4. Update the RegStatus value by subtracting 1.
5. Retrieve the ID of the previous module with matching RegId, Line, Module, and RegStatus values.
6. Check if a record exists in TAMS_Reg_Role with the previously retrieved RegModID.
7. If a record exists, select relevant details from TAMS_Reg_Role and TAMS_Role tables based on the RegRoleID column.
8. Check if a record exists in TAMS_Reg_QueryDept with the previously retrieved RegModID.
9. Return results.

### Data Interactions
* **Reads:** 
	+ TAMS_Registration table
	+ TAMS_Reg_Module table
	+ TAMS_WFStatus table
	+ TAMS_Reg_Role table
	+ TAMS_Reg_QueryDept table
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-get-rolesbylinemodule'></a>
# Procedure: sp_TAMS_Get_RolesByLineModule

### Purpose
This stored procedure retrieves roles associated with a specific line, track type, and module from the TAMS_Role table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(100) | The line number to filter by. |
| @TrackType | NVARCHAR(50) | The track type to filter by. |
| @Module | NVARCHAR(100) | The module to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Role table.
2. It filters the results based on the provided line number, track type, and module using LIKE operators with the input parameters.
3. The filtered data is then returned.

### Data Interactions
* **Reads:** TAMS_Role

---


<a id='database-reference-sql-sp-tams-get-signupstatusbyloginid'></a>
# Procedure: sp_TAMS_Get_SignUpStatusByLoginID

### Purpose
This stored procedure retrieves and displays the access status for a given login ID, including the workflow status, pending role, and notified date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) | The login ID to retrieve access status for. |

### Logic Flow
1. The procedure first checks if a registration exists for the given login ID.
2. If a registration is found, it retrieves the ID of the registration and creates a temporary table to store the access status.
3. It then opens a cursor to iterate through each line and module associated with the registration.
4. For each line and module, it retrieves the workflow status, pending role, and notified date from the TAMS_WFStatus and TAMS_Registration tables.
5. Based on the workflow status, it determines whether the user is external or internal and updates the pending role accordingly.
6. It then inserts a new row into the temporary table with the line, module, workflow status, pending role, and notified date.
7. Finally, it closes the cursor, deallocates the cursor handle, and returns the access status from the temporary table.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus

---


<a id='database-reference-sql-sp-tams-get-useraccessroleinfo-by-id'></a>
# Procedure: sp_TAMS_Get_UserAccessRoleInfo_by_ID

This procedure retrieves user access role information for a specified user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The ID of the user to retrieve access role information for. |

### Logic Flow
1. Check if a user with the provided UserID exists in the TAMS_User table.
2. If the user exists, retrieve all rows from the TAMS_User_Role and TAMS_Role tables where the roleID matches the ID of the specified role in the TAMS_Role table, and the UserID in the TAMS_User_Role table matches the provided UserID.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Role

---


<a id='database-reference-sql-sp-tams-get-useraccessstatusinfo-by-loginid'></a>
# Procedure: sp_TAMS_Get_UserAccessStatusInfo_by_LoginID

### Purpose
This stored procedure retrieves user access status information for a given login ID, including approved and pending approvals.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) | The login ID to retrieve access status information for. |

### Logic Flow
1. Check if the provided login ID exists in the TAMS_User table.
2. If it does, select the corresponding user ID from the TAMS_User table.
3. Open a cursor to iterate through distinct lines, track types, and modules from the TAMS_Role table where the line is not 'All' and the role is active (1).
4. For each iteration:
   - Check if the current user has access to the current line, track type, and module by joining the TAMS_User_Role table.
   - If they do, insert a new record into the #AccessStatus temporary table with an approved status.
   - If they don't, check if there is a registration associated with the login ID, line, track type, and module that has not been approved or rejected.
     - If such a registration exists, insert a new record into the #AccessStatus temporary table with a pending approval status.
5. Repeat steps 3-4 until all lines, track types, and modules have been processed.
6. Close and deallocate the cursor.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Role, TAMS_User_Role, TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus

---


<a id='database-reference-sql-sp-tams-get-userinfo'></a>
# Procedure: sp_TAMS_Get_UserInfo

### Purpose
This stored procedure retrieves user information from the TAMS database, including account status and role assignments.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @uid | NVARCHAR(100) | The login ID of the user to retrieve information for. |

### Logic Flow
The stored procedure checks the existence of a valid user account based on the provided login ID and current date. It then updates the last login timestamp if the account is active. If the account has expired or been deactivated, it sets specific status messages. Finally, it retrieves the user's role assignments.

### Data Interactions
* **Reads:** [TAMS_User], [TAMS_User_Role], [TAMS_Role]
* **Writes:** [TAMS_User] (lastlogin timestamp)

---


<a id='database-reference-sql-sp-tams-get-userinfo-by-id'></a>
# Procedure: sp_TAMS_Get_UserInfo_by_ID

### Purpose
This stored procedure retrieves user information based on a provided user ID, including access details for different roles and modules.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(100) | The ID of the user to retrieve information for. |

### Logic Flow
The procedure follows these steps:
1. It first checks if a user exists with the provided ID in the TAMS_User table.
2. If a user is found, it then retrieves company information from the TAMS_Company table based on the user's CompanyID.
3. Next, it fetches user query department details for the specified user ID.
4. The procedure then breaks down the access rights into four categories:
   - DTL TAR: Retrieves role and module information for the 'DTL' line and 'TAR' module with a TrackType of 'mainline'.
   - DTL OCC: Retrieves role and module information for the 'DTL' line and 'OCC' module with a TrackType of 'mainline'.
   - NEL TAR: Retrieves role and module information for the 'NEL' line and 'TAR' module with a TrackType of 'mainline'.
   - NEL OCC: Retrieves role and module information for the 'NEL' line and 'OCC' module with a TrackType of 'mainline'.
5. Finally, it fetches depot access details for the user ID.

### Data Interactions
* Reads from:
	+ TAMS_User
	+ TAMS_Company
	+ TAMS_User_QueryDept
	+ TAMS_Role
	+ TAMS_User_Role
* Writes to: None

---


<a id='database-reference-sql-sp-tams-get-userinfo-by-loginid'></a>
# Procedure: sp_TAMS_Get_UserInfo_by_LoginID

### Purpose
This stored procedure retrieves user information from the TAMS_User table based on a provided LoginID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(100) | The unique identifier for the user to retrieve information for. |

### Logic Flow
1. The procedure checks if a record exists in the TAMS_User table with the specified LoginID.
2. If a matching record is found, it selects all columns from the TAMS_User table where the LoginID matches the provided value.

### Data Interactions
* **Reads:** TAMS_User

---


<a id='database-reference-sql-sp-tams-get-user-list-by-line'></a>
# Procedure: sp_TAMS_Get_User_List_By_Line

### Purpose
This stored procedure retrieves a list of users based on various search criteria, including user type, active status, and module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CurrentUser | NVARCHAR(100) | The current user's login ID. |
| @SearchRail | NVARCHAR(10) | The rail line to search for. Can be 'ALL' or a specific value. |
| @SearchUserType | NVARCHAR(10) | The user type to filter by (e.g., Internal, External). |
| @SearchActive | NVARCHAR(10) | The active status to filter by (e.g., 1 for active, 0 for inactive). Can be '%1%', '%0%', or 'ALL'. |
| @SearchModule | NVARCHAR(10) | The module to search for. |
| @SearchUserID | NVARCHAR(100) | The user ID to search for. |
| @SearchUserName | NVARCHAR(200) | The username to search for. |

### Logic Flow
1. The procedure starts by creating a temporary table #UserTable to store the results.
2. It then declares several variables to hold intermediate results and initializes them with default values.
3. The procedure retrieves a list of user lines from the TAMS_User_Role table, grouped by role line, for the current user's login ID.
4. If the search rail is 'ALL', it retrieves all non-'All' user lines; otherwise, it uses the provided search rail value.
5. It then opens a cursor to iterate over the users in the retrieved list and performs the following steps:
	* Retrieves the module(s) associated with each user's role ID.
	* Checks if the user has access to TAR, OCC, or DCC modules; if so, sets the @UModule variable accordingly.
	* If the user does not have access to any of these modules, it sets @UModule to a default value (e.g., 'TAR, OCC, DCC').
	* Retrieves the rail line(s) associated with each user's role ID and updates the @UserRail variable accordingly.
	* Inserts the user into the #UserTable if they do not already exist.
6. The procedure closes all cursors and deletes the temporary table.

### Data Interactions
* Reads: TAMS_User, TAMS_User_Role, TAMS_Role
* Writes: None

---


<a id='database-reference-sql-sp-tams-get-user-list-by-line-20211101'></a>
# Procedure: sp_TAMS_Get_User_List_By_Line_20211101

### Purpose
This stored procedure retrieves a list of users based on various search criteria, including user type, active status, and module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CurrentUser | NVARCHAR(100) | The current user's login ID. |
| @SearchRail | NVARCHAR(10) | The rail line to search for. |
| @SearchUserType | NVARCHAR(10) | The user type to filter by. |
| @SearchActive | NVARCHAR(10) | The active status to filter by. |
| @SearchModule | NVARCHAR(10) | The module to filter by. |
| @SearchUserID | NVARCHAR(100) | The user ID to search for. |
| @SearchUserName | NVARCHAR(200) | The username to search for. |

### Logic Flow
1. The procedure starts by creating a temporary table #UserTable to store the retrieved user data.
2. It then declares several variables to hold the user's ID, type, name, and module.
3. A cursor is opened to iterate through the users who match the current user's login ID and the search criteria.
4. For each matching user, the procedure checks if they have access to both TAR and OCC modules. If so, it sets @UModule to 'TAR, OCC'. Otherwise, it sets @UModule to either 'TAR' or 'OCC'.
5. The procedure then retrieves the rail lines for the current user and sets @UserRail to a comma-separated list of these rail lines.
6. If the user is not already in the #UserTable, their data is inserted into the table with the updated @UModule value.
7. The procedure repeats steps 4-6 until all matching users have been processed.
8. Finally, it closes the cursor and deletes the temporary table.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Role, TAMS_User u, TAMS_User_Role ur, TAMS_Role r
* **Writes:** #UserTable

---


<a id='database-reference-sql-sp-tams-get-user-railline'></a>
# Procedure: sp_TAMS_Get_User_RailLine

### Purpose
This stored procedure retrieves the rail line associated with a given user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserId | NVARCHAR(100) | The user ID to retrieve the rail line for. |

### Logic Flow
1. The procedure checks if the provided user ID exists in the TAMS_User_Role table and matches a specific condition.
2. If the condition is met, it returns a list of three predefined rail lines ('DTL', 'NEL', and 'SPLRT').
3. If the condition is not met, it retrieves the distinct rail line(s) associated with the user ID from the TAMS_User_Role table.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User

---


<a id='database-reference-sql-sp-tams-get-user-railline-depot'></a>
# Procedure: sp_TAMS_Get_User_RailLine_Depot

### Purpose
This stored procedure retrieves the rail line and depot information for a given user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserId | NVARCHAR(100) | The user ID to retrieve information for. |

### Logic Flow
1. The procedure first checks if the provided user ID exists in the TAMS_User_Role table with a Line value of 'All' and matches the user's LoginID.
2. If the user has a role that includes all lines, it returns a hardcoded value 'NEL' as the rail line.
3. If the user does not have a role that includes all lines, it retrieves the distinct Line values from the TAMS_User_Role table where the UserID matches the provided ID and TrackType is 'Depot'.
4. The procedure then returns these Line values as the rail line.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-get-user-tracktype'></a>
# Procedure: sp_TAMS_Get_User_TrackType

### Purpose
This stored procedure retrieves a list of unique track types associated with a specific user, based on their login ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Loginid | NVARCHAR(100) | The login ID of the user to retrieve track types for. |

### Logic Flow
1. The procedure starts by selecting distinct track types from the TAMS_User_Role table.
2. It joins this table with the TAMS_User table on the UserID column, ensuring that only roles associated with a specific user are considered.
3. The procedure then filters the results to include only rows where the LoginID matches the provided @Loginid parameter.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User

---


<a id='database-reference-sql-sp-tams-get-user-tracktype-line'></a>
# Procedure: sp_TAMS_Get_User_TrackType_Line

### Purpose
This stored procedure retrieves a list of unique track types associated with a specific user and line.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(100) | The line number to filter track types by. |
| @UserId | NVARCHAR(100) | The ID of the user to retrieve track types for. |

### Logic Flow
1. The procedure starts by selecting distinct track types from the TAMS_User_Role and TAMS_User tables.
2. It filters the results to only include rows where the UserID in TAMS_User matches the provided @UserId, and the LoginID in TAMS_User matches the provided @Line.
3. The resulting track types are returned as a list.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User

---


<a id='database-reference-sql-sp-tams-inbox-child-onload'></a>
# Procedure: sp_TAMS_Inbox_Child_OnLoad

### Purpose
This stored procedure is used to load child TARs into a temporary table for further processing. It filters TARs based on various conditions such as status, type, and sector.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the sector to process |
| @TrackType | NVARCHAR(50) | The track type of the sector to process |
| @AccessDate | NVARCHAR(20) | The access date for the TARs to filter |
| @TARType | NVARCHAR(20) | The type of TAR to filter |
| @LoginUser | NVARCHAR(50) | The login user ID to filter |
| @SectorID | INT | The sector ID to process |

### Logic Flow
The procedure follows these steps:

1. It retrieves the user ID from the TAMS_USER table based on the provided login user ID.
2. It creates three temporary tables: #TmpSector, #TmpInbox, and #TmpInboxList.
3. It truncates the existing data in the temporary tables.
4. It inserts data into #TmpSector by selecting sectors that match the line number, track type, and are active with an effective date within the specified access date range.
5. It inserts data into #TmpInbox by selecting TARs that match the provided conditions such as status, type, sector, and endorser ID.
6. It creates a cursor to iterate through the #TmpInbox table and checks if the user ID is associated with any of the TARs in the current iteration.
7. If the user ID is not associated, it inserts the TAR into #TmpInboxList.
8. Finally, it selects the data from #TmpInboxList based on the sector ID.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_Endorser
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList

---


<a id='database-reference-sql-sp-tams-inbox-child-onload-20230406'></a>
# Procedure: sp_TAMS_Inbox_Child_OnLoad_20230406

### Purpose
This stored procedure performs a daily load of TAR (Trade Agreement) inbox data, removing any cancelled TARs and populating the #TmpInboxList table with the remaining TARs.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to load TARs for. |
| @AccessDate | NVARCHAR(20) | The access date to filter TARs by. |
| @TARType | NVARCHAR(20) | The TAR type to filter TARs by. |
| @LoginUser | NVARCHAR(50) | The login user ID to filter TARs by. |
| @SectorID | INT | The sector ID to load TARs for. |

### Logic Flow
1. The procedure starts by selecting the current user ID from TAMS_USER based on the provided login user.
2. It then sets the current date and time, which is used to filter TARs by access date.
3. The procedure removes any cancelled TARs by checking if there are any workflows with a status other than 'Pending' for each TAR.
4. If no such workflows exist, the TAR is added to the #TmpInboxList table.
5. If workflows do exist, the procedure checks if the user ID matches the current user ID. If it does, the TAR is added to the #TmpInboxList table; otherwise, it skips this TAR.
6. The procedure repeats steps 4-5 for each TAR in the #TmpInbox table.
7. Finally, the procedure selects and groups the TARs from the #TmpInboxList table based on the sector ID.

### Data Interactions
* Reads: TAMS_USER, TAMS_TAR, TAMS_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* Writes: #TmpSector, #TmpInbox, #TmpInboxList

---


<a id='database-reference-sql-sp-tams-inbox-child-onload-20230706'></a>
# Procedure: sp_TAMS_Inbox_Child_OnLoad_20230706

### Purpose
This stored procedure loads child TARs into a temporary inbox table, filtering out cancelled and pending TARs based on user access.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to load TARs for. |
| @AccessDate | NVARCHAR(20) | The access date filter (optional). |
| @TARType | NVARCHAR(20) | The TAR type filter (optional). |
| @LoginUser | NVARCHAR(50) | The login user ID. |
| @SectorID | INT | The sector ID to load TARs for. |

### Logic Flow
1. The procedure starts by selecting the current user ID from the TAMS_USER table based on the provided login user ID.
2. It then sets a cursor to retrieve all TARs in the temporary inbox table, ordered by TAR ID and sector ID.
3. For each TAR in the inbox table:
   1. If there are no workflow records for the current TAR with a status other than 'Pending', it is inserted into the temporary inbox list table.
   2. If there are workflow records for the current TAR with a status other than 'Pending', it checks if the user ID of the endorser matches the current user ID. If not, it skips to the next iteration.
4. After processing all TARs in the inbox table, the procedure groups and orders the temporary inbox list table by TAR ID, sector ID, TAR type, access date, and access type.

### Data Interactions
* Reads: TAMS_USER, TAMS_TAR, TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* Writes: #TmpSector, #TmpInbox, #TmpInboxList

---


<a id='database-reference-sql-sp-tams-inbox-child-onload-20240925'></a>
# Procedure: sp_TAMS_Inbox_Child_OnLoad_20240925

### Purpose
This stored procedure loads child TARs into a temporary table, filtering out cancelled and pending TARs based on user access.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @TrackType | NVARCHAR(50) | The track type to filter by. |
| @AccessDate | NVARCHAR(20) | The access date to filter by. |
| @TARType | NVARCHAR(20) | The TAR type to filter by. |
| @LoginUser | NVARCHAR(50) | The login user ID. |
| @SectorID | INT | The sector ID. |

### Logic Flow
1. The procedure starts by selecting the user ID from the TAMS_USER table based on the provided login user ID.
2. It then creates three temporary tables: #TmpSector, #TmpInbox, and #TmpInboxList to store the filtered data.
3. The procedure truncates these temporary tables before inserting new data.
4. It selects the TARs from the TAMS_TAR table that match the provided line number, track type, access date, and TAR type, as well as the sector ID.
5. For each TAR, it checks if there are any workflows with a status other than 'Pending'. If not, it inserts the TAR into the #TmpInboxList table.
6. If there are workflows with a status other than 'Pending', it opens a cursor to retrieve the action by user ID and checks if the current user is the same as the action by user ID. If so, it increments a counter.
7. After checking all TARs, it selects the data from the #TmpInboxList table where the sector ID matches the provided sector ID and groups the results by TAR ID, TAR number, TAR type, access date, and access type.

### Data Interactions
* Reads: TAMS_USER, TAMS_TAR, TAMS_Sector, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* Writes: #TmpSector, #TmpInbox, #TmpInboxList

---


<a id='database-reference-sql-sp-tams-inbox-child-onload-20230406-m'></a>
# Procedure: sp_TAMS_Inbox_Child_OnLoad_20230406_M

### Purpose
This stored procedure performs a daily load of TAR (Trade Agreement Record) inbox data, removing any cancelled records and populating the #TmpInboxList table with the remaining records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		| NVARCHAR(10) | The line number to process. |
| @AccessDate	| NVARCHAR(20) | The access date for the TARs. |
| @TARType	| NVARCHAR(20) | The type of TAR to load. |
| @LoginUser	| NVARCHAR(50) | The login user ID. |
| @SectorID	| INT | The sector ID. |

### Logic Flow
1. The procedure starts by selecting the current user ID from the TAMS_USER table based on the provided login user ID.
2. It then sets the current date and time to the GETDATE() function, which returns the current date and time in the format specified.
3. The procedure creates temporary tables #TmpSector and #TmpInbox to store the sector data and TAR inbox records, respectively.
4. It truncates these temporary tables to ensure they are empty before populating them with new data.
5. The procedure then selects the sector data from the TAMS_Sector table based on the provided line number and filters out any inactive or expired sectors.
6. Next, it selects the TAR inbox records from the TAMS_TAR table, filtering out any cancelled records (based on the WFStatus column) and records with a user ID other than the current user ID.
7. The procedure then creates a cursor (@Cur01) to iterate through the #TmpInbox table, selecting each record in turn.
8. For each record, it checks if there are any workflow actions associated with that TAR (based on the TAMS_TAR_Workflow table). If not, it inserts the record into the #TmpInboxList table.
9. If there are workflow actions associated with the TAR, it creates another cursor (@Cur02) to iterate through these actions and checks if the current user ID is the action owner. If so, it increments a counter variable (@ActionByChk).
10. After iterating through all the workflow actions, if the counter variable (@ActionByChk) is still 0, it means that the TAR has no associated workflow actions and inserts the record into the #TmpInboxList table.
11. Finally, the procedure selects the records from the #TmpInboxList table and groups them by TAR ID, line number, sector ID, access date, and type.

### Data Interactions
* **Reads:**
	+ TAMS_USER
	+ TAMS_Sector
	+ TAMS_TAR
	+ TAMS_TAR_Workflow
	+ TAMS_Endorser
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-inbox-master-onload'></a>
# Procedure: sp_TAMS_Inbox_Master_OnLoad

### Purpose
This stored procedure performs a master load of TAMS inbox data, including sectors and corresponding TARs, based on user input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line number to filter by. |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by. |
| @AccessDate | NVARCHAR(20) | Specifies the access date to filter by. |
| @TARType | NVARCHAR(20) | Specifies the TAR type to filter by. |
| @LoginUser | NVARCHAR(50) | Specifies the login user ID for filtering purposes. |

### Logic Flow
1. The procedure starts by selecting the user ID from the TAMS_USER table based on the provided login user ID.
2. It then creates temporary tables (#TmpSector, #TmpInbox, and #TmpInboxList) to store sector data and TARs with their corresponding access details.
3. The procedure truncates these temporary tables before populating them with new data.
4. It inserts sector data into the #TmpSector table based on the provided line number and track type.
5. For each sector, it selects TARs from the TAMS_TAR table that match the specified TAR type and access date, as well as the user ID.
6. The procedure then checks if there are any pending workflows for each TAR. If not, it inserts the TAR data into the #TmpInboxList table.
7. If there are pending workflows, it opens a cursor to iterate through the workflow actions and checks if the current action is associated with the same user ID as the login user. If so, it increments an action by counter.
8. Based on the action by counter value, it either inserts or skips the TAR data into the #TmpInboxList table.
9. Finally, the procedure joins the sector data from the #TmpSector table with the TAR data from the #TmpInboxList table and groups the results by sector order.

### Data Interactions
* **Reads:** TAMS_USER, TAMS_Sector, TAMS_TAR, TAMS_TAR_Sector, TAMS_TAR_Workflow, TAMS_Endorser
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList

---


<a id='database-reference-sql-sp-tams-inbox-master-onload-20230406'></a>
# Procedure: sp_TAMS_Inbox_Master_OnLoad_20230406

### Purpose
This stored procedure performs a master load of TAMS inbox data, including filtering and processing based on user access.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line to filter by. |
| @AccessDate | NVARCHAR(20) | Specifies the access date to filter by. |
| @TARType | NVARCHAR(20) | Specifies the TAR type to filter by. |
| @LoginUser | NVARCHAR(50) | Specifies the login user ID for filtering and authorization. |

### Logic Flow
The procedure follows these steps:

1. It retrieves the user ID from the TAMS_USER table based on the provided login user ID.
2. It creates temporary tables (#TmpSector, #TmpInbox, and #TmpInboxList) to store sector data, inbox data, and processed inbox list data, respectively.
3. It truncates the existing data in these temporary tables.
4. It inserts data from the TAMS_Sector table into the #TmpSector table based on the specified line and date range.
5. It inserts data from the TAMS_TAR table into the #TmpInbox table based on the specified TAR type, access date, and user ID.
6. It processes the #TmpInbox table by checking if there are any pending workflows for each TAR ID. If not, it adds the TAR ID to the #TmpInboxList table.
7. If there are pending workflows, it retrieves the action by from the TAMS_TAR_Workflow table and checks if the user is authorized to perform that action. If so, it updates the #TmpInboxList table with the action by.
8. It fetches the next record from the #TmpInbox table and repeats steps 6-7 until all records are processed.
9. Finally, it joins the #TmpSector table with the #TmpInboxList table based on sector ID and orders the results by sector order.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_USER, TAMS_TAR_Workflow, TAMS_Endorser
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList

---


<a id='database-reference-sql-sp-tams-inbox-master-onload-20230406-m'></a>
# Procedure: sp_TAMS_Inbox_Master_OnLoad_20230406_M

### Purpose
This stored procedure performs a master load of TAMS inbox data, including filtering and processing based on user input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		| AS NVARCHAR(10) | Specifies the line number to filter by |
| @AccessDate	| AS NVARCHAR(20) | Specifies the access date to filter by |
| @TARType	| AS NVARCHAR(20) | Specifies the TAR type to filter by |
| @LoginUser	| AS NVARCHAR(50) | Specifies the login user ID |

### Logic Flow
The procedure follows these steps:

1. It retrieves the user ID from the TAMS_USER table based on the provided login user ID.
2. It creates temporary tables (#TmpSector and #TmpInbox) to store sector data and inbox data, respectively.
3. It truncates the existing data in the temporary tables.
4. It inserts data into the temporary tables by selecting relevant data from the TAMS_Sector and TAMS_TAR tables based on the provided line number, access date, TAR type, and user ID.
5. It creates a cursor (@Cur01) to iterate through the inbox data in the #TmpInbox table.
6. For each row in the inbox data, it checks if there are any pending workflows associated with the corresponding TAMS_TAR record. If not, it inserts the data into the #TmpInboxList table.
7. If there are pending workflows, it creates another cursor (@Cur02) to retrieve the action by user ID from the TAMS_TAR_Workflow table.
8. It checks if the current user ID matches the action by user ID retrieved from the cursor. If not, it skips the data insertion.
9. After processing all rows in the inbox data, it closes both cursors and deallocates them.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_User, TAMS_Endorser tables.
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList tables.

---


<a id='database-reference-sql-sp-tams-inbox-onload'></a>
# Procedure: sp_TAMS_Inbox_OnLoad

### Purpose
This stored procedure is used to populate a temporary inbox table with TAR (Task Assignment Record) data that meets specific criteria, including access date and type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the sector. |
| @AccessDate | NVARCHAR(20) | The access date for the TAR data. |
| @TARType | NVARCHAR(20) | The type of TAR data to include. |
| @LoginUser | NVARCHAR(50) | The login user ID. |

### Logic Flow
The procedure follows these steps:

1. It retrieves the user ID from the TAMS_USER table based on the provided login user ID.
2. It creates temporary tables (#TmpSector, #TmpInbox, and #TmpInboxList) to store sector data, TAR data, and a list of TARs with specific criteria, respectively.
3. It populates the #TmpSector table with sector data from TAMS_Sector based on the provided line number and date range.
4. It populates the #TmpInbox table with TAR data from TAMS_TAR that meets specific criteria, including access date and type, and is not already in the inbox list.
5. For each TAR in the #TmpInbox table, it checks if there are any workflows associated with it that have a status other than 'Pending'. If so, it retrieves the action by from TAMS_TAR_Workflow.
6. Based on the action by retrieved, it inserts or updates the corresponding TAR in the #TmpInboxList table.
7. Finally, it joins the #TmpSector and #TmpInboxList tables based on sector ID and direction, and groups the results to display the final inbox data.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_TAR, TAMS_TAR_Workflow, TAMS_User, TAMS_TAM
* **Writes:** #TmpSector, #TmpInbox, #TmpInboxList

---


<a id='database-reference-sql-sp-tams-insert-externaluserregistration'></a>
# Procedure: sp_TAMS_Insert_ExternalUserRegistration

### Purpose
This stored procedure performs the business task of inserting a new external user registration into the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UENNo | NVARCHAR(20) | Unique identifier for the external user. |
| @Company | NVARCHAR(200) | The company associated with the external user. |
| @Name | NVARCHAR(200) | The name of the external user. |
| @Email | NVARCHAR(500) | The email address of the external user. |
| @Dept | NVARCHAR(200) | The department of the external user. |
| @OfficeNo | NVARCHAR(20) | The office number of the external user. |
| @Mobile | NVARCHAR(20) | The mobile phone number of the external user. |
| @SBSTCPName | NVARCHAR(200) | The name of the SBSTC department. |
| @SBSTCPDept | NVARCHAR(200) | The department of the SBSTC. |
| @SBSTCPOfficeNo | NVARCHAR(20) | The office number of the SBSTC. |
| @ValidTo | NVARCHAR(20) | The date until which the registration is valid. |
| @Purpose | NVARCHAR(MAX) | The purpose of the external user's registration. |
| @LoginID | NVARCHAR(200) | The login ID for the external user. |
| @Password | NVARCHAR(100) | The password for the external user. |

### Logic Flow
1. The procedure starts by encrypting the provided password using the `dbo.EncryptString` function.
2. It then inserts a new record into the `TAMS_Registration` table, specifying all required fields and parameters.
3. If an error occurs during this insertion process, the transaction is rolled back to maintain database consistency.

### Data Interactions
* **Reads:** None explicitly listed in the procedure code.
* **Writes:** 
  * TAMS_Registration table

---


<a id='database-reference-sql-sp-tams-insert-externaluserregistrationmodule'></a>
# Procedure: sp_TAMS_Insert_ExternalUserRegistrationModule

### Purpose
This stored procedure performs the business task of inserting a new external user registration module into the TAMS system, triggering an email notification to approvers for approval or rejection.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |
| @Line | NVARCHAR(20) | The line number associated with the registration. |
| @TrackType | NVARCHAR(50) | The type of track for the registration. |
| @Module | NVARCHAR(20) | The module name for the registration. |

### Logic Flow
The procedure follows these steps:

1. It determines the level of the workflow based on whether a company is registered or not.
2. It retrieves the next stage in the workflow, including the ID and title.
3. It inserts a new record into the TAMS_Reg_Module table with the provided data.
4. It inserts an audit log entry for the registration action.
5. If the level of the workflow is 3 (indicating that it's the final step), it sends an email notification to approvers with instructions on how to access and approve or reject the user registration.

### Data Interactions
* Reads: TAMS_Company, TAMS_Registration, TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_Reg_Module, TAMS_Action_Log.
* Writes: TAMS_Reg_Module, TAMS_Action_Log.

---


<a id='database-reference-sql-sp-tams-insert-externaluserregistrationmodule-20231009'></a>
# Procedure: sp_TAMS_Insert_ExternalUserRegistrationModule_20231009

### Purpose
This stored procedure performs the business task of inserting a new external user registration module into the TAMS system, including sending an email to approvers for approval or rejection.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |
| @Line | NVARCHAR(20) | The line number in the workflow. |
| @TrackType | NVARCHAR(50) | The type of track for the registration. |
| @Module | NVARCHAR(20) | The module associated with the registration. |

### Logic Flow
The procedure follows these steps:

1. It checks if a company is registered and, based on that, determines the level in the workflow to insert.
2. It retrieves the next stage ID and endorser ID from the TAMS system based on the line number and track type.
3. It inserts a new record into the TAMS_Reg_Module table with the provided data.
4. It inserts an audit log entry for the user registration submission.
5. If the level is 3, it sends an email to approvers with a link to access the TAMS system for approval or rejection.

### Data Interactions
* Reads: TAMS_Company, TAMS_Registration, TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_Reg_Module, TAMS_Action_Log
* Writes: TAMS_Reg_Module

---


<a id='database-reference-sql-sp-tams-insert-internaluserregistration'></a>
# Procedure: sp_TAMS_Insert_InternalUserRegistration

### Purpose
This stored procedure performs internal user registration by inserting a new record into the TAMS_Registration table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @SapNo | NVARCHAR(20) | Unique SAP number for the registered user. |
| @Name | NVARCHAR(200) | Full name of the registered user. |
| @UserName | NVARCHAR(200) | Username chosen by the registered user. |
| @Email | NVARCHAR(500) | Email address of the registered user. |
| @Mobile | NVARCHAR(20) | Mobile number of the registered user. |
| @OfficeNo | NVARCHAR(20) | Office number of the registered user. |
| @Dept | NVARCHAR(100) | Department of the registered user. |
| @ValidTo | NVARCHAR(100) | Date until which the registration is valid. |
| @Purpose | NVARCHAR(MAX) | Purpose of the internal user registration. |

### Logic Flow
1. The procedure starts by beginning a transaction.
2. It then attempts to insert a new record into the TAMS_Registration table using the provided parameters, including the username as the primary key.
3. If the insertion is successful, the procedure commits the transaction.
4. If an error occurs during the insertion process, the procedure rolls back the transaction.

### Data Interactions
* **Reads:** None explicitly listed in this procedure.
* **Writes:** TAMS_Registration table

---


<a id='database-reference-sql-sp-tams-insert-internaluserregistrationmodule'></a>
# Procedure: sp_TAMS_Insert_InternalUserRegistrationModule

### Purpose
This stored procedure performs internal user registration by submitting a new registration request to the system, which then triggers a workflow for approval and notification of relevant users.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | Unique identifier for the registered user. |
| @Line | NVARCHAR(20) | Line number associated with the registration request. |
| @TrackType | NVARCHAR(50) | Track type (e.g., TAR, DCC, OCC) indicating the workflow to be triggered. |
| @Module | NVARCHAR(20) | Module name (e.g., TAR, DCC, OCC) used for tracking and notification purposes. |

### Logic Flow
1. The procedure starts by checking if a specific module (@Module) is provided. Based on this, it determines the corresponding workflow ID (@WorkflowID) to be triggered.
2. It then retrieves the next stage in the workflow (e.g., @NextStageID, @WFStatus) for the given line number (@Line) and track type (@TrackType).
3. The procedure inserts a new record into the TAMS_Reg_Module table with the provided registration details.
4. An audit log entry is created to track the submission of the user registration request.
5. If the module is TAR, an email is sent to relevant users (sys approvers) for approval and notification purposes.

### Data Interactions
* Reads: TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_Reg_Module, TAMS_User_Role, TAMS_Action_Log
* Writes: TAMS_Reg_Module

---


<a id='database-reference-sql-sp-tams-insert-internaluserregistrationmodule-20231009'></a>
# Procedure: sp_TAMS_Insert_InternalUserRegistrationModule_20231009

### Purpose
This stored procedure performs internal user registration for a given module, including updating workflow status and sending an email notification to approvers.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |
| @Line | NVARCHAR(20) | The line number associated with the registration. |
| @TrackType | NVARCHAR(50) | The type of track for the registration. |
| @Module | NVARCHAR(20) | The module being registered (e.g., TAR or OCC). |

### Logic Flow
1. The procedure starts by checking if the module is 'TAR'. If it is, it retrieves the workflow ID from the TAMS_Workflow table based on the line number and track type.
2. If the module is not 'TAR', it retrieves the workflow ID from the TAMS_Workflow table based on the line number and track type, but with a different workflow type ('OCCIntUser').
3. The procedure then retrieves the next stage ID and other relevant information (e.g., endorser ID, workflow status) from the TAMS_Endorser and TAMS_WFStatus tables.
4. It inserts a new record into the TAMS_Reg_Module table with the provided registration details.
5. An audit log is inserted to track the registration activity.
6. The procedure sends an email notification to approvers (identified by their email addresses) with a link to access the TAMS system and approve/reject the user registration.

### Data Interactions
* Reads: TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_Reg_Module, TAMS_User_Role, TAMS_Action_Log
* Writes: TAMS_Reg_Module

---


<a id='database-reference-sql-sp-tams-insert-internaluserregistrationmodule-bak20230112'></a>
# Procedure: sp_TAMS_Insert_InternalUserRegistrationModule_bak20230112

### Purpose
This stored procedure performs the business task of inserting a new internal user registration module into the TAMS system, triggering a workflow and sending an email to approvers for approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |

### Logic Flow
1. The procedure starts by beginning a transaction.
2. It retrieves the next stage in the workflow for the given line and module, which determines the status of the registration.
3. Based on the retrieved status, it inserts a new record into the TAMS_Reg_Module table with the provided details.
4. An audit log is inserted to track the action taken.
5. The procedure then sends an email to approvers (sys approvers) for approval, including a link to access the TAMS system and approve/reject the registration.

### Data Interactions
* Reads: TAMS_Workflow, TAMS_Endorser, TAMS_WFStatus, TAMS_Reg_Module, TAMS_Action_Log
* Writes: TAMS_Reg_Module, TAMS_Action_Log

---


<a id='database-reference-sql-sp-tams-insert-regquerydept-sysadminapproval'></a>
# Procedure: sp_TAMS_Insert_RegQueryDept_SysAdminApproval

### Purpose
This stored procedure performs a system-level approval for inserting new records into the TAMS_Reg_QueryDept table, ensuring that only authorized users can make changes.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module associated with the query department. |
| @RegRoleID | INT | The ID of the role associated with the query department. |
| @Dept | NVARCHAR(200) | The name of the query department. |
| @UpdatedBy | INT | The ID of the user who initiated the update. |

### Logic Flow
1. The procedure begins by attempting to start a new transaction.
2. It then attempts to insert a new record into the TAMS_Reg_QueryDept table, passing in the provided parameters and current date/time values for creation and last update timestamps.
3. If the insertion is successful, the procedure commits the transaction, effectively making the changes permanent.
4. If any errors occur during the insertion process, the procedure rolls back the transaction, ensuring that no changes are made to the database.

### Data Interactions
* **Reads:** None explicitly listed in this procedure.
* **Writes:** TAMS_Reg_QueryDept table

---


<a id='database-reference-sql-sp-tams-insert-regquerydept-sysownerapproval'></a>
# Procedure: sp_TAMS_Insert_RegQueryDept_SysOwnerApproval

### Purpose
This stored procedure inserts a new record into the TAMS_Reg_QueryDept table, which is used to track departmental queries for registered modules. It also checks if a user query department record already exists and inserts one if necessary.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registered module being inserted into the TAMS_Reg_QueryDept table. |
| @RegRoleID | INT | The role ID associated with the departmental query. |
| @Dept | NVARCHAR(200) | The name of the department for which a query is being tracked. |
| @UpdatedBy | INT | The user ID who last updated the record. |

### Logic Flow
1. The procedure starts by beginning a transaction to ensure data consistency.
2. It retrieves the user ID associated with the login ID used in the TAMS_Registration table, linked to the registered module being inserted.
3. A new record is inserted into the TAMS_Reg_QueryDept table with the provided departmental query details and timestamps for creation and update.
4. The procedure checks if a user query department record already exists for the same user ID, role ID, and department.
5. If no existing record is found, a new record is inserted into the TAMS_User_QueryDept table.
6. Finally, the transaction is committed to save the changes.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Registration, TAMS_Reg_Module, TAMS_Reg_QueryDept, TAMS_User_QueryDept
* **Writes:** TAMS_Reg_QueryDept, TAMS_User_QueryDept

---


<a id='database-reference-sql-sp-tams-insert-userquerydeptbyuserid'></a>
# Procedure: sp_TAMS_Insert_UserQueryDeptByUserID

### Purpose
This stored procedure inserts a new record into the TAMS_User_QueryDept table if the specified user query department does not already exist for that user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user to insert the query department for. |
| @Dept | NVARCHAR(100) | The department code to insert as a new record. |
| @UpdatedBy | INT | The ID of the user who is updating the query department. |

### Logic Flow
1. The procedure checks if a record already exists in the TAMS_User_QueryDept table for the specified user and department.
2. If no record exists, it retrieves the department line from the TAMS_Parameters table based on the provided department code.
3. It then retrieves the role ID from the TAMS_Role table that matches the department line and has a specific pattern (ApplicantHOD).
4. With the role ID in hand, it inserts a new record into the TAMS_User_QueryDept table with the specified user ID, role ID, department code, and update information.

### Data Interactions
* **Reads:** TAMS_Parameters, TAMS_Role, TAMS_User_QueryDept
* **Writes:** TAMS_User_QueryDept

---


<a id='database-reference-sql-sp-tams-insert-userregrole-sysadminapproval'></a>
# Procedure: sp_TAMS_Insert_UserRegRole_SysAdminApproval

### Purpose
This stored procedure performs the business task of inserting a new user registration role with sysadmin approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registered module. |
| @RegRoleID | INT | The ID of the role to be assigned. |
| @IsAssigned | BIT | A flag indicating whether the role is assigned or not. |
| @UpdatedBy | INT | The ID of the user who updated the registration. |

### Logic Flow
1. The procedure starts by beginning a transaction.
2. It then retrieves the next stage ID for the specified registered module and workflow type, as well as the new workflow status ID and endorser ID.
3. If these values are found, it inserts a new record into the TAMS_Reg_Role table with the provided parameters.

### Data Interactions
* **Reads:** TAMS_Workflow, TAMS_Endorser, TAMS_Reg_Module, TAMS_Reg_Role
* **Writes:** TAMS_Reg_Role

---


<a id='database-reference-sql-sp-tams-insert-userrolebyuseridrailmodule'></a>
# Procedure: sp_TAMS_Insert_UserRoleByUserIDRailModule

### Purpose
This stored procedure inserts a new user role into the TAMS_User_Role table if it does not already exist for a given user ID and role ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user to insert the role for. |
| @Rail | NVARCHAR(10) | The rail associated with the role. |
| @TrackType | NVARCHAR(50) | The track type associated with the role. |
| @Module | NVARCHAR(10) | The module associated with the role. |
| @RoleID | INT | The ID of the role to insert. |
| @UpdatedBy | INT | The ID of the user who is updating the role. |

### Logic Flow
1. The procedure checks if a record already exists in the TAMS_User_Role table for the given user ID and role ID.
2. If no record exists, it inserts a new record into the TAMS_User_Role table with the provided values.

### Data Interactions
* **Reads:** TAMS_User_Role table
* **Writes:** TAMS_User_Role table

---


<a id='database-reference-sql-sp-tams-occ-addtvfackremarks'></a>
# Procedure: sp_TAMS_OCC_AddTVFAckRemarks

### Purpose
This stored procedure adds a new record to the TAMS_TVF_Ack_Remark table, which stores remarks for TVF acknowledgments, and also inserts an audit record into the TAMS_TVF_Ack_Remark_Audit table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserId | int | The ID of the user who is adding the remark. |
| @TVFAckId | int | The ID of the TVF acknowledgment being added a remark for. |
| @TVFRemarks | nvarchar(1000) | The text of the remark to be added. |

### Logic Flow
1. The procedure starts by declaring a variable @NewID, which will hold the ID of the newly inserted record.
2. It then attempts to start a transaction and insert a new record into the TAMS_TVF_Ack_Remark table with the provided @TVFRemarks and @UserId.
3. After inserting the record, it selects the ID of the newly inserted record from the SCOPE_IDENTITY() function and stores it in @NewID.
4. Next, it inserts an audit record into the TAMS_TVF_Ack_Remark_Audit table with the provided information, including the user who added the remark and the date and time of the addition.
5. If any part of this process fails, the transaction is rolled back to maintain data consistency.

### Data Interactions
* **Reads:** None explicitly listed from tables; however, it uses GETDATE() and @UserID which are likely derived from other tables or variables.
* **Writes:** 
	+ TAMS_TVF_Ack_Remark table (new record)
	+ TAMS_TVF_Ack_Remark_Audit table (audit record)

---


<a id='database-reference-sql-sp-tams-occ-generate-authorization'></a>
# Procedure: sp_TAMS_OCC_Generate_Authorization

### Purpose
This stored procedure generates an authorization for a TAMS OCC (Traction and Maintenance Services Operations Center) operation, based on the provided line, track type, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the operation. |
| @TrackType | NVARCHAR(50) | The type of track for the operation. |
| @AccessDate | NVARCHAR(20) | The access date for the operation. |

### Logic Flow
1. The procedure first determines the current date and time, as well as a cutoff time.
2. If no access date is provided, it calculates the previous day's date based on the current date and time.
3. It then checks if there are any existing authorizations for the specified line and track type on the calculated date. If not, it proceeds to generate a new authorization.
4. The procedure creates temporary tables to store sector data and OCC authentication details.
5. It populates these tables with relevant data from the main database.
6. It then iterates through each sector in the temporary table, checking if there is an existing authorization for that sector on the specified date.
7. If no authorization exists, it generates a new one by inserting into the #TmpOCCAuth table and updating the corresponding sector details.
8. The procedure also inserts into the TAMS_OCC_Auth table with the generated authorization details.
9. It then creates a workflow for the newly generated authorization and inserts into the TAMS_OCC_Auth_Workflow table.
10. Finally, it inserts into the TAMS_OCC_Auth_Audit and TAMS_OCC_Auth_Workflow_Audit tables to track changes.

### Data Interactions
* **Reads:** 
	+ [dbo].[TAMS_Traction_Power]
	+ [dbo].[TAMS_TAR]
	+ [dbo].[TAMS_TAR_Sector]
	+ [dbo].[TAMS_Power_Sector]
	+ [dbo].[TAMS_Endorser]
	+ [dbo].[TAMS_Workflow]
* **Writes:** 
	+ #TmpOCCAuth
	+ #TmpTARSectors
	+ #TmpOCCAuthWorkflow

---


<a id='database-reference-sql-sp-tams-occ-generate-authorization-20230215'></a>
# Procedure: sp_TAMS_OCC_Generate_Authorization_20230215

### Purpose
This stored procedure generates an authorization for a TAMS OCC (Traction and Maintenance Services Operations Control) operation, based on the provided line number and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the TAMS OCC operation. |
| @AccessDate | NVARCHAR(20) | The access date for the TAMS OCC operation. |

### Logic Flow
The procedure follows these steps:

1. Determine the current date and time.
2. If no access date is provided, calculate the previous day's date based on the current date and time.
3. Calculate the effective date range for the workflow by checking if the current date and time falls within the workflow's effective date range.
4. Retrieve the workflow ID, WFStatusId, and EndorserID from the TAMS_Workflow table.
5. Create temporary tables to store the sector data and OCC authentication details.
6. Insert data into the temporary tables based on the provided line number.
7. Iterate through the sector data and update the OCC authentication details in the temporary tables accordingly.
8. Insert the updated OCC authentication details into the TAMS_OCC_Auth table.
9. Insert the workflow-related data into the TAMS_OCC_Auth_Workflow table.

### Data Interactions
* **Reads:**
	+ TAMS_Workflow
	+ TAMS_Traction_Power
	+ TAMS_TAR
	+ TAMS_TAR_Sector
	+ TAMS_Power_Sector
	+ TAMS_Endorser
	+ TAMS_OCC_Auth
	+ TAMS_OCC_Auth_Workflow
* **Writes:**
	+ #TmpTARSectors (temporary table)
	+ #TmpOCCAuth (temporary table)
	+ #TmpOCCAuthWorkflow (temporary table)

---


<a id='database-reference-sql-sp-tams-occ-generate-authorization-trace'></a>
# Procedure: sp_TAMS_OCC_Generate_Authorization_Trace

### Purpose
This stored procedure generates an authorization trace for a given line of operation, taking into account the access date and effective dates of workflows.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line of operation to generate the authorization trace for. |
| @AccessDate | NVARCHAR(20) | The access date to use when generating the authorization trace. |

### Logic Flow
The procedure follows these steps:

1. Determine the current date and time, as well as a cutoff time.
2. If no access date is provided, calculate the previous day's date based on the current date and time.
3. Otherwise, use the provided access date.
4. Retrieve the workflow ID for the given line of operation that matches the calculated effective dates.
5. Retrieve the endorser ID for the workflow.
6. Create temporary tables to store sector data and OCC authentication details.
7. Insert sector data into the temporary table based on the line of operation.
8. Iterate through the sector data, updating the OCC authentication details in the temporary table as necessary.
9. Insert the updated OCC authentication details into a final table.
10. Generate an authorization workflow for each OCC authentication detail.
11. Drop the temporary tables.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TAR_Sector, TAMS_Traction_Power_Detail, TAMS_Workflow, TAMS_Endorser, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* Writes: #TmpTARSectors, #TmpOCCAuth, #TmpOCCAuthWorkflow

---


<a id='database-reference-sql-sp-tams-occ-generate-authorization-20230215-m'></a>
# Procedure: sp_TAMS_OCC_Generate_Authorization_20230215_M

### Purpose
This stored procedure generates authorization for TAMS OCC operations based on the provided line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to generate authorization for. |
| @AccessDate | NVARCHAR(20) | The access date to use for generating authorization. |

### Logic Flow
1. Determine the current date and time.
2. If no access date is provided, calculate the previous day's date based on the current date and time.
3. If an access date is provided, use it; otherwise, use the calculated previous day's date.
4. Retrieve the workflow ID for the specified line and workflow type (OCCAuth).
5. Retrieve the endorser ID for the workflow.
6. Create temporary tables to store TARSectors and OCCAuth data.
7. Iterate through the TAMS_Traction_Power table, updating the IsBuffer and PowerOn columns in #TmpOCCAuth based on the presence of matching TARSectors.
8. Insert new records into #TmpOCCAuth if necessary.
9. Retrieve existing records from TAMS_OCC_Auth that match the line, access date, and operation date.
10. If no matches are found, insert a new record into #TmpOCCAuthWorkflow for each matching record in TAMS_OCC_Auth.

### Data Interactions
* **Reads:** 
	+ TAMS_Traction_Power
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_TAR
	+ TAMS_TAR_Sector
	+ TAMS_Power_Sector
	+ TAMS_OCC_Auth
	+ TAMS_OCC_AuthWorkflow
* **Writes:** 
	+ #TmpOCCAuth
	+ #TmpTARSectors

---


<a id='database-reference-sql-sp-tams-occ-generate-authorization-20230215-poweronissue'></a>
# Procedure: sp_TAMS_OCC_Generate_Authorization_20230215_PowerOnIssue

### Purpose
This stored procedure generates authorization for TAMS OCC operations based on the provided line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to generate authorization for. |
| @AccessDate | NVARCHAR(20) | The access date to use for generating authorization. |

### Logic Flow
The procedure follows these steps:

1. Determine the current date and time.
2. If no access date is provided, calculate the previous day's date if the current time is after 6:00 AM, otherwise use the current date minus one day.
3. Calculate the operation date based on the determined dates.
4. Retrieve the workflow ID for the specified line and workflow type (OCCAuth).
5. Retrieve the endorser ID for the workflow.
6. Create temporary tables to store sector data and OCC authentication details.
7. Insert sector data into the temporary table based on the provided line number.
8. Iterate through the sector data, updating the OCC authentication details in the temporary table if necessary.
9. Insert the updated OCC authentication details into the TAMS_OCC_Auth table.
10. Create a workflow for each OCC authentication detail in the TAMS_OCC_Auth table.

### Data Interactions
* Reads: 
	+ TAMS_TAR
	+ TAMS_TAR_Sector
	+ TAMS_Traction_Power_Detail
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_OCC_Auth
	+ TAMS_OCC_Auth_Workflow
* Writes:
	+ #TmpTARSectors (temporary table)
	+ #TmpOCCAuth (temporary table)
	+ #TmpOCCAuthWorkflow (temporary table)
	+ TAMS_OCC_Auth
	+ TAMS_OCC_Auth_Workflow

---


<a id='database-reference-sql-sp-tams-occ-getendorserbyworkflowid'></a>
# Procedure: sp_TAMS_OCC_GetEndorserByWorkflowId

This procedure retrieves a list of endorsers for a specific workflow ID, filtered by level and effective/expiry dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ID | INT | The ID of the workflow to retrieve endorses for. |

### Logic Flow
1. The procedure starts by selecting columns from the TAMS_Endorser table.
2. It filters the results to only include rows where the WorkflowId matches the input parameter @ID, and the Level is 1.
3. The EffectiveDate must be less than or equal to the current date, and the ExpiryDate must be greater than or equal to the current date.
4. Only active records are included in the results.
5. The results are ordered by ID.

### Data Interactions
* **Reads:** TAMS_Endorser

---


<a id='database-reference-sql-sp-tams-occ-getoccauthbylineandaccessdate'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthByLineAndAccessDate

### Purpose
This stored procedure retrieves data from the TAMS_OCC_Auth table based on a specified line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter by. |
| @AccessDate | nvarchar(50) | The access date to filter by. |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_OCC_Auth table.
2. It filters the data based on the provided line and access date, using a case-sensitive comparison for the line number.
3. The access date is converted to a datetime format before being compared with the provided @AccessDate parameter.
4. The results are ordered by the ID column in ascending order.

### Data Interactions
* **Reads:** [dbo].[TAMS_OCC_Auth]

---


<a id='database-reference-sql-sp-tams-occ-getoccauthpreviewbyparameters'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthPreviewByParameters

### Purpose
This stored procedure retrieves and previews the OCC authentication data for a given set of parameters, including line, track type, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter by. |
| @TrackType | nvarchar(50) | The track type to filter by. |
| @OperationDate | date | The operation date to filter by. |
| @AccessDate | date | The access date to filter by. |

### Logic Flow
1. The procedure creates two temporary tables, #TMP and #TMP_OCCAuthPreview.
2. It then inserts data from the TAMS_Traction_Power table into #TMP based on the provided line number and track type.
3. Next, it inserts data from the TAMS_OCC_Auth table into #TMP_OCCAuthPreview based on the operation date, access date, and other parameters.
4. The procedure then iterates through the OCC authentication IDs in #TMP_OCCAuthPreview and updates the corresponding records in #TMP_OCCAuthPreview with additional information based on the workflow status.
5. Finally, it returns all the data from #TMP_OCCAuthPreview.

### Data Interactions
* **Reads:** [TAMS_Traction_Power], [TAMS_OCC_Auth]
* **Writes:** [TAMS_Traction_Power], [TAMS_OCC_Auth]

---


<a id='database-reference-sql-sp-tams-occ-getoccauthpreviewbyparameters-nel'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthPreviewByParameters_NEL

### Purpose
This stored procedure retrieves and previews the OCC authentication data for a specified line, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line for which to retrieve OCC authentication data. |

### Logic Flow
1. The procedure starts by creating a temporary table #TMP_OCCAuthPreview to store the retrieved data.
2. It then checks if the input line is 'NEL'. If true, it proceeds with the logic for this line.
3. For each row in the TAMS_Traction_Power and TAMS_OCC_Auth tables where the operation date matches the input operation date and access date matches the input access date, and the line matches the input line, it inserts a new row into #TMP_OCCAuthPreview.
4. The procedure then creates a cursor to iterate over the OCC authentication IDs in #TMP_OCCAuthPreview.
5. For each OCC authentication ID, it opens another cursor to retrieve the corresponding data from the TAMS_OCC_Auth_Workflow table.
6. It updates the data in #TMP_OCCAuthPreview based on the workflow status and action by user for each OCC authentication ID.
7. Finally, it closes both cursors and deallocates them.

### Data Interactions
* **Reads:** 
	+ TAMS_Traction_Power
	+ TAMS_OCC_Auth
	+ TAMS_OCC_Auth_Workflow
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-occ-getoccauthpreviewbyparameters-nel-bak20230728'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthPreviewByParameters_NEL_bak20230728

The purpose of this stored procedure is to retrieve and preview the OCC Auth data for a specific line, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to filter the OCC Auth data. |

### Logic Flow

1. The procedure starts by creating a temporary table #TMP_OCCAuthPreview to store the initial OCC Auth data.
2. It then checks if the input line is 'NEL'. If true, it inserts the relevant data into the temporary table based on the operation date and access date.
3. A cursor is created to iterate through the OCC Auth IDs in the temporary table.
4. For each OCC Auth ID, another cursor is used to retrieve the corresponding endorser ID, workflow status, action time, and action by user.
5. Based on the endorser ID, the procedure updates the relevant columns in the temporary table with the appropriate data from the TAMS_OCC_Auth_Workflow table.
6. The procedure repeats steps 4-5 for each OCC Auth ID until all records have been processed.
7. Finally, the temporary table is selected and displayed.

### Data Interactions
* **Reads:** [TAMS_Traction_Power], [TAMS_OCC_Auth], [TAMS_OCC_Auth_Workflow]
* **Writes:** [TAMS_OCCAuthPreview]

---


<a id='database-reference-sql-sp-tams-occ-getoccauthorisationbyparameters-nel'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL

### Purpose
This stored procedure retrieves and updates OCC (Operations Control Centre) authorisation data based on provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | User ID for authentication purposes. |

### Logic Flow
The procedure follows these steps:

1. It first checks if a workflow exists with the specified Line, TrackType, and is active.
2. If a workflow exists, it retrieves endorser data from TAMS_Endorser table based on the workflow ID and line.
3. For each endorser, it updates corresponding fields in #TMP_OCCAuthNEL table based on the endorser's role and status.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power], [TAMS_OCC_Auth]
* **Writes:** [TAMS_OCC_AuthNEL]

---


<a id='database-reference-sql-sp-tams-occ-getoccauthorisationbyparameters-nel-001'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL_001

### Purpose
This stored procedure retrieves OCC authorisation details based on provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user to retrieve authorisation for. |

### Logic Flow
1. The procedure starts by selecting the workflow ID from the TAMS_Workflow table where the line matches the provided line parameter and the workflow type is 'OCCAuth' and the record is active.
2. It then inserts data into a temporary table #TMP_Endorser, which contains endorser IDs, levels, titles, and roles for the specified line.
3. The procedure creates another temporary table #TMP_OCCAuthNEL to store OCC authorisation details.
4. A cursor is created to iterate through the OCC authorisation ID in #TMP_OCCAuthNEL.
5. For each OCC authorisation ID, a sub-procedure is executed to update the corresponding endorser IDs and levels in #TMP_Endorser.
6. The procedure then updates the OCC authorisation details in #TMP_OCCAuthNEL based on the updated endorser data.
7. Finally, the procedure selects all data from #TMP_OCCAuthNEL.

### Data Interactions
* **Reads:** TAMS_Workflow, TAMS_Endorser, TAMS_Traction_Power, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow

---


<a id='database-reference-sql-sp-tams-occ-getoccauthorisationbyparameters-nel-bak20230727'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthorisationByParameters_NEL_bak20230727

### Purpose
This stored procedure retrieves OCC authorisation details based on provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user. |
| @Line | nvarchar(10) | The line number. |
| @TrackType | nvarchar(50) | The track type. |
| @OperationDate | date | The operation date. |
| @AccessDate | date | The access date. |
| @RosterCode | nvarchar(50) | The roster code. |

### Logic Flow
1. The procedure starts by selecting the workflow ID from the TAMS_Workflow table where the line, track type, and workflow type match the provided parameters.
2. It then inserts data into a temporary table #TMP_Endorser with endorser details based on the selected workflow ID and line number.
3. Next, it selects OCC authorisation details from the TAMS_OCC_Auth table and inserts them into another temporary table #TMP_OCCAuthNEL.
4. The procedure then declares two cursors: one for each temporary table.
5. It iterates through the cursors, updating the corresponding fields in #TMP_OCCAuthNEL based on the endorser ID and roster code.
6. Finally, it selects all data from #TMP_OCCAuthNEL.

### Data Interactions
* Reads:
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_OCC_Auth
* Writes: None

---


<a id='database-reference-sql-sp-tams-occ-getoccauthorisationccbyparameters'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthorisationCCByParameters

### Purpose
This stored procedure retrieves OCC authorisation CC data by providing parameters such as user ID, line number, track type, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | User ID |

### Logic Flow
The procedure starts by checking if the provided line number is 'DTL'. If it is, it retrieves the workflow ID from the TAMS_Workflow table where the line number matches and the workflow type is 'OCCAuth' and the status is active. 

Next, it inserts data into temporary tables #TMP_Endorser and #TMP based on the retrieved workflow ID. The #TMP table contains traction power IDs with their corresponding station names, while the #TMP_Endorser table contains endorser IDs, levels, titles, and roles.

The procedure then selects OCCAuthID from the #TMP_OCCAuthCC temporary table and iterates through each value. For each OCCAuthID, it retrieves endorser ID, level, title, and role ID from the #TMP_Endorser table. 

Based on the retrieved endorser ID, it updates specific fields in the #TMP_OCCAuthCC table with values from the TAMS_OCC_Auth_Workflow table where the OCCAuthID matches.

Finally, it closes all cursors, deallocates memory, and selects all data from the #TMP_OCCAuthCC table for output.

---


<a id='database-reference-sql-sp-tams-occ-getoccauthorisationpfrbyparameters'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthorisationPFRByParameters

### Purpose
This stored procedure retrieves OCC authorisation data for a given set of parameters, including user ID, line, track type, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the data. |

### Logic Flow
The procedure follows these steps:

1. It first checks if the line is 'DTL' and retrieves the workflow ID from the TAMS_Workflow table.
2. If the line is 'DTL', it inserts data into two temporary tables: #TMP and #TMP_Endorser.
3. The procedure then iterates over each OCCAuthID in the #TMP_OCCAuthPFR table, retrieving the corresponding endorser data from the #TMP_Endorser table.
4. For each endorser ID, it updates the relevant fields in the #TMP_OCCAuthPFR table based on the workflow status and action taken by the endorser.
5. Finally, it selects all data from the #TMP_OCCAuthPFR table.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power], [TAMS_Station], [TAMS_OCC_Auth], [TAMS_OCC_Duty_Roster]
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-occ-getoccauthorisationpfrbyparameters-bak20230727'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthorisationPFRByParameters_bak20230727

### Purpose
This stored procedure retrieves and processes OCC authorisation data for a given set of parameters, including user ID, line number, track type, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the data. |
| @Line | nvarchar(10) | The line number for which to retrieve data (optional). |
| @TrackType | nvarchar(50) | The track type for which to retrieve data (optional). |
| @OperationDate | date | The operation date for which to retrieve data. |
| @AccessDate | date | The access date for which to retrieve data. |

### Logic Flow
The procedure follows these steps:

1. It first checks if the line number is 'DTL' and retrieves the corresponding workflow ID.
2. If the line number is 'DTL', it then inserts data into temporary tables #TMP_Endorser and #TMP based on the retrieved workflow ID.
3. The procedure then creates a cursor to iterate over the OCCAuthID column in the #TMP_OCCAuthPFR table.
4. For each OCCAuthID, it iterates over the EndorserID column in the #TMP_Endorser table and updates the corresponding data in #TMP_OCCAuthPFR based on the EndorserLevel.
5. The procedure then checks the WFStatus for each EndorserID and updates the corresponding data in #TMP_OCCAuthPFR accordingly.
6. Finally, it selects all data from #TMP_OCCAuthPFR.

### Data Interactions
* **Reads:** [TAMS_Workflow], [TAMS_Endorser], [TAMS_Traction_Power], [TAMS_OCC_Auth], [TAMS_OCC_Duty_Roster]
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-occ-getoccauthorisationtcbyparameters'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthorisationTCByParameters

### Purpose
This stored procedure retrieves OCC authorisation data for a specified track type and operation date, based on user input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the data. |
| @Line | nvarchar(10) | The line number to filter by (optional). |
| @TrackType | nvarchar(50) | The track type to filter by (optional). |
| @OperationDate | date | The operation date to filter by. |
| @AccessDate | date | The access date to filter by. |

### Logic Flow
1. The procedure starts by creating temporary tables to store intermediate results.
2. It then selects the workflow ID from the TAMS_Workflow table where the line number matches the input parameter and the workflow type is 'OCCAuth' and the effective date is less than or equal to the current date and the expiry date is greater than or equal to the current date.
3. If a line number is provided, it inserts data into the #TMP_Endorser table from the TAMS_Endorser table where the line number matches the input parameter and the workflow ID matches the selected workflow ID.
4. It then selects the traction power IDs from the TAMS_Traction_Power table where the line number matches the input parameter and the track type matches the input parameter, groups by the traction power ID, and stores the results in the #TMP table.
5. The procedure then selects data from the TAMS_OCC_Auth table where the operation date matches the input parameter and the access date matches the input parameter, and joins it with the #TMP table on the traction power ID.
6. It then loops through each OCC authorisation record in the #TMP_OCCAuthTC table and updates the corresponding records in the #TMP_OCCAuthTC table based on the endorser ID.
7. Finally, it selects all data from the #TMP_OCCAuthTC table.

### Data Interactions
* **Reads:** 
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_Traction_Power
	+ TAMS_OCC_Auth
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-occ-getoccauthorisationtcbyparameters-20230216'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthorisationTCByParameters_20230216

### Purpose
This stored procedure retrieves OCC authorisation data for a given set of parameters, including user ID, line, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the OCC authorisation data. |
| @Line | nvarchar(10) | The line for which to retrieve OCC authorisation data (optional). |
| @OperationDate | date | The operation date for which to retrieve OCC authorisation data. |
| @AccessDate | date | The access date for which to retrieve OCC authorisation data. |

### Logic Flow
1. The procedure starts by creating temporary tables to store intermediate results.
2. It then checks if the specified line is 'DTL' and retrieves the workflow ID from the TAMS_Workflow table based on this condition.
3. If the line is 'DTL', it inserts data into the #TMP_Endorser table, which contains endorser information for the specified workflow ID.
4. The procedure then creates a cursor to iterate over the OCCAuthID column in the #TMP_OCCAuthTC table and retrieves the corresponding data from this table.
5. For each OCCAuthID retrieved, it iterates over the #TMP_Endorser table again to retrieve endorser information for that specific OCCAuthID.
6. Based on the endorser ID, it updates the TrainClearCert, AuthForTrackAccess, LineClearCertTOA, and AuthForTrainInsert columns in the #TMP_OCCAuthTC table with the corresponding values from the TAMS_OCC_Auth_Workflow table.
7. After iterating over all OCCAuthIDs, it closes the cursors and deallocates memory for the temporary tables.

### Data Interactions
* **Reads:**
	+ [TAMS_Workflow]
	+ [TAMS_Endorser]
	+ [TAMS_Traction_Power_Detail]
	+ [TAMS_Station]
	+ [TAMS_Traction_Power]
	+ [TAMS_OCC_Auth]
	+ [TAMS_OCC_Auth_Workflow]
* **Writes:**
	+ #TMP
	+ #TMP_Endorser
	+ #TMP_OCCAuthTC

---


<a id='database-reference-sql-sp-tams-occ-getoccauthorisationtcbyparameters-20230216-m'></a>
# Procedure: sp_TAMS_OCC_GetOCCAuthorisationTCByParameters_20230216_M

### Purpose
This stored procedure retrieves OCC authorisation data for a given set of parameters, including user ID, line, operation date, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the OCC authorisation data. |
| @Line | nvarchar(10) | The line for which to retrieve OCC authorisation data (optional). |
| @OperationDate | date | The operation date for which to retrieve OCC authorisation data. |
| @AccessDate | date | The access date for which to retrieve OCC authorisation data. |

### Logic Flow
The procedure follows these steps:

1. It first checks if the `@Line` parameter is 'DTL'. If it is, it retrieves the workflow ID from the `TAMS_Workflow` table where the line matches and the workflow type is 'OCCAuth' and the status is active.
2. It then inserts data into temporary tables `#TMP_Endorser` and `#TMP` based on the retrieved workflow ID and user ID.
3. The procedure then creates a cursor to iterate over the OCC authorisation IDs in the `#TMP_OCCAuthTC` table.
4. For each OCC authorisation ID, it iterates over the endorser IDs in the `#TMP_Endorser` table and updates the corresponding fields in the `#TMP_OCCAuthTC` table based on the endorser level and title.
5. The procedure then closes the cursor and deallocates the temporary tables.

### Data Interactions
* **Reads:** 
	+ [TAMS_Workflow]
	+ [TAMS_Endorser]
	+ [TAMS_Traction_Power_Detail]
	+ [TAMS_Station]
	+ [TAMS_Traction_Power]
	+ [TAMS_OCC_Auth]
	+ [TAMS_OCC_Auth_Workflow]
	+ [TAMS_OCC_Duty_Roster]
* **Writes:** 
	+ #TMP_Endorser
	+ #TMP
	+ #TMP_OCCAuthTC

---


<a id='database-reference-sql-sp-tams-occ-getocctvfackbyparameters'></a>
# Procedure: sp_TAMS_OCC_GetOCCTVFAckByParameters

### Purpose
This stored procedure retrieves and updates data from various tables to provide a comprehensive view of TVF (Traffic Video Feedback) acknowledgments for a specific set of parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the data. |
| @Line | nvarchar(10) | The line number to filter the data (default is NULL). |
| @TrackType | nvarchar(50) | The track type to filter the data (default is NULL). |
| @OperationDate | date | The operation date to filter the data. |
| @AccessDate | date | The access date to filter the data. |

### Logic Flow
The procedure follows these steps:

1. It checks if the `@Line` parameter is 'DTL'. If it is, it proceeds with the filtering and processing of the data.
2. It retrieves the count of TVF acknowledgments for the specified `@AccessDate`.
3. If there are no acknowledgments, it truncates a temporary table (`#TMP_TVF_ToUpdate`) and inserts new records from the `TAMS_TAR` table based on the `TrackType` and `OperationDate`.
4. It loops through each record in the `#TMP_TVF_ToUpdate` table and updates the corresponding records in the `#TMP_OCCTVF_Ack` table.
5. If there are no acknowledgments, it inserts new records into the `#TMP_OCCTVF_Ack` table directly.

### Data Interactions
* **Reads:**
	+ [TAMS_TAR]
	+ [TAMS_TAR_TVF]
	+ [TAMS_TVF_Acknowledge]
	+ [TAMS_Station]
	+ [TAMS_User]
* **Writes:**
	+ #TMP_Station
	+ #TMP_OCCTVF_Ack
	+ #TMP_TVF_ToUpdate

---


<a id='database-reference-sql-sp-tams-occ-getocctvfackbyparameters-preview'></a>
# Procedure: sp_TAMS_OCC_GetOCCTVFAckByParameters_Preview

### Purpose
This stored procedure retrieves a preview of TVF acknowledge data for a specified operation date, line, track type, and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | User ID (not used in this procedure) |

### Logic Flow
1. The procedure starts by checking if the input parameter `@Line` is 'DTL'. If it is, it proceeds with the logic.
2. It then retrieves the count of TVF acknowledge records for the specified operation date using a SELECT statement.
3. If there are any records found, it inserts data into temporary tables to store station information and TVF acknowledge details.
4. The procedure then joins the TAMS_TVF_Acknowledge table with the #TMP_Station temporary table on the StationId column and filters for records where OperationDate equals @OperationDate and AccessDate equals @AccessDate.
5. It selects specific columns from this joined table, including SNO, ID, AccessDate, OperationDate, StationId, StationName, TVFDirection1, TVFDirection2, TVFMode, AcknowledgedBy, AcknowledgedOn, TVFOnTime, OperatedBy, VerifiedBy, and VerifiedOn.
6. The selected data is then inserted into the #TMP_OCCTVF_Ack temporary table in order of StationId ASC.
7. Finally, the procedure drops the temporary tables.

### Data Interactions
* **Reads:** [TAMS_TVF_Acknowledge], [TAMS_Station]
* **Writes:** #TMP_Station, #TMP_OCCTVF_Ack

---


<a id='database-reference-sql-sp-tams-occ-getocctvfackfromtablebyparameters'></a>
# Procedure: sp_TAMS_OCC_GetOCCTVFAckFromTableByParameters

### Purpose
This stored procedure retrieves data from various tables to generate a report of TVF (Traffic Video Feedback) acknowledgments for a specific date range, taking into account user permissions and station IDs.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user requesting the data. |
| @Line | nvarchar(10) | The line number (DTL or other). |
| @OperationDate | date | The operation date for which to retrieve data. |
| @AccessDate | date | The access date for which to retrieve data. |

### Logic Flow
1. If the `@Line` parameter is 'DTL', the procedure proceeds with retrieving data.
2. It counts the number of TVF acknowledgments for the specified `@OperationDate`.
3. If no acknowledgments are found, it truncates a temporary table (`#TMP_TVF_ToUpdate`) and inserts new records from the `TAMS_TAR` table based on the `AccessDate`.
4. The procedure then iterates through each record in the `#TMP_TVF_ToUpdate` table, updating the corresponding records in the `#TMP_OCCTVF_Ack` table.
5. If no acknowledgments are found for the specified line and date range, it inserts new records into both tables.

### Data Interactions
* **Reads:**
	+ [TAMS_TAR]
	+ [TAMS_TVF_Acknowledge]
	+ [TAMS_Station]
	+ [TAMS_User]
* **Writes:**
	+ #TMP_OCCTVF_Ack
	+ #TMP_TVF_ToUpdate

---


<a id='database-reference-sql-sp-tams-occ-getocctvfackremarkbyid'></a>
# Procedure: sp_TAMS_OCC_GetOCCTVFAckRemarkById

### Purpose
This stored procedure retrieves a specific acknowledgement record for a TVF (Transaction Video Feedback) from the TAMS database, including relevant details such as ID, remark, and creation/update timestamps.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ID | INT | The ID of the TVF acknowledgement to retrieve |

### Logic Flow
1. The procedure starts by declaring two variables: `@TVFMode` and `@TVFDirection`, which are not used in the provided code snippet.
2. It then selects data from the `TAMS_TVF_Ack_Remark` table, aliasing it as `tvf`, and joins it with the `TAMS_User` table on the `CreatedBy` column.
3. The procedure filters the results to only include records where the `TVFAckId` matches the provided `@ID`.
4. It returns a list of columns including `ID`, `TVFAckId`, `Remark`, `CreatedOn`, `CreatedBy`, `UpdatedOn`, and `UpdatedBy`.

### Data Interactions
* **Reads:** TAMS_TVF_Ack_Remark, TAMS_User

---


<a id='database-reference-sql-sp-tams-occ-getocctartvfbyparameters'></a>
# Procedure: sp_TAMS_OCC_GetOCCTarTVFByParameters

### Purpose
This stored procedure retrieves and updates TVF (Traffic Volume Forecast) data for a specified station and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @StationId | int | The ID of the station to retrieve TVF data for. |
| @AccessDate | date | The access date to filter TVF data by. |

### Logic Flow
1. The procedure starts by clearing temporary tables #TMP_TVF and #TMP_TAR_TVF.
2. It then inserts data from TAMS_TAR, TAMS_TAR_TVF, and TAMS_TOA tables into the temporary tables based on the specified station ID and access date.
3. A cursor is created to iterate through the data in #TMP_TVF.
4. For each row in the cursor, it checks if a corresponding record exists in #TMP_TAR_TVF with the same ID. If not, it inserts a new record into #TMP_TAR_TVF based on the TVF direction ('XB' or 'BB').
5. If a corresponding record does exist in #TMP_TAR_TVF, it updates the existing record by setting the appropriate bit for the TVF direction.
6. Finally, it selects all records from #TMP_TAR_TVF and deallocates the cursor.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_TVF, TAMS_TOA tables
* **Writes:** #TMP_TVF, #TMP_TAR_TVF tables

---


<a id='database-reference-sql-sp-tams-occ-gettarsectorbylineandtaraccessdate'></a>
# Procedure: sp_TAMS_OCC_GetTarSectorByLineAndTarAccessDate

The procedure retrieves data from the TAMS database for a specific line and access date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to retrieve data for. Can be either 'DTL' or 'NEL'. |
| @AccessDate | nvarchar(50) | The access date to filter results by. |

### Logic Flow
1. The procedure first checks if the provided line is 'DTL'.
2. If it is, the procedure retrieves data from the TAMS database for the specified line and access date.
3. The retrieved data includes sector IDs, traction power IDs, and other relevant information.
4. The results are ordered by traction power ID in ascending order.
5. If the provided line is not 'DTL', the procedure checks if it is 'NEL'.
6. If it is, the procedure retrieves data from the TAMS database for the specified line and access date.
7. The retrieved data includes sector IDs, power sector IDs, and other relevant information.
8. The results are ordered by power sector ID in ascending order.

### Data Interactions
* **Reads:** tams_tar, TAMS_TAR_Sector, TAMS_Traction_Power_Detail, TAMS_TAR_Sector_reno, TAMS_Power_Sector

---


<a id='database-reference-sql-sp-tams-occ-gettractionpowerdetailsbyidandtype'></a>
# Procedure: sp_TAMS_OCC_GetTractionPowerDetailsByIdAndType

### Purpose
This stored procedure retrieves traction power details by ID and type, filtering for active records with a specific sector type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ID | int | The ID of the traction power detail to retrieve. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Traction_Power_Detail table.
2. It filters the records based on the provided ID, ensuring only matching records are returned.
3. Additionally, it filters for records with a specific sector type ('Sector') and ensures they are active (IsActive = 1).
4. The results are ordered by the ID in ascending order.

### Data Interactions
* **Reads:** TAMS_Traction_Power_Detail

---


<a id='database-reference-sql-sp-tams-occ-gettractionspowerbyline'></a>
# Procedure: sp_TAMS_OCC_GetTractionsPowerByLine

### Purpose
This stored procedure retrieves traction power data for a specified line, filtered by effective and expiry dates, and order status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | nvarchar(10) | The line number to retrieve traction power data for. |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_Traction_Power table.
2. It filters the results based on the provided line number, ensuring that only records with an effective date within the current date range and an active status are included.
3. The results are ordered by the order status in ascending order.

### Data Interactions
* **Reads:** [dbo].[TAMS_Traction_Power]
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-occ-getworkflowbylineandtype'></a>
# Procedure: sp_TAMS_OCC_GetWorkflowByLineAndType

### Purpose
This stored procedure retrieves workflow information for a specific line and type, filtering by effective date and active status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @Type | NVARCHAR(50) | The workflow type to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Workflow table.
2. It filters the results based on the provided Line and Type parameters, ensuring that only records with matching values are returned.
3. The EffectiveDate and ExpiryDate columns are filtered to ensure that only records within the current date range (i.e., where EffectiveDate is less than or equal to the current date and ExpiryDate is greater than or equal to the current date) are included.
4. Finally, the procedure orders the results by the ID column.

### Data Interactions
* **Reads:** TAMS_Workflow table

---


<a id='database-reference-sql-sp-tams-occ-inserttvfackbyparameters'></a>
# Procedure: sp_TAMS_OCC_InsertTVFAckByParameters

### Purpose
This stored procedure performs an insert operation into the TAMS_TVF_Acknowledge table, creating a new record for TVF acknowledgement. It also updates existing records and inserts audit logs.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | Date of the operation |
| @AccessDate | datetime | Date of access |
| @UserID | int | ID of the user performing the action |
| @StationId | int | ID of the station involved |
| @TVFMode | varchar(10) | Mode of TVF |
| @TVFDirection1 | bit | Direction 1 of TVF |
| @TVFDirection2 | bit | Direction 2 of TVF |

### Logic Flow
The procedure starts by declaring a new ID variable. It then attempts to execute the following steps within a transaction block:

1. Insert a new record into TAMS_TVF_Acknowledge with the provided parameters.
2. Select the newly generated ID from the inserted record.
3. Update existing records in TAMS_TVF_Acknowledge where TVFMode is 'Select' by setting AcknowledgedBy, AcknowledgedOn, CreatedOn, and CreatedBy to NULL.
4. Insert an audit log for the new record into TAMS_TVF_Acknowledge_Audit.

If any errors occur during this process, the transaction is rolled back; otherwise, it is committed.

### Data Interactions
* Reads: TAMS_TVF_Acknowledge, TAMS_TVF_Acknowledge_Audit
* Writes: TAMS_TVF_Acknowledge

---


<a id='database-reference-sql-sp-tams-occ-inserttodutyoccrostertable'></a>
# Procedure: sp_TAMS_OCC_InsertToDutyOCCRosterTable

### Purpose
This stored procedure inserts or updates a new record to the TAMS_OCC_Duty_Roster table based on the provided data from the @TAMS_OCC_DutyRoster READONLY parameter.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_DutyRoster | [dbo].[TAMS_OCC_DutyRoster] READONLY | The input data to be inserted or updated in the TAMS_OCC_Duty_Roster table. |

### Logic Flow
The procedure checks if a record with the same operation date, shift, line, and track type already exists in the TAMS_OCC_Duty_Roster table for the provided @TAMS_OCC_DutyRoster READONLY parameter. If no matching record is found, it inserts a new record into the TAMS_OCC_Duty_Roster table along with an audit log entry. If a matching record is found, it updates the existing record in the TAMS_OCC_Duty_Roster table and also creates an audit log entry.

### Data Interactions
* **Reads:** @TAMS_OCC_DutyRoster
* **Writes:** TAMS_OCC_Duty_Roster, TAMS_OCC_Duty_Roster_Audit

---


<a id='database-reference-sql-sp-tams-occ-inserttodutyoccrostertable-20221116'></a>
# Procedure: sp_TAMS_OCC_InsertToDutyOCCRosterTable_20221116

### Purpose
This stored procedure inserts or updates a record in the TAMS_OCC_Duty_Roster table based on the provided data from the @TAMS_OCC_DutyRoster READONLY parameter.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_DutyRoster | [dbo].[TAMS_OCC_DutyRoster] READONLY | The input data to be inserted or updated in the TAMS_OCC_Duty_Roster table. |

### Logic Flow
The procedure checks if a record with the same operation date, shift, and line exists in the TAMS_OCC_Duty_Roster table. If no record is found, it inserts a new record into the table along with an audit log entry. If a record is found, it updates the existing record with the provided data and also creates an audit log entry.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_OCC_Duty_Roster_Audit
* **Writes:** TAMS_OCC_Duty_Roster

---


<a id='database-reference-sql-sp-tams-occ-inserttodutyoccrostertable-20221116-m'></a>
# Procedure: sp_TAMS_OCC_InsertToDutyOCCRosterTable_20221116_M

### Purpose
This stored procedure inserts or updates a record in the TAMS_OCC_Duty_Roster table based on the provided data from the @TAMS_OCC_DutyRoster READONLY parameter.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_DutyRoster | [dbo].[TAMS_OCC_DutyRoster] READONLY | The input data to be inserted or updated in the TAMS_OCC_Duty_Roster table. |

### Logic Flow
The procedure checks if a record with the same operation date, shift, and line already exists in the TAMS_OCC_Duty_Roster table. If no record is found, it inserts a new record into the table along with an audit log entry. If a record is found, it updates the existing record with the provided data and also creates an audit log entry.

### Data Interactions
* **Reads:** @TAMS_OCC_DutyRoster (the input data)
* **Writes:** TAMS_OCC_Duty_Roster (for insertion or update), TAMS_OCC_Duty_Roster_Audit (for audit log entries)

---


<a id='database-reference-sql-sp-tams-occ-inserttooccauthtable'></a>
# Procedure: sp_TAMS_OCC_InsertToOCCAuthTable

### Purpose
This stored procedure inserts data from a temporary table (@TAMS_OCC_Auth) into the TAMS_OCC_Auth table, effectively updating or adding new records to the OCCAuthStatusId column.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_Auth | [dbo].[TAMS_OCC_Auth] READONLY | A temporary table containing data to be inserted into TAMS_OCC_Auth. |

### Logic Flow
1. The procedure selects all columns from the @TAMS_OCC_Auth table.
2. It then inserts these selected values into the TAMS_OCC_Auth table.

### Data Interactions
* **Reads:** TAMS_OCC_Auth, @TAMS_OCC_Auth
* **Writes:** TAMS_OCC_Auth

---


<a id='database-reference-sql-sp-tams-occ-inserttooccauthworkflowtable'></a>
# Procedure: sp_TAMS_OCC_InsertToOCCAuthWorkflowTable

This procedure inserts data into the TAMS_OCC_Auth_Workflow table from a temporary storage location.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TAMS_OCC_Auth_Workflow | [dbo].[TAMS_OCC_Auth_Workflow] READONLY | Temporary storage location for data to be inserted |

### Logic Flow
1. The procedure takes a temporary storage location, @TAMS_OCC_Auth_Workflow, which contains data to be inserted into the TAMS_OCC_Auth_Workflow table.
2. The procedure selects all columns from this temporary storage location and inserts them into the TAMS_OCC_Auth_Workflow table.

### Data Interactions
* **Reads:** TAMS_OCC_Auth_Workflow
* **Writes:** TAMS_OCC_Auth_Workflow

---


<a id='database-reference-sql-sp-tams-occ-rejecttvfackbyparameters-pfr'></a>
# Procedure: sp_TAMS_OCC_RejectTVFAckByParameters_PFR

### Purpose
This stored procedure performs a rejection of TVF acknowledgement by parameters, updating the TAMS_TVF_Acknowledge table and creating an audit record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | The date of the operation. |
| @AccessDate | datetime | The access date. |
| @UserID | int | The ID of the user performing the action. |
| @StationId | int | The ID of the station. |
| @TVFMode | varchar(10) | The mode of TVF. |
| @TVFDirection1 | bit | The direction of TVF 1. |
| @TVFDirection2 | bit | The direction of TVF 2. |

### Logic Flow
The procedure starts by beginning a transaction. It then updates the TAMS_TVF_Acknowledge table with the provided parameters, setting the TVF mode and directions, and marking it as unverified. After updating the table, an audit record is created in the TAMS_TVF_Acknowledge_Audit table for each affected row, including the user ID, current date and time, action type, and other relevant details.

### Data Interactions
* **Reads:** TAMS_TVF_Acknowledge, TAMS_TVF_Acknowledge_Audit
* **Writes:** TAMS_TVF_Acknowledge

---


<a id='database-reference-sql-sp-tams-occ-updateoccauthorisationccbyparameters'></a>
# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationCCByParameters

### Purpose
This stored procedure updates the OCC authorization status for a given ID, based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The user ID performing the update. |
| @OCCAuthID | int | The ID of the OCC authorization to be updated. |
| @OCCLevel | int | The level of the OCC authorization (used for conditional updates). |
| @Line | nvarchar(10) | The line number associated with the OCC authorization. |
| @TrackType | nvarchar(50) | The track type associated with the OCC authorization (optional). |
| @RemarksCC | nvarchar(1000) | The remarks for the OCC authorization update (optional). |

### Logic Flow
1. Check if the line is 'DTL'. If true, proceed to the DTL logic block.
2. Within the DTL logic block:
   a. Begin a transaction.
   b. Retrieve the workflow ID and endorser ID associated with the OCC authorization.
   c. Update the OCC authorization status in the TAMS_OCC_Auth_Workflow table based on the OCC level.
   d. Insert a new record into the TAMS_OCC_Auth_Workflow_Audit table to log the update action.
   e. Insert a new record into the TAMS_OCC_Auth_Audit table to log the update details.
   f. Commit the transaction.

3. If the line is not 'DTL', skip to the end of the procedure.

### Data Interactions
* Reads: 
  * [TAMS_Workflow]
  * [TAMS_Endorser]
  * [TAMS_OCC_Auth]
  * [TAMS_OCC_Auth_Workflow]
  * [TAMS_OCC_Auth_Workflow_Audit]
  * [TAMS_OCC_Auth_Audit]
* Writes: 
  * [TAMS_OCC_Auth_Workflow]
  * [TAMS_OCC_Auth_Audit]

---


<a id='database-reference-sql-251-sp-tams-occ-updateoccauthorisationnelbyparametersmd'></a>
This stored procedure is used to update the status of an OCC (Offshore Company Code) authentication record. The procedure takes into account various levels of approval and validation, ensuring that only authorized personnel can make changes.

Here's a step-by-step breakdown of the logic:

1. **Check for existing workflow**: Before starting the process, the procedure checks if there is already an active workflow associated with the OCC authentication record.
2. **Determine current status**: The procedure determines the current status of the OCC authentication record and compares it to the desired new status.
3. **Validate user permissions**: The procedure validates the user's permissions to make changes to the OCC authentication record, ensuring that only authorized personnel can proceed.
4. **Update workflow status**: If the user is authorized, the procedure updates the workflow status to reflect the new approval level and any associated validation requirements.
5. **Insert audit records**: After updating the workflow status, the procedure inserts audit records into two separate tables: `TAMS_OCC_Auth_Workflow_Audit` and `TAMS_OCC_Auth_Audit`. These records capture the changes made to the OCC authentication record, including the user who made the change, the date and time of the update, and any relevant details.
6. **Commit or rollback transaction**: Finally, the procedure either commits the transaction (if all updates are successful) or rolls back the transaction (if any errors occur).

The logic is designed to ensure that changes to OCC authentication records are properly validated, authorized, and audited, providing a secure and transparent record-keeping system.

**Key considerations:**

* The procedure uses a TRY-CATCH block to handle any errors that may occur during execution.
* It validates user permissions using a combination of checks, including access controls and validation rules.
* The procedure updates the workflow status in real-time, ensuring that changes are reflected immediately.
* Audit records are inserted into two separate tables, providing a comprehensive record of all changes made to the OCC authentication record.

---


<a id='database-reference-sql-sp-tams-occ-updateoccauthorisationnelbyparameters-bak20230711'></a>
# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationNELByParameters_bak20230711

### Purpose
This stored procedure updates the OCC Authorisation for a given NEL by processing the specified workflow level and endorser ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The user ID performing the update. |
| @OCCAuthID | int | The ID of the OCC Authorisation to be updated. |
| @OCCLevel | int | The workflow level to process (1-12). |
| @Line | nvarchar(10) | The line number for which the update is being performed. |
| @Remarks | nvarchar(100) | Optional remarks for the update. |
| @SelectionValue | nvarchar(50) | The new status value for OCC Auth workflow level 15. |

### Logic Flow
The procedure follows these steps:

1. Check if the line number matches 'NEL'. If true, proceed with the update.
2. Begin a transaction to ensure data consistency.
3. Declare variables to store endorser IDs and workflow IDs.
4. For each OCC Level (1-12), perform the following actions:
	* Retrieve the workflow ID for the specified level.
	* Update the corresponding OCC Auth workflow status to 'Completed' if it's not already set.
	* Insert a new OCC Auth workflow record with the next endorser ID and pending status.
	* Update the OCC Auth record with the new status ID, remarks, and updated timestamps.
5. If the line number matches 'NEL', also perform additional updates:
	* Insert an audit record for each OCC Auth workflow update.
	* Insert another audit record for each OCC Auth update with a specific action type ('I' or 'U').
6. Commit the transaction if all updates are successful.

### Data Interactions
* Reads: [TAMS_Workflow], [TAMS_Endorser], [TAMS_OCC_Auth], [TAMS_OCC_Auth_Workflow], [TAMS_OCC_Auth_Workflow_Audit], and [TAMS_OCC_Auth_Audit].
* Writes: [TAMS_OCC_Auth_Workflow] and [TAMS_OCC_Auth].

---


<a id='database-reference-sql-sp-tams-occ-updateoccauthorisationnelremark'></a>
# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationNELRemark

### Purpose
This stored procedure updates the remark field for a specific OCC authorisation, along with the user ID and current date, in the TAMS_OCC_Auth table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user making the update. |
| @OCCAuthID | int | The ID of the OCC authorisation being updated. |
| @Line | nvarchar(10) | Not used in this procedure ( possibly a placeholder for future use). |
| @TrackType | nvarchar(50) | Not used in this procedure (possibly a placeholder for future use). |
| @Remarks | nvarchar(100) | The new remark to be stored. |

### Logic Flow
1. The procedure starts by updating the remark field of the specified OCC authorisation ID.
2. It also updates the user ID and current date fields with the provided values.

### Data Interactions
* **Reads:** None explicitly listed, but it is assumed that the system retrieves data from other tables as needed for this update operation.
* **Writes:** 
  * TAMS_OCC_Auth table: Updated with new remark value, updated on field, and updated by field.

---


<a id='database-reference-sql-sp-tams-occ-updateoccauthorisationpfrbyparameters'></a>
# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationPFRByParameters

### Purpose
This stored procedure updates the OCC Authorisation PFR status for a given set of parameters, including user ID, OCC Auth ID, OCC level, line, track type, remarks PFR, selection value, and station name.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user performing the update. |
| @OCCAuthID | int | The ID of the OCC Auth to be updated. |
| @OCCLevel | int | The level of the OCC Auth being updated. |
| @Line | nvarchar(10) | The line number associated with the OCC Auth. |
| @TrackType | nvarchar(50) | The type of track for the OCC Auth. |
| @RemarksPFR | nvarchar(1000) | The remarks PFR for the OCC Auth. |
| @SelectionValue | nvarchar(50) | The selection value for the OCC Auth. |
| @StationName | nvarchar(50) | The name of the station associated with the OCC Auth. |

### Logic Flow
The procedure follows a hierarchical structure based on the OCC level, updating the status and remarks accordingly.

1. For OCC levels 4-6, it updates the WFStatus to 'Completed' or 'Pending', sets the StationId, ActionOn, and ActionBy fields, and inserts a new record into TAMS_OCC_Auth_Workflow.
2. For OCC levels 7-12, it updates the WFStatus to 'Completed' or 'Pending', sets the StationId, ActionOn, and ActionBy fields, and inserts a new record into TAMS_OCC_Auth_Workflow.
3. For OCC level 13, it updates the WFStatus to 'Completed' or 'Pending', sets the StationId, ActionOn, and ActionBy fields, and inserts a new record into TAMS_OCC_Auth_Workflow.
4. For OCC levels 15-17, it updates the WFStatus to 'Completed' or 'Pending', sets the StationId, ActionOn, and ActionBy fields, and inserts a new record into TAMS_OCC_Auth_Workflow.
5. It also updates the PFRRemark field in TAMS_OCC_Auth for all OCC levels.

### Data Interactions
* Reads: TAMS_Workflow, TAMS_Endorser, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_OCC_Auth_Audit, TAMS_OCC_Auth_Workflow_Audit, TAMS_Station.
* Writes: TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_OCC_Auth_Audit, TAMS_OCC_Auth_Workflow_Audit.

---


<a id='database-reference-sql-sp-tams-occ-updateoccauthorisationpfrbyparameters-bak20230711'></a>
# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationPFRByParameters_bak20230711

The purpose of this stored procedure is to update the OCC Authorisation PFR status for a given set of parameters.

### Parameters

| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user performing the operation. |
| @OCCAuthID | int | The ID of the OCC Authorisation to be updated. |
| @OCCLevel | int | The level of the OCC Authorisation. |
| @Line | nvarchar(10) | The line number for which the update is being performed. |
| @RemarksPFR | nvarchar(100) | The remarks for the PFR status. |
| @SelectionValue | nvarchar(50) | The selected value for the OCC Authorisation level. |
| @StationName | nvarchar(50) | The name of the station associated with the update. |

### Logic Flow

The procedure follows a series of conditional statements based on the value of `@OCCLevel`. For each level, it performs the following steps:

1.  Retrieves the workflow ID and endorser ID from the TAMS_Workflow and TAMS_Endorser tables.
2.  Updates the OCC Authorisation status in the TAMS_OCC_Auth table based on the selected value for `@OCCLevel`.
3.  Inserts a new record into the TAMS_OCC_Auth_Workflow table with the updated status and station ID.
4.  If the update is for level 18, it updates the FISTestResult field in the TAMS_OCC_Auth_Workflow table.

### Data Interactions

*   **Reads:** TAMS_Workflow, TAMS_Endorser, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
*   **Writes:** TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow

---


<a id='database-reference-sql-sp-tams-occ-updateoccauthorisationtcbyparameters'></a>
# Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationTCByParameters

### Purpose
This stored procedure updates the OCC Authorisation status for a given Traction Centre (TC) based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | int | The ID of the user performing the update. |
| @OCCAuthID | int | The ID of the OCC Authorisation to be updated. |
| @OCCLevel | int | The level of the OCC Authorisation (1-20). |
| @Line | nvarchar(10) | The line number for the Traction Centre. |
| @TrackType | nvarchar(50) | The track type for the Traction Centre. |
| @SelectionValue | nvarchar(50) | The new status value for the OCC Authorisation (used for levels 11-20). |

### Logic Flow
1. Check if the line number is 'DTL'. If true, proceed with the update.
2. Begin a transaction to ensure data consistency.
3. Retrieve the workflow ID and endorser ID for the given line number and track type.
4. Update the OCC Authorisation status in the TAMS_OCC_Auth_Workflow table based on the provided level.
5. Insert a new record into the TAMS_OCC_Auth_Workflow_Audit table to log the update action.
6. If the level is 11 or higher, insert another record into the TAMS_OCC_Auth_Workflow_Audit table for the pending status.
7. Update the OCC Authorisation status in the TAMS_OCC_Auth table based on the new value.
8. Insert a record into the TAMS_OCC_Auth_Audit table to log the update action.
9. Commit the transaction.

### Data Interactions
* Reads: [TAMS_Workflow], [TAMS_Endorser], [TAMS_OCC_Auth], [TAMS_OCC_Auth_Workflow], [TAMS_OCC_Auth_Workflow_Audit]
* Writes: [TAMS_OCC_Auth_Workflow], [TAMS_OCC_Auth]

---


<a id='database-reference-sql-sp-tams-occ-updatetvfackbyparameters-cc'></a>
# Procedure: sp_TAMS_OCC_UpdateTVFAckByParameters_CC

### Purpose
This stored procedure updates the TVF acknowledge status for a specific station based on provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | The date of operation. |
| @AccessDate | datetime | The access date. |
| @UserID | int | The user ID. |
| @StationId | int | The station ID. |
| @TVFMode | varchar(10) | The TVF mode. |
| @TVFDirection1 | bit | The first direction of the TVF. |
| @TVFDirection2 | bit | The second direction of the TVF. |

### Logic Flow
The procedure starts by beginning a transaction. It then updates the TAMS_TVF_Acknowledge table with the provided parameters for the specified station and operation date. If an update is successful, it inserts a new record into the TAMS_TVF_Acknowledge_Audit table with the updated information.

If any errors occur during the procedure, it catches the error message and rolls back the transaction to maintain data consistency.

### Data Interactions
* **Reads:** TAMS_TVF_Acknowledge, TAMS_TVF_Acknowledge_Audit
* **Writes:** TAMS_TVF_Acknowledge

---


<a id='database-reference-sql-sp-tams-occ-updatetvfackbyparameters-pfr'></a>
# Procedure: sp_TAMS_OCC_UpdateTVFAckByParameters_PFR

The procedure updates TVF acknowledge records based on provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @OperationDate | datetime | The date of the operation. |
| @AccessDate | datetime | The access date. |
| @UserID | int | The ID of the user performing the action. |
| @StationId | int | The ID of the station. |
| @TVFMode | varchar(10) | The mode of TVF. |
| @TVFDirection1 | bit | The direction of TVF 1. |
| @TVFDirection2 | bit | The direction of TVF 2. |

### Logic Flow
The procedure first attempts to execute the update operation within a transaction block. If successful, it updates the TAMS_TVF_Acknowledge table with the provided values and commits the transaction. If an error occurs during this process, the transaction is rolled back.

1. The procedure starts by beginning a new transaction.
2. It then selects the records from TAMS_TVF_Acknowledge that match the specified StationId, OperationDate, and AccessDate.
3. For each matching record, it updates the TVFMode, TVFDirection1, and TVFDirection2 fields with the provided values.
4. The procedure also updates the OperatedBy field with the @UserID value and sets the TVFOnTime to the current date and time.
5. After updating the records, the procedure inserts a new record into TAMS_TVF_Acknowledge_Audit for each matching record.
6. The audit record includes information about the action performed (O), the ID of the user performing the action (@UserID), the current date and time (GETDATE()), and other relevant fields.

### Data Interactions
* **Reads:** TAMS_TVF_Acknowledge, TAMS_TVF_Acknowledge_Audit
* **Writes:** TAMS_TVF_Acknowledge

---


<a id='database-reference-sql-sp-tams-opd-onload'></a>
# Procedure: sp_TAMS_OPD_OnLoad

### Purpose
This stored procedure performs data loading and filtering for track operations on a daily basis, taking into account the current date and time.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Specifies the type of line (DTL or NB) to process. |
| @TrackType | NVARCHAR(50) | Specifies the track type for which data is being loaded. |

### Logic Flow
The procedure starts by determining the current date and time, as well as a cutoff time for operations. It then checks if the current time exceeds the cutoff time; if so, it sets the operation date to the current date and the access date to the next day. Otherwise, it sets the operation date to the previous day and the access date to the current date.

The procedure then creates a temporary table #TmpOPD to store data from TAMS_Sector and TAMS_Track_Coordinates tables based on the specified line and track type. It truncates the existing data in the temporary table and inserts new data into it.

After loading the data, the procedure filters the data by direction (BB or NB) and horizontal coordinates, and orders the results by sector ID. Finally, it returns the operation date and access date.

### Data Interactions
* **Reads:** TAMS_Sector, TAMS_Track_Coordinates tables.
* **Writes:** #TmpOPD table.

---


<a id='database-reference-sql-sp-tams-rgs-ackreg'></a>
# Procedure: sp_TAMS_RGS_AckReg

### Purpose
This stored procedure acknowledges a registration request for a Train Access Management System (TAMS) and sends an SMS notification to the registered mobile number.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR (Train Access Request) being acknowledged. |
| @UserID | NVARCHAR(500) | The ID of the user who initiated the registration request. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that stores the SMS message to be sent. |

### Logic Flow
1. The procedure checks if a transaction has already been started. If not, it starts one.
2. It retrieves the TOA status and track type from the TAMS_TAR and TAMS_TOA tables based on the provided TAR ID.
3. If the TOA status is 1 (pending), it updates the TOA status to 2 (acknowledged) in the TAMS_TOA table.
4. It checks if a Depot Auth record already exists for the given TAR ID. If yes, it returns without inserting a new record.
5. Otherwise, it inserts a new Depot Auth record into the TAMS_Depot_Auth table with the provided track type and user ID.
6. It also inserts records into the TAMS_Depot_Auth_Workflow and TAMS_Depot_DTCAuth_SPKS tables.
7. Based on the track type, it constructs an SMS message to be sent to the registered mobile number.
8. If the SMS message is not empty, it sends the SMS using the sp_api_send_sms stored procedure.
9. Finally, it returns the constructed SMS message or an error message if any errors occur during execution.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow, TAMS_Depot_DTCAuth_SPKS
* Writes: TAMS_TOA (TOA status), TAMS_Depot_Auth (new record), TAMS_Depot_Auth_Workflow (workflow ID), TAMS_Depot_DTCAuth_SPKS (SPKSID)

---


<a id='database-reference-sql-sp-tams-rgs-ackreg-20221107'></a>
# Procedure: sp_TAMS_RGS_AckReg_20221107

### Purpose
This stored procedure acknowledges a registration and sends an SMS notification to the registered user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Target Area Record) being acknowledged. |
| @UserID	| NVARCHAR(500) | The ID of the user who is sending the acknowledgement. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets an internal flag to indicate that a new transaction has begun.
2. It then updates the TOAStatus in the TAMS_TOA table to 2 (Acknowledged) and sets the AckRegisterTime and UpdatedOn fields to the current date and time, along with the ID of the user who made the update.
3. The procedure then retrieves additional information from the TAMS_TAR table based on the TARID provided, including the TARNo, Line, AckRegTime, and MobileNo (HPNo).
4. Depending on the value of the Line field, it constructs an SMS message that includes the TARNo, AckRegTime, and current date.
5. If the HPNo is not empty, it sends the SMS using the sp_api_send_sms stored procedure.
6. If there are any errors during this process, it sets a message indicating the error and exits the procedure.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR
* **Writes:** TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-ackreg-20230807'></a>
# Procedure: sp_TAMS_RGS_AckReg_20230807

### Purpose
This stored procedure acknowledges a registration and sends an SMS notification to the user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | TAR ID of the registration to be acknowledged |
| @UserID	| NVARCHAR(500) | User ID who is sending the acknowledgement |

### Logic Flow

1. The procedure starts by checking if a transaction has already been started. If not, it sets an internal flag and begins a new transaction.
2. It then updates the TOAStatus of the TAMS_TOA table to 2 (acknowledged) for the specified TAR ID.
3. Next, it retrieves additional information about the registration from the TAMS_TAR table, including the TAR No, Line, Ack Register Time, and Mobile No.
4. Based on the Line value, it constructs an SMS message with a specific format.
5. If the Mobile No is not empty, it sends the SMS using the sp_api_send_sms stored procedure.
6. After sending the SMS, it checks for any errors that may have occurred during this process.
7. If no errors were found, it commits the transaction and returns a success message. Otherwise, it rolls back the transaction and returns an error message.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR
* **Writes:** TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-ackreg-20230807-m'></a>
# Procedure: sp_TAMS_RGS_AckReg_20230807_M

### Purpose
This stored procedure acknowledges a registration request for a TAMS (Tracking and Management System) user, updating the status of their TOA (Temporary Authorization) record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID		| BIGINT | TAR ID of the user requesting registration |
| @UserID		| NVARCHAR(500) | User ID of the person acknowledging the registration request |
| @Message	| NVARCHAR(500) | Output message to be returned |

### Logic Flow
1. The procedure checks if a transaction has already been started and sets an internal flag (@IntrnlTrans) accordingly.
2. It retrieves the current TOA status for the specified TAR ID from the TAMS_TAR and TAMS_TOA tables.
3. If the TOA status is 1 (pending), it updates the TOA status to 2 (approved) in the TAMS_TOA table, setting the AckRegisterTime and UpdatedOn fields to the current date and time, and updating the UpdatedBy field with the user ID provided.
4. It retrieves additional information about the TAR record from the TAMS_TAR table, including the TAR No, Line, AckRegTime, and MobileNo (HPNo).
5. Based on the value of the Line field, it constructs a message to be sent via SMS to the user's mobile number using the sp_api_send_sms stored procedure.
6. If an error occurs during SMS sending, it sets the @Message parameter to 'Error SMS Sending' and jumps to the TRAP_ERROR label.
7. If the TOA status is 2 (already approved), it sets the @Message parameter to '1' (indicating success) and jumps to the TRAP_ERROR label.
8. If any other error occurs, it sets the @Message parameter to 'Invalid TAR status. Please refresh RGS.' and jumps to the TRAP_ERROR label.
9. Finally, if no errors occurred, it commits the transaction and returns the constructed message.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-acksms'></a>
# Procedure: sp_TAMS_RGS_AckSMS

### Purpose
This stored procedure sends an SMS acknowledgement to a TAMS user, depending on their access type and the status of their protection limit.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID of the user to send the SMS to. |
| @EncTARID | NVARCHAR(250) | The encrypted TAR ID of the user to send the SMS to. |
| @SMSType | NVARCHAR(5) | The type of SMS message to send (e.g., '2' for acknowledgement). |
| @Message | NVARCHAR(500) | The output parameter that stores the success or error message. |

### Logic Flow
1. The procedure checks if a transaction has already been started and sets an internal transaction flag accordingly.
2. It retrieves the TAR ID, line number, access type, TOA number, and HP number from the TAMS_TAR and TAMS_TOA tables based on the provided TAR ID.
3. If the access type is 'Possession', it updates the AckGrantTOATime and ReqProtectionLimitTime fields in the TAMS_TOA table if the SMSType is '2'. Otherwise, it updates the AckProtectionLimitTime field.
4. It sets an SMS message based on the TOA number and sends an SMS using the sp_api_send_sms stored procedure.
5. If any errors occur during the process, it sets an error message in the @Message output parameter.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-acksms-20221107'></a>
# Procedure: sp_TAMS_RGS_AckSMS_20221107

### Purpose
This stored procedure sends an SMS acknowledgement to a TAMS user when their protection limit or grant time has been updated.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The TAR ID of the TAMS record being updated. |

### Logic Flow
1. The procedure starts by checking if a transaction is already in progress. If not, it begins a new transaction.
2. It retrieves the necessary data from the `TAMS_TAR` and `TAMS_TOA` tables based on the provided TAR ID.
3. Depending on the access type (Possession or Not), it updates the corresponding grant or protection limit time in the `TAMS_TOA` table.
4. If the SMS message is not empty, it sends an SMS using the `sp_api_send_sms` procedure.
5. If any errors occur during the process, it sets a message and either commits or rolls back the transaction depending on whether an error occurred.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-acksms-20221214'></a>
# Procedure: sp_TAMS_RGS_AckSMS_20221214

### Purpose
This stored procedure performs the business task of sending an acknowledgement SMS to a TAR (Transportation Asset Record) after it has been granted or protection limit has been set up.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR being acknowledged. |
| @EncTARID | NVARCHAR(250) | The encrypted TAR ID. |
| @SMSType | NVARCHAR(5) | The type of SMS to be sent (e.g., 2 for acknowledgement). |
| @Message | NVARCHAR(500) = NULL OUTPUT | The message to be sent in the SMS. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it begins a new transaction.
2. It retrieves the TAR details from the TAMS_TAR and TAMS_TOA tables based on the provided @TARID and @EncTARID.
3. Depending on the access type of the TAR (Possession or not), it updates the corresponding fields in the TAMS_TOA table with the current date and time.
4. If the SMS type is 2, it updates the AckGrantTOATime field and sets up a link to report once protection limit has been set up.
5. It inserts an audit record into the TAMS_TOA_Audit table for the updated TAR details.
6. If a message is generated, it sends an SMS using the sp_api_send_sms stored procedure.
7. If any errors occur during the process, it sets an error message and commits or rolls back the transaction accordingly.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-acksms-m'></a>
# Procedure: sp_TAMS_RGS_AckSMS_M

### Purpose
This stored procedure performs an acknowledgement of a SMS message for a specific TAMS (Transportation Asset Management System) record, updating the corresponding TAMS_TOA record with the latest information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID		| BIGINT | The ID of the TAMS record to be acknowledged. |
| @EncTARID	| NVARCHAR(250) | The encrypted ID of the TAMS record to be acknowledged. |
| @SMSType	| NVARCHAR(5) | The type of SMS message being sent. |
| @Message	| NVARCHAR(500) = NULL OUTPUT | The output parameter that stores the acknowledgement message. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it begins a new transaction.
2. It then retrieves the necessary information from the TAMS_TAR and TAMS_TOA tables based on the provided @TARID and @EncTARID values.
3. Depending on the access type of the TAMS record, it determines whether to send an SMS message with a specific acknowledgement code (e.g., '2' for possession) or not.
4. If an SMS message is determined to be sent, it constructs the message by concatenating the TOANo and additional information.
5. The procedure then inserts a new audit record into the TAMS_TOA_Audit table to track changes made to the TAMS_TOA record.
6. It sends the constructed SMS message using the sp_api_send_sms stored procedure, which returns an error code.
7. If an error occurs during SMS sending, it sets the @Message output parameter to 'Error SMS Sending' and commits or rolls back the transaction accordingly.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA
* **Writes:** TAMS_TOA_Audit

---


<a id='database-reference-sql-sp-tams-rgs-acksms-20221214-m'></a>
# Procedure: sp_TAMS_RGS_AckSMS_20221214_M

### Purpose
This stored procedure performs a series of actions to acknowledge SMS messages for a specific TAR (Transportation Asset Record) and update the corresponding records in the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID		| BIGINT | The ID of the TAR being processed. |
| @EncTARID	| NVARCHAR(250) | The encrypted TAR ID. |
| @SMSType	| NVARCHAR(5) | The type of SMS message (e.g., 2 for acknowledgement). |
| @Message	| NVARCHAR(500) = NULL OUTPUT | The output message to be sent via SMS. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it begins a new transaction.
2. It retrieves the TAR details from the TAMS_TAR and TAMS_TOA tables based on the provided @TARID and @EncTARID values.
3. Depending on the access type (Possession or not), it updates the corresponding records in the TAMS_TOA table with the current date and time.
4. If the SMS message is not empty, it sends an SMS notification to the mobile number associated with the TAR using the sp_api_send_sms stored procedure.
5. After sending the SMS, it checks if any errors occurred during this process. If so, it sets a failure message and exits the transaction.
6. If no errors occurred, it commits the transaction and returns the output message.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA tables
* **Writes:** TAMS_TOA table (for updates)

---


<a id='database-reference-sql-sp-tams-rgs-acksurrender'></a>
# Procedure: sp_TAMS_RGS_AckSurrender

### Purpose
This stored procedure acknowledges a surrender request for a Traction Asset Management System (TAMS) resource, updating the status and sending an SMS notification to the relevant stakeholders.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR (Traction Asset Resource) being surrendered. |
| @UserID | NVARCHAR(500) | The ID of the user performing the surrender action. |
| @Message | NVARCHAR(500) | An output parameter to store the acknowledgement message. |

### Logic Flow
1. The procedure checks if a transaction has been started and sets an internal flag (`@IntrnlTrans`) accordingly.
2. It retrieves the `Userid` from the `TAMS_User` table based on the provided `@UserID`.
3. It checks the current status of the TAR being surrendered (`@TOAStatusChk`) and updates it to 5 (Acknowledged) if it's not already in this state.
4. If the TAR has been acknowledged, it:
	* Retrieves the Traction Power ID from the `TAMS_Traction_Power_Detail` table based on the TAR ID.
	* Checks if all OCC (OCC Auth) requests for the Traction Power ID have been completed and sends an SMS notification to the relevant stakeholders using the `sp_api_send_sms` procedure.
	* Updates the OCC Auth status of the Traction Power ID to 9 (Completed).
5. If the TAR has not been acknowledged, it:
	* Retrieves the Traction Power ID from the `TAMS_Traction_Power_Detail` table based on the TAR ID.
	* Checks if all OCC requests for the Traction Power ID have been completed and sends an SMS notification to the relevant stakeholders using the `sp_api_send_sms` procedure.
	* Updates the OCC Auth status of the Traction Power ID to 9 (Completed).
6. If any errors occur during the process, it sets the `@Message` parameter to an error message and either commits or rolls back the transaction depending on whether an internal transaction was started.

### Data Interactions
* **Reads:** `TAMS_User`, `TAMS_TAR`, `TAMS_TOA`, `TAMS_Traction_Power_Detail`
* **Writes:** `TAMS_TOA` (updated TAR status), `TAMS_OCC_Auth` (OCC Auth status updates), `TAMS_OCC_Auth_Workflow` (OCC Auth workflow updates)

---


<a id='database-reference-sql-sp-tams-rgs-acksurrender-20221107'></a>
# Procedure: sp_TAMS_RGS_AckSurrender_20221107

### Purpose
This stored procedure acknowledges a surrender for a TAMS (Technical Assistance Management System) record and sends an SMS notification to the relevant party.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Technical Assistance Record) being surrendered. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the action. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message to be sent via SMS. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets a flag and begins a new transaction.
2. It then retrieves the ID of the user performing the action from the TAMS_User table based on their login ID.
3. The procedure updates the TOAStatus to 5 (Acknowledged) in the TAMS_TOA table for the specified TARID.
4. It then checks if all acknowledgments are complete by iterating through the TOAStatus of each TOA record associated with the TARID. If any status is not 5, it sets a flag indicating that not all acknowledgments are complete.
5. Based on the line (DTL or NEL) of the TAR record, it performs different actions:
	* For DTL lines, it updates the OCCAuthStatusId to 11 and inserts a new workflow into TAMS_OCC_Auth_Workflow for each OCC Auth record with status 10. It also updates the OCCAuthStatusId to 13 for each OCC Auth record with status 7.
	* For NEL lines, it updates the OCCAuthStatusId to 9 and inserts a new workflow into TAMS_OCC_Auth_Workflow for each OCC Auth record with status 7.
6. After completing these actions, it constructs an SMS message based on the TOANo and sends it via the sp_api_send_sms stored procedure.

### Data Interactions
* Reads: TAMS_User, TAMS_TOA, TAMS_TAR, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-acksurrender-20230308'></a>
# Procedure: sp_TAMS_RGS_AckSurrender_20230308

### Purpose
This stored procedure acknowledges a surrender for a RGS (Remote Gateway Server) and updates the relevant records in the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Test Access Record) to be acknowledged. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the action. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that will contain a message if an error occurs. |

### Logic Flow
The procedure follows these steps:

1. It checks if there is already a transaction in progress and sets `@IntrnlTrans` to 1 if not.
2. It retrieves the user ID from the TAMS_User table based on the provided login ID.
3. It updates the TOAStatus, AckSurrenderTime, UpdatedOn, and UpdatedBy fields for the specified TARID in the TAMS_TOA table.
4. It inserts a new record into the TAMS_TOA_Audit table with the current user ID and timestamp.
5. It retrieves various fields from the TAMS_TAR and TAMS_TOA tables based on the provided TARID, line, and access date.
6. If the line is 'DTL', it checks if there are any OCCAuthStatusId values that need to be updated or inserted into the TAMS_OCC_Auth table. It also checks for buffer zone records and updates them accordingly.
7. If the line is not 'DTL', it performs similar checks as above but for NEL (Network End).
8. After completing these checks, it sets a message based on the line and sends an SMS using the sp_api_send_sms stored procedure.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_TOA_Audit

---


<a id='database-reference-sql-sp-tams-rgs-acksurrender-osreq'></a>
# Procedure: sp_TAMS_RGS_AckSurrender_OSReq

### Purpose
This stored procedure acknowledges a surrender request for an Operating System (OS) and sends a corresponding SMS message to the endorser.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Transaction Acknowledgement Request) being acknowledged. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the action. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message to be sent as an SMS. |

### Logic Flow
1. Check if a transaction is already in progress. If not, set a flag and begin a new transaction.
2. Update the TOAStatus of the TAR being acknowledged to 5 (Acknowledged).
3. Set the AckSurrenderTime to the current date and time.
4. Retrieve the TAR and TOA IDs from the TAMS_TAR and TAMS_TOA tables based on the @TARID parameter.
5. Check if the line is 'DTL' or not. If it's 'DTL', proceed with the DTL logic; otherwise, proceed with the NEL logic.
6. For the DTL logic:
	* Retrieve the IDs of the endorser for each OCCAuth status (10, 11, and 12).
	* Update the OCCAuthStatusId in TAMS_OCC_Auth to reflect the new status.
	* Insert a new record into TAMS_OCC_Auth_Workflow with the updated status and endorser ID.
7. For the NEL logic:
	* Retrieve the IDs of the endorser for each OCCAuth status (7).
	* Update the OCCAuthStatusId in TAMS_OCC_Auth to reflect the new status.
	* Insert a new record into TAMS_OCC_Auth_Workflow with the updated status and endorser ID.
8. Construct the SMS message based on the line type ('DTL' or 'NEL') and the current date and time.
9. If an error occurs during the process, set the @Message parameter to indicate the error and exit the procedure.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-acksurrender-20230209-allcancel'></a>
# Procedure: sp_TAMS_RGS_AckSurrender_20230209_AllCancel

### Purpose
This stored procedure acknowledges a surrender for all TAMS (Test and Measurement Systems) records with a specific status, updates the corresponding TOA (Test Operation Assignment) records, and sends an SMS notification to the user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAMS record being acknowledged. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the action. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message to be sent via SMS. |

### Logic Flow
The procedure follows these steps:

1. It checks if a transaction has been started and sets an internal flag (`@IntrnlTrans`) accordingly.
2. It retrieves the user ID from the `TAMS_User` table based on the provided login ID.
3. It updates the corresponding TOA records in the `TAMS_TOA` table with the new status (5) and timestamp.
4. It inserts an audit record into the `TAMS_TOA_Audit` table for each updated TOA record.
5. It checks if all TAMS records have been acknowledged by iterating through the TOA records and checking their status.
6. If all records are acknowledged, it sends an SMS notification to the user with a success message.
7. If any record is not acknowledged, it sets an error message in the `@Message` output parameter.

### Data Interactions
* **Reads:** TAMS_User, TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_TOA_Audit
* **Writes:** TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-cancel'></a>
# Procedure: sp_TAMS_RGS_Cancel

### Purpose
This stored procedure cancels a Request for Goods (RGS) on TAMS, updating the status and sending an SMS notification to the OCC contact.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR sector being cancelled. |
| @CancelRemarks	| NVARCHAR(1000) | Optional remarks for the cancellation. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the cancellation. |
| @tracktype as nvarchar(50)='MAINLINE' | nvarchar(50) | The type of track to use (in this case, MAINLINE). |
| @Message	| NVARCHAR(500) | Output parameter that will contain an error message if any. |

### Logic Flow
1. Check if a transaction is already in progress and set the internal transaction flag accordingly.
2. Initialize the output parameter @Message with an empty string.
3. Retrieve the current status of the TAR sector being cancelled from TAMS_TOA.
4. Update the TOAStatus to 6 (cancelled) and CancelRemark to the provided value in TAMS_TOA.
5. Insert a new record into TAMS_TAMSAudit for the updated TAR sector.
6. Determine the ID of the user associated with the current login ID in TAMS_User.
7. Check if the track type is MAINLINE. If so, proceed with the cancellation logic.
8. For MAINLINE tracks:
	* Retrieve the list of traction power IDs from TAMS_Traction_Power_Detail that are associated with the TAR sector being cancelled.
	* Iterate through each traction power ID and perform the following actions:
		+ Update OCCAuthStatusId to 9 (cancelled) in TAMS_OCC_Auth for the current traction power ID.
		+ Insert a new record into TAMS_OCC_Auth_Workflow for the updated OCC Auth status.
		+ Insert a new record into TAMS_OCC_Auth_Audit for the updated OCC Auth status.
9. For NEL tracks:
	* Retrieve the list of traction power IDs from TAMS_Traction_Power_Detail that are associated with the TAR sector being cancelled.
	* Iterate through each traction power ID and perform the following actions:
		+ Update OCCAuthStatusId to 9 (cancelled) in TAMS_OCC_Auth for the current traction power ID.
		+ Insert a new record into TAMS_OCC_Auth_Workflow for the updated OCC Auth status.
		+ Insert a new record into TAMS_OCC_Auth_Audit for the updated OCC Auth status.
10. If all surrender records are found, update the DepotAuthStatusId in TAMS_Depot_Auth to reflect the new workflow ID.
11. Determine if there is an existing DepotAuthWorkFlow record with the same DTCAuthID and WorkflowID as the newly inserted record.
12. If so, update the isCancelled flag to 1 (true) in TAMS_Depot_Auth_Workflow.
13. Insert a new record into TAMS_Depot_Auth_Workflow for the updated Depot Auth status.
14. Update the DepotAuthStatusId in TAMS_Depot_Auth to reflect the new workflow ID.
15. If any errors occur during the cancellation process, set @Message to an error message and exit the procedure.

### Data Interactions
* Reads: TAMS_TOA, TAMS_Traction_Power_Detail, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_OCC_Auth_Audit, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow.
* Writes: TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_OCC_Auth_Audit, TAMS_Depot_Auth, TAMS_Depot_Auth_Workflow.

---


<a id='database-reference-sql-sp-tams-rgs-cancel-20221107'></a>
# Procedure: sp_TAMS_RGS_Cancel_20221107

### Purpose
This stored procedure cancels a Request for Goods (RGS) by updating the status of related records and sending an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID		| BIGINT | The ID of the RGS to be cancelled. |
| @CancelRemarks	| NVARCHAR(1000) | Optional remarks for cancellation. |
| @UserID		| NVARCHAR(500) | The ID of the user performing the cancellation. |
| @Message	| NVARCHAR(500) | Output parameter containing the message sent via SMS. |

### Logic Flow
1. Check if a transaction is already in progress and set an internal flag accordingly.
2. Initialize variables for storing messages and IDs.
3. Update the status of related records (TAMS_TOA) to reflect cancellation.
4. Retrieve user IDs from TAMS_User table based on the provided user ID.
5. Determine the line type ('DTL' or 'NEL') and retrieve endorser IDs accordingly.
6. Iterate through a cursor of TOAStatus values, checking if any are not in the expected range (0 or 6). If so, set @lv_IsAllAckSurrender to 0.
7. Based on the line type, perform different actions:
	* For 'DTL', update OCC_Auth records and insert workflow entries for each related record.
	* For 'NEL', update OCC_Auth records and insert workflow entries for each related record.
8. Construct an SMS message based on the TOANo value.
9. Send the SMS notification using sp_api_send_sms stored procedure.
10. If any errors occur, rollback the transaction and return an error message.

### Data Interactions
* Reads: TAMS_TOA, TAMS_User, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-cancel-20230308'></a>
# Procedure: sp_TAMS_RGS_Cancel_20230308

### Purpose
This stored procedure cancels a Request for Goods Service (RGS) on TAMS due to inactivity.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Task Assignment Record) to be cancelled. |
| @CancelRemarks	| NVARCHAR(1000) | Optional remarks for cancellation. |
| @UserID	| NVARCHAR(500) | The ID of the user performing the cancellation. |
| @Message	| NVARCHAR(500) | Output parameter containing the message sent via SMS. |

### Logic Flow
1. Check if a transaction is already in progress. If not, start a new transaction.
2. Initialize variables for internal transactions and log messages.
3. Update the TOAStatus to 6 (Cancelled) and CancelRemark with @CancelRemarks in TAMS_TOA table where TARId matches @TARID.
4. Insert an audit record into TAMS_TOA_Audit table for the updated TOA record.
5. Retrieve the ID of the user from TAMS_User table based on @UserID.
6. Initialize variables for SMS message and cursor to iterate through OCC Auth records.
7. Check if all acknowledgement surrenders are acknowledged (TOAStatus = 5). If not, set @lv_IsAllAckSurrender to 0.
8. Iterate through OCC Auth records where TARId matches @TARID and Line is 'DTL' or 'NEL'. For each record:
	* Update the OCCAuthStatusId in TAMS_OCC_Auth table to a pending status (11, 13, or 9) based on the Level of the workflow.
	* Insert an audit record into [dbo].[TAMS_OCC_Auth_Workflow] table for the updated OCC Auth record.
9. If @Line is 'DTL', construct the SMS message with TOANo and send it via sp_api_send_sms procedure. Otherwise, construct the SMS message with TARNo and send it via SP_Call_SMTP_Send_SMSAlert procedure.
10. Check if any errors occurred during SMS sending or RGS cancellation. If so, return an error message.

### Data Interactions
* Reads: TAMS_TOA, TAMS_User, TAMS_OCC_Auth, [dbo].[TAMS_OCC_Auth_Workflow], TAMS_Action_Log, TAMS_TAR
* Writes: TAMS_TOA (TOAStatus and CancelRemark), TAMS_OCC_Auth (OCCAuthStatusId), [dbo].[TAMS_OCC_Auth_Workflow]

---


<a id='database-reference-sql-sp-tams-rgs-cancel-20250403'></a>
# Procedure: sp_TAMS_RGS_Cancel_20250403

### Purpose
This stored procedure cancels a Request for Goods (RGS) on TAMS and sends an SMS notification to the OCC contact.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR sector being cancelled. |
| @CancelRemarks	| NVARCHAR(1000) | The reason for cancellation. |
| @UserID	| NVARCHAR(500) | The user ID performing the cancellation. |
| @tracktype as nvarchar(50)='MAINLINE' | nvarchar(50) | The type of track (MAINLINE). |
| @Message	| NVARCHAR(500) | Output parameter to store the SMS message. |

### Logic Flow
1. Check if a transaction is already in progress.
2. If not, set an internal transaction flag and begin a new transaction.
3. Initialize an output parameter `@Message` to store the SMS message.
4. Retrieve the TAR sector ID from TAMS_TAR table based on the input `@TARID`.
5. Update the TOA status in TAMS_TOA table to 6 (cancelled) and set the cancellation remarks.
6. Insert a new record into TAMS_TOA_Audit table to log the cancellation.
7. Retrieve the user ID from TAMS_User table based on the input `@UserID`.
8. Check if the track type is MAINLINE. If so, proceed with the cancellation logic.
9. For MAINLINE tracks:
	* Declare a cursor to iterate through TAMS_OCC_Auth table and find records with a specific status (8 or 9).
	* Update these records in TAMS_OCC_Auth table to reflect the new status (9) and insert new records into TAMS_OCC_Auth_Workflow table.
	* Insert new records into TAMS_OCC_Auth_Audit table to log the changes.
10. If the track type is not MAINLINE, proceed with the cancellation logic for NEL tracks.
11. For NEL tracks:
	* Declare a cursor to iterate through TAMS_TAR_Power_Sector table and find records associated with the TAR sector being cancelled.
	* Check if all these records have cleared (i.e., their status is not 0, 5, or 6). If so, proceed with the cancellation logic.
12. For NEL tracks:
	* Cancel authorisation for any existing Depot Auth records associated with the TAR sector being cancelled.
	* Update the Depot Auth Status ID in TAMS_Depot_Auth table to reflect the new status (e.g., 'Line Clear Certification (TOA/SCD) (CC)' or 'Line Clear Certification (TOA/SCD) (DTC)').
13. Send an SMS notification to the OCC contact based on the track type and TAR sector ID.
14. If any errors occur during the procedure, roll back the transaction and return an error message.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_OCC_Auth_Audit, TAMS_Depot_Auth, TAMS_WFStatus.
* **Writes:** TAMS_TOA, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_OCC_Auth_Audit, TAMS_Depot_Auth.

---


<a id='database-reference-sql-sp-tams-rgs-cancel-osreq'></a>
# Procedure: sp_TAMS_RGS_Cancel_OSReq

### Purpose
This stored procedure cancels an Order Status Request (OSR) and updates the corresponding records in the TAMS database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR record to be canceled. |
| @CancelRemarks	| NVARCHAR(1000) | Optional remarks for canceling the OSR. |
| @UserID	| NVARCHAR(500) | The user ID performing the cancellation. |
| @Message	| NVARCHAR(500) | Output parameter containing a message after execution. |

### Logic Flow
1. Check if a transaction is already in progress. If not, start a new transaction.
2. Initialize variables for storing internal transactions and SMS messages.
3. Update the TOAStatus to 6 (Canceled) and CancelRemark in TAMS_TOA table where TARId matches @TARID.
4. Determine the line type ('DTL' or 'NEL') based on the TAR record's Line field.
5. If the line is 'DTL', perform the following steps:
	* Retrieve OCC Auth IDs with a specific status and update their status to 11 (Pending) and add an entry in TAMS_OCC_Auth_Workflow table.
	* Update the status of other OCC Auth IDs to 12 (Terminated) and add entries in TAMS_OCC_Auth_Workflow table.
6. If the line is 'NEL', perform the following steps:
	* Retrieve OCC Auth IDs with a specific status and update their status to 8 (Pending) and add an entry in TAMS_OCC_Auth_Workflow table.
7. Construct an SMS message based on the line type and TAR record details.
8. Send the SMS message using the @Message output parameter.
9. If any errors occur during execution, roll back the transaction and return an error message.
10. Commit the transaction if no errors occurred.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TAR, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-cancel-20230209-allcancel'></a>
# Procedure: sp_TAMS_RGS_Cancel_20230209_AllCancel

### Purpose
This stored procedure cancels all RGS (Remote Gateway Server) operations for a given TARID (TAR ID), updates the TOA status, and sends an SMS notification to the user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The TAR ID to cancel all RGS operations for. |
| @CancelRemarks	| NVARCHAR(1000) | Optional remarks for the cancellation. |
| @UserID	| NVARCHAR(500) | The user ID performing the cancellation. |
| @Message	| NVARCHAR(500) | Output parameter to store the SMS message. |

### Logic Flow
1. Check if a transaction is already in progress and set an internal flag accordingly.
2. Initialize variables for storing the TOA status, Cancel Remarks, and User ID.
3. Update the TOA status, Cancel Remarks, and Updated By fields for all RGS operations with the given TARID.
4. Insert an audit record into TAMS_TOA_Audit for each updated TOA record.
5. Retrieve the user ID from TAMS_User based on the provided User ID.
6. Initialize variables for storing SMS message components (e.g., TARNo, TOANo, Line).
7. Query TAMS_TAR and TAMS_TOA to retrieve relevant data for the given TARID and current date/time.
8. Iterate through all RGS operations with a status not equal to 5 (i.e., not already cancelled) and update their status to 6 (cancelled).
9. For each RGS operation, check if it's the last one in the sequence and perform additional actions:
	* If it's a DTL (Detailed) line, update OCCAuthStatusId and insert an audit record.
	* If it's an NEL (Notification) line, update OCCAuthStatusId and insert an audit record.
10. Construct the SMS message based on the TARNo, TOANo, and Line values.
11. Send the SMS notification using sp_api_send_sms.
12. Check for any errors during the process and return a corresponding error message.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TAR, TAMS_User, TAMS_OCC_Auth, TAMS_OCC_Auth_Workflow, TAMS_Action_Log, TAMS_Action_Log
* Writes: TAMS_TOA (updated status), TAMS OCC_Auth (updated status and audit record), TAMS OCC_Auth_Workflow (audit record)

---


<a id='database-reference-sql-sp-tams-rgs-get-upddets'></a>
# Procedure: sp_TAMS_RGS_Get_UpdDets

This procedure retrieves and decrypts specific data from the TAMS_TOA table based on a provided TARID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TARID to filter the data by |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_TOA table.
2. It filters the results based on the provided TARID, if specified.
3. The selected columns are then decrypted using a function named dbo.DecryptString.

### Data Interactions
* **Reads:** TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-granttoa'></a>
# Procedure: sp_TAMS_RGS_GrantTOA

### Purpose
This stored procedure grants a TOA (Temporary Authorization) to a RGS (Railway Grade Signal) for a specific TAR (Track Access Record).

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR being granted TOA. |
| @EncTARID | NVARCHAR(250) | The encrypted TAR ID. |
| @UserID | NVARCHAR(500) | The user ID of the person granting the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it begins a new transaction.
2. It then retrieves the TAR details from the TAMS_TAR and TAMS_TOA tables based on the provided @TARID and @EncTARID.
3. If the TOA status is 2 (Pending), it generates a reference number for the TOA using the sp_Generate_Ref_Num_TOA stored procedure.
4. It then updates the TOA status to 3 (Granted) in the TAMS_TOA table, sets the new TOANo and GrantTOATime fields, and inserts an audit record into the TAMS_TOA_Audit table.
5. Depending on the access type ('Possession' or not), it constructs a message for sending an SMS to the user with the reference number.
6. It then sends the SMS using the sp_api_send_sms stored procedure.
7. If any errors occur during this process, it sets the @Message output parameter to an error message and either commits or rolls back the transaction depending on whether an error occurred.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-granttoa-001'></a>
# Procedure: sp_TAMS_RGS_GrantTOA_001

### Purpose
This stored procedure grants a TOA (Temporary Authorization) to a user for a specific TAR (Track and Record) ID, updating the TOA status and sending an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID for which the TOA is being granted. |
| @EncTARID | NVARCHAR(250) | The Encoded TAR ID used in the SMS notification link. |
| @UserID | NVARCHAR(500) | The user ID of the person granting the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message to be returned by the procedure, which will contain an error message if any errors occur during execution. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets a flag and begins a new transaction.
2. It then retrieves the TAR No, Line, Operation Date, Access Type, and Mobile No for the specified TAR ID from the TAMS_TAR and TAMS_TOA tables.
3. The procedure generates a reference number (Ref Num) using the sp_Generate_Ref_Num_TOA stored procedure.
4. It updates the TOA status in the TAMS_TOA table to 3, sets the new Ref Num, Grant TOA Time, Updated On, and Updated By fields.
5. An audit record is inserted into the TAMS_TOA_Audit table for the updated TAR ID.
6. The procedure then constructs an SMS message based on the Access Type (Possession or Non-Possession).
7. If the user has a Mobile No, it sends an SMS notification using the sp_api_send_sms stored procedure.
8. Finally, if any errors occur during execution, the procedure rolls back the transaction and returns an error message; otherwise, it commits the transaction and returns the output message.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-granttoa-20221107'></a>
# Procedure: sp_TAMS_RGS_GrantTOA_20221107

### Purpose
This stored procedure grants a TOA (Temporary Access Authorization) to a user for a specific TAR (Track and Record) ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID for which the TOA is being granted. |
| @EncTARID | NVARCHAR(250) | The Encoded TAR ID. |
| @UserID | NVARCHAR(500) | The user ID of the person granting the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that stores any error messages. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets an internal transaction flag and begins a new transaction.
2. It then retrieves the TAR ID, Line, Operation Date, Access Type, and HP No from the TAMS_TAR and TAMS_TOA tables based on the provided @TARID.
3. The procedure generates a reference number for the TOA using the sp_Generate_Ref_Num_TOA stored procedure.
4. It updates the TOA status in the TAMS_TOA table to 3, sets the TOANo to the generated reference number, and sets the GrantTOATime and UpdatedOn fields to the current date and time.
5. Depending on the Access Type, it constructs an SMS message with a link to acknowledge the TOA.
6. If the HP No is not empty, it sends the SMS using the sp_api_send_sms stored procedure.
7. If any errors occur during the process, it sets the @Message output parameter to an error message and either commits or rolls back the transaction depending on whether an internal transaction was started.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-granttoa-20221214'></a>
# Procedure: sp_TAMS_RGS_GrantTOA_20221214

### Purpose
This stored procedure grants a TOA (Temporary Authorization) to a TAR (Track and Record) for a specific user, updating the TAR's status and sending an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR to grant TOA to. |
| @EncTARID | NVARCHAR(250) | The encrypted TAR ID. |
| @UserID | NVARCHAR(500) | The ID of the user granting the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message for the procedure, which will be populated with an error message if an error occurs. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets a flag and begins a new transaction.
2. It retrieves the TAR's details from the TAMS_TAR table based on the provided @TARID and @EncTARID.
3. It generates a reference number for the TOA using the sp_Generate_Ref_Num_TOA stored procedure.
4. The procedure updates the TAR's status to 3 (granted) in the TAMS_TOA table, sets the TOANo field to the generated reference number, and records the grant time and updated by fields.
5. It inserts a new record into the TAMS_TOA_Audit table for the granted TAR.
6. Depending on the access type ('Possession' or not), it constructs an SMS message with a link to acknowledge the TOA.
7. If @HPNo is not empty, it sends an SMS notification using the sp_api_send_sms stored procedure.
8. It checks if any errors occurred during the execution of the procedure and returns an error message if so.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-granttoa-20230801'></a>
# Procedure: sp_TAMS_RGS_GrantTOA_20230801

### Purpose
This stored procedure grants a TOA (Temporary Authorization) to a user for a specific TAR (Track and Record) ID, updating the TOA status and sending an SMS notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID for which the TOA is being granted. |
| @EncTARID | NVARCHAR(250) | The Encoded TAR ID used in the SMS notification link. |
| @UserID | NVARCHAR(500) | The user ID of the person granting the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output parameter that stores any error message if an issue occurs during the procedure execution. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets a flag and begins a new transaction.
2. It retrieves the TAR No, Line, Operation Date, Access Type, and Mobile No for the specified TAR ID from the TAMS_TAR and TAMS_TOA tables.
3. It generates a reference number (Ref Num) using the sp_Generate_Ref_Num_TOA stored procedure.
4. The procedure updates the TOA status in the TAMS_TOA table with the new Ref Num, Grant TOA time, updated on date, and updated by user.
5. An audit record is inserted into the TAMS_TOA_Audit table for the updated TAR ID.
6. It sets the current date and time.
7. Depending on the access type ('Possession' or not), it constructs an SMS message with a link to acknowledge the TOA.
8. If the user has a Mobile No, it sends an SMS notification using the sp_api_send_sms stored procedure.
9. If any errors occur during the procedure execution, it sets an error message in the @Message output parameter and either commits or rolls back the transaction depending on whether an error occurred.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-granttoa-20230801-m'></a>
# Procedure: sp_TAMS_RGS_GrantTOA_20230801_M

### Purpose
This stored procedure grants a TOA (Temporary Authorization) to a user for a specific TAR (Track and Record) ID, based on the provided user ID and message.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID for which the TOA is being granted. |
| @EncTARID | NVARCHAR(250) | The Encoded TAR ID. |
| @UserID | NVARCHAR(500) | The user ID of the person granting the TOA. |
| @Message | NVARCHAR(500) = NULL OUTPUT | The message to be sent to the user after the TOA is granted. |

### Logic Flow
1. The procedure checks if a transaction has already started. If not, it starts one.
2. It retrieves the TAR and TOA status for the provided TAR ID from the TAMS_TAR and TAMS_TOA tables.
3. If the TOA status is 2 (Pending), it generates a reference number using the sp_Generate_Ref_Num_TOA stored procedure.
4. It updates the TOA status to 3 (Granted) in the TAMS_TOA table with the new reference number, grant time, and updated by fields.
5. It inserts an audit record into the TAMS_TOA_Audit table for the updated TAR ID.
6. Depending on the access type ('Possession' or not), it sets a message to be sent to the user via SMS using the sp_api_send_sms stored procedure.
7. If the SMS sending process fails, it sets an error message and skips to the TRAP_ERROR label.
8. If the TOA status is 3 (Granted) after checking again, it sets a success message and exits the procedure.
9. If any errors occur during the procedure, it rolls back the transaction if one was started.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_TOA_Audit
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-onload'></a>
# Procedure: sp_TAMS_RGS_OnLoad

### Purpose
This stored procedure is used to retrieve and process data related to possession, protection, and cancellation of railway goods (RGs) for a specific line and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number for which the RG data is being processed. |
| @TrackType | NVARCHAR(50) | The track type (e.g., mainline, NEL) for which the RG data is being processed. |

### Logic Flow
The procedure follows these steps:

1. It determines the current date and time.
2. Based on the current time, it sets the operation date and access date accordingly.
3. It retrieves the possession, protection, and cancellation background values from the TAMS_Parameters table based on the line number and track type.
4. It checks if there are any existing possessions for the specified line and track type. If yes, it sets a flag indicating that there is an existing possession.
5. It processes the data by retrieving additional information such as electrical sections, power off times, circuit break out times, parties involved, work descriptions, contact numbers, and remarks.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Sector, TAMS_TAR_Power_Sector
* Writes: None

---


<a id='database-reference-sql-sp-tams-rgs-onload-20221107'></a>
# Procedure: sp_TAMS_RGS_OnLoad_20221107

### Purpose
This stored procedure performs a daily load of data for the RGS (Remote Grid System) system, updating and populating various tables with relevant information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
The procedure starts by truncating two temporary tables: #TmpRGS and #TmpRGSSectors. It then sets the current date and time, as well as the operation and access dates for the day.

Next, it retrieves the RGS possession background (RGSPossBG) and protection background (RGSProtBG) values from the TAMS_Parameters table based on the line number (@Line).

The procedure then checks if the current time is greater than a certain cutoff time. If so, it sets the operation date to the current date and access date to the next day. Otherwise, it sets the operation date to the previous day and access date to the current date.

It then declares two cursors: @Cur01 for TAMS_TAR and TAMS_TOA tables, and @Cur02 for TAMS_TAR_Power_Sector table. The procedure iterates through each row in these tables, extracting relevant information such as TARNo, TOANo, PartiesName, NoOfPersons, WorkDescription, ContactNo, etc.

Based on the line number (@Line), it performs different operations:

- For 'DTL' lines:
  - It sets @lv_Remarks to a string containing the rack out remark and TVF mode.
  - If @lv_PossessionCtr is greater than 0, it sets @lv_IsGrantTOAEnable to 0. Otherwise, it sets @lv_IsGrantTOAEnable to 1.

- For other lines:
  - It sets @lv_Remarks to a string containing the TVF stations.
  - If @AccessType is 'Possession', it sets @lv_ColourCode to RGSPossBG and updates @lv_PossessionCtr accordingly. Otherwise, it sets @lv_ColourCode to RGSProtBG.

The procedure then inserts the extracted information into #TmpRGS table.

Finally, it fetches the operation date, access date, and other relevant information from #TmpRGS table and displays them in a list format.

### Data Interactions
* **Reads:**
	+ TAMS_TAR
	+ TAMS_TOA
	+ TAMS_TAR_Power_Sector
	+ TAMS_Parameters
	+ TAMS_Access_Requirement
* **Writes:**
	+ #TmpRGS table
	+ #TmpRGSSectors table

---


<a id='database-reference-sql-sp-tams-rgs-onload-20221118'></a>
# Procedure: sp_TAMS_RGS_OnLoad_20221118

### Purpose
This stored procedure performs a daily load of data for the RGS (Remote Grid System) system, updating and populating various tables with relevant information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
The procedure starts by truncating two temporary tables: #TmpRGS and #TmpRGSSectors. It then sets the current date and time, as well as the operation and access dates for the day.

Next, it selects the RGS parameters (RGSPossessionBG and RGSProtectionBG) based on the line number (@Line). If the current time is after a certain cutoff time ('06:00:00'), it sets the operation date to the current date; otherwise, it sets it to the previous day.

The procedure then declares two cursors (@Cur01 and @Cur02) to iterate through the TAMS_TAR and TAMS_TOA tables. For each row in these tables, it extracts various fields such as TARNo, TOANo, PartiesName, NoOfPersons, WorkDescription, ContactNo, etc.

Based on the line number (@Line), it performs different operations:

* If @Line = 'DTL', it sets the Remarks field to a combination of the ARRemark and TVFMode values.
* If @Line = 'NEL', it sets the Remarks field to a specific value indicating that it's a NEL (Network Extension Line) operation.

The procedure then inserts data into #TmpRGS based on the extracted fields. It also updates various counters and flags, such as PossessionCtr, IsGrantTOAEnable, etc.

Finally, it fetches the Sno, TARNo, ElectricalSections, PowerOffTime, CircuitBreakOutTime, PartiesName, NoOfPersons, WorkDescription, ContactNo, TOANo, CallbackTime, RadioMsgTime, LineClearMsgTime, Remarks, TOAStatus, IsTOAAuth, ColourCode, IsGrantTOAEnable, UpdQTSTime, AccessType, AckGrantTOATime, AckProtLimitTime, TARID, TOAID, and InchargeNRIC from #TmpRGS and orders the results by Sno.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_TAR_Sector, TAMS_Sector, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Power_Sector, TAMS_Access_Requirement, TAMS_Parameters.
* **Writes:** #TmpRGS, #TmpRGSSectors.

---


<a id='database-reference-sql-sp-tams-rgs-onload-20230202'></a>
# Procedure: sp_TAMS_RGS_OnLoad_20230202

### Purpose
This stored procedure performs a daily load of data for the RGS (Remote Grid System) system, updating and populating various tables with relevant information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
The procedure starts by truncating two temporary tables: #TmpRGS and #TmpRGSSectors. It then sets the current date and time, as well as the operation and access dates for the day.

Next, it retrieves the RGS possession background (RGSPossBG) and protection background (RGSProtBG) values from the TAMS_Parameters table based on the line number (@Line). If the current time is after a certain cutoff time, it sets the operation date to the current date; otherwise, it sets the operation date to the previous day.

The procedure then declares two cursors: @Cur01 and @Cur02. The first cursor fetches data from the TAMS_TAR and TAMS_TOA tables based on the line number (@Line) and access date (@AccessDate). The second cursor is used for electrical sector processing, but its logic is not fully explained in the provided code.

For each row fetched by the cursors, the procedure updates various fields in the #TmpRGS table. It also checks for certain conditions, such as the TOA status (6) and the possession counter, to determine whether to grant or cancel a TOA (Temporary Occupation Authorization).

Finally, the procedure inserts the updated data into the #TmpRGS table and fetches the next row from the cursors.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_TAR_Sector, TAMS_Sector, TAMS_TAR_Power_Sector, TAMS_Access_Requirement, TAMS_Traction_Power_Detail, TAMS_OCC_Auth, TAMS_Power_Sector
* **Writes:** #TmpRGS

---


<a id='database-reference-sql-sp-tams-rgs-onload-20230707'></a>
# Procedure: sp_TAMS_RGS_OnLoad_20230707

### Purpose
This stored procedure performs a daily load of TAMS RGS data, including reading and processing various tables to generate reports.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used for parameterization |

### Logic Flow
The procedure starts by truncating two temporary tables: #TmpRGS and #TmpRGSSectors. It then sets up various variables, including the current date and time, cutoff times, and parameters.

1. If the current time is after the cutoff time, it sets the operation date to the current date and the access date to the next day.
2. Otherwise, it sets the operation date to the previous day and the access date to the current date.
3. The procedure then selects various parameters from TAMS_Parameters based on the line number.
4. It uses two cursors (@Cur01 and @Cur02) to iterate through the TAMS_TAR table, selecting relevant data for each row.
5. For each row, it generates a new record in #TmpRGS by combining data from various tables, including TAMS_TOA, TAMS_TAR_Sector, and TAMS_TAR_Power_Sector.
6. It also inserts data into #TmpRGSSectors based on the sector ID.
7. After processing all rows, it fetches the final records from @Cur01 and inserts them into #TmpRGS.
8. Finally, it drops the temporary tables.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_TAR_Sector, TAMS_Power_Sector, TAMS_Parameters, TAMS_OCC_Auth
* **Writes:** #TmpRGS, #TmpRGSSectors

---


<a id='database-reference-sql-sp-tams-rgs-onload-20250128'></a>
# Procedure: sp_TAMS_RGS_OnLoad_20250128

### Purpose
This stored procedure performs a series of operations to retrieve and process data related to TAMS (Track and Maintenance System) for RGS (Railway Group Standardization) on-board equipment.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used to filter the data. |
| @TrackType | NVARCHAR(50) | The track type used to filter the data. |

### Logic Flow

1. The procedure starts by setting up variables for the current date and time, as well as a cutoff time.
2. It then checks if the current time is after the cutoff time. If it is, the procedure sets the operation date to the current date and the access date to the next day. Otherwise, it sets the operation date to the previous day and the access date to the current date.
3. The procedure retrieves three parameters from the TAMS_Parameters table: RGSPossessionBG, RGSProtectionBG, and RGSCancelledBG, based on the line number provided.
4. It then checks if there are any existing possession controls for the specified line and track type. If there are, it sets a flag to 1; otherwise, it sets the flag to 0.
5. The procedure then selects data from the TAMS_TAR and TAMS_TOA tables based on the access date, track type, and line number provided. It orders the results by AccessType, TOAStatus, and TARId.
6. For each row in the result set, it calculates various values such as PowerOffTime, CircuitBreakOutTime, and CallBackTime using subqueries and case statements.
7. The procedure then joins the TAMS_TAR and TAMS_TOA tables again to retrieve additional data such as PartiesName, NoOfParties, WorkDescription, ContactNo, TOANo, and Remarks.
8. Finally, it orders the results by AccessType, TOAStatus, and TARId.

### Data Interactions

* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-rgs-onload-acksms'></a>
# Procedure: sp_TAMS_RGS_OnLoad_AckSMS

The procedure retrieves and formats data from TAMS_TOA and TAMS_TAR tables to display access type, grant time, protection limit time, TAR number, and TOANumber for a specific TARID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR to retrieve data for. |

### Logic Flow
1. The procedure starts by selecting data from TAMS_TOA and TAMS_TAR tables.
2. It filters the data based on the provided TARID, ensuring only relevant records are retrieved.
3. The selected data is then formatted into a readable format, including access type, grant time, protection limit time, TAR number, and TOANumber.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR

---


<a id='database-reference-sql-sp-tams-rgs-onload-acksms-20221107'></a>
# Procedure: sp_TAMS_RGS_OnLoad_AckSMS_20221107

### Purpose
This stored procedure retrieves and formats specific data from the TAMS_TOA and TAMS_TAR tables to acknowledge SMS notifications for a given TARID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID	| BIGINT | The ID of the TAR (Target Access Record) for which to retrieve acknowledgement data. |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_TOA and TAMS_TAR tables.
2. It filters the results based on the provided TARID, ensuring that only matching records are returned.
3. The selected data is then formatted into a readable format for acknowledgement purposes.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR

---


<a id='database-reference-sql-sp-tams-rgs-onload-enq'></a>
# Procedure: sp_TAMS_RGS_OnLoad_Enq

### Purpose
This stored procedure performs an on-load inquiry for TAMS RGS data, retrieving relevant information from various tables and performing calculations to determine the status of each record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used to filter records. |
| @TrackType | nvarchar(50) | The track type used to filter records. |
| @OPDate | NVARCHAR(20) | The operation date used to filter records. |

### Logic Flow
The procedure follows these steps:

1. It truncates two temporary tables, #TmpRGS and #TmpRGSSectors, to ensure a clean start.
2. It sets the current date and time variables based on the input parameters @OPDate and @Line.
3. If the current time is greater than a specified cutoff time (06:00:00), it sets the operation date to the current date and the access date to the next day; otherwise, it sets both dates to the previous day.
4. It retrieves values from TAMS_Parameters table based on input parameters @Line and @TrackType to determine TOACallBackTime, RGSPossBG, RGSProtBG, and RGSCancBG.
5. It checks if there are any records in TAMS_OCC_Auth that match the current date and time, and if so, it sets IsTOAAuth to 1.
6. For each record in TAMS_TAR, it performs the following checks:
	* If the line is 'DTL', it retrieves additional information from TAMS_TAR_AccessReq table based on @Line and @TrackType.
	* It calculates the color code for the record based on its status and sets IsGrantTOAEnable accordingly.
7. It inserts the calculated values into #TmpRGS temporary table.
8. Finally, it fetches all records from #TmpRGS and displays them in a sorted order.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_TAR_Sector, TAMS_Sector, TAMS_Parameters, TAMS_TAMSTOASector, TAMS_TAR_AccessReq.
* **Writes:** #TmpRGS temporary table.

---


<a id='database-reference-sql-sp-tams-rgs-onload-enq-20221107'></a>
# Procedure: sp_TAMS_RGS_OnLoad_Enq_20221107

### Purpose
This stored procedure is used to retrieve and process data related to RGS (Remote Ground Station) operations, specifically for possession and non-possession scenarios.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used to filter the data. |

### Logic Flow
The procedure follows these steps:

1. It first checks if the current time is greater than a specified cutoff time (06:00:00). If true, it sets the operation date and access date accordingly.
2. It then retrieves the TOA callback time, RGS possession background, and RGS protection background from the TAMS_Parameters table based on the line number.
3. The procedure then loops through each TAR record that matches the specified conditions (TOAStatus <> 0) and fetches the corresponding TOA details.
4. For each TAR record, it checks if the sector is a power sector or not. If it's a power sector, it processes the data accordingly. Otherwise, it treats it as a non-power sector scenario.
5. The procedure then inserts the processed data into two temporary tables: #TmpRGS and #TmpRGSSectors.
6. Finally, it retrieves the data from these temporary tables and returns it in a formatted structure.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_Parameters, TAMS_TAR_Sector, TAMS_Sector, TAMS_Traction_Power_Detail, TAMS_Power_Sector

---


<a id='database-reference-sql-sp-tams-rgs-onload-enq-20230202'></a>
# Procedure: sp_TAMS_RGS_OnLoad_Enq_20230202

### Purpose
This stored procedure performs a load of data for the RGS (Remote Grid System) onboarding process, including retrieving and processing relevant data from various tables.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used to retrieve specific parameters. |

### Logic Flow
The procedure follows these steps:

1. It sets up two cursors, `@Cur01` and `@Cur02`, to iterate through the relevant data in the `TAMS_TAR` and `TAMS_TOA` tables.
2. For each iteration, it retrieves specific parameters such as `ARRemark`, `TVFMode`, `AccessType`, `TOAStatus`, `ProtTimeLimit`, `GrantTOATime`, `AckSurrenderTime`, `AckGrantTOATime`, `UpdateQTSTime`, and `InchargeNRIC`.
3. It then processes this data to determine the relevant RGS information, such as `ElectricalSections`, `PowerOffTime`, `CircuitBreakOutTime`, `PartiesName`, `NoOfPersons`, `WorkDescription`, `ContactNo`, `TOANo`, `CallBackTime`, `RadioMsgTime`, `LineClearMsgTime`, and `Remarks`.
4. It inserts this processed data into a temporary table, `#TmpRGS`.
5. Finally, it retrieves the data from the temporary table and returns it in a formatted output.

### Data Interactions
* **Reads:**
	+ TAMS_TAR
	+ TAMS_TOA
	+ TAMS_Parameters
	+ TAMS_TAR_Sector
	+ TAMS_Power_Sector
	+ TAMS_Access_Requirement
	+ TAMS_Get_ES
	+ TAMS_Get_TOA_TVF_Stations
* **Writes:**
	+ #TmpRGS

---


<a id='database-reference-sql-sp-tams-rgs-onload-enq-20230202-m'></a>
# Procedure: sp_TAMS_RGS_OnLoad_Enq_20230202_M

### Purpose
This stored procedure performs a load of data for the RGS (Radio Frequency System) onboarding process, including retrieving and processing data from various tables in the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to be processed. |

### Logic Flow
The procedure follows these steps:

1. It truncates two temporary tables, #TmpRGS and #TmpRGSSectors, to ensure a clean start.
2. It retrieves the current date and time using the GETDATE() function.
3. It sets up variables for the operation date and access date based on the current date and time.
4. If the current time is greater than 6:00 AM, it sets the operation date to the current date; otherwise, it sets it to the previous day's date.
5. It retrieves parameters from the TAMS_Parameters table using the @Line parameter.
6. It loops through each sector in the TAMS_TAR_Power_Sector or TAMS_TAR_Sector tables and processes the data accordingly:
	* For sectors with a power sector ID, it inserts data into #TmpRGSSectors.
	* For sectors without a power sector ID, it inserts data into #TmpRGS.
7. It retrieves additional parameters from the TAMS_TAR table using the @Line parameter.
8. If the line number is 'DTL', it sets up variables for the electrical sections and parties name based on the retrieved data.
9. It loops through each record in the TAMS_TOA table and processes the data accordingly:
	* For records with a TOA status of 6, it inserts data into #TmpRGS.
	* For records without a TOA status of 6, it sets up variables for the electrical sections and parties name based on the retrieved data.
10. It inserts the processed data from #TmpRGS into the TAMS_TAR table.
11. Finally, it drops the temporary tables.

### Data Interactions
* **Reads:**
	+ TAMS_Parameters
	+ TAMS_TAR_Power_Sector
	+ TAMS_TAR_Sector
	+ TAMS_TAR
	+ TAMS_TOA
	+ TAMS_TAMSSectors
* **Writes:**
	+ #TmpRGS
	+ #TmpRGSSectors
	+ TAMS_TAR

---


<a id='database-reference-sql-sp-tams-rgs-onload-m'></a>
# Procedure: sp_TAMS_RGS_OnLoad_M

### Purpose
This stored procedure performs a daily maintenance task for the RGS (Remote Grid System) system, updating and populating various tables with data from the TAMS (Transmission Automation Management System) database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
The procedure starts by truncating two temporary tables, #TmpRGS and #TmpRGSSectors, which are used to store intermediate data during the processing.

1. It then retrieves the current date and time.
2. Based on the value of @Line, it determines whether to use the sector or power sector cursor to retrieve data from TAMS_TAR and TAMS_TAR_Power_Sector tables.
3. For each record retrieved, it populates a temporary table with various fields such as ElectricalSections, PowerOffTime, PartiesName, etc.
4. It then inserts these records into #TmpRGS.
5. After processing all records, it fetches the final data from #TmpRGS and orders it by Sno.
6. Finally, it drops the temporary tables.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_TAR_Sector, TAMS_Sector, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Power_Sector
* **Writes:** #TmpRGS

---


<a id='database-reference-sql-sp-tams-rgs-onload-trace'></a>
# Procedure: sp_TAMS_RGS_OnLoad_Trace

### Purpose
This stored procedure performs a series of operations to trace and record the status of RGS (Remote Ground Station) systems, including power off and circuit break times, parties involved, and other relevant details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number for which the procedure is being executed. |

### Logic Flow
The procedure follows these steps:

1. It truncates two temporary tables, #TmpRGS and #TmpRGSSectors, to ensure they are empty before processing.
2. It sets various variables based on the current date and time, as well as parameters passed to the procedure.
3. It uses two cursors, @Cur01 and @Cur02, to iterate through TAMS_TAR and TAMS_TOA tables, respectively, filtering rows where the TOAStatus is not 0, 5, or 6, and the AccessDate matches the specified date.
4. For each row in the cursor, it extracts various details such as TARNo, PartiesName, PowerOffTime, CircuitBreakOutTime, etc., and stores them in temporary variables.
5. It then inserts these details into #TmpRGS table based on the line number passed to the procedure.
6. After processing all rows in both cursors, it fetches the Sno values from #TmpRGS and orders them by Sno for display purposes.
7. Finally, it drops the temporary tables and returns.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_Sector, TAMS_Power_Sector
* **Writes:** #TmpRGS, #TmpRGSSectors

---


<a id='database-reference-sql-sp-tams-rgs-onload-yd-test-20231208'></a>
# Procedure: sp_TAMS_RGS_OnLoad_YD_TEST_20231208

### Purpose
This stored procedure performs a series of operations to load data into temporary tables for further processing, specifically for the RGS (Remote Grid System) system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
1. The procedure starts by truncating two temporary tables, #TmpRGS and #TmpRGSSectors.
2. It then sets the current date and time variables based on the system clock.
3. Depending on the value of @Line (either 'DTL' or 'NEL'), it performs different operations:
	* For 'DTL', it checks for rackout records, calculates possession counters, and updates grant TOA enable flags.
	* For 'NEL', it follows a similar process but with some differences in logic.
4. It then fetches data from the TAMS_TAR and TAMS_TOA tables based on the specified line number and track type.
5. The procedure processes each record by:
	* Calculating possession counters
	* Updating grant TOA enable flags
	* Setting colors for rackout and grant TOA records
	* Inserting data into #TmpRGS
6. After processing all records, it fetches the operation date and access date.
7. Finally, it drops the temporary tables.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_TAR_Sector, TAMS_Sector, TAMS_Parameters
* **Writes:** #TmpRGS

---


<a id='database-reference-sql-sp-tams-rgs-onload-20221118-m'></a>
# Procedure: sp_TAMS_RGS_OnLoad_20221118_M

### Purpose
This stored procedure performs a series of tasks to load data into various tables, including TAMS_TAR and TAMS_TOA. The purpose is to update the status of possession and protection for each line.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number for which data needs to be loaded |

### Logic Flow
The procedure starts by truncating two temporary tables, #TmpRGS and #TmpRGSSectors. It then sets the current date and time variables based on the input line.

Next, it checks if the current time is greater than a certain cutoff time (06:00:00). If true, it sets the operation date to the current date and the access date to the next day. Otherwise, it sets the operation date to the previous day and the access date to the current date.

The procedure then selects data from TAMS_TAR and TAMS_TOA tables based on the input line and access date. It loops through each record and performs the following steps:

1. Checks if the TOA status is 6 (cancelled). If true, it sets a flag indicating that the TOA has been cancelled.
2. Retrieves data from TAMS_TAMSSectors table for each sector ID in the current line.
3. Loops through each sector record and performs the following steps:
	* Checks if the sector ID exists in the TAMS_Sector table. If true, it inserts a new record into #TmpRGSSectors table.
	* Retrieves data from TAMS_TAR_Power_Sector table for each power sector ID in the current line.
4. Loops through each power sector record and performs the following steps:
	* Checks if the power sector ID exists in the TAMS_Power_Sector table. If true, it inserts a new record into #TmpRGSSectors table.
5. Inserts data from #TmpRGS temporary table into TAMS_TAR and TAMS_TOA tables.

### Data Interactions
* **Reads:** 
	+ TAMS_TAR
	+ TAMS_TOA
	+ TAMS_TAMSSectors
	+ TAMS_Power_Sector
	+ TAMS_Sector
	+ TAMS_Access_Requirement
	+ TAMS_Parameters
* **Writes:** 
	+ #TmpRGS temporary table
	+ TAMS_TAR
	+ TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-onload-20230202-m'></a>
# Procedure: sp_TAMS_RGS_OnLoad_20230202_M

### Purpose
This stored procedure performs a daily load of data for the RGS (Remote Grid System) system, updating and populating various tables with relevant information.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number to process. |

### Logic Flow
1. The procedure starts by truncating two temporary tables: #TmpRGS and #TmpRGSSectors.
2. It then retrieves the current date and time, as well as the operation and access dates for the day.
3. Based on the line number (@Line), it determines whether to process a DTL (Distribution Transformer Load) or NEL (Network Equipment Load) scenario.
4. For each line, it iterates through all TAMS_TAR records with an AccessDate matching the current date and TOAStatus not equal to 0 or 6.
5. It then fetches the corresponding TAMS_TOA record for each TARId and processes its data:
	* If the TOAStatus is 6 (cancelled), it updates the #TmpRGS table with the cancelled remark.
	* Otherwise, it populates the #TmpRGS table with various fields such as Sno, TARNo, ElectricalSections, PowerOffTime, CircuitBreakOutTime, PartiesName, NoOfPersons, WorkDescription, ContactNo, TOANo, CallbackTime, RadioMsgTime, LineClearMsgTime, Remarks, TOAStatus, IsTOAAuth, ColourCode, IsGrantTOAEnable, UpdQTSTime, AccessType, AckGrantTOATime, AckProtLimitTime, TARID, TOAID, and InchargeNRIC.
6. After populating the #TmpRGS table, it fetches the corresponding TAMS_TAR_Sector or TAMS_Power_Sector records for each line and processes their data:
	* For TAMS_TAR_Sector records, it updates the #TmpRGSSectors table with various fields such as OCCAuthStatusId, OperationDate, AccessDate, SectorID, Sector, WorkFlowTime.
	* For TAMS_Power_Sector records, it updates the #TmpRGSSectors table with various fields such as OCCAuthStatusId, OperationDate, AccessDate, PowerSectorId, WorkFlowTime.
7. Finally, it closes both cursors and deallocates resources.

### Data Interactions
* **Reads:**
	+ TAMS_TAR records
	+ TAMS_TOA records
	+ TAMS_TAR_Sector records
	+ TAMS_Power_Sector records
	+ TAMS_Parameters records (for retrieving RGS-related parameters)
* **Writes:**
	+ #TmpRGS table
	+ #TmpRGSSectors table

---


<a id='database-reference-sql-sp-tams-rgs-update-details'></a>
# Procedure: sp_TAMS_RGS_Update_Details

### Purpose
This stored procedure updates the details of a TAMS Record Group (RGS) by checking the qualification status of an in-charge person and updating their details if necessary.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID of the RGS to be updated. |
| @InchargeNRIC | NVARCHAR(50) | The NRIC of the in-charge person. |
| @MobileNo | NVARCHAR(20) | The mobile number of the in-charge person. |
| @TetraRadioNo | NVARCHAR(50) | The Tetra radio number of the in-charge person. |
| @UserID | NVARCHAR(50) | The ID of the user updating the RGS. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |

### Logic Flow
1. The procedure checks if a transaction has been started and sets an internal transaction flag.
2. It creates a temporary table #tmpnric to store the qualification status of the in-charge person.
3. The procedure truncates the temporary table and inserts a new record into it using a stored procedure sp_TAMS_TOA_QTS_Chk.
4. It selects the in-charge name and status from the temporary table.
5. If the in-charge status is 'InValid', the procedure checks if the access type is 'Protection'. If so, it truncates the temporary table again and inserts a new record into it using sp_TAMS_TOA_QTS_Chk with the correct qualification code.
6. The procedure then checks if the in-charge person is new or not. If they are new, it updates their details in TAMS_TOA and inserts audit records for TAMS_TOA and TAMS_TOA_Parties.
7. If the in-charge status is 'Valid', the procedure updates the mobile number and Tetra radio number of the in-charge person in TAMS_TOA.
8. The procedure then commits or rolls back the transaction based on whether an error occurred during execution.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_TOA_Audit, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties

---


<a id='database-reference-sql-sp-tams-rgs-update-qts'></a>
# Procedure: sp_TAMS_RGS_Update_QTS

### Purpose
This stored procedure updates the qualification status of a train's access date and retrieves the corresponding QTS (Qualification Time System) code.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The TAR ID of the train to update. |
| @InchargeNRIC | NVARCHAR(50) | The NRIC of the in-charge person. |
| @UserID | NVARCHAR(500) | The user ID of the current user. |
| @TrackType | NVARCHAR(50)='Mainline' | The track type of the train (default: Mainline). |
| @Message | NVARCHAR(500) = NULL OUTPUT | The output message indicating the result of the update operation. |
| @QTSQCode | NVARCHAR(50) = NULL OUTPUT | The QTS code corresponding to the updated qualification status. |
| @QTSLine | NVARCHAR(10) = NULL OUTPUT | The line number corresponding to the updated qualification status. |

### Logic Flow
1. Check if a transaction is already in progress. If not, start a new transaction.
2. Create a temporary table `#tmpnric` to store the results of the QTS check.
3. Truncate the temporary table and insert a record into it using the `sp_TAMS_TOA_QTS_Chk` stored procedure.
4. Retrieve the in-charge name and status from the temporary table.
5. Check if the in-charge status is 'InValid'. If so, perform additional checks:
	* If the access type is 'Protection', truncate the temporary table and insert a new record using `sp_TAMS_TOA_QTS_Chk`.
	* Otherwise, set the QTS fin status to 'InValid' and the QTS fin qualification code to an empty string.
6. If the in-charge status is not 'InValid', update the QTS fin status and qualification code based on the retrieved values from the temporary table.
7. Call the `sp_api_tams_qts_upd_accessdate` stored procedure to update the access date of the train.
8. Insert an audit record into the `TAMS_TOA_Audit` table.
9. If any errors occur during the update operation, log the error and return a message indicating the result.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TAR, TAMS_Parameters, QTSDB (for storing audit records)
* Writes: TAMS_TOA_Audit

---


<a id='database-reference-sql-sp-tams-rgs-update-qts-20230907'></a>
# Procedure: sp_TAMS_RGS_Update_QTS_20230907

### Purpose
This stored procedure updates the qualification status of a TAR (Tender Acceptance Record) based on the QTS (Qualification Testing System) data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR to be updated. |
| @InchargeNRIC | NVARCHAR(50) | The NRIC number of the in-charge person. |
| @UserID | NVARCHAR(500) | The user ID of the person performing the update. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |
| @QTSQCode | NVARCHAR(50) = NULL OUTPUT | An output parameter to store the QTS qualification code. |
| @QTSLine | NVARCHAR(10) = NULL OUTPUT | An output parameter to store the line number of the TAR. |

### Logic Flow
1. The procedure starts by checking if a transaction has been started. If not, it sets an internal flag and begins a new transaction.
2. It creates a temporary table #tmpnric to store the in-charge person's details.
3. The procedure then selects the TAR ID, access date, TOA ID, and access type from the TAMS_TOA and TAMS_TAR tables based on the provided TAR ID.
4. It retrieves the QTS qualification code and protocol code for the selected line number from the TAMS_Parameters table.
5. If the in-charge person's status is 'InValid', it checks if they have access to the protection area. If not, it truncates the temporary table and sets the in-charge person's details again.
6. It then updates the TAR with the new QTS qualification code and line number, and inserts an audit record into the TAMS_TOA_Audit table.
7. The procedure then calls another stored procedure [mssqldevpsvr1].[QTSDB].[dbo].[sp_api_tams_qts_upd_accessdate] to update the access date of the in-charge person based on the new QTS qualification code.
8. If an error occurs during this process, it sets an error message and returns it to the caller.
9. Finally, if no errors occurred, it commits the transaction and returns a success message.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_TOA_Audit
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-update-qts-bak20221229'></a>
# Procedure: sp_TAMS_RGS_Update_QTS_bak20221229

### Purpose
This stored procedure updates the qualification status of a TAR (Target Area Record) based on the user's input and checks for any errors.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR record to be updated. |
| @InchargeNRIC | NVARCHAR(50) | The NRIC (National Registration Identity Card) number of the in-charge person. |
| @UserID | NVARCHAR(500) | The user ID of the person performing the update. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |
| @QTSQCode | NVARCHAR(50) = NULL OUTPUT | An output parameter to store the updated QTS (Qualification and Standards) code. |
| @QTSLine | NVARCHAR(10) = NULL OUTPUT | An output parameter to store the updated QTS line number. |

### Logic Flow
1. The procedure starts by checking if a transaction has been started. If not, it sets an internal flag (`@IntrnlTrans`) to 1 and begins a new transaction.
2. It creates a temporary table (`#tmpnric`) to store the in-charge person's details.
3. The procedure truncates the temporary table and then inserts a record into it using a dynamic SQL command (`sp_TAMS_TOA_QTS_Chk`).
4. It selects the in-charge person's name and status from the temporary table.
5. Based on the in-charge person's status, the procedure checks if the TAR record is valid or not. If it's invalid, it updates the QTS code to 'InValid' and sets `@QTSFinStatus` to 'InValid'. If it's valid, it updates the QTS code to the corresponding value.
6. The procedure then updates the TAR record with the new QTS code and inserts an audit record into the `TAMS_TOA_Audit` table.
7. Finally, it checks for any errors that may have occurred during the update process and returns an error message if necessary.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_TOA_Audit
* **Writes:** TAMS_TOA

---


<a id='database-reference-sql-sp-tams-rgs-update-qts-test'></a>
# Procedure: sp_TAMS_RGS_Update_QTS_test

### Purpose
This stored procedure updates the qualification status of a user's access to a TAR (Technical Access Record) based on their QTS (Qualification and Testing System) code.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAR record being updated. |
| @InchargeNRIC | NVARCHAR(50) | The National Registration Identification Number (NRIC) of the in-charge person. |
| @UserID | NVARCHAR(500) | The user ID of the user whose access is being updated. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that returns a message indicating the result of the update operation. |
| @QTSQCode | NVARCHAR(50) = NULL OUTPUT | An output parameter that returns the QTS qualification code for the user's access. |
| @QTSLine | NVARCHAR(10) = NULL OUTPUT | An output parameter that returns the line number associated with the user's access. |

### Logic Flow
1. The procedure starts by checking if a transaction has been started. If not, it sets an internal transaction flag to 1 and begins a new transaction.
2. It creates a temporary table #tmpnric to store the in-charge person's details.
3. The procedure then selects the TAR record associated with the given @TARID and retrieves the user's access date, TOA ID, and access type from TAMS_TOA and TAMS_TAR tables respectively.
4. It then checks if the user has a valid QTS qualification code for their access. If not, it sets an error message and returns without updating the TAR record.
5. If the user has a valid QTS qualification code, it updates the TAR record with the new QTS qualification code and inserts an audit record into TAMS_TOA_Audit table.
6. The procedure then checks if there are any errors during the update operation. If so, it rolls back the transaction and returns an error message.
7. If no errors occur, it commits the transaction and returns a success message with the updated QTS qualification code and line number.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TAR, TAMS_Parameters, TAMS_TOA_Audit
* Writes: #tmpnric (temporary table), TAMS_TOA (TAR record)

---


<a id='database-reference-sql-sp-tams-reject-userregistrationrequestbyregmodid'></a>
# Procedure: sp_TAMS_Reject_UserRegistrationRequestByRegModID

### Purpose
This stored procedure is used to reject a user registration request based on the status of the corresponding module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the module that needs to be rejected. |
| @UpdatedBy | INT | The ID of the user who is updating the registration request. |

### Logic Flow
The procedure follows these steps:
1. It retrieves the current status and details of the module with the given ID.
2. If the status is 'Pending Company Registration' or 'Pending Company Approval', it rejects the entire request by setting the status to 'Rejected'.
3. If the status is 'Pending System Admin Approval' or 'Pending System Approver Approval', it also rejects the request but moves to a different stage.
4. It sends an email notification to the registered user with the rejection reason.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_WFStatus, TAMS_Registration, TAMS_Action_Log, EAlertQ_EnQueue

---


<a id='database-reference-sql-sp-tams-reject-userregistrationrequestbyregmodid-20231009'></a>
# Procedure: sp_TAMS_Reject_UserRegistrationRequestByRegModID_20231009

### Purpose
This stored procedure is used to reject a user registration request based on the status of the corresponding company registration module.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the company registration module. |
| @UpdatedBy | INT | The ID of the user who updated the registration request. |

### Logic Flow
The procedure follows these steps:

1. It retrieves the current status of the company registration module associated with the provided `@RegModID`.
2. If the status is 'Pending Company Registration' or 'Pending Company Approval', it rejects the entire request and sends an email to all registered users.
3. If the status is 'Pending System Admin Approval' or 'Pending System Approver Approval', it rejects the request and sends an email to the user who submitted the registration request.

### Data Interactions
* **Reads:** TAMS_Reg_Module, TAMS_WFStatus, TAMS_Registration
* **Writes:** TAMS_Reg_Module (updates RegStatus), TAMS_Action_Log

---


<a id='database-reference-sql-sp-tams-sectorbooking-onload'></a>
# Procedure: sp_TAMS_SectorBooking_OnLoad

### Purpose
This stored procedure is used to load sector booking data into a temporary table, which can then be used for further processing or reporting.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number of the track type. |
| @TrackType | NVARCHAR(50) | The track type (e.g., 'DTL', 'NEL'). |
| @AccessDate | NVARCHAR(20) | The access date for the sector booking. |
| @TARType | NVARCHAR(20) | The TAR type (e.g., '2', '3'). |
| @AccessType | NVARCHAR(20) | The access type (e.g., 'Protection', 'Possession'). |

### Logic Flow
The procedure follows these steps:

1. It truncates an existing temporary table (`#ListES`) to ensure it is empty before loading new data.
2. Based on the `@Line` parameter, it determines whether to load data for a 'DTL' or 'NEL' track type.
3. For each line number, it selects relevant sector data from the `TAMS_Sector` table based on the track type and active status.
4. It then iterates through the selected sectors, updating the temporary table with entry station information, color codes, and other relevant details.
5. Depending on the access type, it updates the temporary table to reflect whether a sector is enabled or disabled.
6. Finally, it selects data from the temporary table for both 'DirID' values (1 and 2) and orders the results by `OrderID` and `SectorID`.

### Data Interactions
* Reads: `TAMS_Sector`, `TAMS_Station`, `TAMS_Entry_Station`, `TAMS_TAR`, `TAMS_Access_Requirement`
* Writes: `#ListES`

---


<a id='database-reference-sql-sp-tams-sectorbooking-onload-bak20230605'></a>
# Procedure: sp_TAMS_SectorBooking_OnLoad_bak20230605

### Purpose
This stored procedure loads sector booking data for TAMS (Track and Manage Systems) based on the provided line, access date, TAR type, and access type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		| NVARCHAR(10) | The line number to load sector booking data for. |
| @AccessDate	| NVARCHAR(20) | The access date to filter sector booking data by. |
| @TARType	| NVARCHAR(20) | The TAR type to filter sector booking data by. |
| @AccessType	| NVARCHAR(20) | The access type to filter sector booking data by. |

### Logic Flow
1. The procedure starts by creating a temporary table #ListES to store the loaded sector booking data.
2. It truncates the existing data in #ListES and declares several cursor variables to iterate through the sector booking data.
3. Based on the provided line, it inserts data into #ListES from TAMS_Sector table if the line is 'DTL'. If the line is 'NEL', it inserts data into #ListES from TAMS_Sector table based on specific conditions.
4. It opens a cursor to iterate through the sector booking data for the specified line and access date.
5. For each iteration, it updates the EntryStation and ColorCode columns in #ListES based on the corresponding TAR type and access type.
6. If the access type is 'Protection', it filters the sector booking data further based on specific conditions.
7. Finally, it selects the loaded sector booking data from #ListES and returns the results.

### Data Interactions
* **Reads:** TAMS_Sector table
* **Writes:** TAMS_Sector table

---


<a id='database-reference-sql-sp-tams-sectorbooking-qts-chk'></a>
# Procedure: sp_TAMS_SectorBooking_QTS_Chk

### Purpose
This stored procedure checks if a sector booking is valid for a given person, based on their qualification details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(MAX) | The National Registration Identity Number of the person. |
| @qualdate | NVARCHAR(MAX) | The date of the person's qualification. |
| @line | NVARCHAR(MAX) | The line number associated with the sector booking. |
| @TrackType | NVARCHAR(50) | The type of track for the sector booking. |

### Logic Flow
1. The procedure starts by declaring variables to store error messages and cursor handles.
2. It then creates temporary tables #tmpnric and #tmpqtsqc to store qualification data.
3. The procedure truncates these tables before processing new data.
4. It selects the relevant qualification details from TAMS_Parameters based on the provided line number and date of qualification.
5. For each person in the #tmpnric table, it queries the QTS_Personnel and QTS_Qualification tables to retrieve their qualification details.
6. If no suspension information is found for a person's qualification, the procedure updates their status as "InValid".
7. If suspension information is found, but the person's qualification date is before the valid access date or after the valid till date, the procedure updates their status as "InValid".
8. Otherwise, if the person's qualification date falls within the valid access and valid till dates, the procedure updates their status as "Valid".
9. Finally, the procedure returns the updated qualification details for each person.

### Data Interactions
* **Reads:** TAMS_Parameters, QTS_Personnel, QTS_Qualification tables.
* **Writes:** #tmpnric and #tmpqtsqc temporary tables.

---


<a id='database-reference-sql-sp-tams-sectorbooking-special-rule-chk'></a>
# Procedure: sp_TAMS_SectorBooking_Special_Rule_Chk

### Purpose
This stored procedure checks for special rules related to sector bookings, specifically for possession and protection access types.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessType | NVARCHAR(20) | The type of access (Possession or Protection) |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sector IDs |
| @PowerSelTxt | NVARCHAR(50) | The selected power option |

### Logic Flow
The procedure follows these steps:

1. Determine the power on indicator based on the selected power option.
2. If possession access type is selected and power is off, check if there are any special sectors with active bookings.
3. If protection access type is selected and power is off, check if there are any special sectors with active bookings.
4. For each sector ID in the list, check if it has a corresponding booking record in the TAMS_Special_Sector_Booking table.
5. If a booking record exists, check if all combinations for that sector ID have been completed (i.e., CombCheck = 1).
6. If any combination is missing, update the corresponding records in #TmpCombSectMax with CombCheck = 0.
7. After checking all sector IDs, count the number of missing combinations and return a result code.

### Data Interactions
* Reads: TAMS_Sector, TAMS_Special_Sector_Booking
* Writes: #TmpCombSect, #TmpCombSectMax

---


<a id='database-reference-sql-sp-tams-sectorbooking-subset-chk'></a>
# Procedure: sp_TAMS_SectorBooking_SubSet_Chk

### Purpose
This stored procedure checks if two sets of sector IDs are subsets of each other.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @D1SelSec	| NVARCHAR(2000) | The first set of sector IDs separated by semicolons. |
| @D2SelSec	| NVARCHAR(2000) | The second set of sector IDs separated by semicolons. |

### Logic Flow
The procedure works as follows:
1. It creates temporary tables to store the sector IDs from both input sets.
2. It truncates these temporary tables, effectively removing any existing data.
3. It inserts the sector IDs from both input sets into their respective temporary tables.
4. It counts the number of unique sector IDs in each table.
5. If the first set has more unique sector IDs than the second set, it checks if all sector IDs in the first set are present in the second set.
6. If the second set has more unique sector IDs than the first set, it performs a similar check in reverse.
7. Based on these comparisons, the procedure sets an error code indicating whether the two sets are subsets of each other.

### Data Interactions
* **Reads:** [dbo].[SPLIT], [dbo].[SPLIT]
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-summaryreport-onload'></a>
# Procedure: sp_TAMS_SummaryReport_OnLoad

### Purpose
This stored procedure generates a summary report for TAMS (Tracking and Management System) by retrieving data from various tables based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Specifies the line type (DTL or NEL). |

### Logic Flow
The procedure follows these steps:

1. It checks if the current time is before a specified cut-off time based on the provided line and track type parameters.
2. If the current time is before the cut-off, it sets the access date to the previous day; otherwise, it sets it to the current date.
3. It checks if the access date is valid for the selected report date.
4. If the access date is not valid, it returns an error message.
5. Otherwise, it retrieves data from various tables (TAMS_TAR, TAMS_TOA) based on the provided parameters and line type.
6. It calculates the number of approved tar for possession, protection, executed, and not executed categories.
7. It constructs lists of approved tar numbers for each category by concatenating the retrieved IDs.
8. Finally, it returns a summary report with the calculated values.

### Data Interactions
* Reads: TAMS_TAR, TAMS_TOA
* Writes: None

---


<a id='database-reference-sql-sp-tams-summaryreport-onload-20230713'></a>
# Procedure: sp_TAMS_SummaryReport_OnLoad_20230713

### Purpose
This stored procedure generates a summary report for TAMS (Tactical Air Missile System) operations, including possession and protection counts, cancellations, and extended periods.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		NVARCHAR(20) = NULL, 
| @StrAccDate	NVARCHAR(20) = NULL |

### Logic Flow
1. The procedure starts by determining the current date and time.
2. It then checks if the current time is before a specified cut-off time for operations. If so, it sets the access date to the previous day; otherwise, it sets it to the current date.
3. The procedure then checks if the access date is valid for the selected report period. If not, it returns an error message.
4. It then retrieves counts of possession and protection TARS (Tactical Air Missile Systems) with specific statuses and lines.
5. Next, it iterates through a cursor of protection TARS to identify cancellations and updates the corresponding cancellation counters and strings.
6. Similarly, it iterates through a cursor of possession TARS to identify cancellations and updates the corresponding cancellation counters and strings.
7. Finally, it calculates extended periods for possession and protection TARS based on TOA (Tactical Operations Area) status and surrenders.
8. The procedure returns the calculated counts and statistics.

### Data Interactions
* **Reads:** 
	+ TAMS_TAR table
	+ TAMS_TOA table
	+ TAMS_Parameters table
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-summaryreport-onload-trace'></a>
# Procedure: sp_TAMS_SummaryReport_OnLoad_Trace

### Purpose
This stored procedure generates a summary report for TAMS (Tactical Air Missile System) on-load tracing, providing an overview of possession and protection status for specific lines and dates.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		NVARCHAR(20) = NULL | Specifies the line number to filter by. |
| @StrAccDate	NVARCHAR(20) = NULL | Specifies the access date to filter by. |

### Logic Flow
The procedure follows these steps:

1. It determines the current cut-off time for operations based on the provided line number.
2. If the current time is before the cut-off time, it sets the access date to the previous day; otherwise, it sets it to the current date.
3. It checks if the access date is valid and not ready for reporting (i.e., not equal to the specified access date).
4. If the access date is valid, it retrieves counts of possession and protection status for specific lines and dates from TAMS_TAR and TAMS_TOA tables.
5. It iterates through the retrieved data using cursors to identify canceled possessions and protections by checking if a line is not in the TOA table with a non-zero status.
6. It calculates additional counters for extended possession and protection statuses based on specific conditions (e.g., TOAStatus = 3 or SurrenderTime > '04:00:00').
7. Finally, it returns the calculated counts as output.

### Data Interactions
* Reads:
	+ TAMS_TAR table
	+ TAMS_TOA table
* Writes:
	+ None

---


<a id='database-reference-sql-sp-tams-summaryreport-onload-20240112-m'></a>
# Procedure: sp_TAMS_SummaryReport_OnLoad_20240112_M

### Purpose
This stored procedure generates a summary report for TAMS (Tracking and Asset Management System) on a specific date, providing insights into various aspects of the system.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Specifies the line type (DTL or NEL). |

### Logic Flow
The procedure follows these steps:

1. It determines the current date and time.
2. If the current time is before a specified cut-off time, it sets the access date to the previous day; otherwise, it sets it to the current date.
3. It checks if the selected access date matches the specified date in the report. If not, it returns an error message.
4. It retrieves data from various tables (TAMS_TAR and TAMS_TOA) based on the line type, track type, and access date.
5. For each retrieved record, it categorizes the TAR status into one of five categories: Possession, Protection, Executed, Not Executed, and Cancelled.
6. It counts and lists the number of records in each category for both Possession and Protection lines.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA

---


<a id='database-reference-sql-sp-tams-summaryreport-onload-bak20230712'></a>
# Procedure: sp_TAMS_SummaryReport_OnLoad_bak20230712

### Purpose
This stored procedure generates a summary report for TAMS (Tracking and Management System) on load, providing an overview of possession and protection status for specific lines and track types.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		NVARCHAR(20) = NULL | Specifies the line number to filter by. |
| @TrackType	NVARCHAR(50) = NULL | Specifies the track type to filter by. |
| @StrAccDate	NVARCHAR(20) = NULL | Specifies the access date to filter by. |

### Logic Flow
1. The procedure starts by determining the current cut-off time for operations based on the provided line and track type.
2. It then checks if the current time is before the cut-off time, and if so, sets the access date to the previous day; otherwise, it sets the access date to the current date.
3. If the access date is not equal to the specified access date, an error message is returned.
4. The procedure then initializes counters for possession and protection status, as well as variables to store the corresponding line numbers.
5. It uses two cursors (TARNo and TARNo2) to iterate through the TAMS_TAR table, filtering by access type, power on status, and line/track type. The cursors exclude rows with a TOAStatus of 0.
6. For each row in the cursors, it increments the corresponding counter for possession or protection status and appends the line number to the CancelPoss or CancelProt variable if it is not already set.
7. After iterating through all rows, it calculates the total count of possession and protection status using another two counters (ExtPossCtr and ExtProtCtr).
8. Finally, the procedure returns a result set containing the counts for possession, protection, and extended status.

### Data Interactions
* Reads: TAMS_TAR table
* Writes: None

---


<a id='database-reference-sql-sp-tams-summaryreport-onload-bak20240223'></a>
# Procedure: sp_TAMS_SummaryReport_OnLoad_bak20240223

### Purpose
This stored procedure generates a summary report for TAMS (Tracking and Management System) based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | Specifies the line type ('DTL' or 'NEL') to filter TAMS data. |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter TAMS data. |
| @StrAccDate | NVARCHAR(20) | Specifies the access date for which the report is generated. |

### Logic Flow
The procedure follows these steps:

1. It determines the cutoff time based on the provided line and track types.
2. If the current time is before the cutoff time, it sets the access date to the previous day; otherwise, it sets it to the current date.
3. It checks if the access date is valid for the selected report date. If not, it returns an error message.
4. It initializes counters and variables for possession, protection, and cancellation counts.
5. It queries TAMS_TAR table to retrieve possession and protection data based on the line type, track type, and access date.
6. It uses cursors to iterate through the retrieved data and update the counters and variables accordingly.
7. Finally, it returns the summary report with possession, protection, cancellation counts, and other relevant information.

### Data Interactions
* Reads: TAMS_TAR table for possession and protection data.
* Writes: None (the procedure only reads data from the database).

---


<a id='database-reference-sql-sp-tams-tar-view-detail-onload'></a>
# Procedure: sp_TAMS_TAR_View_Detail_OnLoad

### Purpose
This stored procedure is used to view detailed information on a specific TAMS TAR record, including its status, access details, and related data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the TAMS TAR record to be viewed. |
| @LogInUser | NVARCHAR(20) | The login user's username. |

### Logic Flow

1. The procedure starts by selecting the Line and AccessDate from the TAMS_TAR table where the ID matches the provided @TARID.
2. It then selects all columns from the TAMS_TAR table where the ID is equal to @TARID, which includes detailed information such as TARNo, TARType, Company, Designation, Name, OfficeNo, MobileNo, Email, SubmitDate, AccessDate, and more.
3. The procedure then performs several group-by operations on related tables:
	* TAMS_TAR_Sector: groups sectors by their ID and selects the SectorId where the IsBuffer flag is 0 or 1.
	* TAMS_TAR_Station: groups stations by their StationCode and selects the StationCode where the TARId matches @TARID and the station is active.
4. It then calculates the IsGap value based on the selected sectors, which indicates whether a sector is not gap (IsBuffer = 0) or gap (IsBuffer = 1).
5. The procedure then performs several SELECT operations on other related tables:
	* TAMS_TAR_AccessReq: selects access requirements for the TARId where the IsSelected flag is 1 and the OperationRequirement matches a specific ID.
	* TAMS_Possession: selects possession details for the TARId, including summary, work description, type of work, and more.
	* TAMS_Possession_Limit: selects limit details for the PossessionId, including type of protection limit and red flashing lamps location.
	* TAMS_Possession_WorkingLimit: selects working limit details for the PossessionId, including ID and red flashing lamps location.
	* TAMS_Possession_OtherProtection: selects other protection details for the PossessionId, including ID and other protection information.
	* TAMS_Possession_PowerSector: selects power sector details for the PossessionId, including ID, power on/off status, number of SCDs, and breaker out.
6. It then calculates the maximum workflow level, pending workflow count, and approved workflow count based on the TARId.
7. The procedure then performs several SELECT operations on workflows:
	* TAMS_TAR_Workflow: selects workflows for the TARId where the WFStatus is 'Approved' or 'Pending'.
8. Finally, it creates two temporary tables (#TmpExc and #TmpExcSector) to store excluded data and truncates them before selecting all sectors from the TAMS_Sector table that do not match any excluded data.

### Data Interactions
* Reads: 
	+ TAMS_TAR
	+ TAMS_TAR_Sector
	+ TAMS_TAR_Station
	+ TAMS_Access_Requirement
	+ TAMS_Possession
	+ TAMS_Possession_Limit
	+ TAMS_Possession_WorkingLimit
	+ TAMS_Possession_OtherProtection
	+ TAMS_Possession_PowerSector
	+ TAMS_TAR_Workflow
* Writes: None

---


<a id='database-reference-sql-sp-tams-tb-gen-report'></a>
# Procedure: sp_TAMS_TB_Gen_Report

### Purpose
This stored procedure generates a report for TAMS TB data based on specified parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type (DTL or NEL) to filter the report. |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter the report. |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date for access data filtering. |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date for access data filtering. |
| @AccessType | NVARCHAR(20) | Specifies the access type to filter the report. |

### Logic Flow
1. The procedure checks if the specified line type (@Line) is 'DTL'. If true, it proceeds with the DTL logic.
2. For DTL logic:
	* It selects data from TAMS_TAR table where the access date falls within the specified range (@AccessDateFrom and @AccessDateTo).
	* It filters by TARStatusId based on the line type (@Line) and track type (@TrackType).
	* It also filters by access type (@AccessType) or an empty string if no value is provided.
	* The selected data is ordered by access date and TARNo.
3. If the specified line type (@Line) is not 'DTL', it proceeds with the NEL logic.
4. For NEL logic:
	* It selects data from TAMS_TAR table where the access date falls within the specified range (@AccessDateFrom and @AccessDateTo).
	* It filters by TARStatusId based on the line type (@Line) and track type (@TrackType).
	* It also filters by access type (@AccessType) or an empty string if no value is provided.
	* The selected data is ordered by access date and TARNo.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** No writes are performed in this procedure.

---


<a id='database-reference-sql-sp-tams-tb-gen-report-20230904'></a>
# Procedure: sp_TAMS_TB_Gen_Report_20230904

### Purpose
This stored procedure generates a report for TAMS TB data, filtering by access date range and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @TrackType | NVARCHAR(50) | The track type to filter by. |
| @AccessDateFrom | NVARCHAR(20) | The start date of the access date range. |
| @AccessDateTo | NVARCHAR(20) | The end date of the access date range. |
| @AccessType | NVARCHAR(20) | The access type to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table.
2. It filters the data based on the provided access date range, track type, and access type.
3. If no access type is specified, it defaults to an empty string.
4. The procedure then joins with two other tables: dbo.TAMS_Get_Station and dbo.TAMS_Get_ES.
5. It orders the results by the access date in ascending order.

### Data Interactions
* **Reads:** TAMS_TAR table, dbo.TAMS_Get_Station table, dbo.TAMS_Get_ES table

---


<a id='database-reference-sql-sp-tams-tb-gen-report-20230911'></a>
# Procedure: sp_TAMS_TB_Gen_Report_20230911

This procedure generates a report for TAMS TB data, filtering by access date range and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @TrackType | NVARCHAR(50) | The track type to filter by. |
| @AccessDateFrom | NVARCHAR(20) | The start date of the access date range. |
| @AccessDateTo | NVARCHAR(20) | The end date of the access date range. |
| @AccessType | NVARCHAR(20) | The access type to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table.
2. It filters the data based on the provided access date range, track type, and access type.
3. If no access type is specified, it defaults to an empty string.
4. The procedure then joins with two other tables: dbo.TAMS_Get_Station and dbo.TAMS_Get_ES_NoBufferZone.
5. Finally, the procedure orders the results by access date and TAR number.

### Data Interactions
* **Reads:** TAMS_TAR, dbo.TAMS_Get_Station, dbo.TAMS_Get_ES_NoBufferZone

---


<a id='database-reference-sql-sp-tams-tb-gen-report-20230915'></a>
# Procedure: sp_TAMS_TB_Gen_Report_20230915

### Purpose
This stored procedure generates a report for TAMS TB data, filtering by access date range and other specified criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type to filter by (e.g., 'NEL') |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date of the access date range |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date of the access date range |
| @AccessType | NVARCHAR(20) | Specifies the access type to filter by |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table based on the specified parameters.
2. It filters the data by access date range, using the provided start and end dates.
3. It also applies additional filters based on the line type, track type, and access type specified in the parameters.
4. The procedure then joins with other tables (TAMS_Get_Station and TAMS_Get_ES_NoBufferZone) to retrieve additional data for each record.
5. Finally, it orders the results by access date and TAR ID.

### Data Interactions
* **Reads:** TAMS_TAR table, TAMS_Get_Station table, TAMS_Get_ES_NoBufferZone table

---


<a id='database-reference-sql-sp-tams-tb-gen-report-20231009'></a>
# Procedure: sp_TAMS_TB_Gen_Report_20231009

This procedure generates a report for TAMS TB data based on specified parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type (e.g., NEL, TAMS_TAR). |
| @TrackType | NVARCHAR(50) | Specifies the track type. |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date for access. |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date for access. |
| @AccessType | NVARCHAR(20) | Specifies the access type (e.g., ''). |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table based on the specified parameters.
2. It filters the data to include only records where the AccessDate falls within the specified range (@AccessDateFrom and @AccessDateTo).
3. For NEL lines, it includes records with a TARStatusId of 9; otherwise, it includes records with a TARStatusId of 8.
4. It also filters by access type (if specified) or allows empty strings for this parameter.
5. The procedure then joins the selected data with two additional tables: TAMS_Get_Station and TAMS_Get_ES_NoBufferZone to retrieve related information.
6. Finally, it orders the results by AccessDate and TARNo.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_Get_Station, TAMS_Get_ES_NoBufferZone

---


<a id='database-reference-sql-sp-tams-tb-gen-report-20230904-m'></a>
# Procedure: sp_TAMS_TB_Gen_Report_20230904_M

### Purpose
This stored procedure generates a report for TAMS TB data, filtering by access date range and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line number to filter by. |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by. |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date of the access date range. |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date of the access date range. |
| @AccessType | NVARCHAR(20) | Specifies the access type to filter by. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table.
2. It filters the data based on the specified line number, track type, and access date range.
3. The data is then joined with two other tables: dbo.TAMS_Get_Station and dbo.TAMS_Get_ES_NoBufferZone to retrieve additional information.
4. The procedure orders the results by access date.

### Data Interactions
* **Reads:** TAMS_TAR, dbo.TAMS_Get_Station, dbo.TAMS_Get_ES_NoBufferZone

---


<a id='database-reference-sql-sp-tams-tb-gen-report-20230911-m'></a>
# Procedure: sp_TAMS_TB_Gen_Report_20230911_M

### Purpose
This stored procedure generates a report for TAMS TB data, filtering by access date range and other criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line to filter by (e.g., NEL). |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by. |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date of the access date range. |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date of the access date range. |
| @AccessType | NVARCHAR(20) | Specifies the access type to filter by (optional). |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TAR table.
2. It filters the data based on the specified line, track type, and access date range.
3. If a specific line is specified, it further filters by TAR status ID 9 for NEL lines or 8 for other lines.
4. The procedure also filters by access type if provided.
5. Finally, it orders the results by access date.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** No data is written to any tables; only read operations are performed.

---


<a id='database-reference-sql-sp-tams-tb-gen-report-20230915-m'></a>
# Procedure: sp_TAMS_TB_Gen_Report_20230915_M

### Purpose
This stored procedure generates a report for TAMS TB data, filtering by access date range and line type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type to filter by (DTL or NEL). |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by. |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date of the access date range. |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date of the access date range. |
| @AccessType | NVARCHAR(20) | Specifies the access type to filter by (optional). |

### Logic Flow
1. The procedure checks if the `@Line` parameter is 'DTL'. If true, it proceeds with the DTL logic.
2. For DTL logic:
	* It selects data from the `TAMS_TAR` table where the access date falls within the specified range and matches the line type (`@Line`) and track type (`@TrackType`).
	* The selected columns include TAR ID, Company/Dept, Access Type, Name, Access Stations, TAR Date, Electrical Section, Nature of Work, and Remarks.
3. If the `@Line` parameter is not 'DTL', it proceeds with the NEL logic.
4. For NEL logic:
	* It selects data from the `TAMS_TAR` table where the access date falls within the specified range and matches the line type (`@Line`) and track type (`@TrackType`).
	* The selected columns include TAR ID, Company/Dept, Access Type, Name, Access Stations, TAR Date, Track Sector, Nature of Work, and Remarks.
5. In both cases, the data is ordered by TAR date and TAR ID.

### Data Interactions
* **Reads:** TAMS_TAR table
* **Writes:** No writes are performed in this procedure.

---


<a id='database-reference-sql-sp-tams-tb-gen-summary'></a>
# Procedure: sp_TAMS_TB_Gen_Summary

### Purpose
This stored procedure generates a summary of TAMS data based on input parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type to filter by (DTL or NEL) |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter by |
| @AccessDateFrom | NVARCHAR(20) | Specifies the start date for access data filtering |
| @AccessDateTo | NVARCHAR(20) | Specifies the end date for access data filtering |
| @AccessType | NVARCHAR(20) | Specifies the access type to filter by |

### Logic Flow
The procedure first checks if the `@Line` parameter is 'DTL'. If it is, it generates three separate result sets based on different conditions. The conditions are:
- Power Off With Rack Out / 22KV Isolation
- Use of Tunnel Ventilation
- Electrical Section (Electrical Section and Nature of Work)

If the `@Line` parameter is not 'DTL', the procedure checks if it is 'NEL'. If it is, it generates five separate result sets based on different conditions. The conditions are:
- Power Off With Rack Out / 22KV Isolation
- Use of Tunnel Ventilation
- Electrical Section (Electrical Section and Nature of Work)
- NEL ISCS and Systems
- NEL Communications

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Get_ES_NoBufferZone, TAMS_Get_Station, TAMS_Get_ES_NoBufferZone (for NEL), TAMS_Get_TVF_Station

---


<a id='database-reference-sql-sp-tams-tb-gen-summary20250120'></a>
# Procedure: sp_TAMS_TB_Gen_Summary20250120

### Purpose
This stored procedure generates a summary of TAMS data for a specific date range, including access dates, TAR IDs, electrical sections, nature of work, and remarks.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type (DTL or NEL) to be processed. |

### Logic Flow

1. The procedure checks if the specified line type is 'DTL'. If true, it processes data for 'DTL' lines.
2. For 'DTL' lines, it selects data from multiple tables based on various conditions and filters, including access dates, TAR IDs, electrical sections, nature of work, and remarks.
3. The procedure also checks if the specified line type is 'NEL'. If true, it processes data for 'NEL' lines.
4. For 'NEL' lines, it selects data from multiple tables based on various conditions and filters, including access dates, TAR IDs, electrical sections, nature of work, and remarks.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Get_ES_NoBufferZone, TAMS_Get_Station_Dir, TAMS_Get_ES_NoBufferZone, TAMS_Get_TVF_Station, and TAMS_Parameters.
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-tb-gen-summary-20230904'></a>
# Procedure: sp_TAMS_TB_Gen_Summary_20230904

### Purpose
This stored procedure generates a summary of TAMS TB data for a specific date range, including access dates, TAR IDs, electrical sections, nature of work, and remarks.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line type (DTL or NEL) to generate summary for. |

### Logic Flow

1. The procedure checks if the specified line type is 'DTL'. If true, it generates a summary of DTL data.
2. For DTL data, it selects records from TAMS_TAR, TAMS_TAR_AccessReq, and TAMS_Access_Requirement tables based on specific conditions (e.g., access date range, TAR status ID, access type).
3. The procedure then orders the results by access date and TAR number.
4. If the specified line type is 'NEL', it generates a summary of NEL data.
5. For NEL data, it selects records from TAMS_TAR, TAMS_TAR_AccessReq, and TAMS_Access_Requirement tables based on specific conditions (e.g., access date range, TAR status ID, access type).
6. The procedure then orders the results by access date.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Get_ES, TAMS_Get_Station_Dir, TAMS_Get_ES, TAMS_Get_TVF_Station, and TAMS_Get_Station tables.
* **Writes:** No writes are performed by this stored procedure.

---


<a id='database-reference-sql-sp-tams-tb-gen-summary-20230904-m'></a>
# Procedure: sp_TAMS_TB_Gen_Summary_20230904_M

### Purpose
This stored procedure generates a summary of TAMS data for a specific date range, filtered by line and track type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | Specifies the line to filter on (DTL or NEL) |
| @TrackType | NVARCHAR(50) | Specifies the track type to filter on |
| @AccessDateFrom | NVARCHAR(20) | Start date for access data filtering |
| @AccessDateTo | NVARCHAR(20) | End date for access data filtering |
| @AccessType | NVARCHAR(20) | Access type to filter on |

### Logic Flow
The procedure first checks if the line is 'DTL'. If it is, it generates three sets of results based on different conditions:
- Condition 1: Power Off With Rack Out / 22KV Isolation
- Condition 2: Use of Tunnel Ventilation
- Condition 3: Other operations (including electrical section and nature of work)

If the line is not 'DTL', the procedure checks if it is 'NEL'. If it is, it generates five sets of results based on different conditions:
- Condition 1: Power Off With Rack Out / 22KV Isolation
- Condition 2: Use of Tunnel Ventilation
- Condition 3: Electrical section and nature of work
- Condition 4: NEL ISCS and Systems
- Condition 5: NEL Communications

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TAR_AccessReq, TAMS_Access_Requirement, TAMS_Get_ES_NoBufferZone, TAMS_Get_Station, TAMS_Get_ES_NoBufferZone (for NEL), TAMS_Get_TVF_Station, TAMS_Get_Station_Dir
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-toa-add-parties1'></a>
# Procedure: sp_TAMS_TOA_Add_Parties1

### Purpose
This stored procedure adds new parties to a TAMS TOA record, updating the number of parties associated with it if a party with the same NRIC already exists.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesFIN	| NVARCHAR(50) | The FIN (Financial Identification Number) of the party to be added. |
| @PartiesName	| NVARCHAR(200) | The name of the party to be added. |
| @IsTMC	| NVARCHAR(5) | A flag indicating whether the party is in charge or not. |
| @NoOfParties	| BIGINT | The number of parties associated with the TAMS TOA record. |
| @TOAID	| BIGINT | The ID of the TAMS TOA record to be updated. |
| @Message	| NVARCHAR(500) | An output parameter containing a message indicating the result of the procedure. |

### Logic Flow
1. The procedure checks if a transaction has already been started and sets an internal flag accordingly.
2. It then checks if a party with the same NRIC (as encrypted) already exists in the TAMS_TOA_Parties table for the specified TOAID.
3. If a party is found, it updates the number of parties associated with the TAMS TOA record to 1 and sets an error message indicating that a duplicate party was found.
4. If no party is found, it inserts a new party into the TAMS_TOA_Parties table for the specified TOAID, updating the number of parties associated with the TAMS TOA record accordingly.
5. The procedure then checks if any errors occurred during the insertion process and sets an error message if necessary.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Parties

---


<a id='database-reference-sql-sp-tams-toa-add-parties'></a>
# Procedure: sp_TAMS_TOA_Add_Parties

### Purpose
This stored procedure adds new parties to a TAMS TOA record, updating the number of parties if they already exist.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesFIN	| NVARCHAR(50) | The NRIC of the party being added |
| @PartiesName	| NVARCHAR(200) | The name of the party being added |
| @IsTMC	| NVARCHAR(5) | Whether the party is in charge (Y/N) |
| @NoOfParties	| BIGINT | The new number of parties |
| @TOAID	| BIGINT | The ID of the TAMS TOA record being updated |
| @Message	| NVARCHAR(500) | An output parameter containing a message about the result |

### Logic Flow
1. Check if a transaction has already started; if not, start one.
2. Determine if the party is in charge based on the value of @IsTMC.
3. Count the number of existing parties with the same NRIC as the new party being added.
4. If a party with the same NRIC exists, set @Message to '1' (indicating an update).
5. Otherwise, update the TAMS TOA record with the new number of parties and insert a new party into the TAMS_TOA_Parties table.
6. Check for any errors during insertion; if found, roll back the transaction and set @Message to an error message.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TOA_Parties
* **Writes:** TAMS_TOA, TAMS_TOA_Parties

---


<a id='database-reference-sql-sp-tams-toa-add-pointno'></a>
# Procedure: sp_TAMS_TOA_Add_PointNo

### Purpose
This stored procedure adds a new point number to the TAMS_TOA table, including the TOAID and creation date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @pointno | nvarchar(200) | The point number to be added. |
| @toaid | int | The ID of the TOA associated with the point number. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that stores any error message generated during the procedure execution. |
| @CreatedBy | nvarchar(50) | The user who created the new point number. |

### Logic Flow
1. The procedure starts by declaring a variable to track internal transactions.
2. It checks if there are any active transactions and sets the internal transaction flag accordingly.
3. If no transactions are active, it begins a new transaction.
4. It initializes an error message variable to empty.
5. Inside the transaction block:
   * It inserts a new record into the TAMS_TOA_PointNo table with the provided TOAID, point number, creation date, and creator's name.
   * If any errors occur during this insertion, it sets the error message and jumps to the TRAP_ERROR label.
6. After successful insertion or if an error occurs:
   * It checks the internal transaction flag. If it is 1 (indicating a new transaction), it commits the transaction and returns the error message.
   * If the internal transaction flag is not 1, it rolls back the transaction and returns the error message.

### Data Interactions
* **Reads:** None explicitly listed; however, the procedure uses system tables like @@TRANCOUNT to track transactions.
* **Writes:** 
    + TAMS_TOA_PointNo table: inserted records.

---


<a id='database-reference-sql-sp-tams-toa-add-protectiontype'></a>
# Procedure: sp_TAMS_TOA_Add_ProtectionType

### Purpose
This stored procedure adds a new protection type to the TAMS_TOA table and updates related data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @pointno | dbo.Point | The point number to be associated with the new protection type. |
| @protectiontype | char(5) | The new protection type to be added. |
| @toaid | int | The ID of the TAMS_TOA record to which the new protection type is being added. |
| @Message | NVARCHAR(500) | An output parameter that contains a message indicating whether the operation was successful or not. |
| @CreatedBy | nvarchar(50) | The user who created the new protection type. |

### Logic Flow
1. The procedure starts by checking if there are any open transactions. If not, it sets an internal transaction flag to 1.
2. It then updates the TAMS_TOA record with the specified ID and new protection type.
3. Next, it deletes all existing point numbers associated with the same TAMS_TOA record.
4. After that, it inserts a new point number into the TAMS_TOA_PointNo table, linking it to the updated TAMS_TOA record.
5. The procedure then checks if any errors occurred during this process. If so, it sets an error message and skips the rest of the procedure.
6. Finally, if no errors occurred, the procedure commits the internal transaction (if one was started) and returns a success message.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TOA_PointNo tables
* **Writes:** TAMS_TOA, TAMS_TOA_PointNo tables

---


<a id='database-reference-sql-sp-tams-toa-bookout-parties'></a>
# Procedure: sp_TAMS_TOA_BookOut_Parties

### Purpose
This stored procedure performs a book out operation for a specified party, updating its status and recording the current date and time.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesID | BIGINT | The ID of the party to be booked out. |
| @TOAID | BIGINT | The ID of the TOA (Treatment Order Assignment) associated with the party. |
| @Message | NVARCHAR(500) | An output parameter that stores any error messages generated during the procedure execution. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag to 0.
2. If no transactions are currently active, it sets the flag to 1 and begins a new transaction.
3. It initializes an error message variable to empty.
4. The procedure updates the BookOutTime and BookInStatus columns in the TAMS_TOA_Parties table for the specified party (identified by @PartiesID) and TOA ID (@TOAID).
5. If any errors occur during this update, it sets the error message variable and jumps to the TRAP_ERROR label.
6. After successful updates, if an internal transaction was started, it commits the transaction and returns the error message.
7. If an error occurred, it rolls back the internal transaction and returns the error message.

### Data Interactions
* **Reads:** TAMS_TOA_Parties table
* **Writes:** TAMS_TOA_Parties table

---


<a id='database-reference-sql-sp-tams-toa-delete-parties'></a>
# Procedure: sp_TAMS_TOA_Delete_Parties

### Purpose
This stored procedure deletes parties from the TAMS_TOA_Parties table and updates the corresponding TOA record in the TAMS_TOA table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PartiesID | BIGINT | The ID of the party to be deleted. |
| @TOAID | BIGINT | The ID of the TOA associated with the parties. |
| @Message | NVARCHAR(500) | An output parameter that stores any error message. |

### Logic Flow
1. The procedure starts by checking if a transaction has already been started. If not, it sets a flag to indicate that a transaction is about to be started.
2. It then checks the number of parties associated with the specified TOA ID. If there are less than 2 parties, an error message is raised.
3. If there are 2 or more parties, the procedure deletes the specified party from the TAMS_TOA_Parties table and updates the corresponding TOA record in the TAMS_TOA table by setting the NoOfParties field to the count of remaining parties.
4. The procedure then checks for any errors that occurred during the execution of the stored procedure. If an error occurs, it sets the @Message parameter with an error message and exits the procedure.
5. If no errors occur, the procedure commits the transaction and returns the value of the @Message parameter.

### Data Interactions
* **Reads:** TAMS_TOA_Parties table
* **Writes:** TAMS_TOA_Parties table, TAMS_TOA table

---


<a id='database-reference-sql-sp-tams-toa-delete-pointno'></a>
# Procedure: sp_TAMS_TOA_Delete_PointNo

### Purpose
This stored procedure deletes a point from the TAMS_TOA_PointNo table based on the provided TOAID and point ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @pointid | BIGINT | The ID of the point to be deleted. |
| @TOAID | BIGINT | The ID of the TOA associated with the point to be deleted. |
| @Message | NVARCHAR(500) | An output parameter that stores any error message generated during the procedure execution. |

### Logic Flow
1. Initialize a variable `@IntrnlTrans` to 0, which tracks whether a transaction is in progress.
2. Check if a transaction is already active. If not, set `@IntrnalTrans` to 1 and begin a new transaction.
3. Attempt to delete the point from the TAMS_TOA_PointNo table where TOAID matches @TOAID and Id matches @pointid.
4. If an error occurs during deletion, print 'ERROR INSERTING' to the error log, set `@Message` to an error message, and exit the procedure with a trap error.
5. If no errors occur, commit the transaction if one was started.
6. Return the value of `@Message`, which contains any error messages generated.

### Data Interactions
* **Reads:** TAMS_TOA_PointNo table
* **Writes:** TAMS_TOA_PointNo table

---


<a id='database-reference-sql-sp-tams-toa-genurl'></a>
# Procedure: sp_TAMS_TOA_GenURL

### Purpose
This stored procedure generates a URL for each station or depot in the TAMS_Station table, based on whether it is a station or a depot.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | Not applicable |

### Logic Flow
The procedure starts by selecting data from the TAMS_Station table. It then applies a conditional logic to determine whether each station is marked as a station or a depot, and assigns 'Station' or 'Depot' accordingly. The selected data is then returned.

### Data Interactions
* **Reads:** TAMS_Station

---


<a id='database-reference-sql-sp-tams-toa-genurl-qrcode'></a>
# Procedure: sp_TAMS_TOA_GenURL_QRCode

This stored procedure generates a URL and QR code for each record in the TAMS_TOA_URL table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ID | int | Unique identifier of the record to generate URL and QR code for |

### Logic Flow
1. The procedure starts by selecting specific columns from the TAMS_TOA_URL table.
2. It retrieves the ID, PLine, PLoc, PType, EncPLine, EncPLoc, EncPType, and GenURL for each record.
3. The selected data is then returned as output.

### Data Interactions
* **Reads:** [dbo].[TAMS_TOA_URL]
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-toa-get-parties'></a>
# Procedure: sp_TAMS_TOA_Get_Parties

The procedure retrieves party information for a specific TOA (TAMs Toa) ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TOAID | BIGINT | The ID of the TOA for which to retrieve parties |

### Logic Flow
1. The procedure first selects the number of parties associated with the specified TOA ID from the TAMS_TOA table.
2. It then retrieves a list of all parties, including their name, NRIC (National Registration Identity Card), whether they are a TMC (TAMs Toa Management Committee) member, and their in-charge status, ordered by party ID.
3. The procedure also generates two additional lists: one for witness parties and another for selected witnesses.
4. Finally, it counts the number of parties that have been booked in and the total count of such bookings.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TOA_Parties

---


<a id='database-reference-sql-sp-tams-toa-get-pointno'></a>
# Procedure: sp_TAMS_TOA_Get_PointNo

This procedure retrieves the point number associated with a given TOA (TAMs Toa) ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TOAID | BIGINT | The ID of the TAMS Toa to retrieve the point number for. |

### Logic Flow
1. The procedure first selects the ProtectionType from the TAMS_TOA table where the Id matches the provided TOAID.
2. It then selects the Sno (point number) and PointNo columns from the TAMS_TOA_PointNo table, filtering by the same TOAID as before, and orders the results in ascending order by Sno.

### Data Interactions
* Reads: TAMS_TOA, TAMS_TOA_PointNo tables

---


<a id='database-reference-sql-sp-tams-toa-get-station-name'></a>
# Procedure: sp_TAMS_TOA_Get_Station_Name

### Purpose
This stored procedure retrieves the station code from the TAMS_Station table based on a given line and station name.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(10) | The line number to filter by. |
| @StationName | NVARCHAR(20) | The station name to filter by. |

### Logic Flow
1. The procedure starts by selecting the StationCode column from the TAMS_Station table.
2. It filters the results based on two conditions: Line and StationName, which are passed as input parameters (@Line and @StationName).
3. If a match is found, the corresponding station code is returned.

### Data Interactions
* **Reads:** TAMS_Station

---


<a id='database-reference-sql-sp-tams-toa-login'></a>
# Procedure: sp_TAMS_TOA_Login

### Purpose
This stored procedure performs a login operation for TAMS TOA, handling internal transactions and error messages.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARNo	| NVARCHAR(50) | TAR number |
| @TPOPCNRIC	| NVARCHAR(50) | POPCNRIC number |
| @Message	| NVARCHAR(500) | Error message |

### Logic Flow
1. The procedure starts by setting an internal transaction flag to 0.
2. It checks if the current transaction count is 0, and if so, sets the internal transaction flag to 1 and begins a new transaction.
3. It then selects data from the TAMS_Parameters table.
4. If any errors occur during this process, it sets an error message and jumps to the TRAP_ERROR label.
5. Otherwise, it commits the transaction and returns the error message if the internal transaction flag is 1.
6. If an error occurs, it rolls back the transaction and returns the error message.

### Data Interactions
* **Reads:** TAMS_Parameters table

---


<a id='database-reference-sql-sp-tams-toa-onload'></a>
# Procedure: sp_TAMS_TOA_OnLoad

### Purpose
This stored procedure retrieves and decrypts data from the TAMS_TOA table based on a provided TOAID, returning various fields such as InchargeNRIC, InchargeName, MobileNo, and more.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TOAID | BIGINT | The ID of the TAMS_TOA record to retrieve data for. |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_TOA table where the Id matches the provided TOAID.
2. It then joins this data with the TAMS_TAR table based on the TARId field, which is assumed to be linked to the Id in TAMS_TOA.
3. The selected data is then decrypted using a decryption function (QTS_MaskText) applied to the InChargeNRIC field.
4. The procedure returns various fields from the decrypted data.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TAR

---


<a id='database-reference-sql-sp-tams-toa-qts-chk'></a>
# Procedure: sp_TAMS_TOA_QTS_Chk

### Purpose
This stored procedure checks if a person has a valid qualification for a specific line of service, based on their access date and status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric		NVARCHAR(50) | The National Registration Identity Card number. |
| @qualdate	NVARCHAR(20) | The qualification date to check against. |
| @line	NVARCHAR(20) | The line of service for which the qualification is being checked. |
| @QualCode	NVARCHAR(20) | The qualification code to match with the person's qualifications. |

### Logic Flow
1. The procedure starts by declaring variables and setting up temporary tables.
2. It then selects the relevant data from the QTS_Personnel, QTS_Personnel_Qualification, and QTS_Qualification tables based on the input parameters.
3. If no matching records are found, the procedure sets a status of 'InValid'.
4. If matching records are found, it checks if the qualification date is within the valid access period.
5. Based on this check, the procedure sets a status of either 'Valid' or 'InValid'.
6. Finally, it returns the person's name, line of service, qualification date, qualification code, and status.

### Data Interactions
* **Reads:** QTS_Personnel, QTS_Personnel_Qualification, QTS_Qualification tables.
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-toa-qts-chk-20230323'></a>
# Procedure: sp_TAMS_TOA_QTS_Chk_20230323

### Purpose
This stored procedure checks if a TAMS TOA (Training on Assignment) record is valid for a given line of rail and access type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | The National Registration Identification Number. |
| @qualdate | NVARCHAR(20) | The qualification date. |
| @line | NVARCHAR(20) | The line of rail. |
| @AccessType | NVARCHAR(20) | The access type. |

### Logic Flow
1. The procedure starts by declaring variables to store the message, EPC counter, BLC counter, RTC counter, and return value.
2. It then creates two temporary tables, #tmpqtsqc and #tmpnric, to store the qualification data and TAMS TOA records respectively.
3. The procedure truncates these tables before processing new data.
4. It selects the qualification code from the TAMS Parameters table based on the line of rail and access type.
5. For each TAMS TOA record in the #tmpnric table, it checks if there is a matching qualification record in the QTS_Personnel_Qualification and QTS_Personnel tables.
6. If no matching record is found, it updates the TAMS TOA record with an invalid status.
7. If a matching record is found, it checks if there is any suspension information for the qualification record.
8. If there is no suspension information, it updates the TAMS TOA record with a valid status.
9. The procedure then closes the cursor and deallocates resources.

### Data Interactions
* **Reads:** 
	+ TAMS_Parameters table
	+ QTS_Personnel_Qualification table
	+ QTS_Personnel table
	+ #tmpqtsqc table
	+ #tmpnric table
* **Writes:** 
	+ #tmpqtsqc table
	+ #tmpnric table

---


<a id='database-reference-sql-sp-tams-toa-qts-chk-20230907'></a>
# Procedure: sp_TAMS_TOA_QTS_Chk_20230907

### Purpose
This stored procedure checks if a TAMS TOA (Trainee On Assignment) record is valid based on the provided qualification date, line, and access type.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | The National Registration Identification Number of the trainee. |
| @qualdate | NVARCHAR(20) | The qualification date of the trainee. |
| @line | NVARCHAR(20) | The line number of the trainee's assignment. |
| @AccessType | NVARCHAR(20) | The access type of the trainee's assignment. |

### Logic Flow
The procedure follows these steps:

1. It initializes several variables to store the results and sets up temporary tables to store intermediate data.
2. It checks if a record exists in the TAMS Parameters table with the specified line number and qualification code, and updates the @QualCode variable accordingly.
3. It inserts a new record into the #tmpnric table with the provided nric, qualdate, line, and access type.
4. It creates a cursor to iterate over the records in the #tmpnric table, starting from the first record.
5. For each record, it checks if there is any suspension information available for the trainee's assignment. If not, it updates the qualstatus column to 'InValid'.
6. If suspension information is available, it checks if the qualification date falls within a valid period (between pq_validaccess_date and pq_validtill_date). If so, it updates the qualstatus column to 'Valid'; otherwise, it updates it to 'InValid'.
7. After iterating over all records, it selects the final values from the #tmpnric table and returns them.

### Data Interactions
* **Reads:** 
	+ TAMS_Parameters table
	+ QTS_Personnel_Qualification table
	+ QTS_Personnel table
* **Writes:**
	+ #tmpnric table
	+ #tmpqtsqc table

---


<a id='database-reference-sql-sp-tams-toa-qts-chk-20230323-m'></a>
# Procedure: sp_TAMS_TOA_QTS_Chk_20230323_M

### Purpose
This stored procedure checks the validity of a TAMS TOA (Training on Assignment) record based on the provided parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | The National Registration Identification Number. |
| @qualdate | NVARCHAR(20) | The qualification date. |
| @line | NVARCHAR(20) | The line number. |
| @AccessType | NVARCHAR(20) | The access type. |

### Logic Flow
1. Initialize variables to store the message, EPC counter, BLC counter, RTC counter, and return value.
2. Create temporary tables #tmpqtsqc and #tmpnric to store the qualification data and personal details, respectively.
3. Truncate the existing data in these tables.
4. Retrieve the qualification code from TAMS_Parameters based on the provided line number and date.
5. Insert a new record into #tmpnric with the provided nric, namestr, qualdate, qualcode, line, and qualstatus.
6. Create a cursor to iterate through the records in #tmpnric.
7. For each record:
   1. Check if there is any suspension information for the current record.
      - If yes, update the qualstatus to 'Valid' or 'InValid' based on the presence of suspension information.
      - If no suspension information, check if the qualification date falls within a valid period.
         - If yes, update the qualstatus to 'Valid'.
         - If not, update the qualstatus to 'InValid'.
8. Close and deallocate the cursor.
9. Select and return the updated records from #tmpnric.

### Data Interactions
* Reads: 
  + TAMS_Parameters
  + QTS_Personnel
  + QTS_Qualification
  + QTS_Personnel_Qualification
* Writes:
  + #tmpqtsqc
  + #tmpnric

---


<a id='database-reference-sql-sp-tams-toa-register'></a>
# Procedure: sp_TAMS_TOA_Register

### Purpose
This stored procedure registers a new TAR (Track and Record) entry into the TAMS system, including tracking the qualification status of the track.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the track. |
| @TrackType | NVARCHAR(50) | The type of track. |
| @Type | NVARCHAR(20) | The type of track. |
| @Loc | NVARCHAR(20) | The location of the track. |
| @TARNo | NVARCHAR(30) | The TAR number. |
| @NRIC | NVARCHAR(20) | The NRIC (National Registration Identity Card) number. |
| @TOAID | BIGINT OUTPUT | The ID of the TOA (Track and Record) entry. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the registration process. |

### Logic Flow
1. Check if a transaction has already started. If not, start one.
2. Create a temporary table to store the NRIC data for qualification checking.
3. Truncate the temporary table and prepare it for insertion.
4. Retrieve the cut-off time for the track based on the line number and track type.
5. Retrieve the QTS (Qualification Tracking System) code for the track based on the line number and track type.
6. Check if the TAR number is valid by counting the number of records in the TAMS_TAR table with the same TAR number and status ID.
7. If the TAR number is not valid, set an error message and return it.
8. Retrieve the TOA ID for the TAR number based on its ID.
9. Check if the track access date is within the allowed range (between the cut-off time and one day after the current date).
10. If the track access date is invalid, set an error message and return it.
11. Perform qualification checking using the temporary table and QTS code.
12. If the qualification status is valid, insert a new TOA entry into the TAMS_TOA table with the required data.
13. Insert a new record into the TAMS_TOA_Registration_Log table to log the registration process.

### Data Interactions
* Reads: TAMS_TAR, TAMS Parameters, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties, TAMS_TAR_Station, TAMS_Station.
* Writes: TAMS_TOA, TAMS_TOA_Registration_Log.

---


<a id='database-reference-sql-sp-tams-toa-register-20221117'></a>
# Procedure: sp_TAMS_TOA_Register_20221117

### Purpose
This stored procedure registers a new TOA (TAR Management System - Terminal Access) record, including the TAR number, location, and qualification details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line of operation (e.g., NEL or TAMS_TAR). |
| @Type | NVARCHAR(20) | The type of TOA. |
| @Loc | NVARCHAR(20) | The location of the TAR. |
| @TARNo | NVARCHAR(30) | The TAR number. |
| @NRIC | NVARCHAR(20) | The National Registration Identity Card (NRIC) number. |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA record. |
| @Message | NVARCHAR(500) OUTPUT | An error message if any errors occur during registration. |

### Logic Flow
1. Check if a transaction has already started. If not, start one.
2. Initialize variables for internal transactions and temporary tables.
3. Retrieve the cut-off time for the current line of operation from the TAMS_Parameters table.
4. Retrieve the QTS qualification code and protocol from the TAMS_Parameters table based on the line of operation and possession status.
5. Check if the TAR number exists in the TAMS_TAR table with a power-on status of 0. If not, set an error message.
6. Check if the location exists for the selected TAR number. If not, set an error message.
7. If both checks pass, proceed to register the TOA record:
	* Retrieve the TAR ID and access date from the TAMS_TAR table.
	* Check if the line of operation matches the TAR line. If not, set an error message.
	* Calculate the operation date based on the cut-off time and access date.
	* Insert a new TOA record into the TAMS_TOA table with the calculated operation date and other details.
	* Insert parties into the TAMS_TOA_Parties table for the newly created TOA record.
8. If any errors occur during registration, set an error message and return it.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_TAR, TAMS_TAR_Station, TAMS_TOA, TAMS_TOA_Parties
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-toa-register-20230107'></a>
# Procedure: sp_TAMS_TOA_Register_20230107

### Purpose
This stored procedure registers a new TAR (Traction Alignment Record) and updates the corresponding TOA (Track and Maintenance System - Operations Area) record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the TAR. Can be either 'NEL' or 'TAMS_TAR'. |
| @Type | NVARCHAR(20) | The type of the TAR. |
| @Loc | NVARCHAR(20) | The location of the TAR. Must match a station in TAMS_Station table. |
| @TARNo | NVARCHAR(30) | The number of the TAR. |
| @NRIC | NVARCHAR(20) | The NRIC (National Registration Identity Card) number of the person registering. |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA record. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the registration process. |

### Logic Flow
1. Check if a transaction has already started. If not, start a new transaction.
2. Create a temporary table #tmpnric to store the results of the QTS qualification check.
3. Truncate the temporary table and initialize variables for the execution string and date.
4. Retrieve the cut-off time and QTS qualification code from TAMS_Parameters table based on the line number and effective dates.
5. Check if the TAR exists in TAMS_TAR table with a status of 0 (not powered on). If not, set an error message.
6. Check if the location matches a station in TAMS_Station table. If not, set an error message.
7. If both checks pass, proceed to register the TAR and update the TOA record.
8. Retrieve the TAR ID, line number, access date, and access type from TAMS_TAR table.
9. Check if the line number matches the TAR line number. If not, set an error message.
10. Register the TAR by inserting a new record into TAMS_TOA table with the retrieved values.
11. Update the TOA ID in the temporary table #tmpnric.
12. Insert a new record into TAMS_TOA_Audit table to log the registration process.
13. If the TAR has an InChargeNRIC, check if it matches the NRIC number of the person registering. If not, set an error message.
14. Update the TOA record by setting the OperationDate and TOAStatus based on the access date and status.
15. Insert a new record into TAMS_TOA_Parties table to log the registration process.
16. Commit or roll back the transaction depending on whether an error occurred.

### Data Interactions
* Reads: TAMS_Station, TAMS_TAR, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-toa-register-20230801'></a>
# Procedure: sp_TAMS_TOA_Register_20230801

### Purpose
This stored procedure performs a registration process for a TAR (TAR No) and updates various tables accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the TAR. |
| @Type | NVARCHAR(20) | The type of the TAR. |
| @Loc | NVARCHAR(20) | The location of the TAR. |
| @TARNo | NVARCHAR(30) | The TAR No to be registered. |
| @NRIC | NVARCHAR(20) | The NRIC (National Registration Identity Card Number) of the person registering. |
| @TOAID | BIGINT OUTPUT | The ID of the TOA (TAR Operation Area) being created or updated. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the outcome of the registration process. |

### Logic Flow
1. The procedure first checks if a transaction has been started. If not, it starts one.
2. It then truncates a temporary table to ensure any previous data is cleared.
3. The procedure retrieves various parameters from the TAMS_Parameters table based on the line number of the TAR and the current date.
4. It checks if the TAR No exists in the TAMS_TAR table and if it has not been activated (PowerOn = 0). If not, it sets an error message and returns.
5. The procedure then checks if the location of the TAR matches any station in the TAMS_Station table associated with the TAR. If not, it sets an error message and returns.
6. If both checks pass, the procedure creates a TOA ID for the TAR No and retrieves the TAR details from the TAMS_TAR table.
7. It then checks if the TAR access date matches the current date or is within one day of the current date. If not, it sets an error message and returns.
8. The procedure then inserts a new record into the TAMS_TOA table with the relevant details.
9. After inserting the record, it updates the TOA status in the TAMS_TOA table based on the TAR access date.
10. It also checks if there are any parties associated with the TAR and updates their status accordingly.
11. Finally, the procedure inserts a new log entry into the TAMS_TOA_Registration_Log table to track the registration process.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_TAR, TAMS_Station, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties, TAMS_TOA_Registration_Log
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-toa-register-20221117-m'></a>
# Procedure: sp_TAMS_TOA_Register_20221117_M

### Purpose
This stored procedure registers a new TOA (TAR Management System - Terminal Access) record, including the TAR number, location, and qualification details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line of the TAR (e.g., 'NEL' or 'TAMS_TAR') |
| @Type | NVARCHAR(20) | The type of qualification (e.g., 'Possession' or '') |
| @Loc | NVARCHAR(20) | The location of the TAR station |
| @TARNo | NVARCHAR(30) | The TAR number |
| @NRIC | NVARCHAR(20) | The NRIC (National Registration Identity Card) number |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA record |
| @Message | NVARCHAR(500) OUTPUT | An error message if any |

### Logic Flow
1. Check if a transaction has already started; if not, start one.
2. Initialize variables for internal transactions and temporary tables.
3. Retrieve the cut-off time for the current line from the TAMS_Parameters table.
4. Retrieve the QTS qualification code and protocol from the TAMS_Parameters table based on the current line and possession status.
5. Check if the TAR number exists in the TAMS_TAR table; if not, set an error message.
6. Check if a valid location for the selected TAR exists; if not, set an error message.
7. If both checks pass, proceed to register the TOA record:
	* Retrieve the TAR ID and access date from the TAMS_TAR table.
	* Check if the qualification details match with the existing records in the TAMS_TOA table; if not, set an error message.
	* If the qualification details are valid, insert a new TOA record into the TAMS_TOA table.
	* Insert parties into the TAMS_TOA_Parties table for the newly created TOA record.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_TAR, TAMS_TOA, TAMS_TOA_Parties
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-toa-register-20230107-m'></a>
# Procedure: sp_TAMS_TOA_Register_20230107_M

### Purpose
This stored procedure registers a new TAR (Traction Alignment Record) into the TAMS system, including booking in and updating relevant records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line of the TAR (e.g. 'NEL' or 'NOR') |
| @Type | NVARCHAR(20) | The type of the TAR (e.g. 'Possession' or '') |
| @Loc | NVARCHAR(20) | The location of the TAR (used to select the station name) |
| @TARNo | NVARCHAR(30) | The number of the TAR |
| @NRIC | NVARCHAR(20) | The National Registration Identity Card number of the person booking in |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA (Traction Alignment Record) |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the registration process |

### Logic Flow
1. Check if a transaction has already started; if not, start one.
2. Create a temporary table to store the results of the qualification check for the person booking in.
3. Retrieve the cut-off time and QTS qualification code from the TAMS parameters table based on the line of the TAR.
4. Check if the TAR number is valid (i.e. it exists in the TAMS_TAR table with a status ID of 9 or 8).
5. If the TAR number is invalid, set an error message and exit the procedure.
6. Retrieve the station name from the TAMS_Station table based on the location of the TAR.
7. Check if the TAR number is valid (i.e. it exists in the TAMS_TAR table with a status ID of 9 or 8) and the station name matches; if not, set an error message and exit the procedure.
8. If the TAR number and station name are valid, proceed to book in the TAR.
9. Retrieve the TAR ID, line, access date, and access type from the TAMS_TAR table based on the TAR number.
10. Check if the operation date is within the allowed range; if not, set an error message and exit the procedure.
11. Perform a qualification check for the person booking in using the QTS qualification code.
12. If the qualification check fails, set an error message and exit the procedure.
13. Book in the TAR into the TAMS system, including updating relevant records such as the TOA table and parties table.
14. Return the ID of the newly created TOA and any error messages.

### Data Interactions
* Reads: TAMS_TAR, TAMS_Station, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties
* Writes: TAMS_TOA

---


<a id='database-reference-sql-sp-tams-toa-register-20230801-m'></a>
# Procedure: sp_TAMS_TOA_Register_20230801_M

### Purpose
This stored procedure registers a new TAR (Traction and Maintenance System) record, including the line, station, TAR number, and other relevant details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line of the TAR. |
| @Type | NVARCHAR(20) | The type of the TAR. |
| @Loc | NVARCHAR(20) | The location of the station. |
| @TARNo | NVARCHAR(30) | The number of the TAR. |
| @NRIC | NVARCHAR(20) | The National Registration Identity Card number. |
| @TOAID | BIGINT OUTPUT | The ID of the newly created TOA (Traction and Maintenance System) record. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the registration process. |

### Logic Flow
1. The procedure checks if a transaction has already started. If not, it starts one.
2. It truncates a temporary table to ensure any previous data is cleared.
3. The procedure retrieves various parameters from the TAMS_Parameters table based on the input line and TAR number.
4. It checks if the station exists for the given TAR number. If not, it sets an error message and returns.
5. If the station exists, it checks if the TAR number is valid. If not, it sets an error message and returns.
6. The procedure then checks if the line matches the TAR line. If not, it sets an error message and returns.
7. It retrieves the TOA ID from the TAMS_TOA table based on the TAR ID. If no TOA ID is found, it creates a new one.
8. The procedure then checks the qualification status of the person associated with the NRIC number. If the qualification is invalid, it sets an error message and returns.
9. If the qualification is valid, it inserts a new record into the TAMS_TOA table with the relevant details.
10. It also updates the TOA parties table with the newly created TOA ID and other relevant details.
11. Finally, it logs the registration process in the TAMS_TOA_Registration_Log table.

### Data Interactions
* Reads: TAMS_Parameters, TAMS_TAR, TAMS_TAR_Station, TAMS_Station, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties, TAMS_TOA_Registration_Log
* Writes: #tmpnric (temporary table), TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties

---


<a id='database-reference-sql-sp-tams-toa-register-bak20230801'></a>
# Procedure: sp_TAMS_TOA_Register_bak20230801

### Purpose
This stored procedure performs a registration process for a TAR (TAR No) and updates various tables accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number of the TAR. |
| @Type | NVARCHAR(20) | The type of the TAR. |
| @Loc | NVARCHAR(20) | The location of the TAR. |
| @TARNo | NVARCHAR(30) | The TAR No to be registered. |
| @NRIC | NVARCHAR(20) | The NRIC (National Registration Identity Card Number) of the person registering. |
| @TOAID | BIGINT OUTPUT | The ID of the TOA (TAR Operation Area) being registered. |
| @Message | NVARCHAR(500) OUTPUT | A message indicating the result of the registration process. |

### Logic Flow
1. Check if a transaction has already started. If not, start a new transaction.
2. Create a temporary table to store the NRIC and its corresponding qualification status.
3. Truncate the temporary table.
4. Retrieve the cut-off time for the TAR No from the TAMS_Parameters table based on the line number.
5. Retrieve the QTS (Qualification Time Stamp) code and protocol code from the TAMS_Parameters table based on the line number.
6. Check if the TAR No exists in the TAMS_TAR table with a status of 0 (Power On = 0). If not, set an error message and return.
7. Check if the location of the TAR No matches any station in the TAMS_Station table. If not, set an error message and return.
8. If the TAR No exists and its location is valid, proceed with the registration process.
9. Retrieve the TAR ID, line number, access date, and access type from the TAMS_TAR table based on the TAR No.
10. Check if the line number matches the TAR line number. If not, set an error message and return.
11. If the line numbers match, proceed with the registration process.
12. Retrieve the TOA ID from the TAMS_TOA table based on the TAR ID. If no TOA ID is found, create a new one.
13. Check if the access date of the TAR No matches the current date and time. If not, set an error message and return.
14. If the access dates match, proceed with the registration process.
15. Retrieve the qualification status from the temporary table based on the NRIC. If no qualification status is found, create a new one.
16. Check if the qualification status is valid. If not, set an error message and return.
17. Insert a new record into the TAMS_TOA table with the registration details.
18. Insert a new record into the TAMS_TOA_Audit table to log the registration process.
19. Insert a new record into the TAMS_TOA_Parties table to add parties to the TOA.
20. If any errors occur during the registration process, roll back the transaction and return an error message.

### Data Interactions
* Reads: TAMS_Station, TAMS_TAR, TAMS_Parameters, TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties
* Writes: TAMS_TOA, TAMS_TOA_Audit, TAMS_TOA_Parties

---


<a id='database-reference-sql-sp-tams-toa-save-protectiontype'></a>
# Procedure: sp_TAMS_TOA_Save_ProtectionType

### Purpose
This stored procedure saves a new or updated protection type for a given TOAID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @toaid | int | The ID of the TOA to save the protection type for. |
| @protectiontype | nvarchar(50) | The new or updated protection type. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that returns a message indicating success or failure. |

### Logic Flow
1. The procedure starts by checking if there is an active transaction. If not, it sets the internal transaction flag to 1 and begins a new transaction.
2. It then checks if the protection type is 'B'. If so, it deletes all records from TAMS_TOA_PointNo where TOAID matches the provided @toaid.
3. Next, it updates the ProtectionType field in TAMS_TOA for the specified Id (@toaid) to the value of @protectiontype.
4. After updating the data, it sets the @Message output parameter to an empty string.
5. If any errors occur during this process (i.e., @@ERROR is not 0), it sets @Message to 'ERROR SELECTING PROTECTION TYPE' and jumps to the TRAP_ERROR label.
6. If no errors occurred, it commits the transaction if there was one and returns the value of @Message.
7. If an error did occur, it rolls back the transaction and also returns the value of @Message.

### Data Interactions
* **Reads:** TAMS_TOA_PointNo, TAMS_TOA
* **Writes:** TAMS_TOA_PointNo, TAMS_TOA

---


<a id='database-reference-sql-sp-tams-toa-submit-register'></a>
# Procedure: sp_TAMS_TOA_Submit_Register

### Purpose
This stored procedure submits a new registration for a TAMS TOA (Tactical Air Mission Support Team Operations) and updates related records.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(20) | The user ID associated with the registration. |
| @PartiesWitness | BIGINT = 0 | The ID of the party witness, which is set to 0 by default. |
| @TOAID | BIGINT = 0 | The ID of the TAMS TOA being registered. |
| @Message | NVARCHAR(500) = NULL OUTPUT | An output parameter that stores any error message generated during the procedure execution. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag to 0, indicating that no transactions are currently active.
2. If there is no current transaction, it sets the internal transaction flag to 1 and begins a new transaction.
3. It then updates the TAMS TOA record with the specified ID to reflect its new status as registered, along with the current date and time of registration and update.
4. An audit record is inserted into the TAMS TOA Audit table for the same ID, capturing the current date and time of the update.
5. The procedure then updates the parties witness record in the TAMS TOA Parties table to reflect that it has been designated as a witness for the specified TAMS TOA ID and party witness ID.
6. It also updates the book-in time field in the same parties witness record, setting it to the current date and time.
7. If any errors occur during these updates, an error message is stored in the @Message output parameter and the procedure proceeds to roll back the transaction if one was active.

### Data Interactions
* **Reads:** [dbo].[TAMS_TOA], [dbo].[TAMS_TOA_Audit], [dbo].[TAMS_TOA_Parties]
* **Writes:** [dbo].[TAMS_TOA], [dbo].[TAMS_TOA_Audit], [dbo].[TAMS_TOA_Parties]

---


<a id='database-reference-sql-sp-tams-toa-surrender'></a>
# Procedure: sp_TAMS_TOA_Surrender

The purpose of this stored procedure is to update the status of a TAMS TOA record from an inactive state to a surrendered state, and also logs the audit trail for the change.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TOAID | BIGINT | The ID of the TAMS TOA record to be updated. |
| @Message | NVARCHAR(500) | An output parameter that stores an error message if any error occurs during the procedure execution. |

### Logic Flow
1. The procedure first checks if a transaction is already in progress by checking the @@TRANCOUNT system variable.
2. If no transaction is in progress, it sets @IntrnlTrans to 1 and begins a new transaction.
3. It then updates the TOAStatus column of the TAMS_TOA table from an inactive state (not equal to 6) to a surrendered state (equal to 4), and also updates the SurrenderTime and UpdatedOn columns with the current date and time.
4. Next, it inserts a new record into the TAMS_TOA_Audit table that includes the updated record's data, along with the timestamp of the update and a flag indicating the type of operation (U for Update).
5. If any error occurs during this process, it sets @Message to an error message and jumps to the TRAP_ERROR label.
6. Otherwise, if a transaction was started earlier, it commits the transaction and returns the @Message output parameter.
7. If an error occurred, it rolls back the transaction and also returns the @Message output parameter.

### Data Interactions
* Reads: TAMS_TOA table
* Writes: TAMS_TOA table (update), TAMS_TOA_Audit table (insert)

---


<a id='database-reference-sql-sp-tams-toa-update-details'></a>
# Procedure: sp_TAMS_TOA_Update_Details

### Purpose
This stored procedure updates details of a TAMS TOA record, including mobile number and tetra radio number, based on the provided ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @MobileNo | NVARCHAR(50) | Mobile number to update |
| @TetraRadioNo | NVARCHAR(50) | Tetra radio number to update |
| @UserID | NVARCHAR(20) | User ID for updating record |
| @TOAID | BIGINT | ID of the TAMS TOA record to update |
| @Message | NVARCHAR(500) | Error message output |

### Logic Flow
1. The procedure starts by setting an internal transaction flag and beginning a transaction if no existing one is found.
2. It then updates the specified fields in the TAMS_TOA table based on the provided ID, including mobile number and tetra radio number.
3. If any error occurs during this update process, it sets an error message output parameter and jumps to the TRAP_ERROR label.
4. After successful update or if an error occurred, the procedure checks the internal transaction flag. If a transaction was started, it commits the changes; otherwise, it returns the error message.
5. If an error occurred during the update process, the procedure rolls back the transaction and returns the error message.

### Data Interactions
* **Reads:** [dbo].[TAMS_TOA]
* **Writes:** [dbo].[TAMS_TOA]

---


<a id='database-reference-sql-sp-tams-toa-update-toa-url'></a>
# Procedure: sp_TAMS_TOA_Update_TOA_URL

### Purpose
This stored procedure updates a record in the TAMS_TOA_URL table with new values for the specified parameters.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @PLine	| NVARCHAR(50) | The line number to be updated. |
| @PLoc	| NVARCHAR(50) | The location to be updated. |
| @PType	| NVARCHAR(50) | The type to be updated. |
| @EncPLine	| NVARCHAR(100) | The encrypted line number. |
| @EncPLoc	| NVARCHAR(100) | The encrypted location. |
| @EncPType	| NVARCHAR(100) | The encrypted type. |
| @GenURL	| NVARCHAR(500) | The generated URL. |
| @Message	| NVARCHAR(500) = NULL OUTPUT | An output parameter to store any error messages. |

### Logic Flow
1. The procedure starts by setting an internal transaction flag to 0.
2. If the current transaction count is 0, it sets the internal transaction flag to 1 and begins a new transaction.
3. It then inserts a new record into the TAMS_TOA_URL table with the provided values for PLine, PLoc, PType, EncPLine, EncPLoc, EncPType, and GenURL.
4. If an error occurs during the insertion process, it sets the @Message output parameter to an error message and jumps to the TRAP_ERROR label.
5. If no errors occur, it commits the transaction if one was started and returns the value of the @Message output parameter.
6. If an error occurred, it rolls back the transaction and returns the value of the @Message output parameter.

### Data Interactions
* **Reads:** None explicitly selected from tables.
* **Writes:** TAMS_TOA_URL table (insertion)

---


<a id='database-reference-sql-sp-tams-update-company-details-by-id'></a>
# Procedure: sp_TAMS_Update_Company_Details_By_ID

### Purpose
This stored procedure updates company details for a specific company ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CompID | INT | The ID of the company to be updated. |

### Logic Flow
1. The procedure starts by attempting to begin a transaction.
2. It then checks if a record exists in the TAMS_Company table with the specified ID (@CompID).
3. If a record is found, it updates the corresponding record in the TAMS_Company table with the new company details.
4. After updating the record, it commits the transaction.

### Data Interactions
* **Reads:** TAMS_Company
* **Writes:** TAMS_Company

---


<a id='database-reference-sql-sp-tams-update-external-userpasswordbyuserid'></a>
# Procedure: sp_TAMS_Update_External_UserPasswordByUserID

### Purpose
This stored procedure updates the external user password for a specified user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The unique identifier of the user whose password is to be updated. |
| @Password | NVARCHAR(200) | The new password for the specified user ID. |

### Logic Flow
1. The procedure begins by attempting to start a transaction.
2. It then checks if a record exists in the TAMS_User table with the specified UserID.
3. If such a record is found, the procedure updates the Password column of that record using an encryption function (dbo.EncryptString) and sets the PasswordChangedDate to the current date and time.
4. After updating the password, the procedure commits the transaction if no errors occurred.
5. If any error occurs during this process, the procedure rolls back the transaction.

### Data Interactions
* **Reads:** TAMS_User table
* **Writes:** TAMS_User table

---


<a id='database-reference-sql-sp-tams-update-external-user-details-by-id'></a>
# Procedure: sp_TAMS_Update_External_User_Details_By_ID

### Purpose
This stored procedure updates external user details for a specified user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The unique identifier of the user to update. |

### Logic Flow
1. The procedure checks if a record exists in the TAMS_User table with the specified UserID.
2. If a record is found, it updates all relevant fields (Name, Department, OfficeNo, MobileNo, Email, SBSTContactPersonName, SBSTContactPersonDept, SBSTContactPersonOfficeNo, ValidTo, IsActive, UpdatedBy, and UpdatedOn) for that user ID.
3. The changes are committed to the database if the update is successful.

### Data Interactions
* **Reads:** TAMS_User table
* **Writes:** TAMS_User table

---


<a id='database-reference-sql-sp-tams-update-userregmodule-applicantregistercompany'></a>
# Procedure: sp_TAMS_Update_UserRegModule_ApplicantRegisterCompany

### Purpose
This stored procedure updates company details for a registered user and triggers the approval process for the applicant registration.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |

### Logic Flow
1. The procedure starts by checking if there is an existing record in TAMS_Reg_Module with a pending status for the given RegID.
2. If such a record exists, it updates the company details in TAMS_Registration and creates a new record in #TMP_RegModule.
3. It then iterates through each record in #TMP_RegModule, retrieves the next stage ID for the current record, and updates the corresponding record in TAMS_Reg_Module with the new status.
4. After updating all records, it sends an email to the registered user's email address with a link to access TAMS for approval/rejection of the registration.

### Data Interactions
* **Reads:** 
	+ TAMS_Reg_Module
	+ TAMS_Registration
	+ TAMS_User
	+ TAMS_User_Role
	+ TAMS_WFStatus
	+ TAMS_Endorser
	+ TAMS_Workflow
	+ TAMS_Action_Log
* **Writes:**
	+ #TMP_RegModule (temporary table)
	+ TAMS_Reg_Module
	+ TAMS_Registration

---


<a id='database-reference-sql-sp-tams-update-userregmodule-applicantregistercompany-20231009'></a>
# Procedure: sp_TAMS_Update_UserRegModule_ApplicantRegisterCompany_20231009

### Purpose
This stored procedure updates company details for a registered user in the TAMS system, including sending an email to external users for approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | INT | The ID of the registered user. |

### Logic Flow
1. The procedure starts by creating a temporary table #TMP_RegModule to store the modules that need to be updated.
2. It checks if there are any existing TAMS_Reg_Module records for the given RegID and updates the Company details in TAMS_Registration.
3. For each module, it retrieves the next stage ID from TAMS_Workflow and gets the corresponding endorser ID and workflow status ID.
4. It then inserts a new record into TAMS_Reg_Module with the updated values and sends an email to external users for approval using EAlertQ_EnQueue.
5. Finally, it commits or rolls back the transaction based on whether any errors occur during execution.

### Data Interactions
* **Reads:** 
	+ TAMS_Reg_Module
	+ TAMS_Registration
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_WFStatus
	+ TAMS_User
	+ TAMS_User_Role
	+ TAMS_Parameters
* **Writes:** 
	+ #TMP_RegModule (temporary table)
	+ TAMS_Reg_Module
	+ TAMS_Action_Log

---


<a id='database-reference-sql-sp-tams-update-userregmodule-sysadminapproval'></a>
# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproval

### Purpose
This stored procedure updates a user registration module for system admin approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the user registration module to be updated. |
| @UpdatedBy | INT | The ID of the user who is updating the module. |

### Logic Flow
1. The procedure starts by selecting relevant data from the TAMS_Reg_Module and TAMS_Registration tables based on the provided @RegModID.
2. It then determines the next stage in the workflow for the selected module, taking into account the module's type and the current registration status.
3. If the module is external, it sets the work flow type to 'ExtUser'. Otherwise, it sets the work flow type based on the module's type (TAR, DCC, or OCC).
4. The procedure then selects the workflow ID, new WF status ID, and endorser ID for the selected module.
5. It updates the registration module with the new values and inserts an audit log entry.
6. Finally, it sends an email to the registered users with a link to access TAMS and approve/reject the user registration.

### Data Interactions
* Reads: TAMS_Reg_Module, TAMS_Registration
* Writes: TAMS_Reg_Module (updated), TAMS_Action_Log

---


<a id='database-reference-sql-sp-tams-update-userregmodule-sysadminapproval-20231009'></a>
# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproval_20231009

### Purpose
This stored procedure is used to update a user registration module for system admin approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module to be updated. |
| @UpdatedBy | INT | The ID of the user who is updating the registration module. |

### Logic Flow
1. The procedure starts by selecting the relevant data from the TAMS_Reg_Module and TAMS_Registration tables based on the provided @RegModID.
2. It then determines the next stage in the workflow for the selected registration module, taking into account the current status and any external factors.
3. If the registration module is already approved, it updates the WFStatus to 'Approved' and sets the UpdatedOn and UpdatedBy fields accordingly.
4. The procedure then inserts a new record into the TAMS_Reg_Module table with the updated data.
5. It also generates an email notification for system admin approval, including a link to access the registration module and instructions on how to proceed.

### Data Interactions
* **Reads:** 
	+ TAMS_Reg_Module
	+ TAMS_Registration
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_WFStatus
	+ TAMS_User
	+ TAMS_User_Role
* **Writes:**
	+ TAMS_Reg_Module (new record)
	+ TAMS_Action_Log

---


<a id='database-reference-sql-sp-tams-update-userregmodule-sysadminapprovecompany'></a>
# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproveCompany

### Purpose
This stored procedure is used to update a user's registration module status from "Pending Company Approval" to "Approved" by a system administrator, and also sends an email notification to the endorser and other relevant stakeholders.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module being updated. |
| @UserID | NVARCHAR(200) | The ID of the user whose registration module status is being updated. |

### Logic Flow
1. Check if the specified registration module exists and has a pending company approval status.
2. If it does, retrieve the relevant information from the TAMS_Reg_Module table.
3. Create a temporary table to store the data for further processing.
4. Open a cursor to iterate through the data in the temporary table.
5. For each iteration, check if there is an active workflow with the same line and track type as the current registration module.
6. If an active workflow exists, retrieve the next stage ID for this TAMS_Reg_Module.
7. Update the WFStatus column in the TAMS_Reg_Module table to reflect the new status.
8. Send an email notification to the endorser and other relevant stakeholders using the EAlertQ_EnQueue stored procedure.
9. If a company registration record exists for the user, update its CompanyID field with the ID of the newly created company.
10. Insert an audit log entry into the TAMS_Action_Log table.

### Data Interactions
* Reads: 
	+ TAMS_Reg_Module
	+ TAMS_WFStatus
	+ TAMS_Endorser
	+ TAMS_Workflow
	+ TAMS_Company
	+ TAMS_Registration
	+ TAMS_User_Role
	+ TAMS_Action_Log
* Writes:
	+ TAMS_Reg_Module (updated WFStatus column)
	+ TAMS_Company (newly created company record)

---


<a id='database-reference-sql-sp-tams-update-userregmodule-sysadminapprovecompany-20231009'></a>
# Procedure: sp_TAMS_Update_UserRegModule_SysAdminApproveCompany_20231009

### Purpose
This stored procedure is used to update a user's registration module status from 'Pending Company Approval' to 'Approved' by a system administrator, and also registers the company information into TAMS_Company.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module to be updated. |
| @UserID | NVARCHAR(200) | The user ID associated with the registration module. |

### Logic Flow
1. Check if the specified registration module exists and has a status of 'Pending Company Approval'. If not, exit the procedure.
2. Retrieve the company information from TAMS_Registration based on the user's ID.
3. Create a temporary table to store the updated registration modules with the new workflow status.
4. Open a cursor to iterate through the rows in the temporary table and update the corresponding registration module with the new workflow status.
5. Insert an audit log entry for the system administrator approving the company registration.
6. Register the company information into TAMS_Company if it does not already exist.
7. Update the Company ID in TAMS_Registration based on the retrieved company information.
8. Commit the transaction.

### Data Interactions
* **Reads:** 
	+ TAMS_Reg_Module
	+ TAMS_WFStatus
	+ TAMS_Workflow
	+ TAMS_Endorser
	+ TAMS_User
	+ TAMS_Registration
	+ TAMS_Company
	+ TAMS_Action_Log
* **Writes:** 
	+ TAMS_Reg_Module
	+ TAMS_Action_Log

---


<a id='database-reference-sql-sp-tams-update-userregmodule-sysownerapproval'></a>
# Procedure: sp_TAMS_Update_UserRegModule_SysOwnerApproval

### Purpose
This stored procedure updates the registration module status to "Approved" and creates a new user account if necessary, based on the system owner's approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module being updated. |
| @UpdatedBy | INT | The ID of the user updating the registration module status. |

### Logic Flow
1. Check if the registration module is external or not.
2. If it's external, set the workflow type to 'ExtUser'.
3. If it's not external, determine the workflow type based on the module type (TAR, DCC, OCC).
4. Retrieve the next stage ID and status from TAMS_WFStatus table.
5. Find the workflow ID associated with the current line and workflow type.
6. Get the endorser ID and role ID for the current line and workflow ID.
7. Check if there are any existing registration modules with the same ID, and update their status to 'Approved' if so.
8. Create a new user account if necessary (i.e., if the registration module is not external).
9. Insert an audit log entry for the system owner's approval.
10. Send an email notification to the registered users.

### Data Interactions
* Reads: TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_Workflow, TAMS_Endorser, TAMS_User, TAMS_Action_Log
* Writes: TAMS_Reg_Module (updated status), TAMS_User (new account creation)

---


<a id='database-reference-sql-sp-tams-update-userregmodule-sysownerapproval-20230112'></a>
# Procedure: sp_TAMS_Update_UserRegModule_SysOwnerApproval_20230112

### Purpose
This stored procedure updates the registration module status to "Approved" and creates a new user account if necessary, based on the system owner's approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module to be updated. |
| @UpdatedBy | INT | The ID of the user who approved the registration module. |

### Logic Flow
1. Check if the registration module is external. If it is, set the workflow type to "ExtUser". Otherwise, determine the workflow type based on the module type.
2. Retrieve the current status and line number of the registration module from TAMS_Reg_Module and TAMS_Registration tables.
3. Find the next stage ID and status for the system owner's approval in TAMS_WFStatus table.
4. Get the workflow ID, role ID, and endorser ID associated with the registration module in TAMS_Workflow, TAMS_Endorser, and TAMS_Endorser tables respectively.
5. Check if the registration module already exists in TAMS_Reg_Module table. If it does, update its status to "Approved" and set the updated on and updated by fields.
6. Create a new user account for the registration module if necessary, based on the system owner's approval.
7. Insert an audit log entry for the system owner's approval.

### Data Interactions
* Reads: TAMS_Reg_Module, TAMS_Registration, TAMS_WFStatus, TAMS_Workflow, TAMS_Endorser, TAMS_Action_Log, TAMS_User
* Writes: TAMS_Reg_Module

---


<a id='database-reference-sql-sp-tams-update-userregmodule-sysownerapproval-20231009'></a>
# Procedure: sp_TAMS_Update_UserRegModule_SysOwnerApproval_20231009

### Purpose
This stored procedure updates a user registration module's status to "Approved" and creates or updates a corresponding user account if necessary.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module to be updated. |
| @UpdatedBy | INT | The ID of the user updating the registration module. |

### Logic Flow
1. The procedure checks if the registration module is external or not.
2. If it's external, it sets a specific workflow type; otherwise, it determines the workflow type based on the module name.
3. It retrieves the next stage title and ID from the TAMS_WFStatus table where the line matches the registration module's line.
4. It finds the workflow ID and work flow type that match the determined workflow type and the current date range.
5. If a corresponding user account exists, it updates the registration module's status to "Approved" and sets the updated on and updated by fields.
6. If no user account exists, it creates one based on the registration module's data.
7. It inserts an audit log entry for the system owner approving the registration module.
8. It sends an email notification to the registered users with a link to access TAMS.

### Data Interactions
* Reads: TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_Workflow, TAMS_Endorser, TAMS_Action_Log, TAMS_User
* Writes: TAMS_Reg_Module (updated), TAMS_User (created or updated)

---


<a id='database-reference-sql-sp-tams-update-userregrole-sysownerapproval'></a>
# Procedure: sp_TAMS_Update_UserRegRole_SysOwnerApproval

### Purpose
This stored procedure updates the user registration role system owner approval status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module. |
| @RegRoleID | INT | The ID of the registration role. |
| @IsAssigned | BIT | A flag indicating whether the user is assigned to the role. |
| @RejectRemarks | NVARCHAR(MAX) | Remarks for rejecting the assignment. |
| @UpdatedBy | INT | The ID of the user updating the approval status. |

### Logic Flow
1. The procedure starts by declaring variables and selecting data from various tables based on the input parameters.
2. It then updates the registration role table with the new approval status, updated date, reject remarks, and updated by user ID.
3. If the user is assigned to the role, it checks if the user already has an entry in the TAMS_User_Role table for the same line, role, and track type. If not, it inserts a new record into this table.

### Data Interactions
* **Reads:** TAMS_User, TAMS_Registration, TAMS_Reg_Module, TAMS_Reg_Role, TAMS_User_Role
* **Writes:** TAMS_Reg_Role

---


<a id='database-reference-sql-sp-tams-update-user-details-by-id'></a>
# Procedure: sp_TAMS_Update_User_Details_By_ID

### Purpose
This stored procedure updates user details in the TAMS_User table based on a provided user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The unique identifier of the user to be updated. |

### Logic Flow
1. The procedure begins by attempting to start a transaction.
2. It then checks if a record exists in the TAMS_User table with the specified user ID.
3. If a record is found, the procedure updates the corresponding fields (Name, Email, Department, OfficeNo, MobileNo, ValidTo, IsActive, UpdatedBy, and UpdatedOn) with the provided values.
4. After updating the record, the procedure commits the transaction if successful.
5. If any error occurs during the execution of the stored procedure, it rolls back the transaction to maintain database consistency.

### Data Interactions
* **Reads:** TAMS_User table
* **Writes:** TAMS_User table

---


<a id='database-reference-sql-sp-tams-user-checklastemailrequest'></a>
# Procedure: sp_TAMS_User_CheckLastEmailRequest

### Purpose
This stored procedure checks if a user has made an email request within a specified rate limit.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(200) | The login ID of the user to check. |
| @Mode | NVARCHAR(200) | The mode of operation, either 'User Detail View' or 'Forget Password'. |

### Logic Flow
The procedure first checks if a valid login ID is provided. If it is, it retrieves the registration details for that user and then checks the email requests made by that user within the last 60 seconds (defined by the Rate Limiting parameter). If an email request was made recently, the procedure returns -1; otherwise, it returns 1.

### Data Interactions
* **Reads:** TAMS_Registration, EAlertQTo, eAlertQ, TAMS_Parameters

---


<a id='database-reference-sql-sp-tams-user-checklastuserregistration'></a>
# Procedure: sp_TAMS_User_CheckLastUserRegistration

### Purpose
This stored procedure checks if a user has registered within the allowed time frame as defined by the 'Rate Limiting-UserReg' parameter.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(200) | The login ID of the user to check. |

### Logic Flow
1. If a valid login ID is provided, the procedure checks if there is an existing registration record for that user.
2. If a registration record exists, it retrieves the maximum date of creation from that record.
3. It then compares this date with the current date and time using the 'DATEDIFF' function to calculate the difference in seconds.
4. If the difference is less than the rate limiting value defined by the 'Rate Limiting-UserReg' parameter, the procedure returns -1 indicating that the user has registered too recently.
5. Otherwise, it returns 1.

### Data Interactions
* **Reads:** TAMS_Registration table
* **Writes:** None

---


<a id='database-reference-sql-sp-tams-usersmanual'></a>
# Procedure: sp_TAMS_UsersManual

### Purpose
This stored procedure retrieves user manual data from the TAMS_Parameters table based on a specific parameter code and date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | The parameter code to filter results |

### Logic Flow
1. The procedure starts by selecting data from the TAMS_Parameters table.
2. It filters the data based on the ParaCode column, which must match 'TOAUM'.
3. Additionally, it applies a date range filter using the EffectiveDate and ExpiryDate columns, ensuring that the data is only returned for dates within this period.
4. The filtered data is then retrieved and returned as part of the procedure's output.

### Data Interactions
* **Reads:** TAMS_Parameters table

---


<a id='database-reference-sql-sp-tams-withdrawtarbytarid'></a>
# Procedure: sp_TAMS_WithdrawTarByTarID

### Purpose
This stored procedure performs a withdrawal of a TAR (Tender And Request) by updating its status and recording the action in the TAMS_Action_Log table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TarId | integer | The ID of the TAR to be withdrawn. |
| @UID | integer | The user ID of the person withdrawing the TAR. |
| @Remark | nvarchar(1000) | A remark or comment for the withdrawal. |

### Logic Flow
1. The procedure starts by declaring variables to store line numbers, status IDs, and names.
2. It then attempts to begin a transaction and execute the following steps within it:
   - Selects the line number from TAMS_TAR where the TAR ID matches @TarId.
   - Retrieves the status ID for the selected line from TAMS_WFStatus based on certain conditions.
   - Finds the user name associated with the provided UID in TAMS_User.
3. If all previous steps are successful, it updates the TAR's status and records the withdrawal action in TAMS_Action_Log:
   - Updates TARStatusId to the retrieved status ID.
   - Sets WithdrawRemark to the provided remark.
   - Records the withdrawal by setting WithdrawBy to @UID and WithdrawDate to the current date and time.
4. If any step fails, it rolls back the transaction.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_WFStatus, TAMS_User
* **Writes:** TAMS_TAR (updated), TAMS_Action_Log

---


<a id='database-reference-sql-sp-api-send-sms'></a>
# Procedure: sp_api_send_sms

### Purpose
This stored procedure sends an SMS message to a list of contacts.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @contactno | nvarchar(MAX) | The contact numbers to send the SMS to, separated by commas. |
| @subject | nvarchar(500) | The subject of the SMS message. |
| @msg | nvarchar(MAX) | The content of the SMS message. |
| @ret | nvarchar(5) output | The return value indicating whether the operation was successful (0 = success, 1 = failure). |

### Logic Flow
The procedure starts by declaring variables and setting up a cursor to iterate over the contact numbers. It then fetches each contact number from the list, appends it to a string `@DerContactNo`, and executes an external stored procedure `SMSEAlertQ_EnQueue` to send the SMS message to all contacts in the list.

### Data Interactions
* **Reads:** [dbo].[SPLIT] table (explicitly selected)
* **Writes:** None

---


<a id='database-reference-sql-uxp-cmdshell'></a>
# Procedure: uxp_cmdshell

### Purpose
This stored procedure executes a command from the Windows Command Prompt, allowing for external commands to be executed within the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @cmd | VARCHAR(2048) | The command to be executed in the Windows Command Prompt. |

### Logic Flow
1. The stored procedure is created with a parameter @cmd, which holds the command to be executed.
2. When the procedure is executed, it uses the xp_cmdshell system stored procedure to execute the command specified in @cmd.
3. The xp_cmdshell procedure is used to interact with the Windows Command Prompt and execute the external command.

### Data Interactions
* **Reads:** None
* **Writes:** None

---

