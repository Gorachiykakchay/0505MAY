
from random import choice, randint
from itertools import permutations


class MenuGenerator:
    def __init__(self, k, n):
        self.k = k
        self.n = n
        self.fruits = [f'Фрукт {i}' for i in range(1, k+1)]
        self.days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    
    def generate_menu(self):
        menu_combinations = list(permutations(self.fruits, self.n))
        random_menu = [choice(menu_combinations) for i in range(len(self.days_of_week))]
        menu = []
        for i, day in enumerate(self.days_of_week):
            daily_menu = {}
            for fruit in random_menu[i]:
                calories = randint(1, 100)
                daily_menu[fruit] = calories
            max_calories_fruit = max(daily_menu, key=daily_menu.get)
            daily_menu[f'Самый калорийный фрукт на день {day} ({max_calories_fruit}, {daily_menu[max_calories_fruit]})'] = ""
            menu_item = f'{day}: {", ".join([f"{fruit} ({calories} ккал)" for fruit, calories in daily_menu.items()])})'
            menu.append(menu_item)
        return menu

    def total_combinations(self):
        menu_combinations = list(permutations(self.fruits, self.n))
        return len(menu_combinations)


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

print('\nПервая часть')

menu_generator = MenuGenerator(k, n)
random_menu = [choice(list(permutations(menu_generator.fruits, menu_generator.n))) for i in range(len(menu_generator.days_of_week))]
menu = []
for i, day in enumerate(menu_generator.days_of_week):
    menu_item = f'{day}: {", ".join(random_menu[i])}'
    menu.append(menu_item)

for item in menu:
    print(item)

print(f"{menu_generator.total_combinations()} возможных комбинаций меню")

print('\nВторая часть')

menu = menu_generator.generate_menu()
for item in menu:
    print(item)

print(f"{menu_generator.total_combinations()} возможных комбинаций меню")
