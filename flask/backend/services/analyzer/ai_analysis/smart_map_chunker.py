import json
import os
from collections import defaultdict

# --- CONFIGURATION ---
INPUT_FILE = os.path.join(os.path.expanduser("~"), "Documents", "all_analysis_results1.json")
OUTPUT_DIR = 'smart_chunks'
MAX_CHARS_PER_CHUNK = 25000  # Conservative limit for local AI (approx 6-7k tokens)

# --- HELPER FUNCTIONS ---
def get_file_name(item):
    """Robustly find the filename."""
    if "file" in item and item["file"]: return item["file"]
    if "fileName" in item and item["fileName"]: return item["fileName"]
    if "ir" in item:
        if "path" in item["ir"] and item["ir"]["path"]: return item["ir"]["path"]
        if "file" in item["ir"] and item["ir"]["file"]: return item["ir"]["file"]
    return "Unknown_File"

def get_namespace(item):
    """Extract namespace to determine which group this file belongs to."""
    if "namespaces" in item and item["namespaces"] and len(item["namespaces"]) > 0:
        return item["namespaces"][0]
    elif "ir" in item and "namespaces" in item["ir"] and item["ir"]["namespaces"] and len(item["ir"]["namespaces"]) > 0:
        return item["ir"]["namespaces"][0]
    return "Miscellaneous" # Fallback for files without a namespace

def has_classes(item):
    """Check if the file actually contains code classes (filters out empty views)."""
    if "classes" in item and item["classes"]: return True
    if "ir" in item and "types" in item["ir"] and item["ir"]["types"]: return True
    return False

# --- MAIN SCRIPT ---
def main():
    print(f"Reading {INPUT_FILE}...")
    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error: {e}")
        return

    # 1. GROUPING PHASE
    print("Grouping files by Namespace...")
    groups = defaultdict(list)
    
    for item in data:
        # Filter out noise (files with no classes)
        if not has_classes(item):
            continue
            
        ns = get_namespace(item)
        groups[ns].append(item)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # 2. CHUNKING PHASE
    map_lines = ["PROJECT NAVIGATION MAP", "======================"]
    
    for ns, items in groups.items():
        # Sanitize namespace for filename
        safe_ns = ns.replace('.', '_')
        
        current_chunk = []
        current_chars = 0
        part_counter = 1
        
        # Sort items by filename within the namespace for consistency
        items.sort(key=lambda x: get_file_name(x))

        for item in items:
            item_str = json.dumps(item)
            item_size = len(item_str)
            
            # If this single item is massive, we must add it alone (rare case)
            if item_size > MAX_CHARS_PER_CHUNK and not current_chunk:
                current_chunk.append(item)
                # Force save
            
            # Check if full
            elif (current_chars + item_size > MAX_CHARS_PER_CHUNK) and current_chunk:
                # Save current chunk
                filename = f"{safe_ns}_Part{part_counter}.json"
                path = os.path.join(OUTPUT_DIR, filename)
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(current_chunk, f, indent=2)
                
                # Add to Map
                map_lines.append(f"\n[CHUNK: {filename}] (Namespace: {ns})")
                for c_item in current_chunk:
                    fname = get_file_name(c_item)
                    # Extract class names for the map
                    cls_names = [c.get('name', 'Unk') for c in c_item.get('classes', [])]
                    if not cls_names and 'ir' in c_item:
                        cls_names = [t.get('name', 'Unk') for t in c_item['ir'].get('types', [])]
                    map_lines.append(f"  - {fname} [{', '.join(cls_names)}]")

                # Reset
                part_counter += 1
                current_chunk = [item]
                current_chars = item_size
            else:
                current_chunk.append(item)
                current_chars += item_size

        # Save remaining items
        if current_chunk:
            suffix = f"_Part{part_counter}" if part_counter > 1 else ""
            filename = f"{safe_ns}{suffix}.json"
            path = os.path.join(OUTPUT_DIR, filename)
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(current_chunk, f, indent=2)
            
            map_lines.append(f"\n[CHUNK: {filename}] (Namespace: {ns})")
            for c_item in current_chunk:
                fname = get_file_name(c_item)
                cls_names = [c.get('name', 'Unk') for c in c_item.get('classes', [])]
                if not cls_names and 'ir' in c_item:
                    cls_names = [t.get('name', 'Unk') for t in c_item['ir'].get('types', [])]
                map_lines.append(f"  - {fname} [{', '.join(cls_names)}]")

    # 3. SAVE MAP
    with open(os.path.join(OUTPUT_DIR, "master_map.txt"), 'w', encoding='utf-8') as f:
        f.write("\n".join(map_lines))

    print(f"\nDone! Processed {len(groups)} namespaces.")
    print(f"Output saved to folder: '{OUTPUT_DIR}'")
    print(f"Check '{OUTPUT_DIR}/master_map.txt' to navigate your code.")

if __name__ == "__main__":
    main()