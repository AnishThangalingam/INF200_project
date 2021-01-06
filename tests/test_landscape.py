# -*- coding: utf-8 -*-

__author__ = 'Anish Thangalingam'
__email__ = 'anish.thangalingam@nmbu.no'

from biosim.landscape import *

def test_get_number_of_Herbivores(self):
    """
    Return number of Herbivores in this landscape
    """
    self.population_Herbivore = [2]

    assert get_number_of_Herbivores(self.population_Herbivore) == 2


