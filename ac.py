import glob
import os
import pathlib

from PIL import Image, EpsImagePlugin

EpsImagePlugin.gs_windows_binary = r'D:\Program Files\gs\gs9.26\bin\gswin64c'

ASSETSROOTDIRS = [
    pathlib.Path(r'd:\Google Диск\LinePoets\Works\(A-F)'),
]


def parse_folders(path):
    def is_end_dir(files_and_dirs_list):
        for file_or_dir in files_and_dirs_list:
            if file_or_dir.is_dir():
                return False
        return True

    def is_eps_suffix(file):
        if file.suffix == '.eps':
            return True
        return False

    files_and_dirs = glob.glob(str(path) + os.sep + "\\*", recursive=False)
    for i in range(len(files_and_dirs)):
        files_and_dirs[i] = pathlib.Path(files_and_dirs[i])

    if is_end_dir(files_and_dirs):
        for file in files_and_dirs:
            if is_eps_suffix(file):
                print(file)
                image = Image.open(file)
                image.show()
                exit()
    else:
        for file_or_dir in files_and_dirs:
            if pathlib.Path(file_or_dir).is_dir():
                parse_folders(file_or_dir)


for root_dir in ASSETSROOTDIRS:
    parse_folders(root_dir)
