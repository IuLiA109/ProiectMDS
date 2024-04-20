import sys
from xml.dom.minidom import Entity

import pygame

from MarioWithAI.game import GameController
from constants import *
from gameStateManager import GameStateManager
from utils import load_images, load_image
from level1 import Level1
from tiles import *
from constants import *

class Editor:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('editor')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.assets = {
            'floor': load_image('tiles/floor.png'),
            'wall': load_image('tiles/wall.png'),
            # 'platform': load_image('tiles/platform.png'),
            # 'mistery': load_image('tiles/mistery.png'),
        }

        self.movement = [False, False, False, False]

        self.tilemap = Tilemap(self, tile_size=16)

        try:
            self.tilemap.load('map.json')
        except FileNotFoundError:
            pass

        self.scroll = [0, 0]

        self.tile_list = list(self.assets)
        self.tile_group = 0
        self.tile_variant = 0

        self.clicking = False
        self.right_clicking = False
        self.shift = False
        self.ongrid = True

        self.clicking = False
        self.right_clicking = False

        # partea pentru schimbarea intre variante
        self.shift = False

    def run(self ):
        while True:
            self.display.fill((0, 0, 0))



            current_tile_img = self.assets[self.tile_list[self.tile_group]].copy()
            current_tile_img.set_alpha(100)

            self.tilemap.render(self.display)

            mpos = pygame.mouse.get_pos()
            mpos = (mpos[0] / RENDER_SCALE, mpos[1] / RENDER_SCALE)

            tile_pos = (int((mpos[0] + self.scroll[0]) // self.tilemap.tile_size), int((mpos[1] + self.scroll[1]) // self.tilemap.tile_size))

            self.display.blit(current_tile_img, (tile_pos[0] * self.tilemap.tile_size - self.scroll[0], tile_pos[1] * self.tilemap.tile_size - self.scroll[1]))

            self.scroll[0] += (self.movement[1] - self.movement[0]) * 2
            self.scroll[1] += (self.movement[3] - self.movement[2]) * 2

            if self.clicking:
                self.tilemap.tilemap[str(tile_pos[0]) + ';' + str(tile_pos[1])] = {'type': self.tile_list[self.tile_group], 'variant': self.tile_variant, 'pos': tile_pos}

            if self.right_clicking:
                tile_loc = str(tile_pos[0]) + ';' + str(tile_pos[1])
                if tile_loc in self.tilemap.tilemap:
                    del self.tilemap.tilemap[tile_loc]

            # cand o sa avem mai multe variante la  tileuri, o sa trebuiasca sa facem un sistem de scroll al variantei dar acum nu avem
            # current_tile_img = self.assets[self.tile_list[self.tile_group]][self.tile_variant].copy()


            self.display.blit(current_tile_img, (5, 5))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicking = True
                    if event.button == 3:
                        self.right_clicking = True
                        # Pentru cand/daca o sa avem mai multe variante la tileuri
                        #   ''''if self.shift:
                        #       if event.button == 4:
                        #           self.tile_variant = (self.tile_variant - 1) % len(self.assets[self.tile_list[self.tile_group]])
                        #      if event.button == 5:
                        #          self.tile_variant = (self.tile_variant + 1) % len(self.assets[self.tile_list[self.tile_group]])

                    if event.button == 4:
                        self.tile_group = (self.tile_group - 1) % len(self.tile_list)
                        # self.tile_variant = 0
                    if event.button == 5:
                        self.tile_group = (self.tile_group + 1) % len(self.tile_list)
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicking = False
                    if event.button == 3:
                        self.right_clicking = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                    if event.key == pygame.K_g:
                        self.ongrid = not self.ongrid
                    if event.key == pygame.K_t:
                        self.tilemap.autotile()
                    if event.key == pygame.K_o:
                        self.tilemap.save('map.json')
                    if event.key == pygame.K_LSHIFT:
                        self.shift = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False
                    if event.key == pygame.K_LSHIFT:
                        self.shift = False

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)


Editor().run()
