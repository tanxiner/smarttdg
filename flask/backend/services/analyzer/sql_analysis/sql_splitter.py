import os
import re
import chardet 

# --- CONFIGURATION ---
INPUT_SQL_FILE = os.path.join(os.path.expanduser("~"), "Documents", "script.sql") 
OUTPUT_DIR = 'SQL_Documentation_Prompts'

# --- TEMPLATE ---
TEMPLATE = """
### SYSTEM ROLE
You are a **Senior Database Architect**.
You are NOT a Coder. You DO NOT write SQL code.

### OBJECTIVE
Document the logic of the Stored Procedure provided below.

### 🛑 STRICT CONSTRAINTS
1. **NO SQL CODE BLOCKS.** Do not rewrite the procedure code.
2. **NO** "Here is the documentation" filler.
3. **NO** generic explanations.
4. **DO NOT EXPAND ACRONYMS.**
   (Treat these as proper nouns: [{ACRONYM_LIST}])

### ✅ REQUIRED OUTPUT FORMAT
Output exactly this structure:

# Procedure: {ProcedureName}

### Purpose
{One clear sentence explaining what business task this performs.}

### Parameters
| Name | Type | Purpose |
| :--- | :--- | :--- |
| @ParamName | DataType | {Inferred usage} |

### Logic Flow
{Step-by-step plain English explanation.}

### Data Interactions
* **Reads:** {List tables explicitly selected from}
* **Writes:** {List tables inserted/updated/deleted}

---

### ⬇️ RAW SQL INPUT ⬇️
{code_chunk}

### ⬆️ END OF INPUT ⬆️
**INSTRUCTION:** Document the logic above in English.
"""

# --- HELPERS ---

def detect_encoding(file_path):
    try:
        with open(file_path, 'rb') as f:
            raw = f.read(50000)
        return chardet.detect(raw)['encoding'] or 'utf-8'
    except:
        return 'latin-1'

def get_dynamic_acronyms(text):
    """Scans for UPPERCASE words to protect them from expansion."""
    exclude = {
        # Standard SQL Commands & Keywords
        "ADD", "ALL", "ALTER", "AND", "ANY", "AS", "ASC", "BACKUP", "BEGIN", "BETWEEN", "BREAK", "BULK", "BY", 
        "CASE", "CATCH", "CHECK", "CHECKPOINT", "CLOSE", "COALESCE", "COLUMN", "COMMIT", "COMPUTE", "CONSTRAINT", "CONTAINS", 
        "CONTINUE", "CONVERT", "CREATE", "CROSS", "CURRENT", "CURSOR", "DATABASE", "DBCC", "DEALLOCATE", "DECLARE", 
        "DEFAULT", "DELETE", "DENY", "DESC", "DISTINCT", "DISTRIBUTED", "DOUBLE", "DROP", "ELSE", "END", "ERRLVL", 
        "ESCAPE", "EXCEPT", "EXEC", "EXECUTE", "EXISTS", "EXIT", "FETCH", "FILE", "FILLFACTOR", "FOR", "FOREIGN", 
        "FREETEXT", "FROM", "FULL", "FUNCTION", "GOTO", "GRANT", "GROUP", "HAVING", "HOLDLOCK", "IDENTITY", 
        "IDENTITY_INSERT", "IDENTITYCOL", "IF", "IN", "INDEX", "INNER", "INSERT", "INTERSECT", "INTO", "IS", "JOIN", 
        "KEY", "KILL", "LEFT", "LIKE", "LINENO", "LOAD", "MERGE", "NATIONAL", "NOCHECK", "NONCLUSTERED", "NOT", "NULL", 
        "NULLIF", "OF", "OFF", "OFFSETS", "ON", "OPEN", "OPENDATASOURCE", "OPENQUERY", "OPENROWSET", "OPENXML", "OPTION", 
        "OR", "ORDER", "OUTER", "OVER", "PERCENT", "PIVOT", "PLAN", "PRIMARY", "PRINT", "PROC", "PROCEDURE", "PUBLIC", 
        "RAISERROR", "READ", "READTEXT", "RECONFIGURE", "REFERENCES", "REPLICATION", "RESTORE", "RESTRICT", "RETURN", 
        "REVERT", "REVOKE", "RIGHT", "ROLLBACK", "ROWCOUNT", "ROWGUIDCOL", "RULE", "SAVE", "SCHEMA", "SELECT", "SET", 
        "SETUSER", "SHUTDOWN", "SOME", "STATISTICS", "SYS", "TABLE", "TEXTSIZE", "THEN", "TO", "TOP", "TRAN", "TRANSACTION", 
        "TRIGGER", "TRUNCATE", "TRY", "TSEQUAL", "TYPE", "UNION", "UNIQUE", "UNPIVOT", "UPDATE", "UPDATETEXT", "USE", "USER", "VALUES", 
        "VARYING", "VIEW", "WAITFOR", "WHEN", "WHERE", "WHILE", "WITH", "WRITETEXT", "XML",
        
        # Security & Context (Added OWNER, CALLER, SELF)
        "OWNER", "CALLER", "SELF", "GUEST", "MASTER",
        
        # Transaction Isolation Levels
        "ISOLATION", "LEVEL", "UNCOMMITTED", "COMMITTED", "REPEATABLE", "SERIALIZABLE", "SNAPSHOT",
        
        # String/Math/System Functions
        "LTRIM", "RTRIM", "TRIM", "UPPER", "LOWER", "LEN", "REPLACE", "SUBSTRING", "CHARINDEX", "LEFT", "RIGHT",
        "PATINDEX", "TEXTPTR", "DATALENGTH", "REPLICATE", "SPACE", "STR", "STUFF", "SPLIT",
        "MIN", "MAX", "SUM", "AVG", "COUNT", "ABS", "ROUND", "CEILING", "FLOOR",
        
        # Date & Time 
        "YEAR", "MONTH", "DAY", "DATEPART", "DATEDIFF", "DATEADD", "ISDATE",
        
        # Window Functions & Ranking
        "DENSE_RANK", "RANK", "ROW_NUMBER", "NTILE", "PARTITION",
        
        # Cursor & Flow
        "NEXT", "PRIOR", "FIRST", "LAST", "ABSOLUTE", "RELATIVE",
        
        # Data Types & Modifiers
        "INT", "INTEGER", "VARCHAR", "NVARCHAR", "CHAR", "NCHAR", "DATE", "DATETIME", "BIT", "DECIMAL", "NUMERIC", "FLOAT", "REAL",
        "MONEY", "SMALLINT", "TINYINT", "BIGINT", "OUTPUT", 
        
        # System Globals, Error Handling & Common Vars
        "ISNULL", "GETDATE", "OBJECT_ID", "NOCOUNT", "XACT_ABORT", "ANSI_NULLS", "QUOTED_IDENTIFIER", "SYSNAME", "CAST", 
        "COALESCE", "TRANCOUNT", "ERROR", "TRAP_ERROR", "SPID", "ERROR_MESSAGE", "ERROR_STATE", "ERROR_SEVERITY",
        "RES", "PATH"
    }
    candidates = re.findall(r'\b[A-Z0-9_]{2,10}\b', text)
    unique = sorted(list(set([w for w in candidates if not w.isdigit() and w not in exclude])))
    return ", ".join(f'"{a}"' for a in unique)

