#Глецевич Карина 49 группа
#лабораторная работа 1, вариант 5

from itertools import product

a = input().strip()  
if len(a)>10:
    print('Количество символов больше 10')
    exit()
    
n = int(input())
if n>10:
    print ('Количество чисел больше 10')
    exit()

for p in product (a, repeat=n):
    print("".join(p)) #объединение строк в одну без пробела
    