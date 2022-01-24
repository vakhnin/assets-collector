import shutil

from PIL import Image

from html.html import CONTENTHTML, TOPHTML, BOTTOMHTML
from settings.settings import EXCLUDEDIRS, INCLUDEDIRS, THUMBNAILSIZE, PATHFORSAVE


class BaseCaseMainRecursive:
    def __init__(self, files):
        self.files = files

    def check(self, files):
        parent_files_and_dirs = files[0].parent.name

        for dir_ in EXCLUDEDIRS:
            if dir_.lower() in parent_files_and_dirs.lower():
                return False
        for dir_ in INCLUDEDIRS:
            if not dir_.lower() in parent_files_and_dirs.lower():
                print('Warning: dir is not in include dirs:')
                print(parent_files_and_dirs)
                return False

            eps_list = []

            for file in files:
                if self.is_eps_suffix(file):
                    eps_list.append(file)
            if len(eps_list) == 0:
                print('Warning: directory does not include .eps files:')
                print(parent_files_and_dirs)
                return False
            elif len(eps_list) > 1:
                print('Warning: directory includes more than one .eps files:')
                print(parent_files_and_dirs)
                return False
            return eps_list[0]

    def base_case(self, eps_file):
        if PATHFORSAVE.exists():
            shutil.rmtree(PATHFORSAVE)

        with Image.open(eps_file) as im:
            im = Image.open(eps_file)
            im.thumbnail(THUMBNAILSIZE)

            if not PATHFORSAVE.is_dir():
                PATHFORSAVE.mkdir()
            if not (PATHFORSAVE / 'img').is_dir():
                (PATHFORSAVE / 'img').mkdir()
            if (PATHFORSAVE / 'img' / eps_file.name).exists():
                print('Error: more then one name .eps files:')
                print(PATHFORSAVE / 'img' / eps_file.name)
                return
            im.save(PATHFORSAVE / 'img' / eps_file.name, 'JPEG')

        with PATHFORSAVE / 'ac.html' as file:
            file.write_text(TOPHTML + CONTENTHTML + BOTTOMHTML)
        exit()

    def is_eps_suffix(self, file):
        if file.suffix == '.eps':
            return True
        return False
