# Page: AssemblyInfo
**File:** SAGE_API_SCS\SAGE_API\My Project\AssemblyInfo.vb

### 1. User Purpose
This page's user purpose is Unknown (no explicit domain information in the code).

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |

# Page: SAGE_API_SCS\SAGE_API\Common.vb
**File:** Common.vb

### 1. User Purpose
Users interact with this page to establish database connections.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| getConnection1 | Establishes a database connection. |
| getConnection2 | Establishes a database connection. |
| getConnection3 | Establishes a database connection. |
| getConnection4 | Establishes a database connection. |
| Get_BC_Service_Info(data_str: String) | Retrieves service information based on input data. (inferred from: baseType='SBSTransit.Common', file='SAGE_API_SCS\SAGE_API\Common.vb') |

### 3. Data Interactions
* **Reads:** None
* **Writes:** None

# Page: Constants
**File:** SAGE_API_SCS\SAGE_API\Constants.vb

### 1. User Purpose
This page defines constants used throughout the application.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| SCRIPT_ALERT_MESSAGE | Displays an alert message to the user. |

### 3. Data Interactions
* **Reads:** None
* **Writes:** None

# Page: GetServiceDriver
**File:** GetServiceDriver.aspx.vb

### 1. User Purpose
Users access this page to retrieve a service driver.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | This method is executed when the page loads. It initializes the driver object and populates the driver details based on the provided input. |

### 3. Data Interactions
* **Reads:** Driver (implied, based on driver object initialization)
* **Writes:** None

# Page: Log
**File:** Log.vb

### 1. User Purpose
Users utilize this page to log messages to a file.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| logging(Filename: String, msg: String) | This method writes a message to a specified file. |
| logging(Filename: String, msg: String, stopcode: String) | This method writes a message to a specified file, and also includes a stopcode parameter. |
| logging_traceFile(trace_filename: String, msg: String) | This method writes a message to a specified file. |

# Page: MyWebExtension
**File:** MyWebExtension.vb

### 1. User Purpose
Users use this page to submit a completed order.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Submit | This method handles the submission of the completed order form. It calls a method to save the order data and then sends an email notification. |

### 3. Data Interactions
* **Reads:**  (no explicit data reads in the provided IR)
* **Writes:**  (no explicit data writes in the provided IR)