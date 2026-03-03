# Procedure: sp_TAMS_Insert_ExternalUserRegistrationModule

### Purpose
Insert a new external user registration module record, log the action, and, if the registration is for a company, notify system approvers.

### Parameters
| Name      | Type          | Purpose |
| :-------- | :------------ | :------ |
| @RegID    | INT           | Identifier of the registration record. |
| @Line     | NVARCHAR(20)