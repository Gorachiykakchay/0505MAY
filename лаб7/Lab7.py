import random


class FruitContainer:
    def __init__(self, num_fruits, num_per_container, days):
        self.num_fruits = num_fruits
        self.num_per_container = num_per_container
        self.days = days
        self.fruits = [f'ф{i}' for i in range(1, num_fruits + 1)]
        self.menu_options = []
        self.generate_menu_options()

    def generate_menu_options(self):
        for i in range(self.num_fruits ** self.num_per_container):
            option = []
            for j in range(self.num_per_container):
                index = (i // self.num_fruits ** j) % self.num_fruits
                option.append(self.fruits[index])
            if len(set(option)) == self.num_per_container:
                self.menu_options.append(option)

    def print_menu_options(self):
        total_combinations = len(self.menu_options)
        print(f'Всего вариантов меню: {total_combinations}')
        print('Варианты меню:')
        for option in self.menu_options:
            print(' '.join(option))

    def simulate_days(self):
        print('--------------------')
        for day in range(self.days):
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


def main():
    k = int(input('Введите количество разных фруктов K: '))
    while True:
        n = int(input('Введите количество фруктов в одном полднике N: '))
        if n <= 0:
            print('Некорректное количество фруктов')
        elif n > k:
            print(f"Недостаточно фруктов. Введите число фруктов не больше {k}")
        else:
            break

    days = int(input('Введите количество дней: '))

    container = FruitContainer(k, n, days)
    container.print_menu_options()
    container.simulate_days()


if __name__ == '__main__':
    main()
