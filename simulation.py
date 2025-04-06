""" Main program to run a simulation. we are going to make a 0.1s time step. 
Should implement a maximum simulation time where we think the BO is bad. Lets say 25min and any simulation needs.
All times are given in seconds. We use float even if we have integer values, as our simulation will make small steps and then we need this.
"""

from consumables import Sheep, Consumable, Boar, Berries, HuntableAnimal
from units import Villager, Combatant, Unit
from buildings import Building, TownCenter
from utilities import Resources

class Simulation:
    """ Let's simulate Age of Empires early game where we have sheep boar berries and enough gold stone and wood to do whatever."""
    consumables: list[Consumable] = []
    villagers: list[Villager]
    combatants: list[Combatant]
    now: float = 0
    delta_t: float = 0.1
    max_time: float = 25 * 60
    buildings: list[Building]
    population: int
    population_allowed: int
    resources: Resources

    def __init__(self, n_sheep, n_boar, n_berries, n_villagers, target_reached, ):
        """ Target reached is a method that returns true when a certain condition is met."""
        sheep = [Sheep(parent=self)] * n_sheep
        boar = [Boar(self)] * n_boar
        berries = [Berries(self)] * n_berries
        self.consumables.extend(sheep)
        self.consumables.extend(boar)
        self.consumables.extend(berries)
        self.villagers = [Villager(self)] * n_villagers
        self.combatants = [] # For now we ignore the scout that we start with... 
        self.target_reached = target_reached

        self.resources = Resources(food=200, wood=200, gold=100, stone=200)
        self.buildings = [TownCenter(self)]
        self.training_units = []

    def time_step(self):
        if self.now < self.max_time and not self.target_reached(self):
            self.now += self.delta_t
            for consumable in self.consumables:
                if isinstance(consumable, HuntableAnimal):
                    consumable.decay(self.delta_t)
            for building in self.buildings:
                match building:
                    case TownCenter():
                        building.progress(self.now, self.delta_t)
            for villager in self.villagers:
                villager.actions # DO SOMETHING ALREADY

    def get_population(self):
        return len(self.villagers) + len(self.combatants)

    def get_population_allowed(self):
        pop_allow = 0
        for b in self.buildings:
            pop_allow += b.population
        return pop_allow
    
    def add_training_unit(self, unit: Unit):
        if len(self.training_units) + self.get_population() < self.get_population_allowed():
            self.training_units.append(unit)
            return True
        elif unit in self.training_units:
            return True
        else:
            return False