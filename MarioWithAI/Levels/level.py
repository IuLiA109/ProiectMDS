import pygame

class Level:
    def __init__(self, game):
        self.game = game
        self.enemiesList = []
        self.powerUpsList = []
        self.enemiesPositions = []
        self.powerUpsPositions = []
        self.nrOfEnemies = 0
        self.nrOfPowerUps = 0
        self.current_time = 300

    def checkEvents(self, eventList):
        self.game.player.checkEvents(eventList)

    def init_Level(self):
        self.game.player.loadPlayer()

    def updateLevel(self):
        self.game.updateCamera()
        self.game.player.update()
        for enemy in self.enemiesList:
            # will only update enemies that are in range with player
            enemy.isOnScreen()
            enemy.update()
        for powerUp in self.powerUpsList:
            powerUp.isOnScreen()
            powerUp.update()

    def renderLevel(self, surf, offset=(0, 0)):
        self.game.tilemap.render(surf, offset)
        self.game.player.render(surf, offset)
        for enemy in self.enemiesList:
            enemy.render(surf, offset)
        for powerUp in self.powerUpsList:
            powerUp.render(surf, offset)
