# Module: Log.vb
**File:** Log.vb

### 1. Purpose
This module provides methods for logging messages to a file.

### 2. Key Declarations
| Symbol | Kind | Description |
| :--- | :--- | :--- |
| `logging` | Method | Logs a message to a specified file. |
| `logging_traceFile` | Method | Logs a message to a specified trace file. |

### 3. Important Behavior & Side Effects
- The `logging` and `logging_traceFile` methods write to a file. The exact file path is not specified in the module definition.
- The `logging` method accepts an optional `stopcode` parameter.

### 4. Data Interactions
* **Reads:** None at runtime
* **Writes:** To a file. The file path is not defined within this module.