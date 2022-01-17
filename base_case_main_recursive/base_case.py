from PIL import Image

from ac import EXCLUDEDIRS, INCLUDEDIRS, THUMBNAILSIZE, PATHFORSAVE
from html import CONTENTHTML, TOPHTML, BOTTOMHTML


class BaseCaseMainRecursive:
    def __init__(self, files):
        self.files = files

    def check(self, files):
        parent_files_and_dirs = files[0].parent.name

        for dir in EXCLUDEDIRS:
            if dir.lower() in parent_files_and_dirs.lower():
                return False
        for dir in INCLUDEDIRS:
            if not dir.lower() in parent_files_and_dirs.lower():
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
            return True

    def base_case(self, eps_file):
        with Image.open(eps_file) as im:
            im = Image.open(eps_file)
            im.thumbnail(THUMBNAILSIZE)

            if not PATHFORSAVE.is_dir():
                PATHFORSAVE.mkdir()
            if not (PATHFORSAVE / 'img').is_dir():
                (PATHFORSAVE / 'img').mkdir()
            im.save(PATHFORSAVE / 'img' / 'test.jpg', 'JPEG')

        with PATHFORSAVE / 'ac.html' as file:
            file.write_text(TOPHTML + CONTENTHTML + BOTTOMHTML)
        exit()

    def is_eps_suffix(self, file):
        if file.suffix == '.eps':
            return True
        return False
