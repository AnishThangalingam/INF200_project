# -*- encoding: utf-8 -*-

__author__ = "Majorann Thevarjah & Anish Thangalingam"
__email__ = "Majorann.thevarajah@nmbu.no & Anish.thangalingam@nmbu.no"

from biosim.animals import Herbivore, Carnivore


def test_parameter_set():
    """
    Testing the parameter_set function are able to update parameters
    """

    new_parameters = {"a_half": 100, "F": 2}
    present_parameters = Herbivore.parameters
    new_parameters = Herbivore.parameter_set(new_parameters)
    assert present_parameters is not new_parameters


def test_weight_at_birth():
    """
    Testing if the animals weight at birth is higher than 0 when
    we start by inserting None.
    """
    herbivore = Herbivore(0, None)
    assert herbivore.weight > 0

    carnivore = Carnivore(0, None)
    assert carnivore.weight > 0
