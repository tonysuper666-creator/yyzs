"""Batch worker - processes ALL functions from ONE module in a single subprocess."""
import sys, os, marshal, types, json
EXT = sys.argv[1]; OUT = sys.argv[2]; MOD = sys.argv[3]
MANIFEST = sys.argv[4]  # JSON file with list of [func_name, kind]

HDR = b'\xf3\x0d\x0d\x0a' + b'\x00' * 12
sys.path.insert(0, EXT)
import pyarmor_runtime_011372
sys.modules.pop(MOD, None)
mod = __import__(MOD)

with open(MANIFEST, 'r') as f:
    items = json.load(f)

def save_meta(aname, co, kind):
    """Save metadata JSON (safe, no co_code access)."""
    meta = {
        'module': MOD, 'func': aname, 'kind': kind,
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
        elif c is None: meta['consts'].append({'type': 'None'})
        elif isinstance(c, bytes): meta['consts'].append({'type': 'bytes', 'len': len(c)})
        elif isinstance(c, (types.BuiltinFunctionType, types.BuiltinMethodType)): meta['consts'].append({'type': 'builtin'})
        elif isinstance(c, types.CodeType): meta['consts'].append({'type': 'code', 'name': c.co_name})
        elif isinstance(c, tuple): meta['consts'].append({'type': 'tuple', 'len': len(c)})
        else: meta['consts'].append({'type': type(c).__name__})
    
    safe = f"{MOD}__{aname.replace('.','_')}"
    with open(os.path.join(OUT, safe + '_meta.json'), 'w', encoding='utf-8') as fh:
        json.dump(meta, fh, indent=2, ensure_ascii=False)
    return safe

def try_marshal(safe, co):
    """Try to marshal - may crash the process."""
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
    with open(os.path.join(OUT, safe + '.pyc'), 'wb') as fh:
        fh.write(HDR + raw)
    return len(raw)

# Phase 1: Save metadata for ALL functions (safe)
print(f"META_START:{len(items)}", flush=True)
for i, (func_name, kind) in enumerate(items):
    try:
        if kind == 'func':
            attr = getattr(mod, func_name)
        else:
            clsname, mname = func_name.split('.', 1)
            cls = getattr(mod, clsname)
            attr = getattr(cls, mname)
        co = attr.__code__
        save_meta(func_name, co, kind)
        print(f"META:{i}:{func_name}", flush=True)
    except Exception as e:
        print(f"META_ERR:{i}:{func_name}:{e}", flush=True)

# Phase 2: Try to marshal each (may crash, but metadata already saved)
print(f"PYC_START", flush=True)

# Use a checkpoint file to track which ones were tried
checkpoint = os.path.join(OUT, f"_checkpoint_{MOD}.txt")

for i, (func_name, kind) in enumerate(items):
    safe = f"{MOD}__{func_name.replace('.','_')}"
    
    # Skip if already processed
    if os.path.exists(os.path.join(OUT, safe + '.pyc')):
        print(f"PYC_SKIP:{i}:{func_name}", flush=True)
        continue
    
    try:
        if kind == 'func':
            attr = getattr(mod, func_name)
        else:
            clsname, mname = func_name.split('.', 1)
            cls = getattr(mod, clsname)
            attr = getattr(cls, mname)
        co = attr.__code__
        size = try_marshal(safe, co)
        print(f"PYC:{i}:{func_name}:{size}", flush=True)
        
        # Save checkpoint
        with open(checkpoint, 'a') as f:
            f.write(f"{func_name}\n")
    except Exception as e:
        print(f"PYC_ERR:{i}:{func_name}:{e}", flush=True)

print(f"DONE", flush=True)
