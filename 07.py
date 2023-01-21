# Создайте список из случайных чисел. Найдите количество различных элементов в нем.
import random

mylist = []
for n in range(0, 100):
    x = random.randint(0, 100)
    mylist.append(x)
mylist_set = set(mylist)
print(mylist)
print(mylist_set)
print(len(mylist_set))
