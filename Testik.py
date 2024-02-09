import random
import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(95, 161, 223);\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:1, y2:0.517, stop:0 rgba(1, 45, 52, 137), stop:1 rgba(128, 204, 85, 135));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.523, x2:1, y2:0.505636, stop:0 rgba(0, 49, 45, 255), stop:1 rgba(128, 38, 74, 135));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Text_Label = QtWidgets.QLabel(self.centralwidget)
        self.Text_Label.setScaledContents(True)
        self.Text_Label.setWordWrap(True) 
        self.Text_Label.setGeometry(QtCore.QRect(-1, 10, 800, 220))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.Text_Label.setFont(font)
        self.Text_Label.setMouseTracking(False)
        self.Text_Label.setTabletTracking(False)
        self.Text_Label.setAutoFillBackground(False)
        self.Text_Label.setStyleSheet("background-color: rgba(152, 46, 173, 20);\n"
"color: rgb(231, 231, 231);")
        self.Text_Label.setObjectName("Text_Label")
        self.Text_Label.setAlignment(QtCore.Qt.AlignTop)

        self.Vvod = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Vvod.setGeometry(QtCore.QRect(200, 410, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Vvod.setFont(font)
        self.Vvod.setStyleSheet("background-color: rgb(83,147, 130);\n"
"color: rgb(225, 225, 225);\n"
"background-color: rgb(57, 57, 57);")
        self.Vvod.setObjectName("Vvod")

        self.Otvet_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Otvet_Button.clicked.connect(self.check_answer)
        self.Otvet_Button.setEnabled(False)
        self.Otvet_Button.setGeometry(QtCore.QRect(610, 410, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.Otvet_Button.setFont(font)
        self.Otvet_Button.setStyleSheet("background-color: rgb(52, 156, 76);\n")
        self.Otvet_Button.setObjectName("Otvet_Button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.Start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Button.setGeometry(QtCore.QRect(360, 450, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        self.Start_Button.setFont(font)
        self.Start_Button.setStyleSheet("background-color: rgb(52, 156, 76);\n"
"color: rgb(194, 194, 194);\n"
"background-color: rgba(146, 7, 156, 150);")
        self.Start_Button.setObjectName("Start_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.Start_Button.clicked.connect(self.load_questions)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.create_questions()


    def set_question_text(self, question):
        self.Text_Label.setText(question)

    
    def check_answer(self):
        user_answer = self.Vvod.toPlainText()
        if self.correct_answers and user_answer.lower() == self.correct_answers[0].lower():
            self.correct_answers.pop(0)

            self.Vvod.setPlainText("")
            if self.shuffled_questions:
                self.load_questions()
            else:
                self.display_result(self.t_start)
        else:
            self.Text_Label.setText("Неверный ответ. Нажмите 'Начать тест'")
            self.Vvod.setPlainText("")
            self.create_questions() 
    
        
    def load_questions(self):
        if self.shuffled_questions:
              question = self.shuffled_questions.pop(0)
              self.Text_Label.setText(question)
              self.Otvet_Button.setEnabled(True)
        else:
            self.display_result(self.t_start)
              
              
    def create_questions(self):
        self.t_start = time.monotonic()
        self.questions = {}
        self.correct_answers = []
        with open('config.txt', 'r', encoding='utf8') as file:
                lines = file.readlines()
        for line in lines:
                key, value = line.strip().split(':')
                self.questions[key.strip()] = value.strip()
        self.shuffled_questions = list(self.questions.keys())
        random.shuffle(self.shuffled_questions)
        for i in self.shuffled_questions:
            self.correct_answers.append(self.questions[i])


    def display_result(self, t_start):
        t_stop = time.monotonic()
        t_run = t_stop - t_start
        self.Text_Label.setText(f"Поздравляю, вы прошли тест. Итоговое время в секундах: {t_run:.2f}")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Test"))
        self.Start_Button.setText(_translate("MainWindow", "Начать"))
        self.Otvet_Button.setText(_translate("MainWindow", "Ответить"))
        self.Text_Label.setText(_translate("MainWindow", "Нажмите 'Начать'"))

                        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
