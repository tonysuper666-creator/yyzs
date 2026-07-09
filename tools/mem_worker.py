"""Memory bypass worker - runs in subprocess for safety."""
import sys, os, marshal, types, struct, ctypes
EXT = sys.argv[1]; OUT = sys.argv[2]; MOD = sys.argv[3]; FUNC = sys.argv[4]; OFFSET = int(sys.argv[5])
HDR = b'\xf3\x0d\x0d\x0a' + b'\x00' * 12
sys.path.insert(0, EXT)
import pyarmor_runtime_011372
sys.modules.pop(MOD, None)
mod = __import__(MOD)
attr = getattr(mod, FUNC)
co = attr.__code__

try:
    # Read raw struct
    co_ptr = id(co)
    sz = 256  # Use fixed size, don't call methods on co
    buf_type = ctypes.c_ubyte * sz
    buf = buf_type.from_address(co_ptr)
    raw = bytes(buf)
    
    # Read co_code pointer at the given offset
    co_code_ptr = struct.unpack_from('<Q', raw, OFFSET)[0]
    
    # Validate pointer
    if co_code_ptr < 0x1000000 or co_code_ptr > 0x7FFFFFFFFFFF:
        print(f"ERR:bad_ptr:0x{co_code_ptr:X}")
        sys.exit(1)
    
    # Read PyBytesObject header at the pointer
    header_type = ctypes.c_ubyte * 32
    try:
        header = header_type.from_address(co_code_ptr)
    except:
        print(f"ERR:cannot_read_header")
        sys.exit(1)
    
    header_bytes = bytes(header)
    ob_size = struct.unpack_from('<Q', header_bytes, 16)[0]
    
    if ob_size <= 0 or ob_size > 100000:
        print(f"ERR:bad_size:{ob_size}")
        sys.exit(1)
    
    # Read bytecode data
    total = 32 + ob_size + 1
    data_type = ctypes.c_ubyte * total
    try:
        data = data_type.from_address(co_code_ptr)
    except:
        print(f"ERR:cannot_read_data")
        sys.exit(1)
    
    data_bytes = bytes(data)
    bytecode = data_bytes[32:32 + ob_size]
    
    # Clean constants
    nc = []
    for c in co.co_consts:
        if isinstance(c, (types.BuiltinFunctionType, types.BuiltinMethodType)):
            nc.append(None)
        elif isinstance(c, types.CodeType):
            nc.append(None)
        elif isinstance(c, tuple):
            r = list(c)
            for j in range(len(r)):
                if isinstance(r[j], (types.BuiltinFunctionType, types.BuiltinMethodType, types.CodeType)):
                    r[j] = None
            nc.append(tuple(r))
        else:
            try: marshal.dumps(c); nc.append(c)
            except: nc.append(None)
    
    new_co = co.replace(co_consts=tuple(nc))
    raw_m = marshal.dumps(new_co)
    
    safe = f"{MOD}__{FUNC}_mem"
    with open(os.path.join(OUT, safe + '.pyc'), 'wb') as f:
        f.write(HDR + raw_m)
    
    print(f"OK:{len(raw_m)}:{ob_size}")
    
except Exception as e:
    print(f"ERR:{type(e).__name__}:{e}")
