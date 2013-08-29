import pygame, sys, os

class Game_over_screen(object):
    
    def __init__(self,title_screen_image, restart_button_image, exit_button_image):
        self.gameOver = pygame.mixer.Sound(os.path.join('sound', "gameover.ogg"))
        # game over screen variables
        #self.title_screen_image = pygame.image.load(title_screen_image)
        #self.title_image_dimensions = self.title_screen_image.get_rect()
	self.gameOverImage = pygame.image.load(os.path.join('image','gameover3.png'))
        
        # restart button variables
        self.restart_button_image = pygame.image.load(os.path.join('image','main-menu.png'))
        (self.restart_button_size_x, self.restart_button_size_y) = self.restart_button_image.get_size()
        self.restart_button_x = 365
        self.restart_button_y = 475
        self.restart_button_coordinates = (self.restart_button_x, self.restart_button_y)
        
        # exit button variables
        self.exit_button_image = pygame.image.load(os.path.join('image', 'Exit-Game.png'))
        (self.exit_button_size_x, self.exit_button_size_y) = self.exit_button_image.get_size()
        self.exit_button_x = 365
        self.exit_button_y = 575
        self.exit_button_coordinates = (self.exit_button_x, self.exit_button_y)
        
        self.outLine = pygame.image.load(os.path.join('image', 'outline.png'))
        
    def draw(self,screen, level):
        # constants
        LEFT_MOUSE_BUTTON = 1
        self.level = level
        # display title screen
        run_title_screen = 1
        self.gameOver.play(-1)
        while run_title_screen:
	    mouse_x, mouse_y = pygame.mouse.get_pos()
            pygame.mouse.set_visible(True) # show the mouse cursor for clickable menu
            for event in pygame.event.get() :
                if event.type == pygame.QUIT: #if window close clicked
                    pygame.quit() # quit the game
                    sys.exit() # exit the system
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_MOUSE_BUTTON: # User clicked somewhere
                    x, y = event.pos
                    if x >= self.exit_button_x and x <= (self.exit_button_x + self.exit_button_size_x) and y <= (self.exit_button_y + self.exit_button_size_y) and y >= self.exit_button_y:
                        pygame.quit()     
			sys.exit()
			self.gameOver.stop()
                    elif x >= self.restart_button_x and x <= (self.restart_button_x + self.restart_button_size_x) and y <= (self.restart_button_y + self.restart_button_size_y) and y >= self.restart_button_y:
                        run_title_screen = 0
			self.gameOver.stop()
                        
            screen.blit(self.gameOverImage, (265, 200))
            screen.blit(self.restart_button_image, self.restart_button_coordinates)
            screen.blit(self.exit_button_image, self.exit_button_coordinates)
	    if mouse_x >= self.exit_button_x and mouse_x <= (self.exit_button_x + self.exit_button_size_x) and mouse_y <= (self.exit_button_y + self.exit_button_size_y) and mouse_y >= self.exit_button_y:
		screen.blit(self.outLine, (self.exit_button_x, self.exit_button_y))
	    if mouse_x >= self.restart_button_x and mouse_x <= (self.restart_button_x + self.restart_button_size_x) and mouse_y <= (self.restart_button_y + self.restart_button_size_y) and mouse_y >= self.restart_button_y:
		screen.blit(self.outLine, (self.restart_button_x, self.restart_button_y))
		
            pygame.display.flip()