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