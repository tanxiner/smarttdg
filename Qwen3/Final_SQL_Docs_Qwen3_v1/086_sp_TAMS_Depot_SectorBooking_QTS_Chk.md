# Procedure: sp_TAMS_Depot_SectorBooking_QTS_Chk

### Purpose
This stored procedure checks if a person's qualification status is valid for a specific depot sector booking.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @nric | NVARCHAR(MAX) | The person's ID number. |
| @qualdate | NVARCHAR(MAX) | The date of the qualification. |
| @line | NVARCHAR(MAX) | The line number. |
| @TrackType | NVARCHAR(50) | The track type. |

### Logic Flow
The procedure follows these steps:

1. It initializes several variables to keep track of the results.
2. It creates temporary tables to store the qualification data and the person's details.
3. It loops through each row in the #tmpnric table, which contains the person's details.
4. For each row, it checks if there is a matching record in the #tmpqtsqc table, which contains the qualification status for each person.
5. If no matching record is found, it updates the person's status to "InValid".
6. If a matching record is found, it checks if the person has any suspension information. If not, it updates the person's status to "Valid". If there is suspension information, it checks if the qualification date is within the valid period. If it is, it updates the person's status to "Valid". Otherwise, it updates the person's status to "InValid".
7. Finally, it returns the updated person's details.

### Data Interactions
* **Reads:** #tmpnric, #tmpqtsqc
* **Writes:** #tmpnric