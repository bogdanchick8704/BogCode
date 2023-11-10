import random
import time
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
t_start = time.monotonic()
a = True

'''class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Тест")
        self.setGeometry(960, 540, 350, 450)

        self.newText = QLabel(self)

        self.main_text = QLabel(self)
        self.main_text.setText("Вас приветствует метапредметный тест. \nПеред началом настоятельно рекомендуется \nпрочитать теоретический материал,который \nбудет представлен ниже")
        self.main_text.move(80,100)
        self.main_text.adjustSize()
        self.btn = QPushButton(self)
        self.btn.move(80, 200)
        self.btn.setText("Нажмите для показа теории")
        self.btn.setFixedWidth(200)
        self.btn.clicked.connect(self.theory)



    def theory(self):
        self.newText.setText("ТЕОРЕТИЧЕСКАЯ ЧАСТЬ")




def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    application()
'''


while a:
    print('(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Вас приветствует метапредметный тест. Перед началом настоятельно рекомендуется прочитать теоретический материал,который будет представлен ниже ')
    print()
    questions = {"1) Основатель книгопечатания в России и на Украине, издатель первой в Российском государстве точно датированной печатной книги «Апостол».":'Иван Федоров',
                 "2) В 1581 г. на средства купцов Строгановых для похода в Сибирь был снаряжён отряд казаков, который возглавил казачий атаман":'Ермак Тимофеевич',
                 "3) В период правления Ивана Грозного Россия вела _______________ войну.:":'Ливонскую',
                 "4) Прочтите отрывок из сочинения историка и укажите море, название которого пропущено в тексте. \n «В итоге Северной войны коренным образом изменилось международное положение России.Она стала одной из великих держав мира. \n Отныне без её участия не мог решаться ни одинкрупный международный вопрос. Приобретение надёжного выхода к _______________ морю содействовало сближению Русского государства с другими европейскими странами. \n После Ништадтского мира постоянными факторами международных отношений становятся взаимодействие России и Западной Европы и взаимное влияние их друг на друга.  \n Все это явилось результатом усилий русской армии и только что созданного в России военно-морского флота. По образному выражению Пушкина, Россия вошла в семью европейских держав,""как спущенный корабль, \n — при стуке топора и громе пушек"".":'Балтийское',
                 "5) Какой из приведённых памятников культуры был создан в XIX в.? \n 1) «Задонщина»; \n 2) роман «Война и мир»; \n 3) «Калязинская челобитная»":'2',
                 "6) Аркадию 28 лет, он работает врачом. Какие обязанности есть у него как у гражданинаРоссии? Запишите цифры, под которыми они указаны. 1) заключать трудовой договор 2) вносить вклады в кредитные учреждения 3) заботиться о сохранении исторического и культурного наследия 4) платить налоги 5) распоряжаться своим заработком":'34',
                 "7) Найдите в приведённом ниже списке два примера финансово грамотных действий граждан при инвестировании и запишите цифры, под которыми они указаны. \n 1) Лавр, рассчитывая на высокие доходы, инвестировал в рискованные активы и разочаровался, увидев первые убытки \n 2) Порфирий выбирал инвестиционные инструменты, не определив заранее сумму и периодичность инвестирования. \n 3) Эмилия, формируя свой первый инвестиционный портфель, чётко представляла, сколько процентов от вложенной суммы она готова потерять без сожаления. \n 4) Глафира внимательно изучила информацию о собственных основных средствах и других дорогостоящих активах финансовой организации. \n 5) Давид приобрёл финансовые инструменты под влиянием эмоций.":'34',
                 "8) Пётр получил CМС-сообщение от известного банка о том, что этот банк проводит опрос потребителей финансовых услуг. Петру предлагалось перейти по ссылке на интернет-сайт, пройти опрос и получить вознаграждение в 10 тысяч рублей. Для получения доступа к опросу требовалось перечислить со счёта телефона 200 рублей. В чём состоит опасность данной ситуации для личных финансов Петра? Как ему правильно поступить в данной ситуации? \n 1) Перевести деньги \n 2) Игнорировать сообщение":'2'
                 }
    shuffled_questions = list(questions.keys())
    random.shuffle(shuffled_questions)


    for question in shuffled_questions:
        print(question)
        answer = input("Ваш ответ: ")
        if answer.lower() != questions[question].lower():
            print("Неправильный ответ. Попробуйте еще раз.")
            break
        else:
            print("Правильно, идём дальше")
    else:
        a = False

t_stop = time.monotonic()
t_run = t_stop - t_start


print("Поздравляю, вы прошли тест! Итоговое время в секундах: ",t_run)