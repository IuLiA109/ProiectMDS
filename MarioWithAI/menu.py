import pygame
from constants import *

SCALING_FACTOR = SCREEN_WIDTH / VIRTUALSCREEN_WIDTH

class Menu:
    def __init__(self, game, type):
        self.type = type
        self.game = game
        self.image = None
        self.loadMenu()

    def changeType(self, type):
        self.type = type
        self.loadMenu()

    def loadMenu(self):
        if self.type == "Pause Menu":
            self.image = pygame.image.load("data/images/menus/PauseMenu.png")

    def handleEvents(self, eventList):
        pass

    def update(self):
        pass

    def render(self, surf):
        surf.blit(self.image, (0, 0))