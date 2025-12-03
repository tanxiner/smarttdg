# Page: TOABookOut  
**File:** TOABookOut.aspx.cs  

### 1. User Purpose  
Users complete a multi‑step form to book a TOA (Transfer of Ownership) out, adding parties, reviewing details, and finally surrendering the registration.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page, loads existing TOA data via the DAL, and sets up controls for the current step. |
| lbNextV1_Click | Advances the wizard from step 1 to step 2, validating current inputs before proceeding. |
| Tab1_Click | Switches the view to the first tab, ensuring any unsaved data is preserved. |
| Tab2_Click | Switches the view to the second tab, preparing the party list section. |
| lbPrevV2_Click | Returns the wizard from step 2 back to step 1, allowing the user to edit earlier information. |
| lbAddParties_Click | Adds a new party to the TOA registration; updates the parties grid and persists the change through the DAL. |
| gvParties_RowDataBound | Formats each row of the parties grid (e.g., alternating colors, adding action links). |
| gvParties_RowCommand | Handles commands from the parties grid such as delete or edit; updates the underlying data via the DAL. |
| lbSurrender_Click | Finalizes the TOA out process, marking the registration as surrendered and recording the action in the database. |
| LogError | Static helper that records exception details to a log for troubleshooting. |

### 3. Data Interactions  
* **Reads:** TOA registration record, list of parties associated with the registration.  
* **Writes:** Updates to the TOA registration status, additions or deletions of parties, surrender record.

---

# Page: TOAError  
**File:** TOAError.aspx.cs  

### 1. User Purpose  
Displays a user‑friendly error message when an unexpected issue occurs during TOA processing.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Retrieves the error details (typically from query parameters or session) and presents them to the user. |

### 3. Data Interactions  
* **Reads:** Error information passed to the page.  
* **Writes:** None.

---

# Page: TOAGenURL  
**File:** TOAGenURL.aspx.cs  

### 1. User Purpose  
Allows users to generate a secure URL that encodes a TOA registration identifier, and to decode such URLs back to readable form.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Sets up the page, possibly pre‑filling fields if a URL is already provided. |
| lblGen_Click | Takes the user’s input, encodes it using `ToEncode`, and displays the resulting URL. |
| ToEncode | Static helper that transforms a plain string into an encoded representation suitable for URLs. |
| ToDecode | Static helper that reverses the encoding, returning the original string. |

### 3. Data Interactions  
* **Reads:** None (operates on user input).  
* **Writes:** None (output is displayed to the user).

---

# Page: TVFAcknowledgement  
**File:** TVFAcknowledgement.aspx.cs  

### 1. User Purpose  
Shows a list of TVF (Transfer of Vehicle) acknowledgements and allows the user to load detailed acknowledgement controls for specific records.

### 2. Key Events & Logic  
| Event / Method | Business Logic Summary |
| :--- | :--- |
| Page_Load | Initializes the page and triggers the grid binding to display current acknowledgements. |
| BindGrid | Queries the database via the DAL to retrieve acknowledgement records and binds them to the grid control. |
| LoadOCCTVF_AckCtrl | Loads a detailed acknowledgement control for a given user ID, enabling further actions such as viewing or printing. |

### 3. Data Interactions  
* **Reads:** Acknowledgement records from the database.  
* **Writes:** None (display‑only functionality).