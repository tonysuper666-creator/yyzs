"""
6号自动化助手 - main_pyqt_v3.py

状态说明:
  - 函数签名/参数名/字符串常量/引用的API: 100%% 准确
  - 标记 [DISASM] 的函数: 有完整字节码反汇编
  - 标记 [META] 的函数: 仅元数据，无字节码
  - editor/ 目录: 100%% 原始源码
"""

class CoordOverlay:
    """Reconstructed from PyArmor-protected bytecode."""

    def closeEvent(self, event):  # [DISASM]
        # Referenced APIs: timer, stop, super, closeEvent
        #
        # === Bytecode Disassembly ===
        #     # Raw bytecode (174 bytes):
        #     #   0000: 3e 01 1e c5 1e fe 53 02 22 00 53 03 34 01 36 00  >.....S.".S.4.6.
        #     #   0010: 20 00 95 00 53 01 6e 02 1e 41 1e 15 00 c0 05 79   ...S.n..A.....y
        #     #   0020: 00 00 36 f8 6e 13 35 dc 00 00 00 00 00 00 19 a6  ..6.n.5.........
        #     #   0030: 28 8b 00 00 00 00 00 00 3a 91 00 00 76 be 95 99  (.......:...v...
        #     #   0040: 26 dc 61 4a 00 00 6e 4f 08 37 00 fd 35 d4 00 00  &.aJ..nO.7..5...
        #     #   0050: 00 00 00 00 35 cf 00 00 00 00 00 00 00 26 28 dc  ....5........&(.
        #     #   0060: 00 00 00 00 00 00 6d 94 26 61 19 d9 39 ad 67 d4  ......m.&a..9.g.
        #     #   0070: 35 a7 00 00 00 00 00 00 00 19 33 5d 00 84 4b f2  5.........3]..K.
        #     #   0080: 49 c2 5d db 00 00 53 04 1e 00 22 00 53 03 35 01  I.]...S...".S.5.
        #     #   0090: 00 00 00 00 00 00 20 00 66 00 3d 03 1f 00 66 01  ...... .f.=...f.
        #     #   00a0: 53 04 22 00 53 03 34 01 36 00 20 00 24 00        S.".S.4.6. .$.
        # Full disassembly: docs/FINAL_DISASSEMBLY/closeEvent.dis
        pass  # [DISASM available above]

    def update_position(self):  # [DISASM]
        # Referenced APIs: CoordOverlay, pyautogui, position, label, setText, move
        #
        # === Bytecode Disassembly ===
        #     # Raw bytecode (346 bytes):
        #     #   0000: 1e c2 1e c7 53 02 22 00 53 03 34 01 36 00 20 00  ....S.".S.4.6. .
        #     #   0010: 95 00 53 01 6e 01 1e 00 1e e9 00 2c 35 40 00 00  ..S.n......,5@..
        #     #   0020: 00 00 00 00 5e 3e 05 3b 00 00 00 74 10 8d 11 fe  ....^>.;...t....
        #     #   0030: 6c 4d 00 00 00 00 00 00 00 00 0b 59 52 87 00 00  lM.........YR...
        #     #   0040: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
        #     #   0050: 00 ae 40 24 1c 42 1d 50 00 f0 41 b4 34 5c 35 8b  ..@$.B.P..A.4\5.
        #     #   0060: 00 00 00 00 00 00 4d d1 00 00 76 49 69 6a 1c c9  ......M...vIij..
        #     #   0070: 00 e7 6c 38 00 00 00 00 00 00 00 00 66 07 35 7e  ..l8........f.5~
        #     #   0080: 00 00 00 00 00 00 52 ad 00 00 00 00 00 00 00 00  ......R.........
        #     #   0090: 00 00 00 00 00 00 00 00 00 00 00 0d 35 e9 00 00  ............5...
        #     #   00a0: 00 00 00 00 3a 0f 00 00 1e 2a 00 6c 56 8c 1f 1e  ....:....*.lV...
        #     #   00b0: 28 34 00 00 00 00 00 00 39 1c 00 15 2d fd 00 00  (4......9...-...
        #     #   00c0: 35 af 00 00 00 00 00 00 5e 24 00 73 2f e0 2e 8c  5.......^$.s/...
        #     #   00d0: 52 c7 00 00 00 00 00 00 00 00 00 00 00 00 00 00  R...............
        #     #   00e0: 00 00 00 00 1c e9 16 1d 75 d0 00 00 35 94 00 00  ........u...5...
        #     #   00f0: 00 00 00 00 62 a6 00 00 39 a5 5d 81 00 00 4f c9  ....b...9.]...O.
        #     #   0100: 05 4a 00 00 00 2c 00 2c 38 7b 51 39 35 e4 00 00  .J...,.,8{Q95...
        #     #   0110: 00 00 00 00 2d 6a 00 00 3a 81 00 00 56 72 52 f1  ....-j..:...VrR.
        #     #   0120: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
        #     #   0130: 00 00 53 07 1e 00 22 00 53 03 35 01 00 00 00 00  ..S...".S.5.....
        #     #   0140: 00 00 20 00 66 00 3d 03 1f 00 66 01 53 07 22 00  .. .f.=...f.S.".
        #     #   0150: 53 03 34 01 36 00 20 00 24 00                    S.4.6. .$.
        # Full disassembly: docs/FINAL_DISASSEMBLY/update_position.dis
        pass  # [DISASM available above]

