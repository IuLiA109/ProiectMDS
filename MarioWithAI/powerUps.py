import pygame
import random

from constants import VIRTUALSCREEN_WIDTH
from entities import PhysicsEntity
from utils import load_image


class PowerUp(PhysicsEntity):
    def __init__(self, game, pos=(0, 0), size=(16, 16)):
        super().__init__(game, 'powerUp/mushroom', pos, size, action='')
        self.walking = 0
        self.index = 0
        self.walking_animation_frame = 0
        self.walking_animation_duration = 250
        self.walking_animation_timer = 0
        self.animation = self.game.assets['powerUp/mushroom/run']
        self.image = self.game.assets['powerUp/mushroom']

    def check_collision_with_player(self):
        player_rect = self.game.player.rect()
        hitbox = self.rect()

        if hitbox.colliderect(player_rect):
            print("sau attins")
            #self.die()
        else:
            print("nu a fost atins")
            #self.game.running = False

    def die(self,level):
        level.powerUpsList.remove(self)

    def isOnScreen(self):
        if self.game.camera[0] + VIRTUALSCREEN_WIDTH < self.pos[0]:
            return False
        self.walking = 1
        return True

    def update(self):
        if self.walking:
            if (self.collisions['right'] or self.collisions['left']):
                self.flip = not self.flip

                self.movement = (- 0.5 if self.flip else 0.5, self.movement[1])
            else:
                self.movement = (- 0.5 if self.flip else 0.5, self.movement[1])

        self.check_collision_with_player()
        #self.move()

       # super().update()


        if self.pos[1] <= self.game.virtual_screen.get_height():
            self.action = 'run'
        else:
            self.action = 'stay'
            self.die()

        #self.animation.update()
