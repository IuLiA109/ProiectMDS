import pygame
import json

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'floor', 'wall', 'brick_wall', 'mystery','mystery/used', 'pipe_up', 'pipe_extension', 'invisible_block'}


class Tilemap:
    def __init__(self, game, tile_size=16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []

        #for i in range(30):
        #   self.tilemap[str(3 + i) + ';10'] = {'type': 'floor', 'variant': 0, 'pos': (3 + i, 10)}
        #  self.tilemap['10;' + str(5 + i)] = {'type': 'wall', 'variant': 0, 'pos': (10, 5 + i)}
        # self.tilemap['20;' + str(5 + i)] = {'type': 'wall', 'variant': 0, 'pos': (20, 5 + i)}


    def setTile(self, pos, tile_type):
        tile_loc = (int(pos[0]), int(pos[1]))
        self.tilemap[str(tile_loc[0]) + ';' + str(tile_loc[1])] = {'type': tile_type, 'pos': tile_loc}

    def hitTileAnimation(self, pos):
        # Make the tile move up and down
        pass

    def load(self, filename):
        f = open(filename, 'r')
        data = json.load(f)
        f.close()

        self.tilemap = data['tilemap']
        self.tile_size = data['tile_size']
        self.offgrid_tiles = data['offgrid_tiles']

    def tiles_around(self, pos):
        tiles = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles

    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in PHYSICS_TILES:
                rects.append(
                    pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size,
                                self.tile_size))
        return rects

    def render(self, surf, offset=(0, 0)):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']],
                      (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1]))

        for x in range(int(offset[0] // self.tile_size), int((offset[0] + surf.get_width()) // self.tile_size + 1)):
            for y in range(int(offset[1] // self.tile_size),
                           int((offset[1] + surf.get_height()) // self.tile_size + 1)):
                loc = str(x) + ';' + str(y)
                if loc in self.tilemap:
                    tile = self.tilemap[loc]
                    surf.blit(self.game.assets[tile['type']], (
                        tile['pos'][0] * self.tile_size - offset[0], tile['pos'][1] * self.tile_size - offset[1]))

    def save(self, path):
        f = open(path, 'w')
        json.dump({'tilemap': self.tilemap, 'tile_size': self.tile_size, 'offgrid_tiles': self.offgrid_tiles}, f)
        f.close()
