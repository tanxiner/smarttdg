# Procedure: sp_TAMS_Email_PasswordResetLinkByRegID

### Purpose
Sends a password‑reset link to a user’s registered email address.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserID | NVARCHAR(200) | Identifier of the user requesting a password reset. |
| @Cipher | NVARCHAR(200) | Encrypted token appended to the reset URL. |

### Logic Flow
1. Verify that a record exists in **TAMS_User** with the supplied **@UserID**.  
2. If the user exists, initialise email‑related variables: sender, system identifiers, subject, greeting, and recipient lists.  
3. Retrieve the user’s email address into **@ToList**.  
4. Construct the reset link by concatenating the base URL with **@Cipher**.  
5. Build the email body in three parts:  
   * **@Body1** – contains the reset link and a one‑day validity notice.  
   * **@Body2** – closing signature from the System Administrator.  
   * **@Body3** – automated‑email disclaimer.  
6. Concatenate the three body parts into **@Body**.  
7. Call **EAlertQ_EnQueue** to enqueue the email for delivery, passing all prepared parameters and capturing the generated **@AlertID**.

### Data Interactions
* **Reads:** `TAMS_User` (to confirm user existence and obtain the email address).  
* **Writes:** `EAlertQ_EnQueue` (inserts a new alert record for email dispatch).