# -*- coding: utf-8 -*-

__author__ = 'Anish Thangalingam'
__email__ = 'anish.thangalingam@nmbu.no'

from biosim.landscape import Landscape

def test_get_number_of_Herbivores():
    """
    Tests if it checks amount of Herbivores in the island
    """
    population = [{'species': 'Herbivores', 'age': 8, 'weight': 13},
                  {'species': 'Herbivores', 'age': 4, 'weight': 11},
                  {'species': 'Herbivores', 'age': 7, 'weight': 24}]

    population_Herbivores = 3

    assert Landscape.get_number_of_Herbivores(population) == population_Herbivores

def test_get_number_of_Carnivores():
    """
    Tests if it checks amount of Herbivores in the island
    """
    population = [{'species': 'Carnivores', 'age': 8, 'weight': 13},
                  {'species': 'Carnivores', 'age': 4, 'weight': 11},
                  {'species': 'Carnivores', 'age': 7, 'weight': 24}]

    population_Carnivores = 3

    assert Landscape.get_number_of_Carnivores(population) == population_Carnivores

def test_animal_aging():
    """
    Tests if the animals are aging by one year every year
    """
    present_animal_age = 5
    aged_animal_age = 6
    assert animal_aging(present_animal_age) == aged_animal_age

def test_animal_death():
    """

    """


def animal_death(self):
        """
        Remove the dying animals for both Herbivores and Carnivores, so the animal which remains are
        the newborns and old ones.
        """
        def living_animals(population)
            return [animal for animal in population if not animal.dies()]

        self.population_Carnivore = living_animals(self.population_Carnivore)
        self.population_Herbivore = living_animals(self.population_Herbivore)




def test_animal_weight_loss():


