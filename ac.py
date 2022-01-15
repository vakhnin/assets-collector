import glob
import os
import pathlib

ASSETSROOTDIRS = [
    pathlib.Path(r'd:\Google Диск\LinePoets\Works\(A-F)'),
]


def parse_folders(path):
    for subpath in glob.glob(str(path) + os.sep + "\\*", recursive=False):
        print(subpath)


for root_dir in ASSETSROOTDIRS:
    parse_folders(root_dir)
