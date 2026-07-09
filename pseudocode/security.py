"""
6号自动化助手 - security.py

状态说明:
  - 函数签名/参数名/字符串常量/引用的API: 100%% 准确
  - 标记 [DISASM] 的函数: 有完整字节码反汇编
  - 标记 [META] 的函数: 仅元数据，无字节码
  - editor/ 目录: 100%% 原始源码
"""

def clear_force_offline_reason():  # [DISASM]
    """清除强制下线原因（UI已显示后调用）"""
    # === Bytecode Disassembly ===
    #  492           NOP
    #                NOP
    #                LOAD_CONST               2 (None)
    #                PUSH_NULL
    #  493           LOAD_CONST               3 (b'@\xb3k\xf0W\x02\x00\x00\x03\x00\x00\x1a\x1a\x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RESUME                   0
    #                LOAD_CONST               1 (None)
    #                STORE_FAST               0 (__assert_armored__)
    #                NOP
    #                NOP
    #  492           NOP
    #  495   L1:     LOAD_CONST               4 (None)
    #                STORE_GLOBAL             0 (_force_offline_reason)
    #        L2:     LOAD_CONST               4 (None)
    #                NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD            19 (to L5)
    #                CACHE
    #                CACHE
    #                CACHE
    #                POP_TOP
    #                RETURN_CONST             4 (None)
    #   --   L3:     PUSH_EXC_INFO
    #  495           LOAD_CONST               5 (None)
    #                NOP
    #                PUSH_NULL
    #                LOAD_CONST               3 (b'@\xb3k\xf0W\x02\x00\x00\x03\x00\x00\x1a\x1a\x00\x00\x00\x01\x00\x00\x00')
    #                CALL                     1
    #                POP_TOP
    #                RERAISE                  0
    #   --   L4:     COPY                     3
    #                POP_EXCEPT
    #                RERAISE                  1
    #        L5:     LOAD_CONST               5 (None)
    #                PUSH_NULL
    #                LOAD_CONST               3 (b'@\xb3k\xf0W\x02\x00\x00\x03\x00\x00\x1a\x1a\x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RETURN_VALUE
    # ExceptionTable:
    #   L1 to L2 -> L3 [0]
    #   L3 to L4 -> L4 [1] lasti
    # Full: docs/FINAL_DISASSEMBLY/clear_force_offline_reason.dis
    pass  # [DISASM available above]

def get_api_secret_key():  # [META]
    """运行时获取解密后的API密钥"""
    # Referenced APIs: bytes, decode
    # const: 'utf-8'
    # const: 'INVALID_KEY'
    pass  # [META only]

def get_force_offline_reason():  # [DISASM]
    """获取强制下线原因（服务端解绑/删除激活码时推送），返回None表示无强制下线"""
    # === Bytecode Disassembly ===
    #  488           NOP
    #                NOP
    #                LOAD_CONST               2 (None)
    #                PUSH_NULL
    #  489           LOAD_CONST               3 (b'\x008\x83\x04\xa3\x01\x00\x00\x01\x00\x00\x1a \x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RESUME                   0
    #                LOAD_CONST               1 (None)
    #                STORE_FAST               0 (__assert_armored__)
    #                NOP
    #                NOP
    #  488           NOP
    #  490   L1:     LOAD_GLOBAL              0 (_force_offline_reason)
    #        L2:     NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD            20 (to L5)
    #                CALL                     1
    #                POP_TOP
    #                RETURN_VALUE
    #   --   L3:     PUSH_EXC_INFO
    #  490           LOAD_CONST               4 (None)
    #                NOP
    #                PUSH_NULL
    #                LOAD_CONST               3 (b'\x008\x83\x04\xa3\x01\x00\x00\x01\x00\x00\x1a \x00\x00\x00\x01\x00\x00\x00')
    #                CALL                     1
    #                POP_TOP
    #                RERAISE                  0
    #   --   L4:     COPY                     3
    #                POP_EXCEPT
    #                RERAISE                  1
    #        L5:     LOAD_CONST               4 (None)
    #                PUSH_NULL
    #                LOAD_CONST               3 (b'\x008\x83\x04\xa3\x01\x00\x00\x01\x00\x00\x1a \x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RETURN_VALUE
    # ExceptionTable:
    #   L1 to L2 -> L3 [0]
    #   L3 to L4 -> L4 [1] lasti
    # Full: docs/FINAL_DISASSEMBLY/get_force_offline_reason.dis
    pass  # [DISASM available above]

