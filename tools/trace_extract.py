"""
BYpass attempt: Use sys.settrace to capture bytecode during execution.
When a protected function runs, its bytecode is being executed - 
the trace function receives the frame, which has access to the code object.
"""
import sys, os, marshal, types, io

EXT = r"C:\Users\1\Downloads\Telegram Desktop\6hzsv2.23.exe_extracted"
OUT = r"C:\Users\1\Downloads\Telegram Desktop\decrypted"
HDR = b'\xF3\x0D\x0D\x0A' + b'\x00' * 12

sys.path.insert(0, EXT)
import pyarmor_runtime_011372

def clean_co(co):
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
    return co.replace(co_consts=tuple(nc))

# Test approach: import a crashing function, set trace, call it in a sandbox
import security

captured = {}

def trace_func(frame, event, arg):
    """Trace function - called for each function call."""
    if event == 'call':
        co = frame.f_code
        fname = co.co_name
        if fname not in captured and '<frozen' in co.co_filename:
            try:
                # Try to access co_code inside the trace (might work since we're in execution context)
                codelen = len(co.co_code)
                cc = clean_co(co)
                raw = marshal.dumps(cc)
                safe_name = f"trace__{fname}"
                with open(os.path.join(OUT, safe_name + '.pyc'), 'wb') as f:
                    f.write(HDR + raw)
                print(f"  CAPTURED {fname}: {codelen}B bytecode, {len(raw)}B marshalled")
                captured[fname] = True
            except Exception as e:
                print(f"  FAILED {fname}: {type(e).__name__}")
    return trace_func

# Try with a simple crashing function that has no side effects
print("=== Testing trace capture on clear_force_offline_reason (working) ===")
sys.settrace(trace_func)
try:
    security.clear_force_offline_reason()
except:
    pass
sys.settrace(None)

# Now try with a crashing function
print("\n=== Testing trace capture on get_app_path (automation) ===")
sys.modules.pop('automation', None)
import automation

sys.settrace(trace_func)
try:
    # get_app_path should return a path without side effects
    result = automation.get_app_path()
    print(f"  Result: {result}")
except Exception as e:
    print(f"  Function call error: {e}")
sys.settrace(None)

# Try another - precise_sleep with a very short sleep
print("\n=== Testing trace capture on precise_sleep (automation) ===")
sys.settrace(trace_func)
try:
    automation.precise_sleep(0.001)  # Very short sleep
    print(f"  OK")
except Exception as e:
    print(f"  Error: {e}")
sys.settrace(None)

# Try get_work_folder
print("\n=== Testing trace capture on get_work_folder (activation) ===")
sys.modules.pop('activation', None)
import activation

sys.settrace(trace_func)
try:
    result = activation.get_work_folder()
    print(f"  Result: {result}")
except Exception as e:
    print(f"  Error: {e}")
sys.settrace(None)

print(f"\nCaptured: {len(captured)} functions")
for name in captured:
    print(f"  {name}")
