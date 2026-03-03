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