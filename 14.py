# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.

n = int(input("введите число N: "))

sqr = 2
i = 2
while n >= sqr:
    print(sqr)
    sqr = 2**i
    i += 1
    
