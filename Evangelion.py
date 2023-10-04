from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QButtonGroup, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QMessageBox, QGroupBox
from random import shuffle

class Question():
    def __init__(self, question, war_1, war_2, war_3):
        self.question = question
        self.war_1 = war_1
        self.war_2 = war_2
        self.war_3 = war_3
question_list = []
question_list.append(Question('Объявлена тревога! Выберите пилота!','Аянами Рей','С.Аска Ленгли','Синдзи Икари'))
question_list.append(Question('Выберите Евангелион','Eva-00','Eva-01','Eva-02'))

app = QApplication([])
window = QWidget()
window.setWindowTitle('Project "Evangelion"')
btn_OK = QPushButton('Answer')
main_Question = QLabel('Какой национальности не существует?')

R_G_B = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')
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

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result)
layout_res.addWidget(lb_Correct)
AnsGroupBox.setLayout(layout_res)
layout_line1.addWidget(main_Question)
layout_line2.addWidget(R_G_B)   
layout_line2.addWidget(AnsGroupBox)  
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
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
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
    shuffle(answers)
    answers[0].setText(q.war_1)
    answers[1].setText(q.war_2)
    answers[2].setText(q.war_3)
    main_Question.setText(q.question)
    show_question()

def next_question():
    window.total += 1
    print('Статистика\nВсего вопросов:', window.total,'\nПравильных ответов:', window.score)
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0
    q = question_list[window.cur_question]
    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить':
        next_question()
RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Project "Evangelion"')
window.cur_question = -1
btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0

next_question()
window.resize(600, 600)

window.show()
app.exec()