'''
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
Вариант 25. У няни неограниченное количество  фруктов К разных названий (ф1,…фК). Сформировать (вывести) все возможные варианты меню полдника (N фруктов) для ребенка на неделю.
'''
import random
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

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
        results_text.insert(END, f'Всего вариантов меню: {total_combinations}\n')
        results_text.insert(END, 'Варианты меню:\n')
        for option in self.menu_options:
            results_text.insert(END, ' '.join(option) + '\n')

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

            results_text.insert(END, f"\nМеню на день {day + 1}:\n")
            for option, option_calories in day_calories:
                option = ' '.join(f"{fruit} ({calories[fruit]} ккал)" for fruit in option)
                results_text.insert(END, f"{option} ({option_calories} ккал)\n")

            results_text.insert(END, f"\nСамый калорийный фрукт на день {day + 1}: {max_calories_fruit[0]} ({max_calories_fruit[1]} ккал)\n")

def combination():
    results_text.delete(1.0, END)
    k = int(fruits_count.get())
    if k <= 0:
        messagebox.showerror("Ошибка", "Фрукты закончились")
        return
    n = int(fruits_per_lunch.get())
    if n <= 0:
        messagebox.showerror("Ошибка", "Некорректное количество фруктов")
    elif n > k:
        messagebox.showerror("Ошибка", f"Недостаточно фруктов. Введите число фруктов не больше {k}")
    else:
        menu_generator = MenuGenerator(k)
        menu_generator.generate_menu_options(n)
        menu_generator.print_menu_options()

        while True:
            try:
                days = int(days_entry.get())
                if days <= 0:
                    messagebox.showerror("Ошибка", "Некорректное количество дней")
                else:
                    break
            except ValueError:
                messagebox.showerror("Ошибка", "Введите число дней")

        menu_analyzer = MenuAnalyzer(menu_generator.fruits, menu_generator.menu_options)
        menu_analyzer.analyze_menu(days)
def click():
    window.destroy()

window = Tk()
window.title("Задание <<Лабораторной работы №8>>")
window.geometry('500x200')
lb = Label(window, text='У няни неограниченное количество', font=('Times', 12))
lb.place(relx=0.5, rely=0.15, anchor=CENTER)
lbe = Label(window, text='Сформировать (вывести) все возможные варианты меню полдника', font=('Times', 12))
lbe.place(relx=0.5, rely=0.40, anchor=CENTER)
lbr = Label(window, text=' (N фруктов) для ребенка на неделю.', font=('Times', 12))
lbr.place(relx=0.5, rely=0.65, anchor=CENTER)
exit_button = Button(window, text="Exit", command=click)
exit_button.place(relx=0.5, rely=0.85, anchor=CENTER)

window.mainloop()

window = Tk()
window.title('Лабораторная работа №8')
window.geometry('1000x750')

lbl = Label(window, text='Введите количество доступных фруктов', font=('Times', 12))
lbl.place(relx=0.5, rely=0.05, anchor=CENTER)

fruits_count = StringVar()
txt = Entry(window, textvariable=fruits_count, width=10)
txt.place(relx=0.5, rely=0.1, anchor=CENTER)

lbl2 = Label(window, text='Введите количество фруктов в одном полднике', font=('Times', 12))
lbl2.place(relx=0.5, rely=0.15, anchor=CENTER)

fruits_per_lunch = StringVar()
txt2 = Entry(window, textvariable=fruits_per_lunch, width=10)
txt2.place(relx=0.5, rely=0.2, anchor=CENTER)

lbl3 = Label(window, text='Введите количество дней', font=('Times', 12))
lbl3.place(relx=0.5, rely=0.25, anchor=CENTER)

days_entry = Entry(window, width=10)
days_entry.place(relx=0.5, rely=0.3, anchor=CENTER)

btn = Button(window, text='Сгенерировать комбинации', command=combination)
btn.place(relx=0.5, rely=0.35, anchor=CENTER)

results_text = scrolledtext.ScrolledText(window, width=100, height=20)
results_text.bind('<Key>', lambda e: 'break')  # Разрешает только чтение
results_text.place(relx=0.5, rely=0.6, anchor=CENTER)

window.mainloop()
