# Procedure: test

### Purpose
This procedure retrieves all data from a specified READONLY table.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @test | Table | Input table to be read. |

### Logic Flow
The procedure receives a table named @test as input. It then executes a select statement that retrieves all rows and columns from the specified table. The result of this select statement is not further processed or modified within the procedure. The retrieved data is simply returned.

### Data Interactions
* **Reads:** [dbo].[test]
* **Writes:** None