# Procedure: sp_TAMS_Update_UserRegModule_SysOwnerApproval_20231009
**Type:** Stored Procedure

The purpose of this stored procedure is to update a user's registration module status from "External" to "Approved" and perform additional actions such as sending an email notification.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module being updated. |
| @UpdatedBy | INT | The user ID of the system owner who is updating the status. |

### Logic Flow
1. Checks if the user exists.
2. Inserts into Audit table.
3. Returns ID.

### Data Interactions
* Reads: TAMS_Registration, TAMS_Reg_Module, TAMS_WFStatus, TAMS_Workflow, TAMS_Endorser, TAMS_User_Role
* Writes: TAMS_Reg_Module

The procedure first checks if the user exists by querying the TAMS_Registration table. If the user does not exist, it inserts a new record into the TAMS_User table.

Next, it retrieves the current status of the registration module from the TAMS_Reg_Module table and updates it to "Approved".

It then sends an email notification to the user using the EAlertQTo procedure. The email contains a link to access the system.

Finally, it inserts a new record into the TAMS_User_Role table if the user is not already assigned to the role.

# Procedure: sp_TAMS_Update_UserRegRole_SysOwnerApproval
**Type:** Stored Procedure

The purpose of this stored procedure is to update the assignment status of a registration module role from "External" to "Assigned".

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegModID | INT | The ID of the registration module being updated. |
| @RegRoleID | INT | The ID of the registration module role being updated. |
| @IsAssigned | BIT | The new assignment status. |
| @RejectRemarks | NVARCHAR(MAX) | Optional rejection remarks. |
| @UpdatedBy | INT | The user ID of the system owner who is updating the status. |

### Logic Flow
1. Retrieves the current user ID from the TAMS_Registration table.
2. Updates the registration module role status in the TAMS_Reg_Role table.
3. Inserts or updates a new record into the TAMS_User_Role table if necessary.

### Data Interactions
* Reads: TAMS_Registration, TAMS_Reg_Module, TAMS_Reg_Role, TAMS_User_Role
* Writes: TAMS_Reg_Role

The procedure first retrieves the current user ID from the TAMS_Registration table. It then updates the registration module role status in the TAMS_Reg_Role table.

If the new assignment status is "Assigned", it inserts or updates a new record into the TAMS_User_Role table if necessary.

# Procedure: sp_TAMS_Update_User_Details_By_ID
**Type:** Stored Procedure

The purpose of this stored procedure is to update user details by ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | INT | The ID of the user being updated. |
| @Name | NVARCHAR(100) | The new name for the user. |
| @Email | NVARCHAR(200) | The new email address for the user. |
| @Mobile | NVARCHAR(20) | The new mobile phone number for the user. |
| @OfficeTel | NVARCHAR(20) | The new office telephone number for the user. |
| @Dept | NVARCHAR(100) | The new department for the user. |
| @ValidTo | NVARCHAR(20) | The new valid-to date for the user. |
| @IsActive | BIT | The new active status for the user. |
| @UpdatedBy | INT | The user ID of the system owner who is updating the details. |

### Logic Flow
1. Checks if the user exists.
2. Updates the user details in the TAMS_User table.

### Data Interactions
* Reads: TAMS_User
* Writes: TAMS_User

The procedure first checks if the user exists by querying the TAMS_User table. If the user does not exist, it inserts a new record into the TAMS_User table.

Next, it updates the user details in the TAMS_User table based on the provided parameters.

# Procedure: sp_TAMS_User_CheckLastEmailRequest
**Type:** Stored Procedure

The purpose of this stored procedure is to check if an email request has been made within a certain time limit for a specific user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(200) | The ID of the user being checked. |
| @Mode | NVARCHAR(200) | The mode of check (User Detail View or Forget Password). |

### Logic Flow
1. Retrieves the maximum date of email requests for the specified user.
2. Checks if an email request has been made within the allowed time limit.

### Data Interactions
* Reads: TAMS_Registration, EAlertQTo

The procedure first retrieves the maximum date of email requests for the specified user by querying the EAlertQTo table.

Next, it checks if an email request has been made within the allowed time limit by comparing the current date with the maximum date retrieved earlier.

# Procedure: sp_TAMS_User_CheckLastUserRegistration
**Type:** Stored Procedure

The purpose of this stored procedure is to check if a user registration has been made within a certain time limit for a specific user.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LoginID | NVARCHAR(200) | The ID of the user being checked. |

### Logic Flow
1. Retrieves the maximum date of user registrations for the specified user.
2. Checks if a user registration has been made within the allowed time limit.

### Data Interactions
* Reads: TAMS_Registration

The procedure first retrieves the maximum date of user registrations for the specified user by querying the TAMS_Registration table.

Next, it checks if a user registration has been made within the allowed time limit by comparing the current date with the maximum date retrieved earlier.

# Procedure: sp_TAMS_UsersManual
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve the users manual value from the TAMS_Parameters table.

### Logic Flow
1. Retrieves the users manual value from the TAMS_Parameters table.
2. Returns the value.

### Data Interactions
* Reads: TAMS_Parameters