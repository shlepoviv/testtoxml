from pathlib import Path
from docx import Document

from src.class_moodle_question import MoodleQuestion

DATA_DIR = 'data'

def get_list_file():
    res = []
    for f in Path(DATA_DIR).glob('*.docx'):
        res.append(f)
    return res

def clearing_text(text):
    def clearing(s:str):               
        i = 0
        while not s[i].isalpha() and i <len(s):
            i +=1
        return s[i:]
    if isinstance(text,list):
        for i in range(len(text)):
            text[i] = clearing(text[i])    
    else:
        return clearing(text)


def parse_doc(document,name_file:list,list_qyestion:list):
    i = 0
    while i <= len(document.paragraphs):
        question = MoodleQuestion()
        question.question = clearing_text(document.paragraphs[i].text)
        list_anwer_options = []
        i += 1
        while document.paragraphs[i].text != '':      
            list_anwer_options.append(document.paragraphs[i].text)
            i += 1
        question.answer_options = clearing_text(list_anwer_options[:-1])
        question.correct_answer_number = int(list_anwer_options[-1])
        question.topyc = name_file
        list_qyestion.append(question)

            


list_questions = []


for file in get_list_file():
    doc = Document(file)
    parse_doc(doc,file.name,list_questions)

