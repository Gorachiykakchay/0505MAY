'''
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
Вариант 25. У няни неограниченное количество  фруктов К разных названий (ф1,…фК). Сформировать (вывести) все возможные варианты меню полдника (N фруктов) для ребенка на неделю.
'''
import random
from itertools import product
from random import randint

print('Введите количество разных фруктов K: ', end='')
k = int(input())
if k <= 0:
    print('Фрукты закончились')
    quit()

while True:
    n = int(input('Введите количество фруктов в одном полднике N: '))
    if n <= 0:
        print('Некорректное количество фруктов')
    elif n > k:
        print(f"Недостаточно фруктов. Введите число фруктов не больше {k}")
    else:
        break

print('\nЧАСТЬ 1')
print('--------------------')
fruits = [f'ф{i}' for i in range(1, k + 1)]
menu_options = list(product(fruits, repeat=n))
total_combinations = len(menu_options)
print(f'Всего вариантов меню: {total_combinations}')
print('Варианты меню:')
for option in menu_options:
    print(' '.join(option))

while True:
    days = int(input('Введите количество дней: '))
    if days <= 0:
        print('Некорректное количество дней')
    else:
        break
        
print('\nЧАСТЬ 2')
print('--------------------')

for day in range(days):
    calories = {fruit: randint(50, 150) for fruit in fruits}
    day_combinations = menu_options[:]
    
    for i, option in enumerate(day_combinations):
        random_order = list(range(n))
        random.shuffle(random_order)
        option = [option[j] for j in random_order]
        option_calories = sum(calories[fruit] for fruit in option)
        day_combinations[i] = (option, option_calories)
    
    day_combinations = sorted(day_combinations, key=lambda x:x[1], reverse=True)
    max_calories_fruit = max(calories.items(), key=lambda x: x[1])
    
    print(f"\nМеню на день {day + 1}:")
    for option, option_calories in day_combinations:
        option = ' '.join(f"{fruit} ({calories[fruit]} ккал)" for fruit in option)
        print(f"{option} ({option_calories} ккал)")
    
    print(f"\nСамый калорийный фрукт на день {day + 1}: {max_calories_fruit[0]} ({max_calories_fruit[1]} ккал)")
