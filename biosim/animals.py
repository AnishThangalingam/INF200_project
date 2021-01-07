# -*- encoding: utf-8 -*-

__author__ = "Majorann Thevarjah & Anish Thangalingam"
__email__ = "Majorann.thevarajah@nmbu.no & Anish.thangalingam@nmbu.no"

import math
import numpy as np
import random

class Animal:
    parameters = {}

    def __init__(self, age=None, weight = None):
        """
        # legg inn kommentar
        """
        if age is None:
            self.age = 0
        elif age < 0:
            raise ValueError('The age must be non-negative')
        else:
            self.age = age

        if weight is None:
            self.weight = self.calculated_weight()
        elif weight < 0:
            raise ValueError('The weight must be non-negative')
        else:
            self.weight = weight
        self.fitness = self.get_fitness
