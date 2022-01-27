import pathlib

PATH_FOR_SAVE = pathlib.Path('result/')

COLLECTOR_PROFILE = 'Shutter'

INCLUDE_DIRS = [
    'Shutter'
]

EXCLUDE_DIRS = [
    'source',
    'Release',
    'iStock',
    'Workspace',
    '(other)',
]

ASSETS_ROOT_DIRS = [
    # pathlib.Path(r'd:\Google Диск\LinePoets\Works\(A-F)'),
    # pathlib.Path(r'd:\Google Диск\LinePoets\Works\(G-M)'),
    # pathlib.Path(r'd:\Google Диск\LinePoets\Works\(O-S)'),
    pathlib.Path(r'd:\Google Диск\LinePoets\Works\(T-Z)'),
]

STYLE_PATH = pathlib.Path.cwd() / 'html' / 'ac.css'

FAVICON_PATH = pathlib.Path.cwd() / 'html' / 'img' / 'favicon.ico'

THUMBNAIL_SIZE = 200, 200
