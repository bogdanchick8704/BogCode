
def read():
    файл=open("pituhon.txt","r+",encoding='utf-8')
    print(файл.readline())
    файл.close

def write(Строчка):
    файл=open("pituhon.txt","w+",encoding='utf-8')
    файл.write(Строчка)
    файл.close
    return  Строчка
    


Строчка=input("Введите строчку которую хотите записать: ")


write(Строчка)
read()

print(write(Строчка))
