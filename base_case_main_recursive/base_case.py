from eps_obj_list.eps_obj_list import EpsObj, main_list
from settings.settings import EXCLUDE_DIRS, INCLUDE_DIRS


class BaseCaseMainRecursive:
    def __init__(self, files):
        self.files = files

    def check(self, files):
        file = files[0]
        parent_files_and_dirs = files[0].parent.name

        for dir_ in EXCLUDE_DIRS:
            if dir_.lower() in parent_files_and_dirs.lower():
                return False
        for dir_ in INCLUDE_DIRS:
            if not dir_.lower() in parent_files_and_dirs.lower():
                print('\nWarning: dir is not in include dirs:')
                print(file)
                return False

            eps_list = []

            for file in files:
                if self.is_eps_suffix(file):
                    eps_list.append(file)
            if len(eps_list) == 0:
                print('\nWarning: directory does not include .eps files:')
                print(file)
                return False
            elif len(eps_list) > 1:
                print('\nWarning: directory includes more than one .eps files:')
                print(file)
                return False
            return eps_list[0]

    @staticmethod
    def base_case(eps_file):
        print('.', end='')
        eps_obj = EpsObj(eps_file)
        main_list.append(eps_obj)

    @staticmethod
    def is_eps_suffix(file):
        if file.suffix == '.eps':
            return True
        return False