def init_integrity_check():  # [DISASM]
    """初始化完整性校验，返回hash供后续验证"""
    # === Bytecode Disassembly ===
    #  514           NOP
    #                NOP
    #                LOAD_CONST               2 (None)
    #                PUSH_NULL
    #  515           LOAD_CONST               3 (b'0\x0f\xba\x04\xa3\x01\x00\x00\x03\x00\x00\x1a4\x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RESUME                   0
    #                LOAD_CONST               1 (None)
    #                STORE_FAST               0 (__assert_armored__)
    #                NOP
    #                NOP
    #  514           NOP
    #  517   L1:     LOAD_GLOBAL              1 (_calculate_exe_hash + NULL)
    #                CALL                     0
    #                STORE_GLOBAL             1 (_exe_hash)
    #  518           LOAD_GLOBAL              2 (_exe_hash)
    #        L2:     NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD            20 (to L5)
    #                CALL                     1
    #                POP_TOP
    #                RETURN_VALUE
    #   --   L3:     PUSH_EXC_INFO
    #  518           LOAD_CONST               4 (None)
    #                NOP
    #                PUSH_NULL
    #                LOAD_CONST               3 (b'0\x0f\xba\x04\xa3\x01\x00\x00\x03\x00\x00\x1a4\x00\x00\x00\x01\x00\x00\x00')
    #                CALL                     1
    #                POP_TOP
    #                RERAISE                  0
    #   --   L4:     COPY                     3
    #                POP_EXCEPT
    #                RERAISE                  1
    #        L5:     LOAD_CONST               4 (None)
    #                PUSH_NULL
    #                LOAD_CONST               3 (b'0\x0f\xba\x04\xa3\x01\x00\x00\x03\x00\x00\x1a4\x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RETURN_VALUE
    # ExceptionTable:
    #   L1 to L2 -> L3 [0]
    #   L3 to L4 -> L4 [1] lasti
    # Full: docs/FINAL_DISASSEMBLY/init_integrity_check.dis
    pass  # [DISASM available above]

def init_security(server_url, machine_id):  # [DISASM]
    """初始化安全模块
在程序启动时调用

Args:
    server_url: 服务器地址（用于心跳验证）
    machine_id: 机器ID（用于心跳验证）"""
    # Referenced APIs: init_integrity_check, init_time_check, getattr, sys, security_check_with_warning, exit, start_heartbeat
    # const: 'frozen'
    # === Bytecode Disassembly ===
    #  674           NOP
    #                NOP
    #                LOAD_CONST               2 (None)
    #                PUSH_NULL
    #  675           LOAD_CONST               3 (b'\x10\x84\xc1\x04\xa3\x01\x00\x00\x03\x00\x00\x1a\xe4\x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RESUME                   0
    #                LOAD_CONST               1 (None)
    #                STORE_FAST               2 (__assert_armored__)
    #                NOP
    #                NOP
    #  674           NOP
    #  684   L1:     LOAD_GLOBAL              1 (init_integrity_check + NULL)
    #                CALL                     0
    #                POP_TOP
    #  687           LOAD_GLOBAL              3 (init_time_check + NULL)
    #                CALL                     0
    #                POP_TOP
    #  690           LOAD_GLOBAL              5 (getattr + NULL)
    #                LOAD_GLOBAL              6 (sys)
    #                LOAD_CONST               4 ('frozen')
    #                LOAD_CONST               5 (False)
    #                CALL                     3
    #                TO_BOOL
    #                POP_JUMP_IF_FALSE       61 (to L3)
    #  691           LOAD_GLOBAL              9 (security_check_with_warning + NULL)
    #                CALL                     0
    #                TO_BOOL
    #                POP_JUMP_IF_TRUE        22 (to L2)
    #  692           LOAD_GLOBAL              6 (sys)
    #                LOAD_ATTR               10 (exit)
    #                PUSH_NULL
    #                LOAD_CONST               6 (1)
    #                CALL                     1
    #                POP_TOP
    #  695   L2:     LOAD_FAST                0 (server_url)
    #                TO_BOOL
    #                POP_JUMP_IF_FALSE       17 (to L3)
    #                LOAD_FAST                1 (machine_id)
    #                TO_BOOL
    #                POP_JUMP_IF_FALSE       10 (to L3)
    #  696           LOAD_GLOBAL             13 (start_heartbeat + NULL)
    #                LOAD_FAST_LOAD_FAST      1 (server_url, machine_id)
    #                LOAD_CONST               7 (120)
    #                LOAD_CONST               8 (('interval',))
    #                CALL_KW                  3
    #                POP_TOP
    #  698   L3:     LOAD_CONST              10 (True)
    # Full: docs/FINAL_DISASSEMBLY/init_security.dis
    pass  # [DISASM available above]

