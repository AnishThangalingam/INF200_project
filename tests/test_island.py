# -*- encoding: utf-8 -*-
"""
This script contains several tests, which test the island scripts functions.

To use this script the user must have installed the python package to the Python environment and
import the island.py from the biosim package. The user must also import pytest

"""

__author__ = "Anish Thangalingam, Majorann Thevarjah"
__email__ = "anish.thangalingam@nmbu.no ,Majorann.thevarajah@nmbu.no"

from biosim.island import Island
import pytest


def test_check_boundary():
    """
    Tests if the function checks the boundaries and raises valueerror
    """

    test_map = """\
               HWH
               WHW
               WWW"""

    with pytest.raises(ValueError):
        Island(island_map=test_map, initial_population=[])


def test_invalid_landscape():
    """
    Tests if a landscape is invalid and raises valueerror
    """
    test_map = """\
               ZWW
               WHW
               WWW"""

    with pytest.raises(ValueError):
        Island(island_map=test_map, initial_population=[])


def test_check_map_lines():
    """
    Tests if all the map lines has the same length, if not it will raise valueerror.
    """
    test_map = """\
               WWW
               WHHW
               WWW"""

    with pytest.raises(ValueError):
        Island(island_map=test_map, initial_population=[])


def test_move_to_cell(mocker):
    """
    Tests if the function gives us a random choice of the four neighbouring cells, the animal can move
    to.
    """
    mocker.patch("numpy.random.choice", return_value=2)
    test_map = """\
               WWWWWW
               WHHHHW
               WDDDDW
               WWWWWW"""

    island = Island(island_map=test_map, initial_population=[])
    current_cell = (2, 3)
    next_cell = island.move_to_cell(current_cell)

    assert current_cell != next_cell
    assert next_cell == (2, 4)


def test_population_in_cell():
    """
    Tests if the function gives us the population of a particular cell.
    """
    test_map = """\
                  WWWWWW
                  WHHHHW
                  WDDDDW
                  WWWWWW"""

    population = [{'loc': (3, 3),
                   'pop': [{'species': 'Carnivore', 'age': 5, 'weight': 20.0}]},
                  {'loc': (3, 3),
                   'pop': [{'species': 'Carnivore', 'age': 8, 'weight': 31.0}]},
                  {'loc': (3, 3),
                   'pop': [{'species': 'Carnivore', 'age': 4, 'weight': 29.0}]}]

    island = Island(island_map=test_map, initial_population=[])
    island.population_in_cell(population)

    assert len(island.map[(3, 3)].population_carnivore) == 3


def test_map_creating():
    """
    Tests if the function creates a map for the island Rossumøya, so if the island map creating test passes,
    it means the function works and will create a map
    """
    test_map = """\
                    WWWWWW
                    WHHHHW
                    WHHHHW
                    WDDDDW
                    WWWWWW"""

    population = [{'loc': (3, 3),
                   'pop': [{'species': 'Carnivore', 'age': 5, 'weight': 20}]},
                  {'loc': (3, 3),
                   'pop': [{'species': 'Carnivore', 'age': 8, 'weight': 31.0}]},
                  {'loc': (3, 3),
                   'pop': [{'species': 'Carnivore', 'age': 4, 'weight': 29.0}]}]

    island = Island(island_map=test_map, initial_population=[])
    island.population_in_cell(population)
    island.map_creating()


def test_migration(mocker):
    """
    Test if animals migrate to suitable landscapes, if the population before is not the same as the population after,
    it means that the function works and that the animals migrate to a suitable landscape
    """
    mocker.patch("numpy.random.choice", return_value=2)
    mocker.patch("random.random", return_value=0)
    test_map = """\
                    WWWWWW
                    WHHHHW
                    WHHHHW
                    WDDDDW
                    WWWWWW"""

    population = [{'loc': (2, 3),
                   'pop': [{'species': 'Carnivore', 'age': 5, 'weight': 20}]},
                  {'loc': (2, 3),
                   'pop': [{'species': 'Carnivore', 'age': 8, 'weight': 31.0}]},
                  {'loc': (2, 3),
                   'pop': [{'species': 'Carnivore', 'age': 4, 'weight': 29.0}]}]

    island = Island(island_map=test_map, initial_population=[])
    island.population_in_cell(population)
    population_before = len(island.map[(2, 3)].population_carnivore)
    island.migration((2, 3))
    population_after = len(island.map[(2, 3)].population_carnivore)

    assert population_before != population_after


def test_island_season_cycle(mocker):
    """
    Tests if the function gives us the population after a annual cycle in the cell, so if the island cycle pass the
    test, it means the function work annually

    """
    mocker.patch("random.random", return_value=0)
    test_map = """\
                    WWWWWW
                    WHHHHW
                    WHHHHW
                    WDDDDW
                    WWWWWW"""

    population = [{'loc': (3, 3),
                   'pop': [{'species': 'Carnivore', 'age': 5, 'weight': 20}]},
                  {'loc': (3, 3),
                   'pop': [{'species': 'Carnivore', 'age': 8, 'weight': 31.0}]},
                  {'loc': (3, 3),
                   'pop': [{'species': 'Carnivore', 'age': 4, 'weight': 29.0}]}]

    island = Island(island_map=test_map, initial_population=[])
    island.population_in_cell(population)
    island.island_season_cycle()
