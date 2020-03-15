"""
This is the barin of the dot(s).
"""

import random
import math


class Brain:
    """
    A brain.
    """

    def __init__(self, size):
        """
        Create a brain (wow).
        """
        self.directions = []
        self.step = 0
        self.size = size

        self.__randomize(size)

    def __randomize(self, size):
        """
        Create random instructions for the dot.
        """
        for _ in range(size):
            random_angle = random.random() * 2 * math.pi
            x_part = math.cos(random_angle)
            y_part = math.sin(random_angle)
            self.directions.append([x_part, y_part])

    def clone(self):
        """
        Clone this brain to make a new one (wow).
        """
        newbrain = Brain(self.size)
        for i in range(self.size):
            newbrain.directions[i] = self.directions[i]
        return newbrain

    def mutate(self):
        """
        Mutation by radiation.
        Or whatever sets the random value on this pc.
        """
        mutationrate = 0.01  # 1% chance for each direction to be overwritten
        for i in range(self.size):
            rand = random.random()
            if rand < mutationrate:
                random_angle = random.random() * 2 * math.pi
                x_part = math.cos(random_angle)
                y_part = math.sin(random_angle)
                self.directions[i] = [x_part, y_part]


if __name__ == '__main___':
    print("Please run smart__dots.py as main.")
