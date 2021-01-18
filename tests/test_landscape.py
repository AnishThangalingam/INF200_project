# -*- coding: utf-8 -*-

__author__ = 'Anish Thangalingam'
__email__ = 'anish.thangalingam@nmbu.no'

from biosim.landscape import Highland, Lowland, Desert

def test_new_parameter_set():
    """

    :return:
    """



def test_set_population():
    """

    :return:
    """



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


def test_animal_aging():
    """
    Tests if animal age
    """
    population = [{'species': 'Carnivore', 'age': 8, 'weight': 13}]

    lowland = Lowland()
    lowland.set_a_population(population)
    age_before = lowland.population_Carnivore[0].age
    lowland.animal_aging()
    age_after = lowland.population_Carnivore[0].age

    assert age_after == age_before + 1


def test_animal_death():
    """
    Tests if the function removes dead animals
    """
    population = [{'species': 'Carnivore', 'age': 8, 'weight': 13},
                  {'species': 'Carnivore', 'age': 4, 'weight': 11},
                  {'species': 'Carnivore', 'age': 7, 'weight': 24}]

    desert = Desert()
    desert.set_a_population(population)
    desert.population_Carnivore[1].weight = 0
    pop_before = desert.population_Carnivore
    desert.animal_death()
    pop_after = desert.population_Carnivore

    assert len(pop_before) - 1 == len(pop_after)


def test_weight_loss():
    """

    :return:
    """
    population = [{'species': 'Carnivore', 'age': 8, 'weight': 13}]

    highland = Highland()
    highland.set_a_population(population)
    weight_before = highland.population_Carnivore[0].weight
    highland.animal_weight_loss()
    weight_after = highland.population_Carnivore[0].weight

    assert weight_before > weight_after


def test_new_herbivore_babies(mocker):
    """
    tests if the newborn herbivores are added to the herbivore population
    """
    mocker.patch("random.random", return_value=0)

    population = [{'species': 'Herbivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Herbivore', 'age': 4, 'weight': 29.0},
                  {'species': 'Herbivore', 'age': 7, 'weight': 40.0}]

    lowland = Lowland()
    lowland.set_a_population(population)
    lowland.new_herbivore_babies()

    assert len(lowland.population_Herbivore) > len(population)


def test_new_carnivore_babies(mocker):
    """
    tests if the newborn carnivores are added to the carnivore population
    """
    mocker.patch("random.random", return_value=0)

    population = [{'species': 'Carnivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Carnivore', 'age': 4, 'weight': 39.0},
                  {'species': 'Carnivore', 'age': 7, 'weight': 24.0}]

    lowland = Lowland()
    lowland.set_a_population(population)
    lowland.new_carnivore_babies()

    assert len(lowland.population_Carnivore) > len(population)

def test_set_parameters():

def test_herbivore_eat():
    """
    tests if herbivore eats, because if they eat they will weigh more
    :return:
    """
    population = [{'species': 'Herbivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Herbivore', 'age': 4, 'weight': 29.0},
                  {'species': 'Herbivore', 'age': 7, 'weight': 40.0}]

    highland = Highland()
    highland.set_a_population(population)
    highland.set_food_parameters()
    weight_before = highland.population_Herbivore[0].weight
    highland.herbivore_eat()
    weight_after = highland.population_Herbivore[0].weight

    assert weight_before < weight_after

def test_carnivore_eat():

    population = [{'species': 'Carnivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Carnivore', 'age': 4, 'weight': 29.0},
                  {'species': 'Carnivore', 'age': 7, 'weight': 24.0},
                  {'species': 'Herbivore', 'age': 8, 'weight': 31.0},
                  {'species': 'Herbivore', 'age': 4, 'weight': 29.0}]

    desert = Desert()
    desert.set_a_population(population)
    weight_before = desert.population_Carnivore[0].weight
    desert.carnivore_eat()
    weight_after = desert.population_Carnivore[0].weight

    assert weight_before == weight_after

def test_animal_migrate():


