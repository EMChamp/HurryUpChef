import pygame, os

from const import *

class ScreenStats(object):
    
    def __init__(self):
        self.font = pygame.font.Font(os.path.join('font', 'Gretoon.ttf'), 45) # create a new Font object from a file
        self.fontScore = pygame.font.Font(os.path.join('font', 'Gretoon.ttf'), 30)
        self.fontScoreCount = pygame.font.Font(os.path.join('font', 'Gretoon.ttf'), 42)
        
        self.timeText = self.font.render("Time:", True, MAGENTA)    
        self.scoreText = self.fontScore.render("Score:", True, SCOREBLUE)
        self.speedText = self.fontScore.render("Speed:", True, SCOREBLUE)
        self.levelText = self.fontScore.render("Level:", True, SCOREBLUE)
        
        self.framecount = 0
        self.scoreCount = 0
        self.speedCount = 0

        self.speedOneLock = False
        self.speedTwoLock = False
        self.speedThreeLock = False
        
        self.totalSeconds = 0
    def run(self, screen):
        
        #timer display
        screen.blit(self.timeText, [120, 175])
        self.totalSeconds = self.framecount // 60
        minutes = self.totalSeconds // 60
        seconds = self.totalSeconds % 60
        timer = self.font.render("%02d:%02d" % (minutes,seconds), True, BLACK)
        screen.blit(timer, [130, 225]) 
        self.framecount += 1
        
        screen.blit(self.scoreText, [635, 210])
        scoreBoard = self.fontScoreCount.render("%05d" % self.scoreCount, True, BLACK)
        screen.blit(scoreBoard, [630, 250])
        
        #changes speed of the game corresponding to the score
        #if self.scoreCount > 50 and self.scoreCount < 100:
            #if self.speedOneLock == False:
                #pygame.time.set_timer(UPDATE_PLAYFIELD, 3000)
                #self.speedCount = 1
                #self.speedOneLock = True
        #elif self.scoreCount > 100 and self.scoreCount < 150:
            #if self.speedTwoLock == False:
                #pygame.time.set_timer(UPDATE_PLAYFIELD, 2000)
                #self.speedCount = 2
                #self.speedTwoLock = True
        #elif self.scoreCount > 150 and self.scoreCount < 200:
            #if self.speedThreeLock == False:
                #pygame.time.set_timer(UPDATE_PLAYFIELD, 1000)
                #self.speedCount = 3
                #self.speedThreeLock = True      
            
        screen.blit(self.speedText, [635, 300])
        speedCountDisplay = self.fontScoreCount.render("%01d" % self.speedCount, True, BLACK) 
        screen.blit(speedCountDisplay, [690, 340])