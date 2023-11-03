from pathlib import Path
from docx import Document

from src.class_moodle_question import MoodleQuestion
from src.export import export_to_xml

from conf import DATA_DIR

def get_list_file():
    res = []
    for f in Path(DATA_DIR).glob('*.docx'):
        res.append(f)
    return res

def clearing_text(text):
    def clearing(s:str):               
        i = 0
        while i <len(s) and not s[i].isalpha():
            i +=1
        return s[i:]
    if isinstance(text,list):
        for i in range(len(text)):
            text[i] = clearing(text[i]) 
        return text   
    else:
        return clearing(text)


def parse_doc(document,name_file,questions:list):
    i = 0
    while i < len(document.paragraphs):
        question = MoodleQuestion()
        while document.paragraphs[i].text == '':  
            i += 1  
            if i >= len(document.paragraphs): break            
        question.question = clearing_text(document.paragraphs[i].text)
        list_anwer_options = []
        i += 1
        if i >= len(document.paragraphs): break
        while document.paragraphs[i].text != '':      
            list_anwer_options.append(document.paragraphs[i].text)
            i += 1
            if i >= len(document.paragraphs): break
        question.answer_options = clearing_text(list_anwer_options[:-1])
        question.correct_answer_number = int(list_anwer_options[-1])
        question.tag = name_file
        questions.append(question)

list_questions = []


for file in get_list_file():
    doc = Document(file)
    parse_doc(doc,file.stem,list_questions)

export_to_xml(list_questions,'text.xml')
