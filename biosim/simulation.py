# -*- encoding: utf-8 -*-

__author__ = "Majorann Thevarjah & Anish Thangalingam"
__email__ = "Majorann.thevarajah@nmbu.no & Anish.thangalingam@nmbu.no"

from biosim.animals import Herbivore, Carnivore
from biosim.landscape import Highland, Lowland
from biosim.island import Island
from biosim.visualization import Visualization
import random
import pandas as pd
import numpy as np
import subprocess
import textwrap


_FFMPEG_BINARY = 'ffmpeg'


class BioSim:
    def __init__(self, island_map, ini_pop, seed,
                 ymax_animals=None, cmax_animals=None, hist_specs=None,
                 img_base=None, img_fmt='png'):

        """
        :param island_map: Multi-line string specifying island geography
        :param ini_pop: List of dictionaries specifying initial population
        :param seed: Integer used as random number seed
        :param ymax_animals: Number specifying y-axis limit for graph showing animal numbers
        :param cmax_animals: Dict specifying color-code limits for animal densities
        :param hist_specs: Specifications for histograms, see below
        :param img_base: String with beginning of file name for figures, including path
        :param img_fmt: String with file type for figures, e.g. ’png’

        If ymax_animals is None, the y-axis limit should be adjusted automatically.

        If cmax_animals is None, sensible, fixed default values should be used.
        cmax_animals is a dict mapping species names to numbers, e.g.,
            {’Herbivore’: 50, ’Carnivore’: 20}
        hist_specs is a dictionary with one entry per property for which a histogram shall be shown.
        For each property, a dictionary providing the maximum value and the bin width must be
        given, e.g.,
            {’weight’: {’max’: 80, ’delta’: 2}, ’fitness’: {’max’: 1.0, ’delta’: 0.05}}
        Permitted properties are ’weight’, ’age’, ’fitness’.

        If img_base is None, no figures are written to file.
        Filenames are formed as
        ’{}_{:05d}.{}’.format(img_base, img_no, img_fmt)

        where img_no are consecutive image numbers starting from 0.
        img_base should contain a path and beginning of a file name.
        """

        random.seed(seed)
        self.island_map = island_map
        self.ini_pop = ini_pop
        self.island = Island(self.island_map, self.ini_pop)

        if ymax_animals is None:
            # Adjust y-max value
            self.ymax_animals = 18000
        else:
            self.ymax_animals = ymax_animals

        if cmax_animals is None:
            self.cmax_animal = {"Herbivore": 200, "Carnivore": 100}
        else:
            self.cmax_animal = cmax_animals

        if hist_specs is None:
            self.hist_spec = {"weight": {"max": 60, "delta": 2},
                              "fitness": {"max": 1.0, "delta": 0.05},
                              "age": {"max": 60, "delta": 2}}
        else:
            self.hist_spec = hist_specs

        if img_base is not None:
            self.image_base = img_base
        else:
            self.image_base = None

        self.image_format = img_fmt
        self._present_year = 0
        self.visual = Visualization(self.cmax_animal, self.hist_spec)
        self.image_counter = 0
        self.count = 0

    @staticmethod
    def set_animal_parameters(species, params):
        """
        Set parameters for animal species.
        :param species: String, name of animal species
        :param params: Dict with valid parameter specification for species
        """
        if species == "Herbivore":
            Herbivore.parameter_set(params)
        elif species == "Carnivore":
            Carnivore.parameter_set(params)
        else:
            raise TypeError("Species can only be Herbivore or Carnivore")

    @staticmethod
    def set_landscape_parameters(landscape, params):
        """
        Set parameters for landscape type.
        :param landscape: String, code letter for landscape
        :param params: Dict with valid parameter specification for landscape
        """
        landscapes_changeable = {"H": Highland, "L": Lowland}
        if landscape in landscapes_changeable:
            landscapes_changeable[landscape].new_parameter_set(params)

    def simulate(self, num_years, vis_years=1, img_years=None):
        """
        Run simulation while visualizing the result.
        :param num_years: number of years to simulate
        :param vis_years: years between visualization updates
        :param img_years: years between visualizations saved to files (default: vis_years)
        Image files will be numbered consecutively.
        """
        self.visual.creat_a_window()
        num_years = num_years + self._present_year
        self.visual.subplot_for_the_animal_count_curves(num_years+1, self.ymax_animals)


        self.visual.subplot_for_map()
        string_island_map = textwrap.dedent(self.island_map)
        string_island_map.replace("\n", " ")
        self.visual.map_graphics(string_island_map)

        self.visual.subplot_for_year()

        self.visual.subplot_for_distribution_plot()
        distribution = self.distributions
        self.visual.herbivore_heat_map_update(distribution)
        self.visual.carnivore_heat_map_update(distribution)

        self.visual.subplot_for_histogram()

    @property
    def year(self):
        """Last year simulated."""
        return self._present_year

    @property
    def num_animals(self):
        """Total number of animals on island."""
        total_of_each_species_in_island = self.num_animals_per_species
        total_population_in_island = (total_of_each_species_in_island["Carnivore"] +
                                      total_of_each_species_in_island["Herbivore"])
        return total_population_in_island

    @property
    def num_animals_per_species(self):
        """Number of animals per species in island, as dictionary."""
        count_of_per_species = {"Herbivore": 0, "Carnivore": 0}
        for position in self.island.map:
            if self.island.map[position].flag:
                count_of_per_species["Carnivore"] += len(self.island.map[position].population_Carnivore)
                count_of_per_species["Herbivore"] += len(self.island.map[position].population_Herbivore)
        return count_of_per_species

    @property
    def distributions(self):

        cell_data = []
        for coordinate, cell in self.island.map.items():
            row = coordinate[0]
            col = coordinate[1]
            herbivore = len(cell.population_Herbivore)
            carnivore = len(cell.population_Carnivore)
            cell_data.append([row, col, herbivore, carnivore])
        distribution = pd.DataFrame(data=cell_data, columns=['Row', 'Col', 'Herbivore'])
        return distribution

    @property
    def hist_fitness_data(self):
        """
        Function that takes in the data for fitness

        :return: herbivore_fitness_dictionary: a dictionary with data
        :return: carnivore_fitness_dictionary: a dictionary with dat
        """
        fitness_herbivore_list = []
        fitness_carnivore_list = []
        herbivore_fitness_dictionary = {"fitness": []}
        carnivore_fitness_dictionary = {"fitness": []}
        for cell in self.island.map:
            if self.island.map[cell].flag:
                for carnivore in self.island.map[cell].population_Carnivore:
                    fitness_carnivore_list.append(carnivore.fitness)

            for herbivore in self.island.map[cell].population_Herbivore:
                fitness_herbivore_list.append(herbivore.fitness)
        herbivore_fitness_dictionary["fitness"] = np.array(fitness_herbivore_list)
        carnivore_fitness_dictionary["fitness"] = np.array(fitness_carnivore_list)
        return herbivore_fitness_dictionary, carnivore_fitness_dictionary

    @property
    def hist_age_data(self):
        """
        Function that takes in the data for age.

        :return: herbivore_age_dictionary: a dictionary with data
        :return: carnivore_age_dictionary: a dictionary with data
        """
        age_herbivore_list = []
        age_carnivore_list = []
        herbivore_age_dictionary = {"age": []}
        carnivore_age_dictionary = {"age": []}
        for cell in self.island.map:
            if self.island.map[cell].flag:
                for carnivore in self.island.map[cell].population_Carnivore:
                    age_carnivore_list.append(carnivore.age)

                for herbivore in self.island.map[cell].population_Herbivore:
                    age_herbivore_list.append(herbivore.age)
        herbivore_age_dictionary["age"] = np.array(age_herbivore_list)
        carnivore_age_dictionary["age"] = np.array(age_carnivore_list)

        return herbivore_age_dictionary, carnivore_age_dictionary

    @property
    def hist_weight_data(self):
        """
        Function that takes in the data for weight.

        :return: herbivore_weight_dictionary: a dictionary with data
        :return: carnivore_weight_dictionary: a dictionary with data
        """
        weight_herbivore_list = []
        weight_carnivore_list = []
        herbivore_weight_dictionary = {"weight": []}
        carnivore_weight_dictionary = {"weight": []}
        for cell in self.island.map:
            if self.island.map[cell].flag:
                for carnivore in self.island.map[cell].population_Carnivore:
                    weight_carnivore_list.append(carnivore.weight)

                for herbivore in self.island.map[cell].population_Herbivore:
                    weight_herbivore_list.append(herbivore.weight)
        herbivore_weight_dictionary["weight"] = np.array(weight_herbivore_list)
        carnivore_weight_dictionary["weight"] = np.array(weight_carnivore_list)

        return herbivore_weight_dictionary, carnivore_weight_dictionary

    def make_movie(self):
        """
        Create MPEG4 movie from visualization images saved.
        The code below is inspired by a lecture hold by Hans Ekkehard Plesser.
        """
        format_of_the_movie = 'mp4'
        if self.image_base is None:
            raise RuntimeError('The filename is not defined')

        try:
            subprocess.check_call(
                [
                    _FFMPEG_BINARY,
                    "-i",
                    "{}_%05d.png".format(self.image_base),
                    "-y",
                    "-profile:v",
                    "baseline",
                    "-filter:v",
                    "setpts=5*PTS",
                    "-level",
                    "3.0",
                    "-pix_fmt",
                    "yuv420p",
                    "{}.{}".format(self.image_base, format_of_the_movie),
                ]
            )

        except subprocess.CalledProcessError as err:
            raise RuntimeError("ERROR: ffmpeg failed with: {}".format(err))


