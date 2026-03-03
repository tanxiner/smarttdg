# Technical Documentation

## Table of Contents

### System Documentation
- [AssemblyInfo](#ystemocumentation-agesnknownart1-1-assemblyinfo)
- [SAGE_API_SCS\SAGE_API\Common.vb](#ystemocumentation-agesnknownart1-2-sage-api-scssage-apicommonvb)
- [Constants](#ystemocumentation-agesnknownart1-3-constants)
- [GetServiceDriver](#ystemocumentation-agesnknownart1-4-getservicedriver)
- [Log](#ystemocumentation-agesnknownart1-5-log)
- [MyWebExtension](#ystemocumentation-agesnknownart1-6-mywebextension)

### Database Reference (SQL)
- [SAGE_GET_BC_Service](#atabaseeference-001ervice-1-sage-get-bc-service)

<br>


<a id='ystemocumentation-agesnknownart1-1-assemblyinfo'></a>
# Page: AssemblyInfo
**File:** SAGE_API_SCS\SAGE_API\My Project\AssemblyInfo.vb

### 1. User Purpose
This page's user purpose is Unknown (no explicit domain information in the code).

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |

---


<a id='ystemocumentation-agesnknownart1-2-sage-api-scssage-apicommonvb'></a>
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

---


<a id='ystemocumentation-agesnknownart1-3-constants'></a>
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

---


<a id='ystemocumentation-agesnknownart1-4-getservicedriver'></a>
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

---


<a id='ystemocumentation-agesnknownart1-5-log'></a>
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

---


<a id='ystemocumentation-agesnknownart1-6-mywebextension'></a>
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

---


<a id='atabaseeference-001ervice-1-sage-get-bc-service'></a>
# Procedure: SAGE_GET_BC_Service

### Purpose
This procedure retrieves departure information for a specific bus run, including driver, departure time, arrival time, and related details, considering potential disruptions and mileage data.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_BusNo | nvarchar(8) | The bus number identifier. |
| @P_ActDepTime | varchar(30) | The actual departure time of the bus run. |

### Logic Flow
The procedure begins by initializing several variables, including date and time related variables. It then calculates the current date and time, and adjusts the current time to account for potential time differences. It converts the input `ActDepTime` into a date/time format.

Next, the procedure attempts to retrieve departure information from the `scs_time_sheet_dep` table, joining it with the `SCS_TRIP_DEPARTURE` table based on location code, service number, and trip sequence number. It also joins with `SCS_CURR_RUN` to get the run number. The query filters based on the input bus number, bus prefix, and the actual departure time, ensuring that the departure time is before or equal to the provided `ActDepTime`. It also filters based on service number, excluding specific service numbers (024, 027, 053, 053A) to handle potential disruptions.

If no departing data is found, the procedure falls back to retrieving data from the `scs_trip_departure` table, joining it with `SCS_CURR_RUN` to get the run number. This fallback is used when the initial search in `scs_time_sheet_dep` doesn't yield results.

The procedure then attempts to determine the direction of travel based on the service number. If the service number starts with 'G' or 'W', it retrieves the direction from the `BIBS_SVC_GW` table. Otherwise, it retrieves the direction from the `BST_BSTMAST_DETAILS` table.

Finally, the procedure retrieves mileage data from the `SCS_MTV_SCHED_TRIP_FORSAGE` table, joining it with the departure data. It then selects and returns the relevant information, including the service number, direction, driver, departure time, arrival time, trip sequence number, terminal location code, end location code, run time, and mileage data.

---

