# Technical Documentation

## Table of Contents

### Web Pages
- [DateTimePicker.aspx](#ebages-agenknown1ateimeickeraspx-1-datetimepickeraspx)
- [GetServiceDriver.aspx](#ebages-agenknown2eterviceriveraspx-1-getservicedriveraspx)

### Modules/Others
- [AssemblyInfo.vb](#odulesthers-odulenknown4ssemblynfovb-1-assemblyinfovb)
- [Common.vb](#odulesthers-odulenknown1ommonvb-1-commonvb)
- [Constants.vb](#odulesthers-odulenknown2onstantsvb-1-constantsvb)
- [Log.vb](#odulesthers-odulenknown3ogvb-1-logvb)
- [MyWebExtension.vb](#odulesthers-odulenknown5yebxtensionvb-1-mywebextensionvb)

### Database Reference (SQL)
- [SAGE_GET_BC_Service](#atabaseeference-001ervice-1-sage-get-bc-service)

<br>


<a id='ebages-agenknown1ateimeickeraspx-1-datetimepickeraspx'></a>
# Page: DateTimePicker.aspx
**Web Page File:** DateTimePicker.aspx
**Code-Behind File:** DateTimePicker.aspx.vb

### 1. User Purpose
This page provides a date and time picker control for the user to select a date and time.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| `$('#datetimepicker1').datetimepicker();` | This JavaScript code initializes the Bootstrap datepicker control, named 'datetimepicker1', within the page. It likely sets up the UI elements and event handlers for the date and time selection. |

### 3. Data Interactions
* **Reads:**
    * User interaction with the date and time picker control (selecting a date and time).
* **Writes:**
    * The selected date and time are likely sent to the server as part of a form submission or AJAX request.  The exact mechanism is not visible in the provided IR.

---


<a id='ebages-agenknown2eterviceriveraspx-1-getservicedriveraspx'></a>
# Page: GetServiceDriver.aspx
**Web Page File:** GetServiceDriver.aspx
**Code-Behind File:** GetServiceDriver.aspx.vb

### 1. User Purpose
This page's user purpose is Unknown (no explicit domain information in the code).

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | This method is executed when the page is first loaded.  The specific logic within this method is not defined in the provided metadata. |

### 3. Data Interactions
* **Reads:** None explicitly defined in the provided metadata.
* **Writes:** None explicitly defined in the provided metadata.

---


<a id='odulesthers-odulenknown4ssemblynfovb-1-assemblyinfovb'></a>
# AssemblyInfo.vb
**File:** AssemblyInfo.vb

### 1. Purpose
This module defines attributes for the assembly, primarily related to versioning and copyright information.

### 2. Key Declarations
| Symbol | Kind | Description |
| :--- | :--- | :--- |
| `Version` | Constant | Represents the assembly version number. |
| `Copyright` | Constant | Specifies the copyright statement for the assembly. |

### 3. Important Behavior & Side Effects
- The `Version` and `Copyright` constants are used to configure the assembly metadata.  Changes to these constants will affect the metadata associated with the assembly.

### 4. Data Interactions
* **Reads:** None at runtime
* **Writes:** None at runtime

---


<a id='odulesthers-odulenknown1ommonvb-1-commonvb'></a>
# Common.vb
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

---


<a id='odulesthers-odulenknown2onstantsvb-1-constantsvb'></a>
# Constants.vb
**File:** Constants.vb

### 1. Purpose
This module defines a class containing a single constant used for displaying alert messages.

### 2. Key Declarations
| Symbol | Kind | Description |
| :--- | :--- | :--- |
| SCRIPT_ALERT_MESSAGE | Constant | A string literal used to display alert messages. |

### 3. Important Behavior & Side Effects
None at runtime. The constant is intended for use in displaying alert messages.

### 4. Data Interactions
* **Reads:** None at runtime.
* **Writes:** None at runtime.

---


<a id='odulesthers-odulenknown3ogvb-1-logvb'></a>
# Log.vb
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

---


<a id='odulesthers-odulenknown5yebxtensionvb-1-mywebextensionvb'></a>
# MyWebExtension.vb
**File:** MyWebExtension.vb

### 1. Purpose
This module provides a framework for extending web applications with custom functionality.

### 2. Key Declarations
| Symbol | Kind | Description |
| :--- | :--- | :--- |
| `MyWebExtension` | Class | The main class for defining and managing web extensions. |

### 3. Important Behavior & Side Effects
- The `MyWebExtension` class is designed to be instantiated and configured to handle specific web application events.
- Configuration of the extension determines its behavior and the events it responds to.

### 4. Data Interactions
* **Reads:** None at runtime
* **Writes:** None at runtime

---


<a id='atabaseeference-001ervice-1-sage-get-bc-service'></a>
# Procedure: SAGE_GET_BC_Service

### Purpose
This procedure retrieves departure information for a specific service, driver, and trip, incorporating data from multiple tables including time sheets, trip departure details, and MTV (Non-Open Mileage) data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_BusNo | nvarchar(8) | The bus number prefix. |
| @P_ActDepTime | varchar(30) | The actual departure time. |

### Logic Flow
The procedure begins by initializing several variables, including the current date and time, and various data fields. It then calculates the current time, handling cases where the actual departure time is before 4:00 AM.  It converts the input `P_ActDepTime` to a datetime value.

Next, the procedure extracts the bus number without the prefix and the bus number prefix from the input `P_BusNo`. It then attempts to find matching departure information from the `SCS_TIME_SHEET_DEP` table, joining it with `SCS_TRIP_DEPARTURE` based on location code, service number, and trip sequence number. This join retrieves the driver's number, scheduled arrival time, trip sequence number, end location code, service number, run time, and departure time.

The procedure then attempts to retrieve MTV (Non-Open Mileage) data associated with the trip and driver. It joins the MTV data with the trip departure details based on the trip date, service number, and duty number.

Finally, the procedure constructs a result set containing the service number, direction, driver number, departure time, duty number, scheduled arrival time, trip sequence number, start location code, end location code, run time, and MTV data.  It handles cases where the service number is '024', '027', '053', or '053A' by doubling the run time.  The procedure also includes error handling and data validation to ensure data integrity.

---

