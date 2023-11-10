def say_udachi():
    print('Тест начался,удачи!')

def add_label():
    label = tk.Label(win,text='Тест начался,удачи')
    label.pack()


def st1():
    start_window1()


def WIN1():
    WIN1 = tk.Toplevel(win)
    WIN1.title("Первый вопрос")
    WIN1.geometry("500x600+600+300")



'''
questions={'сколько будет 2+2':'4','сколько будет 3+3':'6'}
score=0
def test(score):
    for i, j in questions.items():
        print(i)
        answer=(input('Ваш ответ: '))
        if answer != j:
            print('Ответ неверный')
        else:
            print('Верный ответ, идём дальше')
            score+=1
    print('Вы набрали', score, 'очков')


test(score)

'''


import tkinter as tk#импортируем библиотеку для создания UI интерфейса приложения



win = tk.Tk()#создание главного окна
photo = tk.PhotoImage(file="stud.png")#установить иконку
win.iconphoto(False, photo)#вспомогательная команда для размещения иконки
win.title("Тест")#заголовок программы
L_1 = tk.Label(win, text= "Тест по метапредмету",
                    bg="#60f5f7",
                    fg="white",
                    font=("Arial",20,'bold'),
                    width=20,
                    height=0,
                    anchor='n',
                    relief=tk.RAISED)#заголовок в окне и его параметры(виджет)

L_1.grid(row=0, column=0)#расположение виджета на окне
win.geometry("500x600+600+300")#задать размеры и расположение окна




def BUTTONS():
    tk.Button(text='A').grid(row=1, column=0, stick='we')
    tk.Button(text='B').grid(row=2, column=0, stick='we')
    tk.Button(text='C').grid(row=3, column=0, stick='we')
    tk.Button(text='D').grid(row=4, column=0, stick='we')

tk.Button(text='Начать тест',command=WIN1).grid(row=5, column=0, stick='we')



win.grid_columnconfigure(0,minsize=500)
win.grid_columnconfigure(1,minsize=500)
win.grid_columnconfigure(2,minsize=500)


BUTTONS()


'''btn2 = tk.Button(win, text='Нажми для продолжения',
                             command=add_label
                                     )#задача кнопки и текст

btn3 = tk.Button(win, text='a',
                             command=add_label)


btn4 = tk.Button(win, text='b',
                             command=add_label)

btn5 = tk.Button(win, text='c',
                             command=add_label)

btn6 = tk.Button(win, text='d',
                             command=add_label)


btn2.pack()#размещение кнопки
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()'''

win.mainloop()#запуск окна в главный цикл и режим ожидания
