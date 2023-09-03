# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

def count_min_coin(count_coin):

    count_coin_1 = 0
    count_coin_0 = 0
    min_coin = 0

    for i in range(count_coin):
        coin = random.randrange(1, 9)
        print(coin, end = " ")

        if coin % 2 == 0:
            count_coin_0 += 1
        else:
            count_coin_1 += 1

    if count_coin_0 < count_coin_1:
        min_coin = count_coin_0
    else:
        min_coin = count_coin_1

    print(end = "\n")
    return min_coin




number = int(input("Введите кол-во монет: "))


print(count_min_coin(number))