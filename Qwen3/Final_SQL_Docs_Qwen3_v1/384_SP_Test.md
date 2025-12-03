# Procedure: SP_Test

### Purpose
This stored procedure performs a quality control check on a specific National Registration Identity Card (NRIC) number, verifying its validity and updating its status accordingly.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | NRIC Number |

### Logic Flow
1. The procedure starts by setting up temporary tables and variables to store the results of the quality control check.
2. It then calls another stored procedure, `sp_TAMS_TOA_QTS_Chk`, with specific parameters to perform the quality control check on the provided NRIC number.
3. If the result is invalid, the procedure truncates the temporary table, updates the status, and calls the same stored procedure again with different parameters to recheck the validity of the NRIC number.
4. The procedure continues this process until it determines whether the NRIC number is valid or not.
5. Finally, it drops the temporary table and prints the final result.

### Data Interactions
* **Reads:** #tmpnric table (temporary table created during the procedure)
* **Writes:** #tmpnric table (temporary table), as well as other tables involved in the quality control check process