class MainWindow:
    """Reconstructed from PyArmor-protected bytecode."""

    def _append_log(self, text):  # [META]
        # Referenced APIs: log_text, append, verticalScrollBar, setValue, maximum
        pass  # [META only - no bytecode recovered]

    def _apply_countdown_style(self, remaining_secs):  # [META]
        """根据剩余秒数设置倒计时样式颜色"""
        # Referenced APIs: activation_label, setStyleSheet
        # const: 'rgba(34, 197, 94, 0.3)'
        # const: '#86efac'
        # const: 'rgba(245, 158, 11, 0.3)'
        # const: '#fcd34d'
        # const: 'rgba(239, 68, 68, 0.3)'
        pass  # [META only - no bytecode recovered]

    def _check_editable_updates(self):  # [META]
        """检查可编辑配置是否有更新"""
        # Referenced APIs: web_server, get_updated_workflow, current_workflow, add_log, stop
        # const: '✅ 自定义配置已同步更新并保存'
        pass  # [META only - no bytecode recovered]

    def _check_force_offline(self):  # [META]
        """快速检查服务端强制下线通知（每5秒，配合10秒心跳实现近实时下线）"""
        # Referenced APIs: hasattr, activation, is_activated, get_force_offline_reason, clear_force_offline_reason, add_log, engine, is_running, stop_execution, update_activation_display, show_activation_dialog
        # const: 'activation'
        # const: '⚠️ '
        pass  # [META only - no bytecode recovered]

    def _copy_images_from_folder(self, folder):  # [META]
        """从文件夹复制所有图片"""
        # Referenced APIs: shutil, os, listdir, path, join, isfile, copy2, images_folder
        pass  # [META only - no bytecode recovered]

    def _copy_workflows_from_folder(self, folder):  # [META]
        """从文件夹复制所有配置文件（JSON 和加密 ENC）"""
        # Referenced APIs: shutil, os, listdir, lower, endswith, path, join, isfile, copy2, workflows_folder
        pass  # [META only - no bytecode recovered]

    def _decrypt_config_file(self, filepath):  # [META]
        """解密加密配置文件，返回 (配置数据, 是否可编辑)"""
        # Referenced APIs: base64, hashlib, cryptography.hazmat.primitives.ciphers, Cipher, algorithms, modes, cryptography.hazmat.backends, default_backend, bytes, sha256, digest, open, read, startswith, len
        # const: 'rb'
        # const: '无效的加密文件格式'
        # const: '解密数据为空'
        # const: '无效的填充长度'
        # const: 'PKCS7填充验证失败，文件可能已损坏'
        pass  # [META only - no bytecode recovered]

    def _do_detect_window(self):  # [META]
        """实际执行窗口检测"""
        # Referenced APIs: ctypes, ctypes.wintypes, win32gui, win32process, psutil, wintypes, POINT, windll, user32, GetCursorPos, byref, WindowFromPoint, x, y, GetParent
        # const: '(无标题)'
        # const: '✅ 检测成功！点击复制按钮可复制对应内容'
        # const: 'color: #10b981; font-size: 13px;'
        # const: '❌ 未检测到窗口'
        # const: 'color: #ef4444; font-size: 13px;'
        pass  # [META only - no bytecode recovered]

    def _encrypt_and_save_config(self, data, filepath, is_editable):  # [META]
        """加密并保存配置文件"""
        # Referenced APIs: base64, hashlib, cryptography.hazmat.primitives.ciphers, Cipher, algorithms, modes, cryptography.hazmat.backends, default_backend, current_workflow, get, bytes, sha256, digest, json, dumps
        # const: '_enc_editable'
        # const: 'utf-8'
        # const: 'wb'
        pass  # [META only - no bytecode recovered]

    def _extract_archive(self, archive_path, extract_to):  # [META]
        """解压压缩包到指定目录"""
        # Referenced APIs: tempfile, os, path, basename, lower, endswith, zipfile, ZipFile, namelist, realpath, join, startswith, sep, add_log, extractall
        # const: '.zip'
        # const: '⚠️ 检测到不安全的压缩包路径: '
        # const: '.rar'
        # const: '⚠️ 需要安装 rarfile 库来解压 RAR 文件: pip install rarfile'
        # const: '.7z'
        pass  # [META only - no bytecode recovered]

    def _is_archive_file(self, filename):  # [META]
        """判断是否是压缩包文件"""
        # Referenced APIs: lower, endswith
        pass  # [META only - no bytecode recovered]

    def _is_image_file(self, filename):  # [META]
        """判断是否是图片文件"""
        # Referenced APIs: lower, endswith
        pass  # [META only - no bytecode recovered]

    def _on_screenshot_cancelled(self):  # [META]
        """截图取消"""
        # Referenced APIs: show, screenshot_window
        pass  # [META only - no bytecode recovered]

    def _on_screenshot_done(self, filepath):  # [META]
        """截图完成"""
        # Referenced APIs: show, add_log, os, path, basename, screenshot_window
        # const: '截图已保存: '
        pass  # [META only - no bytecode recovered]

    def _periodic_security_check(self):  # [META]
        """定期安全检查（带容错+反Hook检测）"""
        # Referenced APIs: id, perform_full_security_check, add_log, engine, is_running, stop_execution, is_heartbeat_valid, getattr, start_heartbeat, requests, post, Session, hasattr, activation, activation_expiry
        # const: '⚠️ 检测到安全模块异常'
        # const: '__code__'
        # const: 'verify_signature'
        # const: '_verify_local_hmac'
        # const: '⚠️ 检测到验证模块异常'
        pass  # [META only - no bytecode recovered]

    def _process_extracted_folder(self, folder):  # [META]
        """处理解压后的文件夹，返回 (图片数, 配置数)"""
        # Referenced APIs: shutil, os, walk, path, basename, lower, join, copy2, images_folder, endswith, workflows_folder
        # const: 'images'
        # const: 'workflows'
        # const: '.json'
        # const: '.enc'
        pass  # [META only - no bytecode recovered]

    def _refresh_hotkeys(self):  # [META]
        """定时刷新快捷键，防止失效"""
        # Referenced APIs: register_hotkeys, Exception, print
        # const: '刷新快捷键失败: '
        pass  # [META only - no bytecode recovered]

    def _save_current_workflow(self):  # [META]
        """保存当前workflow到文件"""
        # Referenced APIs: current_workflow, hasattr, current_workflow_path, items, startswith, endswith, open, json, dump, Exception, add_log
        # const: 'current_workflow_path'
        # const: '.enc'
        # const: 'utf-8'
        # const: '⚠️ 保存配置失败: '
        pass  # [META only - no bytecode recovered]

    def _show_import_result(self, images, workflows, errors):  # [META]
        """显示导入结果"""
        # Referenced APIs: show_message, len, refresh_workflow_list
        # const: '导入失败'
        # const: '未找到可导入的文件\n\n支持的格式：\n• 图片：png, jpg, jpeg, bmp\n• 配置：json'
        # const: 'warning'
        # const: '✅ 导入完成！\n\n'
        # const: '📷 图片: '
        pass  # [META only - no bytecode recovered]

    def _start_editable_update_checker(self):  # [META]
        """启动定时检查可编辑配置更新"""
        # Referenced APIs: hasattr, PyQt5.QtCore, QTimer, timeout, connect, start
        # const: '_editable_check_timer'
        pass  # [META only - no bytecode recovered]

    def _start_screenshot(self):  # [META]
        """启动截图窗口"""
        # Referenced APIs: ScreenshotWindow, images_folder, screenshot_window, screenshot_taken, connect, screenshot_cancelled
        pass  # [META only - no bytecode recovered]

    def _update_countdown(self):  # [META]
        """更新倒计时"""
        # Referenced APIs: detect_countdown, detect_status_label, setText, countdown_timer, stop
        # const: '⏱️ '
        # const: ' 秒后检测，请将鼠标移到目标窗口...'
        # const: '🔍 正在检测...'
        pass  # [META only - no bytecode recovered]

    def _update_expiry_countdown(self):  # [META]
        """每秒更新到期倒计时显示"""
        # Referenced APIs: hasattr, activation, is_activated, stop, get_remaining_seconds, activation_label, setText, setStyleSheet, add_log, engine, is_running, stop_execution, start_btn, setEnabled, get_remaining_time
        # const: 'activation'
        # const: '❌ 已过期'
        # const: '⏰ 激活码已到期，自动停止运行'
        # const: 'engine'
        pass  # [META only - no bytecode recovered]

    def _update_workflow_display(self):  # [META]
        """更新工作流显示"""
        # Referenced APIs: current_workflow, get, sum, hasattr, len, config_stats_label, setText
        # const: 'groups'
        # const: 'config_stats_label'
        # const: 'default_group'
        # const: 'name'
        # const: '组合 1'
        pass  # [META only - no bytecode recovered]

    def _verify_activation_integrity(self):  # [META]
        """验证激活完整性（内联HMAC验证，防止函数Hook和属性篡改）"""
        # Referenced APIs: json, hmac, hashlib, os, path, exists, activation, activation_file, open, load, get, bytes, items, dumps, encode
        # const: 'utf-8'
        # const: 'hmac'
        # const: 'machine_id'
        # const: 'signed_data'
        # const: 'expiry'
        pass  # [META only - no bytecode recovered]

    def add_log(self, message):  # [META]
        """log_enabled"""
        # Referenced APIs: hasattr, log_enabled, datetime, now, strftime, log_signal, emit
        # const: '%H:%M:%S'
        # const: '] '
        pass  # [META only - no bytecode recovered]

    def auto_clear_log(self):  # [META]
        """自动清理日志"""
        # Referenced APIs: log_text, clear, add_log
        # const: '日志已自动清理（每6小时）'
        pass  # [META only - no bytecode recovered]

    def check_activation(self):  # [META]
        # Referenced APIs: activation, check_activation_status, update_activation_display, show_activation_dialog
        pass  # [META only - no bytecode recovered]

    def check_activation_required(self):  # [META]
        """检查激活状态（增强版：多重验证）"""
        # Referenced APIs: activation, is_activated, show_activation_dialog, perform_full_security_check, is_heartbeat_valid, add_log
        # const: '⚠️ 网络验证失败'
        pass  # [META only - no bytecode recovered]

    def check_version(self):  # [META]
        """检测软件版本更新"""
        # Referenced APIs: threading, Thread, start
        pass  # [META only - no bytecode recovered]

    def clear_log(self):  # [META]
        # Referenced APIs: log_text, clear
        pass  # [META only - no bytecode recovered]

    def closeEvent(self, event):  # [DISASM]
        """coord_overlay"""
        # Referenced APIs: getattr, stop, hasattr, coord_overlay, close, mini_window, engine, web_server, hotkey_hooks, keyboard, remove_hotkey, accept
        # const: 'mini_window'
        #
        # === Bytecode Disassembly ===
        #     # Raw bytecode (174 bytes):
        #     #   0000: 3e 01 1e c5 1e fe 53 02 22 00 53 03 34 01 36 00  >.....S.".S.4.6.
        #     #   0010: 20 00 95 00 53 01 6e 02 1e 41 1e 15 00 c0 05 79   ...S.n..A.....y
        #     #   0020: 00 00 36 f8 6e 13 35 dc 00 00 00 00 00 00 19 a6  ..6.n.5.........
        #     #   0030: 28 8b 00 00 00 00 00 00 3a 91 00 00 76 be 95 99  (.......:...v...
        #     #   0040: 26 dc 61 4a 00 00 6e 4f 08 37 00 fd 35 d4 00 00  &.aJ..nO.7..5...
        #     #   0050: 00 00 00 00 35 cf 00 00 00 00 00 00 00 26 28 dc  ....5........&(.
        #     #   0060: 00 00 00 00 00 00 6d 94 26 61 19 d9 39 ad 67 d4  ......m.&a..9.g.
        #     #   0070: 35 a7 00 00 00 00 00 00 00 19 33 5d 00 84 4b f2  5.........3]..K.
        #     #   0080: 49 c2 5d db 00 00 53 04 1e 00 22 00 53 03 35 01  I.]...S...".S.5.
        #     #   0090: 00 00 00 00 00 00 20 00 66 00 3d 03 1f 00 66 01  ...... .f.=...f.
        #     #   00a0: 53 04 22 00 53 03 34 01 36 00 20 00 24 00        S.".S.4.6. .$.
        # Full disassembly: docs/FINAL_DISASSEMBLY/closeEvent.dis
        pass  # [DISASM available above]

    def copy_to_clipboard(self, text):  # [META]
        """复制到剪贴板"""
        # Referenced APIs: PyQt5.QtWidgets, QApplication, clipboard, setText, detect_status_label, setStyleSheet
        # const: '📋 已复制: '
        # const: 'color: #6366f1; font-size: 13px;'
        pass  # [META only - no bytecode recovered]

    def delete_selected_workflow(self):  # [META]
        """删除选中的配置文件"""
        # Referenced APIs: config_combo, currentData, show_message, os, path, basename, PyQt5.QtWidgets, QMessageBox, setWindowTitle, setText, setInformativeText, setIcon, Warning, setStandardButtons, Yes
        # const: '提示'
        # const: '请先选择要删除的配置文件'
        # const: 'warning'
        # const: '确认删除'
        # const: '确定要删除配置文件吗？\n\n📄 '
        pass  # [META only - no bytecode recovered]

    def detect_window_info(self):  # [META]
        """检测窗口信息"""
        # Referenced APIs: detect_countdown, detect_status_label, setText, setStyleSheet, window_info_frame, setVisible, PyQt5.QtCore, QTimer, countdown_timer, timeout, connect, start
        # const: '⏱️ 3 秒后检测，请将鼠标移到目标窗口...'
        # const: 'color: #f59e0b; font-size: 13px;'
        pass  # [META only - no bytecode recovered]

    def import_drag_enter(self, event):  # [META]
        """拖拽进入事件"""
        # Referenced APIs: mimeData, hasUrls, acceptProposedAction
        pass  # [META only - no bytecode recovered]

    def import_drop(self, event):  # [META]
        """拖拽放下事件"""
        # Referenced APIs: mimeData, urls, toLocalFile, process_import_paths
        pass  # [META only - no bytecode recovered]

    def load_hotkey_settings(self):  # [META]
        """utf-8"""
        # Referenced APIs: os, path, exists, settings_file, open, json, load, hotkeys, update, Exception, print
        # const: 'hotkeys'
        # const: '加载快捷键设置失败: '
        pass  # [META only - no bytecode recovered]

    def load_last_workflow(self):  # [META]
        """加载上次的配置"""
        # Referenced APIs: os, path, exists, settings_file, open, json, load, get, load_workflow_file, Exception, print
        # const: 'utf-8'
        # const: 'last_workflow'
        # const: '加载上次配置失败: '
        pass  # [META only - no bytecode recovered]

    def load_screenshot_settings(self):  # [META]
        """加载截图设置"""
        # Referenced APIs: os, path, join, get_app_path, exists, open, json, load, screenshot_local_mode, setChecked, get, screenshot_position, setCurrentIndex, screenshot_resolution, screenshot_max_count
        # const: 'screenshot_settings.json'
        # const: 'utf-8'
        # const: 'local_mode'
        # const: 'position'
        # const: 'center'
        pass  # [META only - no bytecode recovered]

    def load_selected_workflow(self):  # [META]
        """加载选中的配置"""
        # Referenced APIs: check_activation_required, config_combo, currentData, show_message, load_workflow_file
        # const: '提示'
        # const: '请先选择配置文件'
        # const: 'warning'
        pass  # [META only - no bytecode recovered]

    def load_workflow_file(self, filepath):  # [META]
        """加载配置文件（支持加密 .enc 文件）"""
        # Referenced APIs: endswith, Exception, show_message, engine, load_workflow, current_workflow, current_workflow_path, get, os, path, basename, config_name_label, setText, len, sum
        # const: '.enc'
        # const: '_encrypted'
        # const: '_enc_editable'
        # const: '错误'
        # const: '解密配置文件失败: '
        pass  # [META only - no bytecode recovered]

    def mouseMoveEvent(self, event):  # [META]
        # Referenced APIs: buttons, Qt, LeftButton, move, globalPos
        pass  # [META only - no bytecode recovered]

    def mousePressEvent(self, event):  # [META]
        # Referenced APIs: button, Qt, LeftButton, globalPos, frameGeometry, topLeft
        pass  # [META only - no bytecode recovered]

    def mouseReleaseEvent(self, event):  # [META]
        pass  # [META only - no bytecode recovered]

    def on_execution_complete(self):  # [META]
        """暂停 (F11)"""
        # Referenced APIs: start_btn, setEnabled, stop_btn, pause_btn, setText, setToolTip
        pass  # [META only - no bytecode recovered]

    def open_config_encryptor(self):  # [META]
        """打开配置文件加密工具"""
        # Referenced APIs: PyQt5.QtWidgets, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFileDialog, QTextEdit, QGroupBox, PyQt5.QtCore, Qt, PyQt5.QtGui, QFont, base64, hashlib
        # const: 'EncryptorDialog'
        pass  # [META only - no bytecode recovered]

    def open_custom_config_editor(self):  # [META]
        """打开自定义配置编辑器（仅用于enc加密配置）"""
        # Referenced APIs: check_activation_required, current_workflow, show_message, get, web_server, set_editable_config, get_url, webbrowser, open, add_log
        # const: '提示'
        # const: '请先加载配置文件'
        # const: 'warning'
        # const: 'editable_config'
        # const: 'enabled'
        pass  # [META only - no bytecode recovered]

    def open_editor(self):  # [META]
        """_encrypted"""
        # Referenced APIs: check_activation_required, web_server, get_url, current_workflow_path, os, path, basename, current_workflow, get, set_current_workflow, show_message, webbrowser, open, add_log
        # const: '_enc_editable'
        # const: '提示'
        # const: '正式版加密配置不能在编辑器中打开'
        # const: 'warning'
        # const: '?open='
        pass  # [META only - no bytecode recovered]

    def open_screenshot_folder(self):  # [META]
        """打开截图文件夹"""
        # Referenced APIs: os, path, join, get_app_path, exists, makedirs, startfile
        # const: 'jt'
        pass  # [META only - no bytecode recovered]

    def process_import_paths(self, paths):  # [META]
        """处理导入的路径列表"""
        # Referenced APIs: shutil, os, path, exists, isdir, basename, lower, join, listdir, isfile, copy2, images_folder, Exception, append, endswith
        # const: 'images'
        # const: 'workflows'
        # const: ': '
        # const: '📦 正在解压: '
        # const: '✅ 解压完成: '
        pass  # [META only - no bytecode recovered]

    def refresh_workflow_list(self):  # [META]
        """刷新配置文件列表"""
        # Referenced APIs: config_combo, clear, addItem, glob, os, path, join, workflows_folder, sorted, basename, endswith, get, replace, open, json
        # const: '-- 请选择配置文件 --'
        # const: '*.json'
        # const: '*.enc'
        # const: '.enc'
        # const: ' 🔒'
        pass  # [META only - no bytecode recovered]

    def register_hotkeys(self, silent):  # [META]
        """screenshot"""
        # Referenced APIs: hotkey_hooks, keyboard, remove_hotkey, clear, hotkeys, get, add_hotkey, append, add_log, join, Exception
        # const: '截图='
        # const: 'start'
        # const: '开始='
        # const: 'pause'
        # const: '暂停='
        pass  # [META only - no bytecode recovered]

    def save_log(self):  # [META]
        """保存日志"""
        # Referenced APIs: QFileDialog, getSaveFileName, open, write, log_text, toPlainText, add_log
        # const: '文本文件 (*.txt)'
        # const: 'utf-8'
        # const: '日志已保存: '
        pass  # [META only - no bytecode recovered]

    def save_screenshot_settings(self, dialog):  # [META]
        """保存截图设置"""
        # Referenced APIs: screenshot_local_mode, isChecked, get, screenshot_position, currentIndex, screenshot_resolution, screenshot_max_count, value, screenshot_prefix, text, screenshot_quality, screenshot_push_enabled, push_api_key, strip, b64encode
        # const: 'center'
        # const: 'top_left'
        # const: 'top_right'
        # const: 'bottom_left'
        # const: 'bottom_right'
        pass  # [META only - no bytecode recovered]

    def save_settings(self, settings):  # [META]
        """utf-8"""
        # Referenced APIs: os, path, exists, settings_file, open, json, load, update, dump, Exception, print
        # const: '保存设置失败: '
        pass  # [META only - no bytecode recovered]

    def select_import_files(self):  # [META]
        """点击选择文件导入"""
        # Referenced APIs: QFileDialog, setFileMode, ExistingFiles, setNameFilter, setWindowTitle, exec_, selectedFiles, process_import_paths
        # const: '选择要导入的文件或压缩包'
        pass  # [META only - no bytecode recovered]

    def setup_home_page(self):  # [META]
        """主页 - 配置选择和信息"""
        # Referenced APIs: QWidget, QVBoxLayout, setContentsMargins, setSpacing, QLabel, setObjectName, addWidget, QFrame, QHBoxLayout, QComboBox, config_combo, setMinimumWidth, view, setStyleSheet, QPushButton
        # const: '主页'
        # const: 'pageTitle'
        # const: 'configSelector'
        # const: '📄 配置文件:'
        # const: 'configCombo'
        pass  # [META only - no bytecode recovered]

    def setup_log_page(self):  # [META]
        """日志页面"""
        # Referenced APIs: QWidget, QVBoxLayout, setContentsMargins, setSpacing, QLabel, setObjectName, addWidget, QFrame, QHBoxLayout, addStretch, QPushButton, clicked, connect, clear_log, save_log
        # const: '执行日志'
        # const: 'pageTitle'
        # const: 'logPanel'
        # const: 'logHeader'
        # const: '📋 完整日志记录'
        pass  # [META only - no bytecode recovered]

    def setup_main_content(self, parent_layout):  # [META]
        """mainContent"""
        # Referenced APIs: QFrame, setObjectName, QVBoxLayout, setContentsMargins, setSpacing, setup_window_controls, QStackedWidget, pages, setup_home_page, setup_log_page, setup_tools_page, addWidget
        pass  # [META only - no bytecode recovered]

    def setup_sidebar(self, parent_layout):  # [META]
        """sidebar"""
        # Referenced APIs: QFrame, setObjectName, QVBoxLayout, setContentsMargins, setSpacing, QWidget, QHBoxLayout, QLabel, os, path, join, bundle_folder, exists, QPixmap, scaled
        # const: '006.ico'
        # const: '6号助手'
        # const: 'sidebarTitle'
        # const: '📢 正版QQ群: 1082696738'
        pass  # [META only - no bytecode recovered]

    def setup_tools_page(self):  # [META]
        """工具页面"""
        # Referenced APIs: QWidget, QVBoxLayout, setContentsMargins, setSpacing, QLabel, setObjectName, addWidget, QHBoxLayout, QPushButton, setFixedSize, clicked, connect, take_screenshot, detect_window_info, show_dpi_setting
        # const: '工具箱'
        # const: 'pageTitle'
        # const: '📷 截图'
        # const: '🔍 检测窗口'
        # const: '🎮 设置DPI'
        pass  # [META only - no bytecode recovered]

    def setup_ui(self):  # [META]
        # Referenced APIs: QWidget, setCentralWidget, QHBoxLayout, setContentsMargins, setSpacing, setup_sidebar, setup_main_content
        pass  # [META only - no bytecode recovered]

    def setup_window_controls(self, parent_layout):  # [META]
        """windowControls"""
        # Referenced APIs: QFrame, setObjectName, setFixedHeight, QHBoxLayout, setContentsMargins, addStretch, QPushButton, clicked, connect, showMinimized, addWidget, max_btn, toggle_maximize, close
        # const: 'closeBtn'
        pass  # [META only - no bytecode recovered]

    def show_activation_dialog(self):  # [META]
        """软件激活"""
        # Referenced APIs: QDialog, setWindowTitle, setWindowFlags, windowFlags, Qt, FramelessWindowHint, setFixedSize, setStyleSheet, QVBoxLayout, setContentsMargins, setSpacing, QHBoxLayout, addStretch, QPushButton, clicked
        # const: 'background: transparent; font-size: 14px;'
        # const: '🔐 软件激活'
        # const: 'Microsoft YaHei UI'
        # const: '✅ 已激活，剩余: '
        pass  # [META only - no bytecode recovered]

    def show_dpi_setting(self):  # [META]
        """显示DPI设置对话框"""
        # Referenced APIs: PyQt5.QtWidgets, QInputDialog, engine, fps_user_dpi, fps_standard_dpi, getInt, save_fps_dpi_config, QMessageBox, information, int
        # const: '设置鼠标DPI'
        # const: '请输入你的鼠标DPI值:\n\n当前DPI: '
        # const: '\n标准DPI: '
        # const: '\n当前倍率: '
        # const: '.2f'
        pass  # [META only - no bytecode recovered]

    def show_hotkey_settings(self):  # [META]
        """快捷键设置"""
        # Referenced APIs: QDialog, setWindowTitle, setWindowFlags, windowFlags, Qt, FramelessWindowHint, setFixedSize, setStyleSheet, QVBoxLayout, setContentsMargins, setSpacing, QHBoxLayout, addStretch, QPushButton, clicked
        # const: 'background: transparent; font-size: 12px;'
        # const: '⌨️ 快捷键设置'
        # const: 'Microsoft YaHei UI'
        # const: 'HotkeyLineEdit'
        pass  # [META only - no bytecode recovered]

    def show_screenshot_settings(self):  # [META]
        """显示截图设置对话框"""
        # Referenced APIs: PyQt5.QtWidgets, QGroupBox, QFormLayout, QSpinBox, QDialog, QCheckBox, setWindowTitle, setFixedSize, setStyleSheet, QVBoxLayout, setSpacing, setContentsMargins, screenshot_local_mode, setChecked, addWidget
        # const: '截图设置'
        # const: '📁 本地保存截图'
        # const: '截图位置:'
        # const: '分辨率:'
        pass  # [META only - no bytecode recovered]

    def show_update_notice(self, latest_version):  # [META]
        """显示更新提示"""
        # Referenced APIs: show_message, CURRENT_VERSION
        # const: '🆕 版本更新提示'
        # const: '发现新版本！\n\n当前版本: '
        # const: '\n最新版本: '
        # const: '\n\n请前往官网下载最新版本。'
        # const: 'info'
        pass  # [META only - no bytecode recovered]

    def show_workflow_detail(self):  # [META]
        """查看配置详情"""
        # Referenced APIs: current_workflow, get, webbrowser, open
        # const: 'detail_url'
        pass  # [META only - no bytecode recovered]

    def start_execution(self):  # [META]
        """⚠️ 激活验证失败"""
        # Referenced APIs: engine, is_running, check_activation_required, add_log, hasattr, security_timer, isActive, id, perform_full_security_check, requests, post, current_workflow, show_message, start_btn, setEnabled
        # const: 'security_timer'
        # const: '⚠️ 安全检查异常'
        # const: '⚠️ 安全模块异常'
        # const: '⚠️ 网络模块异常'
        # const: '提示'
        pass  # [META only - no bytecode recovered]

    def start_log_cleanup_timer(self):  # [META]
        """启动日志定时清理（每6小时）"""
        # Referenced APIs: QTimer, log_cleanup_timer, timeout, connect, auto_clear_log, start
        pass  # [META only - no bytecode recovered]

    def stop_execution(self):  # [META]
        """已停止执行"""
        # Referenced APIs: engine, stop, add_log, on_execution_complete
        pass  # [META only - no bytecode recovered]

    def switch_page(self, index):  # [META]
        """active"""
        # Referenced APIs: pages, setCurrentIndex, enumerate, nav_buttons, setProperty, setStyle, style
        pass  # [META only - no bytecode recovered]

    def switch_to_mini_mode(self):  # [META]
        """切换到迷你模式"""
        # Referenced APIs: geometry, main_geometry, hide, MiniWindow, mini_window, show
        pass  # [META only - no bytecode recovered]

    def switch_to_normal_mode(self):  # [META]
        """从迷你模式切换回正常模式"""
        # Referenced APIs: hasattr, mini_window, close, setGeometry, main_geometry, show
        # const: 'mini_window'
        # const: 'main_geometry'
        pass  # [META only - no bytecode recovered]

    def take_screenshot(self):  # [META]
        """截图 - 使用PyQt5实现"""
        # Referenced APIs: check_activation_required, hide, QTimer, singleShot
        pass  # [META only - no bytecode recovered]

    def toggle_coord_display(self):  # [META]
        """切换实时坐标显示"""
        # Referenced APIs: hasattr, coord_overlay, CoordOverlay, show, coord_btn, setText, setStyleSheet, close
        # const: 'coord_overlay'
        # const: '📍 关闭坐标'
        # const: 'background-color: #ef4444; color: white;'
        # const: '📍 显示坐标'
        pass  # [META only - no bytecode recovered]

    def toggle_log_enabled(self):  # [META]
        """切换日志开关"""
        # Referenced APIs: log_enabled, toggle_log_btn, setText, setStyleSheet
        # const: '🔔 开启'
        # const: '🔕 关闭'
        # const: 'background: #dc2626;'
        pass  # [META only - no bytecode recovered]

    def toggle_maximize(self):  # [META]
        # Referenced APIs: isMaximized, showNormal, max_btn, setText, showMaximized
        pass  # [META only - no bytecode recovered]

    def toggle_pause(self):  # [META]
        """切换暂停状态"""
        # Referenced APIs: engine, is_running, toggle_pause, pause_btn, setText, setToolTip
        # const: '继续 (F11)'
        # const: '暂停 (F11)'
        pass  # [META only - no bytecode recovered]

    def toggle_topmost(self):  # [META]
        """切换窗口置顶"""
        # Referenced APIs: topmost_btn, isChecked, setWindowFlags, windowFlags, Qt, WindowStaysOnTopHint, add_log, show
        # const: '窗口已置顶'
        # const: '已取消置顶'
        pass  # [META only - no bytecode recovered]

    def update_activation_display(self):  # [META]
        """✅ 已激活
⏳"""
        # Referenced APIs: activation, is_activated, get_remaining_time, activation_label, setText, get_remaining_seconds, isActive, start, stop, setStyleSheet
        # const: '❌ 未激活'
        pass  # [META only - no bytecode recovered]

