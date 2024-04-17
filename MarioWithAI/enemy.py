import pygame
import random

from MarioWithAI.utils import load_image
from constants import *
from entities import PhysicsEntity
class Enemy(PhysicsEntity):
    def __init__(self, game, pos=(0, 0), size=(16, 16)):
        super().__init__(game, 'enemy', pos, size)
        self.walking = 0
        self.index = 0
        self.walking_animation_frame = 0
        self.walking_animation_duration = 250
        self.walking_animation_timer = 0
        self.image = load_image(self.game.assets['enemy/run'] + str(self.walking_animation_frame) + '.png')


    def update_animation(self):
        self.walking_animation_timer += self.game.clock.get_time()
        if self.walking_animation_timer >= self.walking_animation_duration:
            self.walking_animation_timer = 0
            self.walking_animation_frame = 1 - self.walking_animation_frame
            self.image = load_image(self.game.assets['enemy/run'] + str(self.walking_animation_frame) + '.png')


    def update(self):
        if self.walking:
            if (self.collisions['right'] or self.collisions['left']):
                self.flip = not self.flip
                self.movement = (0, self.movement[1])
            else:
                self.movement = (- 0.5 if self.flip else  0.5, self.movement[1])
            self.walking = max(0, self.walking - 1)
        elif random.random() < 0.01:
            self.walking = random.randint(30, 120)

        '''    #incercare de collide enemy - player
        player_rect = self.game.player.rect()
        enemy_rect = self.rect()
        if enemy_rect.colliderect(player_rect):
            #print(player_rect.y)
            #print("-------")
            #print(enemy_rect.y)
            #print("--------------------")
            if enemy_rect.y == player_rect.y + self.game.player.size[1]:
                print("ON HEAD")
                #self.game.running = False
        '''
        super().update()

        if self.movement[0] != 0:
            self.action = 'run'
        else:
            self.action = 'stay'

        self.update_animation()

    def render(self, surf):
        surf.blit(self.image, self.pos)