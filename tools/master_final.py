"""
Task 1: Extract main_pyqt_v3 - subprocess isolation for each function.
Task 2: Extract metadata from 9 crashing functions.
Combined into one script for efficiency.
"""
import sys, os, marshal, types, subprocess, json

EXT = r"C:\Users\1\Downloads\Telegram Desktop\6hzsv2.23.exe_extracted"
OUT = r"C:\Users\1\Downloads\Telegram Desktop\decrypted"
os.makedirs(OUT, exist_ok=True)
PYTHON = r"C:\Users\1\AppData\Local\Programs\Python\Python313\python.exe"
HDR = b'\xF3\x0D\x0D\x0A' + b'\x00' * 12

# === Worker script ===
WORKER = os.path.join(os.path.dirname(__file__), 'extract_worker.py')
with open(WORKER, 'w') as f:
    f.write("""import sys, os, marshal, types, json
EXT = sys.argv[1]; OUT = sys.argv[2]; MOD = sys.argv[3]; FUNC = sys.argv[4]; KIND = sys.argv[5]
HDR = b'\\xf3\\x0d\\x0d\\x0a' + b'\\x00' * 12
sys.path.insert(0, EXT)
import pyarmor_runtime_011372
sys.modules.pop(MOD, None)
mod = __import__(MOD)

if KIND == 'func':
    attr = getattr(mod, FUNC)
else:  # class method
    clsname, mname = FUNC.split('.', 1)
    cls = getattr(mod, clsname)
    attr = getattr(cls, mname)

co = attr.__code__

# Try to marshal
try:
    def clean(co):
        nc = []
        for c in co.co_consts:
            if isinstance(c, (types.BuiltinFunctionType, types.BuiltinMethodType)): nc.append(None)
            elif isinstance(c, types.CodeType): nc.append(clean(c))
            elif isinstance(c, tuple):
                r = list(c)
                for j in range(len(r)):
                    if isinstance(r[j], (types.BuiltinFunctionType, types.BuiltinMethodType)): r[j] = None
                    elif isinstance(r[j], types.CodeType): r[j] = clean(r[j])
                nc.append(tuple(r))
            else:
                try: marshal.dumps(c); nc.append(c)
                except: nc.append(None)
        return co.replace(co_consts=tuple(nc))
    
    cc = clean(co)
    raw = marshal.dumps(cc)
    safe = f"{MOD}__{FUNC.replace('.','_')}"
    with open(os.path.join(OUT, safe + '.pyc'), 'wb') as fh:
        fh.write(HDR + raw)
    print(f"PYC:{len(raw)}")
except:
    # Save metadata
    meta = {
        'name': co.co_name, 'filename': co.co_filename,
        'argcount': co.co_argcount, 'nlocals': co.co_nlocals,
        'stacksize': co.co_stacksize, 'flags': co.co_flags,
        'names': list(co.co_names), 'varnames': list(co.co_varnames),
        'cellvars': list(co.co_cellvars), 'freevars': list(co.co_freevars),
        'consts': []
    }
    for c in co.co_consts:
        if isinstance(c, str): meta['consts'].append({'type': 'str', 'value': c})
        elif isinstance(c, (int, float)): meta['consts'].append({'type': type(c).__name__, 'value': c})
        elif c is None: meta['consts'].append({'type': 'None', 'value': None})
        elif isinstance(c, bytes): meta['consts'].append({'type': 'bytes', 'len': len(c), 'hex': c[:64].hex()})
        elif isinstance(c, (types.BuiltinFunctionType, types.BuiltinMethodType)): meta['consts'].append({'type': 'builtin', 'repr': repr(c)[:100]})
        elif isinstance(c, types.CodeType): meta['consts'].append({'type': 'code', 'name': c.co_name})
        elif isinstance(c, tuple): meta['consts'].append({'type': 'tuple', 'len': len(c)})
        else: meta['consts'].append({'type': type(c).__name__})
    
    safe = f"{MOD}__{FUNC.replace('.','_')}"
    with open(os.path.join(OUT, safe + '_meta.json'), 'w', encoding='utf-8') as fh:
        json.dump(meta, fh, indent=2, ensure_ascii=False)
    print(f"META:ok")
""")

