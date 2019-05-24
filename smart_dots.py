"""
This is a AI tutorial form:
https://www.youtube.com/watch?v=BOZfhUcNiqk&t=41s

The dots will try to reach the goal as quickly as possible.
But they learn randomly.

There might / will be some modifictations over the code from the tutorial.
"""

import pygame

import gameworld
import population
# import dot

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
GAMEDISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption(f"Smart Dots")
CLOCK = pygame.time.Clock()
BACKGROUND = pygame.Surface(GAMEDISPLAY.get_size())
BACKGROUND = BACKGROUND.convert()
BACKGROUND.fill(WHITE)

GOAL_X, GOAL_Y = 1100, 360
GWORLD = gameworld.GameWorld(DISPLAY_WIDTH, DISPLAY_HEIGHT, GOAL_X, GOAL_Y)
GWORLD.add_wall([200, 0, 10, 500])
# GWORLD.add_wall([500, 220, 10, 500])
# GWORLD.add_wall([800, 0, 10, 500])
TEST = population.Population(GWORLD, [100, DISPLAY_HEIGHT / 2], 1000)
print(f"Starting generation 1")

GAME_QUIT = False

while not GAME_QUIT:

    GAMEDISPLAY.blit(BACKGROUND, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_QUIT = True
        else:
            pass
            # print(event)

    if TEST.alldotsdead():
        TEST.calculatefitness()
        TEST.naturalselection()
        TEST.mutatedembabies()

    GWORLD.showgoal(GAMEDISPLAY)
    GWORLD.showwalls(GAMEDISPLAY)

    TEST.update()
    TEST.show(GAMEDISPLAY)

    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
quit()
