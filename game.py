"""
 Hurry Up Chef
 Developed by Team Super Group
"""
import os, sys, pygame
from playfield import *
from sound import *
from title_screen import *
from pause_screen import *
from game_over_screen import *
from screen_stats import *
from const import *
from level import *

timeTracker = 0

# Game class to run() the game
class Game(object):
    
    # initialize PyGame
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1' # center display
        pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
        pygame.init() # initialize all imported pygame modules
        self.screen = pygame.display.set_mode(SIZE) # initialize a window or screen for display
        pygame.display.set_caption("Hurry Up Chef") # set the current window caption
        pygame.display.set_icon(Image.load_image('icon.png')) # change the system image for the display window
        self.introMusic = pygame.mixer.Sound(os.path.join('sound', "Boot.ogg"))
        self.playIntro()
        #pygame.mouse.set_visible(False) # hide the mouse cursor
        pygame.key.set_repeat(20,120) # generate multiple KEYDOWN events from keys held down
        self.clock = pygame.time.Clock() # create an object to help track time
         # load playfield
        self.init(1) # initialize the game
        
    # initialize the game
    def init(self, level):
        self.SCORE = Image.load_image('score.png') # load score board image
        self.TIME = Image.load_image('time.png') # load time board image
        self.CHEF = Image.load_image('chef.png') # load chef image
        self.titleMusic = pygame.mixer.Sound(os.path.join('sound', "title.ogg"))

        
        self.game_over = False
        self.game_quit = False
	self.speedOneLock = False
	self.speedTwoLock = False
	self.speedThreeLock = False	
	self.speedFourLock = False
	self.speedFiveLock = False	
        
        self.titleMusic.play(-1)
        # setup title screen
        self.title_screen = Title_screen(TITLE_SCREEN)
        self.title_screen.enableLevel = level
        # setup pause screen
        self.pause_screen = Pause_screen(PAUSE_SCREEN)
        
        # setup game over screen
        
        self.title_screen.draw(self.screen)
        
        self.playfield = Playfield(self.title_screen.levelSelect)
                        
        #selects background image
        if self.playfield.level == 1:
            self.BACKGROUND = Image.load_image('background1.png') # load background image
            self.OVERLAY = Image.load_image('background_overlay1.png') # load background overlay image     
        elif self.playfield.level == 2:
            self.BACKGROUND = Image.load_image('background2.png') # load background image
            self.OVERLAY = Image.load_image('background_overlay2.png') # load background overlay image
        elif self.playfield.level == 3:
            self.BACKGROUND = Image.load_image('background3.png') # load background image
            self.OVERLAY = Image.load_image('background_overlay3.png') # load background overlay image 
            
        self.sound = Sound(self.playfield.level)        
        
        if self.playfield.level == 1:
            self.LEVEL = Image.load_image('story1.jpg')
            flag = True
            while flag:
                self.screen.blit(self.LEVEL, POSITION)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        flag = False
        elif self.playfield.level == 2:
            self.LEVEL = Image.load_image('story2.jpg')
            flag = True
            while flag:
                self.screen.blit(self.LEVEL, POSITION)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        flag = False
        elif self.playfield.level == 3:
            self.LEVEL = Image.load_image('story3.jpg')
            flag = True
            while flag:
                self.screen.blit(self.LEVEL, POSITION)
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        flag = False
        
        self.titleMusic.stop()
        self.game_over_screen = Game_over_screen(GAME_OVER_SCREEN, GAME_RESTART_BUTTON, GAME_EXIT_BUTTON)
                    
        self.countDownPlay()
        
        #selects background music in accordance with level select
        if self.playfield.level == 1:
            pygame.mixer.music.load(os.path.join('sound', LEVEL1))
            pygame.mixer.music.play(-1) #start the main background music
        elif self.playfield.level == 2:
            pygame.mixer.music.load(os.path.join('sound', LEVEL2))
            pygame.mixer.music.play(-1) #start the main background music 
        elif self.playfield.level == 3:
            pygame.mixer.music.load(os.path.join('sound', LEVEL3))
            pygame.mixer.music.play(-1) #start the main background music                
        pygame.time.set_timer(UPDATE_PLAYFIELD, INTERVAL) # call UPDATE_PLAYFIELD event every 5 seconds
         
    # quit the game
    def quit(self):
        self.game_over = True
        self.game_quit = True
        
    def countDownPlay(self):
        pygame.time.set_timer(COUNTDOWNPLAY, COUNTDOWNPLAY_INTERVAL)
        pygame.display.flip()
        counter = 0
        self.sound.countDown.play()
        while 1:
            self.screen.fill(COLOR) # clear the screen
            self.screen.blit(self.BACKGROUND, POSITION) # draw background
            self.playfield.ingredient_group.draw(self.screen)
            self.screen.blit(self.OVERLAY, POSITION) # draw background_overlay
            self.playfield.cursor_group.draw(self.screen) # draw cursor
            self.screen.blit(self.SCORE, (SCORE_X, SCORE_Y)) # draw score board
            self.screen.blit(self.TIME, (TIME_X, TIME_Y)) # draw time board
            self.screen.blit(self.CHEF, (CHEF_X, CHEF_Y)) # draw chef

            for event in pygame.event.get():
                if event.type == COUNTDOWNPLAY:
                    if counter == 0:
                        self.sound.countDown.play()
                        counter += 1
                    elif counter == 1:
                        self.sound.countDown.play()
                        counter += 1                     
                    elif counter == 2:
                        counter += 1
                    elif counter == 3:
                        break
                    
            if counter == 0:
                self.screen.blit(self.title_screen.countDownThree, (420,400))
            elif counter == 1:
                self.screen.blit(self.title_screen.countDownTwo, (420,400))
            elif counter == 2:
                self.screen.blit(self.title_screen.countDownOne, (420,400)) 
                
            pygame.display.flip() # display everything in the screen     
            self.clock.tick(FPS)            
            if counter == 3:
                self.sound.countDownComplete.play()
                break
                    
                    
    def playIntro(self):
        movie = pygame.movie.Movie(os.path.join('image', "introtest.mpg"))
        movie_resolution = movie.get_size ()
        pygame.display.set_mode (movie_resolution)
        movie.set_display (pygame.display.get_surface ())
        self.introMusic.play()
        movie.play ()
        while movie.get_busy():
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # If user clicked close (the X button)
                    pygame.quit()
                    sys.exit()
        
    def check_game_over(self): # check if game over
        if not self.playfield.top_row_empty():
            self.game_over = True
        
    # run the game
    def run(self):
        global timeTracker
        self.congrats = Image.load_image('congratulations.png')
        levelThree = False
        PLAYING = False
        gameOver = False
        testCount = 0
	
        while not self.game_quit:
            # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.sound.criticalMusic.stop()
                    pygame.mixer.music.stop()
                    self.init()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    self.playfield.cursor.move_up()
                    self.sound.moveSound.play()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    self.playfield.cursor.move_down()
                    self.sound.moveSound.play()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    self.playfield.cursor.move_left()
                    self.sound.moveSound.play()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    self.playfield.cursor.move_right()
                    self.sound.moveSound.play()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pygame.key.set_repeat(20,120) # prevent multiple KEYDOWN event for K_SPACE
                    if not self.game_over:
                        self.playfield.swap()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    self.playfield.print_dictionary()
                elif event.type == UPDATE_PLAYFIELD or (event.type == pygame.KEYDOWN and event.key == pygame.K_w):
                    self.check_game_over()
                    if self.game_over:
                        self.playfield.inanimate()
                        gameOver = True
                        testCount += 1
                    elif not self.playfield.animating:
                        self.playfield.cursor.move_up()
                        self.playfield.move_up()
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not self.game_over:
                    self.sound.pauseSound.play()
                    self.pause_screen.draw(self.screen)
                    
            # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
            
            
            
            # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
            self.playfield.tick.update(pygame.time.get_ticks())
            self.playfield.ingredient_group.update(pygame.time.get_ticks())
            self.playfield.cursor_group.update(pygame.time.get_ticks())
            
            if self.playfield.critical_point():
                self.sound.criticalMusic.stop()
                pygame.mixer.music.unpause()
                PLAYING = False
            else:
                if PLAYING == False:
                    PLAYING = True
                    self.sound.criticalMusic.play(loops = -1)
                    pygame.mixer.music.pause() 
            # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
            
            
                        
            
            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            self.screen.fill(COLOR) # clear the screen
            self.screen.blit(self.BACKGROUND, POSITION) # draw background
            self.playfield.ingredient_group.draw(self.screen)
            self.screen.blit(self.OVERLAY, POSITION) # draw background_overlay
            self.playfield.cursor_group.draw(self.screen) # draw cursor
            self.screen.blit(self.SCORE, (SCORE_X, SCORE_Y)) # draw score board
            self.screen.blit(self.TIME, (TIME_X, TIME_Y)) # draw time board
            self.screen.blit(self.CHEF, (CHEF_X, CHEF_Y)) # draw chef
            self.playfield.screen_stats.run(self.screen)
            
            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
           
            pygame.display.flip() # display everything in the screen
            self.clock.tick(FPS) # limit the framerate
            #self.clock.tick_busy_loop(FPS) # limit the framerate
            
            
            #level complete
            if self.playfield.level == 1:
                if self.playfield.screen_stats.scoreCount > 150:
                    timeTracker += self.playfield.screen_stats.totalSeconds
                    flag = True
                    if levelThree:
                        self.sound.criticalMusic.stop()
                        pygame.mixer.music.stop()
                        self.sound.congrats.play()
                        pygame.time.set_timer(CONGRATS, CONGRATS_INTERVAL)
                        while flag:
                            for event in pygame.event.get():
                                if event.type == CONGRATS:
                                    flag = False
                            self.screen.blit(self.congrats, (265, 300))
                            pygame.display.flip()
                        self.sound.congrats.stop()
                        self.init(3)
                    else:
                        self.sound.criticalMusic.stop()
                        pygame.mixer.music.stop()
                        self.sound.congrats.play()
                        pygame.time.set_timer(CONGRATS, CONGRATS_INTERVAL)
                        while flag:
                            for event in pygame.event.get():
                                if event.type == CONGRATS:
                                    flag = False  
                            self.screen.blit(self.congrats, (265, 300))
                            pygame.display.flip()                            
                        self.sound.congrats.stop()
                        self.init(2)                        
                        
            elif self.playfield.level == 2:
		
		if self.playfield.screen_stats.scoreCount > 50 and self.playfield.screen_stats.scoreCount < 100:
		    if self.speedOneLock == False:
			pygame.time.set_timer(UPDATE_PLAYFIELD, 5000)
			self.playfield.screen_stats.speedCount = 1
			self.speedOneLock = True
		elif self.playfield.screen_stats.scoreCount > 100 and self.playfield.screen_stats.scoreCount < 150:
		    if self.speedTwoLock == False:
			pygame.time.set_timer(UPDATE_PLAYFIELD, 4000)
			self.playfield.screen_stats.speedCount = 2
			self.speedTwoLock = True
		elif self.playfield.screen_stats.scoreCount > 150 and self.playfield.screen_stats.scoreCount < 200:
		    if self.speedThreeLock == False:
			pygame.time.set_timer(UPDATE_PLAYFIELD, 3000)
			self.playfield.screen_stats.speedCount = 3
			self.speedThreeLock = True			
		
                if self.playfield.screen_stats.scoreCount > 200:
                    timeTracker += self.playfield.screen_stats.totalSeconds
                    flag = True
                    levelThree = True
                    self.sound.criticalMusic.stop()
                    pygame.mixer.music.stop()
                    self.sound.congrats.play()
                    pygame.time.set_timer(CONGRATS, CONGRATS_INTERVAL)
                    while flag:
                        for event in pygame.event.get():
                            if event.type == CONGRATS:
                                flag = False
                        self.screen.blit(self.congrats, (265, 300))
                        pygame.display.flip()                        
                    self.sound.congrats.stop()
                    self.init(3)    
                    
            elif self.playfield.level == 3:
		
		if self.playfield.screen_stats.scoreCount > 50 and self.playfield.screen_stats.scoreCount < 100:
		    if self.speedOneLock == False:
			pygame.time.set_timer(UPDATE_PLAYFIELD, 5000)
			self.playfield.screen_stats.speedCount = 1
			self.speedOneLock = True
		elif self.playfield.screen_stats.scoreCount > 100 and self.playfield.screen_stats.scoreCount < 150:
		    if self.speedTwoLock == False:
			pygame.time.set_timer(UPDATE_PLAYFIELD, 4000)
			self.playfield.screen_stats.speedCount = 2
			self.speedTwoLock = True
		elif self.playfield.screen_stats.scoreCount > 150 and self.playfield.screen_stats.scoreCount < 200:
		    if self.speedThreeLock == False:
			pygame.time.set_timer(UPDATE_PLAYFIELD, 3000)
			self.playfield.screen_stats.speedCount = 3
			self.speedThreeLock = True
		elif self.playfield.screen_stats.scoreCount > 200 and self.playfield.screen_stats.scoreCount < 250:
		    if self.speedFourLock == False:
			pygame.time.set_timer(UPDATE_PLAYFIELD, 2000)
			self.playfield.screen_stats.speedCount = 4
			self.speedFourLock = True	
		elif self.playfield.screen_stats.scoreCount > 250 and self.playfield.screen_stats.scoreCount < 300:
		    if self.speedFiveLock == False:
			pygame.time.set_timer(UPDATE_PLAYFIELD, 1500)
			self.playfield.screen_stats.speedCount = 5
			self.speedFiveLock = True		
		
		if self.playfield.screen_stats.scoreCount > 300:
		    timeTracker += self.playfield.screen_stats.totalSeconds
		    flag = True
		    levelThree = True
		    self.sound.criticalMusic.stop()
		    pygame.mixer.music.stop()
		    self.sound.congrats.play()
		    pygame.time.set_timer(CONGRATS, CONGRATS_INTERVAL)
		    while flag:
			for event in pygame.event.get():
			    if event.type == CONGRATS:
				flag = False
			self.screen.blit(self.congrats, (265, 300))
			pygame.display.flip()
		    self.sound.congrats.stop()
			
		    #game complete
		    self.sound.completeMusic.play(-1)
		    completeFont = pygame.font.Font(os.path.join('font', 'Gretoon.ttf'), 45)
		    completeImage = pygame.image.load(os.path.join('image', "complete.png"))
		    timeTrackerText = completeFont.render("%0d" % timeTracker, True, BLACK)
		    run = 1
		    pygame.time.set_timer(COMPLETE, COMPLETE_INTERVAL)
		    while run:
			for event in pygame.event.get() :
			    if event.type == pygame.QUIT: # If user clicked close (the X button)
				pygame.quit()     
				sys.exit()
			    elif event.type == COMPLETE:
				run = 0
				
			self.screen.blit(completeImage, POSITION)
			self.screen.blit(timeTrackerText, (350, 265))
			pygame.display.flip()
		    #game complete
			
		    #credits roll    
		    completeMovie = pygame.movie.Movie(os.path.join('image', "credits.mpg"))
		    movie_resolution = completeMovie.get_size ()
		    pygame.display.set_mode (movie_resolution)
		    completeMovie.set_display (pygame.display.get_surface ())
		    completeMovie.play ()
		    while completeMovie.get_busy():
			for event in pygame.event.get():
			    if event.type == pygame.QUIT: # If user clicked close (the X button)
				pygame.quit()
				sys.exit()			
		    pygame.quit()     
		    sys.exit()	
		    #credits roll
			
                           
            #level complete
                        
                        
            #game over
            if gameOver:
                testCount += 1
                if testCount == 40:
                    timeTracker += self.playfield.screen_stats.totalSeconds
                    print timeTracker
                    gameOver = False
                    testCount = 0
                    self.sound.criticalMusic.stop()
                    self.game_over_screen.draw(self.screen, self.title_screen.enableLevel)
                    if self.title_screen.enableLevel == 1:
                        pygame.mixer.music.stop()
                        self.sound.criticalMusic.stop()
                        self.init(1)
                    elif self.title_screen.enableLevel == 2:
                        pygame.mixer.music.stop()
                        self.sound.criticalMusic.stop()
                        self.init(2)
                    elif self.title_screen.enableLevel == 3:
                        pygame.mixer.music.stop()
                        self.sound.criticalMusic.stop()
                        self.init(3)
            #game over
                
            
        pygame.quit() # quit the game
        sys.exit() # exit the system

# run the game
if __name__ == "__main__":
    Game().run()