class MiniWindow:
    """Reconstructed from PyArmor-protected bytecode."""

    def closeEvent(self, event):  # [DISASM]
        # Referenced APIs: status_timer, stop, accept
        #
        # === Bytecode Disassembly ===
        #     # Raw bytecode (174 bytes):
        #     #   0000: 3e 01 1e c5 1e fe 53 02 22 00 53 03 34 01 36 00  >.....S.".S.4.6.
        #     #   0010: 20 00 95 00 53 01 6e 02 1e 41 1e 15 00 c0 05 79   ...S.n..A.....y
        #     #   0020: 00 00 36 f8 6e 13 35 dc 00 00 00 00 00 00 19 a6  ..6.n.5.........
        #     #   0030: 28 8b 00 00 00 00 00 00 3a 91 00 00 76 be 95 99  (.......:...v...
        #     #   0040: 26 dc 61 4a 00 00 6e 4f 08 37 00 fd 35 d4 00 00  &.aJ..nO.7..5...
        #     #   0050: 00 00 00 00 35 cf 00 00 00 00 00 00 00 26 28 dc  ....5........&(.
        #     #   0060: 00 00 00 00 00 00 6d 94 26 61 19 d9 39 ad 67 d4  ......m.&a..9.g.
        #     #   0070: 35 a7 00 00 00 00 00 00 00 19 33 5d 00 84 4b f2  5.........3]..K.
        #     #   0080: 49 c2 5d db 00 00 53 04 1e 00 22 00 53 03 35 01  I.]...S...".S.5.
        #     #   0090: 00 00 00 00 00 00 20 00 66 00 3d 03 1f 00 66 01  ...... .f.=...f.
        #     #   00a0: 53 04 22 00 53 03 34 01 36 00 20 00 24 00        S.".S.4.6. .$.
        # Full disassembly: docs/FINAL_DISASSEMBLY/closeEvent.dis
        pass  # [DISASM available above]

    def eventFilter(self, obj, event):  # [META]
        """事件过滤器 - 处理拖拽调整大小"""
        # Referenced APIs: resize_handle, type, MouseButtonPress, button, Qt, LeftButton, resizing, globalPos, y, resize_start_y, log_panel_height, resize_start_height, MouseMove, max, min
        pass  # [META only - no bytecode recovered]

    def mouseMoveEvent(self, event):  # [META]
        """鼠标移动事件 - 拖动窗口"""
        # Referenced APIs: drag_position, buttons, Qt, LeftButton, resizing, move, globalPos, accept
        pass  # [META only - no bytecode recovered]

    def mousePressEvent(self, event):  # [META]
        """鼠标按下事件 - 拖动窗口"""
        # Referenced APIs: button, Qt, LeftButton, resizing, globalPos, frameGeometry, topLeft, drag_position, accept
        pass  # [META only - no bytecode recovered]

    def mouseReleaseEvent(self, event):  # [META]
        """鼠标释放事件"""
        # Referenced APIs: drag_position, accept
        pass  # [META only - no bytecode recovered]

    def on_expand(self):  # [META]
        """展开到正常模式"""
        # Referenced APIs: status_timer, stop, main_window, switch_to_normal_mode
        pass  # [META only - no bytecode recovered]

    def on_pause(self):  # [META]
        """暂停/恢复执行"""
        # Referenced APIs: main_window, toggle_pause, sync_status
        pass  # [META only - no bytecode recovered]

    def on_start(self):  # [META]
        """开始执行"""
        # Referenced APIs: main_window, start_execution, sync_status
        pass  # [META only - no bytecode recovered]

    def on_stop(self):  # [META]
        """停止执行"""
        # Referenced APIs: main_window, stop_execution, sync_status
        pass  # [META only - no bytecode recovered]

    def setup_ui(self):  # [META]
        """QFrame#mainContainer {

                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,

                    stop:0 #1a1a2e, stop:1 #2a2a4e);

                border-radius: 12px;

                border: 1px solid #3a3a5a;

            }"""
        # Referenced APIs: QVBoxLayout, setContentsMargins, setSpacing, QFrame, main_container, setStyleSheet, setObjectName, QHBoxLayout, QLabel, setCursor, QCursor, Qt, SizeAllCursor, addWidget, status_indicator
        # const: 'mainContainer'
        # const: '\n\n            color: #888; font-size: 16px; font-weight: bold;\n\n            padding: 0 4px; cursor: move;\n\n        '
        # const: 'color: #ef4444; font-size: 14px;'
        pass  # [META only - no bytecode recovered]

    def sync_log(self):  # [META]
        """同步主窗口日志"""
        # Referenced APIs: hasattr, main_window, log_text, toPlainText, split, len, mini_log_text, setText, join, verticalScrollBar, setValue, maximum
        # const: 'log_text'
        pass  # [META only - no bytecode recovered]

    def sync_status(self):  # [META]
        """同步主窗口状态"""
        # Referenced APIs: main_window, engine, is_running, is_paused, status_indicator, setStyleSheet, start_btn, setEnabled, stop_btn, pause_btn, setText, log_panel, isVisible, sync_log
        # const: 'color: #f59e0b; font-size: 14px;'
        # const: 'color: #22c55e; font-size: 14px;'
        # const: 'color: #ef4444; font-size: 14px;'
        pass  # [META only - no bytecode recovered]

    def toggle_log_panel(self):  # [META]
        """切换日志面板显示"""
        # Referenced APIs: log_panel, isVisible, setVisible, setFixedHeight, log_panel_height, setFixedSize, sync_log
        pass  # [META only - no bytecode recovered]

    def toggle_topmost(self):  # [META]
        """切换置顶"""
        # Referenced APIs: is_topmost, setWindowFlags, windowFlags, Qt, WindowStaysOnTopHint, topmost_btn, setStyleSheet, show
        pass  # [META only - no bytecode recovered]

