import pygame
from constants import *


class GameStateManager:
    def __init__(self, gameState):
        self.gameState = gameState
        self.previousGameState = None

    def switchGameState(self, gameState, menuType=None):
        self.previousGameState = self.gameState
        self.gameState = gameState

        # I don't need a loading screen when accessing the Menu
        if gameState != "Menu":
            self.game.renderLoadingScreen()

        if "Level" in gameState:
            self.game.advanceToNextLevel()
