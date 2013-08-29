import pygame, sys, os
from sound import *

class Pause_screen(object):
    
    def __init__(self,title_screen_image):
        self.title_screen_image = pygame.image.load(os.path.join('image', title_screen_image)).convert_alpha()
        self.image_dimensions = self.title_screen_image.get_rect()
        self.unpauseSound = pygame.mixer.Sound(os.path.join('sound', "unpause.wav"))
        
    def draw(self,screen):
        runTitleScreen = 1
        pygame.mixer.music.set_volume(0.1)
        while runTitleScreen:
            for event in pygame.event.get() :
                if event.type == pygame.QUIT: #if window close clicked
                    pygame.quit() # quit the game
                    sys.exit() # exit the system
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_ESCAPE :
                        runTitleScreen = 0
                        pygame.mixer.music.set_volume(1.0)
                        self.unpauseSound.play()

            screen.blit(self.title_screen_image, self.image_dimensions)
            pygame.display.flip()