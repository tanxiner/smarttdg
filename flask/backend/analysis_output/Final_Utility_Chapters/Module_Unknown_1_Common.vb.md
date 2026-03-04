# Module: Common.vb
**File:** Common.vb

### 1. Purpose
This module provides utility functions for establishing database connections and retrieving service information.

### 2. Key Declarations
| Symbol | Kind | Description |
| :--- | :--- | :--- |
| `Common` | Class | The primary class containing connection methods and service information retrieval. |
| `Bus_info` | Class | Represents bus information with properties like Bus_No and Timestamp. |

### 3. Important Behavior & Side Effects
- `getConnection1`, `getConnection2`, `getConnection3`, `getConnection4`: These private methods establish database connections. The exact type of connection (e.g., SqlConnection) is returned.
- `Get_BC_Service_Info`: This public method retrieves service information based on input data. It returns a String.

### 4. Data Interactions
* **Reads:** None at runtime
* **Writes:** None at runtime