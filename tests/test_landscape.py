# -*- coding: utf-8 -*-

__author__ = 'Anish Thangalingam'
__email__ = 'anish.thangalingam@nmbu.no'

from biosim.landscape import *

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

def test_animal_weight_loss():


