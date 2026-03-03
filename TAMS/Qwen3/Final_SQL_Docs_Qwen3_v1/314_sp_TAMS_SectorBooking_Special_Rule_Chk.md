# Procedure: sp_TAMS_SectorBooking_Special_Rule_Chk

### Purpose
This stored procedure checks for special rules related to sector bookings, specifically for possession and protection access types.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @AccessType | NVARCHAR(20) | The type of access (Possession or Protection) |
| @Sectors | NVARCHAR(2000) | A comma-separated list of sector IDs |
| @PowerSelTxt | NVARCHAR(50) | The selected power option |

### Logic Flow
The procedure follows these steps:

1. Determine the power on indicator based on the selected power option.
2. If possession access type is selected and power is off, check if there are any special sectors with active bookings.
3. If protection access type is selected and power is off, check if there are any special sectors with active bookings.
4. For each sector ID in the list, check if it has a corresponding booking record in the TAMS_Special_Sector_Booking table.
5. If a booking record exists, check if all combinations for that sector ID have been completed (i.e., CombCheck = 1).
6. If any combination is missing, update the corresponding records in #TmpCombSectMax with CombCheck = 0.
7. After checking all sector IDs, count the number of missing combinations and return a result code.

### Data Interactions
* Reads: TAMS_Sector, TAMS_Special_Sector_Booking
* Writes: #TmpCombSect, #TmpCombSectMax