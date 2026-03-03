# Procedure: EAS_PARAM_REF_DET_Update

### Purpose
This procedure updates information within the EAS_PARAM_REF_DET table based on provided parameter values.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParaRecType | VARCHAR(50) | Specifies the record type for the parameter reference detail. |
| @ParaType | VARCHAR(50) | Identifies the type of parameter being referenced. |
| @ParaCode | VARCHAR(50) | Represents the unique code for the parameter. |
| @ParaDesc | VARCHAR(250) | Stores the description associated with the parameter. |
| @EffFromDate | DATETIME | Defines the effective date range for the parameter reference detail. |
| @EffToDate | DATETIME | Specifies the end date for the effective date range. |
| @d1 | DATETIME | Stores a numerical value associated with the parameter reference detail. |
| @d2 | DATETIME | Stores another numerical value associated with the parameter reference detail. |
| @c1 | VARCHAR(50) | Stores a character value associated with the parameter reference detail. |
| @c2 | VARCHAR(50) | Stores another character value associated with the parameter reference detail. |
| @n1 | INT | Stores an integer value associated with the parameter reference detail. |
| @n2 | DECIMAL(18,2) | Stores a decimal value associated with the parameter reference detail. |
| @t1 | VARCHAR(4) | Stores a character code associated with the parameter reference detail. |
| @t2 | VARCHAR(4) | Stores another character code associated with the parameter reference detail. |
| @UpdatedBy | VARCHAR(50) | Indicates the user who made the update. |
| @P_ErrorMsg | NVARCHAR(MAX) | Output parameter to hold any error messages. |

### Logic Flow
The procedure begins with a try-catch block to handle potential errors during the update process. It then starts a new transaction. The procedure updates the EAS_PARAM_REF_DET table. The update sets the PARAM_DESC, EFF_FROM_DATE, EFF_TO_DATE, PARAM_VAL_D1, PARAM_VAL_D2, PARAM_VAL_C1, PARAM_VAL_C2, PARAM_VAL_N1, PARAM_VAL_N2, PARAM_VAL_T1, and PARAM_VAL_T2 columns. The ISNULL function is used to handle potential NULL values for the D1 and D2 columns. The ModifiedOn and ModifiedBy columns are automatically populated with the current date and the user who performed the update, respectively. The update is performed based on the provided @ParaRecType, @ParaType, and @ParaCode values. After the update is complete, the transaction is committed. If any error occurs during the process, the catch block is executed, rolls back the transaction, and sets the @P_ErrorMsg output parameter with the error message.

### Data Interactions
* **Reads:** [EAS_PARAM_REF_DET]
* **Writes:** [EAS_PARAM_REF_DET]