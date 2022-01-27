import base64
import io
from datetime import datetime

from PIL import Image

from html.html import CONTENT_HTML, TOP_HTML, BOTTOM_HTML
from settings.settings import THUMBNAIL_SIZE, PATH_FOR_SAVE, FAVICON_PATH, STYLE_PATH, COLLECTOR_PROFILE

main_list = []
thumbnail_dict = {}


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
            im.thumbnail(THUMBNAIL_SIZE)

            img_byte_arr = io.BytesIO()
            im.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            thumbnail_dict[self.name] = base64.b64encode(img_byte_arr).decode('ascii')


def make_html(obj_list):
    names_list = []
    obj_list = sorted(obj_list, key=lambda x: x.create_date)

    with STYLE_PATH as style_path:
        style = style_path.read_text()

    with Image.open(FAVICON_PATH) as favicon:
        img_byte_arr = io.BytesIO()
        favicon.save(img_byte_arr, format='ICO')
        img_byte_arr = img_byte_arr.getvalue()

        favicon_base64 = base64.b64encode(img_byte_arr).decode('ascii')

    with PATH_FOR_SAVE / 'ac.html' as file:
        i = 0
        content = TOP_HTML.format(
            style, favicon_base64, ' - ' + COLLECTOR_PROFILE, ' - ' + COLLECTOR_PROFILE)
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

            content += str(CONTENT_HTML.
                           format(color_row, i, thumbnail_dict[obj.name],
                                  obj.name + double, obj.create_date, obj.file))

        content += BOTTOM_HTML
        file.write_text(content, encoding='utf-8')
