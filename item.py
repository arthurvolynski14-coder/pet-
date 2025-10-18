import pygame as pg
class Items:
    def __init__ (self,kartina,cena):
        self.kartina = kartina
        self.cena = cena
        self.pramougolnik = pg.Rect([500,200],self.kartina.get_size())
    def draw(self,okno):
        okno.blit(self.kartina,self.pramougolnik)
