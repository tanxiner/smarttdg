1. **sp_TAMS_Applicant_List_Child_OnLoad**

   This stored procedure retrieves a list of applicants based on various filters such as line, track type, access date range, and sector ID.

   The logic flow:
   1. Checks if user exists.
   2. Inserts into Audit table.
   3. Returns ID.

   Data Interactions:
   * Reads: TAMS_Sector, TAMS_TAR, TAMS_WFStatus
   * Writes: None

2. **sp_TAMS_Applicant_List_Child_OnLoad_20220303**

   This stored procedure is identical to the previous one, with no changes.

3. **sp_TAMS_Applicant_List_Child_OnLoad_20220303_M**

   This stored procedure is also identical to the previous two, with no changes.

4. **sp_TAMS_Applicant_List_Child_OnLoad_Hnin**

   This stored procedure retrieves a list of applicants based on various filters such as line, track type, access date range, and sector ID.

   The logic flow:
   1. Checks if user exists.
   2. Inserts into Audit table.
   3. Returns ID.

   Data Interactions:
   * Reads: TAMS_Sector, TAMS_TAR, TAMS_WFStatus
   * Writes: None

Tables used:

* TAMS_Sector
* TAMS_TAR
* TAMS_WFStatus