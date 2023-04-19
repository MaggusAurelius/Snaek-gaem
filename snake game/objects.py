import pygame, random
from pygame.sprite import Sprite

class Snake_Head(Sprite):                                            # make a class for snackey head
    def __init__(self, x, y):
        super().__init__()                                           # "super().__init__()" inherit from Sprite and init its methods an shit


        #Heads
        self.HeadUp = pygame.image.load("assets/HeadUp.png").convert_alpha()                # loading images for different directions from "asset" folder
        self.HeadDown = pygame.image.load("assets/HeadDown.png").convert_alpha()
        self.HeadLeft = pygame.image.load("assets/HeadLeft.png").convert_alpha()
        self.HeadRight = pygame.image.load("assets/HeadRight.png").convert_alpha()


        # load image for head
        self.image = (self.HeadUp)                                   # set a starting image for snakey sprite
        self.rect = self.image.get_rect()                            # get a rect for the sprite from the picture                             


        # basic shiesh for pos
        self.rect.x = x                                              # init x coordinate
        self.rect.y = y                                              # you know how it works
        self.HeadDir = None                                          # variable vor head dir
        self.lastDir = None                                          # at the beginning of game snake have no direction in life but its set after input

        self.TileSize = 50                                           # how much snake move when it move (tileSize = 50 like in gaem so snake stay in GITTER)
        self.MoveCounter = 0                                         # MoveCounter counts up so snack know when wiggle
        self.MoveCounterMax = 45                                     # basically set how fast snack move cause it move when counter === countermax



    def update(self):                                                         # method must be called "update" cuz thats how pygame sprites work
        
        
        # handle inputs and set direction accordingly
        if pygame.key.get_pressed()[pygame.K_a] and self.lastDir != "right":  # check the keyboard input and prevent moving back in the direction where you came from
            self.HeadDir = "left"                                             
                                                        
       
        if pygame.key.get_pressed()[pygame.K_d] and self.lastDir != "left":
            self.HeadDir = "right"
            
        if pygame.key.get_pressed()[pygame.K_w] and self.lastDir != "down":
            self.HeadDir = "up"
            
        
        if pygame.key.get_pressed()[pygame.K_s] and self.lastDir != "up":
            self.HeadDir = "down"
            

        #do actual moving: 
        if self.HeadDir == "left" and self.MoveCounter >= self.MoveCounterMax:      # check the direction and if counter is high enough
            self.rect.x -= self.TileSize                                            # set the coordinates
            self.image = self.HeadLeft                                              # set new image according to direction
            self.MoveCounter = 0                                                    # reset movecounter because it was over its max (bunch a bad shit happen if u dond)                                             
            self.lastDir = "left"                                                   # important to note lastDir after move, otherwise, if u have quick fingers u can move into yourself, no good
        else: 
            self.MoveCounter += 1                                                   # if movecounter isnt high enough to move the snake you add to it until u haben genuch
                                                                                    
        if self.HeadDir == "right" and self.MoveCounter >= self.MoveCounterMax:     # same shit for all the other directions
            self.rect.x += self.TileSize
            self.image = self.HeadRight
            self.MoveCounter = 0
            self.lastDir = "right"
        else: 
            self.MoveCounter += 1

        if self.HeadDir == "up" and self.MoveCounter >= self.MoveCounterMax:
            self.rect.y -= self.TileSize
            self.image = self.HeadUp
            self.MoveCounter = 0
            self.lastDir = "up"
        else: 
            self.MoveCounter += 1

        if self.HeadDir == "down" and self.MoveCounter >= self.MoveCounterMax:
            self.rect.y += self.TileSize
            self.image = self.HeadDown  
            self.MoveCounter = 0
            self.lastDir = "down"
        else: 
            self.MoveCounter += 1
        

