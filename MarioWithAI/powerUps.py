import pygame
import random

from MarioWithAI.entities import PhysicsEntity
from MarioWithAI.utils import load_image



class PowerUp(PhysicsEntity):
    def __init__(self, game, pos=(0, 0), size=(16, 16)):
        super().__init__(game, 'powerUp', pos, size)
        self.walking = 0
        self.index = 0
        self.image = load_image(game.assets['powerUp/mushroom'])

