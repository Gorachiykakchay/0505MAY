#Задание состоит из двух частей. 
#1 часть – написать программу в соответствии со своим вариантом задания.
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
#Вариант 25. У няни неограниченное количество  фруктов К разных названий (ф1,…фК). Сформировать (вывести) все возможные варианты меню полдника (N фруктов) для ребенка на неделю.


from itertools import product
from random import randint

print('Введите количество разных фруктов K: ', end='')
k = int(input())
if k <= 0:
    print('Фрукты закончились')
    quit()
else:
    print('Введите количество фруктов в одном полднике N: ', end='')
n = int(input())

print('\nПервая часть')
fruits = []
kol = 0

for i in range(1, k + 1):
    fruits.append(f'Фрукт {i}')

for i in product(fruits, repeat=n):
    kol += 1

print('Всего комбинаций:' + str(kol))
print('\nВторая часть')
print('Введите количество дней: ', end='')
days = int(input())
# Создаем пустой словарь меню на каждый день
weekly_menu = {day: {} for day in range(1, days + 1)}

for day in range(1, days + 1):
    print(f'Меню на день {day}:')
    daily_menu = {}
    fruits = []
    for i in range(1, k + 1):
        fruits.append(f'Ф{i}')
    for fruit in fruits:
        calories = randint(1, 100)  # генерируем случайное число для калорийности фрукта
        daily_menu[fruit] = calories

    weekly_menu[day] = daily_menu
    max_calories_fruit = max(daily_menu, key=daily_menu.get)
    weekly_menu[day][f'Самый калорийный фрукт на день {day}'] = daily_menu[max_calories_fruit]
    print(daily_menu)

print(f'Меню на неделю: {weekly_menu}\n')
