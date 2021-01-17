# -*- encoding: utf-8 -*-

__author__ = "Anish Thangalingam, Majorann Thevarjah"
__email__ = "anish.thangalingam@nmbu.no ,Majorann.thevarajah@nmbu.no"

import textwrap

from .landscape import Water, Desert, Highland, Lowland
from .animals import Carnivore, Herbivore

class Island:

    landscapes = {"W": Water, "D": Desert, "H": Highland, "L": Lowland}

    def __init__(self, island_map, initial_population=None):

        self.amount_of_herbivores = []
        self.amount_of_carnivores = []
        self.map = {}

        self.geo = textwrap.dedent(island_map)
        self.line_island = self.geo.splitlines()

        self.ini_pop = initial_population
        self.map_creating()
        self.population_in_cell(self.ini_pop)

        for each_line in self.line_island:
            for type in each_line:
                if type not in self.landscapes.keys():
                    raise ValueError("One or more of the cell type does not exit")

    def map_creating(self):
        """
        Creates a map
        """
        for y_coord, line in enumerate(self.line_island):
            for type, x_coord in enumerate(line):
                self.map[(y_coord + 1, x_coord + 1)] = self.landscapes[type]()
        return self.map