#Задание состоит из двух частей. 
#1 часть – написать программу в соответствии со своим вариантом задания.
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
#Вариант 25. У няни неограниченное количество  фруктов К разных названий (ф1,…фК). Сформировать (вывести) все возможные варианты меню полдника (N фруктов) для ребенка на неделю.


#1 часть:
K = int(input("Введите количество разных фруктов: "))
fruits = []
for i in range(K):
    fruit = input("Введите название фрукта: ")
    fruits.append(fruit)

N = int(input("Введите количество фруктов в полдниковом меню: "))

menu = []

def generate_menu(menu, current_menu):
    if len(current_menu) == N:
        menu.append(current_menu)
    else:
        for fruit in fruits:
            if current_menu.count(fruit) <= 1:
                generate_menu(menu, current_menu + [fruit])

generate_menu(menu, [])

for m in menu:
    print(", ".join(m))


#2 часть:
K = int(input("Введите количество разных фруктов: "))
fruits = []
for i in range(K):
    fruit = input("Введите название фрукта: ")
    fruits.append(fruit)

N = int(input("Введите количество фруктов в полдниковом меню (не более 5): "))

max_repeat = int(input("Введите максимальное количество повторений одного и того же фрукта в меню (не более 2): "))

menu = []

def generate_menu(menu, current_menu):
    if len(current_menu) == N:
        menu.append(current_menu)
    else:
        for fruit in fruits:
            if current_menu.count(fruit) < max_repeat:
                generate_menu(menu, current_menu + [fruit])

generate_menu(menu, [])

max_vitamins = {}

for m in menu:
    vitamins = 0
    for fruit in m:
        if fruit == "яблоко":
            vitamins += 10
        elif fruit == "апельсин":
            vitamins += 12
        elif fruit == "груша":
            vitamins += 8
        elif fruit == "банан":
            vitamins += 15
        elif fruit == "киви":
            vitamins += 9
        elif fruit == "виноград":
            vitamins += 17
        elif fruit == "лимон":
            vitamins += 14
        elif fruit == "авокадо":
            vitamins += 25
        elif fruit == "ананас":
            vitamins += 7
        elif fruit == "гранат":
            vitamins += 21
        elif fruit == "персик":
            vitamins += 8
    max_vitamins[tuple(m)] = vitamins

max_vitamins = dict(sorted(max_vitamins.items(), key=lambda x:x[1], reverse=True))

for m in max_vitamins:
    print(", ".join(m), " | Витамины: ", max_vitamins[m])
