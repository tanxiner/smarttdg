# Procedure: sp_TAMS_Form_Save_Possession

### Purpose
Persist a new possession record for a TAR and return its generated identifier.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @TARID | BIGINT | Identifier of the TAR to associate the possession with |
| @Summary | NVARCHAR(1000) | Short description of the possession |
| @WorkDesc | NVARCHAR(1000) | Detailed work description |
| @TypeOfWorkId | INT | Foreign key to the type of work performed |
| @WorkWithinPossession | NVARCHAR(1000) | Work performed while in possession |
| @TakePossession | NVARCHAR(1000) | Details of taking possession |
| @GiveUpPossession | NVARCHAR(1000) | Details of giving up possession |
| @Remarks | NVARCHAR(1000) | Additional remarks |
| @PowerOnOff | INT | Indicator of power status |
| @EngTrainFormation | NVARCHAR(50) | Formation of the engineering train |
| @EngTrainArriveLoc | NVARCHAR(50) | Arrival location of the engineering train |
| @EngTrainArriveTime | NVARCHAR(10) | Arrival time of the engineering train |
| @EngTrainDepartLoc | NVARCHAR(50) | Departure location of the engineering train |
| @EngTrainDepartTime | NVARCHAR(10) | Departure time of the engineering train |
| @PCNRIC | NVARCHAR(50) | Personal identification number, encrypted before storage |
| @PCName | NVARCHAR(100) | Name of the person responsible |
| @PossID | BIGINT OUTPUT | Identifier of the newly inserted possession record |
| @Message | NVARCHAR(500) OUTPUT | Status or error message after execution |

### Logic Flow
1. Initialise @PossID to 0 and set @IntrnlTrans flag to 0.  
2. If no active transaction exists, set @IntrnlTrans to 1 and begin a new transaction.  
3. Insert a new row into TAMS_Possession using the supplied parameters, encrypting @PCNRIC via dbo.EncryptString.  
4. Capture the generated identity value into @PossID.  
5. If the insert fails, set @Message to an error string and jump to the error handling section.  
6. On successful completion, commit the transaction if it was started internally and return @Message.  
7. In the error handling section, rollback the transaction if it was started internally and return @Message.

### Data Interactions
* **Reads:** None  
* **Writes:** TAMS_Possession  

---