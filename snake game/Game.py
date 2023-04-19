import pygame, random, os
from objects import Snake_Head, Enemy_Head, Mousy


class gaem():
    def __init__(self):
        #pygame
        pygame.init()                                                                                                       #init pygame shish
        self.events = pygame.event.get()                                                                                    #check for events

        #tile system
        self.tile_size = 50                                                                                                 #set tile size for a grid
        self.tile_number = 10                                                                                               #set number of tiles and screen size
        
        #display
        self.screen_width, self.screen_height = self.tile_size * self.tile_number , self.tile_size  *self.tile_number       #define screen width and height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))                                      #initiate screen
        pygame.display.set_caption("fuggin SCHLONG gäem by Maggus")                                                         #make funny caption


        #time
        self.framerate = 60                                                                                                 #make game work on fps
        self.clock = pygame.time.Clock()
        



        #init objects
        self.initialize()                                                                                                   #initialize objects from initialize method now


        #run game
        self.running = True                                                                                                 #set the true for the main game loop
        self.run()                                                                                                          #run game main loop

        


    def initialize(self):
        
  
 
        #init game objects
        self.SnakeyHead = Snake_Head(self.tile_size * random.randint(0,self.tile_number - 1), self.tile_size * random.randint(0,self.tile_number - 1))      #initiate player
        self.Mousy = Mousy(self.tile_size * random.randint(0,self.tile_number - 1), self.tile_size * random.randint(0,self.tile_number - 1))                #initiate mouse
        

        #init score variable
        self.score = 0


        #init sprite groups
        self.SnakeHeadGroup = pygame.sprite.Group()         #create sprite group
        self.SnakeHeadGroup.add(self.SnakeyHead)            #add player to sprite group
        
        self.EnemiesGroup = pygame.sprite.Group()           #created sprite group here, add enemies later
        
        self.MousyGroup = pygame.sprite.Group()             #same stuff......
        self.MousyGroup.add(self.Mousy)

        
        
        #bg_color
        self.color = (0, 0, 0)                              #all this shit not needed, makes background fade colour yah
        self.r = random.randint(1,254)
        self.g = random.randint(1,254)
        self.b = random.randint(1,254)
        self.adder_r = 1
        self.adder_g = 1
        self.adder_b = 1
    
    
    def render(self):                               #update runs every tick in game loop to draw everything
        
        #background
        self.screen.fill((self.color))
        
        #draw elements
        self.SnakeHeadGroup.draw(self.screen)
        self.MousyGroup.draw(self.screen)
        self.EnemiesGroup.draw(self.screen)
        
        #update display
        pygame.display.update()

    def update(self):                               #update runs also every tick in the game loop so here we check for stuff happenin
        

        self.events = pygame.event.get()            #events like closing game 
        
        #color change                               # more stuff nobody needs, basically let the rgb values go up and down until they reach max or min
        if self.r == 254:
            self.adder_r = -0.5
        if self.r == 1:
            self.adder_r = 0.5
        self.r += self.adder_r
        
        if self.g == 254:
            self.adder_g = -0.5
        if self.g == 1:
            self.adder_g = 0.5
        self.g += self.adder_g
        
        if self.b == 254:
            self.adder_b = -0.5
        if self.b == 1:
            self.adder_b = 0.5
        self.b += self.adder_b
        
        self.color = (int(self.r), (self.g), (self.b))


        
        
        
        #make snake come from other side when leave backyard
        if self.SnakeyHead.rect.x < 0:                                                          #if players x coordinate <= 0 he left screen on the left side, so we put him on right side
            self.SnakeyHead.rect.x = self.tile_size * (self.tile_number - 1)                    #looks like he teleports to the right side
        
        if self.SnakeyHead.rect.x > self.tile_size * (self.tile_number - 1):                    #same stuff other axis/side/solar system/galaxy/dimension/....
            self.SnakeyHead.rect.x = 0
        
        if self.SnakeyHead.rect.y < 0:
            self.SnakeyHead.rect.y = self.tile_size * (self.tile_number - 1)                    #same stuff other axis/side/solar system/galaxy/dimension/....

        if self.SnakeyHead.rect.y > self.tile_size * (self.tile_number - 1):                    #same stuff other axis/side/solar system/galaxy/dimension/....
            self.SnakeyHead.rect.y = 0
        
        
        for Enemy in self.EnemiesGroup:                                                         #same stuff for all enemies 
            if Enemy.rect.x < 0:
                Enemy.rect.x = self.tile_size * (self.tile_number - 1)
        
            if Enemy.rect.x > self.tile_size * (self.tile_number - 1):
                Enemy.rect.x = 0
        
            if Enemy.rect.y < 0:
                Enemy.rect.y = self.tile_size * (self.tile_number - 1)

            if Enemy.rect.y > self.tile_size * (self.tile_number - 1):
                Enemy.rect.y = 0
        
        
        #give illusion that mouse change spot but it just go zoom new coordinate teleporationè
        
        if self.SnakeyHead.rect.colliderect(self.Mousy.rect):
            self.Mousy.rect.x = self.tile_size * random.randint(0,self.tile_number - 1)
            self.Mousy.rect.y = self.tile_size * random.randint(0,self.tile_number - 1)
            self.score += 1

        
        #introducing DIFFICULTY and dying

        if self.score == 10:    
            self.EnemiesGroup.add(Enemy_Head(self.tile_size * random.randint(0,self.tile_number - 1), self.tile_size * random.randint(0,self.tile_number - 1)))
            self.score = 0
        
        #^^^ at score 10 we add one enemy and reset score to start counting again
        
        
        
        
        for Enemy in self.EnemiesGroup:                               #check collision between player and enemies, if collision game closes (too lazy to do fancy death screen an stuff)
            if Enemy.rect.colliderect(self.SnakeyHead.rect):
                self.running = False

        
        
        self.SnakeHeadGroup.update()                                  #update all the sprites in sprite group --> here its only the player
        self.EnemiesGroup.update()                                    #update all the sprites in sprite group --> here its the enemies 
        
        
        

    
    def handleEvents(self):
        for event in self.events:
            if event.type == pygame.QUIT:                             #if u press red cross in corner the game closes
                self.running = False
   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:                      #if u press escape the game closes
                    self.running = False
                    
    
    def run(self):                                                    #call run --> initiate zu stuffle yousa needs
        while self.running:                                           #while the main loop is running do the following:
            self.update()                                             #method update --> execute all the code in update()
            self.handleEvents()                                       #same stuff other axis/side/solar system/galaxy/dimension/....
            self.render()                                             #same stuff other axis/side/solar system/galaxy/dimension/....
            self.clock.tick(self.framerate)                           #click clack tock on clock gib gaem time
            os.system("cls")                                          #make terminal look pretty but i dont print anything rn anyways soooooooooooooooooos
            
gaem()                                                                #call the class gaem and all the shit above starts playing

#it doesnt need to be a class and everything could have been way easier but i copied shit from another project and was too lazy to change everything soooooooooooooooooooooo
#I rather took 3x as long coding this shit cause i had no idea what im doing where i am who i am why are you idk? are you? are we? who is? what is?