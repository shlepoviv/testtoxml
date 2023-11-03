from pathlib import Path
import xml.etree.ElementTree as ET

from conf import DATA_DIR

def export_to_xml(questions:list,file_name):
    quiz = ET.Element('quiz')

    elquestion = ET.SubElement(quiz, 'question')
    elquestion.set('type',"category")

    elcategory = ET.SubElement(elquestion,'category')

    eltext = ET.SubElement(elcategory,'text')
    eltext.text = "$system$/top/По умолчанию для Система"

    elinfo = ET.SubElement(elquestion,'info')
    elinfo.set('format','moodle_auto_format')

    eltext = ET.SubElement(elinfo,'text')
    eltext.text = 'Категория по умолчанию для общих вопросов в контексте «Система».'

    elidnumber = ET.SubElement(elquestion,'idnumber')
    
    for question in questions:

        elquestion = ET.SubElement(quiz, 'question')     
        elquestion.set('type',"multichoice")

        elname = ET.SubElement(elquestion,'name')
        eltext = ET.SubElement(elname,'text')
        eltext.text = 'Вопрос'

        elquestiontext = ET.SubElement(elquestion,'questiontext')
        elquestiontext.set('format',"html")

        eltext = ET.SubElement(elquestiontext,'text')
        eltext.text = question.question

        elgeneralfeedback = ET.SubElement(elquestion,'generalfeedback')
        elgeneralfeedback.set('format','html')
        eltext = ET.SubElement(elgeneralfeedback,'text')

        eldefaultgrade = ET.SubElement(elquestion,'defaultgrade')
        eldefaultgrade.text = '1'

        elpenalty = ET.SubElement(elquestion,'penalty')
        elpenalty.text = '0.3333333'

        elhidden = ET.SubElement(elquestion,'hidden')
        elhidden.text = '0'

        elidnumber = ET.SubElement(elquestion,'idnumber')

        elsingle = ET.SubElement(elquestion,'single')

        elshuffleanswers = ET.SubElement(elquestion,'shuffleanswers')
        elshuffleanswers.text = 'true'

        elanswernumbering = ET.SubElement(elquestion,'answernumbering')
        elanswernumbering.text = 'abc'

        elshowstandardinstruction = ET.SubElement(elquestion,'showstandardinstruction')
        elshowstandardinstruction.text = '0'

        elcorrectfeedback = ET.SubElement(elquestion,'correctfeedback')
        elcorrectfeedback.set('format','html')

        eltext = ET.SubElement(elcorrectfeedback,'text')
        eltext.text = 'Ваш ответ верный.'

        elpartiallycorrectfeedback = ET.SubElement(elquestion,'partiallycorrectfeedback')
        elpartiallycorrectfeedback.set('format','html')

        eltext = ET.SubElement(elpartiallycorrectfeedback,'text')
        eltext.text = 'Ваш ответ частично правильный.'

        elincorrectfeedback = ET.SubElement(elquestion,'incorrectfeedback')
        elincorrectfeedback.set('format','html')

        eltext = ET.SubElement(elincorrectfeedback,'text')
        eltext.text = 'Ваш ответ частично правильный.'

        elshownumcorrect = ET.SubElement(elquestion,'shownumcorrect')

        for answer in enumerate(question.answer_options):
            elanswer = ET.SubElement(elquestion,'answer')  
            elanswer.set('format','html')
            elanswer.set('fraction','100' if answer[0] == question.correct_answer_number else '0')

            eltext = ET.SubElement(elanswer,'text') 
            eltext.text = answer[1] 

            elfeedback = ET.SubElement(elanswer,'feedback') 
            elfeedback.set('format','html')

            eltext = ET.SubElement(elfeedback,'text')

        eltags = ET.SubElement(elquestion,'tags')
        eltag = ET.SubElement(eltags,'tag')
        eltext = ET.SubElement(eltag,'text')
        eltext.text = question.tag


    tree = ET.ElementTree(quiz)
    ET.indent(tree, '   ')
    tree.write(Path(DATA_DIR,file_name), encoding="utf-8", xml_declaration=True)