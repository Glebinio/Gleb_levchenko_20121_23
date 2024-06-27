from numpy import array
import tkinter as tk
import copy
import pygame
import random
date = []
vars: list
allVar: list


def sh2 (i_g,n,shh):

    

    def button_clicked(i_g):
        with open("C:\sha\out.txt", "w") as f:
            if not len(i_g):
                f.write("no solutions")
            else:
                f.writelines(f"{str(i)} " for i in i_g)
                f.writelines('\n')


    
    def draw_chessboard(screen, n):
        for y in range(n):
            for x in range(n):
                color = WHITE if (x + y) % 2 == 0 else BLACK
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, color, rect)



    def draw_red_triangle(screen, cell_size, x, y):

        points = [
            (x * cell_size + cell_size / 2, y * cell_size),
            (x * cell_size, y * cell_size + cell_size),
            (x * cell_size + cell_size, y * cell_size + cell_size / 2),
        ]

        # Определение цвета треугольника
        color = (255, 0, 0)  # Красный

        # Отрисовка треугольника
        pygame.draw.polygon(screen, color, points)
    
    def draw_yelow_triangle(screen, cell_size, x, y):

        points = [
            (x * cell_size + cell_size / 2, y * cell_size),
            (x * cell_size, y * cell_size + cell_size),
            (x * cell_size + cell_size, y * cell_size + cell_size / 2),
        ]

        # Определение цвета треугольника
        color = (255, 255, 0)  # Красный

        # Отрисовка треугольника
        pygame.draw.polygon(screen, color, points)

    def draw_red_circles(screen, cell_size, x, y):

        center_x = (x + 0.5) * cell_size
        center_y = (y + 0.5) * cell_size

        # Радиус кружочков
        radius = cell_size // 4

        # Расстановка кружочков по соседним клеткам
        for dx, dy in [(0, 1), (0, 2), (0, -1), (0, -2), (1, 0), (2, 0), (-1, 0), (-2, 0),(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            new_x = dx+center_x + (dx) * cell_size
            new_y = dx+ center_y + (dy) * cell_size
            pygame.draw.circle(screen, (0,0,255), (new_x,new_y),  radius, width=0)






    # Инициализация Pygame
    pygame.init()

    # Размер экрана
    
    # Цвета
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400
    # n = 10  # Размер доски 
    CELL_COUNT_X = n
    CELL_COUNT_Y = n
    CELL_SIZE = SCREEN_WIDTH // CELL_COUNT_X
    
    screen_width = n * CELL_SIZE
    screen_height = n * CELL_SIZE


    # Размер клетки
    x = 0  # Координата X клетки (0-based)
    y = 0  # Координата Y клетки (0-based)
    # Создание двумерного массива 3x3 с помощью list comprehension
    figure_positions = [[False for j in range(n)] for i in range(n)]

    figure_positions[x][y]=True

    # Инициализация шрифта
    font = pygame.font.Font(None, 36)

    # Отрисовка текста
    text = font.render("Записать решение в файл", True, (255, 0, 0))

    # Получение размеров текста
    text_rect = text.get_rect(center=((screen_width +200), (screen_height // 2)-100))
    # Определение параметров кнопки
    button_width =75
    button_height = 40
    button_x = (screen_width+125 + button_width//2)
    button_y = (screen_height - button_height) // 2
    # Создание объекта Rect для кнопки
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)



    # Создание экрана
    screen = pygame.display.set_mode((screen_width+400, screen_height))
    pygame.display.set_caption("Шахматная доска")



    g=[]
    i,j=0,0

    # Главный цикл
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if button_rect.collidepoint(mouse_x, mouse_y):
                    button_clicked(i_g)

                

        # Очистка экрана
        screen.fill((0, 0, 0))

        # Отрисовка шахматной доски
        
        draw_chessboard(screen, n)
        for h in i_g:
            draw_yelow_triangle(screen, CELL_SIZE, h[0],h[1])
            draw_red_circles(screen, CELL_SIZE, h[0], h[1])
        for h in shh:
            draw_red_triangle(screen, CELL_SIZE, h[0], h[1])


        rect = pygame.Rect(screen_width, 0, 400, screen_height)
        pygame.draw.rect(screen, (128,128,128), rect)
        # Отрисовка кнопки
        pygame.draw.rect(screen, (0, 145, 0), button_rect)

        screen.blit(text, text_rect)

        # Обновление экрана
        pygame.display.flip()

    # Завершение Pygame
    pygame.quit()


def ras (n,l,shh):

    class Board:
        def __init__(self, size):
            self.size = size
            self.zero = array([[0] * self.size for _ in range(self.size)])


        def is_under_attack(self,x,y):#поиск возможных ходов
        #Ходы по ходу ладьи и коня
            self.get_attacked_cells( x + 2, y + 1)
            self.get_attacked_cells( x + 2, y - 1)
            self.get_attacked_cells( x - 2, y + 1)
            self.get_attacked_cells( x - 2, y - 1)
            self.get_attacked_cells( x + 1, y + 2)
            self.get_attacked_cells( x + 1, y - 2)
            self.get_attacked_cells( x - 1, y + 2)
            self.get_attacked_cells( x - 1, y - 2)
            self.get_attacked_cells( x - 1, y)
            self.get_attacked_cells( x - 2, y)
            self.get_attacked_cells( x + 2, y)
            self.get_attacked_cells( x + 1, y)
            self.get_attacked_cells( x, y - 1)
            self.get_attacked_cells( x, y - 2)
            self.get_attacked_cells( x, y + 1)
            self.get_attacked_cells( x, y + 2)


        def place_figure(self, figure, vars):#размещение фигуры на доске
            self.zero[figure.x][figure.y] = 1
            vars.append((figure.x, figure.y))
            self.is_under_attack(figure.x, figure.y)
            
            
            
        def get_attacked_cells(self, x, y):#записываем клетки с возможным ударом
            if not (0 <= x < self.size and 0 <= y < self.size):#проверка на выход за пределы поля
                return False
            if self.zero[x][y] != 1:#проверка на поставленную фигуру
                self.zero[x][y] = 2
                return True
            else:
                return True

    class Figure:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        

    def rec(board, x, y, l, n, vars, allVar): #перебор вариантов по строкам и столбцам
        while True:#перебор всех ходов
            y += 1
            if y >= n: 
                y = 0
                x += 1
            if x >= n: 
                break
            a=board.zero
            if a[x][y] == 0:  #Если место доступно для хода, то ставим фигуры
                copy_board = copy.deepcopy(board)
                copy_var = [i for i in vars]
                copy_board.place_figure(Figure (x,y), copy_var)#размещение фигуры
                if l - 1 == 0:#проверка на количество поставленных фигур
                    allVar.append(copy_var)
                    if len(allVar) == 1:
                        print_board_in_console(copy_board)
                    continue
                # рекурсивный перебор
                rec(copy_board, x, y + 1, l - 1, n, copy_var, allVar)

    def print_board_in_console(board):#вывод доски
        a=board.zero
        list_board = []
        x = 0
        y = 0
        for s in a:
            y = 0
            for cell in s:
                if cell == 1:  # если стоит фигура, #
                    list_board.append((x, y, 1))
                elif cell == 2:  # если клетка с возможным ходом *
                    list_board.append((x, y, 2))
                else:  # если клетка пустая, 0
                    list_board.append((x, y, 0))
                y += 1
            x += 1
        for m in a:
            s = ""
            for r in m:
                if r == 1:#если стоит фигура, #
                    s += " " + '#'
                elif r == 2:#если клетка с возможным ходом, *
                    s += " " + '*'
                else:#если клетка пустая, 0
                    s += " " + '0'
            print(s)
        date.append(list_board)


    
    vars = []
    allVar = []
    kit=0

    board = Board (n)
        #Добавление расставленных фигур на доску
    for x,y in shh:

        board.place_figure(Figure (x,y), vars)
    #Если нет фигур которые нужно поставить
    if l == 0:
        if not (len(vars) == 0):
            allVar.append(vars)
        print_board_in_console(board)

    #подбираем расстановки
    rec(board, 0, -1, l, n, vars, allVar)
    # w_out(allVar)
    kit=random.randint (0,len(allVar)-1)
    i_g=allVar[kit]
    sh2(i_g,n,shh)


def sh_1 (n,l) :
    def move_figure(screen, cell_size, figure_positions, x, y, key,n):

        if key == pygame.K_UP and y!=0:
            y = y - 1  # n-1
        elif key == pygame.K_DOWN and y!=n:
            y = n+1  # n+1
        elif key == pygame.K_RIGHT and x!=n:
            x+=1  # k+1
        elif key == pygame.K_LEFT and x!=0:
            x-=1  # k-1

        return (x,y)




    def draw_red_circles(screen, cell_size, x, y):
        
        # Получение координат центра треугольника
        center_x = (x + 0.5) * cell_size
        center_y = (y + 0.5) * cell_size

        # Радиус кружочков
        radius = cell_size // 4

        # Расстановка кружочков по соседним клеткам
        for dx, dy in [(0, 1), (0, 2), (0, -1), (0, -2), (1, 0), (2, 0), (-1, 0), (-2, 0),(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            new_x = dx+center_x + (dx) * cell_size
            new_y = dx+ center_y + (dy) * cell_size
            pygame.draw.circle(screen, (0,0,255), (new_x,new_y),  radius, width=0)

            # Проверка, находится ли кружочек в пределах доски


    def draw_red_triangle(screen, cell_size, x, y):
        
        # Определение вершин треугольника
        points = [
            (x * cell_size + cell_size / 2, y * cell_size),
            (x * cell_size, y * cell_size + cell_size),
            (x * cell_size + cell_size, y * cell_size + cell_size / 2),
        ]

        # Определение цвета треугольника
        color = (255, 0, 0)  # Красный

        # Отрисовка треугольника
        pygame.draw.polygon(screen, color, points)
    def draw_chessboard(screen, n):
        for y in range(n):
            for x in range(n):
                color = WHITE if (x + y) % 2 == 0 else BLACK
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, color, rect)



    # Инициализация Pygame
    pygame.init()

    # Размер экрана
    
    # Цвета
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400
    # n = 10  # Размер доски 
    CELL_COUNT_X = n
    CELL_COUNT_Y = n
    CELL_SIZE = SCREEN_WIDTH // CELL_COUNT_X
    
    screen_width = n * CELL_SIZE
    screen_height = n * CELL_SIZE

    # Размер клетки
    x = 0  # Координата X клетки (0-based)
    y = 0  # Координата Y клетки (0-based)
    figure_positions = [[False for j in range(n)] for i in range(n)]

    figure_positions[x][y]=True



    # Создание экрана
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Шахматная доска")

    k=0
    g=[]
    i,j=0,0

    # Главный цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif  event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x==0 and y==0:
                    x=0
                    y=0
                elif event.key == pygame.K_RIGHT and x==n-1 and y==n-1:
                    x=n-1
                    y=n-1
                elif event.key == pygame.K_RIGHT and x!=n-1:
                    x+=1
                elif event.key == pygame.K_RIGHT and x==n-1:
                    x=0
                    y+=1
                elif event.key == pygame.K_LEFT and x==0:
                    x=0
                    y-=1
                elif event.key == pygame.K_LEFT and x!=0:
                    x-=1
                elif event.key == pygame.K_SPACE:
                    g.append((x,y))
                    k+=1
                elif event.key==pygame.K_RCTRL:
                    g.append ((x,y))
                    ras(n,l,g)

                

        # Очистка экрана
        screen.fill((0, 0, 0))

        # Отрисовка шахматной доски
        draw_chessboard(screen, n)
        if k>0:
            for h in g:
                draw_red_triangle(screen, CELL_SIZE, h[0],h[1])
                draw_red_circles(screen, CELL_SIZE, h[0], h[1])
        elif k==0:
            draw_red_triangle(screen, CELL_SIZE, x,y)
            draw_red_circles(screen, CELL_SIZE, x, y)
            
        draw_red_triangle(screen, CELL_SIZE, x,y)
        draw_red_circles(screen, CELL_SIZE, x, y)

        # Обновление экрана
        pygame.display.flip()

    # Завершение Pygame
    pygame.quit()






def main():
    def create_new_window():
        # Получение значений из полей ввода
        n = int(entry_n.get())
        l = int(entry_l.get())
        sh_1 (n,l)

    # Создание главного окна
    root = tk.Tk()
    root.title("Расстановка фигур")

    # Создание полей ввода
    label_n = tk.Label(root, text="Размер доски (N):")
    label_n.grid(row=0, column=0, padx=5, pady=5)

    entry_n = tk.Entry(root)
    entry_n.grid(row=0, column=1, padx=5, pady=5)

    label_l = tk.Label(root, text="Количество фигур (L):")
    label_l.grid(row=1, column=0, padx=5, pady=5)

    entry_l = tk.Entry(root)
    entry_l.grid(row=1, column=1, padx=5, pady=5)

    # Создание кнопки
    create_button = tk.Button(root, text="Создать", command=create_new_window)
    create_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    # Запуск главного цикла
    root.mainloop()

if __name__ == '__main__':
        main()


    

