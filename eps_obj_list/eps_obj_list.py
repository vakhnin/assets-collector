from PIL import Image

from html.html import CONTENTHTML, TOPHTML, BOTTOMHTML
from settings.settings import THUMBNAILSIZE, PATHFORSAVE


class EpsObj:
    def __init__(self, file):
        self._file = file
        self.name = file.stem
        print(self)

        self.make_html()
        self.make_thumbnail()

        exit()

    def __str__(self):
        return str(f'{self.name} {self._file}')

    def make_html(self):
        with PATHFORSAVE / 'ac.html' as file:
            file.write_text(TOPHTML
                            + CONTENTHTML.format(self.name, self.name)
                            + BOTTOMHTML)

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

