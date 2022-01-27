import glob
import os
import pathlib
import shutil

from PIL import EpsImagePlugin

from base_case_main_recursive.base_case import BaseCaseMainRecursive
from eps_obj_list.eps_obj_list import main_list, make_html
from settings.settings import ASSETS_ROOT_DIRS, PATH_FOR_SAVE

EpsImagePlugin.gs_windows_binary = r'D:\Program Files\gs\gs9.26\bin\gswin64c'


def parse_folders(path):
    def is_end_dir(files_and_dirs_list):
        for file_or_dir_ in files_and_dirs_list:
            if file_or_dir_.is_dir():
                return False
        return True

    files_and_dirs = glob.glob(str(path) + os.sep + "\\*", recursive=False)
    for i in range(len(files_and_dirs)):
        files_and_dirs[i] = pathlib.Path(files_and_dirs[i])

    if is_end_dir(files_and_dirs):
        base_case = BaseCaseMainRecursive(files_and_dirs)
        eps_file = base_case.check(base_case.files)
        if eps_file:
            base_case.base_case(eps_file)
    else:
        for file_or_dir in files_and_dirs:
            if pathlib.Path(file_or_dir).is_dir():
                parse_folders(file_or_dir)


if PATH_FOR_SAVE.exists():
    shutil.rmtree(PATH_FOR_SAVE)

if not PATH_FOR_SAVE.is_dir():
    PATH_FOR_SAVE.mkdir()

for root_dir in ASSETS_ROOT_DIRS:
    parse_folders(root_dir)


make_html(main_list)
