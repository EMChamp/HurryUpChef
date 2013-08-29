import pygame, os
from const import *

class HowTo(object):
    def __init__(self):
        self.screenOne = pygame.image.load(os.path.join('image', 'Tutorial1.jpg'))
        self.screenTwo = pygame.image.load(os.path.join('image', 'Tutorial3.jpg'))
        self.screenThree = pygame.image.load(os.path.join('image', 'Tutorial2.jpg'))
        
    def draw(self, screen):
        run = 1
	counter = 0
        while run:
	    for event in pygame.event.get() :
		if event.type == pygame.QUIT: # If user clicked close (the X button)
		    pygame.quit()     
		    sys.exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
		    counter += 1
		    
	    screen.fill((0,0,0))
	    if counter == 0:
		screen.blit(self.screenOne, POSITION)
	    elif counter == 1:
		screen.blit(self.screenTwo, POSITION)
	    elif counter == 2:
		screen.blit(self.screenThree, POSITION)
	    elif counter == 3:
		run = 0
		
	    pygame.display.flip()