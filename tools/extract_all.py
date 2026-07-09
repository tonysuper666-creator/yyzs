"""
Complete PyArmor extraction - ALL modules, ALL functions.
Cleans unmarshallable C builtins, saves as pyc, then attempts decompilation.
"""
import sys, os, marshal, types, traceback

EXT = r"C:\Users\1\Downloads\Telegram Desktop\6hzsv2.23.exe_extracted"
OUT = r"C:\Users\1\Downloads\Telegram Desktop\decrypted"
os.makedirs(OUT, exist_ok=True)
sys.path.insert(0, EXT)

HDR = b'\xF3\x0D\x0D\x0A' + b'\x00' * 4 + b'\x00' * 8

import pyarmor_runtime_011372
print("runtime ok")

def clean_consts(consts):
    result = []
    for c in consts:
        if isinstance(c, (types.BuiltinFunctionType, types.BuiltinMethodType)):
            result.append(None)
        elif isinstance(c, types.CodeType):
            result.append(make_clean_code(c))
        elif isinstance(c, tuple):
            result.append(tuple(clean_consts(c)))
        else:
            try:
                marshal.dumps(c)
                result.append(c)
            except:
                result.append(None)
    return tuple(result)

def make_clean_code(co):
    consts = clean_consts(co.co_consts)
    
    # Get optional attributes with fallbacks
    lnotab = getattr(co, 'co_lnotab', b'')
    exctab = getattr(co, 'co_exceptiontable', b'')
    posonly = getattr(co, 'co_posonlyargcount', 0)
    kwonly = getattr(co, 'co_kwonlyargcount', 0)
    qualname = getattr(co, 'co_qualname', co.co_name)
    
    return types.CodeType(
        co.co_argcount, posonly, kwonly,
        co.co_nlocals, co.co_stacksize, co.co_flags,
        co.co_code, consts, co.co_names, co.co_varnames,
        co.co_filename, co.co_name, qualname,
        co.co_firstlineno, lnotab, exctab,
        co.co_freevars, co.co_cellvars,
    )

def extract_module(mod_name, frozen_tag):
    print(f"\n[{mod_name}]")
    sys.modules.pop(mod_name, None)
    
    try:
        mod = __import__(mod_name)
    except Exception as e:
        print(f"  IMPORT ERROR: {e}")
        return 0
    
    saved = 0
    
    for aname in sorted(dir(mod)):
        if aname.startswith('_'):
            continue
        
        # Skip known problematic functions
        if (mod_name, aname) in HANGERS:
            print(f"  SKIP {aname}")
            continue
        
        try:
            attr = getattr(mod, aname)
        except:
            continue
        
        if isinstance(attr, types.ModuleType):
            continue
        
        if not hasattr(attr, '__code__'):
            continue
        
        co = attr.__code__
        if frozen_tag not in co.co_filename:
            continue
        
        try:
            clean = make_clean_code(co)
            
            # Also extract nested code objects (closures, comprehensions)
            for i, const in enumerate(co.co_consts):
                if isinstance(const, types.CodeType) and frozen_tag in const.co_filename:
                    nested_clean = make_clean_code(const)
                    nsafe = f"{mod_name}__{aname}__nested{i}"
                    nraw = marshal.dumps(nested_clean)
                    with open(os.path.join(OUT, nsafe + '.pyc'), 'wb') as f:
                        f.write(HDR + nraw)
                    print(f"  + {aname}.nested[{i}] ({const.co_name}): {len(nraw)}B")
            
            raw = marshal.dumps(clean)
            safe = f"{mod_name}__{aname}"
            path = os.path.join(OUT, safe + '.pyc')
            with open(path, 'wb') as f:
                f.write(HDR + raw)
            print(f"  {aname}: {len(raw)}B")
            saved += 1
            
        except ValueError:
            print(f"  {aname}: UNMARSHALLABLE (even after cleaning)")
        except Exception as e:
            print(f"  {aname}: {type(e).__name__}")
    
    print(f"  => {saved} saved")
    return saved

# Functions known to hang during marshal.dumps
HANGERS = {
    ('security', 'get_api_secret_key'),
    ('activation', 'get_api_secret_key'),
}

total = 0
for mod_name, frozen_tag in [
    ('security', '<frozen security>'),
    ('activation', '<frozen activation>'),
    ('automation', '<frozen automation>'),
    ('web_server', '<frozen web_server>'),
]:
    total += extract_module(mod_name, frozen_tag)

print(f"\nTOTAL: {total} code objects")
print(f"Output: {OUT}")
