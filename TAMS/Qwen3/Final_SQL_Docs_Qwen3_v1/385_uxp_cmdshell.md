# Procedure: uxp_cmdshell

### Purpose
This stored procedure executes a command from the Windows Command Prompt, allowing for external commands to be executed within the database.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @cmd | VARCHAR(2048) | The command to be executed in the Windows Command Prompt. |

### Logic Flow
1. The stored procedure is created with a parameter @cmd, which holds the command to be executed.
2. When the procedure is executed, it uses the xp_cmdshell system stored procedure to execute the command specified in @cmd.
3. The xp_cmdshell procedure is used to interact with the Windows Command Prompt and execute the external command.

### Data Interactions
* **Reads:** None
* **Writes:** None