class ScreenshotWindow:
    """Reconstructed from PyArmor-protected bytecode."""

    def cancel(self):  # [META]
        # Referenced APIs: close, screenshot_cancelled, emit
        pass  # [META only - no bytecode recovered]

    def do_save(self, copy_to_clipboard):  # [META]
        """保存截图



Args:

    copy_to_clipboard: 是否同时复制图片名和坐标到剪贴板"""
        # Referenced APIs: selected_rect, cancel, screenshot, copy, datetime, now, strftime, os, path, join, save_folder, makedirs, save, toImage, x
        # const: '%Y%m%d_%H%M%S'
        # const: 'screenshot_'
        # const: '.png'
        # const: 'PNG'
        # const: '截图保存失败: '
        pass  # [META only - no bytecode recovered]

    def do_save_and_copy(self):  # [META]
        """保存截图并复制图片名和坐标到剪贴板"""
        # Referenced APIs: do_save
        pass  # [META only - no bytecode recovered]

    def keyPressEvent(self, event):  # [META]
        # Referenced APIs: key, Qt, Key_Escape, cancel, Key_Return, Key_Enter, selection_done, do_save
        pass  # [META only - no bytecode recovered]

    def mouseMoveEvent(self, event):  # [META]
        # Referenced APIs: is_selecting, start_pos, rubber_band, setGeometry, QRect, pos, normalized
        pass  # [META only - no bytecode recovered]

    def mousePressEvent(self, event):  # [META]
        # Referenced APIs: selection_done, button, Qt, LeftButton, pos, start_pos, rubber_band, setGeometry, QRect, QSize, show, is_selecting, RightButton, cancel
        pass  # [META only - no bytecode recovered]

    def mouseReleaseEvent(self, event):  # [META]
        # Referenced APIs: button, Qt, LeftButton, is_selecting, pos, end_pos, show_confirm
        pass  # [META only - no bytecode recovered]

    def paintEvent(self, event):  # [META]
        """Microsoft YaHei UI"""
        # Referenced APIs: QPainter, drawPixmap, screenshot, fillRect, rect, QColor, selection_done, selected_rect, setPen, drawRect, setFont, QFont, drawText, x, width
        # const: '🖱️ 按住拖动选择区域 | ESC 取消 | 右键 取消'
        pass  # [META only - no bytecode recovered]

    def show_confirm(self):  # [META]
        """显示确认按钮"""
        # Referenced APIs: start_pos, end_pos, cancel, QRect, normalized, width, height, selected_rect, selection_done, rubber_band, hide, setCursor, Qt, ArrowCursor, size_label
        # const: '选区尺寸: '
        # const: ' x '
        # const: ' 像素'
        pass  # [META only - no bytecode recovered]

