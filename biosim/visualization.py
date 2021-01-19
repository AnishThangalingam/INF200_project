# -*- encoding: utf-8 -*-
"""
This script contains visualization class and the pupose of this class is to give detailed visualization of the
simulation in Island. This class will create a plot window with several subplot to show island map,
population growth, heatmaps and histograms. It will show the graphics of the simulation.

The user must have installed math, numpy and matplotlib package to the python environment to run this script.
"""

__author__ = "Majorann Thevarjah & Anish Thangalingam"
__email__ = "Majorann.thevarajah@nmbu.no & Anish.thangalingam@nmbu.no"

import matplotlib.pyplot as plt
import numpy as np
import math


class Visualization:
    """
    Visualization class for the visualization of the simulation
    """

    def __init__(self, cmax, hist_spec):
        """
        Initializing the visualization class

        :param: cmax: max value for heat map distribution
        :param: hist_spec:hist_specs is a dictionary with one entry per property for which a histogram shall be shown.
        """
        self.cmax = cmax
        self.hist_spec = hist_spec
        self._fig = None
        self._grids = None
        self._map = None
        self._year_count = None
        self._fitness_hist_fig = None
        self._age_hist_fig = None
        self._weight_hist_fig = None
        self._animal_count = None
        self._carnivore_curve = None
        self._herbivore_curve = None
        self._herbivore_heat = None
        self._carnivore_heat = None
        self._carnivore_dist = None
        self._herbivore_dist = None
        self._fitness_histogram = None
        self._age_histogram = None
        self._weight_histogram = None
        self._year_text = None

    def creat_a_window(self):
        """
        Creat a window to show the visualization of the simulation
        """
        if self._fig is None:
            self._fig = plt.figure(constrained_layout=True, figsize=(10, 8))
            self._fig.set_facecolor('lightblue')
            self._grids = self._fig.add_gridspec(8, 12)

    def subplot_for_map(self):
        """
        Creat subplot for island map in the visualization window
        """
        if self._map is None:
            self._map = self._fig.add_subplot(self._grids[:3, :5])
            self._map.title.set_text("Island")
            self._map.axis("off")

    def subplot_for_year(self):
        """
        Adding a subplot for year count
        This code is inspired by a lecture hold by Hans Ekkehard Plesser in
        January block 2021.
        """

        if self._year_count is None:
            self._year_count = self._fig.add_subplot(self._grids[:1, 5:7])
            template = "Year: {:5d}"
            self._year_text = self._year_count.text(
                0.5,
                0.5,
                template.format(0),
                horizontalalignment="center",
                verticalalignment="center",
                transform=self._year_count.transAxes,
            )
        self._year_count.axis("off")

    def subplot_for_histogram(self):
        """
        Subplot for fitness, age and weight histogram
        """
        # Subplot for fitness histogram:
        if self._fitness_hist_fig is None:
            self._fitness_hist_fig = self._fig.add_subplot(self._grids[6:, :4])

        # Subplot for age histogram:
        if self._age_hist_fig is None:
            self._age_hist_fig = self._fig.add_subplot(self._grids[6:, 4:8])

        # Subplot for weight histogram:
        if self._weight_hist_fig is None:
            self._weight_hist_fig = self._fig.add_subplot(self._grids[6:, 8:])

    def subplot_for_the_animal_count_curves(self, x_limit, y_limit):
        """
        Subplot for the curves where it count the count of each animal every year
        This code is inspired by a lecture hold by Hans Ekkehard Plesser in january block 2021

        :params: x_limit: det maximum length of x axis
        :parms: y_limit: the maximum length if y axis
        """
        # Subplot for animal:
        if self._animal_count is None:
            self._animal_count = self._fig.add_subplot(self._grids[:3, 7:])
            # Set title and labels for the plor
            self._animal_count.title.set_text("Number count for Herbivore and Carnivore")
            self._animal_count.set_xlabel("Year")
            self._animal_count.set_ylabel("Animal count")
            # Set length of x and y axis
            self._animal_count.set_xlim(0, x_limit)
            self._animal_count.set_ylim(0, y_limit)
        elif self._animal_count is not None:
            self._animal_count.set_xlim(0, x_limit)

        # Carnivore curve
        if self._carnivore_curve is None:
            plot_carnivore = self._animal_count.plot(np.arange(0, x_limit),
                                                     np.full(x_limit, np.nan), label="Carnivore", color="red")
            self._carnivore_curve = plot_carnivore[0]
        elif self._carnivore_curve is not None:
            x_data = self._carnivore_curve.get_data()[0]
            y_data = self._carnivore_curve.get_data()[1]
            x_new = np.arange(x_data[-1] + 1, x_limit)
            if len(x_new) > 0:
                y_new = np.full(x_new.shape, np.nan)
                x_stack = np.hstack((x_data, x_new))
                y_stack = np.hstack((y_data, y_new))
                self._carnivore_curve.set_data(x_stack, y_stack)

        # Herbivore curve
        if self._herbivore_curve is None:
            plot_herbivore = self._animal_count.plot(np.arange(0, x_limit),
                                                     np.full(x_limit, np.nan), label="Herbivore", color="green")
            self._herbivore_curve = plot_herbivore[0]
            self._animal_count.legend(loc="upper left", prop={"size": 6})
        elif self._carnivore_curve is not None:
            x_data = self._herbivore_curve.get_data()[0]
            y_data = self._herbivore_curve.get_data()[1]
            x_new = np.arange(x_data[-1] + 1, x_limit)
            if len(x_new) > 0:
                y_new = np.full(x_new.shape, np.nan)
                x_stack = np.hstack((x_data, x_new))
                y_stack = np.hstack((y_data, y_new))
                self._herbivore_curve.set_data((x_stack, y_stack))

    def subplot_for_distribution_plot(self):
        """
        Create a subplot for the visualization of how the herbivores and
        carnivores are distributed in heat map.
        """
        # Herbivore distribution
        if self._herbivore_heat is None:
            self._herbivore_heat = self._fig.add_subplot(self._grids[3:6, :6])
            self._herbivore_heat.title.set_text("Distribution for herbivores")
            self._herbivore_heat.axis("off")

        # Carnivore distribution
        if self._carnivore_heat is None:
            self._carnivore_heat = self._fig.add_subplot(self._grids[3:6, 6:])
            self._carnivore_heat.title.set_text("Distribution for carnivores")
            self._carnivore_heat.axis("off")

    def map_graphics(self, map_of_island):
        """
        Plot the given island in a defined subplot
        This code is inspired by a lecture hold by Hans Ekkehard Plesser in january block 2021

        :params: map_of_island: Multi-line string specifying island geography
        """
        #                         R    G    B
        rgb_color_value = {'W': (0.0, 0.0, 1.0),
                           'D': (1.0, 1.0, 0.5),
                           'H': (0.5, 1.0, 0.5),
                           'L': (0.0, 0.6, 0.0)}

        island_rgb = [[rgb_color_value[column] for column in row]
                      for row in map_of_island.splitlines()]

        self._map.imshow(island_rgb)
        ax_lg = self._fig.add_axes([0.39, 0.7, 0.05, 0.2])
        ax_lg.axis("off")
        for ix, name in enumerate(('Water', 'Desert', 'Highland', 'Lowland')):
            ax_lg.add_patch(plt.Rectangle((0., ix * 0.2), 0.3, 0.1, edgecolor='none',
                                          facecolor=rgb_color_value[name[0]]))
            ax_lg.text(0.35, ix * 0.21, name, transform=ax_lg.transAxes)

    def year_update(self, island_year):
        """
        Update the year count for each year

        :params: island_year: present year at island
        """
        self._year_text.set_text(f"year: {island_year}")

    def curves_update(self, year, herbivore_count, carnivore_count):
        """
        Updating the curves of amount of herbivores and carnivores each year
        in the animal count plot

        :params: year: present year
        :params: herbivore_count: count of herbivore each year
        :params: carnivore_count: count of carnivores each year
        """
        herbivore_y_data = self._herbivore_curve.get_ydata()
        herbivore_y_data[year] = herbivore_count
        self._herbivore_curve.set_ydata(herbivore_y_data)

        carnivore_y_data = self._carnivore_curve.get_ydata()
        carnivore_y_data[year] = carnivore_count
        self._carnivore_curve.set_ydata(carnivore_y_data)

    def herbivore_heat_map_update(self, distribution):
        """
        Updating the heatmap for herbivores each year. It contains how many
        herbivores that is present in each cell.

        This code is inspired by a lecture hold by Hans Ekkehard Plesser in january block 2021

        :params: distribution: Information about herbivores in each cell.
                               distribution is a dataframe
        """
        if self._herbivore_dist is not None:
            self._herbivore_dist.set_data(distribution.pivot("Row", "Col", "Herbivore"))
        else:
            self._herbivore_dist = self._herbivore_heat.imshow(distribution.pivot("Row", "Col", "Herbivore"),
                                                               interpolation="nearest", vmin=0,
                                                               vmax=self.cmax["Herbivore"])
            self._herbivore_heat.figure.colorbar(self._herbivore_dist, ax=self._herbivore_heat,
                                                 orientation="vertical")

    def carnivore_heat_map_update(self, distribution):
        """
        Updating the heatmap for carnivores each year. It contains how many
        carnivores that is present in each cell.

        This code is inspired by a lecture hold by Hans Ekkehard Plesser in january block 2021

        :params: distribution: Information about carnivores in each cell.
                               distribution is a dataframe
        """
        if self._carnivore_dist is not None:
            self._carnivore_dist.set_data(distribution.pivot("Row", "Col", "Carnivore"))
        else:
            self._carnivore_dist = self._carnivore_heat.imshow(distribution.pivot("Row", "Col", "Carnivore"),
                                                               interpolation="nearest", vmin=0,
                                                               vmax=self.cmax["Carnivore"])
            self._carnivore_heat.figure.colorbar(self._carnivore_dist, ax=self._carnivore_heat,
                                                 orientation="vertical")

    def age_hist_update(self, herbivore_age, carnivore_age):
        """
        This function updates the age histogram of the animals age

        :param: herbivore_age: gets the age of the herbivores
        :param: carnivore_age: gets the age of the carnivores
        """
        if self._age_histogram is None:
            bin_set = math.ceil((self.hist_spec["age"]["max"]) / (self.hist_spec["age"]["delta"]))
            self._age_hist_fig.clear()
            self._age_hist_fig.set_title("Age - Histogram")
            max_range = self.hist_spec["age"]["max"]
            self._age_hist_fig.hist(herbivore_age["age"], bins=int(bin_set), range=(0, max_range),
                                    histtype="step", color="green")
            self._age_hist_fig.hist(carnivore_age["age"], bins=int(bin_set), range=(0, max_range),
                                    histtype="step", color="red")

    def weight_hist_update(self, herbivore_weight, carnivore_weight):
        """
        This function updates the weight histogram of the animals weight

        :param: herbivore_weight: gets the weight of the herbivores
        :param: carnivore_weight: gets the weight of the carnivores
        """
        if self._weight_histogram is None:
            bin_set = math.ceil((self.hist_spec["weight"]["max"]) / (self.hist_spec["weight"]["delta"]))
            self._weight_hist_fig.clear()
            self._weight_hist_fig.set_title("Weight - Histogram")
            max_range = self.hist_spec["weight"]["max"]
            self._weight_hist_fig.hist(herbivore_weight["weight"], bins=int(bin_set), range=(0, max_range),
                                       histtype="step", color="green")
            self._weight_hist_fig.hist(carnivore_weight["weight"], bins=int(bin_set), range=(0, max_range),
                                       histtype="step", color="red")

    def fitness_hist_update(self, herbivore_fitness, carnivore_fitness):
        """
        This function updates the fitness histogram of the animals fitness

        :param: herbivore_fitness: gets the fitness of the herbivores
        :param: carnivore_fitness: gets the fitness of the carnivores
        """
        if self._fitness_histogram is None:
            bin_set = math.ceil((self.hist_spec["fitness"]["max"]) / (self.hist_spec["fitness"]["delta"]))
            self._fitness_hist_fig.clear()
            self._fitness_hist_fig.set_title("Fitness - Histogram")
            max_range = self.hist_spec["fitness"]["max"]
            self._fitness_hist_fig.hist(herbivore_fitness["fitness"], bins=int(bin_set), range=(0, max_range),
                                        histtype="step", color="green")
            self._fitness_hist_fig.hist(carnivore_fitness["fitness"], bins=int(bin_set), range=(0, max_range),
                                        histtype="step", color="red")

    def update_graphics_per_year(self, distribution, number_of_animal, year, herbivore_fitness, carnivore_fitness,
                                 herbivore_age, carnivore_age, herbivore_weight, carnivore_weight):
        """
        updates the graphics every year, so that these functions are updated for every year that passes. This makes it
        possible to show visualisation for over a hundred years.

        :param distribution: Information about carnivores in each cell, distribution is a dataframe.
        :param number_of_animal: gives us the number of the species
        :param year: present year
        :param herbivore_fitness: gets the fitness of the herbivores
        :param carnivore_fitness: gets the fitness of the carnivores
        :param herbivore_age: gets the age of the herbivores
        :param carnivore_age: gets the age of the carnivores
        :param herbivore_weight: gets the weight of the herbivores
        :param carnivore_weight: gets the weight of the carnivores
        """
        self.herbivore_heat_map_update(distribution)
        self.carnivore_heat_map_update(distribution)
        count_herbivore = number_of_animal["Herbivore"]
        count_carnivore = number_of_animal["Carnivore"]
        self.curves_update(year, count_herbivore, count_carnivore)
        self.year_update(year)
        self.fitness_hist_update(herbivore_fitness, carnivore_fitness)
        self.age_hist_update(herbivore_age, carnivore_age)
        self.weight_hist_update(herbivore_weight, carnivore_weight)
        plt.pause(1e-6)
