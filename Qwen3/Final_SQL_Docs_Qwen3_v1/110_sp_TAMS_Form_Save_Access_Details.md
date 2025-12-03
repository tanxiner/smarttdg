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