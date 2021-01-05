# -*- coding: utf-8 -*-

__author__ = 'Anish Thangalingam, Majorann Thevarajah'
__email__ = 'anish.thangalingam@nmbu.no, majorann.thevarajah@nmbu.no'

"""
The main class is Landscape and has four subclasses which is Water, Highland, Lowland and Desert)

"""

from biosim.animals import herbivores

class Landscape():

    parameters = {}

"""
Got to find out the population in each landscape to know how many species each landscape will have
the animal 


Population
Fitness, the weakest will get eaten first
fodder
calculated population



"""

    def __init__(self):


    # de ulike funksjonene


class Highland(Landscape):
    parameters = {
        "f_max": 300}

class Lowland(Landscape):
    parameters = {
        "f_max": 800}

class Water(Landscape):
    parameters = {
        "f_max": 0}

class Desert(Landscape):
    parameters = {
        "f_max": 0}
