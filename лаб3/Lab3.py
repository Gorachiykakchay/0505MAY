'''
Задание на матрицы №1
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.
Вариант 25
Формируется матрица F следующим образом: если в Е количество нулей в нечетных столбцах в области 1 больше, чем произведение чисел по периметру области 2, то поменять в В симметрично области 1 и 3 местами, иначе С и Е поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: ((К*A T)*(F+А)-K* F T . Выводятся по мере формирования А, F и все матричные операции последовательно.
Матрица:
B C
D E
Вид матрицы:
  2  
1   3
  4 
Диагональные элементы включены в область
'''


from random import randint

# Ввод размерности матрицы и числа K с клавиатуры
print('Введите N:', end=' ')
n = int(input())
print('Введите K:', end=' ')
k = int(input())

# Заполнение и вывод исходной матрицы F
F = [[randint(-10, 10) for _ in range(n)] for _ in range(n)]
print('\nОсновная матрица')
for row in F:
    print(' '.join(f"{num:4d}" for num in row))
print()

# Создание матриц A, Proizv, AKT, Ftrans и Sum
A = F.copy()
Proizv = [[0] * n for _ in range(n)]
AKT = [[0] * n for _ in range(n)]
Ftrans = [[0] * n for _ in range(n)]
Sum = [[0] * n for _ in range(n)]

# Подсчет произведения чисел по периметру в зависимости от размерности матрицы
kol = 0
proiz = 1
if n % 4 != 0:
    for i in range(n // 2 + 1, n // 4 + n // 2 + 2):
        for j in range(n // 2 + 1, n // 4 + n // 2 + 2):
            if i <= j and j % 2 == 0 and F[i][j] > k and F[i][n//2 - j] > k:
                kol += 1

    for i in range(n // 4 + n // 2, n):
        for j in range(n // 4 + n // 2, n):
            if i >= j and j != n // 4 + n - i - 1:
                proiz *= F[i][j] * F[i][n // 4 - j]

elif n % 4 == 0:
    for i in range(n // 2, n // 4 + n // 2):
        for j in range(n // 2, n // 4 + n // 2):
            if i <= j and j % 2 == 0 and F[i][j] > k and F[i][n // 2 - 1 - j] > k:
                kol += 1
    for i in range(n // 4 + n // 2, n):
        for j in range(n // 4 + n // 2, n):
            if i >= j and j != n // 4 - 1 + n - i:
                proiz *= F[i][j] * F[i][n // 4 + 1 - j]

# Преобразование матрицы F
if kol > proiz:
    for i in range(n // 2):
        for j in range(n // 2 + 1, n):
            if i >= j - n // 2 - 1:
                F[i][j], F[n - j - 1][n - i - 1] = F[n - j - 1][n - i - 1], F[i][j]
else:
    for i in range(n // 2):
        for j in range(n // 2):
            F[i][j], F[i][j + n // 2] = F[i][j + n // 2], F[i][j]

# Вывод полученной матрицы F
print('\nПреобразованная матрица:')
for row in F:
    print(' '.join(f"{num:4d}" for num in row))
print()

# Перемножение матриц A и F
print('A*F')
for i in range(n):
    for j in range(n):
        for k in range(n):
            Proizv[i][j] += A[i][k] * F[k][j]
        print(f"{Proizv[i][j]:4d}", end="")
    print()

# Умножение полученной матрицы на K
print(f"\nK*(A*F)")
for i in range(n):
    for j in range(n):
        AKT[i][j] = k * Proizv[i][j]
        print(f"{AKT[i][j]:4d}", end="")
    print()

# Транспонирование матрицы F и умножение полученной матрицы на K
print(f"\nK * F транспонированная")
for j in range(n):
    for i in range(n):
        Ftrans[i][j] = k * F[j][i]
        print(f"{Ftrans[i][j]:4d}", end="")
    print()

# Суммирование матриц AKT и Ftrans
print(f"\nК*(A*F) + K * F транспонированная")
for i in range(n):
    for j in range(n):
        Sum[i][j] = AKT[i][j] + Ftrans[i][j]
        print(f"{Sum[i][j]:4d}", end="")
    print()
    
