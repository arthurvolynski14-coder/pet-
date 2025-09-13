import pygame.freetype
import pygame as pg
pg.init()
import images
pisatel = pygame.freetype.Font(None,20)
class Button:
    def __init__(self,name,size,pos):
        self.size = size
        self.kartinka = images.zagruzit_kart("images/button.png",self.size)
        self.pramougolnik = pg.Rect(pos,size)
        kartinka_pramougol = pisatel.render(name)
        self.kartinka_tex = kartinka_pramougol[0]
        self.tex_pramougol = kartinka_pramougol[1]
        self.tex_pramougol.center = self.pramougolnik.center
    def draw (self,okno):
        okno.blit(self.kartinka,self.pramougolnik)
        okno.blit(self.kartinka_tex,self.tex_pramougol)
    def click (self):
        self.kartinka = images.zagruzit_kart("images/button_clicked.png",self.size)
    def unclick(self):
        self.kartinka = images.zagruzit_kart("images/button.png",self.size)