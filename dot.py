"""
This is the basic dot.
"""

import math
import pygame

# import gameworld
import brain

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)


class Dot:
    """
    A dot.
    """

    def __init__(self, gameworld, startpos):
        """
        Create a dot
        """
        self.startpos = startpos
        self.pos = startpos
        self.vel = [0, 0]
        self.acc = [0, 0]
        self.brain = brain.Brain(400)
        self.max_speed = 5
        self.gameworld = gameworld
        self.dead = False
        self.reachedgoal = False
        self.fitness = 0
        self.wasbestdot = False

    def move(self):
        """
        Moves the dot.
        """
        # when available, get next instruction from brain, otherwise, die
        if len(self.brain.directions) > self.brain.step:
            self.acc = self.brain.directions[self.brain.step]
            self.brain.step = self.brain.step + 1
        else:
            self.dead = True
        # veloctiy changes with acceleration
        self.vel = [v+a for v, a in zip(self.vel, self.acc)]
        # limit maximum speed
        speed = math.sqrt(self.vel[0]**2 + self.vel[1]**2)
        if speed > self.max_speed:
            factor = speed / self.max_speed
            self.vel = [v/factor for v in self.vel]
        # position changes with velocity
        self.pos = [round(p+v) for p, v in zip(self.pos, self.vel)]

    def show(self, display):
        """
        Draws the dot on the screen.
        """
        if not self.wasbestdot:
            pygame.draw.circle(display, BLACK, self.pos, 2)
        else:
            pygame.draw.circle(display, GREEN, self.pos, 5)

    def update(self):
        """
        Moves, then checks for events: death by boundary
        """
        if not self.dead and not self.reachedgoal:
            self.move()
            if self.pos[0] < self.gameworld.boundaries[0] or \
                    self.pos[0] > self.gameworld.boundaries[2] or \
                    self.pos[1] < self.gameworld.boundaries[1] or \
                    self.pos[1] > self.gameworld.boundaries[3]:
                self.dead = True
            if math.sqrt((self.gameworld.goal[0] - self.pos[0])**2
                         + (self.gameworld.goal[1] - self.pos[1])**2) < 5:
                self.reachedgoal = True
            for wall in self.gameworld.walls:
                if self.pos[0] > wall[0] and \
                        self.pos[0] < wall[0] + wall[2] and \
                        self.pos[1] > wall[1] and \
                        self.pos[1] < wall[1] + wall[3]:
                    self.dead = True

    def calculate_fitness(self):
        """
        Fitness is distance to goal inverted, because closer is better.
        Also it is squared to boost very close over just close.
        """
        if not self.reachedgoal:
            distancetogoal = math.sqrt((self.gameworld.goal[0] - self.pos[0])**2
                                       + (self.gameworld.goal[1] - self.pos[1])**2)
            self.fitness = 1.0 / distancetogoal**2
        else:
            self.fitness = 1 + 10000.0 / self.brain.step**2
        return self.fitness

    def gimme_baby(self):
        """
        Clone the brain.
        Usually here would be crossover = mixing of 2 brains.
        """
        baby = Dot(self.gameworld, self.startpos)
        baby.brain = self.brain.clone()
        return baby


if __name__ == '__main___':
    print("Please run smart__dots.py as main.")
