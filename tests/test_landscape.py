# -*- coding: utf-8 -*-

__author__ = 'Anish Thangalingam'
__email__ = 'anish.thangalingam@nmbu.no'

from biosim.landscape import Landscape, Highland, Lowland, Water, Desert


def test_get_number_of_Herbivores():
    """
    Tests if it checks amount of Herbivores in the island
    """
    population = [{'species': 'Herbivore', 'age': 8, 'weight': 13},
                  {'species': 'Herbivore', 'age': 4, 'weight': 11},
                  {'species': 'Herbivore', 'age': 7, 'weight': 24}]

    lowland = Lowland()
    lowland.set_a_population(population)
    Test = lowland.get_number_of_Herbivores()

    assert Test == 3


def test_get_number_of_Carnivores():
    """
    Tests if it checks amount of Herbivores in the island
    """
    population = [{'species': 'Carnivore', 'age': 8, 'weight': 13},
                  {'species': 'Carnivore', 'age': 4, 'weight': 11},
                  {'species': 'Carnivore', 'age': 7, 'weight': 24}]

    highland = Highland()
    highland.set_a_population(population)
    Test = highland.get_number_of_Carnivores()

    assert Test == 3
