"""
Simple PyArmor code extraction - import modules and dump all accessible code objects.
"""
import sys
import os
import marshal
import types
import json

EXTRACT_DIR = r"C:\Users\1\Downloads\Telegram Desktop\6hzsv2.23.exe_extracted"
OUTPUT_DIR = r"C:\Users\1\Downloads\Telegram Desktop\decrypted"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sys.path.insert(0, EXTRACT_DIR)

PYC_MAGIC = b'\xF3\x0D\x0D\x0A'
PYC_HEADER = PYC_MAGIC + b'\x00\x00\x00\x00' + b'\x00' * 8

print("[+] Importing PyArmor runtime...")
import pyarmor_runtime_011372
print("    OK")

# Step 1: Extract code objects from a module  
def get_all_code_objects(mod, prefix):
    """Get all code objects from a module's contents."""
    results = []
    seen = set()
    
    def extract(obj, name, depth=0):
        if depth > 4 or id(obj) in seen:
            return
        seen.add(id(obj))
        
        # Direct code object
        if hasattr(obj, '__code__'):
            co = obj.__code__
            results.append((name, co))
            # Check nested code objects in constants
            for i, const in enumerate(co.co_consts):
                if hasattr(const, '__code__'):
                    extract(const, f"{name}.{const.co_name}", depth+1)
        
        # Class - inspect methods
        if isinstance(obj, type):
            for attr_name in dir(obj):
                try:
                    attr = getattr(obj, attr_name)
                    if callable(attr) and hasattr(attr, '__code__'):
                        extract(attr, f"{name}.{attr_name}", depth+1)
                except:
                    pass
        
        # Module - inspect top-level
        if isinstance(obj, types.ModuleType):
            for attr_name in dir(obj):
                if attr_name.startswith('__') and attr_name.endswith('__'):
                    continue
                try:
                    attr = getattr(obj, attr_name)
                    extract(attr, f"{name}.{attr_name}", depth+1)
                except:
                    pass
    
    # Top-level: inspect module's __dict__
    for attr_name, attr_val in list(mod.__dict__.items()):
        if attr_name.startswith('__'):
            continue
        try:
            extract(attr_val, f"{prefix}.{attr_name}", depth=0)
        except Exception as e:
            print(f"    [!] Error extracting {attr_name}: {e}")
    
    return results

# Step 2: Import and extract
PROTECTED_MODULES = ['main_pyqt_v3', 'web_server', 'automation', 'security', 'activation']
all_code = {}
all_info = {}

for mod_name in PROTECTED_MODULES:
    print(f"\n[+] Loading: {mod_name}")
    
    # Clear cache
    sys.modules.pop(mod_name, None)
    
    try:
        mod = __import__(mod_name)
        print(f"    Module: {mod.__file__}")
        
        # List attributes
        attrs = [a for a in dir(mod) if not a.startswith('_')]
        print(f"    Public attributes: {len(attrs)}")
        for a in attrs[:10]:
            obj = getattr(mod, a)
            t = type(obj).__name__
            s = ""
            if hasattr(obj, '__code__'):
                s = f" (function, {len(obj.__code__.co_code)} bytes)"
            elif isinstance(obj, type):
                s = f" (class, {len([m for m in dir(obj) if not m.startswith('_')])} methods)"
            elif isinstance(obj, str) and len(obj) < 120:
                s = f" = \"{obj}\""
            elif isinstance(obj, (int, float, bool)):
                s = f" = {obj}"
            print(f"      {a}: {t}{s}")
        
        # Extract code objects
        code_objects = get_all_code_objects(mod, mod_name)
        print(f"    Code objects found: {len(code_objects)}")
        
        for name, co in code_objects:
            safe_name = name.replace('.', '_').replace('<', '').replace('>', '').replace(' ', '_')
            if len(safe_name) > 200:
                safe_name = safe_name[:200]
            code_bytes = marshal.dumps(co)
            pyc_out = os.path.join(OUTPUT_DIR, f"{safe_name}.pyc")
            with open(pyc_out, 'wb') as f:
                f.write(PYC_HEADER + code_bytes)
            all_code[name] = {'path': pyc_out, 'size': len(code_bytes)}
            print(f"      Saved: {safe_name}.pyc ({len(code_bytes)} bytes)")
        
        # Save attributes info
        all_info[mod_name] = {
            'file': mod.__file__,
            'attributes': attrs,
            'code_objects': list(all_code.keys()),
        }
        
    except Exception as e:
        print(f"    [!] Failed to import {mod_name}: {e}")
        import traceback
        traceback.print_exc()

# Save info
info_path = os.path.join(OUTPUT_DIR, 'extraction_info.json')
with open(info_path, 'w', encoding='utf-8') as f:
    json.dump(all_info, f, indent=2, ensure_ascii=False)

print(f"\n{'='*60}")
print(f"Extraction complete: {len(all_code)} code objects")
print(f"Output: {OUTPUT_DIR}")
print(f"Info: {info_path}")
print(f"{'='*60}")
