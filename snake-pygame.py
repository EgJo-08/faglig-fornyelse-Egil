
import pygame
from sys import exit
import random

ROWS = 25
COLUMNS = ROWS
TILE_SIZE = 25
GAME_WIDTH = TILE_SIZE * COLUMNS
GAME_HEIGHT = TILE_SIZE * ROWS

GAME_OVER = False

pygame.init()

window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 50)
button_font = pygame.font.Font(None, 35)

# Retry button
retry_button = pygame.Rect(250, 250, 150, 50)


def get_random(limit):
    return random.randint(0, limit - 1) * TILE_SIZE


# Reset game function
def reset_game():
    global snake, food, snake_velocity, GAME_OVER

    snake = []
    snake.append(
        pygame.Rect(
            get_random(COLUMNS),
            get_random(ROWS),
            TILE_SIZE,
            TILE_SIZE
        )
    )

    food = pygame.Rect(
        get_random(COLUMNS),
        get_random(ROWS),
        TILE_SIZE,
        TILE_SIZE
    )

    snake_velocity = (0, 0)
    GAME_OVER = False


# Initial game setup
reset_game()


# Game loop
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            #this checks if the snake is moving in one direction it cant move in another
        if not GAME_OVER and event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_w):
             if snake_velocity != (0, TILE_SIZE):
                snake_velocity = (0, -TILE_SIZE)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
              if snake_velocity != (0, -TILE_SIZE):
                   snake_velocity = (0, TILE_SIZE)
            elif event.key in (pygame.K_LEFT, pygame.K_a):
              if snake_velocity != (TILE_SIZE, 0):
                snake_velocity = (-TILE_SIZE, 0)
            elif event.key in (pygame.K_RIGHT, pygame.K_d):
             if snake_velocity != (-TILE_SIZE, 0):
                snake_velocity = (TILE_SIZE, 0)

        # Retry button click
        if GAME_OVER and event.type == pygame.MOUSEBUTTONDOWN:
            if retry_button.collidepoint(event.pos):
                reset_game()

    # Gameplay
    if not GAME_OVER:

        old_tail = snake[-1].copy()


        # Move snake
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = snake[i - 1].copy()

        snake[0].move_ip(snake_velocity)

        # Check food collision
        if snake[0].center == food.center:
            snake.append(old_tail)
            food = pygame.Rect(
                get_random(COLUMNS),
                get_random(ROWS),
                TILE_SIZE,
                TILE_SIZE
            )

        # Check wall collision
        if not window.get_rect().contains(snake[0]):
            GAME_OVER = True

        # check self collision
        for part in snake[1:]:
            if snake[0].colliderect(part):
                GAME_OVER = True

    # Drawing
    window.fill("black")

    if not GAME_OVER:

        pygame.draw.rect(window, "red", food)

        for snake_part in snake:
            pygame.draw.rect(window, "green", snake_part)
     

    else:

        # Game over text
        lose_text = font.render("YOU LOSE", True, "white")
        lose_rect = lose_text.get_rect(center=(GAME_WIDTH // 2, 200))

        window.blit(lose_text, lose_rect)

        #counter text
        counter_text = font.render(f"Count: {len(snake)}", True, "white")

        # Retry button
        pygame.draw.rect(window, "white", retry_button)

        retry_text = button_font.render("RETRY", True, "black")
        retry_rect = retry_text.get_rect(center=retry_button.center)

        window.blit(retry_text, retry_rect)
       

    pygame.display.update()
    clock.tick(10)
