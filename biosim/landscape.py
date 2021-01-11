# -*- coding: utf-8 -*-

__author__ = 'Anish Thangalingam, Majorann Thevarajah'
__email__ = 'anish.thangalingam@nmbu.no, majorann.thevarajah@nmbu.no'

"""
The main class is Landscape and has four subclasses which is: Water, Highland, Lowland and Desert.

"""

from .animals import Herbivore, Carnivore
import operator

class Landscape:
    """
    This is the main class and has four subclasses which is:
    Water, Highland, Lowland and Desert). This Landscape contains two types of animals, Herbivores and
    Carnivores.
    """

    parameters = {}

    @classmethod
    """
    Sets new parameter for the subclasses, because the subclasses
    have different parameters.
    """
    def new_parameter_set(cls, new_parameter):

        for param_name in new_parameter:
            if param_name not in cls.parameters:
                raise KeyError("Invalid parameter name")

        cls.parameter.update(new_parameter)

    def __init__(self):
        """
        Since the population is given in the check sim file we can
        create a empty list for herbivore population and carnivore population. The newborns are calculated from this
        script, so we start the newborn population as an empty list.
        Fixed amount of food f_max is already in the landscape
        """
        self.population_Herbivore = []
        self.population_Carnivore = []
        self.amount_of_food = 0

    def population_set(self, population_list):
    """
    This function sets a population with the given input
    """
    for each_animal in population_list:
        if each_animal['species'] == ['Carnivore']:
            self.population_Carnivore.append(Carnivore(age = each_animal['age'],
                                             weight = each_animal['weight']))

    for each_animal in population_list:
        if each_animal['species'] == ['Herbivore']:
            self.population_Herbivore.append(Herbivore(age = each_animal['age'],
                                             weight = each_animal['weight']))

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

        for herbivore in self.population_Herbivore:
            herbivore.grows_in_age()

        for carnivore in self.population_Herbivore:
            carnivore.grows_in_age()

    def animal_death(self):
        """
        Remove the dying animals for both Herbivores and Carnivores, so the animal which remains are
        the newborns and old ones.
        """
        def living_animals(population):
            return [animal for animal in population if not animal.dies()]

        self.population_Carnivore = living_animals(self.population_Carnivore)
        self.population_Herbivore = living_animals(self.population_Herbivore)

    def animal_weight_loss(self):
        """
        Animals losses weight every year, both Herbivores and Carnivores
        This for loop makes all the animal lose weight every year
        """

        for herbivore in self.population_Herbivore
            herbivore.weight_lose()

        for carnivore in self.population_Herbivore
            carnivore.weight_lose()

    def New_Herbivore_babies(self):
        """
        Since there should be more than one of the same animal the population will be extended, so the newborns
        will be added to the new population
        """

        Herbivores_present_count = self.get_number_of_Herbivores()
        if Herbivores_present_count < 2:
            return False
        else:
            for animal in self.population_Herbivore:
                new_born_weight = animal.birth_and_weight(Herbivores_present_count)
                if new_born_weight is (float or int):
                    self.population_Herbivore.append(
                        Herbivore({'species': "Herbivore", "age": 0, "weight": new_born_weight}))

    def New_Carnivore_babies(self):
        """
        Since there should be more than one of the same animal the population will be extended, so the newborns
        will be added to the new population
        """

        Carnivores_present_count = self.get_number_of_Carnivores()
        if Carnivores_present_count < 2:
            return False
        else:
            for animal in self.population_Carnivore:
                new_born_weight = animal.birth_and_weight(Carnivores_present_count)
                if new_born_weight is (float or int):
                    self.population_Carnivore.append(
                        Carnivore({'species': "Carnivore","age": 0, "weight": new_born_weight}))

    def set_food_parameters(self):
        """
        Sets a fixed amount of food every year to lowland and Highland so the
        Herbivores can eat at those landscapes.
        """
        if type(self) == "Highland":
            self.amount_of_food = self.parameters("f_max")

        if type(self) == "Lowland":
            self.amount_of_food = self.parameters("f_max")

    def Herbivore_available_food(self): #!!!!!!
        """
        Counts available food
        """
        food_amount_needed = Herbivore.parameters["F"]
        Current_food_amount = self.amount_of_food()
        if 0 < self.amount_of_food < food_amount_needed:
            self.amount_of_food = 0
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
        Remove the eaten Herbivore from the herbivores thats going to eat, so the Herbivores, which remains
        are those who have not eaten.
        """

        def Not_eaten_herbivores(population)
            return [animal for animal in population if not animal.eat()]

        self.population_Herbivore = Not_eaten_herbivores(self.population_Herbivore)

    def carnivores_available_food(self):
        """
        Amount of Carnivore food is given by how many Herbivores there are and how much they
        weigh. This is because herbivores are the Carnivores food. So you add all the Herbivores
        weight to the amount of food Carnivores have.

        return: available food for the Carnivore to eat
        """

        food_amount_needed = Carnivore.parameters["F"]
        amount_of_Carnivore_food = 0
        for herbivore in self.population_Herbivore:
            amount_of_Carnivore_food += herbivore.weight
        return amount_of_Carnivore_food
            if food_amount_needed <= amount_of_Carnivore_food:
                amount_of_Carnivore_food -= food_amount_needed
                return food_amount_needed
            else:
                return 0

    def Carnivore_eat(self):
        """
        First sort the Herbivores and Carnivores, so Carnivores with best fitness eat Herbivores with
        low fitness. Carnivore eat from available carnivore food so the eaten amount is taken from what
        carnivore eat.
        :return:
        """

        self.sort_animal_by_fitness(self.population_Carnivore)
        for Carnivore in self.population_Carnivore:
            Carnivore.eat(self.car())

    def animal_migrate(self):
        """
        Legg til kommentar
        """
        Migrated_Herbivores = []
        Migrated_Carnivores = []

        for Herbivore in self.population_Herbivore:
            if Herbivore.possible_for_moving() is True:
                Migrated_Herbivores.append(Herbivore)

        for Carnivore in self.population_Carnivore:
            if Carnivore.possible_for_moving() is True:
                Migrated_Carnivores.append(Carnivore)


class Highland(Landscape):
    parameters = {"f_max": 300}

    def __init__(self):
        super().__init__()

class Lowland(Landscape):
    parameters = {"f_max": 800}

    def __init__(self):
        super().__init__()

class Water(Landscape):

    def __init__(self):
        super().__init__()

class Desert(Landscape):

    def __init__(self):
        super().__init__()



