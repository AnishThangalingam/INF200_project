# -*- coding: utf-8 -*-

__author__ = 'Anish Thangalingam, Majorann Thevarajah'
__email__ = 'anish.thangalingam@nmbu.no, majorann.thevarajah@nmbu.no'

"""
The main class is Landscape and has four subclasses which is: Water, Highland, Lowland and Desert.

"""

from biosim.animals import Animal

class Landscape():
    """
    This is the main class and has four subclasses which is:
    Water, Highland, Lowland and Desert). This Landscape contains two types of animals, Herbivores and
    Carnivores.
    """

    parameters = {}

    def __init__(self):
        """
        Since the population is given in the check sim file we can
        create a empty list for herbivore population and carnivore population. The newborns are calculated from this
        script, so we start the newborn population as an empty list.
        Fixed amount of food f_max is already in the landscape
        """
        self.population_Herbivore = []
        self.population_Carnivore = []
        self.born_in_cell_population_Herbivore = []
        self.born_in_cell_population_Carnivore = []
        self.amount_of_food = 0

    def get_number_of_Herbivores(self):
        """
        Return number of Herbivores in this landscape
        """

        return len(self.population_Herbivore)

    def get_number_of_Carnivores(self):
        """
        Return number of Carnivores in this landscape
        """

        return len(self.population_Carnivore)

    def animal_aging(self):
        """
        Aging is common for both Herbivores and Carnivores, so when we age them, all the
        animals in the landscape age. The animals age one year every year that passes
        """

        for animal in self.population_Herbivore + self.population_Carnivore: #SPØR SABINA
            animal.grows_in_age()

    def animal_death(self):
        """
        Remove the dying animals for both Herbivores and Carnivores, so the animal which remains are
        the newborns and old ones.
        """
        def living_animals(population)
            return [animal for animal in population if not animal.dies()]

        self.population_Carnivore = living_animals(self.population_Carnivore)
        self.population_Herbivore = living_animals(self.population_Herbivore)

    def animal_weight_loss(self):
        """
        Animals losses weight every year, both Herbivores and Carnivores
        This for loop makes all the animal lose weight every year
        """

        for animal in self.population_Herbivore + self.population_Carnivore
            animal.weight_lose()

    def Herbivore_annual_food(self):   #Mat hvertår
        """
        Sets a fixed amount of food every year to a landscape
        """

        self.amount_of_food = self.parameters("f_max")

    def Extend(self):
        """
        Since there should be more than one of the same animal the population will be extended, so the newborns
        will be added to the new population
        """

        Herbivores_count


    def Herbivore_available_food

    def Herbivore_eat(self, food_eaten)
        """
        Calculate the amount of food is left after the animal  and take the amount of food eaten from the fooder, 
        How much food is eaten and calculate how much food is left. 
        """
    def Eaten_Herbivores(self)
        """
        The food grows every year before the herbivores eat, the amount of food growing every year is
        given
        """

class Highland(Landscape):
    parameters = {"f_max": 300}

class Lowland(Landscape):
    parameters = {"f_max": 800}

class Water(Landscape):
    parameters = {"f_max": 0}

class Desert(Landscape):
    parameters = {"f_max": 0}

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