def generate_random_title():  # [DISASM]
    """每次启动生成随机窗口标题"""
    # Referenced APIs: random, choice, join, choices, string, digits, randint
    # === Bytecode Disassembly ===
    #   40           NOP
    #                NOP
    #                LOAD_CONST               2 (None)
    #                PUSH_NULL
    #   41           LOAD_CONST               3 (b'\xc0\xe2N\x07\xa3\x01\x00\x00\x01\x00\x00\x1a,\x01\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RESUME                   0
    #                LOAD_CONST               1 (None)
    #                STORE_FAST               0 (__assert_armored__)
    #                NOP
    #                NOP
    #   40           NOP
    #   44   L1:     BUILD_LIST               0
    #                LOAD_CONST               4 (('系统设置', '控制面板', '系统工具', '设置中心', '配置管理', '任务管理', '服务管理', '系统服务', '工具箱', '管理器', '优化工具', '系统助手', '资源监控', '进程管理', '性能监控'))
    #                LIST_EXTEND              1
    #                STORE_FAST               1 (_var_var_0)
    #   56           LOAD_GLOBAL              0 (random)
    #                LOAD_ATTR                2 (choice)
    #                PUSH_NULL
    #                LOAD_FAST                1 (_var_var_0)
    #                CALL                     1
    #                STORE_FAST               2 (_var_var_1)
    #   58           LOAD_GLOBAL              0 (random)
    #                LOAD_ATTR                0 (random)
    #                PUSH_NULL
    #                CALL                     0
    #                LOAD_CONST               5 (0.5)
    #                COMPARE_OP             148 (bool(>))
    #                POP_JUMP_IF_FALSE       87 (to L3)
    #   60           LOAD_CONST               6 ('')
    #                LOAD_ATTR                5 (join + NULL|self)
    #                LOAD_GLOBAL              0 (random)
    #                LOAD_ATTR                6 (choices)
    #                PUSH_NULL
    #                LOAD_GLOBAL              8 (string)
    #                LOAD_ATTR               10 (digits)
    #                LOAD_GLOBAL              0 (random)
    #                LOAD_ATTR               12 (randint)
    #                PUSH_NULL
    #                LOAD_CONST               7 (1)
    #                LOAD_CONST               8 (3)
    #                CALL                     2
    #                LOAD_CONST               9 (('k',))
    #                CALL_KW                  2
    #                CALL                     1
    #                STORE_FAST               3 (_var_var_2)
    #   62           LOAD_FAST                2 (_var_var_1)
    #                FORMAT_SIMPLE
    # Full: docs/FINAL_DISASSEMBLY/generate_random_title.dis
    pass  # [DISASM available above]