def init_time_check():  # [DISASM]
    """初始化时间检查"""
    # Referenced APIs: time, getattr, sys, os, path, join, dirname, executable, open, write, str, int
    # const: 'frozen'
    # const: '.timestamp'
    # === Bytecode Disassembly ===
    #  561            NOP
    #                 NOP
    #                 LOAD_CONST               2 (None)
    #                 PUSH_NULL
    #  562            LOAD_CONST               3 (b'0\x19\x9f\x04\xa3\x01\x00\x00\x01\x00\x00\x1a\xe6\x01\x00\x00\x01\x00\x00\x00')
    #                 BUILD_TUPLE              1
    #                 CALL_FUNCTION_EX         0
    #                 POP_TOP
    #                 RESUME                   0
    #                 LOAD_CONST               1 (None)
    #                 STORE_FAST               0 (__assert_armored__)
    #                 NOP
    #                 NOP
    #  561            NOP
    #  564    L1:     LOAD_CONST               4 (0)
    #                 LOAD_CONST               5 (None)
    #                 IMPORT_NAME              0 (time)
    #                 STORE_FAST               1 (_var_var_57)
    #  566            LOAD_FAST                1 (_var_var_57)
    #                 LOAD_ATTR                1 (time + NULL|self)
    #                 CALL                     0
    #                 STORE_GLOBAL             1 (_last_valid_time)
    #  569            LOAD_GLOBAL              5 (_get_network_time + NULL)
    #                 CALL                     0
    #                 STORE_FAST               2 (_var_var_79)
    #  570            LOAD_FAST                2 (_var_var_79)
    #                 TO_BOOL
    #                 POP_JUMP_IF_FALSE        9 (to L2)
    #  571            LOAD_FAST                2 (_var_var_79)
    #                 LOAD_GLOBAL              2 (_last_valid_time)
    #                 BINARY_OP               10 (-)
    #                 STORE_GLOBAL             3 (_network_time_offset)
    #  574    L2:     LOAD_GLOBAL              9 (getattr + NULL)
    #                 LOAD_GLOBAL             10 (sys)
    #                 LOAD_CONST               6 ('frozen')
    #                 LOAD_CONST               7 (False)
    #                 CALL                     3
    #                 TO_BOOL
    #                 POP_JUMP_IF_FALSE      140 (to L7)
    #  575            LOAD_GLOBAL             12 (os)
    #                 LOAD_ATTR               14 (path)
    #                 LOAD_ATTR               17 (join + NULL|self)
    #                 LOAD_GLOBAL             12 (os)
    #                 LOAD_ATTR               14 (path)
    #                 LOAD_ATTR               19 (dirname + NULL|self)
    #                 LOAD_GLOBAL             10 (sys)
    #                 LOAD_ATTR               20 (executable)
    #                 CALL                     1
    #                 LOAD_CONST               8 ('.timestamp')
    #                 CALL                     2
    # Full: docs/FINAL_DISASSEMBLY/init_time_check.dis
    pass  # [DISASM available above]

