import pygame

from enemy import Enemy
from constants import *
from tiles import *
from gameStateManager import GameStateManager
from Levels.level import Level


class Level1(Level):
    def __init__(self, game):
        super().__init__(game)
        self.init_Level()

    def init_Level(self):
        self.game.player.loadNewPlayer()
        # super().init_Level()

        self.game.background.fill((108, 190, 237))
        self.game.tilemap = Tilemap(self.game)

        self.enemiesPositions = [(400, 200), (650, 200), (850, 200), (1108, 10), (1140, 10), (1368, 200), (1388, 200),
                                 (1528, 200), (1638, 200), (1658, 200), (1942, 200), (1962, 200), (2002, 200),
                                 (2027, 200), (2646, 200), (2666, 200)]
        self.nrOfEnemies = 16

        ''' Incarcam pe tilemap harta levelului 1 '''
        # levels/level1.json
        self.game.tilemap.load("Maps/map1.json")

        for i in range(self.nrOfEnemies):
            self.enemiesList.append(Enemy(self.game, self.enemiesPositions[i]))

        ''' Setam pozitia initiala a playerului '''
        self.game.player.pos = [50, 10]

    def checkEvents(self, eventList):
        super().checkEvents(eventList)
        ''' Here we check for the event of ending the Level and going through to the next one '''
        # if Something ->
        # then self.game.gameStateManager.switchGameState("Level 2")
