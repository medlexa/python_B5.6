import random

def newpole():
    p = []
    for a in range(4):
        d = []
        if(a == 0):
            d.append("")
            d.append("1")
            d.append("2")
            d.append("3")
        else:
            d.append(str(a))
            for s in range(3):
                d.append("")
        
        # for b in range(4):
            
        p.append(d)

    return p

p = newpole()

# print(newpole())
def prov(p,text):
    #проверка по горизонтали
    for a in range(3):
        # print(f"{p[1][a + 1]} + {p[2][a + 1]} + {p[3][a + 1]}")
        if(p[1][a + 1] == text and p[2][a + 1] == text and p[3][a + 1] == text):
            return text
    #проверка по горизонтали
    for a in range(3):
        # print (f"{p[a + 1][1]} - { p[a + 1][2]} - {p[a + 1][3]}")
        if(p[a + 1][1] == text and p[a + 1][2] == text and p[a + 1][3] == text):
            return text
    #проверка диагонали 1
    if(p[1][1] == text and p[2][2] == text and p[3][3] == text):
        return text
    #проверка диагонали 2
    if(p[1][3] == text and p[2][2] == text and p[3][1] == text):
        return text
    
def hodnul(p):
    j = 9
    while(j>1):
        i = random.randint(1,3)
        k = random.randint(1,3)
        # print (i)
        if(p[i][k] != "X" and p[i][k] != "0"):
            p[i][k] = "0"
            return True
           
        j-=1
    return False

def proverkapol(p):
    k = prov(p,"X")
    # print (f"k = {k}")
    if(k != None):
        print(f"Выйграл {k}")
        print_pole(p)
        print("-------------")
        return False
    else:
        return True
    
    
    
#функция печати поля
def print_pole(p):
    for a in p:
        print(a)
#проверка того что ввел пользователь, возвращаем две переменные
def proverka(a):
    x = 0
    y = 0
    try:
        zn = a.split(" ",2)
        if(len(zn) == 2):
            if(int(zn[0]) > 0 and int(zn[0]) < 4 and int(zn[1]) > 0 and int(zn[1]) < 4):
                return int(zn[0]), int(zn[1])
            else:
                print("Значения должны быть в диапозоне от 1 до 3")
                return x, y
        else:   
            print("Необходимо ввести только 2 числа разделенные пробелом")
            return x,y
       
    except:
        print("Введены некоректные данные! Повторите попытку")
        
    return x,y

print_pole(p)

game = True

while(game):
    x = 0
    y = 0
    while(x == 0):
        x,y = proverka(input("Введите значения своего хода через пробел (ряд столб)"))

    vigre = False

    if(x != 0 and y != 0):
        vigre = True
 
    if(vigre):
        if(p[x][y] == ""):
            p[x][y] = "X"
            nex = proverkapol(p)
            if(nex):
                if(hodnul(p)):
                    print_pole(p)
                    k = prov(p,"X")
                    # print (f"k = {k}")
                    if(k != None):
                        print(f"Выйграл {k}")
                        p = newpole()
                        print_pole(p)
                    k = prov(p,"0")
                    # print (f"k = {k}")
                    if(k != None):
                        print(f"Выйграл {k}")
                        p = newpole()
                        print_pole(p)
                else:
                    print("Ничья")
                    print_pole(p)
                    p = newpole()
                    print_pole(p)
            else:
                p = newpole()
                print_pole(p)
        else:
            print("Данная клетка занята!")
    
    # print("")
    
    
