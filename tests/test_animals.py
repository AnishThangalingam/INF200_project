# -*- encoding: utf-8 -*-

__author__ = "Majorann Thevarjah & Anish Thangalingam"
__email__ = "Majorann.thevarajah@nmbu.no & Anish.thangalingam@nmbu.no"

from biosim.animals import Herbivore, Carnivore
import pytest


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


def test_raise_error_parameter_set():
    """
    Tests whether parameter_set function raise Key Error and value error when
    the new parameter is a invalid parameter and when it has negative value

    Set half instead of a_half and and chek if it raise key error

    Set -32 for F instead of non-negative value and check if it raise Value error
    """
    new_parameters_to_set = {"half": 100, "F": 2}

    with pytest.raises(KeyError):
        Carnivore.parameter_set(new_parameters_to_set)

    new_parameter_with_negative_value = {"F": -32}

    with pytest.raises(ValueError):
        Carnivore.parameter_set(new_parameter_with_negative_value)
