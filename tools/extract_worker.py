"""Improved worker - save metadata FIRST, then try marshal."""
import sys, os, marshal, types, json
EXT = sys.argv[1]; OUT = sys.argv[2]; MOD = sys.argv[3]; FUNC = sys.argv[4]; KIND = sys.argv[5]
HDR = b'\xf3\x0d\x0d\x0a' + b'\x00' * 12
sys.path.insert(0, EXT)
import pyarmor_runtime_011372
sys.modules.pop(MOD, None)
mod = __import__(MOD)

if KIND == 'func':
    attr = getattr(mod, FUNC)
else:
    clsname, mname = FUNC.split('.', 1)
    cls = getattr(mod, clsname)
    attr = getattr(cls, mname)

co = attr.__code__

# Save metadata FIRST (safe - doesn't access co_code)
meta = {
    'module': MOD, 'func': FUNC, 'kind': KIND,
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
    elif isinstance(c, bytes): meta['consts'].append({'type': 'bytes', 'len': len(c), 'hex': c[:64].hex()})
    elif isinstance(c, (types.BuiltinFunctionType, types.BuiltinMethodType)): meta['consts'].append({'type': 'builtin'})
    elif isinstance(c, types.CodeType): meta['consts'].append({'type': 'code', 'name': c.co_name})
    elif isinstance(c, tuple): meta['consts'].append({'type': 'tuple', 'len': len(c)})
    else: meta['consts'].append({'type': type(c).__name__})

safe = f"{MOD}__{FUNC.replace('.','_')}"
meta_path = os.path.join(OUT, safe + '_meta.json')
with open(meta_path, 'w', encoding='utf-8') as fh:
    json.dump(meta, fh, indent=2, ensure_ascii=False)

# Now try to marshal (may crash for protected functions)
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

try:
    cc = clean(co)
    raw = marshal.dumps(cc)
    pyc_path = os.path.join(OUT, safe + '.pyc')
    with open(pyc_path, 'wb') as fh:
        fh.write(HDR + raw)
    print(f"PYC:{len(raw)}")
except:
    print(f"META:ok")
