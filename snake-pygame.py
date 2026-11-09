import pygame
from sys import exit #terminate the programe
import random

from turtledemo.bytedesign import clock

ROWS = 25
COLUMNS = ROWS
TILE_SIZE = 25
GAME_WIDTH = TILE_SIZE * COLUMNS
GAME_HEIGHT = TILE_SIZE * ROWS

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("snake")
clock = pygame.time.Clock() #brugt for frame rate

def get_random(limit):
    return random.randint(0, limit -1) * TILE_SIZE

food = pygame.Rect(get_random(COLUMNS), get_random(ROWS), TILE_SIZE, TILE_SIZE)

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(window, "red", food)
    pygame.display.update()
    clock.tick(10)