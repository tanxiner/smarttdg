**Procedure: sp_TAMS_OCC_UpdateOCCAuthorisationTCByParameters**

Purpose:
This stored procedure updates the OCC authorization status of a TVF acknowledgement based on the provided parameters.

Logic Flow:
1. Checks if user exists.
2. Inserts into Audit table.
3. Returns ID.

Data Interactions:
* Reads: [TAMS_Workflow], [TAMS_Endorser], [TAMS_OCC_Auth_Workflow], [TAMS_OCC_Auth]
* Writes: [TAMS_OCC_Auth_Workflow_Audit]

**Procedure: sp_TAMS_OCC_UpdateTVFAckByParameters_CC**

Purpose:
This stored procedure updates the TVF acknowledgement status based on the provided parameters.

Logic Flow:
1. Updates TAMS_TVF_Acknowledge table with new values.
2. Inserts into Audit table.

Data Interactions:
* Reads: [TAMS_TVF_Acknowledge]
* Writes: [TAMS_TVF_Acknowledge_Audit]

**Procedure: sp_TAMS_OCC_UpdateTVFAckByParameters_PFR**

Purpose:
This stored procedure updates the TVF acknowledgement status based on the provided parameters.

Logic Flow:
1. Updates TAMS_TVF_Acknowledge table with new values.
2. Inserts into Audit table.

Data Interactions:
* Reads: [TAMS_TVF_Acknowledge]
* Writes: [TAMS_TVF_Acknowledge_Audit]

Tables used:

* [TAMS_Workflow]
* [TAMS_Endorser]
* [TAMS_OCC_Auth_Workflow]
* [TAMS_OCC_Auth]
* [TAMS_TVF_Acknowledge]
* [TAMS_TVF_Acknowledge_Audit]