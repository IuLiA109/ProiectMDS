from GameAIGenetic import GameControllerGenetic
from game import GameController

if __name__ == "__main__":
    gameHuman = GameController()
    gameHuman.startGame()
    gameAI = GameControllerGenetic()
    gameAI.restartGame()
    while gameHuman.gameStateManager.game_user is None:
        gameHuman.update()

    if gameHuman.gameStateManager.game_user == "ai":
        gameAI.gameStateManager.switchGameUser("ai")
        gameAI.menu.changeType("Level Menu")
        while True:
            gameAI.update()

    if gameHuman.gameStateManager.game_user == "human":
        while True:
            gameHuman.update()


