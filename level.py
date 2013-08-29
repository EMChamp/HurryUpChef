import pygame, os

from ingredient import *

class Level(object):
    def __init__(self):
        self.ingredients = Ingredient()
        self.level = self.ingredients.playfield.getLevel()
        print self.level
    