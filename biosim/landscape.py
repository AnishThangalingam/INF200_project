# -*- coding: utf-8 -*-
"""
This script contains a main class called landscape and four subclasses called
Highland, Lowland, Desert and Water. The main class contains characteristics that are common
to the Highland, Lowland, Desert and Water.

Purpose of this function is to give detailed information about the landscape and
what happens inside every landscape. Then use this information about the different cells
create a map in the island script.

To use this script the user has to have installed the random and operator
package to the Python environment.
"""

__author__ = 'Anish Thangalingam & Majorann Thevarajah'
__email__ = 'anish.thangalingam@nmbu.no & majorann.thevarajah@nmbu.no'


from biosim.animals import Herbivore, Carnivore
import operator
import random


class Landscape:
    """
    Landscape class is the base class for this script
    """

    parameters = {}

    @classmethod
    def new_parameter_set(cls, new_parameter):
        """
        This function sets new parameter for the subclasses, because the subclasses
        have different parameters. The function updates the parameter
        """
        for param_name in new_parameter:
            if param_name not in cls.parameters:
                raise KeyError("Invalid parameter name")

        cls.parameters.update(new_parameter)

    def __init__(self):
        """
        In this function we create an empty list for the population, and updates the population.
        The amount of food is given as 0, which will updated.
        """
        self.population_herbivore = []
        self.population_carnivore = []
        self.amount_of_food = 0

    def set_a_population(self, population_list):
        """
        This function sets a population for the given population list, it adds carnivore to carnivore
        population and herbivore to herbivore population

        :param: population_list, a list with species
        """
        for each_animal in population_list:
            if each_animal["species"] == "Carnivore":
                self.population_carnivore.append(Carnivore(age=each_animal["age"],
                                                           weight=each_animal["weight"]))

        for each_animal in population_list:
            if each_animal["species"] == "Herbivore":
                self.population_herbivore.append(Herbivore(age=each_animal["age"],
                                                           weight=each_animal["weight"]))

    def get_number_of_herbivores(self):
        """
        This function gives us the number of herbivores in the population

        :return: number of herbivores
        """

        return len(self.population_herbivore)

    def get_number_of_carnivores(self):
        """
        This function gives us the number of carnivores in the population

        :return: number of carnivores
        """

        return len(self.population_carnivore)

    def animal_aging(self):
        """
        Aging is common for both Herbivores and Carnivores, so when we age them, all the
        animals in the landscape age. The animals age one year for every year that passes.
        """

        for herbivore in self.population_herbivore:
            herbivore.grows_in_age()

        for carnivore in self.population_carnivore:
            carnivore.grows_in_age()

    def animal_death(self):
        """
        Remove the dying animals for both Herbivores and Carnivores, so that the animals which remains are the
        living animals.

        :return: the living animals
        """

        def living_animals(population):
            return [animal for animal in population if not animal.death()]

        self.population_carnivore = living_animals(self.population_carnivore)
        self.population_herbivore = living_animals(self.population_herbivore)

    def animal_weight_loss(self):
        """
        Animals losses weight every year, both Herbivores and Carnivores. These for loops makes
        both the herbivores and carnivores to lose weight every year.
        """

        for herbivore in self.population_herbivore:
            herbivore.weight_lose()

        for carnivore in self.population_carnivore:
            carnivore.weight_lose()

    def new_herbivore_babies(self):
        """
        There will be born new animals so if there is more than two animals, a new animal can be born.
        So if a animal is born it will be added to the empty list of newborn herbivores. So the population
        will extend with the list of newborn herbivores.
        """
        newborn_herbivores = []

        herbivores_present_count = self.get_number_of_herbivores()
        if herbivores_present_count < 2:
            return False

        if herbivores_present_count >= 2:
            for animal in self.population_herbivore:
                new_born_baby = animal.baby(herbivores_present_count)
                if new_born_baby is not None:
                    newborn_herbivores.append(new_born_baby)
        self.population_herbivore.extend(newborn_herbivores)

    def new_carnivore_babies(self):
        """
        There will be born new animals so if there are more than two animals, a new animal can be born.
        So if a animal is born it will be added to the empty list of newborn carnivores. So the population
        will extend with the list newborn carnivores.
        """
        newborn_carnivores = []

        carnivores_present_count = self.get_number_of_carnivores()
        if carnivores_present_count < 2:
            return False

        if carnivores_present_count >= 2:
            for animal in self.population_carnivore:
                new_born_baby = animal.baby(carnivores_present_count)
                if new_born_baby is not None:
                    newborn_carnivores.append(new_born_baby)
        self.population_carnivore.extend(newborn_carnivores)

    def set_food_parameters(self):
        """
        Sets a fixed amount of food every year to lowland and Highland so the
        Herbivores can eat at those landscapes.
        """

        self.amount_of_food = self.parameters["f_max"]

    def herbivore_eat(self):
        """
        The herbivore eats in random order and will eat the required amount of food need, but
        they will eat even if the amount of food is less than the required amount of food. The amount of food
        is updated, so that its reduced for every time the herbivores eat.
        """
        random.shuffle(self.population_herbivore)
        for herbivore in self.population_herbivore:
            if self.amount_of_food >= herbivore.parameters["F"]:
                herbivore.eat(herbivore.parameters["F"])
                self.amount_of_food -= herbivore.parameters["F"]
            else:
                herbivore.eat(self.amount_of_food)
                self.amount_of_food = 0

    def carnivore_eat(self):
        """
        First sort the Herbivores and Carnivores, so Carnivores with best fitness eat Herbivores with
        lowest fitness. Then update the list so that the population of herbivore that remains are the
        ones that are not killed by carnivores.
        """

        self.population_herbivore.sort(key=operator.attrgetter('fitness'))
        self.population_carnivore.sort(key=operator.attrgetter('fitness'), reverse=True)

        for carnivore in self.population_carnivore:
            updated_herbivore_population = carnivore.carnivore_eat(self.population_herbivore)
            self.population_herbivore = updated_herbivore_population

    def animal_migrate(self):
        """
        Animals does not stay in one place forever, it will move around in the island. So if it moves
        it will be added to the list of herbivores and carnivores that have migrated.

        :return: lists, lists of which animals that have migrated
        """

        migrated_herbivores = []
        migrated_carnivores = []

        for herbivore in self.population_herbivore:
            if herbivore.possible_for_moving() is True:
                migrated_herbivores.append(herbivore)

        for carnivore in self.population_carnivore:
            if carnivore.possible_for_moving() is True:
                migrated_carnivores.append(carnivore)

        return migrated_herbivores, migrated_carnivores


class Highland(Landscape):
    """
    Highland class is a subclass to the Landscape class
    """
    parameters = {"f_max": 300}
    flag = True

    def __init__(self):
        """
        Initializing the Highland class
        """
        super().__init__()


class Lowland(Landscape):
    """
    Lowland class is a subclass to the Landscape class
    """
    parameters = {"f_max": 800}
    flag = True

    def __init__(self):
        """
        Initializing the Lowland class
        """
        super().__init__()


class Water(Landscape):
    """
    Water class is a subclass to the Landscape class
    flag is False, since animals can not move on water
    """
    parameters = {"f_max": 0}
    flag = False

    def __init__(self):
        """
        Initializing the Water class
        """
        super().__init__()


class Desert(Landscape):
    """
    Desert class is a subclass to the Landscape class
    """
    parameters = {"f_max": 0}
    flag = True

    def __init__(self):
        """
        Initializing the Desert class
        """
        super().__init__()
