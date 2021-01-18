# -*- encoding: utf-8 -*-

__author__ = "Majorann Thevarjah & Anish Thangalingam"
__email__ = "Majorann.thevarajah@nmbu.no & Anish.thangalingam@nmbu.no"

import matplotlib.pyplot as plt
import numpy as np


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

    def creat_a_window(self):
        """
        Creat a window to show the visualization of the simulation
        """
        if self._fig is None:
            self._fig = plt.figure(constrained_layout=True, figsize=(10, 8))
            self._grids = self._fig.add_girdspec(8, 12)

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
            template = "Year: {_5d}"
            self._year_count = self._year_count.text(
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
            self._animal_count.title.set_title("Number count for Herbivore and Carnivore")
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
            x_data = self._herbivore_curve.get_data[0]
            y_data = self._herbivore_curve.get_data[1]
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
            self._carnivore_heat = self._fig.add_subplot(self._grids[3:6, :6])
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
        ax_lg = self._fig.add_axes([0.39, 0.7, 0.85, 0.2])
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
        self._year_count.set_text(f"year: {island_year}")

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
