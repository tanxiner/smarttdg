# Procedure: sp_Get_TypeOfWorkByLine

### Purpose
Retrieve active type‑of‑work records for a specified line and track type, ordered by priority.

### Parameters
| Name        | Type          | Purpose |
| :---        | :---          | :--- |
| @Line       | nvarchar(10)  | Line identifier to filter records. |
| @TrackType  | nvarchar(50)  | Track type to filter records. |

### Logic Flow
1. Accept optional @Line and @TrackType values.  
2. Query the `TAMS_Type_Of_Work` table.  
3. Apply a filter where the `Line` column equals the supplied @Line value.  
4. Apply a filter where the `TrackType` column equals the supplied @TrackType value.  
5. Include only rows where `IsActive` is 1.  
6. Return the columns `ID`, `Line`, `TypeOfWork`, `ColourCode`, `ForSelection`, and `[Order]`.  
7. Sort the result set by the `[Order]` column in ascending order.

### Data Interactions
* **Reads:** `TAMS_Type_Of_Work`  
* **Writes:** None