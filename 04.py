# "Пора учить английский язык", - сказал себе Степа и решил написать программу для изучения английского языка.
# Программа получает на вход слово на английском языке и несколько его переводов на русском языке.
# Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов.
# В этой задаче нужно использовать строчный метод split().
en_ru = {}
count = int(input("Введите количество слов на английском языке: "))
for i in range(count):
    en = input('Введите слово на англиском языке: ')
    ru = input('Введите перевод на русский язык: ')
    en_ru[en] = ru.split(',')
print(en_ru)

