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

    def Herbivore_annual_food(self):
        """
        Sets a fixed amount of food every year to a landscape
        """

        self.amount_of_food = self.parameters("f_max")

    def Extend(self):
        """
        Since there should be more than one of the same animal the population will be extended, so the newborns
        will be added to the new population
        """

        Herbivores_present_count = self.get_number_of_Herbivores():
        for animal in self.population_Herbivore[:Herbivores_present_count]:
            Born_new_weight = animal.birth_and_weight(Herbivores_present_count)
            if Born_new_weight is float:
                self.population_Herbivore.append(
                    Herbivore({"age": 0, "weight": Born_new_weight})
                )

    def Herbivore_available_food(self): #!!!!!!
        """
        Counts available food
        """
        food_amount_needed = Herbivore.parameters["F"]
        Current_food_amount = self.amount_of_food()
        if 0 < self.amount_of_food < food_amount_needed:
            self.amount_of_food=0
            return Current_food_amount
        elif food_amount_needed >= self.amount_of_food:
            self.amount_of_food -= food_amount_needed
            return food_amount_needed
        else:
            return 0

    def Herbivore_eat(self):
        """
        Calculate the amount of food is left after the animal  and take the amount of food eaten from the fooder, 
        How much food is eaten and calculate how much food is left. 
        """

        for Herbivore in self.population_Herbivore:
            Herbivore.eat(self.Herbivore_available_food())

    def Eaten_Herbivores(self):
        """
        Remove the eaten Herbivores, so that the herbivores that has not eaten gets to
        eat
        """





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

