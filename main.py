from pathlib import Path
from docx import Document

DATA_DIR = 'data'

def get_list_file():
    res = []
    for file in Path(DATA_DIR).glob('*.docx'):
        res.append(file)
    return res


