class sh2:

    def __init__(self,i_g,n,shh):
        self.i_g= i_g
        self.n=n
        self.shh=shh

        # Цвета
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.SCREEN_WIDTH = 600
        self.SCREEN_HEIGHT = 400
        self.CELL_COUNT_X = self.n
        self.CELL_COUNT_Y = self.n
        self.CELL_SIZE = self.SCREEN_WIDTH // self.CELL_COUNT_X


    

    def button_clicked(self):
        with open("C:\sha\out.txt", "w") as f:
            if not len(self.i_g):
                f.write("no solutions")
            else:
                f.writelines(f"{str(i)} " for i in self.i_g)
                f.writelines('\n')


    
    def draw_chessboard(self,screen):
        for y in range(self.n):
            for x in range(self.n):
                color = self.WHITE if (x + y) % 2 == 0 else self.BLACK
                rect = pygame.Rect(x * self.CELL_SIZE, y * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE)
                pygame.draw.rect(screen, color, rect)



    def draw_red_triangle(self,screen, cell_size, x, y):

        points = [
            (x * cell_size + cell_size / 2, y * cell_size),
            (x * cell_size, y * cell_size + cell_size),
            (x * cell_size + cell_size, y * cell_size + cell_size / 2),
        ]

        # Определение цвета треугольника
        color = (255, 0, 0)  # Красный

        # Отрисовка треугольника
        pygame.draw.polygon(screen, color, points)
    
    def draw_yelow_triangle(self,screen, cell_size, x, y):

        points = [
            (x * cell_size + cell_size / 2, y * cell_size),
            (x * cell_size, y * cell_size + cell_size),
            (x * cell_size + cell_size, y * cell_size + cell_size / 2),
        ]

        # Определение цвета треугольника
        color = (255, 255, 0)  # Красный

        # Отрисовка треугольника
        pygame.draw.polygon(screen, color, points)

    def draw_red_circles(self,screen, cell_size, x, y):

        center_x = (x + 0.5) * cell_size
        center_y = (y + 0.5) * cell_size

        # Радиус кружочков
        radius = cell_size // 4

        # Расстановка кружочков по соседним клеткам
        for dx, dy in [(0, 1), (0, 2), (0, -1), (0, -2), (1, 0), (2, 0), (-1, 0), (-2, 0),(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]:
            new_x = dx+center_x + (dx) * cell_size
            new_y = dx+ center_y + (dy) * cell_size
            pygame.draw.circle(screen, (0,0,255), (new_x,new_y),  radius, width=0)




    def otr (self):

        # Инициализация Pygame
        pygame.init()

        # Размер экрана
        
        # Цвета
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        SCREEN_WIDTH = 600
        SCREEN_HEIGHT = 400
        CELL_COUNT_X = self.n
        CELL_COUNT_Y = self.n
        CELL_SIZE = SCREEN_WIDTH // CELL_COUNT_X
        
        screen_width = self.n * CELL_SIZE
        screen_height = self.n * CELL_SIZE


        # Размер клетки
        x = 0  # Координата X клетки (0-based)
        y = 0  # Координата Y клетки (0-based)
        # Создание двумерного массива 3x3 с помощью list comprehension
        figure_positions = [[False for j in range(self.n)] for i in range(self.n)]

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
                        self.button_clicked()

                    

            # Очистка экрана
            screen.fill((0, 0, 0))

            # Отрисовка шахматной доски
            
            self.draw_chessboard(screen)
            for h in self.i_g:
                self.draw_yelow_triangle(screen, CELL_SIZE, h[0],h[1])
                self.draw_red_circles(screen, CELL_SIZE, h[0], h[1])
            for h in self.shh:
                self.draw_red_triangle(screen, CELL_SIZE, h[0], h[1])


            rect = pygame.Rect(screen_width, 0, 400, screen_height)
            pygame.draw.rect(screen, (128,128,128), rect)
            # Отрисовка кнопки
            pygame.draw.rect(screen, (0, 145, 0), button_rect)

            screen.blit(text, text_rect)

            # Обновление экрана
            pygame.display.flip()

        # Завершение Pygame
        pygame.quit()
