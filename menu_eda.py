import images
import pygame
class Menu_eda:
    def __init__(self,game):
        self.kartinka = images.zagruzit_kart("images/menu/menu_page.png",[900,550])
        self.game = game
        
    def draw (self,okno):
        okno.blit(self.game.background,[0,0])
        okno.blit(self.kartinka,[0,0])
        pygame.display.flip()
    def event (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.b =   -10000000000000000
                