# -*- encoding: utf-8 -*-
"""
This island script contains an island class, which gives us functions that creates
the map of Rossumøya. The island class also contain happenings that occur on the island
every year.

Purpose of this function is to give detailed information about the island and the annual cycle
of the island. Which can be used to form the island map.
"""

__author__ = "Anish Thangalingam, Majorann Thevarjah"
__email__ = "anish.thangalingam@nmbu.no ,Majorann.thevarajah@nmbu.no"

import textwrap
import random

from .landscape import Water, Desert, Highland, Lowland


class Island:
    """
    Class for the whole island, which tells us what the island contains and this class forms the
    island
    """

    landscapes = {"W": Water, "D": Desert, "H": Highland, "L": Lowland}

    def __init__(self, island_map, initial_population=None):
        """
        This function gives the opportunity to update the parameters

        :param island_map: the map of Rossumøya
        :param initial_population: The population in the island
        """
        self.amount_of_herbivores = []
        self.amount_of_carnivores = []
        self.map = {}

        self.geo = textwrap.dedent(island_map)
        self.line_island = self.geo.splitlines()

        self.ini_pop = initial_population
        self.map_creating()
        self.population_in_cell(self.ini_pop)

    def check_boundary_and_invalid_landscape(self):
        """
        This function checks if the island is surrounded by water. if it is not this function raises a valueerror,
        which tells us what is wrong. This function also checks if a cell type exists, if it does not exist, the
        function raises a valueerror.

        """
        for pos in range(len(self.line_island)):
            if self.line_island[pos][-1] != "W":
                raise ValueError("Boundary, Island is not surrounded by water")
            elif self.line_island[pos][0] != "W":
                raise ValueError("Boundary, Island is not surrounded by water")

        for lines in self.line_island:
            for cell_type in lines:
                if cell_type not in self.landscapes.keys():
                    raise ValueError("Cell type does not exist")

    def check_map_lines(self):
        """
        This function checks if all the map lines have the same length, which they must have. If not this function
        raises a valueerror, which tells us that all the lines must have the same length.

        """
        for line in self.line_island:
            if len(self.line_island[0]) != len(line):
                raise ValueError("All the lines in the island map must have the same length")

    @staticmethod
    def move_to_cell(loc_pos):
        """
        This function gives the animal in the cell which coordinates it can move to. The information we are given is
        that it can go either up, down, left or right. So we make a list with those four neighbour cells.

        :param: loc_pos, the locations position of the cell
        :return: Random cell from the four neighbouring cells
        """
        x_coord = loc_pos[1]
        y_coord = loc_pos[0]

        neighbour_cells_loc = [(y_coord + 1, x_coord), (y_coord - 1, x_coord),
                               (y_coord, x_coord + 1), (y_coord, x_coord - 1)]

        random_cell_from_list = random.choice(neighbour_cells_loc)

        return random_cell_from_list

    def population_in_cell(self, population):
        """
        This function gives us the population of a particular cell and sets a population in the given current
        location. So the function sets a population for the animals in a particular cell.

        :param: population, the population of animals in a cell
        """
        current_population = population

        for animal in current_population:
            pop = animal["pop"]
            loc = animal["loc"]
            self.map[loc].set_a_population[pop]

    def map_creating(self):
        """
        This function creates the island map, taking into account that it checks boundary, invalid lanscapes
        and map lines.

        return: map, it returns the created map
        """

        self.check_boundary_and_invalid_landscape()
        self.check_map_lines()
        for y_coord, line in enumerate(self.line_island):
            for x_coord, cell_type in enumerate(line):
                self.map[(y_coord + 1, x_coord + 1)] = self.landscapes[cell_type]()
        return self.map

    def migration(self, loc_pos):
        """
        This function makes a animal migrate, where flag is the passable landscape for the animal. So if the landscape
        is suitable for the animal it will migrate there, if not it will move on to another random neighbour cell. When
        the animal migrate it will be added to the new location and removed from the old.

        :param: loc_pos, the locations position of the cell
        """

        if self.map[loc_pos].flag:
            migrating_herbivore = self.map[loc_pos].animal_migrate()[0]
            migrating_carnivore = self.map[loc_pos].animal_migrate()[1]

            for herbivore in migrating_herbivore:
                new_loc = self.move_to_cell(loc_pos)
                if not self.map[new_loc].flag:
                    break
                else:
                    self.map[new_loc].population_Herbivore.append(herbivore)
                    self.map[loc_pos].population_Herbivore.remove(herbivore)

            for carnivore in migrating_carnivore:
                new_loc = self.move_to_cell(loc_pos)
                if not self.map[new_loc].flag:
                    break
                else:
                    self.map[new_loc].population_Carnivore.append(carnivore)
                    self.map[loc_pos].population_Carnivore.remove(carnivore)

    def island_season_cycle(self):
        """
        This function gives us the cycle for a year. This is functions work annually and works for all the cells in
        the island.
        """

        for loc_pos in self.map:
            self.map[loc_pos].animal_aging()
            self.map[loc_pos].animal_death()
            self.map[loc_pos].animal_weight_loss()
            self.map[loc_pos].new_herbivore_babies()
            self.map[loc_pos].new_carnivore_babies()
            self.map[loc_pos].set_food_parameters()
            self.map[loc_pos].herbivore_eat()
            self.map[loc_pos].carnivore_eat()
            self.migration(loc_pos)
