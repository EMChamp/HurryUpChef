import pygame, sys, os, random
from sound import *
from howto import *

class Title_screen(object):
    
    def __init__(self,title_screen_image):
        self.title_screen_image = pygame.image.load(os.path.join('image', title_screen_image))
        self.image_dimensions = self.title_screen_image.get_rect()
	self.titleMusic = pygame.mixer.Sound(os.path.join('sound', "title.ogg"))
	self.outLine = Image.load_image('outline.png')
	
	self.tomato_image = pygame.image.load(os.path.join('image', "tomato.png"))
	self.tomato_image2 = pygame.image.load(os.path.join('image', "berry.png"))
	self.tomato_image3 = pygame.image.load(os.path.join('image', "chicken.png"))
	self.tomato_image4 = pygame.image.load(os.path.join('image', "greenpepper.png"))	
	self.tomato_image5 = pygame.image.load(os.path.join('image', "steak.png"))
	self.tomato_image6 = pygame.image.load(os.path.join('image', "egg.png"))	
	
	self.tomato = bounce(257, 300)
	self.tomato2 = bounce(600, 400)
	self.tomato3 = bounce(185, 368)
	self.tomato4 = bounce(500, 200)	
	self.tomato5 = bounce(675, 250)
	self.tomato6 = bounce(75, 225)
	
	self.countDownOne = pygame.image.load(os.path.join('image', "countdown1.png")).convert_alpha()
	self.countDownTwo = pygame.image.load(os.path.join('image', "countdown2.png")).convert_alpha()
	self.countDownThree = pygame.image.load(os.path.join('image', "countdown3.png")).convert_alpha()
	
	self.tutorialButton = Image.load_image('Tutorial.png')
	self.tutorialButton_x = 300
	self.tutorialButton_y = 715
	(self.tutorialButton_size_x, self.tutorialButton_size_y) = self.tutorialButton.get_size()	
	
	self.level1 = Image.load_image('level-1.png')
	self.level1_x = 75
	self.level1_y = 625
	self.level1Disabled_x = self.level1_x
	self.level1Disabled_y = self.level1_y
	(self.level1_size_x, self.level1_size_y) = self.level1.get_size()
	
	self.level2 = Image.load_image('level-2.png')
	self.level2Disabled = Image.load_image('level-2-disabled.png')
	self.level2_x = 300
	self.level2_y = 625
	self.level2Disabled_x = self.level1_x
	self.level2Disabled_y = self.level1_y
	(self.level2_size_x, self.level2_size_y) = self.level2.get_size()
	
	self.level3 = Image.load_image('level-3.png')
	self.level3Disabled = Image.load_image('level-3-disabled.png')
	self.level3_x = 525
	self.level3_y = 625
	self.level3Disabled_x = self.level1_x
	self.level3Disabled_y = self.level1_y
	(self.level3_size_x, self.level3_size_y) = self.level3.get_size()
	
	self.levelSelect = 0
	
	self.enableLevel = 1
	
	self.howTo = HowTo()
	
	
	
    def draw(self,screen):
	
        runTitleScreen = 1
        while runTitleScreen:
	    mouse_x, mouse_y = pygame.mouse.get_pos()
	    LEFT_MOUSE_BUTTON = 1
            for event in pygame.event.get() :
		if event.type == pygame.QUIT: # If user clicked close (the X button)
		    pygame.quit()     
		    sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_MOUSE_BUTTON: # User clicked somewhere
		    x, y = event.pos
		    if x >= self.level1_x and x <= (self.level1_x + self.level1_size_x) and y <= (self.level1_y + self.level1_size_y) and y >= self.level1_y:
			self.levelSelect = 1
			runTitleScreen = 0
		    if (x >= self.level2_x and x <= (self.level2_x + self.level2_size_x) and y <= (self.level2_y + self.level2_size_y) and y >= self.level2_y) and self.enableLevel >= 2:
			self.levelSelect = 2
			runTitleScreen = 0	
		    if (x >= self.level3_x and x <= (self.level3_x + self.level3_size_x) and y <= (self.level3_y + self.level3_size_y) and y >= self.level3_y) and self.enableLevel == 3:
			self.levelSelect = 3
			runTitleScreen = 0
		    if (x >= self.tutorialButton_x and x <= (self.tutorialButton_x + self.tutorialButton_size_x) and y <= (self.tutorialButton_y + self.tutorialButton_size_y) and y >= self.tutorialButton_y):
			self.howTo.draw(screen)		    

	    screen.fill((0,0,0))
	    
	    screen.blit(self.title_screen_image, self.image_dimensions)
	    screen.blit(self.tomato_image, (self.tomato.x, self.tomato.y))
	    screen.blit(self.tomato_image2, (self.tomato2.x, self.tomato2.y))
	    screen.blit(self.tomato_image3, (self.tomato3.x, self.tomato3.y))
	    screen.blit(self.tomato_image4, (self.tomato4.x, self.tomato4.y))
	    screen.blit(self.tomato_image5, (self.tomato5.x, self.tomato5.y))
	    screen.blit(self.tomato_image6, (self.tomato6.x, self.tomato6.y))
	    screen.blit(self.tutorialButton, (self.tutorialButton_x, self.tutorialButton_y))
	    if (mouse_x >= self.tutorialButton_x and mouse_x <= (self.tutorialButton_x + self.tutorialButton_size_x) and mouse_y <= (self.tutorialButton_y + self.tutorialButton_size_y) and mouse_y >= self.tutorialButton_y):  
		screen.blit(self.outLine, (self.tutorialButton_x, self.tutorialButton_y))
	    
	    if self.enableLevel == 1:		
		screen.blit(self.level1, (self.level1_x, self.level1_y))
		screen.blit(self.level2Disabled, (self.level2_x, self.level2_y))
		screen.blit(self.level3Disabled, (self.level3_x, self.level3_y))
		if mouse_x >= self.level1_x and mouse_x <= (self.level1_x + self.level1_size_x) and mouse_y <= (self.level1_y + self.level1_size_y) and mouse_y >= self.level1_y:
		    screen.blit(self.outLine, (self.level1_x, self.level1_y))		
	    elif self.enableLevel == 2:
		screen.blit(self.level1, (self.level1_x, self.level1_y))
		screen.blit(self.level2, (self.level2_x, self.level2_y))
		screen.blit(self.level3Disabled, (self.level3_x, self.level3_y))
		if mouse_x >= self.level1_x and mouse_x <= (self.level1_x + self.level1_size_x) and mouse_y <= (self.level1_y + self.level1_size_y) and mouse_y >= self.level1_y:
		    screen.blit(self.outLine, (self.level1_x, self.level1_y))
		if mouse_x >= self.level2_x and mouse_x <= (self.level2_x + self.level2_size_x) and mouse_y <= (self.level2_y + self.level2_size_y) and mouse_y >= self.level2_y:
		    screen.blit(self.outLine, (self.level2_x, self.level2_y))		
	    elif self.enableLevel == 3:
		screen.blit(self.level1, (self.level1_x, self.level1_y))
		screen.blit(self.level2, (self.level2_x, self.level2_y))		
		screen.blit(self.level3, (self.level3_x, self.level3_y))
		if mouse_x >= self.level1_x and mouse_x <= (self.level1_x + self.level1_size_x) and mouse_y <= (self.level1_y + self.level1_size_y) and mouse_y >= self.level1_y:
		    screen.blit(self.outLine, (self.level1_x, self.level1_y))
		if mouse_x >= self.level2_x and mouse_x <= (self.level2_x + self.level2_size_x) and mouse_y <= (self.level2_y + self.level2_size_y) and mouse_y >= self.level2_y:
		    screen.blit(self.outLine, (self.level2_x, self.level2_y))
		if mouse_x >= self.level3_x and mouse_x <= (self.level3_x + self.level3_size_x) and mouse_y <= (self.level3_y + self.level3_size_y) and mouse_y >= self.level3_y:
		    screen.blit(self.outLine, (self.level3_x, self.level3_y))		    
	    

	    self.tomato.bouncey()
	    self.tomato2.bouncey()
	    self.tomato3.bouncey()
	    self.tomato4.bouncey()
	    self.tomato5.bouncey()
	    self.tomato6.bouncey()
	    
	    pygame.display.flip()

class bounce(object):
    def __init__(self, x, y):
	self.x = x
	self.y = y
	self.speed = random.random() * 3
	self.mainX = 0
	self.maxY = random.randrange(50,100)
	self.lock = True
	
    def bouncey(self):
	if self.mainX < self.maxY and self.mainX >= 0:
	    self.y += self.speed
	    self.mainX += self.speed
	    self.lock = True
	else:
	    if self.lock:
		self.lock = False
		self.mainX = -self.maxY
	    if self.mainX >= -self.maxY and self.mainX < 0:
		self.y -= self.speed
		self.mainX += self.speed