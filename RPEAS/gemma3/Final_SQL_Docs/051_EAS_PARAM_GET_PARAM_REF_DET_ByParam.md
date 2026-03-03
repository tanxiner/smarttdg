# Procedure: EAS_PARAM_GET_PARAM_REF_DET_ByParam

### Purpose
This procedure retrieves detailed reference information from the EAS_PARAM_REF_DET table based on specified parameter criteria.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @Param_Rec_Type | VARCHAR(50) |  Specifies the record type for the parameter reference. |
| @ParaType | VARCHAR(50) |  Identifies the parameter type. |
| @ParaCode | VARCHAR(50) |  Represents the parameter code. |

### Logic Flow
The procedure begins by selecting data from the EAS_PARAM_REF_DET table. The selection is filtered based on three criteria: the value of the @Param_Rec_Type parameter, the value of the @ParaType parameter, and the value of the @ParaCode parameter.  The results are ordered first by @Param_Rec_Type in ascending order, and then by the creation date in descending order within each @Param_Rec_Type group.

### Data Interactions
* **Reads:** dbo.EAS_PARAM_REF_DET
* **Writes:** None