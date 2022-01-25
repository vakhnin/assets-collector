from datetime import datetime

from PIL import Image

from html.html import CONTENTHTML, TOPHTML, BOTTOMHTML
from settings.settings import THUMBNAILSIZE, PATHFORSAVE

main_list = []


class EpsObj:
    def __init__(self, file):
        self._file = file
        self.name = file.stem
        self.create_timestamp = file.stat().st_ctime
        self.create_date = datetime \
            .utcfromtimestamp(self.create_timestamp).strftime('%Y-%m-%d')
        self.make_thumbnail()

    def __str__(self):
        return str(f'{self.name} {self.create_date} {self._file}')

    def make_thumbnail(self):
        with Image.open(self._file) as im:
            im.thumbnail(THUMBNAILSIZE)

            if not (PATHFORSAVE / 'img').is_dir():
                (PATHFORSAVE / 'img').mkdir()
            if (PATHFORSAVE / 'img' / self._file.name).exists():
                print('Error: more then one name .eps files:')
                print(PATHFORSAVE / 'img' / self._file.name)
                return

            im.save(PATHFORSAVE / 'img' / (self.name + '.jpg'), 'JPEG')


def make_html(obj_list):
    with PATHFORSAVE / 'ac.html' as file:
        i = 0
        content = TOPHTML
        for obj in obj_list:
            grey_row = ''
            if i % 2:
                grey_row = ' class="grey-row"'
            i += 1
            content += str(CONTENTHTML.
                           format(grey_row, i, obj.name, obj.name, obj.create_date))
        content += BOTTOMHTML
        file.write_text(content, encoding='utf-8')
