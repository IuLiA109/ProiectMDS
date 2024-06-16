from gameAI import GameControllerAI

if __name__ == "__main__":
    game = GameControllerAI()
    game.startGame()
    while True:
        game.update()