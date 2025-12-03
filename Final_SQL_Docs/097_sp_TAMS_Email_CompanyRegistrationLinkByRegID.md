# Procedure: sp_TAMS_Email_CompanyRegistrationLinkByRegID

### Purpose
Sends a company registration link to the email address associated with a specified registration ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @RegID | NVARCHAR(200) | Identifier of the registration record to process |
| @Cipher | NVARCHAR(200) | Encrypted token used to build the registration URL |

### Logic Flow
1. Verify that a registration record exists for the supplied @RegID.  
2. If the record exists, initialise variables for email composition: sender, system identifiers, subject, greeting, recipient list, and message body sections.  
3. Retrieve the cutoff period from TAMS_Parameters where ParaCode equals 'CompanyRegCutOff'.  
4. Fetch the recipient email address from TAMS_Registration for the given @RegID.  
5. Construct the registration link by appending @Cipher to the base URL.  
6. Build the email body in three parts:  
   - A table containing the link and a note about the link’s validity period.  
   - A closing table with a sign‑off from the System Administrator.  
   - A disclaimer table indicating the email is computer‑generated.  
7. Concatenate the body parts into a single message.  
8. Call the EAlertQ_EnQueue stored procedure, passing all email parameters and the composed body, to enqueue the message for delivery.

### Data Interactions
* **Reads:** TAMS_Registration, TAMS_Parameters  
* **Writes:** Enqueues an alert via EAlertQ_EnQueue (writes to the alert queue)