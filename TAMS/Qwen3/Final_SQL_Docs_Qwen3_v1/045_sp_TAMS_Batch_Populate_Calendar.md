# Procedure: sp_TAMS_Batch_Populate_Calendar

### Purpose
This stored procedure populates the TAMS_Calendar table with data from the TR_CALENDAR_REF table for a specified year.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Year | NVARCHAR(4) | The year to populate the calendar for. If not provided, it defaults to the current year. |
| @YrFlag | INT | A flag indicating whether to add a specific number of years to the default year. |

### Logic Flow
1. The procedure starts by setting up variables and checking if the input parameters are provided.
2. It truncates the TAMS_TR_CALENDAR_REF temporary table, which is used as a reference for the calendar data.
3. It selects all rows from the TR_CALENDAR_REF table, ordered by date, and inserts them into the TAMS_TR_CALENDAR_REF table.
4. It counts the number of days in the specified year that are already populated in the TAMS_Calendar table.
5. If there are existing calendar entries for the specified year, it deletes those entries.
6. It inserts new rows into the TAMS_Calendar table with data from the TAMS_TR_CALENDAR_REF table.

### Data Interactions
* **Reads:** TR_CALENDAR_REF, TAMS_Calendar
* **Writes:** TAMS_TR_CALENDAR_REF, TAMS_Calendar