def extract_proc_name(proc_sql):
    pattern = r'CREATE\s+(?:OR\s+ALTER\s+)?(?:PROC|PROCEDURE)\s+(?:\[?\w+\]?\.?)?\[?([a-zA-Z0-9_]+)\]?'
    match = re.search(pattern, proc_sql, re.IGNORECASE)
    if match:
        return match.group(1)
    return "Unknown_Proc"

def sanitize_filename(name):
    """Removes illegal characters from filenames."""
    return re.sub(r'[\\/*?:"<>|]', "", name)

# --- READING LOGIC (YOUR CUSTOM CODE) ---

def read_procedures(file_path):
    print(f"Reading {file_path}...")
    encoding = detect_encoding(file_path)
    
    with open(file_path, "r", encoding=encoding, errors="replace") as f:
        lines = f.readlines()

    procedures = []
    current_proc = []
    in_proc = False

    for line in lines:
        if re.match(r'(?i)^\s*CREATE\s+(?:OR\s+ALTER\s+)?(?:PROC|PROCEDURE)\b', line):
            if in_proc: 
                procedures.append(''.join(current_proc).strip())
            
            in_proc = True
            current_proc = [line]
            continue

        if in_proc:
            if re.match(r'(?i)^\s*GO\s*$', line):
                procedures.append(''.join(current_proc).strip())
                current_proc = []
                in_proc = False
            else:
                current_proc.append(line)

    if current_proc:
        procedures.append(''.join(current_proc).strip())

    return procedures

# --- MAIN EXECUTION ---

def main():
    if not os.path.exists(INPUT_SQL_FILE):
        print(f"Error: '{INPUT_SQL_FILE}' not found.")
        return

    if not os.path.exists(OUTPUT_DIR): os.makedirs(OUTPUT_DIR)

    # 1. Read procedures
    procs = read_procedures(INPUT_SQL_FILE)
    print(f"Found {len(procs)} valid stored procedures.")

    if not procs:
        print("No procedures found.")
        return

    # 2. Iterate and Save INDIVIDUALLY
    for i, proc_code in enumerate(procs):
        
        # Get metadata
        proc_name = extract_proc_name(proc_code)
        acronyms = get_dynamic_acronyms(proc_code)
        
        # Create Filename: 001_ProcedureName.txt
        safe_name = sanitize_filename(proc_name)
        fname = f"{i+1:03d}_{safe_name}.txt"
        
        # Create Content
        final_content = TEMPLATE.replace("{ProcedureName}", proc_name) \
                                .replace("{ACRONYM_LIST}", acronyms) \
                                .replace("{code_chunk}", proc_code)
        
        # Write File
        with open(os.path.join(OUTPUT_DIR, fname), 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"Saved: {fname}")

    print(f"✅ Success! Created {len(procs)} separate files in '{OUTPUT_DIR}'.")

if __name__ == "__main__":
    main()