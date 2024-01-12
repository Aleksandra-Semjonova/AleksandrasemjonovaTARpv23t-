from math import * #порядок текста неправильный. если короткая то нужно обращаться к модолю, если писать как на строке то ничего длать не надо
print("Ruudu karakteristikud") #одинарные кавычки тоже можно использовать
a=float(input("Sisesta ruudu külje pikkus => ")) #добавить флоат
S=a**2 
print("Ruudu pindala",round (S,2))
P=4*a
print("Ruudu ümbermõõt",round (P,2))
di=a*sqrt(2) #написать правильно sgrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #лишняя скобка
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #добавить флоат
c=float(input("Sisesta ristküliku 2. külje pikkus => "))
S=b*c
print("Ristküliku pindala", S) #изменить кавычки в строке 
P=2*(b+c) #добавить умножение
print("Ristküliku ümbermõõt", P)
di=sqrt(b**2+c**2) #убираем math. потому что на 1 первой строке мы написали math, так же возводим в квадрат 
print("Ristküliku diagonaal", round(di,2)) #добовляем 2 
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #добовляем флоат
d=2*r #добовляем умножение, потому что его всегда нужно писать 
print("Ringi läbimõõt"+ str(d)) 
S=pi*r**2 #убираем скобки, потому это константа, а так же возводим в квардрат
print("Ringi pindala", round (S,2)) #знак в скобки 
C=2*pi*r #так же убираем скобки добовляем умножение 
print("Ringjoone pikkus", round(C,2))
