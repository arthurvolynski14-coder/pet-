import pygame
import images

class Menu_ojedja:
    def __init__ (self,game):
        self.game = game
        self.kartinka = images.zagruzit_kart("images/menu/menu_page.png",[900,550])

    def draw(self,okno):
        okno.blit(self.game.background,[0,0])
        okno.blit(self.kartinka,[0,0])

        pygame.display.flip()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.b = -1929392193921939219


