# 逆向过程文档

## 使用的工具
- pyinstxtractor-ng: PyInstaller 解包
- Python 3.13: 运行 PyArmor 解密
- PyInstaller: 重新打包离线 EXE
- sys.settrace: 运行时字节码捕获
- ctypes: 内存绕过尝试

## 破解步骤
1. pyinstxtractor-ng 解包 → 425个文件
2. 识别 PyArmor 9.2.3 Pro 保护
3. 导入 pyarmor_runtime_011372 运行时
4. co.replace() 清理 C builtin 常量 → 13个函数
5. sys.settrace 执行时捕获 → 22个函数
6. 总计 35个函数完整字节码

## 关键脚本
- master_final.py: 主提取脚本（子进程隔离）
- master_batch.py: 批量提取（每模块一个子进程）
- trace_extract.py: sys.settrace 字节码捕获
- gen_source.py: 生成 src/ 伪代码
- decompile_all.py: 反编译 .pyc → .dis

## 离线 EXE 构建
- launcher.py: 补丁启动器
- PyInstaller --onefile 打包 → 6hzs-offline.exe
