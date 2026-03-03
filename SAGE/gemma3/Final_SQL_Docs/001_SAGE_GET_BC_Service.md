# Procedure: SAGE_GET_BC_Service

### Purpose
This procedure retrieves departure information for a specific bus run, including driver, departure time, arrival time, and related details, considering potential disruptions and mileage data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_BusNo | nvarchar(8) | The bus number identifier. |
| @P_ActDepTime | varchar(30) | The actual departure time of the bus run. |

### Logic Flow
The procedure begins by initializing several variables, including date and time related variables. It then calculates the current date and time, and adjusts the current time to account for potential time differences. It converts the input `ActDepTime` into a date/time format.

Next, the procedure attempts to retrieve departure information from the `scs_time_sheet_dep` table, joining it with the `SCS_TRIP_DEPARTURE` table based on location code, service number, and trip sequence number. It also joins with `SCS_CURR_RUN` to get the run number. The query filters based on the input bus number, bus prefix, and the actual departure time, ensuring that the departure time is before or equal to the provided `ActDepTime`. It also filters based on service number, excluding specific service numbers (024, 027, 053, 053A) to handle potential disruptions.

If no departing data is found, the procedure falls back to retrieving data from the `scs_trip_departure` table, joining it with `SCS_CURR_RUN` to get the run number. This fallback is used when the initial search in `scs_time_sheet_dep` doesn't yield results.

The procedure then attempts to determine the direction of travel based on the service number. If the service number starts with 'G' or 'W', it retrieves the direction from the `BIBS_SVC_GW` table. Otherwise, it retrieves the direction from the `BST_BSTMAST_DETAILS` table.

Finally, the procedure retrieves mileage data from the `SCS_MTV_SCHED_TRIP_FORSAGE` table, joining it with the departure data. It then selects and returns the relevant information, including the service number, direction, driver, departure time, arrival time, trip sequence number, terminal location code, end location code, run time, and mileage data.