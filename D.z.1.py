'''задача 1. Напишите программу, которая принимает на вход цифру, 
   обозначающую день недели, и проверяет, 
   является ли этот день выходным'''
   
   
day = int(input('Введите день недели: '))
if day > 7 or day < 1:
    print('Повторите ввод')
elif day == 6 or day == 7:
    print("Это выходной!")
else:
    print("Это не выходной!")
