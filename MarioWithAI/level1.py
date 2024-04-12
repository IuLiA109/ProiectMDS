import pygame
from constants import *
from tiles import *
from gameStateManager import GameStateManager

class Level1:
    def __init__(self, game):
        self.game = game
        self.init_Level_1()
        self.game.enemiesList = []
        self.game.lastSkeletonFighterSpawn = 0

    def init_Level_1(self):

        self.game.background.fill((100, 50, 80))
        self.game.tilemap = Tilemap(self.game)

        ''' Incarcam pe tilemap harta levelului 1 '''
        self.game.tilemap.load("Levels/level1.json")

        ''' Setam pozitia initiala a playerului '''
        self.game.player.pos = [50, 10]
        self.game.enemy.pos = [70, 10]

    def updateLevel1(self):
        self.game.updateCamera()
        self.game.player.update()
        self.game.enemy.update()


    def checkEvents(self, eventList):
        self.game.player.checkEvents(eventList)

    def renderLevel1(self, surf):

        self.game.tilemap.render(surf)
        self.game.player.render(surf)
        self.game.enemy.render(surf)



