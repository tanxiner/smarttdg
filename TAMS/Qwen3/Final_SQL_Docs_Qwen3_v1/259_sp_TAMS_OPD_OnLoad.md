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