def is_heartbeat_valid():  # [DISASM]
    """检查心跳状态"""
    # === Bytecode Disassembly ===
    #  484           NOP
    #                NOP
    #                LOAD_CONST               2 (None)
    #                PUSH_NULL
    #  485           LOAD_CONST               3 (b'\xd06\x83\x04\xa3\x01\x00\x00\x03\x00\x00\x1a \x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RESUME                   0
    #                LOAD_CONST               1 (None)
    #                STORE_FAST               0 (__assert_armored__)
    #                NOP
    #                NOP
    #  484           NOP
    #  486   L1:     LOAD_GLOBAL              0 (_last_heartbeat_success)
    #        L2:     NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD            20 (to L5)
    #                CALL                     1
    #                POP_TOP
    #                RETURN_VALUE
    #   --   L3:     PUSH_EXC_INFO
    #  486           LOAD_CONST               4 (None)
    #                NOP
    #                PUSH_NULL
    #                LOAD_CONST               3 (b'\xd06\x83\x04\xa3\x01\x00\x00\x03\x00\x00\x1a \x00\x00\x00\x01\x00\x00\x00')
    #                CALL                     1
    #                POP_TOP
    #                RERAISE                  0
    #   --   L4:     COPY                     3
    #                POP_EXCEPT
    #                RERAISE                  1
    #        L5:     LOAD_CONST               4 (None)
    #                PUSH_NULL
    #                LOAD_CONST               3 (b'\xd06\x83\x04\xa3\x01\x00\x00\x03\x00\x00\x1a \x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RETURN_VALUE
    # ExceptionTable:
    #   L1 to L2 -> L3 [0]
    #   L3 to L4 -> L4 [1] lasti
    # Full: docs/FINAL_DISASSEMBLY/is_heartbeat_valid.dis
    pass  # [DISASM available above]

def perform_full_security_check():  # [DISASM]
    """执行完整的安全检查"""
    # Referenced APIs: perform_security_check, verify_integrity, verify_time, is_heartbeat_valid
    # === Bytecode Disassembly ===
    #  632            NOP
    #                 NOP
    #                 LOAD_CONST               2 (None)
    #                 PUSH_NULL
    #  633            LOAD_CONST               3 (b'\xf0\xec\x96\x04\xa3\x01\x00\x00\x03\x00\x00\x1a\x0c\x01\x00\x00\x01\x00\x00\x00')
    #                 BUILD_TUPLE              1
    #                 CALL_FUNCTION_EX         0
    #                 POP_TOP
    #                 RESUME                   0
    #                 LOAD_CONST               1 (None)
    #                 STORE_FAST               0 (__assert_armored__)
    #                 NOP
    #                 NOP
    #  632            NOP
    #  635    L1:     LOAD_GLOBAL              1 (perform_security_check + NULL)
    #                 CALL                     0
    #                 UNPACK_SEQUENCE          2
    #                 STORE_FAST_STORE_FAST   18 (_var_var_84, _var_var_85)
    #  636            LOAD_FAST                1 (_var_var_84)
    #                 TO_BOOL
    #                 POP_JUMP_IF_TRUE        13 (to L3)
    #  637            LOAD_CONST               4 (False)
    #                 LOAD_FAST                2 (_var_var_85)
    #                 BUILD_TUPLE              2
    #  652    L2:     NOP
    #                 NOP
    #                 NOP
    #                 JUMP_FORWARD           121 (to L12)
    #                 CALL                     1
    #                 POP_TOP
    #                 RETURN_VALUE
    #  640    L3:     LOAD_GLOBAL              3 (verify_integrity + NULL)
    #                 CALL                     0
    #                 TO_BOOL
    #                 POP_JUMP_IF_TRUE        11 (to L5)
    #  641    L4:     NOP
    #  652            LOAD_CONST               6 ((False, '程序完整性校验失败'))
    #                 NOP
    #                 NOP
    #                 NOP
    #                 JUMP_FORWARD            94 (to L12)
    #                 CACHE
    #                 CACHE
    #                 CACHE
    #                 POP_TOP
    #                 RETURN_CONST             6 ((False, '程序完整性校验失败'))
    #  644    L5:     LOAD_GLOBAL              5 (verify_time + NULL)
    #                 CALL                     0
    #                 UNPACK_SEQUENCE          2
    #                 STORE_FAST_STORE_FAST   52 (_var_var_86, _var_var_87)
    # Full: docs/FINAL_DISASSEMBLY/perform_full_security_check.dis
    pass  # [DISASM available above]

