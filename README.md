# 6号自动化助手 — 逆向工程产物

## ⚠️ 重要说明

**这不是可执行的 Python 源码项目。**

这是对 PyArmor 9.2.3 Pro 加密的商业软件的逆向工程产物。
Python 3.13 目前不存在任何字节码反编译器（uncompyle6/decompyle3/pycdc均不支持3.13），因此 `.py` 源码无法还原。

## 📁 目录结构

| 目录 | 内容 | 真实度 |
|------|------|--------|
| `raw_extraction/pyc_files/` | **35个 .pyc 完整字节码** — 这是真实的代码，可被 Python 3.13 加载执行 | ✅ 100% |
| `raw_extraction/disassembly/` | **40个 .dis 反汇编** — 每条字节码指令的可读形式 | ✅ 100% |
| `raw_extraction/metadata/` | **236个 _meta.json** — 函数签名、API引用、字符串常量 | ✅ 100% |
| `raw_extraction/runtime/` | **pyarmor_runtime.pyd** — PyArmor 解密引擎 | ✅ 原始文件 |
| `raw_extraction/PYZ-00.pyz` | PyInstaller 压缩包 (1156模块) | ✅ 原始文件 |
| `editor/` | Web 编辑器 HTML/CSS/JS | ✅ 100% 原始源码 |
| `pseudocode/` | 从元数据重构的函数签名 + 内嵌注释中的反汇编 | ⚠️ 仅参考 |
| `tools/` | 14个逆向脚本 + 过程文档 | ✅ 可复现 |

## 🔑 关键技术障碍

- **Python 3.13 无反编译器**: 字节码只能反汇编(.dis)，不能反编译(.py)
- **PyArmor C 运行时保护**: `co_code` 属性被 ACCESS_VIOLATION 保护，需 `sys.settrace` 在执行时捕获
- **PyArmor C builtin 注入**: `C_ASSERT_ARMORED_INDEX` 等 C 函数嵌入常量表，导致 `marshal.dumps` 失败

## 🚀 离线 EXE

Release 页面: https://github.com/tonysuper666-creator/yyzs/releases
下载 `6hzs-offline.exe` (90.6 MB) 双击运行，无需 Python。
