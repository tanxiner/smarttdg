# Procedure: EAS_Form_Save_Attach_Files

### Purpose
This procedure saves file attachment information associated with a form.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_GUID | nvarchar(225) | Unique identifier for the form. |
| @P_FILENM | varchar(200) | Name of the attached file. |
| @P_FileType | varchar(200) | Type of the attached file. |
| @P_FILESIZE | varchar(200) | Size of the attached file. |
| @P_FILEURL | varchar(255) | URL location of the attached file. |
| @p_LoginID | varchar(15) | Identifier for the user creating the attachment. |
| @p_errormsg | varchar(500) | Output parameter to hold error messages. |

### Logic Flow
The procedure initializes an output parameter named @p_errormsg to an empty string. It then inserts a new record into the `EAS_Form_Attach_Document` table. The new record contains the form's unique identifier (@P_GUID), the file name (@P_FILENM), the file type (@P_FileType), the file URL (@P_FILEURL), the file size (@P_FILESIZE), the user identifier (@p_LoginID), and the current date and time.

### Data Interactions
* **Reads:** None
* **Writes:** `EAS_Form_Attach_Document`