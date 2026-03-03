# Procedure: EAS_Admin_GET_Users

### Purpose
This procedure retrieves user records from the EAS_User table based on specified search criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @LanID | VARCHAR(50) | User identifier; if null, ignores this field in the search. |
| @NAME | VARCHAR(200) | User name; performs a partial match using the LIKE operator.  If null, ignores this field in the search. |
| @BArea | VARCHAR(150) | Business area; performs a partial match using the LIKE operator. If null, ignores this field in the search. |
| @Dept | VARCHAR(250) | Department; performs a partial match using the LIKE operator. If null, ignores this field in the search. |
| @Section | VARCHAR(250) | Section; performs a partial match using the LIKE operator. If null, ignores this field in the search. |
| @Designation | VARCHAR(500) | Job title; performs a partial match using the LIKE operator. If null, ignores this field in the search. |
| @Active | VARCHAR(10) | User status; if 'True', returns active users; if 'False', returns inactive users. If null, ignores this field in the search. |

### Logic Flow
The procedure searches the EAS_User table for user records. The search is performed based on multiple criteria, allowing for partial matches using the LIKE operator. The search is performed on the Name, Department, BusinessArea, Designation, and Section fields. The search is case-insensitive. The search prioritizes matching the UserID field if a @LanID is provided. If no @LanID is provided, the search ignores this field. The search also considers the @Active field, returning active users if the value is 'True' or 'False' and ignores this field if the value is null. The results are ordered by the CreatedOn field in descending order.

### Data Interactions
* **Reads:** EAS_User
* **Writes:** None