def get_app_path():  # [DISASM]
    """获取应用程序所在目录（兼容exe打包）"""
    # Referenced APIs: getattr, sys, os, path, dirname, executable, abspath
    # const: 'frozen'
    # === Bytecode Disassembly ===
    #   23           NOP
    #                NOP
    #                LOAD_CONST               2 (None)
    #                PUSH_NULL
    #   24           LOAD_CONST               3 (b'\x80\xe7\x1f\xf2W\x02\x00\x00\x01\x00\x00\x1a,\x01\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RESUME                   0
    #                LOAD_CONST               1 (None)
    #                STORE_FAST               0 (__assert_armored__)
    #                NOP
    #                NOP
    #   23           NOP
    #   25   L1:     LOAD_GLOBAL              1 (getattr + NULL)
    #                LOAD_GLOBAL              2 (sys)
    #                LOAD_CONST               4 ('frozen')
    #                LOAD_CONST               5 (False)
    #                CALL                     3
    #                TO_BOOL
    #                POP_JUMP_IF_FALSE       54 (to L3)
    #   27           LOAD_GLOBAL              4 (os)
    #                LOAD_ATTR                6 (path)
    #                LOAD_ATTR                9 (dirname + NULL|self)
    #                LOAD_GLOBAL              2 (sys)
    #                LOAD_ATTR               10 (executable)
    #                CALL                     1
    #   25   L2:     NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD            93 (to L7)
    #                CALL                     1
    #                POP_TOP
    #                RETURN_VALUE
    #   30   L3:     LOAD_GLOBAL              4 (os)
    #                LOAD_ATTR                6 (path)
    #                LOAD_ATTR                9 (dirname + NULL|self)
    #                LOAD_GLOBAL              4 (os)
    #                LOAD_ATTR                6 (path)
    #                LOAD_ATTR               13 (abspath + NULL|self)
    #                LOAD_GLOBAL             14 (__file__)
    #                CALL                     1
    #                CALL                     1
    #   25   L4:     NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD            20 (to L7)
    #                CALL                     1
    #                POP_TOP
    #                RETURN_VALUE
    # Full: docs/FINAL_DISASSEMBLY/get_app_path.dis
    pass  # [DISASM available above]

