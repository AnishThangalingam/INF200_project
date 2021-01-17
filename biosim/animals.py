# -*- encoding: utf-8 -*-

"""
This script contains a main class called animal and two subclasses called
Herbivore and Carnivore. The main class contains characteristics that are common
to the Herbivore and Carnivore.

Purpose of this function is to give detailed information about the animal
and their behaviors in the Island.

To use this script the user has to have installed the math and random
package to the Python environment.
"""

__author__ = "Majorann Thevarjah & Anish Thangalingam"
__email__ = "Majorann.thevarajah@nmbu.no & Anish.thangalingam@nmbu.no"

import math
import random


class Animal:
    parameters = {}

    @classmethod
    def parameter_set(cls, new_parameters):
        """This function gives the ange to update the parameters"""
        for param_name in new_parameters:
            if param_name not in cls.parameters:
                raise KeyError("Invalid parameter name")

        for param_name in cls.parameters:
            if param_name in new_parameters:
                if new_parameters[param_name] < 0:
                    raise ValueError("Parameter must be non-negative")
        cls.parameters.update(new_parameters)

    def __init__(self, age=None, weight=None):
        """
        # legg inn kommentar
        """
        if age is None:
            self._age = 0
        elif age < 0:
            raise ValueError('The age must be non-negative')
        else:
            self._age = age

        if weight is None:
            self._weight = self.calculated_weight()
        elif weight < 0:
            raise ValueError('The weight must be non-negative')
        else:
            self._weight = weight

    @classmethod
    def calculated_weight(cls):
        """
        Calculate birth weight of the animal from gaussian distribution
        """
        return random.gauss(cls.parameters['w_birth'], cls.parameters['sigma_birth'])

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    def grows_in_age(self):
        """
        Animals are growing up in age every year.
        """
        self._age += 1

    def weight_lose(self):
        """
        The animal decreases every year by the given factor "eta"
        """
        weight_to_reduce = self.weight * (1 - self.parameters['eta'])
        self.weight = weight_to_reduce

    @property
    def fitness(self):
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

    def baby(self, number_of_animal):
        """ A function where it check each animals probability to give birth in a year """
        probability = min(1, self.parameters["gamma"] * self.fitness * (number_of_animal - 1))
        random_number_check = random.random()

        if self.weight < self.parameters["zeta"] * (self.parameters["w_birth"] + self.parameters["sigma_birth"]):
            return None
        elif random_number_check < probability:
            new_baby = type(self)()
            if new_baby.weight * self.parameters["xi"] < self.weight:
                self.weight -= self.parameters["xi"] * new_baby.weight
                return new_baby
            else:
                return None
        else:
            return None

    def death(self):
        """
        If the weight is 0 than the animal is dead.
        If the weight is greater than 0 than we have to compare
        the death probability against a random number and will return
        the result, either False or True
        :return:
        """

        death_probability = self.parameters["omega"] * (1 - self.fitness)
        if self.weight == 0:
            return True
        else:
            return random.random() < death_probability

    def possible_for_moving(self):
        """Chek the possible for an animal to move to an another cell or not"""
        probability = self.parameters["mu"] * self.fitness
        return random.random() < probability


class Herbivore(Animal):
    """
    Husk å legge inn kommentar her når alt er ferdig, jeg heter majorann
    """

    parameters = {
        "w_birth": 8.0,
        "sigma_birth": 1.5,
        "beta": 0.9,
        "eta": 0.05,
        "a_half": 40.0,
        "phi_age": 0.6,
        "w_half": 10.0,
        "phi_weight": 0.1,
        "mu": 0.25,
        "gamma": 0.2,
        "zeta": 3.5,
        "xi": 1.2,
        "omega": 0.4,
        "F": 10.0,
        "DeltaPhiMax": None,
    }

    def __init__(self, age=None, weight=None):
        super().__init__(age, weight)

    def eat(self, amount_of_food):
        """
        Calculate the new weight when the animal takes a certain amount of food.
        The new weight is calculated by beta*F, where F are amount of fodder
        """
        self._weight += self.parameters["beta"] * amount_of_food


class Carnivore(Animal):
    """Carnivore class is a subclass to class Animal. Legge til mere tekst"""

    parameters = {
        "w_birth": 6.0,
        "sigma_birth": 1.0,
        "beta": 0.75,
        "eta": 0.125,
        "a_half": 40.0,
        "phi_age": 0.3,
        "w_half": 4.0,
        "phi_weight": 0.4,
        "mu": 0.4,
        "gamma": 0.8,
        "zeta": 3.5,
        "xi": 1.1,
        "omega": 0.8,
        "F": 50.0,
        "DeltaPhiMax": 10.0,
    }

    def __init__(self, age=None, weight=None):
        """Husk å legge til kommentar"""
        super().__init__(age, weight)
        self.kill_probability = None

    def probability_to_kill(self, herbivore):
        """Legg til kommentar"""
        if self.fitness <= herbivore.fitness:
            self.kill_probability = 0
        elif 0 < self.fitness - herbivore.fitness < self.parameters["DeltaPhiMax"]:
            self.kill_probability = (self.fitness - herbivore.fitness) / self.parameters["DeltaPhiMax"]
        else:
            self.kill_probability = 1

        return random.random() < self.kill_probability

    def carnivore_eat(self, herbivore_least_fit):
        amount_of_food = 0
        update_herbivore = []
        killed_herbivore = []
        appetite = self.parameters["F"]

        for herbivore in herbivore_least_fit:
            if herbivore.fitness >= self.fitness:
                break
            if amount_of_food >= appetite:
                break
            if self.probability_to_kill(herbivore) is True:
                killed_herbivore.append(herbivore)
                if herbivore.weight + amount_of_food < appetite:
                    amount_of_food += herbivore.weight
                    self.weight += self.parameters["beta"] * herbivore.weight
                else:
                    self.weight += (self.parameters["F"] - amount_of_food) * self.parameters["beta"]
                    amount_of_food += self.parameters["F"] - amount_of_food
        for herb in herbivore_least_fit:
            if herb not in killed_herbivore:
                update_herbivore.append(herb)
        return update_herbivore
