# Задача 3. Найдите все простые несократимые дроби,
# лежащие между 0 и 1, знаменатель которых не превышает 11.

def simple_fraction(x,y):
    min_number=min(x,y)
    nod = 1
    for el in range(2, min_number + 1):
        if x % el == 0 and y % el == 0:
            nod = el
            break
    return nod == 1

def zadacha3():    
    for y in range(1,12):
        for x in range(1,y):
            if simple_fraction(x,y):
                print(f'{x}/{y}', end=' ')
        print()
zadacha3()    