def get_crash_log_path():  # [DISASM]
    """获取崩溃日志路径"""
    # Referenced APIs: getattr, sys, os, path, join, dirname, executable, abspath
    # const: 'frozen'
    # const: 'crash_log.txt'
    # === Bytecode Disassembly ===
    # 7180           NOP
    #                NOP
    #                LOAD_CONST               2 (None)
    #                PUSH_NULL
    # 7181           LOAD_CONST               3 (b'\xb0!:\x07\xa3\x01\x00\x00\x01\x00\x00\x1a\xa4\x01\x00\x00\x01\x00\x00\x00')
    #                BUILD_TUPLE              1
    #                CALL_FUNCTION_EX         0
    #                POP_TOP
    #                RESUME                   0
    #                LOAD_CONST               1 (None)
    #                STORE_FAST               0 (__assert_armored__)
    #                NOP
    #                NOP
    # 7180           NOP
    # 7182   L1:     LOAD_GLOBAL              1 (getattr + NULL)
    #                LOAD_GLOBAL              2 (sys)
    #                LOAD_CONST               4 ('frozen')
    #                LOAD_CONST               5 (False)
    #                CALL                     3
    #                TO_BOOL
    #                POP_JUMP_IF_FALSE       84 (to L3)
    # 7183           LOAD_GLOBAL              4 (os)
    #                LOAD_ATTR                6 (path)
    #                LOAD_ATTR                9 (join + NULL|self)
    #                LOAD_GLOBAL              4 (os)
    #                LOAD_ATTR                6 (path)
    #                LOAD_ATTR               11 (dirname + NULL|self)
    #                LOAD_GLOBAL              2 (sys)
    #                LOAD_ATTR               12 (executable)
    #                CALL                     1
    #                LOAD_CONST               6 ('crash_log.txt')
    #                CALL                     2
    # 7184   L2:     NOP
    #                NOP
    #                NOP
    #                JUMP_FORWARD           123 (to L7)
    #                CALL                     1
    #                POP_TOP
    #                RETURN_VALUE
    #        L3:     LOAD_GLOBAL              4 (os)
    #                LOAD_ATTR                6 (path)
    #                LOAD_ATTR                9 (join + NULL|self)
    #                LOAD_GLOBAL              4 (os)
    #                LOAD_ATTR                6 (path)
    #                LOAD_ATTR               11 (dirname + NULL|self)
    #                LOAD_GLOBAL              4 (os)
    #                LOAD_ATTR                6 (path)
    #                LOAD_ATTR               15 (abspath + NULL|self)
    #                LOAD_GLOBAL             16 (__file__)
    #                CALL                     1
    # Full: docs/FINAL_DISASSEMBLY/get_crash_log_path.dis
    pass  # [DISASM available above]

