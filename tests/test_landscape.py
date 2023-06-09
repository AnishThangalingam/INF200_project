# -*- coding: utf-8 -*-

"""
This script contains several tests, which test the landscape scripts functions.

To use this script the user must have installed the python package to the Python environment and
import landscape and its subclasses from the biosim package.
"""

__author__ = 'Anish Thangalingam & Majorann Thevarajah'
__email__ = 'anish.thangalingam@nmbu.no & majorann.thevarajah@nmbu.no'

from biosim.landscape import Highland, Lowland, Desert


def test_get_number_of_herbivores():
    """
    Tests if it checks the amount of Herbivores it is in the population
    """
    population = [{'species': 'Herbivore', 'age': 8, 'weight': 13},
                  {'species': 'Herbivore', 'age': 4, 'weight': 11},
                  {'species': 'Herbivore', 'age': 7, 'weight': 24}]

    lowland = Lowland()
    lowland.set_a_population(population)
    test = lowland.get_number_of_herbivores()

    assert test == 3


def test_get_number_of_carnivores():
    """
    Tests if it checks amount of Carnivores it is in the population
    """
    population = [{'species': 'Carnivore', 'age': 8, 'weight': 13},
                  {'species': 'Carnivore', 'age': 4, 'weight': 11},
                  {'species': 'Carnivore', 'age': 7, 'weight': 24}]

    highland = Highland()
    highland.set_a_population(population)
    test = highland.get_number_of_carnivores()

    assert test == 3


def test_animal_aging():
    """
    Tests if animal age for every year that passes
    """
    population = [{'species': 'Carnivore', 'age': 8, 'weight': 13}]

    lowland = Lowland()
    lowland.set_a_population(population)
    age_before = lowland.population_carnivore[0].age
    lowland.animal_aging()
    age_after = lowland.population_carnivore[0].age

    assert age_after == age_before + 1


def test_animal_death():
    """
    Tests if the function removes dead animals from the list
    """

    population = [{'species': 'Carnivore', 'age': 8, 'weight': 13},
                  {'species': 'Carnivore', 'age': 4, 'weight': 11},
                  {'species': 'Carnivore', 'age': 7, 'weight': 24}]

    desert = Desert()
    desert.set_a_population(population)
    desert.population_carnivore[1].weight = 0
    pop_before = desert.population_carnivore
    desert.animal_death()
    pop_after = desert.population_carnivore

    assert len(pop_before) - 1 == len(pop_after)


def test_weight_loss():
    """
    Tests if the animal has lost weight after a year
    """

    population = [{'species': 'Carnivore', 'age': 8, 'weight': 13}]

    highland = Highland()
    highland.set_a_population(population)
    weight_before = highland.population_carnivore[0].weight
    highland.animal_weight_loss()
    weight_after = highland.population_carnivore[0].weight

    assert weight_before > weight_after


def test_new_herbivore_babies(mocker):
    """
    Tests if the newborn herbivores are added to the herbivore population
    The mocker makes it more likely for a baby animal to be born
    """
    mocker.patch("random.random", return_value=0)

    population = [{'species': 'Herbivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Herbivore', 'age': 4, 'weight': 29.0},
                  {'species': 'Herbivore', 'age': 7, 'weight': 40.0}]

    lowland = Lowland()
    lowland.set_a_population(population)
    lowland.new_herbivore_babies()

    assert len(lowland.population_herbivore) > len(population)


def test_new_carnivore_babies(mocker):
    """
    Tests if the newborn carnivores are added to the carnivore population
    The mocker makes it more likely for a baby animal to be born
    """
    mocker.patch("random.random", return_value=0)

    population = [{'species': 'Carnivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Carnivore', 'age': 4, 'weight': 39.0},
                  {'species': 'Carnivore', 'age': 7, 'weight': 24.0}]

    lowland = Lowland()
    lowland.set_a_population(population)
    lowland.new_carnivore_babies()

    assert len(lowland.population_carnivore) > len(population)


def test_herbivore_eat():
    """
    Tests if herbivore eats, if they eat they will weigh more
    """
    population = [{'species': 'Herbivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Herbivore', 'age': 4, 'weight': 29.0},
                  {'species': 'Herbivore', 'age': 7, 'weight': 40.0}]

    highland = Highland()
    highland.set_a_population(population)
    highland.set_food_parameters()
    weight_before = highland.population_herbivore[0].weight
    highland.herbivore_eat()
    weight_after = highland.population_herbivore[0].weight

    assert weight_before < weight_after


def test_carnivore_eat(mocker):
    """
    Tests if the carnivore eats, if they eat they will weigh more
    """
    mocker.patch("random.random", return_value=0)
    population = [{'species': 'Carnivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Carnivore', 'age': 4, 'weight': 29.0},
                  {'species': 'Carnivore', 'age': 7, 'weight': 24.0},
                  {'species': 'Herbivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Herbivore', 'age': 4, 'weight': 29.0},
                  {'species': 'Herbivore', 'age': 6, 'weight': 25.0}]

    desert = Desert()
    desert.set_a_population(population)
    weight_before = desert.population_carnivore[0].weight
    desert.carnivore_eat()
    weight_after = desert.population_carnivore[0].weight

    assert weight_before < weight_after


def test_animal_migrate(mocker):
    """
    tests if animals migrate

    The mocker patch makes the chances more likely for a animal to migrate from one cell to another
    """
    mocker.patch("random.random", return_value=0)
    population = [{'species': 'Carnivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Carnivore', 'age': 4, 'weight': 29.0},
                  {'species': 'Carnivore', 'age': 7, 'weight': 24.0},
                  {'species': 'Herbivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Herbivore', 'age': 4, 'weight': 29.0},
                  {'species': 'Herbivore', 'age': 6, 'weight': 25.0}]

    highland = Highland()
    highland.set_a_population(population)
    herbivore = highland.animal_migrate()[0]
    carnivore = highland.animal_migrate()[1]

    assert herbivore != []
    assert carnivore != []


def test_new_parameter_set():
    """
    Tests if the function are able to set the new parameters
    """
    test_parameter = {"f_max": 800}

    highland = Highland()
    highland.new_parameter_set(test_parameter)

    assert test_parameter == highland.parameters


def test_set_population():
    """
    Tests if the function are able to set a population
    """
    population = [{'species': 'Carnivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Carnivore', 'age': 4, 'weight': 29.0},
                  {'species': 'Carnivore', 'age': 7, 'weight': 24.0},
                  {'species': 'Herbivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Herbivore', 'age': 4, 'weight': 29.0},
                  {'species': 'Herbivore', 'age': 6, 'weight': 25.0},
                  {'species': 'Herbivore', 'age': 6, 'weight': 25.0}]

    highland = Highland()
    highland.set_a_population(population)

    assert len(highland.population_carnivore) == 3
    assert len(highland.population_herbivore) == 4


def test_set_parameters():
    """
    Tests if the function are able to update the parameters
    """

    lowland = Lowland()
    lowland.set_food_parameters()

    assert lowland.amount_of_food == 800
