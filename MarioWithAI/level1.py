import pygame

from MarioWithAI.enemy import Enemy
from constants import *
from tiles import *
from gameStateManager import GameStateManager

class Level1:
    def __init__(self, game):
        self.game = game
        self.enemiesList = []
        self.init_Level_1()

    def init_Level_1(self):

        self.game.background.fill((108, 190, 237))
        self.game.tilemap = Tilemap(self.game)

        ''' Incarcam pe tilemap harta levelului 1 '''
        self.game.tilemap.load("Levels/level1.json")

        self.enemiesList.append(Enemy(self.game))
        self.enemiesList.append(Enemy(self.game))
        #enemy1 = Enemy(self)
        #enemy2 = Enemy(self)

        ''' Setam pozitia initiala a playerului '''
        self.game.player.pos = [50, 10]
        self.enemiesList[0].pos = [70, 10]
        self.enemiesList[1].pos = [200, 10]


    def updateLevel1(self):
        self.game.updateCamera()
        self.game.player.update()
        for enemy in self.enemiesList:
            enemy.update()


    def checkEvents(self, eventList):
        self.game.player.checkEvents(eventList)

    def renderLevel1(self, surf):

        self.game.tilemap.render(surf)
        self.game.player.render(surf)
        for enemy in self.enemiesList:
            enemy.render(surf)



