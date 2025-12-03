# Procedure: sp_TAMS_SectorBooking_QTS_Chk

### Purpose
This stored procedure checks if a sector booking is valid for a given person, based on their qualification details.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(MAX) | The National Registration Identity Number of the person. |
| @qualdate | NVARCHAR(MAX) | The date of the person's qualification. |
| @line | NVARCHAR(MAX) | The line number associated with the sector booking. |
| @TrackType | NVARCHAR(50) | The type of track for the sector booking. |

### Logic Flow
1. The procedure starts by declaring variables to store error messages and cursor handles.
2. It then creates temporary tables #tmpnric and #tmpqtsqc to store qualification data.
3. The procedure truncates these tables before processing new data.
4. It selects the relevant qualification details from TAMS_Parameters based on the provided line number and date of qualification.
5. For each person in the #tmpnric table, it queries the QTS_Personnel and QTS_Qualification tables to retrieve their qualification details.
6. If no suspension information is found for a person's qualification, the procedure updates their status as "InValid".
7. If suspension information is found, but the person's qualification date is before the valid access date or after the valid till date, the procedure updates their status as "InValid".
8. Otherwise, if the person's qualification date falls within the valid access and valid till dates, the procedure updates their status as "Valid".
9. Finally, the procedure returns the updated qualification details for each person.

### Data Interactions
* **Reads:** TAMS_Parameters, QTS_Personnel, QTS_Qualification tables.
* **Writes:** #tmpnric and #tmpqtsqc temporary tables.