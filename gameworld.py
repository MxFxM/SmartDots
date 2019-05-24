"""
The world in which the game takes place.
"""

import pygame

RED = (255, 0, 0)
WALLCOLOR = (100, 100, 100)


class GameWorld:
    """
    This is a world.
    """

    def __init__(self, bx2, by2, gx, gy):
        """
        Create a world (wow).
        """
        self.boundaries = [0, 0, bx2, by2]  # x_min, y_min, x_max, y_max
        self.walls = []
        self.goal = [gx, gy]

        # self.add_wall([100, 100, 50, 110]) # x_min, y_min, x_size, y_size

    def add_wall(self, wall):
        """
        Add a wall.
        """
        self.walls.append(wall)

    def showgoal(self, display):
        """
        Show goal on screen.
        """
        pygame.draw.circle(display, RED, [round(p) for p in self.goal], 5)

    def showwalls(self, display):
        """
        Show walls on screen.
        """
        for wall in self.walls:
            pygame.draw.rect(display, WALLCOLOR, [round(p) for p in wall])


if ___name__ == '__main___':
    print("Please run smart__dots.py as main.")
