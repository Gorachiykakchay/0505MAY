'''
Задана рекуррентная функция. Область определения функции – натуральные числа. 
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода. 
Результаты сравнительного исследования времени вычисления представить в табличной и графической форме. 
25 вариант F(1) = 4; F(2) = 5; F(w) = 4*F(w-1)- 3*F(w-2) при w > 2.
'''
import sys
import time
import matplotlib.pyplot as plt

sys.setrecursionlimit(100000)

#Ввод

n = input('Введите натуральное число: ')

try:
    n = int(n)
except ValueError:
    sys.exit('Введено не натуральное число, или не число вовсе. Программа завершена.')

if n < 1:
    sys.exit('Введено не натуральное число. Программа завершена.')

# Рекурсия

def recursive_f(number):
    if number == 1:
        return 4
    elif number == 2:
        return 5
    else:
        return 4 * recursive_f(number - 1) - 3 * recursive_f(number - 2)


# Итерация

def iterative_f(number):
    if number == 1:
        return 4
    elif number == 2:
        return 5
    else:
        a, b = 4, 5
        for i in range(3, number + 1):
            c = 4 * b - 3 * a
            a, b = b, c
        return c

# ---------------------------------------------------------

recursion_time = []
iteration_time = []
num_list = []
max_recursion_number = 30    # На больших числах рекурсия будет работать очень медленно

for i in range(1, n + 1):
    num_list.append(i)
    if i <= max_recursion_number:
        start_time = time.perf_counter()
        print(str(i) + ') \nРекурсия: ' + str(recursive_f(i)))

        temp = time.perf_counter() - start_time
        recursion_time.append(temp)
        print('Время: ' + str(temp))
    else:
        recursion_time.append(0)

    start_time = time.perf_counter()
    print('Итерация: ' + str(iterative_f(i)))

    temp = time.perf_counter() - start_time
    print('Время: ' + str(temp))
    iteration_time.append(temp)

answer = [recursion_time]
plt.plot(num_list, recursion_time, label='Рекурсия'), plt.plot(num_list, iteration_time, label='Итерация')
plt.title("График производительности"), plt.xlabel("Проверяемое число"), plt.ylabel("Время вычислений в секундах")
plt.legend()
plt.show()

print(f'\nРекурсивный подход работает быстрее, чем итеративный, для чисел не больше {max_recursion_number}.\n')
