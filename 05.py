from collections import Counter
import random

# игра с конфетами
all_sweets = 50
left_sweets = all_sweets
sweets_play1 = 0
sweets_play2 = 0
sum_sweets = 0

n1 = 0
n2 = 0
while sum_sweets < all_sweets:
    if n1 == n2:
        move_play1 = int(input('первый игрок берет конфеты (не больше 28 шт): '))
        if move_play1 <= 28 and move_play1 <= left_sweets :
            n1 = n1 + 1
            sweets_play1 = sweets_play1 + move_play1
            sum_sweets = sweets_play1 + sweets_play2
            left_sweets = all_sweets - sum_sweets
        elif move_play1 > 28 or move_play1 > left_sweets:
            print('вы взяли слишком много конфет ')
    if n1 > n2 and left_sweets != 0:
        # вариант а
        # move_play2 = int(input('второй игрок берет конфеты (не больше 28 шт): '))
        # вариант б
        move_play2 = random.randint(1, 28)
        if move_play2 <= 28 and move_play2 <= left_sweets:
            n2 = n2 + 1
            sweets_play2 = sweets_play2 + move_play2
            sum_sweets = sweets_play1 + sweets_play2
            left_sweets = all_sweets - sum_sweets
        elif move_play2 > 28 or move_play2 > left_sweets:
            print('вы взяли слишком много конфет ')

    print (sweets_play1, sweets_play2, sum_sweets)

if n1>n2:
    print('выиграл первый игрок со счетом:', sweets_play1)
else:
    print('выиграл второй игрок со счетом:', sweets_play2)
