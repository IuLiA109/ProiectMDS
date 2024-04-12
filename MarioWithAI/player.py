import pygame
import game
from constants import *
from entities import PhysicsEntity

NEIGHBOURS_OFFSET = [[0, 0], [-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]


class Player(PhysicsEntity):  # Inherit from PhysicsEntity
    def __init__(self, game, pos=(0, 0), size=(16, 16)):
        super().__init__(game, 'player', pos, size)

        # Animation frames
        '''
        self.animation_frames = [
            pygame.transform.scale(pygame.image.load("assets/player/frame_1.png").convert_alpha(), size),
            pygame.transform.scale(pygame.image.load("assets/player/frame_2.png").convert_alpha(), size),
            pygame.transform.scale(pygame.image.load("assets/player/frame_3.png").convert_alpha(), size)
        ]
        # Animation variables
        self.current_frame = 0
        self.frame_delay = 350
        self.last_frame_time = 0
        
        self.image = self.animation_frames[self.current_frame]
        '''

        self.image = self.game.assets['player']

        self.size = size
        self.position = list(pos)

        self.game = game
        self.speed = PLAYER_SPEED

    def checkEvents(self, eventList):
        for event in eventList:
            # Movement with W A S D and arrows
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.velocity[1] = -PLAYER_SPEED * 2
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.velocity[1] = PLAYER_SPEED
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.velocity[0] = -PLAYER_SPEED
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.velocity[0] = PLAYER_SPEED

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.velocity[1] = 0
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.velocity[1] = 0
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.velocity[0] = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.velocity[0] = 0

    def render(self, surf):
        surf.blit(self.image, self.pos)
