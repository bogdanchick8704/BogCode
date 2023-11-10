import tkinter as tk#импортируем библиотеку для создания UI интерфейса приложения


def st1():
    WIN1()


def WIN1():
    WIN1 = tk.Toplevel(win)
    WIN1.title("Первый вопрос")
    WIN1.geometry("500x600+1100+300")
    BUTTONS()
    WIN1.grid_columnconfigure(0, minsize=500)
    WIN1.grid_columnconfigure(1, minsize=500)
    WIN1.grid_columnconfigure(2, minsize=500)
    L_1 = tk.Label(WIN1, text="Тест по метапредмету",
                   bg="#60f5f7",
                   fg="white",
                   font=("Arial", 20, 'bold'),
                   width=20,
                   height=0,
                   anchor='n',
                   relief=tk.RAISED)  # заголовок в окне и его параметры(виджет)

    L_1.grid(row=0, column=0)  # расположение виджета на окне


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




win.mainloop()#запуск окна в главный цикл и режим ожидания
