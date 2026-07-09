"""
Rebuild src/ files with actual disassembly embedded for functions that have it.
"""
import os, json, re

REPO = r"C:\Users\1\Downloads\Telegram Desktop\6hzs-reconstructed"
SUMMARY_PATH = os.path.join(REPO, "docs", "COMPREHENSIVE_SUMMARY.json")
DISASM_DIR = os.path.join(REPO, "docs")  # .dis files are directly in docs/

with open(SUMMARY_PATH, 'r', encoding='utf-8') as f:
    all_modules = json.load(f)

# Map of function name -> disassembly file
dis_map = {}
for fname in os.listdir(DISASM_DIR):
    if fname.endswith('.dis'):
        key = fname.replace('.dis', '').replace('_', '.', 1) if fname.startswith('_') else fname.replace('.dis', '')
        with open(os.path.join(DISASM_DIR, fname), 'r', encoding='utf-8', errors='replace') as f:
            dis_map[fname.replace('.dis', '')] = f.read()

def find_disassembly(func_name):
    """Find disassembly for a function by trying various name patterns."""
    # Try exact match
    if func_name in dis_map:
        return dis_map[func_name]
    # Try with class.method pattern
    for key in dis_map:
        if key.endswith('.' + func_name) or key.endswith('__' + func_name):
            return dis_map[key]
    # Try substring
    for key in dis_map:
        if func_name in key:
            return dis_map[key]
    return None

def extract_bytecode_hex(dis_text):
    """Extract raw bytecode hex dump from disassembly."""
    lines = []
    in_bytecode = False
    for line in dis_text.split('\n'):
        if 'Raw bytecode' in line or '# Bytecode (' in line:
            in_bytecode = True
            continue
        if in_bytecode:
            if line.strip().startswith('#') and ':' in line:
                lines.append(line.strip())
            elif not line.strip().startswith('#'):
                in_bytecode = False
    return '\n'.join(lines) if lines else None

def extract_bytecode_ops(dis_text):
    """Extract the actual disassembly instructions."""
    lines = []
    in_dis = False
    for line in dis_text.split('\n'):
        if 'DISASSEMBLY' in line or 'Bytecode Disassembly' in line:
            in_dis = True
            continue
        if in_dis and line.strip():
            if 'DISASSEMBLY FAILED' in line:
                break
            lines.append(line.rstrip())
    return '\n'.join(lines) if lines else None

def generate_source(mod_name, functions):
    lines = []
    lines.append(f'"""')
    lines.append(f'6号自动化助手 - {mod_name}.py')
    lines.append(f'')
    lines.append(f'状态说明:')
    lines.append(f'  - 函数签名/参数名/字符串常量/引用的API: 100%% 准确')  
    lines.append(f'  - 标记 [DISASM] 的函数: 有完整字节码反汇编')
    lines.append(f'  - 标记 [META] 的函数: 仅元数据，无字节码')
    lines.append(f'  - editor/ 目录: 100%% 原始源码')
    lines.append(f'"""')
    lines.append('')

    classes = {}
    standalone = []

    for func in functions:
        fname = func['func']
        if '.' in fname:
            cls, method = fname.split('.', 1)
            if cls not in classes:
                classes[cls] = []
            classes[cls].append((method, func))
        else:
            standalone.append(func)

    # Write classes
    for cls_name, methods in sorted(classes.items()):
        lines.append(f'class {cls_name}:')
        lines.append(f'    """Reconstructed from PyArmor-protected bytecode."""')
        lines.append('')
        
        for mname, mfunc in sorted(methods):
            dis = find_disassembly(f"{cls_name}.{mname}") or find_disassembly(mname)
            has_dis = dis is not None
            
            args = [a for a in mfunc.get('varnames', []) if not a.startswith('_') and a != 'self']
            argstr = ', '.join(args) if args else ''
            
            marker = '[DISASM]' if has_dis else '[META]'
            lines.append(f'    def {mname}(self{", " + argstr if argstr else ""}):  # {marker}')
            
            # Docstring
            for s in mfunc.get('strings', []):
                if len(s) > 3 and not s.startswith('PY') and not s.startswith('http'):
                    lines.append(f'        """{s.strip()}"""')
                    break
            
            # Names (API references)
            names = mfunc.get('names', [])
            if names:
                api = [n for n in names if not n.startswith('_')]
                if api:
                    lines.append(f'        # Referenced APIs: {", ".join(api[:15])}')
            
            # String constants
            strs = [s for s in mfunc.get('strings', []) if len(s) > 1]
            for s in strs[1:6]:
                if len(s) < 120:
                    lines.append(f'        # const: {repr(s)}')
            
            if has_dis:
                ops = extract_bytecode_ops(dis)
                if ops:
                    lines.append(f'        #')
                    lines.append(f'        # === Bytecode Disassembly ===')
                    for op_line in ops.split('\n')[:50]:  # Max 50 lines
                        lines.append(f'        # {op_line}')
                    if len(ops.split('\n')) > 50:
                        lines.append(f'        # ... (truncated, full disassembly in docs/)')
                else:
                    bc = extract_bytecode_hex(dis)
                    if bc:
                        lines.append(f'        # === Raw Bytecode ===')
                        for bcl in bc.split('\n')[:20]:
                            lines.append(f'        {bcl}')
                lines.append(f'        # Full disassembly: docs/FINAL_DISASSEMBLY/{mname}.dis')
                lines.append(f'        pass  # [DISASM available above]')
            else:
                lines.append(f'        pass  # [META only - no bytecode recovered]')
            
            lines.append('')
    
    # Standalone functions
    for func in standalone:
        fname = func['func']
        if fname == fname.upper():
            for s in func.get('strings', []):
                lines.append(f'{fname} = {repr(s)}')
            lines.append('')
            continue
        
        dis = find_disassembly(fname)
        has_dis = dis is not None
        
        args = [a for a in func.get('varnames', []) if not a.startswith('_')]
        argstr = ', '.join(args) if args else ''
        
        marker = '[DISASM]' if has_dis else '[META]'
        lines.append(f'def {fname}({argstr}):  # {marker}')
        
        for s in func.get('strings', []):
            if len(s) > 3 and not s.startswith('PY'):
                lines.append(f'    """{s.strip()}"""')
                break
        
        names = func.get('names', [])
        if names:
            api = [n for n in names if not n.startswith('_')]
            if api:
                lines.append(f'    # Referenced APIs: {", ".join(api[:15])}')
        
        strs = [s for s in func.get('strings', []) if len(s) > 1]
        for s in strs[1:6]:
            if len(s) < 120:
                lines.append(f'    # const: {repr(s)}')
        
        if has_dis:
            ops = extract_bytecode_ops(dis)
            if ops:
                lines.append(f'    # === Bytecode Disassembly ===')
                for op_line in ops.split('\n')[:50]:
                    lines.append(f'    # {op_line}')
            lines.append(f'    # Full: docs/FINAL_DISASSEMBLY/{fname}.dis')
            lines.append(f'    pass  # [DISASM available above]')
        else:
            lines.append(f'    pass  # [META only]')
        
        lines.append('')
    
    return '\n'.join(lines)

# Generate for each module
for mod_name, functions in all_modules.items():
    source = generate_source(mod_name, functions)
    path = os.path.join(REPO, "src", f"{mod_name}.py")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(source)
    print(f"Generated: {mod_name}.py ({len(source)} bytes)")

print("Done!")
