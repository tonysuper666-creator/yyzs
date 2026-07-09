# 未上传的大文件 (从解包目录)
# 这些可以 pip install 替代:

PyTorch5/Qt5/     (31.6 MB) → pip install pyqt5
cv2/               (28.5 MB) → pip install opencv-python
numpy/             (5.3 MB)  → pip install numpy
numpy.libs/        (4.2 MB)  → pip install numpy
cryptography/      (3.5 MB)  → pip install cryptography
PIL/               (2.9 MB)  → pip install pillow
setuptools/        (1.8 MB)  → pip install setuptools
libcrypto-3.dll    (1.6 MB)  → 系统自带或 pip install
base_library.zip   (1.4 MB)  → 标准库，Python自带
python313.dll      (1.8 MB)  → 安装 Python 3.13
VCRUNTIME140.dll   (118 KB)  → 系统自带
ucrtbase.dll       (993 KB)  → 系统自带
40+ api-ms-win-*.dll         → 系统自带
OpenSSL/           (0.2 MB)  → pip install
其余 Python 库目录            → pip install -r requirements.txt

# 结论: 除了 pyarmor_runtime.pyd 和 PYZ-00.pyz，
# 其余304MB都可以通过 pip install 获得
