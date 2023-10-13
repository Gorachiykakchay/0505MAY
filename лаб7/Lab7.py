import random
import itertools


class FruitContainer:
    def __init__(self, num_fruits, num_per_container, days):
        self.num_fruits = num_fruits
        self.num_per_container = num_per_container
        self.days = days
        self.fruits = [f'ф{i}' for i in range(1, num_fruits + 1)] if num_fruits != 0 else []
        self.menu_options = []
        self.generate_menu_options()

    def generate_menu_options(self):
        self.menu_options = list(itertools.combinations(self.fruits, self.num_per_container))

    def print_menu_options(self):
        total_combinations = len(self.menu_options)
        print(f'Всего вариантов меню: {total_combinations}')
        if total_combinations != 0:
            print('Варианты меню:')
            for option in self.menu_options:
                print(' '.join(option))

    def simulate_days(self):
        if self.num_fruits != 0:
            print('--------------------')
            for day in range(self.days):
                calories = {fruit: random.randint(50, 150) for fruit in self.fruits}
                max_calories_fruits = sorted(calories.items(), key=lambda x: x[1], reverse=True)[
                                      :self.num_per_container]
                print(f"\nМеню на день {day + 1}:")
                option = ' '.join(f"{fruit[0]} ({fruit[1]} ккал)" for fruit in max_calories_fruits)
                option_calories = sum(calorie[1] for calorie in max_calories_fruits)
                print(f"{option} ({option_calories} ккал)")
        else:
            print('Нет фруктов для создания меню.')


def main():
    k = int(input('Введите количество разных фруктов K: '))

    if k > 0:
        n = int(input('Введите количество фруктов в одном полднике N: '))
        while n > k:
            print(f"Недостаточно фруктов!")
            n = int(input('Введите количество фруктов в одном полднике N: '))
    else:
        n = 0
        print('Количество фруктов в одном полднике 0')

    days = int(input('Введите количество дней: '))
    container = FruitContainer(k, n, days)
    container.print_menu_options()
    container.simulate_days()


if __name__ == '__main__':
    main()
