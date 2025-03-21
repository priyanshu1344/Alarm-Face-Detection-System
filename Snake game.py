import pygame
import random

pygame.init()

# Set up display
screen_width = 640
screen_height = 480
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake and food properties
block_size = 20
snake_speed = 5

# Fonts
font = pygame.font.SysFont(None, 40)

# Initialize clock
clock = pygame.time.Clock()

# Define directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def draw_snake(snake_list):
    for segment in snake_list:
        pygame.draw.rect(win, green, (segment[0], segment[1], block_size, block_size))

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    win.blit(text_surface, (x, y))

def game_loop():
    game_over = False
    game_close = False

    # Initial snake position and direction
    lead_x = screen_width // 2
    lead_y = screen_height // 2
    lead_x_change = block_size
    lead_y_change = 0

    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
    food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size

    score = 0
    highest_score = 0

    while not game_over:

        while game_close:
            win.fill(white)
            draw_text("Game Over! Press C to Play Again or Q to Quit", red, 50, 200)
            draw_text("Highest Score: " + str(highest_score), red, 220, 250)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and lead_x_change == 0:
                    lead_x_change = -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT and lead_x_change == 0:
                    lead_x_change = block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP and lead_y_change == 0:
                    lead_y_change = -block_size
                    lead_x_change = 0
                if event.key == pygame.K_DOWN and lead_y_change == 0:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= screen_width or lead_x < 0 or lead_y >= screen_height or lead_y < 0:
            game_close = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        win.fill(white)

        pygame.draw.rect(win, red, (food_x, food_y, block_size, block_size))

        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True 

        draw_snake(snake_list)

        draw_text("Score: " + str(score), green, 10, 10)

        pygame.display.update()

        if lead_x == food_x and lead_y == food_y:
            food_x = round(random.randrange(0, screen_width - block_size) / block_size) * block_size
            food_y = round(random.randrange(0, screen_height - block_size) / block_size) * block_size
            snake_length += 1
            score += 10

            if score > highest_score:
                highest_score = score

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
