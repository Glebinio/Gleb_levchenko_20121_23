import tkinter as tk
from tkinter import ttk
import math

class Figure:
    def __init__(self):
        pass

    def area(self):
        pass

    def draw(self, canvas):
        pass

class Triangle(Figure):
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        return 0.5 * self.height * self.base

    def draw(self, canvas):
        canvas.create_polygon(10, 10, 10 + self.base, 10, 10 + self.base / 2, 10 + self.height, fill="blue")

class Rectangle(Figure):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def draw(self, canvas):
        canvas.create_rectangle(10, 10, 10 + self.width, 10 + self.height, fill="green")

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def draw(self, canvas):
        canvas.create_oval(10, 10, 10 + 2 * self.radius, 10 + 2 * self.radius, fill="red")

def draw_figure():
    global figure_choice, height_entry, base_entry, width_entry, radius_entry, canvas
    
    if figure_choice.get() == "Треугольник":
        figure = Triangle(int(height_entry.get()), int(base_entry.get()))
    elif figure_choice.get() == "Прямоугольник":
        figure = Rectangle(int(height_entry.get()), int(width_entry.get()))
    else:
        figure = Circle(int(radius_entry.get()))

    canvas.delete("all")
    figure.draw(canvas)
    area_label.config(text=f"Площадь: {figure.area():.2f}")


root = tk.Tk()
root.title("Рисование фигур")


input_frame = tk.Frame(root)
canvas_frame = tk.Frame(root)
input_frame.pack(side="left")
canvas_frame.pack(side="right")

# Виджеты для ввода данных
figure_choice = ttk.Combobox(input_frame, values=["Треугольник", "Прямоугольник", "Круг"])
figure_choice.pack()

height_label = tk.Label(input_frame, text="Высота (Треугольник, Прямоугольник):")
height_label.pack()
height_entry = tk.Entry(input_frame)
height_entry.pack()

base_label = tk.Label(input_frame, text="Основание (Треугольник):")
base_label.pack()
base_entry = tk.Entry(input_frame)
base_entry.pack()

width_label = tk.Label(input_frame, text="Ширина(Прямоугольник):")
width_label.pack()
width_entry = tk.Entry(input_frame)
width_entry.pack()

radius_label = tk.Label(input_frame, text="Радиус(Круг):")
radius_label.pack()
radius_entry = tk.Entry(input_frame)
radius_entry.pack()

# Кнопка
draw_button = tk.Button(input_frame, text="Отобразить", command=draw_figure)
draw_button.pack()
# окно отображения
canvas = tk.Canvas(canvas_frame, width=300, height=300)
canvas.pack()

# Площадь
area_label = tk.Label(input_frame)
area_label.pack()

root.mainloop()