#Задана рекуррентная функция. Область определения функции – натуральные числа. 
#Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
#Определить границы применимости рекурсивного и итерационного подхода. 
#Результаты сравнительного исследования времени вычисления представить в табличной и графической форме. 
#25 вариант F(1) = 4; F(2) = 5; F(w) = 4*F(w-1)- 3*F(w-2) при w > 2.

import sys
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(100000)

# -------------------------Ввод-------------------------

n = input('Введите натуральное число: ')

try:
    n = int(n)
except ValueError:
    sys.exit('Введено не натуральное число, или не число вовсе. Программа завершена.')

if n < 1:
    sys.exit('Введено не натуральное число. Программа завершена.')


# -----------------------Рекурсия------------------------

def recursive_f(number):
    if number == 1:
        return 4
    elif number == 2:
        return 5
    else:
        return 4 * recursive_f(number - 1) - 3 * recursive_f(number - 2)


# ------------------------Итерация------------------------

def iterative_f(number):
    if number == 1:
        return 4
    elif number == 2:
        return 5
    else:
        num1, num2 = 4, 5
        for i in range(3, number + 1):
            current_num = 4 * num2 - 3 * num1
            num1, num2 = num2, current_num
        return current_num


# ---------------------------------------------------------
recursion_time = []
iteration_time = []
num_list = []

for i in range(1, n + 1, 1):
    num_list.append(i)

    # Рекурсия
    start_time = time.time()
    recursive_result = recursive_f(i)
    temp = time.time() - start_time
    print(str(i) + ') Рекурсия: ' + str(recursive_result))
    print('Время: ' + str(temp))
    recursion_time.append(temp)

    # Итерация
    start_time = time.time()
    iterative_result = iterative_f(i)
    temp = time.time() - start_time
    print('Итерация: ' + str(iterative_result))
    print('Время: ' + str(temp))
    iteration_time.append(temp)

plt.plot(num_list, recursion_time, label='Рекурсия'), plt.plot(num_list, iteration_time, label='Итерация')
plt.title("График производительности"), plt.xlabel("Проверяемое число"), plt.ylabel("Время вычислений в секундах")
plt.legend()
plt.show()
