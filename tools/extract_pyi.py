import pyinstxtractor_ng
import os

input_file = r"C:\Users\1\Downloads\Telegram Desktop\6hzsv2.23.exe"
output_parent = r"C:\Users\1\Downloads\Telegram Desktop"
output_dir = os.path.join(output_parent, os.path.basename(input_file) + "_extracted")

# Switch to output directory so extractFiles creates the right folder
os.chdir(output_parent)

arch = pyinstxtractor_ng.PyInstArchive(input_file)
if arch.open():
    if arch.checkFile():
        if arch.getCArchiveInfo():
            arch.parseTOC()
            arch.printInfo()
            arch.extractFiles(True)  # True = one_dir mode
            print("Extraction complete!")
else:
    print("Failed to open archive")