def main():  # [DISASM]
    """frozen"""
    # Referenced APIs: security, init_security, ImportError, getattr, sys, RuntimeError, QApplication, setAttribute, Qt, AA_EnableHighDpiScaling, AA_UseHighDpiPixmaps, argv, setStyle, MainWindow, show
    # const: '安全模块加载失败'
    # const: 'Fusion'
    # const: '启动错误'
    # const: '程序启动失败，请联系技术支持。\n\n错误信息已保存到 crash_log.txt\n\n简要错误: '
    # === Bytecode Disassembly ===
    #     # Raw bytecode (174 bytes):
    #     #   0000: 3e 01 1e c5 1e fe 53 02 22 00 53 03 34 01 36 00  >.....S.".S.4.6.
    #     #   0010: 20 00 95 00 53 01 6e 02 1e 41 1e 15 00 c0 05 79   ...S.n..A.....y
    #     #   0020: 00 00 36 f8 6e 13 35 dc 00 00 00 00 00 00 19 a6  ..6.n.5.........
    #     #   0030: 28 8b 00 00 00 00 00 00 3a 91 00 00 76 be 95 99  (.......:...v...
    #     #   0040: 26 dc 61 4a 00 00 6e 4f 08 37 00 fd 35 d4 00 00  &.aJ..nO.7..5...
    #     #   0050: 00 00 00 00 35 cf 00 00 00 00 00 00 00 26 28 dc  ....5........&(.
    #     #   0060: 00 00 00 00 00 00 6d 94 26 61 19 d9 39 ad 67 d4  ......m.&a..9.g.
    #     #   0070: 35 a7 00 00 00 00 00 00 00 19 33 5d 00 84 4b f2  5.........3]..K.
    #     #   0080: 49 c2 5d db 00 00 53 04 1e 00 22 00 53 03 35 01  I.]...S...".S.5.
    #     #   0090: 00 00 00 00 00 00 20 00 66 00 3d 03 1f 00 66 01  ...... .f.=...f.
    #     #   00a0: 53 04 22 00 53 03 34 01 36 00 20 00 24 00        S.".S.4.6. .$.
    # Full: docs/FINAL_DISASSEMBLY/main.dis
    pass  # [DISASM available above]

def show_error_msgbox(title, message):  # [META]
    """显示错误消息框（不依赖PyQt）"""
    # Referenced APIs: ctypes, windll, user32, MessageBoxW
    pass  # [META only]

def show_message(parent, title, text, msg_type):  # [META]
    """显示自定义样式的消息框"""
    # Referenced APIs: QMessageBox, setWindowTitle, setText, setStyleSheet, MSG_BOX_STYLE, setIcon, Information, Warning, Critical, Question, setStandardButtons, Yes, No, setDefaultButton, exec_
    # const: 'info'
    # const: 'warning'
    # const: 'error'
    # const: 'question'
    pass  # [META only]

def write_crash_log(error_msg):  # [META]
    """写入崩溃日志"""
    # Referenced APIs: get_crash_log_path, open, write, datetime, now, strftime
    # const: 'utf-8'
    # const: '=================================================='
    # const: '时间: '
    # const: '%Y-%m-%d %H:%M:%S'
    # const: '错误: '
    pass  # [META only]
