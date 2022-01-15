import glob
import os
import pathlib

ASSETSROOTDIRS = [
    pathlib.Path(r'd:\Google Диск\LinePoets\Works\(A-F)'),
]


def parse_folders(path):
    def is_end_dir(files_and_dirs_list):
        for file_or_dir in files_and_dirs_list:
            if pathlib.Path(file_or_dir).is_dir():
                return False
        return True

    files_and_dirs = glob.glob(str(path) + os.sep + "\\*", recursive=False)

    if is_end_dir(files_and_dirs):
        print(files_and_dirs)
        exit()
    else:
        for file_or_dir in files_and_dirs:
            if pathlib.Path(file_or_dir).is_dir():
                parse_folders(file_or_dir)


for root_dir in ASSETSROOTDIRS:
    parse_folders(root_dir)