def perform_security_check():  # [DISASM]
    """执行安全检查
返回: (is_safe: bool, reason: str)"""
    # const: '检测到可疑进程: '
    # const: '检测到可疑模块: '
    # === Bytecode Disassembly ===
    #  275            NOP
    #                 NOP
    #                 LOAD_CONST               2 (None)
    #                 PUSH_NULL
    #  276            LOAD_CONST               3 (b'@<b\x04\xa3\x01\x00\x00\x01\x00\x00\x1a\xd6\x00\x00\x00\x01\x00\x00\x00')
    #                 BUILD_TUPLE              1
    #                 CALL_FUNCTION_EX         0
    #                 POP_TOP
    #                 RESUME                   0
    #                 LOAD_CONST               1 (None)
    #                 STORE_FAST               0 (__assert_armored__)
    #                 NOP
    #                 NOP
    #  275            NOP
    #  281    L1:     LOAD_GLOBAL              1 (_is_debugger_present + NULL)
    #                 CALL                     0
    #                 TO_BOOL
    #                 POP_JUMP_IF_FALSE       11 (to L3)
    #  282    L2:     NOP
    #  298            LOAD_CONST               5 ((False, '检测到调试器'))
    #                 NOP
    #                 NOP
    #                 NOP
    #                 JUMP_FORWARD            99 (to L10)
    #                 CACHE
    #                 CACHE
    #                 CACHE
    #                 POP_TOP
    #                 RETURN_CONST             5 ((False, '检测到调试器'))
    #  285    L3:     LOAD_GLOBAL              3 (_check_suspicious_processes + NULL)
    #                 CALL                     0
    #                 UNPACK_SEQUENCE          2
    #                 STORE_FAST_STORE_FAST   18 (_var_var_41, _var_var_33)
    #  286            LOAD_FAST                1 (_var_var_41)
    #                 TO_BOOL
    #                 POP_JUMP_IF_FALSE       16 (to L5)
    #  287            LOAD_CONST               6 (False)
    #                 LOAD_CONST               7 ('检测到可疑进程: ')
    #                 LOAD_FAST                2 (_var_var_33)
    #                 FORMAT_SIMPLE
    #                 BUILD_STRING             2
    #                 BUILD_TUPLE              2
    #  298    L4:     NOP
    #                 NOP
    #                 NOP
    #                 JUMP_FORWARD            65 (to L10)
    #                 CALL                     1
    #                 POP_TOP
    #                 RETURN_VALUE
    #  290    L5:     LOAD_GLOBAL              5 (_check_loaded_dlls + NULL)
    # Full: docs/FINAL_DISASSEMBLY/perform_security_check.dis
    pass  # [DISASM available above]

