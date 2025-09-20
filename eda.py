import pygame as pg
class Eda:
    def __init__(self,kartinka,cena,):
        self.kartinka = kartinka
        self.cena = cena
        self.pramougolnik = pg.Rect([500,200],self.kartinka.get_size())

    def draw (self,okno):
        okno.blit(self.kartinka,self.pramougolnik)
        