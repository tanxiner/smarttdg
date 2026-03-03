# Procedure: sp_TAMS_Get_User_List_By_Line
**Type:** Stored Procedure

The procedure retrieves a list of users based on various search criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CurrentUser | NVARCHAR(100) | The current user's login ID. |

### Logic Flow
1. Checks if the user exists.
2. Inserts into Audit table.
3. Returns a list of users.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Role
* **Writes:** None

---

# Procedure: sp_TAMS_Get_User_List_By_Line_20211101
**Type:** Stored Procedure

The procedure retrieves a list of users based on various search criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @CurrentUser | NVARCHAR(100) | The current user's login ID. |

### Logic Flow
1. Checks if the user exists.
2. Retrieves modules for each user.
3. Returns a list of users.

### Data Interactions
* **Reads:** TAMS_User, TAMS_User_Role, TAMS_Role
* **Writes:** None

---

# Procedure: sp_TAMS_Get_User_RailLine
**Type:** Stored Procedure

The procedure retrieves the rail line for a given user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserId | NVARCHAR(100) | The user's login ID. |

### Logic Flow
1. Checks if the user has a role with 'All' as the line.
2. If true, returns 'DTL', 'NEL', or 'SPLRT'.
3. Otherwise, returns the distinct line for the user.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User

---

# Procedure: sp_TAMS_Get_User_RailLine_Depot
**Type:** Stored Procedure

The procedure retrieves the rail line for a given user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @UserId | NVARCHAR(100) | The user's login ID. |

### Logic Flow
1. Checks if the user has a role with 'All' as the line.
2. If true, returns 'NEL'.
3. Otherwise, returns the distinct line for the user that is also marked as a depot.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User

---

# Procedure: sp_TAMS_Get_User_TrackType
**Type:** Stored Procedure

The procedure retrieves the track type for a given login ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Loginid | NVARCHAR(100) | The user's login ID. |

### Logic Flow
1. Retrieves the distinct track type for the user.
2. Returns the result.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User

---

# Procedure: sp_TAMS_Get_User_TrackType_Line
**Type:** Stored Procedure

The procedure retrieves the track type for a given line and user ID.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Line | NVARCHAR(100) | The rail line. |
| @UserId | NVARCHAR(100) | The user's login ID. |

### Logic Flow
1. Retrieves the distinct track type for the user on the given line.
2. Returns the result.

### Data Interactions
* **Reads:** TAMS_User_Role, TAMS_User