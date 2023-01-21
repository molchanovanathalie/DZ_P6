# Пользователь вводит число N.
# Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Выведите средний возраст всех друзей и самое длинное имя

friendslist = {}
count = int(input("Введите количество друзей: "))
ages = 0
len_name = 0
max_name = " "
for i in range(count):
    name = input("Введите имя друга: ")
    if len_name < len(name):
        len_name = len(name)
        max_name = name
    age = int(input("Введите возраст друга: "))
    friendslist[name] = age
    ages = ages + age

print(friendslist)
avage = ages/count
print("Средний возраст: ", int(avage))
print("Самое длинное имя: ", max_name)
