# -*- encoding: utf-8 -*-

__author__ = "Majorann Thevarjah & Anish Thangalingam"
__email__ = "Majorann.thevarajah@nmbu.no & Anish.thangalingam@nmbu.no"

from biosim.animals import Herbivore, Carnivore
import random


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

        self.image_format = img_fmt
        self._present_year = 0

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

    @property
    def year(self):
        """Last year simulated."""
        return self._present_year
