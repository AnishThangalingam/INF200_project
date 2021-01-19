# -*- coding: utf-8 -*-

__author__ = 'Anish Thangalingam'
__email__ = 'anish.thangalingam@nmbu.no'

from biosim.landscape import *

def test_get_number_of_Herbivores():
    """
    Tests if it checks amount of Herbivores in the island
    """
    population.Herbivores = 5

    assert get_number_of_Herbivores(population.Herbivores) == population.Herbivores


def test_get_number_of_Herbivores():
    """
    Tests if it checks amount of Herbivores in the island
    """
    population.Carnivores = 5

    assert get_number_of_Carnivores(population.Carnivores) == population.Carnivores

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


