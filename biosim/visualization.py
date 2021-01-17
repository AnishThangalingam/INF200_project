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

    def creat_a_window(self):
        """
        Creat a window to show the visualization of the simulation
        """
        if self._fig is None:
            self._fig = plt.figure(constrained_layout=True, figsize=(10, 8))
            self._grids = self._fig.add_girdspec(8, 12)
