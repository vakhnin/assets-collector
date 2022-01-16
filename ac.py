import glob
import os
import pathlib

from PIL import Image, EpsImagePlugin

EpsImagePlugin.gs_windows_binary = r'D:\Program Files\gs\gs9.26\bin\gswin64c'

EXCLUDEDIRS = [
    'sources',
    'Releases',
    'iStock',
]

ASSETSROOTDIRS = [
    pathlib.Path(r'd:\Google Диск\LinePoets\Works\(T-Z)'),
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
        eps_list = []
        parent_files_and_dirs = files_and_dirs[0].parent.name
        for dir in EXCLUDEDIRS:
            if dir.lower() in parent_files_and_dirs.lower():
                return
        print(parent_files_and_dirs)
        for file in files_and_dirs:
            if is_eps_suffix(file):
                eps_list.append(file)
                image = Image.open(file)
                # image.show()
                # exit()
        if len(eps_list) == 0:
            print(parent_files_and_dirs)
    else:
        for file_or_dir in files_and_dirs:
            if pathlib.Path(file_or_dir).is_dir():
                parse_folders(file_or_dir)


for root_dir in ASSETSROOTDIRS:
    parse_folders(root_dir)
