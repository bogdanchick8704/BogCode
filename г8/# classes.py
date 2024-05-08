# class
class Critter(object):
    total = 0
    @staticmethod
    def status():
        print(f"Всего зверюшек сейчас: {Critter.total}")


    def __init__(self, name, mood):
        print("Появилась на свет новая зверюшка\n")
        self.name = name
        Critter.total += 1

        self.__mood = mood

    def __private_method(self):
        print("Это закрытый метод")# метод закррыт для доступа из main, но другие методы **класса** могут пользоваться и скрытым методом, и скрытыми атрибутами. 


    def public_method(self):
        print("Это открытый метод")
        self.__private_method()


    def __str__(self):
        hren = "Объект класса Critter\n"
        hren += "имя: " + self.name + "\n"
        return hren
    
    def talk(self):
        print(f"Привет. Я зверюшка - экземпляр класс Critter, меня зовут {self.name}\n")
        print(f'Я чувствую себя {self.__mood} ')




#main
print("Нахожу значение атрибута класса Critter.total: ")
print(Critter.total)
#Создание зверюшек
crit1 = Critter("Шапочка", mood = "офигенно")
print(crit1._Critter__mood)#Никогда не выполняйте прямой доступ к закрытым атрибутам и методам извне кода класса, в кото­ром они объявлены.
crit1.talk()
crit1.public_method()
crit2 = Critter("Хрен","хреново")
crit2.talk()
crit3 = Critter("Классово верная зверюшка","попрёт для сельской местности")
crit3.talk()


Critter.status()
print("Обращаюсь к атрибуту класса Critter.total: ")
print(crit1.total)


#print("Вывод обьекта crit1 на экран: ")
#print(crit1)
#print("Вывод обьекта crit2 на экран: ")
#print(crit2)
#print("Непосредственный доступ к атрибуту crit1.name: ")
#print(crit1.name)
#print("Непосредственный доступ к атрибуту crit2.name: ")
#print(crit2.name)










