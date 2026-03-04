# Procedure: SAGE_GET_BC_Service

### Purpose
This procedure retrieves departure information for a specific service, driver, and trip, incorporating data from multiple tables including time sheets, trip departure details, and MTV (Non-Open Mileage) data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_BusNo | nvarchar(8) | The bus number prefix. |
| @P_ActDepTime | varchar(30) | The actual departure time. |

### Logic Flow
The procedure begins by initializing several variables, including the current date and time, and various data fields. It then calculates the current time, handling cases where the actual departure time is before 4:00 AM.  It converts the input `P_ActDepTime` to a datetime value.

Next, the procedure extracts the bus number without the prefix and the bus number prefix from the input `P_BusNo`. It then attempts to find matching departure information from the `SCS_TIME_SHEET_DEP` table, joining it with `SCS_TRIP_DEPARTURE` based on location code, service number, and trip sequence number. This join retrieves the driver's number, scheduled arrival time, trip sequence number, end location code, service number, run time, and departure time.

The procedure then attempts to retrieve MTV (Non-Open Mileage) data associated with the trip and driver. It joins the MTV data with the trip departure details based on the trip date, service number, and duty number.

Finally, the procedure constructs a result set containing the service number, direction, driver number, departure time, duty number, scheduled arrival time, trip sequence number, start location code, end location code, run time, and MTV data.  It handles cases where the service number is '024', '027', '053', or '053A' by doubling the run time.  The procedure also includes error handling and data validation to ensure data integrity.