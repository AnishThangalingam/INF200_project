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


def test_grows_in_age():
    """
    Tests if the animal increases by one year the following year
    """
    herbivore = Herbivore(4, 20)
    present_age_herbivore = herbivore.age
    herbivore.grows_in_age()
    assert present_age_herbivore + 1 == herbivore.age

    carnivore = Carnivore(3, 30)
    present_age_carnivore = carnivore.age
    carnivore.grows_in_age()
    assert present_age_carnivore + 1 == carnivore.age


def test_age_property():
    """
    Test if the age property function works as it should
    """
    carnivore = Carnivore(2, 1)
    present_age_carnivore = carnivore.age
    assert present_age_carnivore == 2

    herbivore = Herbivore(20, 33)
    present_age_herbivore = herbivore.age
    assert present_age_herbivore == 20


def test_weight_property():
    """
    Test if the weight property function works as it should
    """
    carnivore = Carnivore(2, 1)
    present_weight_carnivore = carnivore.weight
    assert present_weight_carnivore == 1

    herbivore = Herbivore(20, 33)
    present_weight_herbivore = herbivore.weight
    assert  present_weight_herbivore == 33


def test_weight_lose():
    """
    Test that weight after weight loss is less than initial weight
    """
    herbivore = Herbivore(1, 10)
    present_weight_herbivore = herbivore.weight
    herbivore.weight_lose()
    assert herbivore.weight < present_weight_herbivore

    carnivore = Carnivore(2, 20)
    present_weight_carnivore = carnivore.weight
    carnivore.weight_lose()
    assert carnivore.weight < present_weight_carnivore


def test_weight_increases_of_eat():
    """
    Test that present weight is less than the weight after
    eating
    """
    amount_of_food = 9
    herbivore = Herbivore(3, 40)
    present_weight_herbivore = herbivore.weight
    herbivore.eat(amount_of_food)
    assert present_weight_herbivore < herbivore.weight


def test_fitness():
    """
    Testing the fitness function calculate as it should.

    Test a herbivore where it is 10 year old with weight 30.
    The fitness should return 0.88.
    0.88 is calculated by hand

    Testing a carnivore with 0 weight. It should return 0
    """
    herbivore = Herbivore(10, 30)
    assert round(herbivore.fitness, 2) == 0.88

    carnivore = Carnivore(10, 0)
    assert round(carnivore.fitness, 2) == 0


def test_fitness_range():
    """
    Tests the fitness range are between 0 and 1
    """
    herbivore = Herbivore(2, 20)
    assert 0 <= herbivore.fitness
    assert 1 >= herbivore.fitness

    carnivore = Carnivore(4, 3)
    assert 0 <= carnivore.fitness
    assert 1 >= carnivore.fitness


def test_error_age_value():
    """
    Chek if Animal class raise value error when age value i negative
    """
    with pytest.raises(ValueError):
        Herbivore(age=-3)

    with pytest.raises(ValueError):
        Carnivore(age=-10)


def test_error_weight_value():
    """
    Chek if Animal class raise value error when weight value i negative
    """
    with pytest.raises(ValueError):
        Herbivore(weight=-5)

    with pytest.raises(ValueError):
        Carnivore(weight=-11)


def test_birth_with_one_animal():
    """
    Testing if the baby function returns None if the number animal is 1 or less.
    """
    herbivore = Herbivore(2, 10)
    number_of_animal = 1
    birth_herbivore = herbivore.baby(number_of_animal)
    assert birth_herbivore is None

    carnivore = Carnivore(20, 40)
    number_of_animal = 1
    birth_carnivore = carnivore.baby(number_of_animal)
    assert birth_carnivore is None


def test_birth_probability(mocker):
    """
    Test if the baby function returns None when the probability to give
    birth is less than the random value
    """
    mocker.patch("random.random", value=2)
    herbivore = Herbivore(3, 14)
    number_of_animal = 3
    birth_herbivore = herbivore.baby(number_of_animal)
    assert birth_herbivore is None

    carnivore = Carnivore(2, 12)
    birth_carnivore = carnivore.baby(number_of_animal)
    assert birth_carnivore is None


def test_death_if_weight_is_zero():
    """
    Test if the death function gives True when the weight of the animal is zero.
    """
    herbivore = Herbivore(2, 10)
    herbivore.weight = 0
    assert herbivore.death() is True

    carnivore = Carnivore(20, 40)
    carnivore.weight = 0
    assert carnivore.death() is True


def test_weight_after_eating():
    """
    Test if the weight increase for herbivore when it eat a amount of food.

    If the amount of food is 20, than the weight should increase with 20*0.9
    """
    herbivore = Herbivore(4, 15)
    herbivore.eat(20)
    assert herbivore.weight == 15 + 20*0.9
