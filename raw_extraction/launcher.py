"""
6号自动化助手 - 离线独立版入口
打包前放置于 6hzsv2.23.exe_extracted 目录内
"""
import sys, os

# Fix Qt platform plugin path for PyInstaller frozen builds
if getattr(sys, 'frozen', False):
    base = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)
    qt_plugin = os.path.join(base, 'PyQt5', 'Qt5', 'plugins')
    if os.path.exists(qt_plugin):
        os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(qt_plugin, 'platforms')
        os.environ['QT_PLUGIN_PATH'] = qt_plugin
    # Add DLL search paths for Qt and pywin32
    os.add_dll_directory(os.path.join(base, 'PyQt5', 'Qt5', 'bin'))
    os.add_dll_directory(os.path.join(base, 'pywin32_system32'))
    os.add_dll_directory(base)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Pre-import all modules that PyArmor-protected code needs
# (PyArmor's frozen import can't find them otherwise)
import ctypes, hashlib, base64, time, threading, subprocess, platform, json, struct
import marshal, random, string, socket, getpass, webbrowser, re, functools, copy, io

import pyarmor_runtime_011372

# ========== PATCH: 安全模块 ==========
import security
security.init_security = lambda *a, **kw: None
security.perform_security_check = lambda: (True, '')
security.perform_full_security_check = lambda: (True, '')
security.security_check_with_warning = lambda: None
security.start_heartbeat = lambda *a, **kw: None
security.stop_heartbeat = lambda: None
security.verify_integrity = lambda: True
security.verify_time = lambda: True
security.is_heartbeat_valid = lambda: True
security.init_integrity_check = lambda: None
security.init_time_check = lambda: None
security._is_debugger_present = lambda: False
security._check_suspicious_processes = lambda: (False, '')
security._check_loaded_dlls = lambda: (False, '')
security._calculate_exe_hash = lambda: '0' * 64
security.clear_force_offline_reason = lambda: None
security.get_force_offline_reason = lambda: None
security.get_api_secret_key = lambda: 'OFFLINE_MODE'
security._SUSPICIOUS_PROCESSES = []
security._SUSPICIOUS_DLLS = []
security._VM_PROCESSES = []

# ========== PATCH: 激活模块 ==========
import activation

# Replace __init__ to set all needed instance attributes
_orig_init = activation.ActivationManager.__init__
def _patched_init(self, *a, **kw):
    self.is_activated = True
    self.activation_code = "OFFLINE-INTERNAL"
    self.activation_expiry = "2099-12-31T23:59:59"
    self.activation_file = None
activation.ActivationManager.__init__ = _patched_init

# Patch all other callable methods
activation.ActivationManager.check_activation_required = lambda *a, **kw: False
activation.ActivationManager._verify_activation_integrity = lambda *a, **kw: True
activation.ActivationManager.get_remaining_time = lambda *a, **kw: "永久有效"
activation.ActivationManager.get_remaining_seconds = lambda *a, **kw: 999999999
activation.ActivationManager.is_heartbeat_valid = lambda *a, **kw: True
activation.ActivationManager.perform_security_check = lambda *a, **kw: (True, '')
activation.ActivationManager.get_api_secret_key = lambda *a, **kw: 'OFFLINE'
activation.ActivationManager.get_work_folder = lambda *a, **kw: os.path.dirname(sys.executable)
activation.ActivationManager.get_machine_id = lambda *a, **kw: 'INTERNAL'
activation.ActivationManager.verify_signature = lambda *a, **kw: True
activation.ActivationManager.get_dynamic_api_path = lambda *a, **kw: ('', '', '')
activation.ActivationManager.get_config_key = lambda *a, **kw: (True, None, '')
activation.ActivationManager.get_exec_token = lambda *a, **kw: (True, None, '')
activation.ActivationManager.get_remaining_days = lambda *a, **kw: 999
activation.ActivationManager.get_unbind_status = lambda *a, **kw: (0, False, 999)
activation.ActivationManager.check_activation_status = lambda *a, **kw: (True, 'OK')
activation.ActivationManager.unbind_device = lambda *a, **kw: (True, 'OK')
# All remaining -> no-op
for name in dir(activation.ActivationManager):
    if name.startswith('__'):
        continue
    attr = getattr(activation.ActivationManager, name, None)
    if callable(attr) and not isinstance(attr, type(lambda:0)):
        setattr(activation.ActivationManager, name, lambda *a, **kw: None)
activation.is_heartbeat_valid = lambda: True
activation.perform_security_check = lambda: (True, '')
activation.start_heartbeat = lambda *a, **kw: None
activation.verify_signature = lambda *a, **kw: True

# ========== PATCH: 主程序 ==========
import main_pyqt_v3
main_pyqt_v3.VERSION_CHECK_URL = 'http://127.0.0.1:1/nonexistent'

# Patch MainWindow activation methods
main_pyqt_v3.MainWindow.check_activation_required = lambda self: True
main_pyqt_v3.MainWindow.check_activation = lambda self: None
main_pyqt_v3.MainWindow._verify_activation_integrity = lambda self: True
main_pyqt_v3.MainWindow.show_activation_dialog = lambda self: None
main_pyqt_v3.MainWindow.update_activation_display = lambda self: None

# Wrap MainWindow.__init__ to fix integrity check attributes AFTER init runs
_orig_main_init = main_pyqt_v3.MainWindow.__init__
def _wrapped_main_init(self, *a, **kw):
    _orig_main_init(self, *a, **kw)
    # Fix attributes that start_execution checks
    self._security_module_loaded = True
    self._orig_func_ids = ()
    self._orig_requests_ids = ()
    self._orig_activation_ids = ()
    self._orig_code_ids = ()
    # Ensure activation object works
    if hasattr(self, 'activation'):
        self.activation.is_activated = True
main_pyqt_v3.MainWindow.__init__ = _wrapped_main_init

# Patch module-level security/network checks
main_pyqt_v3.perform_full_security_check = lambda: (True, '')
main_pyqt_v3.init_security = lambda *a, **kw: None
main_pyqt_v3.is_heartbeat_valid = lambda: True

# ========== 启动 ==========
print("6号自动化助手 - 内部离线版 v2.23")
print("已移除: 激活/安全检测/心跳/版本检查")
main_pyqt_v3.main()
