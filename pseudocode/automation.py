"""
6号自动化助手 - automation.py

状态说明:
  - 函数签名/参数名/字符串常量/引用的API: 100%% 准确
  - 标记 [DISASM] 的函数: 有完整字节码反汇编
  - 标记 [META] 的函数: 仅元数据，无字节码
  - editor/ 目录: 100%% 原始源码
"""

class AutomationEngine:
    """Reconstructed from PyArmor-protected bytecode."""

    def _cleanup_old_screenshots(self, folder, prefix, max_count):  # [META]
        """清理旧截图，保留最新的max_count张"""
        # Referenced APIs: os, listdir, startswith, endswith, path, join, append, getctime, sort, len, pop, remove, log, basename, Exception
        # const: '.png'
        # const: '.jpg'
        # const: '🗑️ 已删除旧截图: '
        # const: '⚠️ 清理旧截图失败: '
        pass  # [META only - no bytecode recovered]

    def _execute_action(self, action, ref_x, ref_y):  # [META]
        """执行单个动作（用于变换识别的动作序列）"""
        # Referenced APIs: get, pyautogui, click, log, keyboard, press_and_release, time, sleep, Exception
        # const: 'type'
        # const: 'delay_after'
        # const: 'click'
        # const: 'offset_x'
        # const: 'offset_y'
        pass  # [META only - no bytecode recovered]

    def _find_image_in_region(self, image_name, region, confidence, color_match):  # [META]
        """在指定区域内识别图片（支持多尺度匹配，适应不同DPI/缩放）



Args:

    image_name: 图片文件名

    region: 区域坐标 {x, y, width, height}

    confidence: 置信度

    color_match: 是否使用彩色匹配（区分颜色）"""
        # Referenced APIs: os, path, join, images_folder, exists, PIL, ImageGrab, grab, np, array, load_image_cv2, cv2, IMREAD_COLOR, IMREAD_GRAYSCALE, cvtColor
        # const: 'width'
        # const: 'height'
        # const: 'color'
        # const: 'gray'
        pass  # [META only - no bytecode recovered]

    def _find_image_safe(self, image_name, confidence):  # [META]
        """线程安全的图片识别（用于常驻任务）"""
        # Referenced APIs: os, path, join, images_folder, exists, PIL, ImageGrab, grab, np, array, cv2, cvtColor, COLOR_RGB2GRAY, load_image_cv2, IMREAD_GRAYSCALE
        pass  # [META only - no bytecode recovered]

    def _handle_image_result(self, step, success, action_name):  # [META]
        """处理图片识别类步骤的成功/失败结果



Args:

    step: 步骤配置

    success: 是否成功

    action_name: 操作名称（用于日志）

    

Returns:

    bool: 是否成功（可能被修改）"""
        # Referenced APIs: get, log, is_running, jump_to_group
        # const: 'on_success'
        # const: 'continue'
        # const: 'stop'
        # const: '成功，停止当前组合'
        # const: 'jump'
        pass  # [META only - no bytecode recovered]

    def _humanize_delay(self):  # [META]
        """添加人类化随机延迟"""
        # Referenced APIs: humanize_enabled, random, uniform, humanize_delay_range, time, sleep
        pass  # [META only - no bytecode recovered]

    def _humanize_position(self, x, y):  # [META]
        """添加人类化位置偏移"""
        # Referenced APIs: humanize_enabled, humanize_position_range, random, randint
        pass  # [META only - no bytecode recovered]

    def _load_fps_dpi_config(self):  # [META]
        """加载FPS DPI配置"""
        # Referenced APIs: os, path, exists, fps_config_file, open, json, load, get, fps_standard_dpi
        # const: 'utf-8'
        # const: 'user_dpi'
        pass  # [META only - no bytecode recovered]

    def _load_push_pack(self):  # [META]
        """从加密包读取推送图片配置"""
        # Referenced APIs: hmac, hashlib, os, path, join, get_app_path, exists, hasattr, open, read, startswith, len, new, sha256, digest
        # const: 'push_images.dat'
        # const: '_push_pack_cache'
        # const: 'rb'
        # const: '⚠️ 推送图片包签名无效，请使用官方包'
        # const: '⚠️ 推送图片包格式无效'
        pass  # [META only - no bytecode recovered]

    def _smooth_move_to(self, target_x, target_y, duration):  # [META]
        """丝滑贝塞尔曲线鼠标移动



使用二次贝塞尔曲线实现自然的鼠标移动轨迹"""
        # Referenced APIs: random, math, pyautogui, position, sqrt, moveTo, max, min, int, atan2, pi, uniform, cos, sin, range
        pass  # [META only - no bytecode recovered]

    def activate_window(self, process_name):  # [META]
        """激活/切换到指定窗口"""
        # Referenced APIs: win32gui, win32con, get_window_by_process, log, IsIconic, ShowWindow, SW_RESTORE, SetForegroundWindow, Exception
        # const: '未找到程序窗口: '
        # const: '切换到窗口: '
        # const: '切换窗口失败: '
        pass  # [META only - no bytecode recovered]

    def activate_window_v2(self, find_by, target):  # [META]
        """激活/切换到指定窗口（支持多种查找方式）"""
        # Referenced APIs: win32gui, win32con, find_window, log, get, IsIconic, ShowWindow, SW_RESTORE, SetForegroundWindow, Exception
        # const: '进程名'
        # const: '窗口标题'
        # const: 'PID'
        # const: '未找到窗口 ['
        # const: '切换到窗口: ['
        pass  # [META only - no bytecode recovered]

    def close_process(self, process_name):  # [META]
        """强制关闭程序"""
        # Referenced APIs: close_process_v2
        # const: 'process_name'
        pass  # [META only - no bytecode recovered]

    def close_process_v2(self, find_by, target):  # [META]
        """强制关闭程序（支持多种查找方式）"""
        # Referenced APIs: find_process, kill, log, get, Exception
        # const: '进程名'
        # const: '窗口标题'
        # const: 'PID'
        # const: '已关闭 '
        # const: ' 个进程 ['
        pass  # [META only - no bytecode recovered]

    def execute_change_detection(self, step):  # [META]
        """执行变换识别（非常驻模式，在超时时间内检测多区域）



按优先级检测多个区域，检测到就执行对应动作序列"""
        # Referenced APIs: get, log, join, len, time, is_running, jump_to_group, is_paused, sleep, append, Exception, sort
        # const: 'regions'
        # const: '⚠️ 变换识别：未配置监控区域'
        # const: 'timeout'
        # const: 'scan_interval'
        # const: 'batch_delay'
        pass  # [META only - no bytecode recovered]

    def execute_color_check(self, step):  # [META]
        """执行颜色识别



检测指定位置的颜色是否与目标颜色匹配（支持容差）

支持循环检测模式：在超时时间内按间隔循环检测



Args:

    step: 包含以下参数

        - x, y: 检测坐标

        - target_color: 目标颜色 [R, G, B]

        - tolerance: 颜色容差（默认30）

        - sample_size: 采样区域大小（默认3，取3x3像素平均值）

        - timeout: 超时时间（秒），0表示只检测一次（默认0）

        - interval: 检测间隔（秒），默认0.5

        - on_match: 匹配时动作 (continue/stop/jump)

        - on_mismatch: 不匹配时动作 (continue/stop/jump)

        - on_timeout: 超时时动作 (continue/stop/jump)"""
        # Referenced APIs: get, isinstance, str, startswith, int, PIL, ImageGrab, time, np, array, float32, log, is_running, jump_to_group, grab
        # const: 'target_color'
        # const: 'tolerance'
        # const: 'sample_size'
        # const: 'timeout'
        # const: 'interval'
        pass  # [META only - no bytecode recovered]

    def execute_group(self, group, group_index):  # [META]
        """执行单个组合



Args:

    group: 组合配置

    group_index: 组合索引

    

Returns:

    bool: 是否正常完成（非跳转）"""
        # Referenced APIs: stop_continuous_tasks, get, humanize_enabled, humanize_position_range, humanize_delay_range, log, int, current_group, jump_to_group, start_continuous_task, append, time, is_running, sleep, stop_group_continuous_tasks
        # const: 'name'
        # const: '组合 '
        # const: 'steps'
        # const: 'humanize'
        # const: 'enabled'
        pass  # [META only - no bytecode recovered]

    def execute_groups(self, workflow, start_group):  # [META]
        """执行多组合工作流



Args:

    workflow: 包含groups数组的工作流配置

    start_group: 起始组合索引（默认使用配置中的default_group）



执行逻辑：

    - 从默认组合开始执行

    - 组合执行完后，如果有跳转配置则跳转，否则停止

    - 不会自动执行下一个组合"""
        # Referenced APIs: is_running, is_paused, jump_to_group, call_stack, return_from_call, get, log, len, execute_group, pop, return_step_index
        # const: 'groups'
        # const: 'steps'
        # const: 'name'
        # const: '默认组合'
        # const: '没有可执行的组合'
        pass  # [META only - no bytecode recovered]

    def execute_pixel_position(self, step):  # [META]
        """像素级定位 - 通过图片识别和WASD按键调整位置

Args:
    step: 包含以下参数
        - image: 参考图片名
        - target_x, target_y: 目标坐标
        - tolerance: 误差范围（像素）
        - ms_per_pixel: 每像素对应的按键时长（毫秒）
        - confidence: 图片识别置信度
        - max_attempts: 最大调整次数
        - key_up, key_down, key_left, key_right: WASD按键"""
        # Referenced APIs: keyboard, get, log, is_running, find_image, time, sleep, abs, press, release
        # const: 'image'
        # const: 'target_x'
        # const: 'target_y'
        # const: 'tolerance'
        # const: 'ms_per_pixel'
        pass  # [META only - no bytecode recovered]

    def execute_step(self, step):  # [META]
        """执行单个步骤"""
        # Referenced APIs: wait_if_paused, get, is_running, is_paused, min, time, sleep, mouse_click_current, mouse_double_click_current, mouse_right_click_current, mouse_move, mouse_drag, mouse_scroll, fps_move, keyboard_type
        # const: 'type'
        # const: 'delay'
        # const: 'click'
        # const: 'button'
        # const: 'left'
        pass  # [META only - no bytecode recovered]

    def execute_workflow(self, workflow, loop_count):  # [META]
        """执行工作流"""
        # Referenced APIs: is_running, is_paused, get, log, range, enumerate, time, sleep, current_step, execute_step
        # const: 'name'
        # const: '未命名流程'
        # const: 'steps'
        # const: '开始执行流程: '
        # const: '第 '
        pass  # [META only - no bytecode recovered]

    def find_all_images(self, image_name, confidence, region):  # [META]
        """查找所有匹配的图片位置"""
        # Referenced APIs: get_image_path, os, path, exists, log, pyautogui, screenshot, np, array, cv2, cvtColor, COLOR_RGB2GRAY, load_image_cv2, IMREAD_GRAYSCALE, matchTemplate
        # const: '图片不存在: '
        # const: '找到 '
        # const: ' 个匹配: '
        # const: '图像识别失败: '
        pass  # [META only - no bytecode recovered]

    def find_image(self, image_name, confidence, region):  # [META]
        """查找图片位置"""
        # Referenced APIs: get_image_path, os, path, exists, log, pyautogui, screenshot, np, array, cv2, cvtColor, COLOR_RGB2GRAY, load_image_cv2, IMREAD_GRAYSCALE, matchTemplate
        # const: '图片不存在: '
        # const: '无法加载图片: '
        # const: '找到图片 '
        # const: ': ('
        # const: ', '
        pass  # [META only - no bytecode recovered]

    def find_process(self, find_by, target):  # [META]
        """通用进程查找函数（用于关闭进程等）



Args:

    find_by: 查找方式 - 'process_name'(进程名), 'window_title'(窗口标题), 'pid'(进程ID)

    target: 查找目标

    

Returns:

    list: 匹配的进程列表"""
        # Referenced APIs: psutil, win32gui, win32process, Process, int, append, process_iter, info, lower, set, EnumWindows, Exception, log
        # const: 'pid'
        # const: 'process_name'
        # const: 'name'
        # const: 'window_title'
        # const: '查找进程失败: '
        pass  # [META only - no bytecode recovered]

    def find_window(self, find_by, target):  # [META]
        """通用窗口查找函数



Args:

    find_by: 查找方式 - 'process_name'(进程名), 'window_title'(窗口标题), 'pid'(进程ID)

    target: 查找目标

    

Returns:

    hwnd: 窗口句柄，未找到返回 None"""
        # Referenced APIs: win32gui, win32process, psutil, EnumWindows, Exception, log
        # const: '查找窗口失败: '
        pass  # [META only - no bytecode recovered]

    def fps_move(self, dx, dy, duration, steps):  # [META]
        """FPS视角移动 - 相对鼠标移动



用于FPS游戏视角控制，通过相对移动实现视角转动

配置值基于标准DPI(1000)编写，自动根据用户DPI换算



Args:

    dx: 水平移动距离（像素），正值向右转，负值向左转

    dy: 垂直移动距离（像素），正值向下看，负值向上看

    duration: 移动持续时间（秒）

    steps: 移动分段数（越多越平滑）"""
        # Referenced APIs: ctypes, time, get_fps_dpi_multiplier, windll, user32, mouse_event, int, range, sleep, log, abs, Exception
        # const: 'FPS视角移动: 水平'
        # const: 'px 垂直'
        # const: 'px (DPI倍率:'
        # const: '.2f'
        # const: 'FPS视角移动失败: '
        pass  # [META only - no bytecode recovered]

    def get_fps_dpi_multiplier(self):  # [META]
        """获取FPS DPI倍率（标准DPI / 用户DPI）"""
        # Referenced APIs: fps_standard_dpi, fps_user_dpi
        pass  # [META only - no bytecode recovered]

    def get_image_path(self, image_name):  # [META]
        """获取图片完整路径"""
        # Referenced APIs: os, path, isabs, join, images_folder
        pass  # [META only - no bytecode recovered]

    def get_window_by_process(self, process_name):  # [META]
        """根据进程名获取窗口句柄（兼容旧代码）"""
        # Referenced APIs: find_window
        # const: 'process_name'
        pass  # [META only - no bytecode recovered]

    def image_click(self, image_name, confidence, offset_x, offset_y, wait_time, max_wait, button, click_delay):  # [META]
        """图像识别并点击



Args:

    click_delay: 鼠标移动到目标后等待多少秒再点击（默认1秒）"""
        # Referenced APIs: time, is_running, jump_to_group, find_image, mouse_move, log, sleep, mouse_click_current
        # const: '移动到目标位置 ('
        # const: ', '
        # const: ')，等待 '
        # const: ' 秒后点击'
        # const: '等待图片超时: '
        pass  # [META only - no bytecode recovered]

    def image_click_ocr(self, image_name, ocr_text, confidence, offset_x, offset_y, max_wait, button, click_delay, ocr_expand):  # [META]
        """图像识别 + OCR 验证后点击



Args:

    image_name: 图片文件名

    ocr_text: 需要验证的文字（支持部分匹配）

    confidence: 图片匹配置信度

    offset_x, offset_y: 点击偏移

    max_wait: 最大等待时间

    button: 鼠标按键

    click_delay: 点击前延迟

    ocr_expand: OCR 识别区域扩展像素（向四周扩展）"""
        # Referenced APIs: time, os, path, join, images_folder, exists, log, load_image_cv2, cv2, IMREAD_COLOR, shape, is_running, jump_to_group, find_image, max
        # const: '[OCR] 图片不存在: '
        # const: '[OCR] 无法读取图片: '
        # const: '[OCR] 识别区域: ('
        # const: ', '
        # const: "[OCR] 文字验证成功: '"
        pass  # [META only - no bytecode recovered]

    def image_find_and_move(self, image_name, confidence, offset_x, offset_y, max_wait, move_duration):  # [META]
        """图像识别并移动鼠标（不点击）"""
        # Referenced APIs: time, is_running, jump_to_group, find_image, log, mouse_move, sleep
        # const: '图片识别成功，移动鼠标到: ('
        # const: ', '
        # const: '图片识别超时: '
        pass  # [META only - no bytecode recovered]

    def keyboard_hold(self, key, duration):  # [META]
        """按住键:"""
        # Referenced APIs: time, perf_counter, pyautogui, keyDown, precise_sleep, keyUp, log, Exception
        # const: '按住键: '
        # const: ' (指定'
        # const: '秒-实际'
        # const: '.3f'
        # const: '秒)'
        pass  # [META only - no bytecode recovered]

    def keyboard_hotkey(self, hold_time, keys):  # [META]
        """组合键:"""
        # Referenced APIs: time, perf_counter, pyautogui, keyDown, precise_sleep, reversed, keyUp, log, join, hotkey, Exception
        # const: '组合键: '
        # const: ' (指定'
        # const: '秒-实际'
        # const: '.3f'
        # const: '秒)'
        pass  # [META only - no bytecode recovered]

    def keyboard_press(self, key, hold_time):  # [META]
        """按下单个键"""
        # Referenced APIs: time, perf_counter, pyautogui, keyDown, precise_sleep, keyUp, log, press, Exception
        # const: '按键: '
        # const: ' (指定'
        # const: '秒-实际'
        # const: '.3f'
        # const: '秒)'
        pass  # [META only - no bytecode recovered]

    def keyboard_type(self, text, interval):  # [META]
        """键盘输入文本 - 使用剪贴板粘贴方式"""
        # Referenced APIs: pyperclip, paste, copy, time, sleep, keyboard, press, release, len, log, Exception
        # const: 'ctrl'
        # const: '...'
        # const: '粘贴文本: '
        # const: '粘贴文本失败: '
        pass  # [META only - no bytecode recovered]

    def load_image_cv2(self, image_path, flags):  # [META]
        """加载图片（支持中文路径）"""
        # Referenced APIs: np, fromfile, uint8, cv2, imdecode, Exception, log
        # const: '加载图片失败: '
        # const: ', 错误: '
        pass  # [META only - no bytecode recovered]

    def load_workflow(self, filepath):  # [META]
        """加载工作流配置"""
        # Referenced APIs: open, json, load, Exception, log
        # const: 'utf-8'
        # const: '加载工作流失败: '
        pass  # [META only - no bytecode recovered]

    def log(self, message):  # [DISASM]
        """记录日志"""
        # Referenced APIs: datetime, now, strftime, print, log_callback
        # const: '%H:%M:%S'
        # const: '] '
        #
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
        # ... (truncated, full disassembly in docs/)
        # Full disassembly: docs/FINAL_DISASSEMBLY/log.dis
        pass  # [DISASM available above]

    def mouse_click(self, x, y, button, clicks):  # [META]
        """鼠标点击（先丝滑移动再点击）"""
        # Referenced APIs: pyautogui, click, log, Exception
        # const: '鼠标点击: ('
        # const: ', '
        # const: ') '
        # const: '键 '
        # const: '鼠标点击失败: '
        pass  # [META only - no bytecode recovered]

    def mouse_click_current(self, button, clicks, hold_time):  # [META]
        """在当前鼠标位置点击"""
        # Referenced APIs: time, perf_counter, pyautogui, mouseDown, precise_sleep, mouseUp, log, click, Exception
        # const: '鼠标按住: 当前位置 '
        # const: '键 (指定'
        # const: '秒-实际'
        # const: '.3f'
        # const: '秒)'
        pass  # [META only - no bytecode recovered]

    def mouse_double_click(self, x, y):  # [META]
        """鼠标双击"""
        # Referenced APIs: mouse_click
        pass  # [META only - no bytecode recovered]

    def mouse_double_click_current(self):  # [META]
        """在当前鼠标位置双击"""
        # Referenced APIs: mouse_click_current
        pass  # [META only - no bytecode recovered]

    def mouse_drag(self, start_x, start_y, end_x, end_y, duration):  # [META]
        """鼠标拖拽"""
        # Referenced APIs: pyautogui, moveTo, time, sleep, drag, log, Exception
        # const: '鼠标拖拽: ('
        # const: ', '
        # const: ') -> ('
        # const: ') '
        # const: '鼠标拖拽失败: '
        pass  # [META only - no bytecode recovered]

    def mouse_move(self, x, y, duration):  # [META]
        """移动鼠标（丝滑贝塞尔曲线移动）"""
        # Referenced APIs: humanize_enabled, random, uniform, log, Exception
        # const: '鼠标移动到: ('
        # const: ', '
        # const: '鼠标移动失败: '
        pass  # [META only - no bytecode recovered]

    def mouse_right_click(self, x, y):  # [META]
        """鼠标右键点击"""
        # Referenced APIs: mouse_click
        # const: 'right'
        pass  # [META only - no bytecode recovered]

    def mouse_right_click_current(self):  # [META]
        """在当前鼠标位置右键点击"""
        # Referenced APIs: mouse_click_current
        # const: 'right'
        pass  # [META only - no bytecode recovered]

    def mouse_scroll(self, clicks, x, y):  # [META]
        """鼠标滚轮"""
        # Referenced APIs: pyautogui, scroll, log, abs, Exception
        # const: '鼠标滚轮: 向'
        # const: '滚动 '
        # const: ' 格'
        # const: '鼠标滚轮失败: '
        pass  # [META only - no bytecode recovered]

    def move_window(self, process_name, x, y, preset_pos):  # [META]
        """移动窗口位置"""
        # Referenced APIs: win32gui, win32api, win32con, get_window_by_process, log, GetWindowRect, GetSystemMetrics, SM_CXSCREEN, SM_CYSCREEN, MoveWindow, Exception
        # const: '未找到程序窗口: '
        # const: '自定义'
        # const: '移动窗口: '
        # const: ' -> ('
        # const: ', '
        pass  # [META only - no bytecode recovered]

    def move_window_v2(self, find_by, target, x, y, preset_pos):  # [META]
        """移动窗口位置（支持多种查找方式）"""
        # Referenced APIs: win32gui, win32con, win32api, find_window, log, get, GetWindowRect, GetSystemMetrics, SM_CXSCREEN, SM_CYSCREEN, MoveWindow, Exception
        # const: '进程名'
        # const: '窗口标题'
        # const: 'PID'
        # const: '未找到窗口 ['
        # const: '自定义'
        pass  # [META only - no bytecode recovered]

    def multi_hold(self, keys):  # [META]
        """同时按住多个按键（键盘或鼠标）"""
        # Referenced APIs: len, log, get, max, pyautogui, keyDown, append, mouseDown, time, perf_counter, set, keyUp, add, mouseUp, sleep
        # const: '没有配置按键'
        # const: 'type'
        # const: 'keyboard'
        # const: 'key'
        # const: 'hold_time'
        pass  # [META only - no bytecode recovered]

    def ocr_read_region(self, x, y, width, height):  # [META]
        """OCR 识别指定区域的文字"""
        # Referenced APIs: get_ocr_reader, log, pyautogui, screenshot, np, array, readtext, join, Exception
        # const: '[OCR] OCR 未初始化'
        # const: '[OCR] 识别结果: '
        # const: '[OCR] 识别失败: '
        pass  # [META only - no bytecode recovered]

    def pause(self):  # [META]
        """暂停执行"""
        # Referenced APIs: is_paused, log
        # const: '执行已暂停'
        pass  # [META only - no bytecode recovered]

    def push_message(self, content, title):  # [META]
        """推送消息到微信

Args:
    content: 消息内容（物料名称，支持多个用顿号分隔）
    title: 消息标题（可选）
    
Returns:
    bool: 是否推送成功"""
        # Referenced APIs: requests, os, path, join, get_app_path, exists, log, open, json, load, get, post, Exception
        # const: 'http://6hzs.nzwl.top'
        # const: 'screenshot_settings.json'
        # const: '❌ 未配置API密钥'
        # const: 'utf-8'
        # const: 'push_api_key'
        pass  # [META only - no bytecode recovered]

    def resize_window(self, process_name, width, height, preset_size):  # [META]
        """调整窗口大小（客户区域大小）"""
        # Referenced APIs: win32gui, win32con, ctypes, get_window_by_process, log, GetWindowRect, GetWindowLong, GWL_STYLE, GWL_EXSTYLE, Structure, windll, user32, AdjustWindowRectEx, byref, right
        # const: '自定义'
        # const: '未找到程序窗口: '
        # const: 'RECT'
        # const: '调整窗口大小: '
        # const: ' -> '
        pass  # [META only - no bytecode recovered]

    def resize_window_v2(self, find_by, target, width, height, preset_size):  # [META]
        """调整窗口大小（支持多种查找方式）"""
        # Referenced APIs: win32gui, win32con, ctypes, find_window, log, get, GetWindowRect, GetWindowLong, GWL_STYLE, GWL_EXSTYLE, wintypes, RECT, windll, user32, AdjustWindowRectEx
        # const: '进程名'
        # const: '窗口标题'
        # const: 'PID'
        # const: '自定义'
        # const: '未找到窗口 ['
        pass  # [META only - no bytecode recovered]

    def resume(self):  # [META]
        """继续执行"""
        # Referenced APIs: is_paused, log
        # const: '执行继续'
        pass  # [META only - no bytecode recovered]

    def save_fps_dpi_config(self, user_dpi):  # [META]
        """保存FPS DPI配置"""
        # Referenced APIs: open, fps_config_file, json, dump, fps_standard_dpi, fps_user_dpi, log, Exception
        # const: 'utf-8'
        # const: 'FPS DPI已保存: '
        # const: '保存FPS DPI失败: '
        pass  # [META only - no bytecode recovered]

    def save_workflow(self, workflow, filepath):  # [META]
        """保存工作流配置"""
        # Referenced APIs: open, json, dump, log, Exception
        # const: 'utf-8'
        # const: '工作流已保存: '
        # const: '保存工作流失败: '
        pass  # [META only - no bytecode recovered]

    def set_log_callback(self, callback):  # [META]
        """设置日志回调函数"""
        # Referenced APIs: log_callback
        pass  # [META only - no bytecode recovered]

    def set_status_callback(self, callback):  # [META]
        """设置状态回调函数"""
        # Referenced APIs: status_callback
        pass  # [META only - no bytecode recovered]

    def set_windowed_mode(self, process_name, width, height, preset_size):  # [META]
        """将全屏/全屏窗口调整为窗口模式"""
        # Referenced APIs: win32gui, win32con, win32api, ctypes, get_window_by_process, log, GetSystemMetrics, SM_CXSCREEN, SM_CYSCREEN, GetWindowLong, GWL_STYLE, WS_POPUP, WS_OVERLAPPEDWINDOW, SetWindowLong, GWL_EXSTYLE
        # const: '自定义'
        # const: '未找到程序窗口: '
        # const: 'RECT'
        # const: '已调整为窗口模式: '
        # const: ' -> '
        pass  # [META only - no bytecode recovered]

    def set_windowed_mode_v2(self, find_by, target, width, height, preset_size):  # [META]
        """调整为窗口模式（支持多种查找方式）"""
        # Referenced APIs: win32gui, win32con, win32api, ctypes, find_window, log, get, GetWindowLong, GWL_STYLE, WS_OVERLAPPEDWINDOW, WS_POPUP, SetWindowLong, GWL_EXSTYLE, wintypes, RECT
        # const: '进程名'
        # const: '窗口标题'
        # const: 'PID'
        # const: '自定义'
        # const: '未找到窗口 ['
        pass  # [META only - no bytecode recovered]

    def start_continuous_task(self, step, group_id):  # [META]
        """启动常驻点击/按键任务（仅在当前组合执行时运行）"""
        # Referenced APIs: get, max, continuous_lock, continuous_tasks, append, threading, Thread, start, log
        # const: 'image'
        # const: 'confidence'
        # const: 'offset_x'
        # const: 'offset_y'
        # const: 'interval'
        pass  # [META only - no bytecode recovered]

    def stop(self):  # [DISASM]
        """停止执行"""
        # Referenced APIs: is_running, is_paused, stop_continuous_tasks, log
        # const: '执行已停止'
        #
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
        # Full disassembly: docs/FINAL_DISASSEMBLY/stop.dis
        pass  # [DISASM available above]

    def stop_continuous_tasks(self):  # [META]
        """停止所有常驻任务"""
        # Referenced APIs: continuous_lock, continuous_tasks, clear
        # const: 'should_stop'
        pass  # [META only - no bytecode recovered]

    def stop_group_continuous_tasks(self, group_id):  # [META]
        """停止指定组合的常驻任务"""
        # Referenced APIs: continuous_lock, continuous_tasks, get
        # const: 'group_id'
        # const: 'should_stop'
        pass  # [META only - no bytecode recovered]

    def take_screenshot(self):  # [META]
        """截图保存功能 - 从全局设置文件读取配置
    
Returns:
    bool: 是否成功"""
        # Referenced APIs: os, path, join, get_app_path, exists, open, json, load, get, rstrip, log, Exception, pyautogui, size, max
        # const: 'screenshot_settings.json'
        # const: 'center'
        # const: '1080p'
        # const: 'screenshot'
        # const: 'utf-8'
        pass  # [META only - no bytecode recovered]

    def toggle_pause(self):  # [META]
        """切换暂停状态"""
        # Referenced APIs: is_paused, resume, pause
        pass  # [META only - no bytecode recovered]

    def update_status(self, group_index, step_index, message):  # [META]
        """更新执行状态"""
        # Referenced APIs: status_callback
        pass  # [META only - no bytecode recovered]

    def wait_for_image(self, image_name, confidence, timeout):  # [META]
        """等待图片出现"""
        # Referenced APIs: time, is_running, jump_to_group, find_image, sleep, log
        # const: '等待图片超时: '
        pass  # [META only - no bytecode recovered]

    def wait_for_image_disappear(self, image_name, confidence, timeout):  # [META]
        """等待图片消失"""
        # Referenced APIs: time, is_running, jump_to_group, find_image, log, sleep
        # const: '图片已消失: '
        # const: '等待图片消失超时: '
        pass  # [META only - no bytecode recovered]

    def wait_if_paused(self):  # [META]
        """如果暂停则等待，返回False表示已停止"""
        # Referenced APIs: is_paused, is_running, time, sleep
        pass  # [META only - no bytecode recovered]

    def window_exists(self, window_title):  # [META]
        """检测窗口是否存在（通过标题或进程名匹配）"""
        # Referenced APIs: win32gui, win32process, psutil, lower, endswith, EnumWindows, log, len, join, Exception
        # const: '.exe'
        # const: '✓ 检测到窗口: '
        # const: '✗ 未检测到窗口: '
        # const: '  当前窗口示例: '
        # const: ', '
        pass  # [META only - no bytecode recovered]

    def window_exists_v2(self, find_by, target):  # [META]
        """检测窗口是否存在（支持多种查找方式）"""
        # Referenced APIs: find_window, win32gui, GetWindowText, log, get, Exception
        # const: '进程名'
        # const: '窗口标题'
        # const: 'PID'
        # const: '✓ 检测到窗口: '
        # const: ' ['
        pass  # [META only - no bytecode recovered]

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

