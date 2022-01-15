import glob
import pathlib

ASSETSROOTDIRS = [
    pathlib.Path(r'd:\Google Диск\LinePoets\Works\(A-F)'),
]


def parse_folders(path):
    # for subpath in path.glob("**"):
    #     print(subpath)
    for subpath in glob.glob(r'd:\Google Диск\LinePoets\Works\(A-F)\*', recursive=False):
        print(subpath)


for root_dir in ASSETSROOTDIRS:
    parse_folders(root_dir)
