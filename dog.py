import pygame as pg
class Doggy:

    def __init__(self):
        
        self.kartinka = pg.image.load("images/dog.png")
        self.kartinka = pg.transform.scale(self.kartinka,[255,100])

        self.pramougol = pg.Rect([350,225],self.kartinka.get_size())
    def draw (self,okno):
        okno.blit(self.kartinka,self.pramougol)
        