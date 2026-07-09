"""
Disassemble all .pyc files into readable pseudo-code.
Also dump summary of key metadata files.
"""
import sys, os, marshal, dis, io, json

OUT = r"C:\Users\1\Downloads\Telegram Desktop\decrypted"
DECOMP = os.path.join(OUT, "disassembly")
os.makedirs(DECOMP, exist_ok=True)

# Python 3.13 uses sys.path to find modules
sys.path.insert(0, OUT)

def disassemble_pyc(pyc_path):
    """Disassemble a .pyc file."""
    with open(pyc_path, 'rb') as f:
        f.read(16)  # Skip header
        try:
            co = marshal.load(f)
        except Exception as e:
            return f"ERROR loading: {e}"
    
    # Build human-readable output
    lines = []
    lines.append(f"# Code Object: {co.co_name}")
    lines.append(f"# File: {co.co_filename}")
    lines.append(f"# Args: {co.co_argcount}, Locals: {co.co_nlocals}, Stack: {co.co_stacksize}")
    lines.append(f"# Flags: {co.co_flags}")
    lines.append(f"")
    
    if co.co_names:
        lines.append(f"# Names: {co.co_names}")
    if co.co_varnames:
        lines.append(f"# Varnames: {co.co_varnames}")
    if co.co_cellvars:
        lines.append(f"# Cellvars: {co.co_cellvars}")
    if co.co_freevars:
        lines.append(f"# Freevars: {co.co_freevars}")
    lines.append("")
    
    # Constants
    for i, c in enumerate(co.co_consts):
        if isinstance(c, str):
            if len(c) < 200:
                lines.append(f"# const[{i}] = {repr(c)}")
            else:
                lines.append(f"# const[{i}] = {repr(c[:200])}...")
        elif isinstance(c, (int, float)):
            lines.append(f"# const[{i}] = {c}")
        elif c is None:
            lines.append(f"# const[{i}] = None")
        elif isinstance(c, bytes):
            lines.append(f"# const[{i}] = bytes({len(c)}) {c[:32].hex()}...")
        elif hasattr(c, 'co_name'):
            lines.append(f"# const[{i}] = <code '{c.co_name}'>")
    
    lines.append("")
    lines.append("#" + "="*70)
    lines.append("# DISASSEMBLY")
    lines.append("#" + "="*70)
    
    try:
        buf = io.StringIO()
        dis.dis(co, file=buf)
        lines.append(buf.getvalue())
    except Exception as e:
        lines.append(f"# DISASSEMBLY FAILED: {e}")
        # Try manual bytecode dump
        try:
            code_bytes = co.co_code
            lines.append(f"# Bytecode ({len(code_bytes)} bytes):")
            for offset in range(0, len(code_bytes), 16):
                chunk = code_bytes[offset:offset+16]
                hex_str = ' '.join(f'{b:02x}' for b in chunk)
                ascii_str = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
                lines.append(f"#   {offset:04x}: {hex_str:<48s} {ascii_str}")
        except:
            lines.append(f"# Bytecode NOT accessible")
    
    return '\n'.join(lines)

# Process all .pyc files
pyc_files = sorted([f for f in os.listdir(OUT) if f.endswith('.pyc')])

for pyc_file in pyc_files:
    pyc_path = os.path.join(OUT, pyc_file)
    dis_path = os.path.join(DECOMP, pyc_file.replace('.pyc', '.py.dis'))
    
    output = disassemble_pyc(pyc_path)
    
    with open(dis_path, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"  {pyc_file} -> {os.path.basename(dis_path)} ({len(output)} chars)")

# Also generate a comprehensive summary from metadata
print(f"\nGenerating comprehensive summary from {236 - 13} metadata files...")

meta_files = sorted([f for f in os.listdir(OUT) if f.endswith('_meta.json')])
meta_summary = {}

for mf in meta_files:
    with open(os.path.join(OUT, mf), 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    mod = data.get('module', '?')
    func = data.get('func', mf)
    if mod not in meta_summary:
        meta_summary[mod] = []
    
    # Extract key info
    info = {
        'func': func,
        'names': data.get('names', []),
        'varnames': data.get('varnames', []),
        'argcount': data.get('argcount', 0),
        'strings': [c['value'] for c in data.get('consts', []) if c.get('type') == 'str'],
    }
    meta_summary[mod].append(info)

# Save summary
summary_path = os.path.join(OUT, "COMPREHENSIVE_SUMMARY.json")
with open(summary_path, 'w', encoding='utf-8') as f:
    json.dump(meta_summary, f, indent=2, ensure_ascii=False)

print(f"\nTotal modules analyzed: {len(meta_summary)}")
for mod, items in sorted(meta_summary.items()):
    print(f"  {mod}: {len(items)} functions")
    for item in items[:3]:
        ns = item['names'][:5]
        ss = [s[:60] for s in item['strings'][:3]]
        print(f"    {item['func']}: names={ns} strings={ss}")
    if len(items) > 3:
        print(f"    ... and {len(items)-3} more")

print(f"\nOutput:")
print(f"  Disassembly: {DECOMP}/ ({len(pyc_files)} files)")
print(f"  Summary: {summary_path}")
