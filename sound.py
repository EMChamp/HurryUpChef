import pygame, os
from playfield import *

class Sound(object):
    def __init__(self, level):
        self.moveSound = pygame.mixer.Sound(os.path.join('sound', "move.wav"))
        
        #chooses critical music corresponding to the level selected
        if level == 1:
            self.criticalMusic = pygame.mixer.Sound(os.path.join('sound', "criticalLevel1.ogg"))
        elif level == 2:
            self.criticalMusic = pygame.mixer.Sound(os.path.join('sound', "criticalLevel2.ogg"))
        elif level == 3:
            self.criticalMusic = pygame.mixer.Sound(os.path.join('sound', "criticalLevel3.ogg"))  
            
        self.clearSound = pygame.mixer.Sound(os.path.join('sound', "clear.wav"))
        self.introMusic = pygame.mixer.Sound(os.path.join('sound', "Boot.ogg"))
        self.dropSound = pygame.mixer.Sound(os.path.join('sound', "drop.wav"))
        self.pauseSound = pygame.mixer.Sound(os.path.join('sound', "pause.wav"))
        self.countDown = pygame.mixer.Sound(os.path.join('sound', "countdown.wav"))
        self.congrats = pygame.mixer.Sound(os.path.join('sound', "congrats.ogg"))
        self.countDownComplete = pygame.mixer.Sound(os.path.join('sound', "countdown_complete.wav"))
        
        
        self.completeMusic = pygame.mixer.Sound(os.path.join('sound', "complete.ogg"))         
        