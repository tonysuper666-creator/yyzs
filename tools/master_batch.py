"""
Master script - one subprocess per module using batch worker.
Phase 1 saves all metadata. Phase 2 tries marshal (may crash but metadata is safe).
"""
import sys, os, subprocess, json, types, time

EXT = r"C:\Users\1\Downloads\Telegram Desktop\6hzsv2.23.exe_extracted"
OUT = r"C:\Users\1\Downloads\Telegram Desktop\decrypted"
os.makedirs(OUT, exist_ok=True)
PYTHON = r"C:\Users\1\AppData\Local\Programs\Python\Python313\python.exe"
BATCH_WORKER = r"C:\Users\1\AppData\Local\Temp\opencode\batch_worker.py"

def safe_has_code(attr):
    try: return hasattr(attr, '__code__')
    except: return False

# === Enumerate all ===
sys.path.insert(0, EXT)
import pyarmor_runtime_011372

TARGETS = [
    ('main_pyqt_v3', '<frozen main_pyqt_v3>'),
    ('security', '<frozen security>'),
    ('activation', '<frozen activation>'),
    ('automation', '<frozen automation>'),
    ('web_server', '<frozen web_server>'),
]

all_manifests = {}

for mod_name, frozen_tag in TARGETS:
    print(f"Enumerating {mod_name}...", flush=True)
    sys.modules.pop(mod_name, None)
    
    try:
        mod = __import__(mod_name)
    except Exception as e:
        print(f"  IMPORT FAILED: {e}")
        continue
    
    items = []
    
    for aname in sorted(dir(mod)):
        if aname.startswith('_'):
            continue
        try:
            attr = getattr(mod, aname)
        except:
            continue
        if isinstance(attr, types.ModuleType):
            continue
        
        if safe_has_code(attr):
            try:
                co = attr.__code__
                if frozen_tag in co.co_filename:
                    items.append((aname, 'func'))
            except:
                pass
            continue
        
        if isinstance(attr, type):
            for mname in sorted(dir(attr)):
                if mname.startswith('__') and mname.endswith('__'):
                    continue
                try:
                    method = getattr(attr, mname)
                except:
                    continue
                if safe_has_code(method):
                    try:
                        co = method.__code__
                        if frozen_tag in co.co_filename:
                            items.append((f"{aname}.{mname}", 'method'))
                    except:
                        pass
    
    print(f"  => {len(items)} items", flush=True)
    all_manifests[mod_name] = items

# === Process each module in a batch subprocess ===
all_results = {}

for mod_name, items in all_manifests.items():
    if not items:
        print(f"\n[{mod_name}] No items, skipping", flush=True)
        continue
    
    print(f"\n{'='*60}")
    print(f"[{mod_name}] {len(items)} items")
    print(f"{'='*60}", flush=True)
    
    # Write manifest
    manifest_path = os.path.join(OUT, f"_manifest_{mod_name}.json")
    with open(manifest_path, 'w') as f:
        json.dump(items, f)
    
    # Spawn batch worker
    t0 = time.time()
    try:
        proc = subprocess.run(
            [PYTHON, BATCH_WORKER, EXT, OUT, mod_name, manifest_path],
            capture_output=True, text=True, timeout=600
        )
        dt = time.time() - t0
        
        # Parse output
        meta_count = 0
        pyc_count = 0
        
        for line in proc.stdout.split('\n'):
            line = line.strip()
            if line.startswith('META:') and ':OK' not in line and '_ERR' not in line:
                meta_count += 1
            elif line.startswith('PYC:') and 'SKIP' not in line and '_ERR' not in line:
                pyc_count += 1
        
        print(f"  Metadata saved: {meta_count}")
        print(f"  PYC saved: {pyc_count}")
        print(f"  Time: {dt:.1f}s")
        
        if proc.returncode != 0 and proc.returncode != -1073741819:
            print(f"  Exit: {proc.returncode}")
            # Print last stderr
            err_lines = [l for l in proc.stderr.split('\n') if l.strip()][-3:]
            for el in err_lines:
                print(f"  ERR: {el[:120]}")
        
        all_results[mod_name] = {
            'items': len(items),
            'meta': meta_count,
            'pyc': pyc_count,
            'exit': proc.returncode,
            'time': dt,
        }
        
    except subprocess.TimeoutExpired:
        proc.kill()
        print(f"  TIMEOUT after 600s")
        all_results[mod_name] = {'items': len(items), 'timeout': True}

# === Final summary ===
print(f"\n{'='*60}")
print("FINAL SUMMARY")
print(f"{'='*60}")

total_pyc = len([f for f in os.listdir(OUT) if f.endswith('.pyc')])
total_meta = len([f for f in os.listdir(OUT) if f.endswith('_meta.json')])

for mod_name, info in all_results.items():
    n = info.get('items', 0)
    m = info.get('meta', 0)
    p = info.get('pyc', 0)
    t = info.get('time', 0)
    e = info.get('exit', '?')
    print(f"  {mod_name}: {n} items, {m} meta, {p} pyc, {t:.1f}s, exit={e}")

print(f"\nTotal output: {total_pyc} .pyc + {total_meta} meta files")
print(f"Output dir: {OUT}")
