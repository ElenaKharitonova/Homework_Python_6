# Задача 1. Дано натуральное число N. Найдите значение
# выражения: N + NN + NNN
# N может быть любой длины.

def zadacha1():
    number = input('Введите натуральное число: ')
    print(f'{number} + {number*2} + {number*3} =\
 {int(number)+int(number*2)+int(number*3)}')
zadacha1()