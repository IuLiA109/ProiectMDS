from game import GameController

class GameControllerAI(GameController):
    def __init__(self):
        super().__init__()



    def restartGame(self):
        self.currentLevel.init_Level()


    def startGame(self):
        self.loadNewGame()

    def loadNewGame(self):
        self.player.loadNewPlayer()
        self.current_world = 1
        self.current_level = 1
        self.saveGame()

    '''
    def loadLevel1(self):
        self.Level1 = Level1(self)
        self.Level1.init_Level_1()
    '''

    def setCurrentLevel(self, levelNumber):
        if levelNumber == 1:
            self.current_level = 1
            self.Level1 = Level1(self)
            self.currentLevel = self.Level1
        if levelNumber == 2:
            self.current_level = 2
            self.Level2 = Level2(self)
            self.currentLevel = self.Level2

        self.saveGame()

    def saveGame(self):
        self.player.savePlayer()

        directory = "saves/"
        file = open(directory + 'gameSave1.json', 'w')

        data = {}
        data['CURRENT_WORLD'] = self.current_world
        data['CURRENT_LEVEL'] = self.current_level

        json_data = json.dumps(data, indent=4)
        file.write(json_data)

    def loadGame(self):
        directory = "saves/"
        file = open(directory + 'gameSave1.json', 'r')
        data = json.load(file)

        self.current_world = data['CURRENT_WORLD']
        self.current_level = data['CURRENT_LEVEL']

        self.player.loadPlayer()

    def advanceToNextLevel(self):

        self.current_level += 1

        if self.current_level > 4:
            self.current_level = 1
            self.current_world += 1

        self.saveGame()

    def renderLoadingScreen(self):

        loadingScreenImg = self.loadingImage
        loadingScreenImg = pygame.transform.scale(loadingScreenImg, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.blit(loadingScreenImg, (0, 0))
        pygame.display.flip()

    def updatePlayer(self):
        # update the player
        self.player.update()

    def updateCamera(self):

        # camera follows the player with a smooth effect , MIGHT CHANGE VALUES LATER
        last_camera = self.camera[0]

        self.camera[0] += (self.player.pos[0] - self.camera[0] - VIRTUALSCREEN_WIDTH / 2 + self.player.size[
            0] / 2) / CAMERA_FOLLOW_RATE

        if self.camera[0] < last_camera:
            self.camera[0] = last_camera
        #self.camera[1] += (self.player.pos[1] - self.camera[1] - VIRTUALSCREEN_HEIGHT / 2 + self.player.size[
           # 1] / 2) / CAMERA_FOLLOW_RATE
        self.render_camera = [(self.camera[0]), (self.camera[1])]

    def update(self):
        # print(self.currentLevel.enemiesList[0].pos)
        #print(self.player.lives)

        if self.running == False:
            pygame.quit()
            quit()

        if self.gameStateManager.gameState == "Menu":
            self.menu.update()

        if self.gameStateManager.gameState == "Level 1":
            self.Level1.updateLevel()

        if self.gameStateManager.gameState == "Level 2":
            self.Level2.updateLevel()

        self.hud.updateHUD()

        # I don't want the clock to be ticking when in the menu
        # As I could exploit the time
        if self.gameStateManager.gameState != "Menu":
            self.clock.tick(FPS)

        self.checkGameEvents()
        self.render()

    def resetPlayerMovement(self):
        self.player.movement = [0, 0]
        self.player.acceleration = [0, 0]
        self.player.velocity = [0, 0]

    def checkGameEvents(self):

        self.eventList = pygame.event.get()

        if self.gameStateManager.gameState == "Menu":
            self.menu.handleEvents(self.eventList)

        #if self.gameStateManager.gameState == "Level 1":
            #self.Level1.checkEvents(self.eventList)
        if "Level " in self.gameStateManager.gameState:
            self.currentLevel.checkEvents(self.eventList)


        for event in self.eventList:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.gameStateManager.gameState != "Menu":
                        self.gameStateManager.switchGameState("Menu","Pause Menu")
                    else:
                        self.gameStateManager.returnToPreviousGameState()


    def render(self):

        # render background on the virtual screen
        self.virtual_screen.blit(self.background, (0, 0))
        self.background.fill((92, 148, 252))
        self.virtual_screen.blit(self.background_image, (-self.camera[0], 45))

        self.hud.renderHUD(self.virtual_screen)

        # --- Rendering the correct Scene based on the gameState ---

        #if self.gameStateManager.gameState == "Level 1":
            #self.Level1.renderLevel(self.virtual_screen, self.render_camera)

        if "Level " in self.gameStateManager.gameState:
            self.currentLevel.renderLevel(self.virtual_screen, self.render_camera)

        # --- Rendering the correct Scene based on the gameState ---


        if self.gameStateManager.gameState == "Menu":
            #self.currentLevel.renderLevel(self.virtual_screen, self.render_camera)

            # If paused I darken the screen
            if self.menu.type == "Pause Menu":
                self.virtual_screen.blit(self.darken_surface, (0, 0))

            self.menu.render(self.virtual_screen)

        # scale the virutal screen onto the actual screen
        scaledScreen = pygame.transform.scale(self.virtual_screen, (SCREEN_WIDTH, SCREEN_HEIGHT), self.screen)
        self.screen.blit(scaledScreen, (0, 0))

        pygame.display.flip()
        pygame.display.update()