def precise_sleep(duration):  # [DISASM]
    """精确延时函数 - 使用忙等待实现高精度计时



Windows 的 time.sleep() 精度通常只有 10-15ms，

此函数通过忙等待实现更高精度的延时。



Args:

    duration: 延时时间（秒）"""
    # Referenced APIs: time, perf_counter, sleep
    # === Bytecode Disassembly ===
    #   74            NOP
    #                 NOP
    #                 LOAD_CONST               2 (None)
    #                 PUSH_NULL
    #   75            LOAD_CONST               3 (b'\xf0z\x1f\xf2W\x02\x00\x00\x03\x00\x00\x1a\x10\x01\x00\x00\x01\x00\x00\x00')
    #                 BUILD_TUPLE              1
    #                 CALL_FUNCTION_EX         0
    #                 POP_TOP
    #                 RESUME                   0
    #                 LOAD_CONST               1 (None)
    #                 STORE_FAST               1 (__assert_armored__)
    #                 NOP
    #                 NOP
    #   74            NOP
    #   92    L1:     LOAD_FAST                0 (duration)
    #                 LOAD_CONST               4 (0)
    #                 COMPARE_OP              58 (bool(<=))
    #                 POP_JUMP_IF_FALSE       11 (to L3)
    #   94    L2:     NOP
    #  114            LOAD_CONST               6 (None)
    #                 NOP
    #                 NOP
    #                 NOP
    #                 JUMP_FORWARD           137 (to L10)
    #                 CACHE
    #                 CACHE
    #                 CACHE
    #                 POP_TOP
    #                 RETURN_CONST             6 (None)
    #  100    L3:     LOAD_GLOBAL              0 (time)
    #                 LOAD_ATTR                2 (perf_counter)
    #                 PUSH_NULL
    #                 CALL                     0
    #                 LOAD_FAST                0 (duration)
    #                 BINARY_OP                0 (+)
    #                 STORE_FAST               2 (_var_var_0)
    #  106            LOAD_FAST                0 (duration)
    #                 LOAD_CONST               7 (0.02)
    #                 COMPARE_OP             148 (bool(>))
    #                 POP_JUMP_IF_FALSE       25 (to L4)
    #  108            LOAD_GLOBAL              0 (time)
    #                 LOAD_ATTR                4 (sleep)
    #                 PUSH_NULL
    #                 LOAD_FAST                0 (duration)
    #                 LOAD_CONST               8 (0.015)
    #                 BINARY_OP               10 (-)
    #                 CALL                     1
    #                 POP_TOP
    #  114    L4:     LOAD_GLOBAL              0 (time)
    #                 LOAD_ATTR                2 (perf_counter)
    # Full: docs/FINAL_DISASSEMBLY/precise_sleep.dis
    pass  # [DISASM available above]
