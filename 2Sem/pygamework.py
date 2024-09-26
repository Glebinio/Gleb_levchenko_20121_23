import pygame
import random

# Инициализация Pygame
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Лови кружки!")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Платформа
platform_width = 100
platform_height = 20
platform_x = WIDTH // 2 - platform_width // 2
platform_y = HEIGHT - platform_height - 10

# Кружки
circle_radius = 15
circles = []

# Скорость кружков и платформы
circle_speed = 0.2
platform_speed = 1
has_falling_circle = False

# Счет
score = 0
font = pygame.font.Font(None, 36)

# Флаг игры
running = True

# Функция для создания нового кружка
def create_circle():
    x = random.randint(circle_radius, WIDTH - circle_radius)
    y = 0
    circles.append([x, y])


def game_over_screen(score):
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 


        screen.fill(WHITE)


        text = font.render("Игра закончена", True, BLACK)
        text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
        screen.blit(text, text_rect)

        score_text = font.render(f"Ваш счет: {score}", True, BLACK)
        score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
        screen.blit(score_text, score_rect)

        pygame.display.flip()
    pygame.quit
# Основной цикл игры
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение платформы
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform_x > 0:
        platform_x -= platform_speed
    if keys[pygame.K_RIGHT] and platform_x + platform_width < WIDTH:
        platform_x += platform_speed

    # Движение кружков и проверка столкновений
    for i in range(len(circles) - 1, -1, -1):  
        circle = circles[i]
        circle[1] += circle_speed

        platform_rect = pygame.Rect(platform_x, platform_y, platform_width, platform_height)
        circle_rect = pygame.Rect(circle[0] - circle_radius, circle[1] - circle_radius, circle_radius * 2, circle_radius * 2)

        if platform_rect.colliderect(circle_rect):
            circles.pop(i) 
            score += 1
        elif circle[1] > HEIGHT:
            circles.pop(i)
            # Игра окончена
            game_over_screen(score)
            running = False
            break  

    # Создание новых кружков
    if not circles:
        create_circle()
    


    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (platform_x, platform_y, platform_width, platform_height))
    for circle in circles:
        pygame.draw.circle(screen, BLACK, circle, circle_radius)

    # Отображение счета
    text = font.render(f"Счет: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()