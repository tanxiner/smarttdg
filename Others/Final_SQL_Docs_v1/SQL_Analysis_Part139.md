# Procedure: sp_TAMS_RGS_OnLoad_YD_TEST_20231208
**Type:** Stored Procedure

The purpose of this stored procedure is to retrieve and process data from various tables in the database, perform calculations, and insert data into temporary tables for further processing.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line		NVARCHAR(20) | Specifies the line type (NEL or DTL) |

### Logic Flow
1. The procedure starts by truncating two temporary tables, #TmpRGS and #TmpRGSSectors.
2. It then retrieves the current date and time using GETDATE() and converts them to DATE and TIME data types, respectively.
3. Based on the value of @Line, it determines whether to use the previous day's or today's date for operations and access dates.
4. The procedure then selects parameters from TAMS_Parameters table based on the line type (@Line) to determine various settings such as TOA call back time, RGS protection background, and RGS possession background.
5. It creates two cursors, @Cur01 and @Cur02, to iterate through TAMS_TAR and TAMS_TOA tables where the TARId matches the current TARId and the access date is either today's or yesterday's date, depending on the line type.
6. For each iteration, it extracts various fields from the TAMS_TAR and TAMS_TOA tables, including TARNo, TOANo, GrantTOATime, AckGrantTOATime, etc., and populates temporary variables such as @lv_Sno, @lv_IsTOAAuth, @lv_PartiesName, etc.
7. It then checks for specific conditions based on the line type (NEL or DTL) to determine various settings such as colour codes, remarks, and grant TOA enable status.
8. If the TARId is not empty, it inserts data into #TmpRGS table with populated temporary variables.
9. After iterating through all records in TAMS_TAR and TAMS_TOA tables, it closes both cursors and deallocates their resources.

### Data Interactions
* **Reads:** 
	+ TAMS_Parameters
	+ TAMS_TAR
	+ TAMS_TOA
	+ TAMS_TAR_Sector
	+ TAMS_Access_Requirement
	+ TAMS_Traction_Power_Detail
* **Writes:** 
	+ #TmpRGS
	+ #TmpRGSSectors