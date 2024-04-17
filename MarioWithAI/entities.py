import pygame
import random

from MarioWithAI.utils import load_image


class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        self.movement = [0, 0]
        self.flip = False
        self.action = 'stay'

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self):
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        frame_movement = (self.movement[0] + self.velocity[0], self.movement[1] + self.velocity[1])

        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in self.game.tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x

        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in self.game.tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y

        if self.movement[0] > 0:
            self.flip = False
        if self.movement[0] < 0:
            self.flip = True

        self.velocity[1] = min(5, self.velocity[1] + 0.1)

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0

    #def render(self, surf):
    #    surf.blit(self.game.assets['player'], self.pos)

'''
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

        ##''    #incercare de collide enemy - player
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
        #''
        super().update()

        if self.movement[0] != 0:
            self.action = 'run'
        else:
            self.action = 'stay'

        self.update_animation()

    def render(self, surf):
        surf.blit(self.image, self.pos)
'''











