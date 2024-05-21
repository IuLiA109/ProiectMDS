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
        self.aux_time = 100

    def checkEvents(self, eventList):
        self.game.player.checkEvents(eventList)

    def init_Level(self):
        self.game.player.loadPlayer()

    def updateTime(self):
        ''' metoda auxiliara pana implementez un cronometru care merge si pentru Pauza '''

        self.aux_time -= 2.5
        if self.aux_time <= 0:
            self.current_time -= 1
            self.aux_time = 100

    def updateLevel(self):
        pygame.mixer.music.load('data/sounds/main_theme.ogg')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        self.sfx['soundtrack'].play(-1)

        if self.current_time <= 0:
            self.game.gameStateManager.switchGameState("Menu", "Game Over Menu") # Or Start Menu

        self.game.updateCamera()
        self.game.player.update()
        self.updateTime()

        for enemy in self.enemiesList:
            # will only update enemies that are in range with player
            enemy.showIfIsOnScreen()
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
