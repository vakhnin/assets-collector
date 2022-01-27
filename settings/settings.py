import pathlib

PATHFORSAVE = pathlib.Path('result/')

INCLUDEDIRS = [
    'Shutter'
]

EXCLUDEDIRS = [
    'source',
    'Release',
    'iStock',
    'Workspace',
    '(other)',
]

ASSETSROOTDIRS = [
    # pathlib.Path(r'd:\Google Диск\LinePoets\Works\(A-F)'),
    # pathlib.Path(r'd:\Google Диск\LinePoets\Works\(G-M)'),
    # pathlib.Path(r'd:\Google Диск\LinePoets\Works\(O-S)'),
    pathlib.Path(r'd:\Google Диск\LinePoets\Works\(T-Z)'),
]

STYLE_PATH = pathlib.Path.cwd() / 'html' / 'ac.css'

FAVICON_PATH = pathlib.Path.cwd() / 'html' / 'img' / 'favicon.ico'

THUMBNAILSIZE = 200, 200