def security_check_with_warning():  # [DISASM]
    """执行安全检查，如果不安全则显示警告"""
    # Referenced APIs: perform_security_check, ctypes, windll, user32, MessageBoxW, print
    # const: '程序检测到异常环境，无法运行。\n原因: '
    # const: '安全检查失败'
    # const: '安全检查失败: '
    # === Bytecode Disassembly ===
    #     # Raw bytecode (288 bytes):
    #     #   0000: 1e 37 1e c7 53 02 22 00 53 03 34 01 36 00 20 00  .7..S.".S.4.6. .
    #     #   0010: 95 00 53 01 6e 00 1e 27 1e bb 49 82 28 e4 00 00  ..S.n..'..I.(...
    #     #   0020: 00 00 00 00 00 58 00 69 59 cf 2d 63 00 00 00 14  .....X.iY.-c....
    #     #   0030: 2f 0d 6c a0 00 00 00 00 00 00 00 00 35 b0 00 00  /.l.........5...
    #     #   0040: 00 00 00 00 0b be 35 69 00 00 00 00 00 00 28 b2  ......5i......(.
    #     #   0050: 00 00 00 00 00 00 00 f0 6c f7 00 00 00 00 00 00  ........l.......
    #     #   0060: 00 00 74 6f 23 6b 00 ca 00 c2 35 32 00 00 00 00  ..to#k....52....
    #     #   0070: 00 00 3a 8b 00 00 70 bc 00 ab 45 be 3a d9 00 00  ..:...p...E.:...
    #     #   0080: 00 2f 3b 2f 00 00 15 0f 54 d5 75 23 00 00 35 1c  ./;/....T.u#..5.
    #     #   0090: 00 00 00 00 00 00 4b 80 6b 17 69 30 00 73 75 8d  ......K.k.i0.su.
    #     #   00a0: 00 00 75 8c 00 00 0b 96 2d 0d 00 00 00 b8 5a e5  ..u.....-.....Z.
    #     #   00b0: 95 73 18 68 00 f9 28 aa 00 00 00 00 00 00 5b 43  .s.h..(.......[C
    #     #   00c0: 00 00 00 00 00 00 00 00 48 72 00 00 05 e1 00 00  ........Hr......
    #     #   00d0: 37 11 00 33 55 8a 28 ed 00 00 00 00 00 00 5b 1f  7..3U.(.......[.
    #     #   00e0: 00 00 00 00 00 00 00 00 52 57 00 00 00 00 00 00  ........RW......
    #     #   00f0: 00 00 00 00 00 00 00 00 00 00 00 00 22 00 53 03  ............".S.
    #     #   0100: 35 01 00 00 00 00 00 00 20 00 66 00 3d 03 1f 00  5....... .f.=...
    #     #   0110: 66 01 53 0a 22 00 53 03 34 01 36 00 20 00 24 00  f.S.".S.4.6. .$.
    # Full: docs/FINAL_DISASSEMBLY/security_check_with_warning.dis
    pass  # [DISASM available above]

def start_heartbeat(server_url, machine_id, interval):  # [DISASM]
    """启动心跳验证"""
    # Referenced APIs: is_alive, threading, Thread, start
    # === Bytecode Disassembly ===
    #  463           NOP
    #                NOP
    #                LOAD_CONST               2 (None)
    #                PUSH_NULL
    #  464           LOAD_CONST               3 (b'\x10B\xbe\x04\xa3\x01\x00\x00\x03\x00\x00\x1a\xce\x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RESUME                   0
    #                LOAD_CONST               1 (None)
    #                STORE_FAST               3 (__assert_armored__)
    #                NOP
    #                NOP
    #  463           NOP
    #  467   L1:     LOAD_GLOBAL              0 (_heartbeat_thread)
    #                POP_JUMP_IF_NONE        36 (to L3)
    #                LOAD_GLOBAL              0 (_heartbeat_thread)
    #                LOAD_ATTR                3 (is_alive + NULL|self)
    #                CALL                     0
    #                TO_BOOL
    #                POP_JUMP_IF_FALSE       11 (to L3)
    #  468   L2:     NOP
    #  477           LOAD_CONST               4 (None)
    #                NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD            78 (to L7)
    #                CACHE
    #                CACHE
    #                CACHE
    #                POP_TOP
    #                RETURN_CONST             4 (None)
    #  470   L3:     LOAD_CONST               6 (False)
    #                STORE_GLOBAL             2 (_heartbeat_stop)
    #  471           LOAD_CONST               7 (0)
    #                LOAD_CONST               4 (None)
    #                IMPORT_NAME              3 (threading)
    #                STORE_FAST               4 (_var_var_73)
    #  472           LOAD_FAST                4 (_var_var_73)
    #                LOAD_ATTR                9 (Thread + NULL|self)
    #  473           LOAD_GLOBAL             10 (_heartbeat_worker)
    #  474           LOAD_FAST_LOAD_FAST      1 (server_url, machine_id)
    #                LOAD_FAST                2 (interval)
    #                BUILD_TUPLE              3
    #  475           LOAD_CONST               8 (True)
    #  472           LOAD_CONST               9 (('target', 'args', 'daemon'))
    #                CALL_KW                  3
    #                STORE_GLOBAL             0 (_heartbeat_thread)
    #  477           LOAD_GLOBAL              0 (_heartbeat_thread)
    #                LOAD_ATTR               13 (start + NULL|self)
    # Full: docs/FINAL_DISASSEMBLY/start_heartbeat.dis
    pass  # [DISASM available above]

