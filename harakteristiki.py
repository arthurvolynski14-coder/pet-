import pygame as pg
import pygame.freetype

class Harakter:
    def __init__(self,kartinka,znachenie,kardinati):
        self.pisatel = pygame.freetype.Font(None,25)
        self.kartinka = kartinka
        self.znachenie = znachenie
        self.pramougolnik = pg.Rect(kardinati,self.kartinka.get_size())

    def draw (self,okno):
        okno.blit(self.kartinka,self.pramougolnik)
        self.pisatel.render_to(okno,[self.pramougolnik.x+100,self.pramougolnik.y + 40],str(self.znachenie))