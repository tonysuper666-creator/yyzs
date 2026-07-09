"""
6号自动化助手 - activation.py

状态说明:
  - 函数签名/参数名/字符串常量/引用的API: 100%% 准确
  - 标记 [DISASM] 的函数: 有完整字节码反汇编
  - 标记 [META] 的函数: 仅元数据，无字节码
  - editor/ 目录: 100%% 原始源码
"""

class ActivationManager:
    """Reconstructed from PyArmor-protected bytecode."""

    def _get_local_fingerprint(self):  # [META]
        """获取本机指纹（用于验证缓存文件是否被复制）"""
        # Referenced APIs: socket, getpass, append, gethostname, getuser, subprocess, run, os, name, CREATE_NO_WINDOW, returncode, stdout, strip, split, join
        # const: 'nt'
        # const: 'InstallDate'
        # const: 'unknown'
        pass  # [META only - no bytecode recovered]

    def _pinned_post(self, url, kwargs):  # [META]
        """带证书固定验证的POST请求"""
        # Referenced APIs: ConnectionError, requests, post
        # const: '服务器证书验证失败，可能存在中间人攻击'
        pass  # [META only - no bytecode recovered]

    def _save_activation(self, code, expiry_str, signature, signed_data):  # [META]
        """保存激活信息到本地文件（带HMAC签名+RSA签名数据）"""
        # Referenced APIs: machine_id, datetime, now, isoformat, open, activation_file, json, dump, is_activated, activation_code, fromisoformat, activation_expiry, Exception, print
        # const: 'signature'
        # const: 'signed_data'
        # const: 'hmac'
        # const: 'utf-8'
        # const: '保存激活信息失败: '
        pass  # [META only - no bytecode recovered]

    def _save_machine_id_cache(self, cache_file, machine_id):  # [META]
        """保存machine_id到缓存文件（带本机指纹验证）"""
        # Referenced APIs: open, write
        pass  # [META only - no bytecode recovered]

    def _update_last_online(self):  # [META]
        """更新最后在线时间（带HMAC签名）"""
        # Referenced APIs: os, path, exists, activation_file, open, json, load, datetime, now, isoformat, dump, Exception, print
        # const: 'utf-8'
        # const: 'last_online'
        # const: 'hmac'
        # const: '更新在线时间失败: '
        pass  # [META only - no bytecode recovered]

    def _verify_cert_pin(self):  # [META]
        """验证服务器证书SPKI Pin（防止中间人攻击，即使安装了伪造CA证书）"""
        # Referenced APIs: server_url, startswith, ssl, socket, urllib.parse, urlparse, cryptography, x509, cryptography.hazmat.primitives.serialization, Encoding, PublicFormat, hostname, port, create_default_context, create_connection
        # const: 'https://'
        # const: 'get_verified_chain'
        # const: '证书固定验证失败! 期望Pin之一: '
        # const: '证书固定检查异常: '
        pass  # [META only - no bytecode recovered]

    def check_activation_status(self):  # [META]
        """检查本地激活状态（增强版：HMAC验证+安全检查）"""
        # Referenced APIs: perform_security_check, print, os, path, exists, activation_file, open, json, load, get, verify_signature, machine_id, datetime, fromisoformat, now
        # const: '安全检查失败: '
        # const: 'utf-8'
        # const: 'code'
        # const: 'expiry'
        # const: 'machine_id'
        pass  # [META only - no bytecode recovered]

    def clear_activation(self):  # [META]
        """清除激活信息"""
        # Referenced APIs: is_activated, activation_code, activation_expiry, os, path, exists, activation_file, remove
        pass  # [META only - no bytecode recovered]

    def get_config_key(self):  # [META]
        """获取配置解密密钥（方案A）"""
        # Referenced APIs: server_url, machine_id, API_SECRET_KEY, CLIENT_VERSION, status_code, json, get, verify_signature, Exception, str
        # const: '/v2/xK9mT2pQ8wR5/config_key'
        # const: 'success'
        # const: 'signature'
        # const: 'config_key'
        # const: 'valid_until'
        pass  # [META only - no bytecode recovered]

    def get_dynamic_api_path(self):  # [META]
        """获取动态API路径（带缓存和容错）"""
        # Referenced APIs: datetime, now, fromisoformat, server_url, API_SECRET_KEY, CLIENT_VERSION, status_code, json, get, verify_signature, isoformat, total_seconds
        # const: 'api_path'
        # const: 'valid_until'
        # const: '/config/get_api_path'
        # const: 'success'
        # const: 'signature'
        pass  # [META only - no bytecode recovered]

    def get_exec_token(self):  # [META]
        """获取执行令牌（方案B）"""
        # Referenced APIs: server_url, machine_id, API_SECRET_KEY, CLIENT_VERSION, status_code, json, get, verify_signature, Exception, str
        # const: '/v2/xK9mT2pQ8wR5/exec_token'
        # const: 'success'
        # const: 'signature'
        # const: 'exec_token'
        # const: 'valid_until'
        pass  # [META only - no bytecode recovered]

    def get_machine_id(self):  # [META]
        """获取机器唯一标识（基于C盘序列号，带缓存机制）"""
        # Referenced APIs: os, path, join, get_work_folder, exists, open, read, strip, split, len, subprocess, run, name, CREATE_NO_WINDOW, returncode
        # const: '.machine_id'
        # const: 'nt'
        # const: 'VolumeSerialNumber'
        # const: 'SerialNumber'
        # const: 'To be filled by O.E.M.'
        pass  # [META only - no bytecode recovered]

    def get_remaining_seconds(self):  # [META]
        """获取剩余总秒数，<=0 表示已过期"""
        # Referenced APIs: is_activated, activation_expiry, int, datetime, now, total_seconds
        pass  # [META only - no bytecode recovered]

    def get_remaining_time(self):  # [META]
        """获取剩余时间（含秒数）"""
        # Referenced APIs: is_activated, activation_expiry, datetime, now, int, total_seconds, days, seconds
        # const: '天 '
        # const: '未激活'
        pass  # [META only - no bytecode recovered]

    def get_unbind_status(self):  # [META]
        """获取解绑状态（冷却时间等）"""
        # Referenced APIs: activation_code, server_url, API_SECRET_KEY, status_code, json, get, Exception
        # const: '/unbind_status'
        # const: 'success'
        # const: 'can_unbind'
        # const: 'unbind_count'
        # const: 'remaining_days'
        pass  # [META only - no bytecode recovered]

    def unbind_device(self):  # [META]
        """手动解绑设备"""
        # Referenced APIs: activation_code, server_url, machine_id, API_SECRET_KEY, status_code, json, get, clear_activation, requests, exceptions, RequestException, Exception, str
        # const: '/unbind'
        # const: 'success'
        # const: 'message'
        # const: '解绑成功'
        # const: '解绑失败'
        pass  # [META only - no bytecode recovered]

    def verify_activation_code(self, code):  # [META]
        """验证激活码"""
        # Referenced APIs: server_url, machine_id, API_SECRET_KEY, CLIENT_VERSION, status_code, json, get, verify_signature, items, datetime, now, isoformat, open, activation_file, dump
        # const: '/v2/xK9mT2pQ8wR5/activate'
        # const: 'valid'
        # const: 'signature'
        # const: 'machine_id'
        # const: 'expiry'
        pass  # [META only - no bytecode recovered]

    def verify_activation_code_silent(self, code):  # [META]
        """静默验证激活码
返回: (success, message, server_reachable)
- server_reachable=True: 服务器有明确响应（成功或拒绝）
- server_reachable=False: 网络不可达/服务器故障"""
        # Referenced APIs: server_url, machine_id, API_SECRET_KEY, CLIENT_VERSION, status_code, json, get, verify_signature, requests, exceptions, RequestException, Exception
        # const: '/v2/xK9mT2pQ8wR5/activate'
        # const: 'valid'
        # const: 'signature'
        # const: 'machine_id'
        # const: 'message'
        pass  # [META only - no bytecode recovered]

    def verify_with_dynamic_api(self, code):  # [META]
        """使用动态API路径验证激活码"""
        # Referenced APIs: get_dynamic_api_path, verify_activation_code, server_url, machine_id, API_SECRET_KEY, CLIENT_VERSION, status_code, json, get, verify_signature, items, Exception, str
        # const: '/dyn/'
        # const: '/activate'
        # const: 'valid'
        # const: 'signature'
        # const: 'expiry'
        pass  # [META only - no bytecode recovered]