def stop_heartbeat():  # [DISASM]
    """停止心跳验证"""
    # === Bytecode Disassembly ===
    #  479           NOP
    #                NOP
    #                LOAD_CONST               2 (None)
    #                PUSH_NULL
    #  480           LOAD_CONST               3 (b'\xa05\x83\x04\xa3\x01\x00\x00\x01\x00\x00\x1a\x1a\x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RESUME                   0
    #                LOAD_CONST               1 (None)
    #                STORE_FAST               0 (__assert_armored__)
    #                NOP
    #                NOP
    #  479           NOP
    #  482   L1:     LOAD_CONST               4 (True)
    #                STORE_GLOBAL             0 (_heartbeat_stop)
    #        L2:     LOAD_CONST               6 (None)
    #                NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD            19 (to L5)
    #                CACHE
    #                CACHE
    #                CACHE
    #                POP_TOP
    #                RETURN_CONST             6 (None)
    #   --   L3:     PUSH_EXC_INFO
    #  482           LOAD_CONST               5 (None)
    #                NOP
    #                PUSH_NULL
    #                LOAD_CONST               3 (b'\xa05\x83\x04\xa3\x01\x00\x00\x01\x00\x00\x1a\x1a\x00\x00\x00\x01\x00\x00\x00')
    #                CALL                     1
    #                POP_TOP
    #                RERAISE                  0
    #   --   L4:     COPY                     3
    #                POP_EXCEPT
    #                RERAISE                  1
    #        L5:     LOAD_CONST               5 (None)
    #                PUSH_NULL
    #                LOAD_CONST               3 (b'\xa05\x83\x04\xa3\x01\x00\x00\x01\x00\x00\x1a\x1a\x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RETURN_VALUE
    # ExceptionTable:
    #   L1 to L2 -> L3 [0]
    #   L3 to L4 -> L4 [1] lasti
    # Full: docs/FINAL_DISASSEMBLY/stop_heartbeat.dis
    pass  # [DISASM available above]

