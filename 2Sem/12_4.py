import tkinter as tk
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Угадай число")

        # Генерация случайного числа
        self.secret_number = random.randint(1, 100)
        self.num_guesses = 0

        # Создание элементов интерфейса
        self.label = tk.Label(master, text="Введите ваше число:")
        self.entry = tk.Entry(master)
        self.button = tk.Button(master, text="Проверить", command=self.check_guess)
        self.result_label = tk.Label(master, text="")
        self.reset_button = tk.Button(master, text="Начать заново", command=self.reset_game)

        # Размещение элементов на форме
        self.label.pack()
        self.entry.pack()
        self.button.pack()
        self.result_label.pack()
        self.reset_button.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.num_guesses += 1

            if guess < self.secret_number:
                self.result_label.config(text="Загаданное число больше")
            elif guess > self.secret_number:
                self.result_label.config(text="Загаданное число меньше")
            else:
                self.result_label.config(text=f"Вы угадали за {self.num_guesses} попыток!")
                self.button.config(state='disabled')
        except ValueError:
            self.result_label.config(text="Пожалуйста, введите число")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.num_guesses = 0
        self.entry.delete(0, 'end')
        self.result_label.config(text="")
        self.button.config(state='normal')

# Создание главного окна
root = tk.Tk()
game = GuessingGame(root)
root.mainloop()