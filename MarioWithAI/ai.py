# ai_player.py

class AIPlayer:
    def __init__(self, game):
        self.game = game

    def decide_action(self):
        player = self.game.player
        actions = {'move_left': False, 'move_right': False, 'jump': False, 'run': False}
        #print(self.is_obstacle_ahead())
        if self.is_obstacle_ahead():
            actions['jump'] = True
        else:
            actions['move_right'] = True
        return actions

    def is_obstacle_ahead(self):
        player = self.game.player
        for tile in self.game.tilemap.tiles_around(player.pos):
            if tile['type'] in ['floor', 'wall', 'brick_wall', 'pipe_up']:
                if 0 < (tile['pos'][0] * self.game.tilemap.tile_size - player.pos[0]) < 20:
                    return True
        return False
