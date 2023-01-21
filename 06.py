from collections import Counter
import random

# игра крестики нолики

x = [
    [' ','1', '2', '3'],
    ['_','_', '_', '_'],
    ['a',' ', ' ', ' '],
    ['b',' ', ' ', ' '],
    ['c',' ', ' ', ' '],
    ['_','_', '_', '_'],
]

for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j], end=' | ')
    print()

print('первый игрок ставит 0, второй - x')

n = 0
while n<9:
    y = 0
    z = 0
    if n%2==0:
        elem_1 = str(input('первый игрок введите горизонтальную координату от 1 до 3: '))
        elem_2 = str(input('первый игрок введите вертикальную координату от a до c: '))
    else:
        elem_1 = str(input('второй игрок введите горизонтальную координату от 1 до 3: '))
        elem_2 = str(input('второйигрок введите вертикальную координату от a до c: '))
    if (elem_1 != '1' and elem_1 != '2' and elem_1 != '3') or   (elem_2 != 'a' and   elem_2 != 'b'  and  elem_2 != 'c'):
        print ('введены неправильные координаты')
    else:
        for i in range(len(x)):
            for j in range(len(x[i])):
                print(x[i][j], end=' | ')
                if n%2==0:
                    Xor0 = '0'
                else: Xor0 = 'x'

                if elem_1 == '1' and elem_2 == 'a':
                    x[2][1] = Xor0
                elif elem_1 == '2' and elem_2 == 'a':
                    x[2][2] = Xor0
                elif elem_1 == '3' and elem_2 == 'a':
                    x[2][3] = Xor0
                elif elem_1 == '1' and elem_2 == 'b':
                    x[3][1] = Xor0
                elif elem_1 == '2' and elem_2 == 'b':
                    x[3][2] = Xor0
                elif elem_1 == '3' and elem_2 == 'b':
                    x[3][3] = Xor0
                elif elem_1 == '1' and elem_2 == 'c':
                    x[4][1] = Xor0
                elif elem_1 == '2' and elem_2 == 'c':
                    x[4][2] = Xor0
                elif elem_1 == '3' and elem_2 == 'c':
                    x[4][3] = Xor0

                if (x[2][1] == 'x' and x[2][2] == 'x' and x[2][3] == 'x') or \
                   (x[3][1] == 'x' and x[3][2] == 'x' and x[3][3] == 'x') or \
                   (x[4][1] == 'x' and x[4][2] == 'x' and x[4][3] == 'x') or \
                   (x[2][1] == 'x' and x[3][1] == 'x' and x[4][1] == 'x') or \
                   (x[2][2] == 'x' and x[3][2] == 'x' and x[4][2] == 'x') or \
                   (x[2][3] == 'x' and x[3][3] == 'x' and x[4][3] == 'x') or \
                   (x[2][1] == 'x' and x[3][2] == 'x' and x[4][3] == 'x') or \
                   (x[4][1] == 'x' and x[3][2] == 'x' and x[2][3] == 'x'):
                    y = y + 1

                elif (x[2][1] == '0' and x[2][2] == '0' and x[2][3] == '0') or \
                     (x[3][1] == '0' and x[3][2] == '0' and x[3][3] == '0') or \
                     (x[4][1] == '0' and x[4][2] == '0' and x[4][3] == '0') or \
                     (x[2][1] == '0' and x[3][1] == '0' and x[4][1] == '0') or \
                     (x[2][2] == '0' and x[3][2] == '0' and x[4][2] == '0') or \
                     (x[2][3] == '0' and x[3][3] == '0' and x[4][3] == '0') or \
                     (x[2][1] == '0' and x[3][2] == '0' and x[4][3] == '0') or \
                     (x[4][1] == '0' and x[3][2] == '0' and x[2][3] == '0'):
                    z = z + 1


            print()
        n = n+1
    if y != 0:
        print('выиграл второй игрок')
        n = 10
    if z != 0:
        print('выиграл первый игрок')
        n = 10

print('игра окончена')