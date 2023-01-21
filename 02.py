# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.


friendslist = {}
count = int(input("Введите количество друзей: "))
for i in range(count):
    name = input("Введите имя друга: ")
    age = int(input("Введите возраст друга: "))
    friendslist[name] = age
print(friendslist)

min_value = min(friendslist.values())
for name, am in friendslist.items():
    if am == min_value:
        print(name)