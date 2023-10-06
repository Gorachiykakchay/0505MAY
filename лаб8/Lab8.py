'''
Задание состоит из двух частей. 
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов и целевую функцию для оптимизации решения.
Вариант 25. У няни неограниченное количество  фруктов К разных названий (ф1,…фК). Сформировать (вывести) все возможные варианты меню полдника (N фруктов) для ребенка на неделю.
'''
import random
import itertools
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

def combination():
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
        results_text.delete(1.0, END)

        fruits = [f'ф{i}' for i in range(1, k + 1)]
        menu_options = []
        for option in itertools.combinations(fruits, n):
            menu_options.append(list(option))

        days = int(days_entry.get())

        for day in range(days):
            daily_menu = menu_options

            calories = {fruit: random.randint(50, 150) for fruit in fruits}
            day_calories = []
            for option in daily_menu:
                option_calories = sum(calories[fruit] for fruit in option)
                day_calories.append((option, option_calories))
            day_calories.sort(key=lambda x: x[1], reverse=True)

            results_text.insert(INSERT, f"\nМеню на день {day + 1}:\n")
            for option, option_calories in day_calories:
                option = ' '.join(f"{fruit} ({calories.get(fruit, 0)} ккал)" for fruit in option)
                results_text.insert(INSERT, f"{option} ({option_calories} ккал)\n")
        results_text.insert(INSERT, '\n')


window = Tk()
window.title("Задание Лабораторной работы №8")
window.geometry('500x100')
lb = Label(window, text='У няни неограниченное количество', font=('Times', 12))
lb.place(relx=0.5, rely=0.15, anchor=CENTER)
lbe = Label(window, text='Сформировать (вывести) все возможные варианты меню полдника', font=('Times', 12))
lbe.place(relx=0.5, rely=0.40, anchor=CENTER)
lbr = Label(window, text=' (N фруктов) для ребенка на неделю.', font=('Times', 12))
lbr.place(relx=0.5, rely=0.65, anchor=CENTER)
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