print(f"Worker: {WORKER}")

# === Enumerate all functions from all modules ===
sys.path.insert(0, EXT)
import pyarmor_runtime_011372

TARGETS = [
    ('main_pyqt_v3', '<frozen main_pyqt_v3>'),
    ('security', '<frozen security>'),
    ('activation', '<frozen activation>'),
    ('automation', '<frozen automation>'),
    ('web_server', '<frozen web_server>'),
]

all_jobs = []  # (mod_name, func_name, kind)

for mod_name, frozen_tag in TARGETS:
    sys.modules.pop(mod_name, None)
    try:
        mod = __import__(mod_name)
    except Exception as e:
        print(f"SKIP {mod_name}: import error {e}")
        continue
    
    count = 0
    for aname in sorted(dir(mod)):
        if aname.startswith('_'):
            continue
        
        try:
            attr = getattr(mod, aname)
        except:
            continue
        
        if isinstance(attr, types.ModuleType):
            continue
        
        # Function
        if hasattr(attr, '__code__'):
            try:
                co = attr.__code__
                if frozen_tag in co.co_filename:
                    all_jobs.append((mod_name, aname, 'func'))
                    count += 1
            except:
                pass
            continue
        
        # Class - enumerate methods
        if isinstance(attr, type):
            for mname in sorted(dir(attr)):
                if mname.startswith('__') and mname.endswith('__'):
                    continue
                try:
                    method = getattr(attr, mname)
                except:
                    continue
                if hasattr(method, '__code__'):
                    try:
                        co = method.__code__
                        if frozen_tag in co.co_filename:
                            all_jobs.append((mod_name, f"{aname}.{mname}", 'method'))
                            count += 1
                    except:
                        pass
    
    print(f"{mod_name}: {count} items")

print(f"\nTotal jobs: {len(all_jobs)}")

# === Process each in subprocess ===
results = {'pyc': [], 'meta': [], 'fail': []}

for i, (mod_name, func_name, kind) in enumerate(all_jobs):
    label = f"{mod_name}.{func_name}"
    print(f"[{i+1}/{len(all_jobs)}] {label}", end=' ', flush=True)
    
    try:
        proc = subprocess.run(
            [PYTHON, WORKER, EXT, OUT, mod_name, func_name, kind],
            capture_output=True, text=True, timeout=60
        )
        out = proc.stdout.strip()
        if proc.returncode == 0:
            if out.startswith('PYC:'):
                size = out.split(':')[1]
                print(f"PYC {size}B")
                results['pyc'].append(label)
            elif out.startswith('META:'):
                print(f"META")
                results['meta'].append(label)
            else:
                print(f"UNKNOWN: {out[:80]}")
                results['fail'].append(label)
        else:
            print(f"FAIL rc={proc.returncode} {proc.stderr[:80]}")
            results['fail'].append(label)
    except subprocess.TimeoutExpired:
        proc.kill()
        print(f"TIMEOUT")
        results['fail'].append(label)
    except Exception as e:
        print(f"ERR: {e}")
        results['fail'].append(label)

# === Summary ===
print(f"\n{'='*60}")
print(f"PYC saved: {len(results['pyc'])}")
for n in results['pyc']:
    print(f"  {n}")
print(f"\nMetadata saved: {len(results['meta'])}")
for n in results['meta']:
    print(f"  {n}")
print(f"\nFailed: {len(results['fail'])}")
for n in results['fail']:
    print(f"  {n}")

with open(os.path.join(OUT, '_all_results.json'), 'w') as f:
    json.dump(results, f, indent=2)

# === Count output files ===
pyc_files = [f for f in os.listdir(OUT) if f.endswith('.pyc')]
meta_files = [f for f in os.listdir(OUT) if f.endswith('_meta.json')]
print(f"\nOutput: {len(pyc_files)} .pyc + {len(meta_files)} meta files")
print(f"{'='*60}")
