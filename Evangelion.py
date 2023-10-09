from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QButtonGroup, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QMessageBox, QGroupBox

class Question():
    def __init__(self, question, war_1, war_2, war_3):
        self.question = question
        self.war_1 = war_1
        self.war_2 = war_2
        self.war_3 = war_3
        
question_list = []
question_list_2 = []
question_list.append(Question('Объявлена тревога! Выберите пилота!','Аянами Рей','С.Аска Ленгли','Синдзи Икари'))
question_list.append(Question('Выберите Евангелион','Eva-00','Eva-01','Eva-02'))
question_list.append(Question('Проведение диагностики','','',''))
question_list.append(Question('Подача LCL','','',''))
question_list.append(Question('Подключение контактного комбинезона','','',''))
question_list.append(Question('Синхронизация пилота','','',''))
question_list.append(Question('Диагностика завершена','','',''))
question_list.append(Question('!Запуск Евангелиона!','','',''))
question_list_2.append(Question('Вы обнаружили ангела, командующий Икари дал приказ - уничтожить ангела, выберите действие:',
    'Использоать позитронную винтовку','Использовать виброкинжал','Вступить в рукопашный бой'))
app = QApplication([])
window = QWidget()
window_2 = QWidget()
window.setWindowTitle('Project "Evangelion"')
window_2.setWindowTitle('Project "Evangelion"')
btn_OK = QPushButton('Answer')
main_Question = QLabel('Какой национальности не существует?')

R_G_B = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
R_G_B.setLayout(layout_ans1)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line1.addWidget(main_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(R_G_B)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2 )
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

layout_line1.addWidget(main_Question)
layout_line2.addWidget(R_G_B) 
R_G_B.hide()
layout_line3.addWidget(btn_OK, stretch=2)
def show_result():
    ''' показать панель ответов '''
    R_G_B.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    ''' показать панель вопросов '''
    R_G_B.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    
    RadioGroup.setExclusive(True)
def test():
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()
answers = [rbtn_1, rbtn_2, rbtn_3]
def ask(q: Question):
    answers[0].setText(q.war_1)
    answers[1].setText(q.war_2)
    answers[2].setText(q.war_3)
    main_Question.setText(q.question)
    show_question()

def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
        window.close()
    q = question_list[window.cur_question]
    ask(q)
def next_question_2():
    window.cur_question_2= window.cur_question_2 + 1
    if window.cur_question == len(question_list_2):
        window.cur_question = 0
        window_2.show()
    q = question_list[window.cur_question_2]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить':
        next_question()
def click_OK_2():
    if btn_OK.text() == 'Ответить':
        next_question_2()
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)

window = QWidget()
window_2 = QWidget()
window.setLayout(layout_card)
window_2.setLayout(layout_card)
window.setWindowTitle('Project "Evangelion"')
window_2.setWindowTitle('Project "Evangelion"')
window.cur_question = -1
btn_OK.clicked.connect(click_OK)
btn_OK.clicked.connect(click_OK_2)
next_question()
window.resize(600, 600)
window_2.resize(600, 600)

window.show()
app.exec()
