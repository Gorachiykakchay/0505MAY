'''
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для отладки использовать не случайное заполнение, а целенаправленное. Вид матрицы А: 
ИСТд-11
В	С	
D	Е	

Для простоты все индексы в подматрицах относительные. 
По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.
Программа должна использовать функции библиотек numpy  и mathplotlib
25.	Формируется матрица F следующим образом: скопировать в нее А и  если в Е количество нулей в нечетных столбцах больше, чем произведение чисел, то поменять в местами  С и В симметрично, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A-1*AT – K * F-1, иначе вычисляется выражение (A +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно.
'''

import numpy as np
import matplotlib.pyplot as plt

K, N = (int(item) for item in input('Press values K and N: ').split())
mid = N//2

# Генерация матрицы A со случайными целыми числами от -10 до 10
A = np.random.randint (-10, 10, (N, N))
print(f'Матрица A:\n{A}')

# Подсчет количества нулей в нечетных столбцах и произведения чисел в четных столбцах, начиная со средней строки
c1 = 0
c2 = 1
for i in range(mid, N):
    for j in range(mid, N, 2):
        item = A[i][j]
        if item == 0:
            c1 += 1
        if j == mid:
            continue
        c2 *= item
print(f'\nВ Е количество нулей в нечетных столбцах = {c1}')
print(  f'В Е в нечетных столбцах произведение чисел  = {c2}')

# Создание матрицы F на основе матрицы A
F = A.copy()
for i in range(mid):
    if c1 > c2:
        for j in range(mid):
            F[i][j], F[i][-1-j], F[-1-i][j], F[-1-i][-1-j] = F[-1-i][-1-j], F[-1-i][j], F[i][-1-j], F[i][j]
    else:
        for j in range(mid, N):
            F[i][j], F[mid+i][j] = F[mid+i][j], F[i][j]
print(f'\nМатрица F:\n{F}')

# Вычисление определителя матрицы A и суммы диагональных элементов матрицы F
determinant = 0
for j in range(N):
    determinant += (-1)**j * A[0][j] * np.linalg.det(np.delete(np.delete(A, 0, axis=0), j, axis=1)) if N > 1 else A[0][0]
sum_diag = 0
for i in range(N):
    sum_diag += F[i][i]

print(f'\nОпределитель матрицы A                 = {determinant:.2f}')
print(  f'Сумма диагональных элементов матрицы F = {sum_diag}')

np.set_printoptions(precision = 2, suppress=True)

if determinant > sum_diag:
    A_inv = np.linalg.inv(A)
    A_t = A.T
    F_inv = np.linalg.inv(F)
    print(f'Вычисляем выражение: A-1*AT – K * F-1')
    print(f'\nРезультат A-1 :\n{A_inv}')
    print(f'\nРезультат At :\n{A_t}')
    res_1 = np.dot(A_inv, A_t)
    print(f'\nРезультат A-1 * At :\n{res_1}')
    KF_inv = K * F_inv
    print(f'\nРезультат K*F-1 :\n{KF_inv}')
    res_2 = res_1 - KF_inv
    print(f'\nРезультат A-1*At - K*F-1 :\n{res_2}')
else:
    G = np.tril(A)
    F_t = F.T
    res_1 = A + G - F_t
    print(f'Вычисляем выражение: (A +GТ-F-1)*K')
    print(f'\nМатрица G:\n{G}')
    print(f'\nРезультат Ft :\n{F_t}')
    res_2 = res_1 * K
    print(f'\nРезультат A+G-Ft :\n{res_1}')
    print(f'\nРезультат (A+G-Ft)*K :\n{res_2}')

# Построение матрицы F в 3-х различных формах
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
