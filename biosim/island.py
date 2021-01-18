# -*- encoding: utf-8 -*-

__author__ = "Anish Thangalingam, Majorann Thevarjah"
__email__ = "anish.thangalingam@nmbu.no ,Majorann.thevarajah@nmbu.no"

import textwrap
import random

from .landscape import Water, Desert, Highland, Lowland


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
            if len(self.line_island[0]) != len(line):
                raise ValueError("All the lines in the island map must have the same length")

    def map_creating(self):
        """
        Creates a map
        """

        self.check_boundary_and_invalid_landscape()
        self.check_map_lines()
        for y_coord, line in enumerate(self.line_island):
            for x_coord, cell_type in enumerate(line):
                self.map[(y_coord + 1, x_coord + 1)] = self.landscapes[cell_type]()
        return self.map

    @staticmethod
    def move_to_cell(loc_pos):
        """
        gives the coordinates to which cell the animal can move to, it can go either up, down, left or right
        """
        x_coord = loc_pos[1]
        y_coord = loc_pos[0]

        neighbour_cells_loc = [(x_coord + 1, y_coord), (x_coord - 1, y_coord),
                               (x_coord, y_coord + 1), (x_coord, y_coord - 1)]

        Random_cell_from_list = random.choice(neighbour_cells_loc)

        return Random_cell_from_list

    def population_in_cell(self, population):
        """
        Gives us the population in a particular cell

        :return:
        """
        if population is None:
            current_population = self.ini_pop
        else:
            current_population = population

        for animal in current_population:
            pop = animal["pop"]
            loc = animal["loc"]
            self.map[loc].set_a_population[pop]

    def migration(self, loc_pos):
        """
        Make a function for the migrating animals, where flag is the passable landscape for the animals. This for loop
        makes the animal migrate to a suited landscape, if it is not a suitable landscape the for loop will break

        :return:
        """

        if self.map[loc_pos].flag:
            migrating_herbivore = self.map[loc_pos].animal_migrate()[0]
            migrating_carnivore = self.map[loc_pos].animal_migrate()[1]

            for herbivore in migrating_herbivore:
                new_loc = self.move_to_cell(loc_pos)
                if self.map[new_loc].flag:
                    self.map[new_loc].population_Herbivore.append(herbivore)
                    self.map[loc_pos].population_Herbivore.remove(herbivore)
                else:
                    break

            for carnivore in migrating_carnivore:
                new_loc = self.move_to_cell(loc_pos)
                if self.map[new_loc].flag:
                    self.map[new_loc].population_Carnivore.append(carnivore)
                    self.map[loc_pos].population_Carnivore.remove(carnivore)
                else:
                    break

    def island_season_cycle(self):
        """
        the given cycle for a year, this is what happens a season, every functions that happens in a cell during a
        season
        :return:
        """

        for loc_pos in self.map:
            self.map[loc_pos].new_parameter_set()
            self.map[loc_pos].set_a_population()
            self.map[loc_pos].get_number_of_herbivores()
            self.map[loc_pos].get_number_of_carnivores()
            self.map[loc_pos].animal_aging()
            self.map[loc_pos].animal_death()
            self.map[loc_pos].animal_weight_loss()
            self.map[loc_pos].new_herbivore_babies()
            self.map[loc_pos].new_carnivore_babies()
            self.map[loc_pos].set_food_parameters()
            self.map[loc_pos].herbivore_eat()
            self.map[loc_pos].carnivore_eat()
            self.map[loc_pos].animal_migrate()
