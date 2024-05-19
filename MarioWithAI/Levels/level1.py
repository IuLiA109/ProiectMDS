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

        ''' Incarcam pe tilemap harta levelului 1 '''
        # levels/level1.json
        self.game.tilemap.load("map.json")

        self.enemiesList.append(Enemy(self.game))
        self.enemiesList.append(Enemy(self.game))
        self.enemiesList.append(Enemy(self.game))
        #enemy1 = Enemy(self)
        #enemy2 = Enemy(self)

        ''' Setam pozitia initiala a playerului '''
        self.game.player.pos = [50, 10]
        self.enemiesList[0].pos = [70, 10]
        self.enemiesList[1].pos = [200, 10]
        self.enemiesList[2].pos = [270, 10]

    def checkEvents(self, eventList):
        super().checkEvents(eventList)
        ''' Here we check for the event of ending the Level and going through to the next one '''
        # if Something ->
        # then self.game.gameStateManager.switchGameState("Level 2")



