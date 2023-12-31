# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

import random

a = random.randrange(1, 1000)
b = random.randrange(1, 1000)

s = a + b
print(f"Сумма {s}")

p = a * b
print(f"Произведение {p}")

# b^2 - b*s + p = 0
# b^2 = b*s - p
# b = s - p/b
# i == (i*s - p)**0.5

for i in range(s):
    if i == (i*s - p)**0.5:
        print(f"Загадано число {i}")
    
    
