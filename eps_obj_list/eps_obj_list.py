import shutil
from datetime import datetime

from PIL import Image

from html.html import CONTENTHTML, TOPHTML, BOTTOMHTML
from settings.settings import THUMBNAILSIZE, PATHFORSAVE, FAVICON_PATH

main_list = []


class EpsObj:
    def __init__(self, file):
        self.file = file
        self.name = file.stem
        self.create_timestamp = file.stat().st_mtime
        self.create_date = datetime \
            .utcfromtimestamp(self.create_timestamp).strftime('%Y-%m-%d')
        self.make_thumbnail()

    def __str__(self):
        return str(f'{self.name} {self.create_date} {self.file}')

    def make_thumbnail(self):
        with Image.open(self.file) as im:
            im.thumbnail(THUMBNAILSIZE)

            if not (PATHFORSAVE / 'img').is_dir():
                (PATHFORSAVE / 'img').mkdir()
            if (PATHFORSAVE / 'img' / self.file.name).exists():
                print('Error: more then one name .eps files:')
                print(PATHFORSAVE / 'img' / self.file.name)
                return

            im.save(PATHFORSAVE / 'img' / (self.name + '.jpg'), 'JPEG')


def make_html(obj_list):
    names_list = []
    obj_list = sorted(obj_list, key=lambda x: x.create_date)

    shutil.copy(FAVICON_PATH, PATHFORSAVE / 'favicon.ico')

    with PATHFORSAVE / 'ac.html' as file:
        i = 0
        content = TOPHTML
        for obj in obj_list:
            color_row = ''
            if i % 2:
                color_row = ' class="grey-row"'
            i += 1

            double = ''
            if obj.name in names_list:
                print('\nWarning: More then one name:')
                print(obj.file)
                color_row = ' class="green-row"'
                double = ' (double)'
            names_list.append(obj.name)

            content += str(CONTENTHTML.
                           format(color_row, i, obj.name,
                                  obj.name + double, obj.create_date, obj.file))

        content += BOTTOMHTML
        file.write_text(content, encoding='utf-8')
