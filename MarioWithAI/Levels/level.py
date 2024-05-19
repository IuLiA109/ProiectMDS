import pygame

class Level:
    def __init__(self, game):
        self.game = game
        self.enemiesList = []
        self.current_time = 300

    def checkEvents(self, eventList):
        self.game.player.checkEvents(eventList)

    def init_Level(self):
        self.game.player.loadPlayer()

    def updateLevel(self):
        self.game.updateCamera()
        self.game.player.update()
        for enemy in self.enemiesList:
            enemy.update()

    def renderLevel(self, surf, offset=(0, 0)):
        self.game.tilemap.render(surf, offset)
        self.game.player.render(surf, offset)
        for enemy in self.enemiesList:
            enemy.render(surf, offset)
