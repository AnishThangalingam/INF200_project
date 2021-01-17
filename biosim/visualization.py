# -*- encoding: utf-8 -*-

__author__ = "Majorann Thevarjah & Anish Thangalingam"
__email__ = "Majorann.thevarajah@nmbu.no & Anish.thangalingam@nmbu.no"

import matplotlib.pyplot as plt


class Visualization:
    """
    Visualization class for the Visualization of the simulation
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

    def creat_a_window(self):
        """
        Creat a window to show the visualization of the simulation
        """
        if self._fig is None:
            self._fig = plt.figure(constrained_layout=True, figsize=(10, 8))
            self._grids = self._fig.add_girdspec(8, 12)

    def map_graphics(self, map_of_island):
        """
        Adding a subplot for map and plot the given island in than subplot
        The code is inspired by a lecture hold by Hans Ekkehard Plesser in january block 2021

        :params: map_of_island: Multi-line string specifying island geography
        """
        if self._map is None:
            self._map = self._fig.add_subplot(self._grids[:3, :5])
            self._map.title.set_text("Island")
            self._map.axis("off")

        #                         R    G    B
        rgb_color_value = {'W': (0.0, 0.0, 1.0),
                           'D': (1.0, 1.0, 0.5),
                           'H': (0.5, 1.0, 0.5),
                           'L': (0.0, 0.6, 0.0)}

        island_rgb = [[rgb_color_value[column] for column in row]
                      for row in map_of_island.splitlines()]

        self._map.imshow(island_rgb)
        ax_lg = self._fig.add_axes([0.39, 0.7, 0.85, 0,2])
        ax_lg.axis("off")
        for ix, name in enumerate(('Water', 'Desert', 'Highland', 'Lowland')):
            ax_lg.add_patch(plt.Rectangle((0., ix * 0.2), 0.3, 0.1, edgecolor='none',
                                          facecolor=rgb_color_value[name[0]]))
            ax_lg.text(0.35, ix * 0.21, name, transform=ax_lg.transAxes)
