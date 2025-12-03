# Procedure: sp_TAMS_Depot_TOA_QTS_Chk
**Type:** Stored Procedure

Purpose: This stored procedure checks if a user has valid qualification data for a specific line and date range.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(50) | The user's NRIC number. |
| @qualdate | NVARCHAR(20) | The date of the qualification check. |
| @line | NVARCHAR(20) | The line for which the qualification is being checked. |
| @QualCode | NVARCHAR(50) | The code for the qualification type. |

### Logic Flow
1. Checks if user exists by decrypting their access ID and comparing it to the provided NRIC number.
2. Retrieves all qualification data for the user, including last access date, valid access date, and valid till date.
3. Checks if any of the qualification data have a suspend till date that is later than the current timestamp, indicating an invalid qualification.
4. If no invalid qualifications are found, checks if the provided qualification date falls within the valid access date range.
5. Returns the user's NRIC number, name string, line, qualification date, qualification code, and qualification status.

### Data Interactions
* **Reads:** QTS_Personnel, QTS_Personnel_Qualification, QTS_Qualification tables.
* **Writes:** None.