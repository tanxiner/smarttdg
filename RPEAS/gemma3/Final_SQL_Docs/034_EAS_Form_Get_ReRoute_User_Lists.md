# Procedure: EAS_Form_Get_ReRoute_User_Lists

### Purpose
This procedure retrieves a list of active user IDs and names from the RPEAS system that are not associated with a specific form approval.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @P_Guid | varchar(225) | The unique identifier of the form. |
| @P_ReRoute_lvl | varchar(1) |  The level of re-routing. |

### Logic Flow
The procedure begins by selecting user identifiers and names from the EAS_USER table. The selection is constrained to users associated with the RPEAS system.  Furthermore, the selection is filtered to include only active users.  The selection is further restricted to exclude users where the user identifier is present in the EAS_Form_Approve_Lvl table, specifically those linked to the provided form GUID. The results are then ordered alphabetically by user name.

### Data Interactions
* **Reads:** EAS_USER, EAS_Form_Approve_Lvl
* **Writes:** None