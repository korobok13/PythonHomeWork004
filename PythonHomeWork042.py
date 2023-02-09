# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
# различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, находясь перед некоторым 
# кустом заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

from random import randint
n = int(input('Введите количество кустов: '))
list_1 = []
i = 0
for i in range(n):
    list_1.append(randint(1, n))
i = 1
list_max = 0
for i in range(len(list_1) - 1):
    list_sum = list_1[i] + list_1[i - 1] + list_1[i + 1]
    if list_sum > list_max:
        list_max = list_sum
        i += 1
print(f'{n} -> {list_1}')
print(list_max)

