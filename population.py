"""
A bunch of dots.
"""

import random

import dot
# import gameworld


class Population:
    """
    A bunch of dots.
    """

    def __init__(self, gameWorld, startpos, size):
        """
        Creat a bunch of dots.
        """
        self.dots = []
        self.gworld = gameWorld
        self.startpos = startpos
        self.size = size
        self.fitnesssum = 0
        self.generation = 1
        self.bestdot = 0
        self.maxsteps = 400
        for _ in range(size):
            self.dots.append(dot.Dot(self.gworld, self.startpos))

    def update(self):
        """
        Update all dots in the population.
        """
        for nextdot in self.dots:
            if nextdot.brain.step > self.maxsteps:
                nextdot.dead = True
            else:
                nextdot.update()

    def show(self, display):
        """
        Show all dots in the population.
        """
        for nextdot in self.dots:
            nextdot.show(display)

    def calculatefitness(self):
        """
        Calculate the fitness for all dots in the population.
        """
        self.fitnesssum = 0
        for nextdot in self.dots:
            self.fitnesssum = self.fitnesssum + nextdot.calculate_fitness()

    def alldotsdead(self):
        """
        Return wheter all the dots are dead or not.
        """
        for nextdot in self.dots:
            if not nextdot.dead and not nextdot.reachedgoal:
                return False
        return True

    def naturalselection(self):
        """
        Create new population,
        select a parent (one parent is enough lol),
        make a babie.
        """
        newdots = []
        self.setbestdot()
        newdots.append(self.dots[self.bestdot].gimme_baby())
        newdots[0].wasbestdot = True
        for _ in range(self.size - 1):
            parent = self.selectparent()
            newdots.append(parent.gimme_baby())
        self.dots = newdots
        self.generation = self.generation + 1
        print(f"Starting generation {self.generation}")

    def mutatedembabies(self):
        """
        Mutate the new children to be better (or worse).
        """
        for nextdot in self.dots[1:]:
            nextdot.brain.mutate()

    def selectparent(self):
        """
        Select a parent.
        Fitter parents are more likely to get a child.
        """
        rand = random.random() * self.fitnesssum
        runningsum = 0
        for nextdot in self.dots:
            runningsum = runningsum + nextdot.fitness
            if runningsum >= rand:
                return nextdot
        # should not be here
        print("FEHLER BEI SELECT PARENT")
        return self.dots[0]

    def setbestdot(self):
        """
        Finds the dot with the highest fitness.
        """
        best = 0
        bestindex = 0
        for i in range(self.size):
            if self.dots[i].fitness > best:
                best = self.dots[i].fitness
                bestindex = i
        self.bestdot = bestindex
        if self.dots[bestindex].reachedgoal:
            self.maxsteps = self.dots[bestindex].brain.step


if __name__ == '__main___':
    print("Please run smart__dots.py as main.")
