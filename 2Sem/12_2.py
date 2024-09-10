import tkinter as tk
from tkinter import simpledialog


my_list = []

def create_list():
    global my_list
    my_list = []
    show_message("Список создан")

def print_list():
    print(my_list)

def save_list():
    with open("my_list.txt", "w") as f:
        for item in my_list:
            f.write(str(item) + "\n")
    show_message("Список сохранен")

def count_elements():
    result = len(my_list)
    show_message(f"Количество элементов: {result}")

def add_element():
    global my_list
    new_item = simpledialog.askstring("Добавление элемента", "Введите элемент:")
    if new_item:
        my_list.append(new_item)
        show_message("Элемент добавлен")

def find_element():
    element_to_find = simpledialog.askstring("Поиск элемента", "Введите элемент для поиска:")
    if element_to_find in my_list:
        show_message("Элемент найден")
    else:
        show_message("Элемент не найден")

def remove_element():
    global my_list
    element_to_remove = simpledialog.askstring("Удаление элемента", "Введите элемент для удаления:")
    if element_to_remove in my_list:
        my_list.remove(element_to_remove)
        show_message("Элемент удален")
    else:
        show_message("Элемент не найден")

def show_message(message):
    tk.messagebox.showinfo("Сообщение", message)

# Главное окно
root = tk.Tk()
root.title("Работа со списком")

# Кнопки
buttons = [
    tk.Button(root, text="Создать список", command=create_list),
    tk.Button(root, text="Вывести список", command=print_list),
    tk.Button(root, text="Сохранить список", command=save_list),
    tk.Button(root, text="Количество элементов", command=count_elements),
    tk.Button(root, text="Добавить элемент", command=add_element),
    tk.Button(root, text="Найти элемент", command=find_element),
    tk.Button(root, text="Удалить элемент", command=remove_element),
    tk.Button(root, text="Выход", command=root.quit)
]

# Размещение кнопок
for i, button in enumerate(buttons):
    button.pack()

root.mainloop()