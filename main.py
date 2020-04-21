#PY_Lesson_TWO
'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

i = 1
null = 0

while i < 6:
    print(i, null)
    i=i+1

# Или

i = 1
null = 0

while i < 10:
    print (i, null)
    i = i + 1
    if i == 6: break

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

times = 0
n = 0
input_figure = ''

while n <10:
    input_figure = input('Введите число')
    if input_figure == '5':
        times += 1
    n+=1

print ('Число', 5, 'найдено', times, 'раз')

'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
sum = 0

for i in range(1,101):
   sum+=i
print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# Если с ноля начинать, то будет всегда 0.
mult = 0

for i in range(1,11):
   mult*=i
print(mult)

# если начинать с 1

mult = 1

for i in range(1,11):
   mult*=i
print(mult)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
integer_number = input('введите число')
if integer_number.isdigit():
    integer_number = int(integer_number)
    while integer_number>0:
     print(integer_number%10)
     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''
integer_number = 72469854487
sum = 0
while integer_number>0:
    sum+=integer_number%10
    integer_number = integer_number//10
print (sum)

'''
Задача 7
Найти произведение цифр числа.
'''
integer_number = 562
mult = 1
while integer_number>0:
    mult*=integer_number%10
    integer_number = integer_number//10
print (mult)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''

integer_number = 72469854487
while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''

integer_number = 547893146
max_number = 0
while integer_number>0:
    if integer_number%10 > max_number:
        max_number = integer_number%10
    integer_number = integer_number//10
print(max_number)

'''
Задача 10
Найти количество цифр 5 в числе
'''
integer_number= 547893146579
times = 0
while integer_number>0:
    if integer_number%10 ==5:
        times+=1
    integer_number = integer_number//10
print('Цифра', 5, 'найдена', times, 'раз')