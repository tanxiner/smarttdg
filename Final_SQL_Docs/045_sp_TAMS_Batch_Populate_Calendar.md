# Procedure: sp_TAMS_Batch_Populate_Calendar

### Purpose
Populate the TAMS_Calendar table with a full set of dates for a specified year, replacing any existing entries for that year.

### Parameters
| Name     | Type      | Purpose |
| :------- | :-------- | :------ |
| @Year    | NVARCHAR(4) | Target year for calendar population; defaults to the current year if omitted. |
| @YrFlag  | INT       | Optional year offset; added to @Year when greater than zero. |

### Logic Flow
1. **Initialize defaults** – If @Year is empty, set it to the current year. If @YrFlag is empty, set it to 0.  
2. **Apply year offset** – If @YrFlag > 0, increment @Year by that amount.  
3. **Prepare temporary reference table** – Truncate TAMS_TR_CALENDAR_REF to clear any prior data.  
4. **Load reference data** – Insert all rows from the remote TR_CALENDAR_REF table (queried via OPENQUERY on SPIN) into TAMS_TR_CALENDAR_REF, ordering by the first column.  
5. **Check for existing calendar data** – Count rows in TAMS_Calendar where the year of CalendarDate equals @Year.  
6. **Remove old data** – If any rows exist for that year, delete them from TAMS_Calendar.  
7. **Insert new calendar rows** – Insert into TAMS_Calendar the date, day, week, and holiday code from TAMS_TR_CALENDAR_REF for the target year, setting CreatedOn, CreatedBy, UpdatedOn, and UpdatedBy to the current date and user 1.  
8. **(Commented out)** – The procedure contains legacy code for inserting into CALENDAR_DAY, but it is not executed.

### Data Interactions
* **Reads:** TR_CALENDAR_REF (via OPENQUERY on SPIN), TAMS_Calendar (for counting existing rows).  
* **Writes:** TAMS_TR_CALENDAR_REF (truncate and insert), TAMS_Calendar (delete and insert).