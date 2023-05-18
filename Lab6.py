#Задание состоит из двух частей. 
#1 часть – написать программу в соответствии со своим вариантом задания.
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
#Вариант 25. У няни неограниченное количество  фруктов К разных названий (ф1,…фК). Сформировать (вывести) все возможные варианты меню полдника (N фруктов) для ребенка на неделю.


from random import choice, randint
from itertools import permutations

print('Введите количество разных фруктов K: ', end='')
k = int(input())
if k <= 0:
    print('Фрукты закончились')
    quit()
else:
    print('Введите количество фруктов в одном полднике N: ', end='')
    n = int(input())

print('\nПервая часть')

fruits = [f'Фрукт {i}' for i in range(1, k+1)]
days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

menu_combinations = list(permutations(fruits, n))
total_combinations = len(menu_combinations)

random_menu = [choice(menu_combinations) for i in range(len(days_of_week))]

menu = []
for i, day in enumerate(days_of_week):
    menu_item = f'{day}: {", ".join(random_menu[i])}'
    menu.append(menu_item)

for item in menu:
    print(item)

print(f"{total_combinations} возможных комбинаций меню")

print('\nВторая часть')
print('Введите количество дней: ', end='')
days = int(input())

#Создаем пустой словарь меню на каждый день

weekly_menu = {}

for day in range(1, days + 1):
    print(f'Меню на день {day}:')
    daily_menu = {}
    fruits = []
    for i in range(1, k + 1):
        fruits.append(f'Ф{i}')
    for fruit in fruits:
        calories = randint(1, 100)  # генерируем случайное число для калорийности фрукта
        daily_menu[fruit] = calories

    max_calories_fruit = max(daily_menu, key=daily_menu.get)

    daily_menu[f'Самый калорийный фрукт на день {day}'] = max_calories_fruit
    weekly_menu[f'День {day}'] = daily_menu

for day, menu in weekly_menu.items():
    print(f'Меню на {day}:')
    for fruit, calories in menu.items():
        if 'Самый калорийный' not in fruit:
            print(f'{fruit}: {calories} ккал')
        else:
            print(fruit + ': ' + menu[fruit])