def verify_integrity():  # [DISASM]
    """验证代码完整性"""
    # Referenced APIs: getattr, sys
    # const: 'frozen'
    # === Bytecode Disassembly ===
    #  520           NOP
    #                NOP
    #                LOAD_CONST               2 (None)
    #                PUSH_NULL
    #  521           LOAD_CONST               3 (b'p\xf7^\x04\xa3\x01\x00\x00\x01\x00\x00\x1a\x86\x00\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RESUME                   0
    #                LOAD_CONST               1 (None)
    #                STORE_FAST               0 (__assert_armored__)
    #                NOP
    #                NOP
    #  520           NOP
    #  522   L1:     LOAD_GLOBAL              0 (_exe_hash)
    #                POP_JUMP_IF_NOT_NONE    31 (to L3)
    #  525           LOAD_GLOBAL              3 (getattr + NULL)
    #                LOAD_GLOBAL              4 (sys)
    #                LOAD_CONST               4 ('frozen')
    #                LOAD_CONST               5 (False)
    #                CALL                     3
    #                TO_BOOL
    #                UNARY_NOT
    #  528   L2:     NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD            48 (to L7)
    #                CALL                     1
    #                POP_TOP
    #                RETURN_VALUE
    #  527   L3:     LOAD_GLOBAL              7 (_calculate_exe_hash + NULL)
    #                CALL                     0
    #                STORE_FAST               1 (_var_var_75)
    #  528           LOAD_FAST                1 (_var_var_75)
    #                LOAD_GLOBAL              0 (_exe_hash)
    #                COMPARE_OP              72 (==)
    #        L4:     NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD            20 (to L7)
    #                CALL                     1
    #                POP_TOP
    #                RETURN_VALUE
    #   --   L5:     PUSH_EXC_INFO
    #  528           LOAD_CONST               6 (None)
    #                NOP
    #                PUSH_NULL
    #                LOAD_CONST               3 (b'p\xf7^\x04\xa3\x01\x00\x00\x01\x00\x00\x1a\x86\x00\x00\x00\x01\x00\x00\x00')
    #                CALL                     1
    #                POP_TOP
    # Full: docs/FINAL_DISASSEMBLY/verify_integrity.dis
    pass  # [DISASM available above]

def verify_time():  # [DISASM]
    """验证时间是否被篡改（增强版）"""
    # Referenced APIs: time, os, path, exists, open, int, read, strip, abs, write, str
    # === Bytecode Disassembly ===
    #  582            NOP
    #                 NOP
    #                 LOAD_CONST               2 (None)
    #                 PUSH_NULL
    #  583            LOAD_CONST               3 (b'0\x1c\x9f\x04\xa3\x01\x00\x00\x01\x00\x00\x1a\xfe\x02\x00\x00\x01\x00\x00\x00')
    #                 BUILD_TUPLE              1
    #                 CALL_FUNCTION_EX         0
    #                 POP_TOP
    #                 RESUME                   0
    #                 LOAD_CONST               1 (None)
    #                 STORE_FAST               0 (__assert_armored__)
    #                 NOP
    #                 NOP
    #  582            NOP
    #  585    L1:     LOAD_CONST               4 (0)
    #                 LOAD_CONST               5 (None)
    #                 IMPORT_NAME              0 (time)
    #                 STORE_FAST               1 (_var_var_57)
    #  587            LOAD_FAST                1 (_var_var_57)
    #                 LOAD_ATTR                1 (time + NULL|self)
    #                 CALL                     0
    #                 STORE_FAST               2 (_var_var_80)
    #  590            LOAD_GLOBAL              2 (_last_valid_time)
    #                 TO_BOOL
    #                 POP_JUMP_IF_FALSE       24 (to L3)
    #                 LOAD_FAST                2 (_var_var_80)
    #                 LOAD_GLOBAL              2 (_last_valid_time)
    #                 LOAD_CONST               6 (600)
    #                 BINARY_OP               10 (-)
    #                 COMPARE_OP              18 (bool(<))
    #                 POP_JUMP_IF_FALSE       11 (to L3)
    #  591    L2:     NOP
    #  627            LOAD_CONST               8 ((False, '检测到系统时间被回拨'))
    #                 NOP
    #                 NOP
    #                 EXTENDED_ARG             1
    #                 JUMP_FORWARD           346 (to L36)
    #                 CACHE
    #                 CACHE
    #                 CACHE
    #                 POP_TOP
    #                 RETURN_CONST             8 ((False, '检测到系统时间被回拨'))
    #  594    L3:     LOAD_GLOBAL              4 (_time_file)
    #                 TO_BOOL
    #                 POP_JUMP_IF_FALSE      126 (to L11)
    #                 LOAD_GLOBAL              6 (os)
    #                 LOAD_ATTR                8 (path)
    #                 LOAD_ATTR               11 (exists + NULL|self)
    #                 LOAD_GLOBAL              4 (_time_file)
    #                 CALL                     1
    # Full: docs/FINAL_DISASSEMBLY/verify_time.dis
    pass  # [DISASM available above]
