# Procedure: sp_TAMS_RGS_OnLoad_Enq

### Purpose
This stored procedure performs an on-load inquiry for TAMS RGS data, retrieving relevant information from various tables and performing calculations to determine the status of each record.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(20) | The line number used to filter records. |
| @TrackType | nvarchar(50) | The track type used to filter records. |
| @OPDate | NVARCHAR(20) | The operation date used to filter records. |

### Logic Flow
The procedure follows these steps:

1. It truncates two temporary tables, #TmpRGS and #TmpRGSSectors, to ensure a clean start.
2. It sets the current date and time variables based on the input parameters @OPDate and @Line.
3. If the current time is greater than a specified cutoff time (06:00:00), it sets the operation date to the current date and the access date to the next day; otherwise, it sets both dates to the previous day.
4. It retrieves values from TAMS_Parameters table based on input parameters @Line and @TrackType to determine TOACallBackTime, RGSPossBG, RGSProtBG, and RGSCancBG.
5. It checks if there are any records in TAMS_OCC_Auth that match the current date and time, and if so, it sets IsTOAAuth to 1.
6. For each record in TAMS_TAR, it performs the following checks:
	* If the line is 'DTL', it retrieves additional information from TAMS_TAR_AccessReq table based on @Line and @TrackType.
	* It calculates the color code for the record based on its status and sets IsGrantTOAEnable accordingly.
7. It inserts the calculated values into #TmpRGS temporary table.
8. Finally, it fetches all records from #TmpRGS and displays them in a sorted order.

### Data Interactions
* **Reads:** TAMS_TAR, TAMS_TOA, TAMS_OCC_Auth, TAMS_Traction_Power_Detail, TAMS_TAR_Sector, TAMS_Sector, TAMS_Parameters, TAMS_TAMSTOASector, TAMS_TAR_AccessReq.
* **Writes:** #TmpRGS temporary table.