class Enemy_Head(Sprite):                                            # make a class for snackey head
    def __init__(self, x, y):
        super().__init__()                                           # "super().__init__()" inherit from Sprite and init its methods an shit


        #Heads
        self.HeadUp = pygame.image.load("assets/HeadUpEnemy.png").convert_alpha()                # loading images for different directions from "asset" folder
        self.HeadDown = pygame.image.load("assets/HeadDownEnemy.png").convert_alpha()
        self.HeadLeft = pygame.image.load("assets/HeadLeftEnemy.png").convert_alpha()
        self.HeadRight = pygame.image.load("assets/HeadRightEnemy.png").convert_alpha()


        # load image for head
        self.image = (self.HeadUp)                                   # set a starting image for snakey sprite
        self.rect = self.image.get_rect()                            # get a rect for the sprite from the picture                             


        # basic shiesh for pos
        self.rect.x = x                                              # init x coordinate
        self.rect.y = y                                              # you know how it works
        self.HeadDir = None                                          # variable vor head dir
        self.lastDir = None                                          # at the beginning of game snake have no direction in life but its set after input

        self.TileSize = 50                                           # how much snake move when it move (tileSize = 50 like in gaem so snake stay in GITTER)
        self.MoveCounter = 0                                         # MoveCounter counts up so snack know when wiggle
        self.MoveCounterMax = 70                                     # basically set how fast snack move cause it move when counter === countermax

        
        self.Directions = [                                          # list to rahdomly choose a direction from
        "left",
        "right",
        "up",
        "down",
        ]
        

        self.ChaosCounter = 0                                        # counter to change direction after an intervall
        self.ChaosCounterMax = 60                                    # set after which time direction change lower number == more chaos
        


    def update(self):                                                # method must be called "update" cuz thats how pygame sprites work
        
        
        
        if self.ChaosCounter <= self.ChaosCounterMax:                # increase chaos counter
            self.ChaosCounter += 1
        
        if self.ChaosCounter == self.ChaosCounterMax:                # if chaos counter at max we pick a new direction

            self.ChaosCounter = 0
            
            self.DirPicker = self.Directions[random.randint(0,3)]
            
            if self.lastDir != "left" and self.DirPicker == "right":
                self.HeadDir = self.DirPicker

            if self.lastDir != "right" and self.DirPicker == "left":
                self.HeadDir = self.DirPicker
                
            
            if self.lastDir != "up" and self.DirPicker == "down":
                self.HeadDir = self.DirPicker
            
            if self.lastDir != "down" and self.DirPicker == "up":
                self.HeadDir = self.DirPicker
        
        #do actual moving: 
        if self.HeadDir == "left" and self.MoveCounter >= self.MoveCounterMax:      # check the direction and if counter is high enough
            self.rect.x -= self.TileSize                                            # set the coordinates
            self.image = self.HeadLeft                                              # set new image according to direction
            self.MoveCounter = 0                                                    # reset movecounter because it was over its max (bunch a bad shit happen if u dond)                                             
            self.lastDir = "left"                                                   # important to note lastDir after move, otherwise, if u have quick fingers u can move into yourself, no good
        else: 
            self.MoveCounter += 1                                                   # if movecounter isnt high enough to move the snake you add to it until u haben genuch
                                                                                    
        if self.HeadDir == "right" and self.MoveCounter >= self.MoveCounterMax:     # same shit for all the other directions
            self.rect.x += self.TileSize
            self.image = self.HeadRight
            self.MoveCounter = 0
            self.lastDir = "right"
        else: 
            self.MoveCounter += 1

        if self.HeadDir == "up" and self.MoveCounter >= self.MoveCounterMax:
            self.rect.y -= self.TileSize
            self.image = self.HeadUp
            self.MoveCounter = 0
            self.lastDir = "up"
        else: 
            self.MoveCounter += 1

        if self.HeadDir == "down" and self.MoveCounter >= self.MoveCounterMax:
            self.rect.y += self.TileSize
            self.image = self.HeadDown  
            self.MoveCounter = 0
            self.lastDir = "down"
        else: 
            self.MoveCounter += 1


class Mousy(Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.image = pygame.image.load("assets/mouse.png").convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y

