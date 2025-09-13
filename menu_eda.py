import images
import pygame
class Menu_eda:
    def __init__(self):
        self.kartinka = images.zagruzit_kart("images/menu/menu_page.png",[900,550])
    def draw (self,okno):
        okno.blit(self.kartinka,[0,0])
        pygame.display.flip()