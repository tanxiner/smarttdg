# Page: ViewProfile
**File:** ViewProfile.aspx.cs

### 1. User Purpose
Users view and manage their profile information, including selecting external systems and adding new internal records.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page on first load by calling `SetupPage`; on postback it may reset or preserve state. |
| SetupPage | Retrieves the current user’s profile data and populates controls; prepares any necessary lookup tables. |
| ResetPage | Clears form fields and resets controls to their default state. |
| buildSystemSelectiondata | Generates a `DataTable` of system options based on whether the user is external or internal. |
| UpdateGVRows | Updates a GridView row with data from a `DataRow`, applying formatting or visibility rules depending on the external flag. |
| btn_externalNext_Click | Advances the user to the next step in the external profile workflow, likely saving current selections and redirecting. |
| btn_internalNewSave_Click | Validates input for a new internal record, persists it to the database, and refreshes the view to show the new entry. |

### 3. Data Interactions
* **Reads:** User profile, system selection lists, existing internal records.  
* **Writes:** New internal record entries; possibly updates to profile selections.

---

# Page: ViewSignUpStatus
**File:** ViewSignUpStatus.aspx.cs

### 1. User Purpose
Users can review the status of their sign‑up process and, if needed, resend the registration link.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Loads the sign‑up status page, invoking `SetupPage` with the current user’s data set. |
| SetupPage | Populates status controls (e.g., labels, progress indicators) using the provided `DataSet`. |
| ResetPage | Clears status displays and resets any interactive elements. |
| btn_externalBack_Click | Navigates the user back to the previous external sign‑up step or page. |
| btn_internalBack_Click | Navigates the user back to the previous internal sign‑up step or page. |
| btn_resendRegistrationLink_Click | Triggers the generation and sending of a new registration link to the user’s email address. |

### 3. Data Interactions
* **Reads:** User sign‑up status information from the database.  
* **Writes:** Sends an email containing a new registration link (no direct database write shown).

---

# Control: ViewSwitcher
**File:** ViewSwitcher.ascx.cs

### 1. User Purpose
Provides a simple interface for switching between two related views (e.g., internal vs. external) by presenting a link or button.

### 2. Key Events & Logic
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Determines the current view context and sets up the switch link or button using the `CurrentView`, `AlternateView`, and `SwitchUrl` properties. |

### 3. Data Interactions
* **Reads:** None explicitly; relies on page context to set view properties.  
* **Writes:** None; only updates UI elements to allow navigation.

---