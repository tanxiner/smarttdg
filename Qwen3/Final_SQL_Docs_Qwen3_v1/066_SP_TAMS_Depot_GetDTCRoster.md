# Procedure: SP_TAMS_Depot_GetDTCRoster

### Purpose
This stored procedure retrieves a roster of depot personnel for a specific date.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @date | Date | The date for which to retrieve the roster. |

### Logic Flow
The procedure starts by setting NOCOUNT ON to prevent extra result sets from interfering with SELECT statements. It then selects distinct RosterCode values from TAMS_OCC_Duty_Roster where TrackType is 'depot'. This step retrieves a list of unique depot personnel codes.

Next, it performs a LEFT OUTER JOIN with the same table but filtered by OperationDate and TrackType='depot' to match the @date parameter. This step ensures that only roster codes for the specified date are included in the results.

The procedure then performs another LEFT OUTER JOIN with TAMS_User on DutyStaffId to retrieve the names and login IDs of the personnel associated with each roster code.

### Data Interactions
* **Reads:** TAMS_OCC_Duty_Roster, TAMS_User