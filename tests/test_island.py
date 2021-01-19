# -*- encoding: utf-8 -*-

__author__ = "Anish Thangalingam, Majorann Thevarjah"
__email__ = "anish.thangalingam@nmbu.no ,Majorann.thevarajah@nmbu.no"

from biosim.island import Island
import pytest


def test_check_boundary():
    """
    tests if the function checks the boundaries and raises valueerror
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
    Tests if the function gives us a random choice of the four neighbouring cells the animal ca move
    to.
    """
    mocker.patch("random.choice", return_value=2)
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


#def test_map_creating():
    """
    Tests if the function 
    
    :return: 
    """

    """
    
    def test_population_in_cell():
    
    def test_migration():
    
    def test_island_season_cycle():
    
    """
