# -*- coding: utf-8 -*-

__author__ = 'Anish Thangalingam, Majorann Thevarajah'
__email__ = 'anish.thangalingam@nmbu.no, majorann.thevarajah@nmbu.no'

"""
The main class is Landscape and has four subclasses which is: Water, Highland, Lowland and Desert)

"""

from biosim.animals import herbivores

class Landscape():
    """
    This is the main class and has four subclasses which is:
    Water, Highland, Lowland and Desert)

    """

    parameters = {}

"""
Got to find out the population in each landscape to know how many species each landscape will have
the animal. The parameters is not mentioned in the landscape class, but in the subclasses we have an amount 
of food which the animal gets every year.  


Population
Fitness, the weakest will get eaten first
fodder
calculated population
"""
# De ulike funksjonene
# Mengden mat og bestemt mat hvert år. 300 fmax hvert år
# Population
# Fodder
# Amount

    def __init__(self):
        self.population_Herbivore = []
        self.population_Carnivore = []
        self.born_in_cell_population_Herbivore = []
        self.born_in_cell_population_Carnivore = []
        self.amount_of_food = 0

    def amount_of_food()


    def herbivore_eat(self, food_eaten)
        """
        Calculate the amount of food is left after the animal  and take the amount of food eaten from the fooder, 
        How much food is eaten and calculate how much food is left. 
        """
        self.food_count -= food_eaten
        self.amount_of_food = self.get_amount_of_food()

    def Herbivores_food(self)
        """
        The food grows every year before the herbivores eat, the amount of food growing every year is
        given
        """
        self.amount_of_food = cls.parameters[f_max]



    #spørs hvor mange det er og hvis det blir født flere
    def food_gone


    #mat som er spist blir jo borte
    def remove eaten herbivores


class Highland(Landscape):
    parameters = {"f_max": 300}

class Lowland(Landscape):
    parameters = {"f_max": 800}

class Water(Landscape):
    parameters = {"f_max": 0}

class Desert(Landscape):
    parameters = {"f_max": 0}
