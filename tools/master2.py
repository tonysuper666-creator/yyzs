"""
Master script v2 - robust enumeration, subprocess isolation for each function.
"""
import sys, os, subprocess, json, types

EXT = r"C:\Users\1\Downloads\Telegram Desktop\6hzsv2.23.exe_extracted"
OUT = r"C:\Users\1\Downloads\Telegram Desktop\decrypted"
os.makedirs(OUT, exist_ok=True)

WORKER = os.path.join(os.path.dirname(__file__), 'worker.py')
PYTHON = r"C:\Users\1\AppData\Local\Programs\Python\Python313\python.exe"

# Worker script
with open(WORKER, 'w') as f:
    f.write("""import sys, os, marshal, types
EXT = sys.argv[1]
OUT = sys.argv[2]
MOD = sys.argv[3]
FUNC = sys.argv[4]
HDR = b'\\xf3\\x0d\\x0d\\x0a' + b'\\x00' * 12
sys.path.insert(0, EXT)
import pyarmor_runtime_011372
sys.modules.pop(MOD, None)
mod = __import__(MOD)
attr = getattr(mod, FUNC)
co = attr.__code__

def clean_co(co):
    nc = []
    for c in co.co_consts:
        if isinstance(c, (types.BuiltinFunctionType, types.BuiltinMethodType)):
            nc.append(None)
        elif isinstance(c, types.CodeType):
            nc.append(clean_co(c))
        elif isinstance(c, tuple):
            nc.append(tuple(_ch(c)))
        else:
            try: marshal.dumps(c); nc.append(c)
            except: nc.append(None)
    return co.replace(co_consts=tuple(nc))

def _ch(data):
    r = []
    for c in data:
        if isinstance(c, (types.BuiltinFunctionType, types.BuiltinMethodType)):
            r.append(None)
        elif isinstance(c, types.CodeType):
            r.append(clean_co(c))
        elif isinstance(c, tuple):
            r.append(tuple(_ch(c)))
        else:
            try: marshal.dumps(c); r.append(c)
            except: r.append(None)
    return r

cc = clean_co(co)
raw = marshal.dumps(cc)
path = os.path.join(OUT, f"{MOD}__{FUNC}.pyc")
with open(path, 'wb') as fh:
    fh.write(HDR + raw)
print(f"OK:{len(raw)}")
""")

print(f"Worker: {WORKER}")

# Enumerate all functions
sys.path.insert(0, EXT)
import pyarmor_runtime_011372

TARGETS = [
    ('security', '<frozen security>'),
    ('activation', '<frozen activation>'),
    ('automation', '<frozen automation>'),
    ('web_server', '<frozen web_server>'),
]

all_funcs = []

for mod_name, frozen_tag in TARGETS:
    sys.modules.pop(mod_name, None)
    try:
        mod = __import__(mod_name)
    except Exception as e:
        print(f"SKIP {mod_name}: import failed: {e}")
        continue
    
    count = 0
    for aname in sorted(dir(mod)):
        if aname.startswith('_'):
            continue
        
        try:
            attr = getattr(mod, aname)
        except Exception:
            continue
        
        # Werkzeug LocalProxy can trigger "Working outside of request context"
        try:
            has_code = hasattr(attr, '__code__')
        except RuntimeError:
            continue
        except Exception:
            continue
        
        if not has_code:
            continue
        
        try:
            co = attr.__code__
        except:
            continue
        
        if frozen_tag in co.co_filename:
            all_funcs.append((mod_name, aname))
            count += 1
    
    print(f"{mod_name}: {count} functions")

print(f"\nTotal: {len(all_funcs)} functions")

# Process each in subprocess
results = {'ok': [], 'fail': []}

for i, (mod_name, func_name) in enumerate(all_funcs):
    print(f"[{i+1}/{len(all_funcs)}] {mod_name}.{func_name}...", end=' ', flush=True)
    
    try:
        proc = subprocess.run(
            [PYTHON, WORKER, EXT, OUT, mod_name, func_name],
            capture_output=True, text=True, timeout=30
        )
        if proc.returncode == 0 and 'OK:' in proc.stdout:
            size = proc.stdout.strip().split(':')[1].strip()
            print(f"OK ({size}B)")
            results['ok'].append((mod_name, func_name, size))
        else:
            rc = proc.returncode
            err = proc.stderr[:150].replace('\n', ' ') if proc.stderr else ''
            out = proc.stdout[:100] if proc.stdout else ''
            print(f"FAIL rc={rc} {err} {out}")
            results['fail'].append((mod_name, func_name, f"rc={rc}"))
    except subprocess.TimeoutExpired:
        proc.kill()
        print(f"TIMEOUT")
        results['fail'].append((mod_name, func_name, "timeout"))
    except Exception as e:
        print(f"ERROR: {e}")
        results['fail'].append((mod_name, func_name, str(e)))

# Final summary
print(f"\n{'='*60}")
print(f"SUCCESS: {len(results['ok'])}")
for m, f, s in results['ok']:
    print(f"  {m}.{f}: {s}B")
print(f"\nFAILED: {len(results['fail'])}")
for m, f, r in results['fail']:
    print(f"  {m}.{f}: {r}")
print(f"{'='*60}")

with open(os.path.join(OUT, 'results.json'), 'w') as f:
    json.dump(results, f, indent=2)
