'''
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для отладки использовать не случайное заполнение, а целенаправленное. Вид матрицы А: 
ИСТд-11
В	С	
D	Е	

Для простоты все индексы в подматрицах относительные. 
По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.
Программа должна использовать функции библиотек numpy  и mathplotlib

Вариант 25
    25.	Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество нулей в нечетных столбцах больше, чем произведение чисел, то поменять в местами  С и В симметрично, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A-1*AT – K * F-1, иначе вычисляется выражение (A +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно.
'''

import numpy as np
from math import prod
from copy import deepcopy

import matplotlib.pyplot as plt

K, N = (int(item) for item in input('Press values K and N: ').split()) #Ввод начальных условий
mid = N//2 # Для удобства расчитываем размерность подматриц

A = np.random.randint (-10, 10, (N, N)) #Генерируем матрицу A случайными числами в диапазоне [-10, 10]
print(f'Матрица A:\n{A}')

c1 = 0
c2 = 1
for row in A[mid:,mid::2]: #Вычисляем данные по условию - В Е количество чисел, больших К в четных столбцах
    for item in row:
        if item == 0: c1 += 1  
    c2 *= prod(row)   #Вычисляем данные по условию - В Е в нечетных столбцах произведение чисел
print(f'\nВ Е количество нулей в нечетных столбцах = {c1}')
print(  f'В Е в нечетных столбцах произведение чисел  = {c2}')

F = deepcopy(A) #создаем матрицу F на основе матрицы A
for i in range(mid): #делаем проход по столбцам\строкам
    if c1>c2: #меняем подматрицы B и C симметрично
        F[:mid,i], F[:mid,-1-i] = deepcopy(F[:mid,-1-i]), deepcopy(F[:mid,i]) 
    else: #меняем подматрицы C и E несимметрично
        F[i, mid:], F[mid+i, mid:] = deepcopy(F[mid+i, mid:]), deepcopy(F[i, mid:])
print(f'\nМатрица F:\n{F}')

determinant = np.linalg.det(A) #Вычисляем определитель матрицы A
sum_diag = np.trace(F) #Вычисляем сумму диагональных элементов матрицы F
print(f'\nОпределитель матрицы A                 = {determinant:.2f}')
print(  f'Сумма диагональных элементов матрицы F = {sum_diag}')

np.set_printoptions(precision = 2, suppress=True) #Устанавливаем параметры для вывода матрицы на печать: 2 знака после запятой

if determinant > sum_diag: 
    #A-1*AT – K * F-1
    print(f'Вычисляем выражение: A-1*AT – K * F-1')
    A_inv = np.linalg.inv(A)
    print(f'\nРезультат A-1 :\n{A_inv}')
    A_t = np.transpose(A)
    print(f'\nРезультат At :\n{A_t}')
    res_1 = np.dot(A_inv, A_t)
    print(f'\nРезультат A-1 * At :\n{res_1}')
    F_inv = np.linalg.inv(F)
    print(f'\nРезультат F-1 :\n{F_inv}')
    print(f'\nРезультат K*F-1 :\n{K*F_inv}')
    print(f'\nРезультат A-1*At - K*F-1 :\n{res_1 - K*F_inv}')
else:
    #(A +G-FТ)*K
    print(f'Вычисляем выражение: (A +GТ-F-1)*K')
    G = np.tril(A)
    print(f'\nМатрица G:\n{G}')
    F_t = np.transpose(F)
    print(f'\nРезультат Ft :\n{F_t}')
    res_1 = A + G - F_t
    print(f'\nРезультат A+G-Ft :\n{res_1}')
    print(f'\nРезультат (A+G-Ft)*K :\n{res_1*K}')

#Для матрицы F выводим три графика

fig = plt.figure()

ax_1 = fig.add_subplot(1, 3, 1, projection='3d')
ax_2 = fig.add_subplot(1, 3, 2)
ax_3 = fig.add_subplot(1, 3, 3, projection='3d')

ax_1.set(title = 'ax_1')
ax_2.set(title = 'ax_2')
ax_3.set(title = 'ax_3')

X = np.arange(0, N, 1)
Y = np.arange(0, N, 1)
X, Y = np.meshgrid(X, Y)

ax_1.scatter(X, Y, F)
ax_2.imshow(F)
ax_3.plot_surface(X, Y, F)

plt.show()