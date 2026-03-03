# Procedure: EAS_PARAM_REF_DET_Insert

### Purpose
This procedure inserts a new record into the EAS_PARAM_REF_DET table, representing a parameter reference detail.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParaRecType | VARCHAR(50) |  Specifies the record type for the parameter reference detail. |
| @ParaType | VARCHAR(50) |  Indicates the type of parameter being referenced. |
| @ParaCode | VARCHAR(50) |  Represents the unique code for the parameter reference. |
| @ParaDesc | VARCHAR(250) |  Provides a description for the parameter reference detail. |
| @EffFromDate | DATETIME |  Defines the start date for the parameter reference detail's validity. |
| @EffToDate | DATETIME |  Specifies the end date for the parameter reference detail's validity. |
| @d1 | DATETIME |  Stores a date/time value. |
| @d2 | DATETIME |  Stores a date/time value. |
| @c1 | VARCHAR(50) |  Stores a character string value. |
| @c2 | VARCHAR(50) |  Stores a character string value. |
| @n1 | INT |  Stores an integer value. |
| @n2 | DECIMAL(18,2) |  Stores a decimal number value. |
| @t1 | VARCHAR(4) |  Stores a character string value representing a time code. |
| @t2 | VARCHAR(4) |  Stores a character string value representing a time code. |
| @CreatedBy | VARCHAR(50) |  Identifies the user who created the record. |
| @P_ErrorMsg | NVARCHAR(MAX) |  Output parameter to hold any error messages. |

### Logic Flow
1.  **Duplicate Check:** The procedure first checks if a record already exists in the EAS_PARAM_REF_DET table with the same `PARAM_REC_TYPE`, `PARAM_TYPE`, and `PARAM_CODE`, and where the `EFF_FROM_DATE` falls within the range defined by `@EffFromDate` and `@EffToDate` or vice versa.
2.  **Error Handling (Duplicate):** If a duplicate record is found, the `EAS_GET_ErrorMessage` procedure is executed with an error code of '151', and the resulting error message is stored in the `@P_ErrorMsg` output parameter. The error message is then returned.
3.  **Transaction Start:** If no duplicate record is found, the procedure begins a new transaction.
4.  **Data Insertion:** A new record is inserted into the `EAS_PARAM_REF_DET` table, populating all the specified fields with the provided input values, including the current date and time for `ModifiedOn` and `CreatedOn` fields, and the `@CreatedBy` user identifier.
5.  **Success Confirmation:** The `EAS_GET_ErrorMessage` procedure is executed with an error code of '101', and the resulting error message is stored in the `@P_ErrorMsg` output parameter.
6.  **Transaction Commit:** The transaction is committed, making the changes permanent.
7.  **Error Handling (General):** If any error occurs during the process (e.g., data validation error), the `CATCH` block is executed. The error message is retrieved using `ERROR_MESSAGE()` and stored in the `@P_ErrorMsg` output parameter.
8.  **Transaction Rollback:** The transaction is rolled back, undoing any changes made during the process.

### Data Interactions
* **Reads:**  `EAS_PARAM_REF_DET`
* **Writes:** `EAS_PARAM_REF_DET`