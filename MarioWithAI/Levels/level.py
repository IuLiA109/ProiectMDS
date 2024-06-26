import pygame

from sound import Sound
#from MarioWithAI.sound import Sound
import random

class Level:
    def __init__(self, game, moves=None):
        self.game = game
        self.enemiesList = []
        self.powerUpsList = []
        self.enemiesPositions = []
        self.powerUpsPositions = []
        self.nrOfEnemies = 0
        self.nrOfPowerUps = 0
        self.current_time = 300
        self.aux_time = 100
        self.frame = 0
        # self.moves = self.generate_moves()
        self.moves = moves
        self.empty = []

    def generate_moves(self):
        return [int(random.uniform(1, 5)) for _ in range(10000)]

    def checkEvents(self, eventList):
        self.game.player.checkEvents(eventList)

    def checkEventsGenetic(self, eventList):
        #pass
        # print(self.frame)
        #move = int(random.uniform(1, 5))
        move = self.moves[self.frame]
        #print(move, self.frame)
        self.empty.append(move)
        self.game.player.move_player(self.empty)
        self.empty = []
        self.frame += 1


    def init_Level(self):

        self.current_time = 300
        self.aux_time = 100
        self.game.player.loadPlayer()
        self.game.sound.play_music('soundtrack')  # Play background music when level starts
        self.frame = 0

    def updateTime(self):
        ''' metoda auxiliara pana implementez un cronometru care merge si pentru Pauza '''

        self.aux_time -= 2.5
        if self.aux_time <= 0:
            self.current_time -= 1
            self.aux_time = 100


    def get_enemiesPositions(self):
        self.updateEnemiesPositions()
        return self.enemiesPositions
    def updateEnemiesPositions(self):
        self.enemiesPositions = []
        for enemy in self.enemiesList:
            self.enemiesPositions.append(enemy.pos)

    def updateLevel(self):

        self.updateEnemiesPositions()

        if self.current_time <= 0:
            self.game.sound.play_sfx('death')  # Play death sound if time runs out
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
