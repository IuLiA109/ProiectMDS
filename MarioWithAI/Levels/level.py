import random

import pygame

from sound import Sound
#from MarioWithAI.sound import Sound

populatie_size = 100
cromozom_length = 50
generatii = 1000
mutation_rate = 0.01

class Level:
    def __init__(self, game, moves):
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
        #self.moves = self.generate_moves()
        self.moves = moves
        self.empty = []

    #def checkEvents(self, eventList):
        #self.game.player.checkEvents(eventList)

    def generate_moves(self):
        return [int(random.uniform(1, 5)) for _ in range(10000)]

    def checkEvents(self, eventList):
        #pass
        #print(self.frame)
        #move = int(random.uniform(1, 5))
        move = self.moves[self.frame]
        #print(move, self.frame)
        self.empty.append(move)
        self.game.player.move_player(self.empty)
        self.empty = []
        self.frame += 1

    def evaluate_fitness(self, cromozom):
        return sum(cromozom)

    def generate_populatie(self, size, length):
        return [[random.randint(0, 1) for _ in range(length)] for _ in range(size)]

    def selection(self, populatie):
        sorted_populatie = sorted(populatie, key=lambda x: self.evaluate_fitness(x), reverse=True)
        return sorted_populatie[:populatie_size // 2]

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(1, cromozom_length - 1)
        return parent1[:crossover_point] + parent2[crossover_point:]

    # Mutarea cromozomilor
    def mutate(self, cromozom):
        for i in range(len(cromozom)):
            if random.random() < mutation_rate:
                cromozom[i] = 1 - cromozom[i]
        return cromozom

    def generate_populatie(self, size=10):
        return [int(random.randint(1, 5)) for _ in range(size)]

    def init_Level(self):
        self.game.player.loadPlayer()
        self.game.sound.play_music('soundtrack')  # Play background music when level starts

    def updateTime(self):
        ''' metoda auxiliara pana implementez un cronometru care merge si pentru Pauza '''

        self.aux_time -= 2.5
        if self.aux_time <= 0:
            self.current_time -= 1
            self.aux_time = 100

    def updateLevel(self):
        #if self.current_time < 200 and self.game.player.pos[0] < 200:
            #self.game.player.die()

        #if self.current_time < 297 and (self.game.player.pos[0] / (300 - self.current_time)) <= 2:
            #self.game.player.die()

        if self.current_time <= 0:
            self.game.player.die()
            #self.game.sound.play_sfx('death')  # Play death sound if time runs out
            #self.game.gameStateManager.switchGameState("Menu", "Game Over Menu") # Or Start Menu

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
