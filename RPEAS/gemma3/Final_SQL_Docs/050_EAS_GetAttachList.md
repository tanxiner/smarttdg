# Procedure: EAS_GetAttachList

### Purpose
This procedure retrieves a list of attachments associated with forms, including file identifiers, names, paths, content types, and constructed file paths.

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | N/A | No input parameters are used. |

### Logic Flow
1.  The procedure begins by selecting data from the `EAS_Form_Attach_Document` table, aliased as `a`, and the `EAS_Form_Master` table, aliased as `b`.
2.  It filters the `EAS_Form_Attach_Document` table to include only records where the `FileContent` column is null.
3.  The procedure joins the `EAS_Form_Attach_Document` table with the `EAS_Form_Master` table using the `FormGuid` column, linking attachments to their corresponding forms.
4.  It constructs a `FilePath` column by concatenating a fixed string with the substring of the `FileURL` column, up to the first forward slash.
5.  It constructs a `FileURL` column by removing the "https://apps.sbstransit.com.sg/RPEAS_Document/" prefix from the `FileURL` column.
6.  The selected data is then ordered by the `FILE_ID` column.
7.  The final result set contains the `FileRefNo`, `FILE_ID`, `FILE_NAME`, `FILE_PATH`, `FILE_CONTENT`, `CONT_TYPE`, and the calculated `FilePath` columns.

### Data Interactions
* **Reads:** `EAS_Form_Attach_Document`, `EAS_Form_Master`
* **Writes:** None