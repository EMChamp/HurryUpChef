import pygame

# static variables
FPS = 60
INTERVAL = 6000
SIZE = (800, 800)
POSITION = (0, 0)
COLOR = (255, 255, 255) #(250, 174, 122)
UPDATE_PLAYFIELD = pygame.USEREVENT+1
COUNTDOWNPLAY = pygame.USEREVENT+2
CONGRATS = pygame.USEREVENT+3
COMPLETE = pygame.USEREVENT+4
COUNTDOWNPLAY_INTERVAL = 1000
CONGRATS_INTERVAL = 6000
COMPLETE_INTERVAL = 10000

# NEED TO MOVE THESE INTO OWN CLASSES
SCORE_X, SCORE_Y = 624, 199
TIME_X, TIME_Y = 100, 171
CHEF_X, CHEF_Y = 16, 402

# static variables
COLS, ROWS = 6, 13
OFFSET_X, OFFSET_Y = 313, 158
GRID_WIDTH, GRID_HEIGHT = 50, 50

# static variables
INGREDIENT_SIZE = 5
INGRED_1, INGRED_2, INGRED_3, INGRED_4, INGRED_5 = xrange(INGREDIENT_SIZE)

# title screen
TITLE_SCREEN = "start.png"
PAUSE_SCREEN = "pause2.png"
GAME_OVER_SCREEN = "game_over_screen.png"
GAME_RESTART_BUTTON = "game_restart_button.png"
GAME_EXIT_BUTTON = "game_exit_button.png"

# screen stats
BLACK = (0, 0, 0)
MAGENTA = (218, 13, 124)
SCOREBLUE = (0, 86, 228)

#Game Background Music
LEVEL1 = "yoshi world.ogg"
LEVEL2 = "level2.ogg"
LEVEL3 = "level3.ogg"

#match scores
MATCHTHREE = 5  #default 5
MATCHFOUR = 8  #default 8
MATCHFIVE = 15  #default 15
MATCHMORE = 25  #default 25