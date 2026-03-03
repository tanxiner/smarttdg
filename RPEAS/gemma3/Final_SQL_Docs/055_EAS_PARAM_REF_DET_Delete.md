# Procedure: EAS_PARAM_REF_DET_Delete

### Purpose
This procedure removes records from the EAS_PARAM_REF_DET table based on specified criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParaRecType | VARCHAR(50) | Identifies the record type. |
| @ParaType | VARCHAR(50) | Identifies the parameter type. |
| @ParaCode | VARCHAR(50) | Identifies the parameter code. |
| @ParaDesc | VARCHAR(250) | Identifies the parameter description. |
| @EffFromDate | DATETIME | Specifies the start date for the deletion. |
| @EffToDate | DATETIME | Specifies the end date for the deletion. |
| @P_ErrorMsg | NVARCHAR(MAX) | Stores any error messages generated during the procedure execution. |

### Logic Flow
1.  The procedure begins with a try-catch block to handle potential errors during execution.
2.  A transaction is initiated to ensure atomicity – either all changes are committed, or none are.
3.  The procedure then executes a DELETE statement against the EAS_PARAM_REF_DET table.
4.  The DELETE statement removes records where the PARAM_TYPE matches the value provided in the @ParaType parameter, the PARAM_CODE matches the value in the @ParaCode parameter, the PARAM_REC_TYPE matches the value in the @ParaRecType parameter, the PARAM_DESC matches the value in the @ParaDesc parameter, the EFF_FROM_DATE matches the value in the @EffFromDate parameter, and the EFF_TO_DATE matches the value in the @EffToDate parameter.
5.  After the DELETE statement completes, the EAS_GET_ErrorMessage procedure is executed with an error code of '102', and the resulting error message is stored in the @P_ErrorMsg parameter.
6.  The transaction is committed if no errors occurred.
7.  If any error occurs within the try block, the transaction is rolled back, and the error message from the database system is stored in the @P_ErrorMsg parameter.

### Data Interactions
* **Reads:** None
* **Writes:** [EAS_PARAM_REF_DET]