def get_work_folder():  # [DISASM]
    """获取工作目录（支持 PyInstaller 打包）"""
    # Referenced APIs: getattr, sys, os, path, dirname, executable, abspath
    # const: 'frozen'
    # === Bytecode Disassembly ===
    #  152           NOP
    #                NOP
    #                LOAD_CONST               2 (None)
    #                PUSH_NULL
    #  153           LOAD_CONST               3 (b'\xe0\xcbd\xffW\x02\x00\x00\x01\x00\x00\x1a,\x01\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RESUME                   0
    #                LOAD_CONST               1 (None)
    #                STORE_FAST               0 (__assert_armored__)
    #                NOP
    #                NOP
    #  152           NOP
    #  156   L1:     LOAD_GLOBAL              1 (getattr + NULL)
    #                LOAD_GLOBAL              2 (sys)
    #                LOAD_CONST               4 ('frozen')
    #                LOAD_CONST               5 (False)
    #                CALL                     3
    #                TO_BOOL
    #                POP_JUMP_IF_FALSE       54 (to L3)
    #  158           LOAD_GLOBAL              4 (os)
    #                LOAD_ATTR                6 (path)
    #                LOAD_ATTR                9 (dirname + NULL|self)
    #                LOAD_GLOBAL              2 (sys)
    #                LOAD_ATTR               10 (executable)
    #                CALL                     1
    #  160   L2:     NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD            93 (to L7)
    #                CALL                     1
    #                POP_TOP
    #                RETURN_VALUE
    #        L3:     LOAD_GLOBAL              4 (os)
    #                LOAD_ATTR                6 (path)
    #                LOAD_ATTR                9 (dirname + NULL|self)
    #                LOAD_GLOBAL              4 (os)
    #                LOAD_ATTR                6 (path)
    #                LOAD_ATTR               13 (abspath + NULL|self)
    #                LOAD_GLOBAL             14 (__file__)
    #                CALL                     1
    #                CALL                     1
    #        L4:     NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD            20 (to L7)
    #                CALL                     1
    #                POP_TOP
    #                RETURN_VALUE
    # Full: docs/FINAL_DISASSEMBLY/get_work_folder.dis
    pass  # [DISASM available above]

def verify_signature(data, signature):  # [META]
    """验证服务器响应的数字签名"""
    # Referenced APIs: serialization, load_pem_public_key, SERVER_PUBLIC_KEY_PEM, encode, default_backend, items, json, dumps, verify, base64, b64decode, padding, PKCS1v15, hashes, SHA256
    # const: 'utf-8'
    # const: 'signature'
    # const: '签名验证失败: '
    pass  # [META only]
