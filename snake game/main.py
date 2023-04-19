# import sys, pygame

# from objects import Button
# from Game import gaem

# class Menu():
#     def __init__(self):
        
#         #pygame
#         pygame.init()
#         self.events = pygame.event.get()

#         #display
    
#         # self.infoObject = pygame.display.Info()
#         # self.screen = pygame.display.set_mode((self.infoObject.current_w, self.infoObject.current_h), pygame.FULLSCREEN)
#         # pygame.display.set_icon(pygame.image.load("assets/schlonge.png"))
        
        
        
#         self.screen_width, self.screen_height = 600, 600
#         self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
#         pygame.display.set_icon(pygame.image.load("assets/schlonge.png"))
        
        
#         #init objects
#         self.initialize()

#         #run game
#         self.running = True
#         self.run()



#     def initialize(self):
        
#         #init menu elements
#         self.playButton = Button((self.screen_width/2) - (256/2), 100, "assets/PlayBtn.png")
#         self.playButton.setResult(gaem)
        
#         #init sprite group
#         self.menu_elements = pygame.sprite.Group()
#         self.menu_elements.add(self.playButton)

        
    
#     def render(self):
        
#         #diplay resize after quit gaem
#         self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        
#         #background
#         self.screen.fill((120, 180, 180))

#         #render menu elements
#         self.menu_elements.draw(self.screen)
        
#         pygame.display.update()

#     def update(self):
#         self.events = pygame.event.get()

       
#     def handleEvents(self):
#         for event in self.events:
#             if event.type == pygame.QUIT:
#                 self.running = False
   
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     self.running = False
    
#         for Button in self.menu_elements:
#             if Button.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == True:
#                 Button.getResult()

    
    
    
    
    
#     def run(self):
#         while self.running:
#             self.update()
#             self.handleEvents()
#             self.render()
#         pygame.quit()
#         sys.exit()


# Menu()
