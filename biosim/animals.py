# -*- encoding: utf-8 -*-

__author__ = "Majorann Thevarjah & Anish Thangalingam"
__email__ = "Majorann.thevarajah@nmbu.no & Anish.thangalingam@nmbu.no"

import math
import numpy as np
import random


class Animal:
    parameters = {}

    def __init__(self, age=None, weight=None):
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

    @classmethod
    def calculated_weight(cls):
        """
        Calculate birth weight of the animal from gaussian distribution
        """
        return random.gauss(cls.parameters['w_birth'], cls.parameters['sigma_birth'])

    def grows_in_age(self):
        """
        Animals are growing up in age every year.
        """
        self.age += 1

    def weight_lose(self):
        """
        The animal decreases every year by the given factor "eta"
        """
        weight_to_reduce = self.weight * (1 - self.parameters['eta'])
        self.weight = weight_to_reduce

        self.fitness = self.get_fitness()

    def eat(self, amount_of_food):
        """
        Calculate the new weight when the animal takes a certain amount of food
        The new wight is calculatet by beta*F, where F are amount of fodder.
        """
        self.weight += self.parameters['beta'] * amount_of_food

        self.fitness = self.get_fitness()

    def get_fitness(self):
        """
        Find the fitness of the animals.
        If the with is is more than 0, the fitness will be calculated by this formula:
        q^(+) * q^(-), where q^(+) = 1/(1+exp(phi age*(age-a_half))
        and  q^(-) = 1/(1+exp(phi weight*(weight-w_half))
        """
        q_plus = 1 / (1 + math.exp(
            self.parameters["phi_age"] * (self.age - self.parameters["a_half"])
        ))
        q_minus = 1 / (1 + math.exp(
            -self.parameters["phi_weight"] * (self.weight - self.parameters["w_half"])
        ))

        if self.weight <= 0:
            return 0
        else:
            return q_plus * q_minus

    def birth_prob(self, number_of_animal):
        """
        Finds the probability of giving birth
        """

        test = self.parameters['zeta'] * (self.parameters['w_birth'] + self.parameters['sigma_birth'])
        if number_of_animal >= 2 and self.weight >= test:
            return min(1, self.parameters['gamma'] * self.fitness * (number_of_animal - 1))

        else:
            return 0

    def birth_take_place(self, number_of_animal):
        """
        Return True if an animal give a birth by
        checking the probability of a child being born with a random number
        """
        create_random_number = np.random.random()
        birth_probability = self.birth_prob(number_of_animal)

        if birth_probability >= create_random_number:
            return True