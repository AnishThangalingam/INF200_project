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
    def new_parameter_set(cls, new_parameter):
        """
        Sets new parameter for the subclasses, because the subclasses
        have different parameters.
        """
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

    def set_a_population(self, population_list):
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

    def new_herbivore_babies(self):
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

    def new_carnivore_babies(self):
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

    def set_food_parameters(self): ####
        """
        Sets a fixed amount of food every year to lowland and Highland so the
        Herbivores can eat at those landscapes.
        """

        self.amount_of_food = self.parameters["f_max"]

    def herbivore_eat(self): ########
        """
        Calculate the amount of food is left after the animal  and take the amount of food eaten from the fooder,
        How much food is eaten and calculate how much food is left.
        """

        for herbivore in self.population_Herbivore:
            if  self.amount_of_food >= herbivore.parameters["F"]:
                herbivore.eat(herbivore.parameters["F"])
                self.amount_of_food -= herbivore.parameters["F"]
            else:
                self.amount_of_food = 0


        #### Husk at dyrene spiser selvom mengden er 5 og de spiser 10


    def carnivore_eat(self): #####
        """
        First sort the Herbivores and Carnivores, so Carnivores with best fitness eat Herbivores with
        low fitness. Carnivore eat from available carnivore food so the eaten amount is taken from what
        carnivore eat.
        :return:
        """

        self.population_Herbivore.sort(key=operator.attrgetter('fitness'))
        self.population_Carnivore.sort(key=operator.attrgetter('fitness'), reverse=True)

        for carnivore in self.population_Carnivore:
            carnivore.eat(self.population_Herbivore)

    def killed_herbivore(self): ########
        """
        remove the killed herbivore from the carnivore eat
        :return:
        """
        def not_killed_by_carnivore(population):
            return [carnivore for carnivore in population if not carnivore.probability_to_kill() is True]

        self.population_Herbivore = not_killed_by_carnivore(self.population_Herbivore)

    def animal_migrate(self):
        """
        Remove killed animals, so the herbivores which remains are the ones
        that have not been killed or eaten.
        """

        Migrated_Herbivores = []
        Migrated_Carnivores = []

        for herbivore in self.population_Herbivore:
            if herbivore.possible_for_moving() is True:
                Migrated_Herbivores.append(herbivore)

        for carnivore in self.population_Carnivore:
            if carnivore.possible_for_moving() is True:
                Migrated_Carnivores.append(carnivore)

##Går dette for hvert år


class Highland(Landscape):
    parameters = {"f_max": 300}

    def __init__(self):
        super().__init__()

class Lowland(Landscape):
    parameters = {"f_max": 800}

    def __init__(self):
        super().__init__()

class Water(Landscape):
    parameters = {"f_max": 0}
### Den kan ikke gå her, så må sette inn noe
    def __init__(self):
        super().__init__()

class Desert(Landscape):
    parameters = {"f_max": 0}
    def __init__(self):
        super().__init__()

### Vis denne vann kan ikke gås på