# Procedure: sp_TAMS_TOA_Get_Parties

The procedure retrieves party information for a specific TOA (TAMs Toa) ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TOAID | BIGINT | The ID of the TOA for which to retrieve parties |

### Logic Flow
1. The procedure first selects the number of parties associated with the specified TOA ID from the TAMS_TOA table.
2. It then retrieves a list of all parties, including their name, NRIC (National Registration Identity Card), whether they are a TMC (TAMs Toa Management Committee) member, and their in-charge status, ordered by party ID.
3. The procedure also generates two additional lists: one for witness parties and another for selected witnesses.
4. Finally, it counts the number of parties that have been booked in and the total count of such bookings.

### Data Interactions
* **Reads:** TAMS_TOA, TAMS_TOA_Parties