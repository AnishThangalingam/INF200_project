# -*- encoding: utf-8 -*-

__author__ = "Anish Thangalingam, Majorann Thevarjah"
__email__ = "anish.thangalingam@nmbu.no ,Majorann.thevarajah@nmbu.no"

import textwrap

from .landscape import Water, Desert, Highland, Lowland
from .animals import Carnivore, Herbivore

class Island:

    landscapes = {"W": Water, "D": Desert, "H": Highland, "L": Lowland}

    def __init__(self, island_map, initial_population=None):
        """

        :param island_map:
        :param initial_population:
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
        Legg inn kommentarer

        :return:
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
        Legg inn kommentar
        :return:
        """
        for line in self.line_island:
            if len(self.line_island[0]) != len(line)
                raise ValueError("All the lines in the island map must have the same length")


    def map_creating(self):
        """
        Creates a map
        """

        self.check_boundary_and_invalid_landscape()
        self.check_map_lines()
        for y_coord, line in enumerate(self.line_island):
            for cell_type, x_coord in enumerate(line):
                self.map[(y_coord + 1, x_coord + 1)] = self.landscapes[cell_type]()
        return self.map






























    herb_