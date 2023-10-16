import random

class MenuGenerator:
    def __init__(self, k):
        self.k = k
        self.fruits = [f'ф{i}' for i in range(1, k + 1)]
        self.menu_options = []

    def generate_menu_options(self, n):
        for i in range(self.k ** n):
            option = []
            for j in range(n):
                index = (i // (self.k ** j)) % self.k
                option.append(self.fruits[index])
            if len(set(option)) == n:
                self.menu_options.append(option)

    def print_menu_options(self):
        total_combinations = len(self.menu_options)
        print(f'Всего вариантов меню: {total_combinations}')
        print('Варианты меню:')
        for option in self.menu_options:
            print(' '.join(option))

class MenuAnalyzer:
    def __init__(self, fruits, menu_options):
        self.fruits = fruits
        self.menu_options = menu_options

    def analyze_menu(self, days):
        for day in range(days):
            calories = {fruit: random.randint(50, 150) for fruit in self.fruits}
            day_calories = []
            for option in self.menu_options:
                option_calories = sum(calories[fruit] for fruit in option)
                day_calories.append((option, option_calories))
            day_calories.sort(key=lambda x: x[1], reverse=True)
            max_calories_fruit = max(calories.items(), key=lambda x: x[1])

            print(f"\nМеню на день {day + 1}:")
            for option, option_calories in day_calories:
                option = ' '.join(f"{fruit} ({calories[fruit]} ккал)" for fruit in option)
                print(f"{option} ({option_calories} ккал)")

            print(f"\nСамый калорийный фрукт на день {day + 1}: {max_calories_fruit[0]} ({max_calories_fruit[1]} ккал)")

if __name__ == '__main__':
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

    menu_generator = MenuGenerator(k)
    menu_generator.generate_menu_options(n)
    menu_generator.print_menu_options()

    while True:
        days = int(input('Введите количество дней: '))
        if days <= 0:
            print('Некорректное количество дней')
        else:
            break

    menu_analyzer = MenuAnalyzer(menu_generator.fruits, menu_generator.menu_options)
    menu_analyzer.analyze_menu(days)
