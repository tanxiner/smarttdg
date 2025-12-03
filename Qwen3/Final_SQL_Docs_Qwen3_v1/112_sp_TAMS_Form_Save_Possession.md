# Procedure: sp_TAMS_Form_Save_Possession

### Purpose
This stored procedure saves a possession record for a train (TAMs) into the database, including various details such as work description, type of work, and possession status.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | The ID of the train (TAMs) for which the possession record is being saved. |
| @Summary | NVARCHAR(1000) | A summary of the work description. |
| @WorkDesc | NVARCHAR(1000) | The detailed work description. |
| @TypeOfWorkId | INT | The ID of the type of work being performed. |
| @WorkWithinPossession | NVARCHAR(1000) | Information about the work within possession. |
| @TakePossession | NVARCHAR(1000) | Details about taking possession. |
| @GiveUpPossession | NVARCHAR(1000) | Details about giving up possession. |
| @Remarks | NVARCHAR(1000) | Any additional remarks or comments. |
| @PowerOnOff | INT | The power on/off status of the train. |
| @EngTrainFormation | NVARCHAR(50) | Information about the engine train formation. |
| @EngTrainArriveLoc | NVARCHAR(50) | Location of the engine train arrival. |
| @EngTrainArriveTime | NVARCHAR(10) | Time of engine train arrival. |
| @EngTrainDepartLoc | NVARCHAR(50) | Location of the engine train departure. |
| @EngTrainDepartTime | NVARCHAR(10) | Time of engine train departure. |
| @PCNRIC | NVARCHAR(50) | The PCNRIC (Personal Computerized National Registration Identification Card) number. |
| @PCName | NVARCHAR(100) | The name associated with the PCNRIC number. |
| @PossID | BIGINT OUTPUT | The ID of the newly saved possession record. |
| @Message | NVARCHAR(500) OUTPUT | Any error message or success message to be returned. |

### Logic Flow
1. Initialize variables and set the output parameter `@PossID` to 0.
2. Check if a transaction has already been started. If not, start a new transaction.
3. Insert the possession record into the `TAMS_Possession` table with all provided details.
4. Retrieve the ID of the newly saved possession record from the database using `SCOPE_IDENTITY()`.
5. Check for any errors during insertion. If an error occurs, set the output parameter `@Message` to an error message and exit the procedure.
6. If no errors occurred, commit the transaction and return the success message.
7. If an error occurred, roll back the transaction and return the error message.

### Data Interactions
* **Reads:** None explicitly selected from tables.
* **Writes:** The `TAMS_Possession` table is inserted with all provided details.