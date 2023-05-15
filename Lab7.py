# Объектно-ориентированная реализация

class Nanny:
    def __init__(self, fruits, menu_size, max_repeat):
        self.fruits = fruits
        self.menu_size = menu_size
        self.max_repeat = max_repeat
    
    def generate_menu(self):
        menu = []
        def generate(menu, current_menu):
            if len(current_menu) == self.menu_size:
                menu.append(current_menu)
            else:
                for fruit in self.fruits:
                    if current_menu.count(fruit) < self.max_repeat:
                        generate(menu, current_menu + [fruit])
        generate(menu, [])
        return menu
        
    def calculate_vitamins(self, menu):
        vitamins = {}
        for m in menu:
            total_vitamins = sum(self.get_vitamins(fruit) for fruit in m)
            vitamins[tuple(m)] = total_vitamins
        return vitamins
    
    def get_vitamins(self, fruit):
        # Здесь можно ограничить характеристики фруктов
        vitamins = {
            "яблоко": 10,
            "апельсин": 12,
            "груша": 8,
            "банан": 15,
            "киви": 9,
            "виноград": 17,
            "лимон": 14,
            "авокадо": 25,
            "ананас": 7,
            "гранат": 21,
            "персик": 8
        }
        return vitamins.get(fruit, 0)
    
    def get_best_menu(self):
        menu = self.generate_menu()
        vitamins = self.calculate_vitamins(menu)
        sorted_vitamins = dict(sorted(vitamins.items(), key=lambda x:x[1], reverse=True))
        return sorted_vitamins

# Использование класса
fruits = ["яблоко", "апельсин", "груша", "банан", "киви", "виноград", "лимон", "авокадо", "ананас", "гранат", "персик"]
menu_size = 3
max_repeat = 2

nanny = Nanny(fruits, menu_size, max_repeat)
best_menu = nanny.get_best_menu()

for m in best_menu:
    print(", ".join(m), " | Витамины: ", best_menu[m])
