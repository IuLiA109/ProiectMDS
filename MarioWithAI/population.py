import playerAI

class Population:
    def __init__(self, size):
        self.player = playerAI.PlayerAI(size)

    def update_live_players(self):
        if self.player.still_alive():
            self.player.think()
            self.player.update()