from tkinter import *
import os
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
class CheckersBoard:
    def __init__(self, master):
        self.master = master
        self.master.title("Шашки")
        self.master.resizable(False, False)  # Запрет изменения размеров окна
        self.center_window()  # Центрирование окна
        self.canvas = Canvas(self.master, width=800, height=600)  # Инициализация canvas
        self.canvas.pack()
        self.users = {}

        global black_queen, white_queen, black_checker, white_checker
        black_checker = ImageTk.PhotoImage((Image.open('image/black-regular.png')).resize((50, 50), Image.Resampling.LANCZOS))
        black_queen = ImageTk.PhotoImage((Image.open('image/black-queen.png')).resize((50, 50), Image.Resampling.LANCZOS))
        white_checker = ImageTk.PhotoImage((Image.open('image/white-regular.png')).resize((50, 50), Image.Resampling.LANCZOS))
        white_queen = ImageTk.PhotoImage((Image.open('image/white-queen.png')).resize((50, 50), Image.Resampling.LANCZOS))

        global vzyat, correct
        vzyat = False
        correct = False
        self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                      [1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0],
                      [2, 2, 2, 2, 2, 2, 2, 2],
                      [2, 2, 2, 2, 2, 2, 2, 2],
                      [0, 0, 0, 0, 0, 0, 0, 0]]

        self.current_player = [1, 3]
        self.selected_piece = None
        self.selected_rectangle = None
        self.need_attack = False

        self.label = Label(text="Вход в аккаунт", font="Arial 22 bold")
        self.label_login = Label(text="Логин", font="Arial 15")
        self.label_password = Label(text="Пароль", font="Arial 15")
        self.entry_login = Entry(width=30, justify="center")
        self.entry_password = Entry(width=30, justify="center")
        self.button_auth = Button(text="Авторизироваться", command=lambda: self.authorization())
        self.button_reg = Button(text="Зарегистрироваться", command=lambda: self.registrate())
        self.button_back = Button(text="Выход", command=lambda: self.authorization())

        self.label.place(x=150, y=10)
        self.label_login.place(x=230, y=55)
        self.entry_login.place(x=170, y=85)
        self.label_password.place(x=230, y=105)
        self.entry_password.place(x=170, y=135)
        self.button_auth.place(x=170, y=165, width=180)
        self.button_reg.place(x=170, y=195, width=180)

    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        window_width = 500
        window_height = 500

        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")
    def password_code(self, password):
        key = 2
        coded_password = ""
        for i in password:
            coded_password_temp = chr(ord(i) + key)
            coded_password += coded_password_temp
            key = -key + 1
        return coded_password

    def open_file(self):
        try:
            text = open("users_checker_file.txt", "r+")
            return text
        except FileNotFoundError:
            try:
                text = open("users_checker_file.txt", "w")
                text.close()
                text = open("users_checker_file.txt", "r+")
                return text
            except FileNotFoundError:
                text = open("users_checker_file.txt", "r+")
                return text

    def authorization(self):
        login = self.entry_login.get()
        password_raw = self.entry_password.get()
        password = self.password_code(password_raw)

        if len(login) == 0 and len(password) == 0:
            messagebox.showwarning(title="Ошибка", message="Введите логин и пароль")
            return

        elif len(login) == 0 and len(password) != 0:
            messagebox.showwarning(title="Ошибка", message="Введите логин")
            return

        elif len(login) != 0 and len(password) == 0:
            messagebox.showwarning(title="Ошибка", message="Введите пароль")
            return

        file = self.open_file()
        a = file.readline()[:-1].split(" ")

        while True:
            if a != [""]:
                self.users[a[0]] = a[1]
                a = file.readline()[:-1].split(" ")
            else:
                break

        flag_reg = False
        for i in self.users.items():
            login_check, password_check = i
            if login == login_check and password == password_check:
                flag_reg = True
                break

        if flag_reg:
            for widget in self.master.winfo_children():
                widget.destroy()

            Label(self.master, text="Вы успешно авторизировались!", font="Arial 16 bold").place(x=90, y=60)
            button = Button(text="Играть", command=self.do_game)
            button.place(x=225, y=150)
        else:
            messagebox.showwarning(title="Ошибка", message="Такого пользователя не существует")

    def registrate(self):
        login = self.entry_login.get()
        password_raw = self.entry_password.get()
        password = self.password_code(password_raw)

        if len(login) == 0 and len(password) == 0:
            messagebox.showwarning(title="Ошибка", message="Введите желаемые логин и пароль")

        elif len(login) == 0 and len(password) != 0:
            messagebox.showwarning(title="Ошибка", message="Введите логин")

        elif len(login) != 0 and len(password) == 0:
            messagebox.showwarning(title="Ошибка", message="Введите пароль")

        else:
            file = self.open_file()
            temp = file.readline()[:-1].split(' ')

            while True:
                if temp != [""]:
                    self.users[temp[0]] = temp[1]
                    temp = file.readline()[:-1].split(' ')
                else:
                    break

            flag_reg = False

            for i in self.users.items():
                l, p = i
                if login == l:
                    flag_reg = True

            if not flag_reg:
                file = self.open_file()
                file.seek(0, os.SEEK_END)
                file.write(f'{login} {password}\n')
                file.close()

                self.canvas.delete("all")
                for widget in self.master.winfo_children():
                    widget.destroy()
                Label(text=f"Вы успешно зарегистрировались!\nВаш логин: {login}\nВаш пароль: {password_raw}",
                      font="Arial 16 bold").place(x=60, y=60)
                button = Button(text="Играть", command=self.do_game)
                button.place(x=225, y=200)
            else:
                messagebox.showwarning(title="Ошибка", message="Такой аккаунт уже существует")

    def do_game(self):
        self.master.title("Шашки")
        self.canvas = Canvas(self.master, width=450, height=400, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board(self.current_player)

    def draw_board(self, current_plr):
        if current_plr == [1, 3]:
            self.canvas.create_text(420, 170, text="Х\nо\nд\n\nБ\nе\nл\nы\nх", font=("Arial", 20), fill="black")
        else:
            self.canvas.create_text(420, 170, text="Х\nо\nд\n\nЧ\nе\nр\nн\nы\nх", font=("Arial", 20), fill="black")
        for row in range(8):
            for col in range(8):
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                color = "#E7CFA9" if (row + col) % 2 == 0 else "#927456"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

                piece = self.board[row][col]
                if piece == 1:
                    self.canvas.create_image(x1, y1, anchor='nw', image=white_checker)
                elif piece == 2:
                    self.canvas.create_image(x1, y1, anchor='nw', image=black_checker)
                elif piece == 3:
                    self.canvas.create_image(x1, y1, anchor='nw', image=white_queen)
                elif piece == 4:
                    self.canvas.create_image(x1, y1, anchor='nw', image=black_queen)

    def on_click(self, event):
        global vzyat, correct
        correct = False
        col = event.x // 50
        row = event.y // 50
        print(self.selected_piece)
        print(self.current_player, self.need_attack)
        if self.selected_piece is None:
            piece = self.board[row][col]
            if piece != 0:
                # создание обводки
                if piece in self.current_player:
                    self.selected_rectangle = self.canvas.create_rectangle(event.x // 50 * 50, event.y // 50 * 50,
                                                                           event.x // 50 * 50 + 50,
                                                                           event.y // 50 * 50 + 50,
                                                                           outline="yellow", width=2)
                self.selected_piece = (row, col)
        else:
            dest_row, dest_col = row, col
            src_row, src_col = self.selected_piece
            if self.board[self.selected_piece[0]][
                self.selected_piece[1]] in self.current_player:  # проверка выбора своей шашки игрока
                correct, vzyat = self.is_valid_move(src_row, src_col, dest_row, dest_col)
                print(correct, vzyat)
                if correct:
                    print('AAAAAAAAAAAAAAAAAAAAA')
                    if self.board[src_row][src_col] == 1 and dest_row == 7:  # становление дамкой у красных
                        self.board[dest_row][src_col] = 3
                        self.board[src_row][src_col] = 0
                        print('Белые стали дамкой')
                    elif self.board[src_row][src_col] == 2 and dest_row == 0:  # становление дамкой у черных
                        self.board[dest_row][src_col] = 4
                        self.board[src_row][src_col] = 0
                        for i in range(len(self.board)):
                            print(self.board[i])
                        print('Черные стали дамкой')
                    else:
                        self.board[dest_row][dest_col] = self.board[src_row][src_col]
                        self.board[src_row][src_col] = 0
                    if vzyat:
                        self.selected_piece = dest_row, dest_col
                        self.canvas.delete("all")
                        self.draw_board(self.current_player)
                        self.selected_rectangle = self.canvas.create_rectangle(dest_col * 50, dest_row * 50,
                                                                               dest_col * 50 + 50, dest_row * 50 + 50,
                                                                               outline="yellow", width=2)
                    else:
                        self.switch_player()
                        self.selected_piece = None
                        self.canvas.delete("all")
                        self.draw_board(self.current_player)
                        self.need_attack = False
                        self.check_win()
                        self.fix_attack(vzyat, dest_row, dest_col)

                    for i in range(len(self.board)):
                        print(self.board[i])
                else:
                    self.selected_piece = None
                    self.canvas.delete("all")
                    self.draw_board(self.current_player)
            else:
                self.selected_piece = None
                self.canvas.delete("all")
                self.draw_board(self.current_player)

    def fix_attack(self, vzyat, row, col):
        if not vzyat:
            if self.current_player == [1, 3]:  # проверка обязаности белых
                for i in range(8):
                    for j in range(8):
                        try:
                            if self.board[i][j] in [2, 4]:
                                if self.board[i - 1][j] == 0:
                                    for k in range(i + 1, 8):
                                        if self.board[k][j] == 3:
                                            self.need_attack = True
                                            break
                                        elif self.board[k][j] in [1, 2, 3, 4]:
                                            break
                                if self.board[i + 1][j] == 0:
                                    for k in range(i - 1, -1, -1):
                                        if self.board[k][j] == 3:
                                            self.need_attack = True
                                            break
                                        elif self.board[k][j] == 1 and abs(i - k) == 1:
                                            self.need_attack = True
                                            break
                                        elif self.board[k][j] in [1, 2, 3, 4]:
                                            break
                        except IndexError:
                            pass
                for i in range(8):
                    for j in range(8):
                        try:
                            if self.board[i][j] in [2, 4]:
                                if self.board[i][j - 1] == 0:
                                    for k in range(j + 1, 8):
                                        if self.board[i][k] == 3:
                                            self.need_attack = True
                                            break
                                        elif self.board[i][k] == 1 and abs(j - k) == 1:
                                            self.need_attack = True
                                            break
                                        elif self.board[i][k] in [1, 2, 3, 4]:
                                            break
                                if self.board[i][j + 1] == 0:
                                    for k in range(j - 1, -1, -1):
                                        if self.board[i][k] == 3:
                                            self.need_attack = True
                                            break
                                        elif self.board[i][k] == 1 and abs(j - k) == 1:
                                            self.need_attack = True
                                            break
                                        elif self.board[i][k] in [1, 2, 3, 4]:
                                            break
                        except IndexError:
                            pass
            if self.current_player == [2, 4]:  # проверка обязанности черных
                print('ЧЕКАЮ')
                for i in range(8):
                    for j in range(8):
                        try:
                            if self.board[i][j] in [1, 3]:
                                if self.board[i - 1][j] == 0:  # проверка атаки вперед
                                    for k in range(i + 1, 8):
                                        if self.board[k][j] == 4:  # проверка для дамки
                                            self.need_attack = True
                                            break
                                        elif self.board[k][j] == 2 and abs(i - k) == 1:
                                            self.need_attack = True
                                            break
                                        elif self.board[k][j] in [1, 3]:
                                            break
                                if self.board[i + 1][j] == 0:  # проверка атаки назад дамкой
                                    for k in range(i - 1, -1, -1):
                                        if self.board[k][j] == 4:
                                            self.need_attack = True
                                            break
                                        elif self.board[k][j] in [1, 2, 3, 4]:
                                            break
                        except IndexError:
                            pass
                for i in range(8):
                    for j in range(8):
                        try:
                            if self.board[i][j] in [1, 3]:
                                if self.board[i][j - 1] == 0:  # проверка атаки влево
                                    for k in range(j + 1, 8):
                                        if self.board[i][k] == 4:  # проверка для дамки
                                            self.need_attack = True
                                            break
                                        elif self.board[i][k] == 2 and abs(j - k) == 1:
                                            self.need_attack = True
                                            break
                                        elif self.board[i][k] in [1, 3]:
                                            break
                                if self.board[i][j + 1] == 0:  # проверка атаки вправо
                                    for k in range(j - 1, -1, -1):
                                        if self.board[i][k] == 4:
                                            self.need_attack = True
                                            break
                                        elif self.board[i][k] == 2 and abs(j - k) == 1:
                                            self.need_attack = True
                                            break
                                        elif self.board[i][k] in [1, 2, 3, 4]:
                                            break
                        except IndexError:
                            pass

    def is_valid_move(self, src_row, src_col, dest_row, dest_col):
        print('тута')
        # Allow vertical (up or down) and horizontal (left or right) moves
        if self.board[src_row][src_col] == 1 and self.board[dest_row][dest_col] == 0:  # проверки для белых пешек
            if (dest_row - src_row == 1 and abs(dest_col - src_col) == 0) or \
                    (dest_row - src_row == 0 and abs(dest_col - src_col) == 1):  # ход на пустую клетку
                if not self.need_attack:
                    return [True, False]
            elif (dest_row - src_row == 2 and abs(dest_col - src_col) == 0 and  # взятие по прямой
                  self.board[dest_row - 1][dest_col] in [2, 4]):
                self.board[dest_row - 1][dest_col] = 0
                if self.need_attack:
                    self.need_attack = False
                try:  # проверка есть ли дальше возможность атаковать
                    if self.board[dest_row + 1][dest_col] in [2, 4] and self.board[dest_row + 2][dest_col] == 0:
                        return [True, True]
                    elif self.board[dest_row][dest_col + 1] in [2, 4] and self.board[dest_row][dest_col + 2] == 0:
                        return [True, True]
                    elif self.board[dest_row][dest_col - 1] in [2, 4] and self.board[dest_row][dest_col - 2] == 0:
                        return [True, True]
                    else:
                        return [True, False]
                except IndexError:
                    return [True, False]
            elif dest_col - src_col == 2 and dest_row == src_row and self.board[dest_row][
                dest_col - 1] in [2, 4]:  # если ход вправо
                self.board[dest_row][dest_col - 1] = 0
                if self.need_attack:
                    self.need_attack = False
                try:  # проверка есть ли дальше возможность атаковать
                    if self.board[dest_row + 1][dest_col] in [2, 4] and self.board[dest_row + 2][dest_col] == 0:
                        return [True, True]
                    elif self.board[dest_row][dest_col + 1] in [2, 4] and self.board[dest_row][dest_col + 2] == 0:
                        return [True, True]
                    else:
                        return [True, False]
                except IndexError:
                    return [True, False]
            elif dest_col - src_col == -2 and dest_row == src_row and self.board[dest_row][
                dest_col + 1] in [2, 4]:  # если ход влево
                self.board[dest_row][dest_col + 1] = 0
                if self.need_attack:
                    self.need_attack = False
                try:  # проверка есть ли дальше возможность атаковать
                    if self.board[dest_row + 1][dest_col] in [2, 4] and self.board[dest_row + 2][dest_col] == 0:
                        return [True, True]
                    elif self.board[dest_row][dest_col - 1] in [2, 4] and self.board[dest_row][dest_col - 2] == 0:
                        return [True, True]
                    else:
                        return [True, False]
                except IndexError:
                    return [True, False]
        elif self.board[src_row][src_col] == 3 and self.board[dest_row][dest_col] == 0:  # првоерка для белой дамки
            print('проверка')
            if (abs(dest_row - src_row) >= 1 and abs(dest_col - src_col) == 0) or \
                    (abs(dest_row - src_row) == 0 and abs(dest_col - src_col) >= 1):  # ход на пустую клетку
                if src_col == dest_col:
                    correct, attack = self.check_col(src_row, dest_row, src_col)
                    if correct and attack == 0 and not self.need_attack:
                        return [True, False]
                    elif correct and attack >= 1:
                        self.board[attack - 1][src_col] = 0
                        if dest_row - (attack - 1) > 0:  # если ход был вниз
                            try:
                                for i in range(dest_row + 1, 8):
                                    if self.board[i][dest_col] in [2, 4] and self.board[i + 1][dest_col] == 0:
                                        return [True, True]
                                    elif self.board[i][dest_col] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_col + 1, 8):  # вправо
                                    if self.board[dest_row][i] in [2, 4] and self.board[dest_row][i + 1] == 0:
                                        return [True, True]
                                    elif self.board[dest_row][i] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_col - 1, 0, -1):  # влево
                                    if self.board[dest_row][i] in [2, 4] and self.board[dest_row][i - 1] == 0:
                                        return [True, True]
                                    elif self.board[dest_row][i] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                        elif dest_row - (attack - 1) < 0:  # если ход был вверх
                            try:
                                for i in range(dest_row - 1, 0, -1):
                                    if self.board[i][dest_col] in [2, 4] and self.board[i - 1][dest_col] == 0:
                                        return [True, True]
                                    elif self.board[i][dest_col] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_col + 1, 8):  # вправо
                                    if self.board[dest_row][i] in [2, 4] and self.board[dest_row][i + 1] == 0:
                                        return [True, True]
                                    elif self.board[dest_row][i] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_col - 1, 0, -1):  # влево
                                    if self.board[dest_row][i] in [2, 4] and self.board[dest_row][i - 1] == 0:
                                        return [True, True]
                                    elif self.board[dest_row][i] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                        return [True, False]
                    else:
                        if not vzyat:
                            return [False, False]
                elif src_row == dest_row:
                    correct, attack = self.check_row(src_col, dest_col, src_row)
                    if correct and attack == 0 and not self.need_attack:
                        return [True, False]
                    elif correct and attack >= 1:
                        self.board[src_row][attack - 1] = 0
                        if dest_col - (attack - 1) > 0:  # если ход был вправо
                            try:
                                for i in range(dest_col + 1, 8):
                                    if self.board[dest_row][i] in [2, 4] and self.board[dest_row][i + 1] == 0:
                                        return [True, True]
                                    elif self.board[dest_row][i] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_row + 1, 8):  # вниз
                                    if self.board[i][dest_col] in [2, 4] and self.board[i + 1][dest_col] == 0:
                                        return [True, True]
                                    elif self.board[i][dest_col] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_row - 1, 0, -1):  # вверх
                                    if self.board[i][dest_col] in [2, 4] and self.board[i - 1][dest_col] == 0:
                                        return [True, True]
                                    elif self.board[i][dest_col] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                        elif dest_col - (attack - 1) < 0:  # если ход был влево
                            print('МИУ')
                            try:
                                for i in range(dest_col - 1, 0, -1):
                                    if self.board[dest_row][i] in [2, 4] and self.board[dest_row][i - 1] == 0:
                                        return [True, True]
                                    elif self.board[dest_row][i] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_row + 1, 8):  # вниз
                                    if self.board[i][dest_col] in [2, 4] and self.board[i + 1][dest_col] == 0:
                                        print('МИУ2')
                                        print(self.board[i][dest_col])
                                        return [True, True]
                                    elif self.board[i][dest_col] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_row - 1, 0, -1):  # вверх
                                    if self.board[i][dest_col] in [2, 4] and self.board[i - 1][dest_col] == 0:
                                        return [True, True]
                                    elif self.board[i][dest_col] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                        return [True, False]
                    else:
                        if not vzyat:
                            return [False, False]
        elif self.board[src_row][src_col] == 2 and self.board[dest_row][dest_col] == 0:  # проверки для черных пешек
            if (dest_row - src_row == -1 and abs(dest_col - src_col) == 0) or \
                    (dest_row - src_row == 0 and abs(dest_col - src_col) == 1):  # ход на пустую клетку
                if not self.need_attack:
                    return [True, False]
            elif (dest_row - src_row == -2 and abs(dest_col - src_col) == 0 and
                  self.board[dest_row + 1][dest_col] in [1, 3]):  # взятие по прямой
                self.board[dest_row + 1][dest_col] = 0
                if self.need_attack:
                    self.need_attack = False
                try:  # проверка есть ли дальше возможность атаковать
                    if self.board[dest_row - 1][dest_col] in [1, 3] and self.board[dest_row - 2][dest_col] == 0:
                        return [True, True]
                    elif self.board[dest_row][dest_col + 1] in [1, 3] and self.board[dest_row][dest_col + 2] == 0:
                        return [True, True]
                    elif self.board[dest_row][dest_col - 1] in [1, 3] and self.board[dest_row][dest_col - 2] == 0:
                        return [True, True]
                    else:
                        return [True, False]
                except IndexError:
                    return [True, False]
            elif dest_col - src_col == 2 and dest_row == src_row and self.board[dest_row][
                dest_col - 1] in [1, 3]:  # если ход вправо
                self.board[dest_row][dest_col - 1] = 0
                if self.need_attack:
                    self.need_attack = False
                try:  # проверка есть ли дальше возможность атаковать
                    if self.board[dest_row - 1][dest_col] in [1, 3] and self.board[dest_row - 2][dest_col] == 0:
                        return [True, True]
                    elif self.board[dest_row][dest_col + 1] in [1, 3] and self.board[dest_row][dest_col + 2] == 0:
                        return [True, True]
                    else:
                        return [True, False]
                except IndexError:
                    return [True, False]
            elif dest_col - src_col == -2 and dest_row == src_row and self.board[dest_row][
                dest_col + 1] in [1, 3]:  # если ход влево
                self.board[dest_row][dest_col + 1] = 0
                if self.need_attack:
                    self.need_attack = False
                try:  # проверка есть ли дальше возможность атаковать
                    if self.board[dest_row - 1][dest_col] in [1, 3] and self.board[dest_row - 2][dest_col] == 0:
                        return [True, True]
                    elif self.board[dest_row][dest_col - 1] in [1, 3] and self.board[dest_row][dest_col - 2] == 0:
                        return [True, True]
                    else:
                        return [True, False]
                except IndexError:
                    return [True, False]
        elif self.board[src_row][src_col] == 4 and self.board[dest_row][dest_col] == 0:  # првоерка для черной дамки
            if (abs(dest_row - src_row) >= 1 and abs(dest_col - src_col) == 0) or \
                    (abs(dest_row - src_row == 0) and abs(dest_col - src_col) >= 1):  # ход
                if src_col == dest_col:
                    correct, attack = self.check_col(src_row, dest_row, src_col)
                    if correct and attack == 0 and not self.need_attack:
                        return [True, False]
                    elif correct and attack >= 1:
                        self.board[attack - 1][src_col] = 0
                        if dest_row - (attack - 1) > 0:  # если ход был вниз
                            try:
                                for i in range(dest_row + 1, 8):
                                    if self.board[i][dest_col] in [1, 3] and self.board[i + 1][dest_col] == 0:
                                        return [True, True]
                                    elif self.board[i][dest_col] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_col + 1, 8):  # вправо
                                    if self.board[dest_row][i] in [1, 3] and self.board[dest_row][i + 1] == 0:
                                        return [True, True]
                                    elif self.board[dest_row][i] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_col - 1, 0, -1):  # влево
                                    if self.board[dest_row][i] in [1, 3] and self.board[dest_row][i - 1] == 0:
                                        return [True, True]
                                    elif self.board[dest_row][i] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                        elif dest_row - (attack - 1) < 0:  # если ход был вверх
                            try:
                                for i in range(dest_row - 1, 0, -1):
                                    if self.board[i][dest_col] in [1, 3] and self.board[i - 1][dest_col] == 0:
                                        return [True, True]
                                    elif self.board[i][dest_col] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_col + 1, 8):  # вправо
                                    if self.board[dest_row][i] in [1, 3] and self.board[dest_row][i + 1] == 0:
                                        return [True, True]
                                    elif self.board[dest_row][i] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_col - 1, 0, -1):  # влево
                                    if self.board[dest_row][i] in [1, 3] and self.board[dest_row][i - 1] == 0:
                                        return [True, True]
                                    elif self.board[dest_row][i] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                        return [True, False]
                    else:
                        if not vzyat:
                            return [False, False]
                elif src_row == dest_row:
                    correct, attack = self.check_row(src_col, dest_col, src_row)
                    if correct and attack == 0 and not self.need_attack:
                        return [True, False]
                    elif correct and attack >= 1:
                        self.board[src_row][attack - 1] = 0
                        if dest_col - (attack - 1) > 0:  # если ход был вправо
                            try:
                                for i in range(dest_col + 1, 8):
                                    if self.board[dest_row][i] in [1, 3] and self.board[dest_row][i + 1] == 0:
                                        return [True, True]
                                    elif self.board[dest_row][i] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_row + 1, 8):  # вниз
                                    if self.board[i][dest_col] in [1, 3] and self.board[i + 1][dest_col] == 0:
                                        return [True, True]
                                    elif self.board[i][dest_col] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_row - 1, 0, -1):  # вверх
                                    if self.board[i][dest_col] in [1, 3] and self.board[i - 1][dest_col] == 0:
                                        return [True, True]
                                    elif self.board[i][dest_col] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                        elif dest_col - (attack - 1) < 0:  # если ход был влево
                            print('МИУ')
                            try:
                                for i in range(dest_col - 1, 0, -1):
                                    if self.board[dest_row][i] in [1, 3] and self.board[dest_row][i - 1] == 0:
                                        return [True, True]
                                    elif self.board[dest_row][i] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_row + 1, 8):  # вниз
                                    if self.board[i][dest_col] in [1, 3] and self.board[i + 1][dest_col] == 0:
                                        print('МИУ2')
                                        print(self.board[i][dest_col])
                                        return [True, True]
                                    elif self.board[i][dest_col] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                            try:
                                for i in range(dest_row - 1, 0, -1):  # вверх
                                    if self.board[i][dest_col] in [1, 3] and self.board[i - 1][dest_col] == 0:
                                        return [True, True]
                                    elif self.board[i][dest_col] in [1, 2, 3, 4]:
                                        break
                            except IndexError:
                                pass
                        return [True, False]
                    else:
                        if not vzyat:
                            return [False, False]
        else:
            if not vzyat:
                return [False, False]

    def switch_player(self):
        if self.current_player == [1, 3]:
            self.current_player = [2, 4]
        else:
            self.current_player = [1, 3]

    def check_win(self):
        count = 0
        count2 = 0
        for i in range(8):
            count += self.board[i].count(1)
            count += self.board[i].count(3)
            count2 += self.board[i].count(2)
            count2 += self.board[i].count(4)
        if count > 1 >= count2:
            messagebox.showinfo("Уведомление", "Победа белых!")
            self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [2, 2, 2, 2, 2, 2, 2, 2],
                          [2, 2, 2, 2, 2, 2, 2, 2],
                          [0, 0, 0, 0, 0, 0, 0, 0]]
            self.canvas.delete("all")
            self.draw_board(self.current_player)
        elif count2 > 1 >= count:
            messagebox.showinfo("Уведомление", "Победа черных!")
            self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [2, 2, 2, 2, 2, 2, 2, 2],
                          [2, 2, 2, 2, 2, 2, 2, 2],
                          [0, 0, 0, 0, 0, 0, 0, 0]]
            self.canvas.delete("all")
            self.draw_board(self.current_player)
        elif count == count2 == 1:
            messagebox.showinfo("Уведомление", "Играла закончилась ничьей!")
            self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                          [1, 1, 1, 1, 1, 1, 1, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [2, 2, 2, 2, 2, 2, 2, 2],
                          [2, 2, 2, 2, 2, 2, 2, 2],
                          [0, 0, 0, 0, 0, 0, 0, 0]]
            self.canvas.delete("all")
            self.draw_board(self.current_player)
        else:
            count = 0
            count2 = 0
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] in [1, 3]:
                        try:
                            if self.board[i + 1][j] == 0 or (
                                    self.board[i + 1][j] in [2, 4] and self.board[i + 2][j] == 0):
                                count += 1
                            elif self.board[i][j + 1] == 0 or (
                                    self.board[i][j + 1] in [2, 4] and self.board[i][j + 2] == 0):
                                count += 1
                            elif self.board[i][j - 1] == 0 or (
                                    self.board[i][j - 1] in [2, 4] and self.board[i][j - 2] == 0):
                                count += 1
                        except IndexError:
                            pass
                    elif self.board[i][j] in [2, 4]:
                        try:
                            if self.board[i - 1][j] == 0 or (
                                    self.board[i - 1][j] in [1, 3] and self.board[i - 2][j] == 0):
                                count2 += 1
                            elif self.board[i][j + 1] == 0 or (
                                    self.board[i][j + 1] in [1, 3] and self.board[i][j + 2] == 0):
                                count2 += 1
                            elif self.board[i][j - 1] == 0 or (
                                    self.board[i][j - 1] in [1, 3] and self.board[i][j - 2] == 0):
                                count2 += 1
                        except IndexError:
                            pass
            print(count, count2)
            if count == 0:
                messagebox.showinfo("Уведомление", "Победа черных!")
                self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1],
                              [1, 1, 1, 1, 1, 1, 1, 1],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [2, 2, 2, 2, 2, 2, 2, 2],
                              [2, 2, 2, 2, 2, 2, 2, 2],
                              [0, 0, 0, 0, 0, 0, 0, 0]]
                self.canvas.delete("all")
                self.draw_board(self.current_player)
            if count2 == 0:
                messagebox.showinfo("Уведомление", "Победа белых!")
                self.board = [[0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 1, 1, 1, 1, 1, 1],
                              [1, 1, 1, 1, 1, 1, 1, 1],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0],
                              [2, 2, 2, 2, 2, 2, 2, 2],
                              [2, 2, 2, 2, 2, 2, 2, 2],
                              [0, 0, 0, 0, 0, 0, 0, 0]]
                self.canvas.delete("all")
                self.draw_board(self.current_player)

    def check_col(self, start, end, col):
        count = 0
        index = 0
        correct_ind = end
        if start > end:
            start, end = end - 1, start - 1
        else:
            correct_ind -= 2
        for i in range(start + 1, end + 1):
            if self.board[i][col] != 0:
                if self.board[i][col] in self.current_player:
                    count += 1
                count += 1
                index = i + 1
        if count == 0:
            return [True, False]
        elif count == 1 and correct_ind + 1 == index - 1:
            return [True, index]
        else:
            return [False, False]

    def check_row(self, start, end, row):
        count = 0
        index = 0
        correct_ind = end - 1
        if start > end:
            correct_ind += 2
            start, end = end, start
        for i in range(start + 1, end):
            if self.board[row][i] != 0:
                if self.board[row][i] in self.current_player:
                    count += 1
                index = i + 1
                count += 1
        if count == 0:
            return [True, False]
        elif count == 1 and correct_ind == index - 1:
            return [True, index]
        else:
            return [False, False]


def main():
    root = Tk()
    app = CheckersBoard(root)
    root.mainloop()


if __name__ == "__main__":
    main()