# Procedure: uxp_cmdshell

### Purpose
Executes an arbitrary operating‑system command supplied by the caller.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @cmd | VARCHAR(2048) | The command string to run via xp_cmdshell. |

### Logic Flow
1. The procedure receives a command string in @cmd.  
2. It calls the system stored procedure master.dbo.xp_cmdshell, passing @cmd as the argument.  
3. Execution of xp_cmdshell runs the command on the server’s operating system and returns any output or error messages to the caller.

### Data Interactions
* **Reads:** *none*  
* **Writes:** *none*